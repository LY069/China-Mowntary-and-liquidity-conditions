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
    """Compare got against want. NOTE: tests/test_live_regressions.py spells
    this differently — check(label, ok, detail) — so a call written for one
    file is silently wrong in the other."""
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
        # MOFCOM serves bare 'YYYYMM' — six characters, which is exactly the
        # format that silently dropped 125 of 136 observations before it was fixed.
        return pd.DataFrame({
            "月份": ["201501", "201502"],
            "社会融资规模增量": ["20516", "13609"],        # 亿元
            "其中-人民币贷款": ["14708", "11437"],
            "其中-委托贷款外币贷款": ["212", "-146"],
            "其中-委托贷款": ["832", "1299"],
            "其中-信托贷款": ["52", "38"],
            "其中-未贴现银行承兑汇票": ["1946", "-592"],
            "其中-企业债券": ["1868", "716"],
            "其中-非金融企业境内股票融资": ["526.0", "542.0"],
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

    def bond_china_close_return_map(self):
        return pd.DataFrame({"cnLabel": ["国债", "同业存单(AAA)"],
                             "value": ["CYCC000", "CYCC999"]})

    def rate_interbank(self, market, symbol, indicator):
        assert symbol in ("Shibor人民币", "Hibor人民币"), symbol
        return pd.DataFrame({
            "报告日": ["2026-01-05"], "利率": [1.88], "涨跌": [0.01],
        })

    def macro_china_central_bank_balance(self):
        return pd.DataFrame({
            "统计时间": ["2026.6", "2026.7"],
            "政府存款": ["50000", "62000"],              # 亿元
            "对其他存款性公司债权": ["212276.16", "218480.42"],
        })

    def macro_china_gdp(self):
        return pd.DataFrame({
            "季度": ["2025年第1-2季度", "2026年第1-2季度"],
            "国内生产总值-绝对值": ["660000.0", "695704.0"],
            "国内生产总值-同比增长": ["5.3", "4.7"],
        })

    def macro_china_reserve_requirement_ratio(self):
        return pd.DataFrame({
            # akshare does NOT date-convert these; East Money serves ISO datetimes
            "公布时间": ["2025-05-07 00:00:00"], "生效时间": ["2025-05-15 00:00:00"],
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
    check("tsf_flow parses bare YYYYMM", r["tsf_flow"][0],
          [("2015-01", 2051.6), ("2015-02", 1360.9)])
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

    print("\nNCD — direct CFETS call, tolerant of the schema change that broke akshare")
    calls = []

    def fake_records(code, s_, e_):
        calls.append((code, s_, e_))
        # Old schema carried newDateValue; upstream dropped it, which is exactly
        # what made akshare's `del temp_df["newDateValue"]` raise KeyError.
        if s_.startswith("202601"):
            return [[rd.as_day("2026-01-05"), 1.92]]
        return [[rd.as_day("2026-02-05"), 1.90]]

    real = rd._ncd_records
    rd._ncd_records = fake_records
    try:
        r = rd.fetch_ncd(ak, "2026-01")
    finally:
        rd._ncd_records = real
    check("curve code resolved from cnLabel/value", calls[0][0], "CYCC999")
    check("walked month by month", [c[1] for c in calls][:2], ["20260101", "20260201"])
    check("ncd_1y_aaa", r["ncd_1y_aaa"][0], [["2026-01-05", 1.92], ["2026-02-05", 1.9]])

    print("\n_ncd_records parses records with and without newDateValue")
    import json as _json

    class FakeResp:
        def __init__(self, payload): self._p = payload
        def raise_for_status(self): pass
        def json(self): return self._p

    import requests as _rq
    saved = _rq.get
    # The real record, read verbatim off the live endpoint:
    #   {"newDateValueCN":"2026-09-10","yearTermStr":"3.0",
    #    "maturityYieldStr":"1.6950","currentYieldStr":"1.6965",
    #    "futureYieldStr":"1.9377"}
    # Fields are read by NAME now. They used to be read positionally, which
    # depended on dict ordering surviving an upstream schema change.
    def rec(day, term, ytm, *, legacy_key=False, fwd="1.89"):
        k = "newDateValue" if legacy_key else "newDateValueCN"
        return {k: day, "yearTermStr": term, "maturityYieldStr": ytm,
                "currentYieldStr": ytm, "futureYieldStr": fwd}

    for label, payload, want in [
        ("current schema (newDateValueCN)",
         [rec("2026-03-02", "1.0", "1.88")], [["2026-03-02", 1.88]]),
        ("legacy key (newDateValue) still parses",
         [rec("2026-03-02", "1.0", "1.88", legacy_key=True)], [["2026-03-02", 1.88]]),
        ("a yield of '---' on an illiquid point is dropped",
         [rec("2026-03-02", "1.0", "---")], []),
        # THE BUG THIS TEST EXISTS FOR: termId does not filter the response.
        # CFETS returns the whole curve for every date, so a parser that reads
        # a yield out of every record collects whichever tenors land in the
        # page. That shipped the 15-year point as the 3-year one.
        ("whole curve returned — only the asked-for tenor is taken",
         [rec("2026-03-02", "0.25", "1.20"),
          rec("2026-03-02", "1.0", "1.88"),
          rec("2026-03-02", "5.0", "2.55"),
          rec("2026-03-02", "15.0", "3.10")],
         [["2026-03-02", 1.88]]),
        ("no record at the asked-for tenor yields nothing, not a wrong number",
         [rec("2026-03-02", "5.0", "2.55"), rec("2026-03-02", "15.0", "3.10")], []),
    ]:
        _rq.get = lambda *a, **k: FakeResp({"records": payload})
        try:
            got = rd._ncd_records("CYCC999", "20260301", "20260331", term="1")
        finally:
            _rq.get = saved
        check(label, got, want)

    # Pagination. pageSize is capped at 50 by the server, and the response
    # carries the whole curve, so fifty records is two or three DAYS. Without
    # paging, a month-long window is truncated silently — which is exactly how
    # this series ended up with twelve observations.
    pages = {}

    def paged(*a, **k):
        n = int(k["params"]["pageNum"])
        pages[n] = pages.get(n, 0) + 1
        if n == 1:
            return FakeResp({"records": [rec(f"2026-03-{d:02d}", "1.0", "1.80")
                                         for d in range(1, 26)]
                                        + [rec(f"2026-03-{d:02d}", "5.0", "2.50")
                                           for d in range(1, 26)]})   # exactly 50
        if n == 2:
            return FakeResp({"records": [rec("2026-03-26", "1.0", "1.85")]})
        return FakeResp({"records": []})

    _rq.get = paged
    try:
        got = rd._ncd_records("CYCC999", "20260301", "20260331", term="1")
    finally:
        _rq.get = saved
    check("a full page triggers the next one", sorted(pages), [1, 2])
    check("page 2's observation survives", ["2026-03-26", 1.85] in got, True)
    check("both pages' 1y points are kept, 5y dropped", len(got), 26)

    # And the tenor actually asked for is honoured, not hard-coded to 1.
    _rq.get = lambda *a, **k: FakeResp({"records": [
        rec("2026-03-02", "1.0", "1.88"), rec("2026-03-02", "3.0", "2.11")]})
    try:
        got3 = rd._ncd_records("CYCC999", "20260301", "20260331", term="3")
    finally:
        _rq.get = saved
    check("term='3' selects the 3-year point", got3, [["2026-03-02", 2.11]])

    print("\ninterbank — SHIBOR and CNH HIBOR")
    r = rd.fetch_interbank(ak, "2026-01")
    check("shibor_3m", r["shibor_3m"][0], [("2026-01-05", 1.88)])
    check("cnh_hibor_on", r["cnh_hibor_on"][0], [("2026-01-05", 1.88)])

    print("\nRRR — keyed on the EFFECTIVE date, not the announcement date")
    r = rd.fetch_rrr(ak, "2015-01")
    check("rrr_large uses 生效时间", r["rrr_large"][0], [("2025-05-15", 9.0)])
    check("rrr_small", r["rrr_small"][0], [("2025-05-15", 6.0)])

    print("\ncentral bank balance sheet — 亿元 converted, both lines extracted")
    r = rd.fetch_central_bank_balance(ak, "2015-01")
    check("govt_deposits_level", r["govt_deposits_level"][0],
          [("2026-06", 5000.0), ("2026-07", 6200.0)])
    check("pboc_claims_odc", r["pboc_claims_odc"][0],
          [("2026-06", 21227.616), ("2026-07", 21848.042)])

    print("\nGDP — nominal growth from like-period YTD levels, deflator as the difference")
    r = rd.fetch_gdp(ak, "2015-01")
    # 695704/660000 - 1 = 5.410%, real 4.7 -> deflator 0.710
    check("nominal_gdp_yoy", r["nominal_gdp_yoy"][0], [["2026-Q2", 5.410]])
    check("gdp_deflator_yoy", r["gdp_deflator_yoy"][0], [["2026-Q2", 0.710]])

    print("\nTSF components — non-government components summed")
    r = rd.fetch_tsf_components(ak, "2015-01")
    flow = dict(r["tsf_ex_govt_flow"][0])
    # 2015-01 components: 14708+212+832+52+1946+1868+526 = 20144 亿元 -> 2014.4 bn
    check("component sum excludes the headline total", flow.get("2015-01"), 2014.4)
    check("note names the components", "人民币贷款" in r["tsf_ex_govt_flow"][2], True)

    print("\nevery fetcher group is registered")
    registered = {s for _, ids in rd.FETCHERS.values() for s in ids}
    for sid in ("m1_yoy", "tsf_flow", "lpr_1y", "dr007", "r007", "dr001", "r001", "cgb_1y",
                "cgb_10y", "ncd_1y_aaa", "shibor_3m", "cnh_hibor_on", "rrr_large",
                "govt_deposits_level", "pboc_claims_odc", "nominal_gdp_yoy",
                "gdp_deflator_yoy", "tsf_ex_govt_yoy", "govt_bond_issuance"):
        check(f"{sid} registered", sid in registered, True)

    print("\nALL PASSED" if not FAILURES else f"\n{len(FAILURES)} FAILURE(S): {FAILURES}")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())
