"""Replay tests for the akshare fetchers in scripts/refresh_data.py.

The endpoints themselves are unreachable from the build sandbox, so these tests
stand a fake `akshare` in front of the fetchers and feed them frames whose
column names are taken VERBATIM from akshare 1.18.94's own source (read by
introspecting the installed package, not guessed). That verifies everything
between the API boundary and the output file: column resolution, date parsing,
unit scaling, month/year windowing, and the shape of what gets written.

What this does NOT verify: that the live endpoints still return those columns.
Only a run with real network does that — see .github/workflows/refresh-data.yml,
which executes the real thing on GitHub's runners.

Run:  python3 tests/test_refresh_fetchers.py      (needs pandas)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

try:
    import pandas as pd
except ImportError:
    print("SKIPPED: pandas not installed (pip install pandas akshare to run these)")
    raise SystemExit(0)

import refresh_data as rd                                    # noqa: E402

FAILURES = []


def check(label, got, want):
    ok = got == want
    print(f"  {'PASS' if ok else 'FAIL'}  {label}")
    if not ok:
        print(f"        got  {got!r}\n        want {want!r}")
        FAILURES.append(label)


class FakeAk:
    """Stands in for akshare. Column names are akshare 1.18.94's own."""

    def __init__(self):
        self.repo_calls, self.cgb_calls = [], []

    # 月份 + the M1/M2 columns, values in 亿元 as akshare returns them
    def macro_china_money_supply(self):
        return pd.DataFrame({
            "月份": ["2024年01月份", "2024年02月份"],
            "货币和准货币(M2)-数量(亿元)": ["2970000", "2995000"],
            "货币和准货币(M2)-同比增长": ["8.7", "8.7"],
            "货币(M1)-数量(亿元)": ["690000", "665000"],
            "货币(M1)-同比增长": ["5.9", "1.2"],
        })

    def macro_china_shrzgm(self):
        return pd.DataFrame({
            "月份": ["2024年01月份", "2024年02月份"],
            "社会融资规模增量": ["64200", "15200"],       # 亿元
        })

    def macro_china_lpr(self):
        return pd.DataFrame({
            "TRADE_DATE": ["2024-07-22", "2024-10-21"],
            "LPR1Y": [3.35, 3.10],
            "LPR5Y": [3.85, 3.60],
        })

    def repo_rate_hist(self, start_date, end_date):
        self.repo_calls.append((start_date, end_date))
        return pd.DataFrame({
            "date": [f"{start_date[:4]}-{start_date[4:6]}-05"],
            "FR001": [1.75], "FR007": [1.95], "FR014": [2.05],
            "FDR001": [1.65], "FDR007": [1.82], "FDR014": [1.90],
        })

    def bond_china_yield(self, start_date, end_date):
        self.cgb_calls.append((start_date, end_date))
        return pd.DataFrame({
            "曲线名称": ["中债国债收益率曲线"],
            "日期": [f"{start_date[:4]}-03-15"],
            "3月": [1.40], "6月": [1.45], "1年": [1.50],
            "3年": [1.60], "5年": [1.65], "7年": [1.70],
            "10年": [1.75], "30年": [2.05],
        })

    def bond_china_close_return(self, symbol, period, start_date, end_date):
        assert symbol == "同业存单(AAA)", symbol
        assert period == "1", period
        return pd.DataFrame({
            "日期": ["2026-01-05", "2026-01-06"],
            "期限": [1.0, 1.0],
            "到期收益率": [1.92, 1.90],
            "即期收益率": [1.92, 1.90],
            "远期收益率": [1.93, 1.91],
        })

    def rate_interbank(self, market, symbol, indicator):
        assert symbol in ("Shibor人民币", "Hibor人民币"), symbol
        return pd.DataFrame({
            "报告日": ["2026-01-05"], "利率": [1.88], "涨跌": [0.01],
        })

    def macro_china_reserve_requirement_ratio(self):
        return pd.DataFrame({
            "公布时间": ["2025-05-07"], "生效时间": ["2025-05-15"],
            "大型金融机构-调整前": [9.5], "大型金融机构-调整后": [9.0],
            "中小金融机构-调整前": [6.5], "中小金融机构-调整后": [6.0],
        })


