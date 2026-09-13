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


def test_workflow_reports_any_failure():
    """The restore and upload steps were keyed to the gate alone, so a crash in
    the rebuild step left no artifact and no restore."""
    print("\nworkflow diagnostics must fire on any failure, not only the gate")
    wf = (ROOT / ".github" / "workflows" / "refresh-data.yml").read_text()
    check("upload fires on any failure", "Upload rejected data on any failure" in wf)
    check("restore fires on any failure", "Restore the previous dataset on any failure" in wf)
    check("neither is still gate-only", "steps.gate.outcome == 'failure'" not in wf)


def main():
    test_nan_does_not_crash_the_build()
    test_refresh_never_shrinks_a_series()
    test_dead_rate_is_not_resurrected()
    test_workflow_reports_any_failure()
    print("\nALL PASSED" if not FAILURES else f"\n{len(FAILURES)} FAILURE(S): {FAILURES}")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())
