#!/usr/bin/env python3
"""
Build the app payload for the China Monetary & Liquidity Conditions Tracker.

Reads:
  data/registry_{monetary,liquidity,context}.json   indicator definitions
  data/composites.json                              composite index construction
  data/seed/series.json                             observed time series

Writes:
  data/registry.json    merged registry (convenience artefact)
  app/data.js           self-contained payload consumed by app/index.html

Design notes
------------
* Everything is optional. Missing series are reported, never faked.
* Derived series are computed only when every input is present.
* Composites are z-scored on a common monthly grid, signed so that
  POSITIVE ALWAYS MEANS LOOSER, then weighted.
* No network access is required or attempted.
"""
from __future__ import annotations

import argparse
import json
import math
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
APP = ROOT / "app"

# ---------------------------------------------------------------- date helpers

def to_month(key: str) -> str | None:
    """Normalise any observation key to a 'YYYY-MM' month stamp."""
    key = str(key)
    if len(key) == 7 and key[4] == "-" and key[5] != "Q":
        return key                                    # 2024-07
    if len(key) == 10 and key[4] == "-":
        return key[:7]                                # 2024-07-19 -> 2024-07
    if "Q" in key:                                    # 2024-Q2 -> 2024-06
        year, q = key.split("-Q")
        return f"{year}-{int(q) * 3:02d}"
    if len(key) == 6 and key[4] == "Q":               # 2024Q2
        return f"{key[:4]}-{int(key[5]) * 3:02d}"
    return None


def month_index(month: str) -> int:
    y, m = month.split("-")
    return int(y) * 12 + int(m) - 1


def index_to_month(i: int) -> str:
    return f"{i // 12:04d}-{i % 12 + 1:02d}"


def monthly_map(series: dict) -> dict[str, float]:
    """Collapse a series' observations onto a monthly grid.

    Daily observations within a month are averaged, which is the right
    convention for money-market rates: the month average is far more
    informative about conditions than a single month-end print, which is
    routinely distorted by quarter-end and tax-date effects.
    """
    buckets: dict[str, list[float]] = {}
    for key, value in series.get("observations", []):
        # `float("nan")` is not None and survives every range comparison, so a NaN
        # from upstream slips past a None check and past the sanity gate's bounds,
        # then detonates inside statistics.pstdev. Reject non-finite values here,
        # at the only door into the pipeline.
        if value is None or not math.isfinite(float(value)):
            continue
        month = to_month(key)
        if month is None:
            continue
        buckets.setdefault(month, []).append(float(value))
    return {m: sum(v) / len(v) for m, v in sorted(buckets.items())}


def step_fill(monthly: dict[str, float], start: int, end: int) -> dict[str, float]:
    """Carry the last observation forward. For policy rates and the RRR, which
    are step functions that only print on change dates."""
    out, last = {}, None
    for i in range(start, end + 1):
        month = index_to_month(i)
        if month in monthly:
            last = monthly[month]
        if last is not None:
            out[month] = last
    return out


# ---------------------------------------------------------------------- series

