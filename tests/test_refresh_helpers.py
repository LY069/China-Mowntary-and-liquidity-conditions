"""Unit tests for the parsing helpers in scripts/refresh_data.py.

The network fetchers cannot be exercised without akshare and outbound access,
but the column resolution and date normalisation are where the real bugs live:
akshare renames columns between releases and returns dates in several formats.
Those are pure functions and are tested here against a minimal DataFrame stub.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import refresh_data as rd                                    # noqa: E402


class FakeDF:
    """Just enough of the pandas DataFrame surface for these helpers."""
    def __init__(self, columns, rows):
        self.columns = columns
        self._rows = rows

    def iterrows(self):
        for i, r in enumerate(self._rows):
            yield i, dict(zip(self.columns, r))


def check(label, got, want):
    ok = got == want
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {got!r}" + ("" if ok else f"  expected {want!r}"))
    return ok


def main():
    ok = True
    print("pick(): exact match wins, then substring")
    df = FakeDF(["月份", "货币(M1)-同比增长", "货币和准货币(M2)-同比增长"], [])
    ok &= check("exact", rd.pick(df, "月份"), "月份")
    ok &= check("first candidate present", rd.pick(df, "统计时间", "月份"), "月份")
    ok &= check("substring fallback", rd.pick(df, "货币(M1)"), "货币(M1)-同比增长")
    ok &= check("token tuple survives renames", rd.pick(df, ("M1", "同比")), "货币(M1)-同比增长")
    ok &= check("token tuple picks M2 not M1", rd.pick(df, ("M2", "同比")), "货币和准货币(M2)-同比增长")
    # the exact-match-first rule is what stops "1年" matching a "10年" column
    df10 = FakeDF(["日期", "10年", "1年"], [])
    ok &= check("exact beats substring for 1y/10y", rd.pick(df10, "1年", "1Y"), "1年")
    ok &= check("10y resolves", rd.pick(df10, "10年", "10Y"), "10年")
    try:
        rd.pick(df, "nope")
        ok &= check("missing raises", "no raise", "KeyError")
    except KeyError:
        ok &= check("missing raises KeyError", True, True)

    print("\nas_month(): every format akshare is known to emit")
    for raw, want in [("2024-07-19", "2024-07"), ("20240719", "2024-07"), ("2024-07", "2024-07"),
                      ("2024年07月份", "2024-07"), ("2024年7月", "2024-07"), ("garbage", None)]:
        ok &= check(repr(raw), rd.as_month(raw), want)

    print("\nas_day()")
    for raw, want in [("2024-07-19", "2024-07-19"), ("20240719", "2024-07-19"),
                      ("2024/07/19", "2024-07-19"), ("2024-07", None)]:
        ok &= check(repr(raw), rd.as_day(raw), want)

    print("\nmonthly(): scaling, dedup, sort, bad-row skipping")
    df = FakeDF(["月份", "v"], [["2024年03月份", "10"], ["2024年01月份", "5"],
                                ["2024年02月份", None], ["bad", "7"], ["2024年01月份", "6"]])
    got = rd.monthly(df, "月份", "v", scale=0.1)
    ok &= check("scaled/deduped/sorted", got, [("2024-01", 0.6), ("2024-03", 1.0)])

    print("\ndaily(): non-numeric values are dropped, not crashed on")
    df = FakeDF(["date", "FDR007"], [["20240102", "1.85"], ["20240103", "--"], ["20240104", 1.9]])
    ok &= check("skips junk", rd.daily(df, "date", "FDR007"),
                [("2024-01-02", 1.85), ("2024-01-04", 1.9)])

    print("\nMANUAL_ONLY covers the series with no machine-readable source")
    for sid in ("walr_general", "excess_reserve_ratio", "omo_7d", "mlf_1y"):
        ok &= check(sid, sid in rd.MANUAL_ONLY, True)

    print("\nALL PASSED" if ok else "\nFAILURES PRESENT")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
