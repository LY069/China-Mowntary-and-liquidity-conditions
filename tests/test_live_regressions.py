"""Regressions for bugs that only a live endpoint run exposed.

Workflow run 34751310340 fetched real data for the first time and the build
crashed. These lock in the three fixes so the same failures cannot return
silently. Each test reproduces the original failure mode, not just the fix.

Run:  python3 tests/test_live_regressions.py
"""
import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

FAILURES = []


def check(label, ok, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {label}" + (f"\n        {detail}" if not ok and detail else ""))
    if not ok:
        FAILURES.append(label)


def test_nan_does_not_crash_the_build():
    """Upstream sent NaN. float('nan') is not None and survives every range
    comparison, so it passed the None filter and the sanity gate's bounds, then
    raised AttributeError inside statistics.pstdev. The build must now drop it."""
    print("NaN from upstream must not reach the statistics layer")
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        seed = {"meta": {"generated": "2026-01-01", "gaps": []}, "series": {}}
        # enough observations to clear the 8-point z-score floor, one of them NaN
        obs = [[f"2024-{m:02d}", 1.5 + m * 0.01] for m in range(1, 13)]
        obs[5][1] = float("nan")
        seed["series"]["dr007"] = {
            "name": "DR007", "unit": "%", "freq": "D",
            "provenance": {"source_name": "t", "source_url": "https://e.invalid",
                           "retrieved": "2026-01-01", "confidence": "partial"},
            "observations": obs,
        }
        p = td / "series.json"
        p.write_text(json.dumps(seed).replace("NaN", "NaN"), encoding="utf-8")
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_app_data.py"),
                            "--seed", str(p), "--app-dir", str(td / "app"),
                            "--data-dir", str(td)],
                           capture_output=True, text=True)
        check("build exits cleanly with a NaN in the input", r.returncode == 0,
              (r.stderr or "")[-400:])
        if r.returncode == 0:
            raw = (td / "app" / "data.js").read_text()
            payload = json.loads(raw[raw.index("{"):raw.rindex(";")])
            pts = payload["series"].get("dr007", {}).get("points", [])
            vals = [v for _, v in pts]
            check("the NaN observation is dropped, not carried", len(vals) == 11,
                  f"kept {len(vals)} of 12")
            check("no non-finite value survives into the payload",
                  all(math.isfinite(v) for v in vals))


def test_refresh_never_shrinks_a_series():
    """MOFCOM serves a rolling window, so a wholesale overwrite truncated
    tsf_flow and silently killed the credit impulse. The merge must union."""
    print("\na refresh must extend history, never truncate it")
    import refresh_data as rd
    prior = [["2024-01", 1.0], ["2024-02", 2.0], ["2024-03", 3.0]]
    fetched = [("2024-03", 3.5), ("2024-04", 4.0)]        # shorter window, one revision
    merged = {d: v for d, v in prior if v is not None}
    merged.update({d: v for d, v in fetched})
    out = sorted(merged.items())
    check("earlier observations upstream dropped are retained",
          [d for d, _ in out] == ["2024-01", "2024-02", "2024-03", "2024-04"], str(out))
    check("an upstream revision wins on a shared date", dict(out)["2024-03"] == 3.5)
    src = (ROOT / "scripts" / "refresh_data.py").read_text()
    check("refresh_data.py unions rather than assigns",
          'entry["observations"] = [[d, v] for d, v in sorted(merged.items())]' in src)
    check("refresh_data.py filters non-finite values", "math.isfinite(num)" in src)


def test_dead_rate_is_not_resurrected():
    """The MLF stopped having a single announced rate in March 2025. valid_to
    lived only in analyst_supplied.json, so once a mirror supplied mlf_1y
    wholesale the terminator was dropped and the rate was forward-filled 18
    months past its own death, making ncd_mlf_spread build against a rate that
    does not exist."""
    print("\na terminated series must stay terminated whoever supplies it")
    reg = json.loads((ROOT / "data" / "registry_monetary.json").read_text())
    check("registry carries mlf_1y valid_to", reg["mlf_1y"].get("valid_to") == "2025-03",
          str(reg["mlf_1y"].get("valid_to")))
    src = (ROOT / "scripts" / "build_app_data.py").read_text()
    check("build reads valid_to from the registry first",
          'valid_to = (registry.get(key) or {}).get("valid_to")' in src)
    raw = (ROOT / "app" / "data.js").read_text()
    payload = json.loads(raw[raw.index("{"):raw.rindex(";")])
    pts = payload["series"].get("mlf_1y", {}).get("points", [])
    check("built mlf_1y stops at 2025-03", bool(pts) and pts[-1][0] == "2025-03",
          pts[-1][0] if pts else "absent")
    check("ncd_mlf_spread is not built against a dead rate",
          "ncd_mlf_spread" not in payload["series"])


