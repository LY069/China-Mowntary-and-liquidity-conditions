#!/usr/bin/env python3
"""
Sanity gate for the dataset. Run after any refresh, and in CI.

The refresh path pulls from endpoints that change their column names and
response shapes without warning. A silent mis-parse is far more dangerous than
a loud failure: it produces a plausible-looking index built on wrong numbers.
This script exists to make that failure loud.

It checks three things:

  1. STRUCTURE  — every series parses, dates are well-formed, sorted and
                  unique, and nothing is dated in the future.
  2. PLAUSIBILITY — each series sits inside a range it cannot leave without
                  something having gone wrong (a policy rate of 40% means the
                  units are wrong, not that the PBoC panicked).
  3. ANCHORS    — a handful of values that are matters of public record. If a
                  refresh changes one of these, the parse broke; the history
                  did not.

Exit code 0 = clean, 1 = failures. Warnings never fail the run.

    python3 scripts/validate_data.py
    python3 scripts/validate_data.py --strict    # warnings fail too
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# series id -> (low, high) bounds a correct value cannot fall outside
BOUNDS = {
    "m1_yoy": (-20, 45), "m2_yoy": (0, 35), "tsf_stock_yoy": (0, 40),
    "cpi_yoy": (-10, 30), "ppi_yoy": (-15, 30), "core_cpi_yoy": (-5, 15),
    "lpr_1y": (1.0, 8.0), "lpr_5y": (1.0, 9.0),
    "omo_7d": (0.5, 6.0), "mlf_1y": (1.0, 7.0),
    "dr007": (0.5, 12.0), "r007": (0.5, 20.0), "ncd_1y_aaa": (0.5, 8.0),
    "cgb_1y": (0.2, 6.0), "cgb_10y": (0.5, 7.0),
    "rrr_large": (4.0, 22.0), "rrr_small": (4.0, 20.0),
    "walr_general": (2.0, 10.0), "excess_reserve_ratio": (0.2, 8.0),
    "real_gdp_yoy": (-10, 20), "usdcny": (5.5, 8.5),   # managed-float era only
    "shibor_3m": (0.5, 10.0), "cnh_hibor_on": (0.0, 70.0),
}

# (series, date, expected, tolerance, why) — matters of public record
ANCHORS = [
    ("lpr_1y",    "2025-06", 3.00, 0.001, "1y LPR has been 3.00% since the May 2025 cut"),
    ("lpr_5y",    "2025-06", 3.50, 0.001, "5y LPR has been 3.50% since the May 2025 cut"),
    ("lpr_1y",    "2024-08", 3.35, 0.001, "1y LPR was 3.35% between the Jul and Oct 2024 cuts"),
    ("rrr_large", "2025-06", 9.00, 0.001, "large-bank RRR went to 9.00% effective 15 May 2025"),
    ("omo_7d",    "2025-06", 1.40, 0.001, "7-day policy rate cut to 1.40% on 8 May 2025"),
    ("omo_7d",    "2024-12", 1.50, 0.001, "7-day policy rate was 1.50% from Sep 2024"),
]

MONTH = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")
DAY = re.compile(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$")
QUARTER = re.compile(r"^\d{4}-Q[1-4]$")

fails: list[str] = []
warns: list[str] = []


def fail(msg): fails.append(msg); print(f"  FAIL  {msg}")
def warn(msg): warns.append(msg); print(f"  warn  {msg}")
def ok(msg):   print(f"  ok    {msg}")


def to_month(key: str) -> str:
    if QUARTER.match(key):
        y, q = key.split("-Q")
        return f"{y}-{int(q) * 3:02d}"
    return key[:7]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = ap.parse_args()

    today = date.today().isoformat()
    this_month = today[:7]

    # ---------------------------------------------------------- 1. structure
    print("STRUCTURE")
    seeds = {}
    for name in ("series.json", "analyst_supplied.json", "mirrors_round2.json"):
        p = ROOT / "data" / "seed" / name
        if not p.exists():
            if name != "series.json":
                print(f"  --    {name} not present (optional)")
                continue
            fail(f"{name} is missing")
            continue
        try:
            seeds[name] = json.loads(p.read_text(encoding="utf-8"))
            ok(f"{name} parses ({len(seeds[name].get('series', {}))} series)")
        except json.JSONDecodeError as e:
            fail(f"{name} is not valid JSON: {e}")

    for fname, doc in seeds.items():
        for sid, s in doc.get("series", {}).items():
            obs = s.get("observations", [])
            if not obs:
                warn(f"{fname}:{sid} has no observations")
                continue
            keys = [o[0] for o in obs]
            for k in keys:
                if not (MONTH.match(k) or DAY.match(k) or QUARTER.match(k)):
                    fail(f"{fname}:{sid} has a malformed date key {k!r}")
                    break
            if len(set(keys)) != len(keys):
                fail(f"{fname}:{sid} has duplicate dates")
            if keys != sorted(keys):
                fail(f"{fname}:{sid} observations are not sorted")
            future = [k for k in keys if to_month(k) > this_month]
            if future:
                fail(f"{fname}:{sid} has {len(future)} observation(s) dated in the "
                     f"future (e.g. {future[0]})")
            prov = s.get("provenance") or {}
            if not prov.get("source_url"):
                warn(f"{fname}:{sid} has no source_url")
            if prov.get("confidence") not in ("verified", "partial", "analyst-supplied", "suspect"):
                warn(f"{fname}:{sid} confidence is {prov.get('confidence')!r}")

    # ------------------------------------------------------- 2. plausibility
    print("\nPLAUSIBILITY")
    built = ROOT / "app" / "data.js"
    if not built.exists():
        fail("app/data.js not built — run scripts/build_app_data.py first")
        return report(args)
    raw = built.read_text(encoding="utf-8")
    payload = json.loads(raw[raw.index("{"):raw.rindex(";")])
    series = payload.get("series", {})
    ok(f"app/data.js parses ({len(series)} series)")

    # The seed files were checked for future dates above, but a bad forward-fill
    # or an off-by-one in the build can invent months that no seed contains, so
    # the built payload has to be checked on its own terms.
    for sid, s_ in series.items():
        future = [d for d, _ in s_.get("points", []) if d[:7] > this_month]
        if future:
            fail(f"built series {sid} has {len(future)} observation(s) dated after "
                 f"{this_month} (e.g. {future[0]}) — the build invented months")
    ok(f"no built series extends past {this_month}")

    checked = 0
    for sid, (lo, hi) in BOUNDS.items():
        pts = series.get(sid, {}).get("points")
        if not pts:
            continue
        checked += 1
        bad = [(d, v) for d, v in pts if v is not None and not (lo <= v <= hi)]
        if bad:
            fail(f"{sid}: {len(bad)} value(s) outside [{lo}, {hi}] — "
                 f"likely a units or column error, e.g. {bad[0]}")
    ok(f"range checks applied to {checked} series")

    # ------------------------------------------------------------ 3. anchors
    print("\nANCHORS (matters of public record)")
    for sid, when, expect, tol, why in ANCHORS:
        pts = dict(series.get(sid, {}).get("points", []))
        if not pts:
            warn(f"{sid} absent — cannot check anchor ({why})")
            continue
        got = pts.get(when)
        if got is None:
            warn(f"{sid} has no observation at {when} — cannot check anchor")
            continue
        if abs(got - expect) > tol:
            fail(f"{sid} at {when} is {got}, expected {expect}. {why}. "
                 f"A refresh should not change this — the parse is wrong.")
        else:
            ok(f"{sid} at {when} = {got}  ({why})")

    # ----------------------------------------------------------- 4. coherence
    print("\nCOHERENCE")
    registry = payload.get("registry", {})
    for key, spec in (payload.get("composites") or {}).items():
        for comp in spec.get("components", []) or []:
            if comp["id"] not in registry:
                fail(f"composite {key} references unknown indicator {comp['id']}")
    orphans = [s for s in series if s not in registry
               and s not in ("mci", "lci", "divergence")]
    if orphans:
        warn(f"{len(orphans)} series have data but no registry entry: "
             f"{', '.join(sorted(orphans)[:6])} — they will not appear in the app")
    for key in ("mci", "lci"):
        b = (payload.get("composite_build") or {}).get(key)
        if not b:
            warn(f"composite {key} was not built")
        elif b.get("stale_months"):
            print(f"  --    {key}: last {b['stale_months']} month(s) rest on "
                  f"carried-forward quarterly inputs (expected; flagged in the app)")
    ok("composite components all resolve")

    return report(args)


def report(args) -> int:
    print(f"\n{'=' * 62}")
    print(f"{len(fails)} failure(s), {len(warns)} warning(s)")
    if fails:
        print("\nFAILURES:")
        for f in fails:
            print(f"  - {f}")
    if args.strict and warns:
        print("\n--strict: warnings are failures")
        return 1
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