def load_json(path: Path, default=None):
    if not path.exists():
        return default
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def build(seed_path: Path | None = None, app_dir: Path | None = None,
          data_dir: Path | None = None) -> int:
    seed_path = seed_path or (DATA / "seed" / "series.json")
    app_dir = app_dir or APP
    data_dir = data_dir or DATA

    registry: dict = {}
    for block in ("monetary", "liquidity", "context", "extra"):
        part = load_json(DATA / f"registry_{block}.json", {})
        for key, entry in part.items():
            entry["id"] = key
            registry[key] = entry

    composites = load_json(DATA / "composites.json", {})
    seed = load_json(seed_path, {"meta": {}, "series": {}})
    observed = dict(seed.get("series", {}))

    # Two supplementary files sit alongside the fetched seed: a second round of
    # mirror sourcing, and values entered by hand. Both merge on EXTEND-ONLY
    # terms — they may add dates a series lacks, but never restate one it already
    # has — so a supplement can only widen coverage, and the primary seed stays
    # the authority wherever they overlap. Keeping the hand-entered values in
    # their own file is what makes them auditable rather than indistinguishable
    # from fetched data; the merged provenance records what each contributed.
    def merge_supplement(doc: dict, label: str) -> None:
        adopted, extended = [], []
        for key, series in (doc or {}).get("series", {}).items():
            fresh = [o for o in series.get("observations", []) if o[1] is not None]
            if not fresh:
                continue
            if key not in observed:
                observed[key] = series
                adopted.append(f"{key} ({len(fresh)} obs)")
                continue
            have = {o[0]: o[1] for o in observed[key].get("observations", [])}
            added = {d: v for d, v in fresh if d not in have}
            if not added:
                continue
            merged = sorted({**added, **have}.items())
            entry = dict(observed[key])
            entry["observations"] = [[d, v] for d, v in merged]
            prov = dict(entry.get("provenance") or {})
            sup = series.get("provenance") or {}
            prov["source_name"] = (f"{prov.get('source_name', 'primary seed')} "
                                   f"(+{len(added)} obs from {sup.get('source_name', label)})")
            # A series is only as trustworthy as its weakest contributor.
            if sup.get("confidence") == "analyst-supplied":
                prov["confidence"] = "analyst-supplied"
            elif prov.get("confidence") == "verified":
                prov["confidence"] = "partial"
            entry["provenance"] = prov
            entry["notes"] = ((entry.get("notes") or "") +
                f" Extended with {len(added)} observation(s) through {max(added)} from "
                f"{label} ({sup.get('source_url', 'source unrecorded')}); where the two "
                f"overlapped the original values were kept.").strip()
            observed[key] = entry
            extended.append(f"{key} (+{len(added)}, now through {merged[-1][0]})")
        if adopted:
            print(f"{label}: adopted {', '.join(adopted)}")
        if extended:
            print(f"{label}: extended {', '.join(extended)}")

    merge_supplement(load_json(seed_path.parent / "mirrors_round2.json", {}),
                     "second-round mirror")
    merge_supplement(load_json(seed_path.parent / "analyst_supplied.json", {}),
                     "analyst-supplied")


    # Seed files name a few series differently from the registry.
    ALIASES = {"new_rmb_loans": "new_loans", "real_gdp_yoy_cum": "real_gdp_yoy"}
    for src, dst in ALIASES.items():
        if src in observed and dst not in observed:
            observed[dst] = observed.pop(src)

    print(f"registry: {len(registry)} indicators")
    print(f"seed:     {len(observed)} observed series")

    # monthly grid for every observed series
    grids: dict[str, dict[str, float]] = {}
    last_original: dict[str, str] = {}   # last month carrying a real observation
    for key, series in observed.items():
        grid = monthly_map(series)
        if grid:
            grids[key] = grid
            last_original[key] = max(grid)

    if not grids:
        print("WARNING: no observations found; app will render the framework only.")
        span_start = span_end = 0
    else:
        all_months = [m for g in grids.values() for m in g]
        span_start = month_index(min(all_months))
        span_end = month_index(max(all_months))

    # Policy rates and the RRR only print on change dates; between them the rate
    # genuinely IS the last value, so forward-filling them is correct rather than
    # stale, and they are excluded from the staleness accounting below.
    STEP = {"omo_7d", "mlf_1y", "lpr_1y", "lpr_5y", "rrr_large", "rrr_small"}

    # Some series carry history from a policy regime that is not comparable with
    # the present one (see usdcny). Trim those before anything is computed from
    # them, so the z-score describes conditions rather than a regime change.
    for key, entry in registry.items():
        floor = entry.get("history_from")
        if floor and key in grids:
            before = len(grids[key])
            grids[key] = {m_: v for m_, v in grids[key].items() if m_ >= floor}
            dropped = before - len(grids[key])
            if dropped:
                print(f"  trimmed {key}: dropped {dropped} observation(s) before {floor}")
                if key in last_original and grids[key]:
                    last_original[key] = max(grids[key])

    # step-function series need forward filling before they can be differenced
    for key in STEP:
        if key in grids:
            stop = span_end
            # The registry is the authority: a supplement that supplies the series
            # without the terminator must not be able to resurrect a dead rate.
            valid_to = (registry.get(key) or {}).get("valid_to") \
                or (observed.get(key) or {}).get("valid_to")
            if valid_to:
                stop = min(stop, month_index(valid_to))
            grids[key] = step_fill(grids[key], span_start, stop)

    # quarterly series forward-filled onto the monthly grid for composite use
    QUARTERLY = {k for k, e in registry.items() if e.get("freq") == "Q"}
    for key in QUARTERLY:
        if key in grids:
            grids[key] = step_fill(grids[key], span_start, span_end)

    # ------------------------------------------------------------- derivations
    def difference(target: str, left: str, right: str, scale: float = 1.0):
        if left not in grids or right not in grids:
            missing = [s for s in (left, right) if s not in grids]
            skipped.append(f"{target} (needs {', '.join(missing)})")
            return
        months = sorted(set(grids[left]) & set(grids[right]))
        if not months:
            skipped.append(f"{target} (no overlapping months)")
            return
        grids[target] = {m: (grids[left][m] - grids[right][m]) * scale for m in months}
        parents = [last_original[p] for p in (left, right)
                   if p in last_original and p not in STEP]
        if parents:
            last_original[target] = min(parents)
        built.append(f"{target}  [{months[0]} .. {months[-1]}, n={len(months)}]")

    built: list[str] = []
    skipped: list[str] = []

    difference("m1_m2_gap", "m1_yoy", "m2_yoy")
    difference("dr007_omo_spread", "dr007", "omo_7d", scale=100)              # -> bp
    difference("r_dr_spread", "r007", "dr007", scale=100)                     # -> bp
    difference("ncd_mlf_spread", "ncd_1y_aaa", "mlf_1y", scale=100)           # -> bp
    difference("ncd_omo_spread", "ncd_issuance_war", "omo_7d", scale=100)     # -> bp
    difference("term_spread", "cgb_10y", "cgb_1y", scale=100)                 # -> bp
    difference("cgb10y_omo_spread", "cgb_10y", "omo_7d", scale=100)           # -> bp
    difference("real_policy_rate", "omo_7d", "cpi_yoy")
    difference("real_policy_rate_core", "omo_7d", "core_cpi_yoy")
    difference("real_lending_rate", "walr_general", "cpi_yoy")
    difference("real_lending_rate_ppi", "walr_general", "ppi_yoy")
    # gdp_deflator_yoy / tsf_minus_ngdp are deliberately NOT derived: the Dec-2024
    # economic census revised the nominal GDP base, so any growth rate spanning that
    # break is wrong. See the `unavailable` note on those registry entries.

    # credit impulse: 12m change in the 12m rolling TSF flow, scaled by
    # trailing nominal GDP. Falls back to scaling by the rolling flow itself
    # when no GDP level series is available, which preserves the turning
    # points (what the indicator is used for) while changing the units.
    if "tsf_flow" in grids:
        flow = grids["tsf_flow"]
        months = sorted(flow)
        rolling: dict[str, float] = {}
        for i, month in enumerate(months):
            if i >= 11:
                window = [flow[m] for m in months[i - 11:i + 1]]
                rolling[month] = sum(window)
        gdp = grids.get("nominal_gdp_level")
        impulse: dict[str, float] = {}
        basis = "nominal GDP" if gdp else "trailing 12m TSF flow"
        for month in sorted(rolling):
            prior = index_to_month(month_index(month) - 12)
            if prior not in rolling:
                continue
            change = rolling[month] - rolling[prior]
            denominator = gdp.get(month) if gdp else rolling[month]
            if denominator:
                impulse[month] = change / denominator * 100
        if impulse:
            grids["credit_impulse"] = impulse
            if "tsf_flow" in last_original:
                last_original["credit_impulse"] = last_original["tsf_flow"]
            if not gdp:
                # Without a nominal GDP level the indicator is the 12-month change in
                # the rolling 12-month credit flow. Turning points — what the impulse
                # is read for — survive; the units do not, so do not keep calling it
                # "pp of GDP".
                entry = registry.setdefault("credit_impulse", {})
                entry["unit"] = "% y/y"
                entry["basis_note"] = (
                    "Scaled by the trailing 12-month credit flow, not nominal GDP, because no "
                    "verified nominal GDP level series was available. Turning points are "
                    "unaffected; the units are not comparable with a conventional "
                    "percent-of-GDP credit impulse.")
            registry.setdefault("credit_impulse", {})["basis"] = basis
            span = sorted(impulse)
            built.append(f"credit_impulse  [{span[0]} .. {span[-1]}, n={len(impulse)}, basis={basis}]")
        else:
            skipped.append("credit_impulse (insufficient TSF flow history)")
    else:
        skipped.append("credit_impulse (needs tsf_flow)")

    print(f"\nderived built ({len(built)}):")
    for line in built:
        print(f"  + {line}")
    if skipped:
        print(f"\nderived skipped ({len(skipped)}):")
        for line in skipped:
            print(f"  - {line}")

    # ------------------------------------------------------------- composites
    def zscores(values: dict[str, float]) -> dict[str, float]:
        nums = [v for v in values.values() if math.isfinite(v)]
        if len(nums) < 8:
            return {}
        mean = statistics.fmean(nums)
        sd = statistics.pstdev(nums)
        if not math.isfinite(sd) or sd == 0:
            return {}
        return {m: (v - mean) / sd for m, v in values.items()}

    composite_out: dict[str, dict] = {}
    for key, spec in composites.items():
        components = spec.get("components")
        if not components:
            continue
        pieces, used, absent = {}, [], []
        for component in components:
            cid = component["id"]
            if cid not in grids:
                absent.append(cid)
                continue
            z = zscores(grids[cid])
            if not z:
                absent.append(f"{cid} (too few observations)")
                continue
            pieces[cid] = (z, component["weight"] * component["sign"])
            used.append(cid)
        if not pieces:
            print(f"\ncomposite {key}: NOT BUILT — no usable components ({', '.join(absent)})")
            continue

        # Unbalanced panel. Components start and end at different dates, so requiring
        # every component to be present would truncate the index to the shortest
        # series — which for liquidity would leave the monitor more than a year stale.
        # Instead each month uses whatever components exist, with the weights
        # renormalised over those present, and we record the count so reduced-coverage
        # months can be flagged in the app rather than passed off as full readings.
        full_weight = sum(abs(w) for _, w in pieces.values())
        months = sorted(set().union(*(set(z) for z, _ in pieces.values())))
        values, coverage = {}, {}
        for month in months:
            avail = [(z[month], w) for z, w in pieces.values() if month in z]
            if len(avail) < 2:            # one component is a series, not an index
                continue
            wsum = sum(abs(w) for _, w in avail)
            values[month] = sum(v * w for v, w in avail) / wsum
            coverage[month] = round(wsum / full_weight, 3)
        if not values:
            print(f"\ncomposite {key}: NOT BUILT — never two components in the same month")
            continue
        months = sorted(values)
        grids[key] = values
        last_cov = coverage[months[-1]]
        composite_out[key] = {
            "components_used": used,
            "components_missing": absent,
            "coverage": f"{months[0]} .. {months[-1]}",
            "n": len(months),
            "weight_coverage": coverage,
            "latest_weight_coverage": last_cov,
            "full_coverage_months": sum(1 for m in months if coverage[m] >= 0.999),
        }
        fresh = [last_original[c] for c in used if c in last_original]
        if fresh:
            freshest = max(fresh)
            composite_out[key]["fresh_until"] = freshest
            stale = [m for m in months if m > freshest]
            composite_out[key]["stale_months"] = len(stale)
            if stale:
                print(f"  WARNING {key}: last {len(stale)} month(s) after {freshest} rest entirely on "
                      f"quarterly inputs carried forward — not fresh readings")
        note = f" | missing: {', '.join(absent)}" if absent else ""
        print(f"\ncomposite {key}: built from {len(used)}/{len(components)} components, "
              f"n={len(months)}, latest month carries {last_cov:.0%} of index weight{note}")

    if "mci" in grids and "lci" in grids:
        months = sorted(set(grids["mci"]) & set(grids["lci"]))
        if months:
            grids["divergence"] = {m: grids["lci"][m] - grids["mci"][m] for m in months}
            composite_out["divergence"] = {
                "components_used": ["lci", "mci"],
                "components_missing": [],
                "coverage": f"{months[0]} .. {months[-1]}",
                "n": len(months),
            }
            print(f"composite divergence: built, n={len(months)}")

    # ------------------------------------------------------------------ output
    payload_series = {}
    for key, grid in grids.items():
        if not grid:
            continue
        entry = registry.get(key, {})
        source = observed.get(key, {})
        payload_series[key] = {
            "points": [[m, round(v, 4)] for m, v in sorted(grid.items())],
            "freq": entry.get("freq", "M"),
            "unit": entry.get("unit", ""),
            "provenance": source.get("provenance"),
            "series_notes": source.get("notes"),
            "last_original": last_original.get(key),
        }

    payload = {
        "meta": {
            "generated": seed.get("meta", {}).get("generated"),
            "built_from_seed": bool(observed),
            "gaps": seed.get("meta", {}).get("gaps", []),
            "seed_note": seed.get("meta", {}).get("note"),
            "derived_built": built,
            "derived_skipped": skipped,
        },
        "registry": registry,
        "composites": composites,
        "composite_build": composite_out,
        "series": payload_series,
    }

    (data_dir / "registry.json").write_text(
        json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8")

    app_dir.mkdir(parents=True, exist_ok=True)
    (app_dir / "data.js").write_text(
        "// Generated by scripts/build_app_data.py — do not edit by hand.\n"
        "window.CMLT_DATA = " + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";\n",
        encoding="utf-8")

    size = (app_dir / "data.js").stat().st_size
    print(f"\nwrote app/data.js  ({size / 1024:.1f} KB, {len(payload_series)} series)")
    print(f"wrote data/registry.json ({len(registry)} indicators)")

    missing = [k for k in registry if k not in payload_series]
    if missing:
        print(f"\nindicators with NO DATA ({len(missing)}): {', '.join(sorted(missing))}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=Path, default=None,
                        help="path to the observed series JSON")
    parser.add_argument("--app-dir", type=Path, default=None,
                        help="directory to write data.js into")
    parser.add_argument("--data-dir", type=Path, default=None,
                        help="directory to write registry.json into")
    args = parser.parse_args()
    return build(args.seed, args.app_dir, args.data_dir)


if __name__ == "__main__":
    raise SystemExit(main())