def main():
    ak = FakeAk()
    print("money supply — 亿元 converted to RMB bn, M1/M2 resolved separately")
    r = rd.fetch_money_supply(ak, "2015-01")
    check("m1_yoy", r["m1_yoy"][0], [("2024-01", 5.9), ("2024-02", 1.2)])
    check("m2_yoy", r["m2_yoy"][0], [("2024-01", 8.7), ("2024-02", 8.7)])
    check("m2_level scaled 亿元->bn", r["m2_level"][0], [("2024-01", 297000.0), ("2024-02", 299500.0)])

    print("\nTSF — 亿元 converted, MOFCOM lag noted")
    r = rd.fetch_tsf(ak, "2015-01")
    check("tsf_flow", r["tsf_flow"][0], [("2024-01", 6420.0), ("2024-02", 1520.0)])
    check("lag documented", "MOFCOM" in r["tsf_flow"][2], True)

    print("\nLPR — TRADE_DATE/LPR1Y/LPR5Y")
    r = rd.fetch_lpr(ak, "2015-01")
    check("lpr_1y", r["lpr_1y"][0], [("2024-07", 3.35), ("2024-10", 3.1)])
    check("lpr_5y", r["lpr_5y"][0], [("2024-07", 3.85), ("2024-10", 3.6)])

    print("\nrepo fixings — the endpoint caps a request at one month")
    r = rd.fetch_repo_fixings(ak, "2026-05")
    check("walked month by month", ak.repo_calls,
          [("20260501", "20260531"), ("20260601", "20260630"), ("20260701", "20260731"),
           ("20260801", "20260831"), ("20260901", "20260930")])
    check("dr007 <- FDR007", r["dr007"][0][0], ("2026-05-05", 1.82))
    check("r007 <- FR007", r["r007"][0][0], ("2026-05-05", 1.95))
    check("dr007 labelled a proxy", "PROXY" in r["dr007"][2], True)

    print("\nCGB curve — ChinaBond caps a window at one year")
    r = rd.fetch_cgb_curve(ak, "2024-01")
    check("walked year by year", ak.cgb_calls,
          [("20240101", "20241231"), ("20250101", "20251231"), ("20260101", "20261231")])
    check("cgb_1y picked exactly, not from '10年'", r["cgb_1y"][0][0], ("2024-03-15", 1.5))
    check("cgb_10y", r["cgb_10y"][0][0], ("2024-03-15", 1.75))

    print("\nNCD — AAA curve, 1-year point")
    r = rd.fetch_ncd(ak, "2026-01")
    check("ncd_1y_aaa", r["ncd_1y_aaa"][0], [("2026-01-05", 1.92), ("2026-01-06", 1.9)])

    print("\ninterbank — SHIBOR and CNH HIBOR")
    r = rd.fetch_interbank(ak, "2026-01")
    check("shibor_3m", r["shibor_3m"][0], [("2026-01-05", 1.88)])
    check("cnh_hibor_on", r["cnh_hibor_on"][0], [("2026-01-05", 1.88)])

    print("\nRRR — keyed on the EFFECTIVE date, not the announcement date")
    r = rd.fetch_rrr(ak, "2015-01")
    check("rrr_large uses 生效时间", r["rrr_large"][0], [("2025-05-15", 9.0)])
    check("rrr_small", r["rrr_small"][0], [("2025-05-15", 6.0)])

    print("\nevery fetcher group is registered")
    registered = {s for _, ids in rd.FETCHERS.values() for s in ids}
    for sid in ("m1_yoy", "tsf_flow", "lpr_1y", "dr007", "r007", "cgb_1y",
                "cgb_10y", "ncd_1y_aaa", "shibor_3m", "cnh_hibor_on", "rrr_large"):
        check(f"{sid} registered", sid in registered, True)

    print("\nALL PASSED" if not FAILURES else f"\n{len(FAILURES)} FAILURE(S): {FAILURES}")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())