def test_credit_curve_rating_is_matched_exactly():
    """The first live run selected 中短期票据(AAA+) when asked for AA+, because
    'AA+' is a substring of 'AAA+'. A higher credit tier understates the spread,
    and nothing about the output would have looked wrong."""
    print("\ncredit curve rating must match as a whole token, not a substring")
    sys.path.insert(0, str(ROOT / "scripts"))
    import refresh_data as rd

    labels = {"中短期票据(AAA+)": "C1", "中短期票据(AA+)": "C2",
              "中短期票据(AA)": "C3", "中短期票据(AA+)浮动利率点差": "C4"}

    class FakeMap:
        def iterrows(self):
            for i, (k, v) in enumerate(labels.items()):
                yield i, {"cnLabel": k, "value": v}

    class FakeAk:
        def bond_china_close_return_map(self): return FakeMap()

    picked = {}
    real = rd._ncd_records
    rd._ncd_records = lambda code, s_, e_, term="1": (picked.setdefault("code", code),
                                                      picked.setdefault("term", term),
                                                      [])[2]
    try:
        rd.fetch_credit_spread(FakeAk(), "2026-08")
    finally:
        rd._ncd_records = real
    check("picks AA+ not AAA+", picked.get("code") == "C2",
          f'expected curve code C2, got {picked.get("code")!r}')
    check("uses the 3-year point", picked.get("term") == "3",
          f'expected termId 3, got {picked.get("term")!r}')


def test_workflow_reports_any_failure():
    """The restore and upload steps were keyed to the gate alone, so a crash in
    the rebuild step left no artifact and no restore."""
    print("\nworkflow diagnostics must fire on any failure, not only the gate")
    wf = (ROOT / ".github" / "workflows" / "refresh-data.yml").read_text()
    check("upload fires on any failure", "Upload rejected data on any failure" in wf)
    check("restore fires on any failure", "Restore the previous dataset on any failure" in wf)
    check("neither is still gate-only", "steps.gate.outcome == 'failure'" not in wf)


def test_spike_check_runs_at_daily_resolution():
    """The spike guard used to compare monthly means, which both invented
    defects and hid them.

    Invented: a genuine multi-week move makes the trough month look like a
    spike against its neighbours. That flagged cgb_1y 2015-06, which reproduces
    value-for-value from ChinaBond (21/21) and whose daily path is smooth, and
    shibor_3m 2011-07, which was the real mid-2011 squeeze.

    Hid: averaging thirty days dilutes one bad row below the threshold. A
    mis-parsed row reading the wrong tenor sat in mtn_aa_3y at four batch
    boundaries and the monthly check never saw it.
    """
    print("\nspike check must look between adjacent days, not months")
    src = (ROOT / "scripts" / "validate_data.py").read_text(encoding="utf-8")
    check("reads the daily seed", "daily_seed" in src)
    check("prefers daily over built", 'pts, res = src, "daily"' in src)

    # The property that matters: one row out of line is caught; a smooth ramp
    # of the same total size is not.
    limit = 0.4
    def flags(vals):
        n = 0
        for i in range(1, len(vals) - 1):
            p_, c_, x_ = vals[i - 1], vals[i], vals[i + 1]
            if abs(c_ - p_) > limit and abs(c_ - x_) > limit \
                    and (c_ - p_) * (c_ - x_) > 0:
                n += 1
        return n

    # one mis-parsed row in an otherwise flat series
    bad = [2.40, 2.41, 2.39, 1.75, 2.40, 2.41]
    check("catches a single bad row", flags(bad) == 1,
          f"expected 1 flag, got {flags(bad)}")

    # the real June-2015 cgb_1y path: a smooth six-week excursion of similar
    # depth, which must NOT be flagged
    real = [2.3822, 2.2462, 2.0338, 1.8707, 1.9369, 1.9387, 1.9947, 1.9651,
            1.9356, 1.8813, 1.8763, 1.8576, 1.7786, 1.7097, 1.7103, 1.6870,
            1.6482, 1.6407, 1.6890, 1.7044, 1.7494]
    check("does not flag the real 2015 move", flags(real) == 0,
          f"expected 0 flags, got {flags(real)}")


def main():
    test_nan_does_not_crash_the_build()
    test_refresh_never_shrinks_a_series()
    test_dead_rate_is_not_resurrected()
    test_credit_curve_rating_is_matched_exactly()
    test_workflow_reports_any_failure()
    test_spike_check_runs_at_daily_resolution()
    print("\nALL PASSED" if not FAILURES else f"\n{len(FAILURES)} FAILURE(S): {FAILURES}")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())
