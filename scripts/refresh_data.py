#!/usr/bin/env python3
"""
Refresh the seed dataset from public sources via akshare.

WHY THIS EXISTS
---------------
The dataset shipped in this repo was assembled inside a sandbox whose egress
policy blocked every macroeconomic data host, so every fetched value came from
third-party GitHub mirrors rather than a primary publisher. This script is the
route back to primary-ish sources for anyone running it on a normal network.

STATUS: the endpoint mapping below is transcribed from research/05-data-sources.md,
which recovered the real endpoint URLs by reading akshare's source. It has NOT been
executed against the live endpoints from this sandbox, because the sandbox cannot
reach them. Treat the first run as a verification exercise: run without --write,
read the report, and confirm the shapes look right before committing anything.

USAGE
-----
    pip install akshare
    python3 scripts/refresh_data.py                  # dry run, reports only
    python3 scripts/refresh_data.py --write          # update data/seed/series.json
    python3 scripts/refresh_data.py --only dr007 r007 --write
    python3 scripts/refresh_data.py --start 2015-01  # history floor (default 2015-01)

Then rebuild the app:
    python3 scripts/build_app_data.py && python3 scripts/make_standalone.py

VERIFIED CONTRACTS
------------------
akshare 1.18.94 was installed and introspected offline (its endpoints are
unreachable from here, but its source is not). Every function below exists,
every signature matches, and the column names are read out of akshare's own
source rather than guessed:

    macro_china_money_supply()  -> 月份, 货币(M1)-同比增长,
                                   货币和准货币(M2)-同比增长,
                                   货币和准货币(M2)-数量(亿元)          [亿元 -> bn]
    macro_china_shrzgm()        -> 月份, 社会融资规模增量                [亿元 -> bn]
    macro_china_lpr()           -> TRADE_DATE, LPR1Y, LPR5Y
    repo_rate_hist(s, e)        -> date, FR001/007/014, FDR001/007/014
                                   *** start and end MUST be within one month ***
    bond_china_yield(s, e)      -> 日期, 3月, 6月, 1年, 3年, 5年, 7年, 10年, 30年
                                   *** window must be under one year ***
    bond_china_close_return(...)-> 日期, 期限, 到期收益率, 即期收益率, 远期收益率
    rate_interbank(...)         -> 报告日, 利率   (symbol "Hibor人民币" == CNH)
    macro_china_reserve_requirement_ratio()
                                -> 生效时间, 大型金融机构-调整后,
                                   中小金融机构-调整后

NOTES ON FIDELITY
-----------------
* FDR007 is NOT DR007 and FR007 is NOT R007. They are the CFETS repo *fixings*,
  which track the underlying weighted rates closely but are a different series.
  They are labelled as proxies in the provenance written out, not silently
  passed off as the real thing.
* `ak.macro_china_shrzgm` reads MOFCOM's republication of the PBoC TSF headline
  and runs two to three months behind the primary release.
* The weighted average lending rate and the excess reserve ratio have no
  machine-readable source at all. They are published only in the quarterly PBoC
  Monetary Policy Report PDF and must be entered by hand.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEED = ROOT / "data" / "seed" / "series.json"

TODAY = date.today().isoformat()
CFETS = "https://www.chinamoney.com.cn"
EASTMONEY = "https://data.eastmoney.com"


def pick(df, *candidates):
    """Resolve a column name robustly. akshare renames columns between releases,
    so never index a DataFrame by a single hard-coded label.

    A candidate is either a string (matched exactly, then as a substring of the
    column) or a tuple of tokens, ALL of which must appear in the column name.
    Token tuples are the durable form: ("M1", "同比") keeps matching whether the
    column is called "货币(M1)-同比增长" or "M1同比增长(%)".
    """
    cols = list(df.columns)
    for c in candidates:                       # exact
        if isinstance(c, str) and c in cols:
            return c
    for c in candidates:                       # all tokens present
        tokens = (c,) if isinstance(c, str) else tuple(c)
        for col in cols:
            if all(t in str(col) for t in tokens):
                return col
    raise KeyError(f"none of {candidates} in {cols}")


def as_month(value) -> str | None:
    """Normalise whatever an endpoint returns for a month into 'YYYY-MM'.

    Every upstream spells this differently and several spell it in ways the
    obvious formats miss. MOFCOM serves bare 'YYYYMM', which is six characters
    and so failed both the strptime list and the len>=7 fallback — that alone
    silently dropped 125 of 136 TSF observations on every refresh. The PBoC
    balance sheet serves '2026.7'. Add a format here rather than a special case
    at each call site.
    """
    s = str(value).strip()
    if " " in s or "T" in s:                      # ISO datetime -> date part
        s = s.replace("T", " ").split(" ", 1)[0]
    for fmt in ("%Y-%m-%d", "%Y%m%d", "%Y-%m", "%Y年%m月份", "%Y年%m月",
                "%Y%m", "%Y.%m", "%Y/%m"):
        try:
            return datetime.strptime(s, fmt).strftime("%Y-%m")
        except ValueError:
            continue
    if len(s) >= 7 and s[4] in "-/年.":
        return s[:4] + "-" + s[5:7].strip("-/.年").zfill(2)
    return None


def as_quarter(value) -> str | None:
    """'2026年第1季度' and '2026年第1-2季度' (cumulative through Q2) -> 'YYYY-Qn'."""
    s = str(value).strip()
    m = re.search(r"(\d{4})\D+?(\d)(?:\s*-\s*(\d))?\s*季度", s)
    if not m:
        return None
    year, first, last = m.group(1), int(m.group(2)), m.group(3)
    return f"{year}-Q{int(last) if last else first}"


def as_day(value) -> str | None:
    """Normalise a date. East Money serves ISO datetimes ("2025-05-15 00:00:00")
    and akshare does not convert 生效时间 at all, so the trailing time component
    reached us intact — that alone made the entire RRR fetch return nothing."""
    s = str(value).strip()
    if " " in s or "T" in s:                      # ISO datetime -> date part
        s = s.replace("T", " ").split(" ", 1)[0]
    s = s.replace("年", "-").replace("月", "-").replace("日", "")
    for fmt in ("%Y-%m-%d", "%Y%m%d", "%Y/%m/%d"):
        try:
            return datetime.strptime(s, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return None


def monthly(df, datecol, valcol, scale=1.0):
    out = []
    for _, row in df.iterrows():
        m = as_month(row[datecol])
        v = row[valcol]
        if m is None or v is None:
            continue
        try:
            num = float(v) * scale
        except (TypeError, ValueError):
            continue
        if not math.isfinite(num):        # upstream sends NaN for missing points
            continue
        out.append([m, round(num, 4)])
    return sorted({m: v for m, v in out}.items())


def daily(df, datecol, valcol):
    out = []
    for _, row in df.iterrows():
        d = as_day(row[datecol])
        v = row[valcol]
        if d is None or v is None:
            continue
        try:
            num = float(v)
        except (TypeError, ValueError):
            continue
        if not math.isfinite(num):        # upstream sends NaN for missing points
            continue
        out.append([d, round(num, 4)])
    return sorted({d: v for d, v in out}.items())


# --------------------------------------------------------------- fetchers ---
# Each returns {series_id: (observations, provenance, notes)}.

def fetch_money_supply(ak, start):
    df = ak.macro_china_money_supply()
    dcol = pick(df, "月份", "统计时间", "date")
    prov = {"source_name": "PBoC money & credit statistics via akshare (East Money mirror)",
            "source_url": f"{EASTMONEY}/cjsj/hbgyl.html",
            "retrieved": TODAY, "confidence": "partial"}
    out = {}
    for sid, *names in [
        ("m1_yoy", "货币(M1)-同比增长", ("M1", "同比")),
        ("m2_yoy", "货币和准货币(M2)-同比增长", ("M2", "同比")),
        ("m2_level", "货币和准货币(M2)-数量(亿元)", ("M2", "数量")),
    ]:
        try:
            col = pick(df, *names)
        except KeyError as e:
            print(f"    skip {sid}: {e}")
            continue
        scale = 0.1 if sid == "m2_level" else 1.0   # 亿元 -> RMB bn
        obs = [o for o in monthly(df, dcol, col, scale) if o[0] >= start]
        note = ("Converted from 100mn RMB to RMB bn." if sid == "m2_level" else
                "M1 was redefined in January 2025; pre- and post-2025 values are different aggregates."
                if sid == "m1_yoy" else None)
        out[sid] = (obs, prov, note)
    return out


def fetch_tsf(ak, start):
    df = ak.macro_china_shrzgm()
    dcol = pick(df, "月份", "date")
    vcol = pick(df, "社会融资规模增量", "当月值")
    prov = {"source_name": "PBoC TSF increment via akshare (MOFCOM republication)",
            "source_url": "https://data.mofcom.gov.cn/gnmy/shrzgm.shtml",
            "retrieved": TODAY, "confidence": "partial"}
    obs = [o for o in monthly(df, dcol, vcol, 0.1) if o[0] >= start]   # 亿元 -> bn
    return {"tsf_flow": (obs, prov,
                         "MOFCOM republishes the PBoC headline two to three months late. "
                         "Converted from 100mn RMB to RMB bn.")}


def fetch_lpr(ak, start):
    df = ak.macro_china_lpr()
    dcol = pick(df, "TRADE_DATE", "日期", "date")
    prov = {"source_name": "NIFC loan prime rate fixing via akshare",
            "source_url": "https://www.chinamoney.com.cn/english/bmklpr/",
            "retrieved": TODAY, "confidence": "partial"}
    out = {}
    for sid, *names in [("lpr_1y", "LPR1Y", "LPR_1Y", ("1年", "LPR"), "1年期"),
                        ("lpr_5y", "LPR5Y", "LPR_5Y", ("5年", "LPR"), "5年期")]:
        try:
            col = pick(df, *names)
        except KeyError as e:
            print(f"    skip {sid}: {e}")
            continue
        obs = [o for o in monthly(df, dcol, col) if o[0] >= start]
        out[sid] = (obs, prov, "Monthly fixing, published on the 20th.")
    return out


def _month_spans(start: str):
    """Yield (YYYYMMDD, YYYYMMDD) pairs, one calendar month at a time."""
    y, m = int(start[:4]), int(start[5:7])
    today = date.today()
    while (y, m) <= (today.year, today.month):
        last = 31
        while True:
            try:
                end = date(y, m, last); break
            except ValueError:
                last -= 1
        yield f"{y}{m:02d}01", end.strftime("%Y%m%d")
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


def fetch_repo_fixings(ak, start):
    # chinamoney's FrrHis endpoint requires start and end inside ONE calendar
    # month ("开始时间与结束时间需要在一个月内" in akshare's own docstring), so a
    # single multi-year call silently returns nothing. Walk it month by month.
    import pandas as pd
    frames = []
    for s_, e_ in _month_spans(start):
        try:
            frames.append(ak.repo_rate_hist(start_date=s_, end_date=e_))
        except Exception as e:                        # noqa: BLE001
            print(f"    repo {s_[:6]}: {e}")
    if not frames:
        return {}
    df = pd.concat(frames, ignore_index=True)
    dcol = pick(df, "date", "日期")
    prov = {"source_name": "CFETS repo fixing history (FrrHis) via akshare",
            "source_url": f"{CFETS}/ags/ms/cm-u-bk-currency/FrrHis",
            "retrieved": TODAY, "confidence": "partial"}
    out = {}
    # FDR001/FR001 arrive in the same response as the 7-day fixings and were
    # being discarded. The overnight tenor is now the PBoC's declared operating
    # anchor (Q1 2026 MPR), so DR001 matters more than DR007 going forward.
    for sid, col, real in [("dr007", "FDR007", "DR007"), ("r007", "FR007", "R007"),
                           ("dr001", "FDR001", "DR001"), ("r001", "FR001", "R001")]:
        try:
            c = pick(df, col)
        except KeyError as e:
            print(f"    skip {sid}: {e}")
            continue
        out[sid] = (daily(df, dcol, c), prov,
                    f"PROXY: this is the CFETS {col} fixing, not {real} itself. The two track "
                    f"closely but are distinct series. Replace with the true weighted rate from "
                    f"CFETS pledged-repo data before relying on the level.")
    return out


def fetch_cgb_curve(ak, start):
    """ChinaBond only serves windows of a year or less, so walk it."""
    import pandas as pd
    frames, year = [], int(start[:4])
    while year <= date.today().year:
        try:
            frames.append(ak.bond_china_yield(start_date=f"{year}0101",
                                              end_date=f"{year}1231"))
        except Exception as e:                        # noqa: BLE001
            print(f"    cgb {year}: {e}")
        year += 1
    if not frames:
        return {}
    df = pd.concat(frames, ignore_index=True)
    if "曲线名称" in df.columns:
        df = df[df["曲线名称"].astype(str).str.contains("国债")]
    dcol = pick(df, "日期", "date")
    prov = {"source_name": "ChinaBond government bond yield curve via akshare",
            "source_url": "https://yield.chinabond.com.cn/",
            "retrieved": TODAY, "confidence": "partial"}
    out = {}
    for sid, *names in [("cgb_1y", "1年", "1Y"), ("cgb_3y", "3年", "3Y"),
                        ("cgb_10y", "10年", "10Y")]:
        # "1年" is a substring of "10年 " in some layouts, so exact match must win;
        # pick() tries exact first, which is why 10y resolves correctly.
        try:
            col = pick(df, *names)
        except KeyError as e:
            print(f"    skip {sid}: {e}")
            continue
        out[sid] = (daily(df, dcol, col), prov, "ChinaBond closing yield curve, maturity point.")
    return out


def _ncd_records(symbol_code, s_, e_, term="1"):
    """Call the CFETS closing-curve endpoint directly, for ONE tenor.

    Two things about this endpoint bite.

    First, akshare's wrapper does `del temp_df["newDateValue"]` and then assigns
    column names positionally. Upstream stopped returning that key, so the
    wrapper raises KeyError and the series vanishes from the refresh entirely.
    This issues the same request but tolerates the key being present or absent.

    Second — and this one shipped wrong numbers — `termId` does NOT filter the
    response. CFETS returns the WHOLE curve for every date in the window, about
    nineteen tenors a day, ordered newest-first. Reading a yield out of each
    record without checking its tenor therefore collects whichever tenors happen
    to land in the page: the stored "3-year AA+ note yield" was in fact the
    15-year point on some dates and the 5-year on others. Nothing about the
    output looked wrong, because every value was a real yield off a real curve.

    So the tenor is matched against the response, not requested and assumed, and
    pageSize is raised past one month of full curves (19 tenors x ~22 trading
    days) so the window is not silently truncated.
    """
    import requests
    want = float(term)
    r = requests.get(
        "https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/ClsYldCurvHis",
        params={"lang": "CN", "reference": "1,2,3", "bondType": symbol_code,
                "startDate": f"{s_[:4]}-{s_[4:6]}-{s_[6:]}",
                "endDate": f"{e_[:4]}-{e_[4:6]}-{e_[6:]}",
                "termId": term, "pageNum": "1", "pageSize": "1000"},
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                               "AppleWebKit/537.36 (KHTML, like Gecko) "
                               "Chrome/108.0.0.0 Safari/537.36"},
        timeout=30)
    r.raise_for_status()
    records = (r.json() or {}).get("records") or []
    out, seen_terms, matched = [], set(), 0
    for rec in records:
        # Read by NAME. The positional read that was here before depended on
        # dict ordering surviving an upstream schema change, which is exactly
        # the assumption that broke.
        day = as_day(rec.get("newDateValueCN") or rec.get("newDateValue"))
        if day is None:
            continue
        try:
            got = float(rec.get("yearTermStr"))
        except (TypeError, ValueError):
            continue
        seen_terms.add(got)
        if abs(got - want) > 1e-6:
            continue
        matched += 1
        try:
            num = float(rec.get("maturityYieldStr"))
        except (TypeError, ValueError):
            continue                                # "---" on illiquid points
        if math.isfinite(num):
            out.append([day, round(num, 4)])
    if records and not out:
        # The window had data but produced nothing. Silence here is how the
        # wrong-tenor values got in, so distinguish the two reasons: the tenor
        # was absent, or it was there and every yield was unquotable.
        if matched:
            print(f"    curve {symbol_code}: {matched} record(s) at term {want} in "
                  f"{s_[:6]}, but no quotable yield on any of them")
        else:
            print(f"    curve {symbol_code}: {len(records)} records in {s_[:6]} but none "
                  f"at term {want}; tenors present: {sorted(seen_terms)[:12]}")
    return out


def fetch_ncd(ak, start):
    # This endpoint also caps a request at one calendar month
    # ("结束日期和开始日期不要超过 1 个月" in akshare's docstring), so it has to be
    # walked rather than asked for a multi-year span.
    try:
        name_code = ak.bond_china_close_return_map()
        code = name_code[name_code["cnLabel"] == "同业存单(AAA)"]["value"].values[0]
    except Exception as e:                         # noqa: BLE001
        print(f"    skip ncd_1y_aaa: could not resolve the curve code ({e})")
        return {}
    obs, failures = [], 0
    for s_, e_ in _month_spans(start):
        try:
            obs.extend(_ncd_records(code, s_, e_))
        except Exception as e:                     # noqa: BLE001
            failures += 1
            if failures <= 3:
                print(f"    ncd {s_[:6]}: {e}")
    if failures:
        print(f"    ncd: {failures} month window(s) failed")
    if not obs:
        return {}
    merged = sorted({d: v for d, v in obs}.items())
    prov = {"source_name": "CFETS closing yield curve, AAA NCD (ClsYldCurvHis), called directly",
            "source_url": "https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/ClsYldCurvHis",
            "retrieved": TODAY, "confidence": "partial"}
    return {"ncd_1y_aaa": ([[d, v] for d, v in merged], prov,
                           "1-year point of the AAA negotiable CD curve. Fetched by calling "
                           "CFETS directly rather than through akshare, whose wrapper breaks "
                           "on the current response schema.")}


def fetch_rrr(ak, start):
    df = ak.macro_china_reserve_requirement_ratio()
    dcol = pick(df, "生效时间", ("生效",))
    prov = {"source_name": "PBoC reserve requirement ratio changes via akshare (East Money)",
            "source_url": "https://data.eastmoney.com/cjsj/ckzbj.html",
            "retrieved": TODAY, "confidence": "partial"}
    out = {}
    for sid, *names in [("rrr_large", "大型金融机构-调整后", ("大型", "调整后")),
                        ("rrr_small", "中小金融机构-调整后", ("中小", "调整后"))]:
        try:
            col = pick(df, *names)
        except KeyError as e:
            print(f"    skip {sid}: {e}")
            continue
        obs = daily(df, dcol, col)
        if not obs:
            print(f"    {sid}: no observations parsed from {dcol!r}/{col!r}")
            continue
        out[sid] = (obs, prov,
                    "Step series keyed on the EFFECTIVE date (生效时间), not the announcement "
                    "date. akshare leaves that column as an ISO datetime string. Reconcile "
                    "against PBoC announcements before relying on it.")
    return out


def fetch_interbank(ak, start):
    out = {}
    for sid, market, symbol, indicator, name in [
        ("shibor_3m", "上海银行同业拆借市场", "Shibor人民币", "3月", "SHIBOR 3M"),
        ("cnh_hibor_on", "香港银行同业拆借市场", "Hibor人民币", "隔夜", "CNH HIBOR overnight"),
    ]:
        try:
            df = ak.rate_interbank(market=market, symbol=symbol, indicator=indicator)
            dcol = pick(df, "报告日", "日期", "date")
            vcol = pick(df, "利率", "利率(%)", "value")
            out[sid] = (daily(df, dcol, vcol),
                        {"source_name": f"{name} via akshare (East Money)",
                         "source_url": "https://datacenter-web.eastmoney.com/api/data/v1/get",
                         "retrieved": TODAY, "confidence": "partial"}, None)
        except Exception as e:                        # noqa: BLE001
            print(f"    skip {sid}: {e}")
    return out


def fetch_central_bank_balance(ak, start):
    """PBoC monetary authority balance sheet.

    Two things the tracker wants live here. 政府存款 is the Treasury Single
    Account — the single largest autonomous drain on bank reserves. And
    对其他存款性公司债权 (claims on other depository corporations) is the STOCK of
    all PBoC lending to banks: open market operations, MLF, PSL and outright
    reverse repo together. Its change is net liquidity injection, which is far
    more robust than scraping daily operation announcements and summing them.
    """
    df = ak.macro_china_central_bank_balance()
    dcol = pick(df, "统计时间", ("统计",), "月份")
    prov = {"source_name": "PBoC monetary authority balance sheet via akshare (Sina)",
            "source_url": "http://www.pbc.gov.cn/diaochatongjisi/116219/116319/index.html",
            "retrieved": TODAY, "confidence": "partial"}
    out = {}
    for sid, names, note in [
        ("govt_deposits_level", ("政府存款", ("政府", "存款")),
         "Treasury Single Account balance. Converted from 100mn RMB to RMB bn. "
         "The month-on-month change is the drain on (or injection into) bank reserves."),
        ("pboc_claims_odc", ("对其他存款性公司债权", ("其他存款性公司",)),
         "Stock of PBoC lending to banks — OMO, MLF, PSL and outright reverse repo "
         "combined. Converted from 100mn RMB to RMB bn. Changes in this stock are net "
         "liquidity injection."),
    ]:
        try:
            col = pick(df, *names)
        except KeyError as e:
            print(f"    skip {sid}: {e}")
            continue
        obs = [o for o in monthly(df, dcol, col, 0.1) if o[0] >= start]
        if obs:
            out[sid] = (obs, prov, note)
    return out


def fetch_gdp(ak, start):
    """Nominal GDP growth and the GDP deflator, from one consistent vintage.

    Neither could be built before. The absolute figures are cumulative
    year-to-date in current prices and the growth column is real, so nominal
    growth comes from comparing like periods a year apart and the deflator is
    the difference between the two. Taking both legs from the same publisher in
    the same request is what avoids the vintage mismatch that made the earlier
    hand-assembled attempt produce a 2.8pp phantom jump across the 2024 census
    revision.
    """
    df = ak.macro_china_gdp()
    qcol = pick(df, "季度", ("季度",))
    lvl = pick(df, "国内生产总值-绝对值", ("国内生产总值", "绝对值"))
    real = pick(df, "国内生产总值-同比增长", ("国内生产总值", "同比"))
    levels, reals = {}, {}
    for _, row in df.iterrows():
        q = as_quarter(row[qcol])
        if q is None:
            continue
        try:
            levels[q] = float(row[lvl])
        except (TypeError, ValueError):
            pass
        try:
            reals[q] = float(row[real])
        except (TypeError, ValueError):
            pass
    prov = {"source_name": "NBS quarterly GDP via akshare (East Money)",
            "source_url": "https://data.eastmoney.com/cjsj/gdp.html",
            "retrieved": TODAY, "confidence": "partial"}
    nominal, deflator = [], []
    for q, v in sorted(levels.items()):
        year, qn = q.split("-Q")
        prior = f"{int(year) - 1}-Q{qn}"
        if prior not in levels or not levels[prior] or not math.isfinite(v):
            continue
        ny = (v / levels[prior] - 1) * 100
        if q >= start[:4]:
            nominal.append([q, round(ny, 3)])
            if q in reals and math.isfinite(reals[q]):
                deflator.append([q, round(ny - reals[q], 3)])
    out = {}
    if nominal:
        out["nominal_gdp_yoy"] = (nominal, prov,
            "Cumulative year-to-date nominal growth, computed by comparing like "
            "year-to-date periods a year apart. Pairs correctly with the cumulative "
            "real growth rate the same source publishes.")
    if deflator:
        out["gdp_deflator_yoy"] = (deflator, prov,
            "Nominal minus real cumulative growth, both legs from the same publisher "
            "and the same request, so the series does not straddle data vintages.")
    return out


def fetch_tsf_components(ak, start):
    """Total social financing excluding government bonds.

    The PBoC does not publish this directly and the component table carries no
    government-bond line, but every component it DOES break out is non-government
    credit. Summing them gives private-sector financing — the series that
    actually maps to demand, and the one headline TSF has been masking while
    government bond issuance carried it.
    """
    df = ak.macro_china_shrzgm()
    dcol = pick(df, "月份", ("月份",))
    parts = [c for c in df.columns if str(c).startswith("其中-")]
    if not parts:
        print("    skip tsf_ex_govt: no 其中- component columns present")
        return {}
    flow = {}
    for _, row in df.iterrows():
        m = as_month(row[dcol])
        if m is None:
            continue
        total = 0.0
        seen = False
        for c in parts:
            try:
                v = float(row[c])
            except (TypeError, ValueError):
                continue
            if math.isfinite(v):
                total += v
                seen = True
        if seen:
            flow[m] = total * 0.1                  # 亿元 -> RMB bn
    if not flow:
        return {}
    prov = {"source_name": "PBoC TSF components via akshare (MOFCOM republication)",
            "source_url": "https://data.mofcom.gov.cn/gnmy/shrzgm.shtml",
            "retrieved": TODAY, "confidence": "partial"}
    note = ("Sum of every non-government component the PBoC breaks out: RMB and FX loans, "
            "entrusted and trust loans, undiscounted bankers' acceptances, corporate bonds "
            "and domestic equity financing. It is a construction, not a published series — "
            "small items outside the published breakdown (ABS, loan write-offs) are excluded. "
            "Components: " + ", ".join(str(c) for c in parts))
    months = sorted(flow)
    out = {"tsf_ex_govt_flow": ([[m, round(flow[m], 2)] for m in months if m >= start],
                                prov, note)}
    # year-on-year growth of the trailing 12-month sum
    roll, yoy = {}, []
    for i, m in enumerate(months):
        if i >= 11:
            roll[m] = sum(flow[x] for x in months[i - 11:i + 1])
    for m in sorted(roll):
        prior = f"{int(m[:4]) - 1}{m[4:]}"
        if prior in roll and roll[prior]:
            v = (roll[m] / roll[prior] - 1) * 100
            if m >= start:
                yoy.append([m, round(v, 3)])
    if yoy:
        out["tsf_ex_govt_yoy"] = (yoy, prov,
            note + " Expressed as the year-on-year change in the trailing 12-month sum.")
    return out


def fetch_govt_bond_issuance(ak, start):
    """Monthly government bond issuance: treasury plus local government.

    GROSS issuance, not net — redemptions are not in this source, so this
    overstates the reserve drain. Still the best available read on the supply
    calendar banks have to absorb.
    """
    import pandas as pd
    frames = []
    for fn in ("bond_treasure_issue_cninfo", "bond_local_government_issue_cninfo"):
        f = getattr(ak, fn, None)
        if f is None:
            print(f"    skip {fn}: not in akshare")
            continue
        for year in range(max(2015, int(start[:4])), date.today().year + 1):
            try:
                frames.append(f(start_date=f"{year}0101", end_date=f"{year}1231"))
            except Exception as e:                 # noqa: BLE001
                print(f"    {fn} {year}: {e}")
    if not frames:
        return {}
    df = pd.concat(frames, ignore_index=True)
    try:
        dcol = pick(df, "发行起始日", ("发行", "日"))
        vcol = pick(df, "实际发行总量", ("实际发行",), "计划发行总量")
    except KeyError as e:
        print(f"    skip govt_bond_issuance: {e}")
        return {}
    buckets = {}
    for _, row in df.iterrows():
        m = as_month(row[dcol])
        if m is None:
            continue
        try:
            v = float(row[vcol])
        except (TypeError, ValueError):
            continue
        if math.isfinite(v):
            buckets[m] = buckets.get(m, 0.0) + v * 0.1     # 亿元 -> RMB bn
    obs = [[m, round(v, 2)] for m, v in sorted(buckets.items()) if m >= start]
    if not obs:
        return {}
    return {"govt_bond_issuance": (obs,
            {"source_name": "Treasury and local government bond issuance via akshare (CNINFO)",
             "source_url": "https://www.cninfo.com.cn/",
             "retrieved": TODAY, "confidence": "partial"},
            "GROSS issuance summed by issue start date — central treasury plus local "
            "government bonds. Redemptions are not in this source, so it overstates the "
            "net drain on bank reserves. Converted from 100mn RMB to RMB bn.")}


def fetch_credit_spread(ak, start):
    """3-year AA+ medium-term note yield, for the spread over CGB.

    The curve code is resolved by matching the published label rather than
    hard-coded: CFETS publishes 75 curves and renames them, so the fetcher
    searches the map itself and logs what it matched. If nothing matches it says
    so and returns nothing, rather than silently fetching the wrong curve.
    """
    try:
        name_code = ak.bond_china_close_return_map()
    except Exception as e:                         # noqa: BLE001
        print(f"    skip credit_spread_aa: curve map unavailable ({e})")
        return {}
    labels = {str(r["cnLabel"]): str(r["value"]) for _, r in name_code.iterrows()}
    # Preference order: the plain medium-term note curve at AA+, then AA, then
    # the enterprise-bond equivalent. Floating-rate spread curves are excluded —
    # they are point spreads, not yields.
    # The rating must be matched as a WHOLE parenthesised token. Matching "AA+"
    # as a loose substring silently selects 中短期票据(AAA+) — a higher credit
    # tier — and understates the spread. That is what the first live run did.
    def find(instrument: str, rating: str):
        token = f"({rating})"
        for lbl, val in labels.items():
            if (instrument in lbl and token in lbl
                    and "浮动" not in lbl and "点差" not in lbl):
                return val, lbl
        return None, None

    code = label = None
    for instrument, rating in (("中短期票据", "AA+"), ("中期票据", "AA+"),
                               ("中短期票据", "AA"), ("企业债", "AA+")):
        code, label = find(instrument, rating)
        if code:
            break
    if not code:
        print(f"    skip credit_spread_aa: no matching curve among {len(labels)} published. "
              f"Labels containing 票据: "
              f"{[l for l in labels if '票据' in l][:8]}")
        return {}
    print(f"    credit_spread_aa: matched curve {code} = {label}")
    obs, failures = [], 0
    for s_, e_ in _month_spans(start):
        try:
            obs.extend(_ncd_records(code, s_, e_, term="3"))
        except Exception as e:                     # noqa: BLE001
            failures += 1
            if failures <= 3:
                print(f"    mtn {s_[:6]}: {e}")
    if not obs:
        return {}
    merged = sorted({d: v for d, v in obs}.items())
    return {"mtn_aa_3y": ([[d, v] for d, v in merged],
            {"source_name": f"CFETS closing yield curve, {label} (ClsYldCurvHis), called directly",
             "source_url": "https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/ClsYldCurvHis",
             "retrieved": TODAY, "confidence": "partial"},
            f"3-year point of the {label} curve, resolved by label match against the published "
            f"curve map (code {code}). The spread over the 3-year CGB is the credit-risk premium.")}


def fetch_loan_direction(ak, start):
    """Corporate medium-and-long-term loans, from the quarterly 贷款投向 report.

    There is no API. The numbers sit in running prose, and the report states
    SIX different 中长期贷款余额 figures in one article — all loans, industry,
    heavy and light industry, services, property, infrastructure. Reading the
    first number that follows the phrase picks up whichever section comes
    first, which is not the corporate one.

    What disambiguates them is the section. Section 一 is 企事业单位贷款, and
    inside it the maturity split appears under 分期限看. Verified verbatim
    against 2025 Q3:

        一、企事业单位贷款增长较为平稳 ... 本外币企事业单位贷款余额184.3万亿元,
        同比增长8.2% ... 分期限看, 短期贷款及票据融资余额62.77万亿元 ...
        中长期贷款余额117.89万亿元, 同比增长7.8% ...

    So the parser anchors on the section heading and takes the 中长期 figure
    from inside it, and cross-checks that short-term plus medium-and-long-term
    does not exceed the corporate total it is supposed to decompose.
    """
    import requests
    hdr = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"}

    def text_of(url):
        r = requests.get(url, headers=hdr, timeout=40)
        r.raise_for_status()
        r.encoding = r.apparent_encoding or "utf-8"
        t = re.sub(r"<[^>]+>", "", r.text)
        return re.sub(r"[ \t\r\n\u3000]+", "", t)

    # Enumerate the 新闻发布 column. Paginated as index.html, index_1.html, ...
    base = "https://www.pbc.gov.cn/goutongjiaoliu/113456/113469"
    seen, articles = set(), []
    for page in range(0, 12):
        url = f"{base}/index.html" if page == 0 else f"{base}/index_{page}.html"
        try:
            r = requests.get(url, headers=hdr, timeout=40)
            if r.status_code != 200:
                break
            r.encoding = r.apparent_encoding or "utf-8"
        except Exception as e:                        # noqa: BLE001
            print(f"    loan_direction: list page {page} failed ({e})")
            break
        for href in re.findall(r'href="(/goutongjiaoliu/113456/113469/[^"]+/index\.html)"', r.text):
            if href not in seen:
                seen.add(href)
                articles.append("https://www.pbc.gov.cn" + href)
    print(f"    loan_direction: {len(articles)} candidate articles")

    obs_bal, obs_yoy, hits = [], [], 0
    for url in articles:
        try:
            t = text_of(url)
        except Exception:                             # noqa: BLE001
            continue
        if "贷款投向统计报告" not in t:
            continue
        hits += 1
        # Section 一 runs to the 二、 heading.
        sec = re.search(r"一、企[事业]*单位贷款.{0,900}?(?=二、)", t)
        if not sec:
            continue
        body = sec.group(0)
        q = re.search(r"(20\d\d)年([一二三四])季度末|(20\d\d)年末", body)
        mlt = re.search(r"中长期贷款余额([\d.]+)万亿元[，,]同比增长([\d.]+)%", body)
        if not (q and mlt):
            continue
        if q.group(3):                                # 「2023年末」 = Q4
            period = f"{q.group(3)}-Q4"
        else:
            period = f"{q.group(1)}-Q{'一二三四'.index(q.group(2)) + 1}"
        level, yoy = float(mlt.group(1)), float(mlt.group(2))
        # Cross-check: the maturity split must decompose the corporate total.
        tot = re.search(r"企[事业]*单位贷款余额([\d.]+)万亿元", body)
        sht = re.search(r"短期贷款及票据融资余额([\d.]+)万亿元", body)
        if tot and sht and level + float(sht.group(1)) > float(tot.group(1)) * 1.02:
            print(f"    loan_direction {period}: {level}+{sht.group(1)} exceeds the "
                  f"corporate total {tot.group(1)} — section parse is wrong, dropped")
            continue
        obs_bal.append([period, round(level, 3)])
        obs_yoy.append([period, round(yoy, 2)])

    print(f"    loan_direction: {hits} 贷款投向 reports, {len(obs_yoy)} parsed")
    if not obs_yoy:
        return {}
    prov = {"source_name": "PBoC 金融机构贷款投向统计报告 (quarterly)",
            "source_url": f"{base}/index.html",
            "retrieved": TODAY, "confidence": "partial"}
    note = ("Read from section 一 (企事业单位贷款) of the quarterly loan-direction report, "
            "under 分期限看. The report states six different 中长期贷款余额 figures — this "
            "is the corporate one, not the all-loans one. 本外币 (local and foreign "
            "currency). Cross-checked so that short-term plus medium-and-long-term does "
            "not exceed the corporate total.")
    return {
        "corp_mlt_loans_yoy": (sorted(obs_yoy), prov, note),
        "corp_mlt_loans_level": (sorted(obs_bal), prov, note + " Balance in RMB trn."),
    }


def fetch_cfets_index(ak, start):
    """The CFETS trade-weighted renminbi index.

    akshare's route for this is broken upstream. CFETS serves it as JSON at
    cm-u-bk-fx/RmbIdxHis — found by probing, since the endpoint appears nowhere
    in the page source or in any public code search.

    ONE IMPORTANT LIMIT, established by probing rather than assumed: the
    endpoint ignores date parameters. Nine spellings of startDate/endDate/
    pageSize and six sibling route names all returned the same rolling
    ~one-year window of ~54 weekly records. So this backfills one year and
    extends forward from there as the weekly refresh accumulates; it cannot
    reach 2015. The extend-only merge in build_app_data.py is what makes that
    accumulation safe.
    """
    import requests
    url = "https://www.chinamoney.com.cn/ags/ms/cm-u-bk-fx/RmbIdxHis"
    try:
        r = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
            "Referer": "https://www.chinamoney.com.cn/chinese/bkrmbidx/"},
            timeout=40)
        r.raise_for_status()
        records = (r.json() or {}).get("records") or []
    except Exception as e:                            # noqa: BLE001
        print(f"    skip cfets: {e}")
        return {}
    if not records:
        print("    skip cfets: endpoint returned no records")
        return {}

    # The value key is taken from a known set rather than guessed at runtime. A
    # heuristic like "the first field that looks like an index level" is
    # exactly how a plausible-but-wrong number gets in; if the schema moves,
    # this says so and returns nothing.
    # Confirmed against the live response, whose record is:
    #   {"showDate","showDateEn","cfetsIndexRateStr","cfetsIndexRate",
    #    "bisIndexRateStr","bisIndexRate","sdrIndexRateStr","sdrIndexRate"}
    # The same record also carries the BIS-basket and SDR-basket indices, which
    # are separate indicators and deliberately not folded in here.
    VALUE_KEYS = ("cfetsIndexRate", "cfetsIndexRateStr", "cfetsIdx", "cfetsIndex")
    DATE_KEYS = ("showDate", "date", "showDateCN")
    sample = records[0]
    vkey = next((k for k in VALUE_KEYS if k in sample), None)
    dkey = next((k for k in DATE_KEYS if k in sample), None)
    if not (vkey and dkey):
        print(f"    skip cfets: unrecognised record schema. Keys: {list(sample)}")
        return {}

    obs = {}
    for rec in records:
        d = as_day(rec.get(dkey))
        if d is None:
            continue
        try:
            v = float(str(rec.get(vkey)).replace(",", ""))
        except (TypeError, ValueError):
            continue
        # The index is based at 2014-12-31 = 100 and has traded roughly 90-110.
        # Anything far outside that is a different field, not a shock.
        if math.isfinite(v) and 50.0 < v < 200.0:
            obs[d] = round(v, 4)
    if not obs:
        print(f"    skip cfets: no plausible values from key {vkey!r}")
        return {}
    print(f"    cfets: {len(obs)} weekly observations, {min(obs)} .. {max(obs)}")
    return {"cfets": ([[d, v] for d, v in sorted(obs.items())],
            {"source_name": "CFETS RMB exchange-rate index (中国外汇交易中心)",
             "source_url": "https://www.chinamoney.com.cn/chinese/bkrmbidx/",
             "retrieved": TODAY, "confidence": "partial"},
            "CFETS trade-weighted renminbi index, 2014-12-31 = 100, published weekly "
            "on the first trading day for the previous Friday. The endpoint serves only "
            "a rolling one-year window, so history accumulates forward from first fetch "
            "rather than reaching back. Basket weights are reset by announcement "
            "periodically — most recently effective 2026-01-01 — so the level is "
            "continuous but the composition is not.")}


FETCHERS = {
    "money":     (fetch_money_supply, ["m1_yoy", "m2_yoy", "m2_level"]),
    "tsf":       (fetch_tsf,          ["tsf_flow"]),
    "lpr":       (fetch_lpr,          ["lpr_1y", "lpr_5y"]),
    "repo":      (fetch_repo_fixings, ["dr007", "r007", "dr001", "r001"]),
    "cgb":       (fetch_cgb_curve,    ["cgb_1y", "cgb_3y", "cgb_10y"]),
    "ncd":       (fetch_ncd,          ["ncd_1y_aaa"]),
    "interbank": (fetch_interbank,    ["shibor_3m", "cnh_hibor_on"]),
    "rrr":       (fetch_rrr,          ["rrr_large", "rrr_small"]),
    "cbbs":      (fetch_central_bank_balance, ["govt_deposits_level", "pboc_claims_odc"]),
    "gdp":       (fetch_gdp,          ["nominal_gdp_yoy", "gdp_deflator_yoy"]),
    "tsfparts":  (fetch_tsf_components, ["tsf_ex_govt_flow", "tsf_ex_govt_yoy"]),
    "govtbonds": (fetch_govt_bond_issuance, ["govt_bond_issuance"]),
    "creditspread": (fetch_credit_spread, ["mtn_aa_3y"]),
    "loandirection": (fetch_loan_direction,
                      ["corp_mlt_loans_yoy", "corp_mlt_loans_level"]),
    "cfets":     (fetch_cfets_index,  ["cfets"]),
}

MANUAL_ONLY = {
    "walr_general": "PBoC Monetary Policy Report PDF only — no machine-readable source exists.",
    "excess_reserve_ratio": "PBoC Monetary Policy Report PDF only — no machine-readable source exists.",
    "omo_7d": "PBoC open market operation announcements; maintained in analyst_supplied.json.",
    "mlf_1y": "PBoC announcements; no single rate exists after the March 2025 move to multi-price bidding.",
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true",
                    help="update data/seed/series.json (default: report only)")
    ap.add_argument("--only", nargs="*", metavar="ID",
                    help="restrict to these series ids")
    ap.add_argument("--start", default="2015-01", metavar="YYYY-MM",
                    help="earliest month to keep (default 2015-01)")
    args = ap.parse_args()

    try:
        import akshare as ak
    except ImportError:
        print("akshare is not installed.  pip install akshare", file=sys.stderr)
        return 1

    print(f"akshare {getattr(ak, '__version__', '?')} · history floor {args.start}")
    if not args.write:
        print("DRY RUN — nothing will be written. Re-run with --write to apply.\n")

    seed = json.loads(SEED.read_text(encoding="utf-8")) if SEED.exists() else {"meta": {}, "series": {}}
    existing = seed.setdefault("series", {})
    fetched, failed = {}, []

    for group, (fn, ids) in FETCHERS.items():
        if args.only and not set(ids) & set(args.only):
            continue
        print(f"[{group}]")
        try:
            result = fn(ak, args.start)
        except Exception as e:                        # noqa: BLE001
            print(f"    FAILED: {type(e).__name__}: {e}")
            failed.append(group)
            continue
        for sid, (obs, prov, note) in result.items():
            if args.only and sid not in args.only:
                continue
            if not obs:
                print(f"    {sid}: no observations returned")
                continue
            was = len(existing.get(sid, {}).get("observations", []))
            print(f"    {sid}: {len(obs)} obs  {obs[0][0]} .. {obs[-1][0]}  (had {was})")
            fetched[sid] = (obs, prov, note)

    print(f"\n{len(fetched)} series fetched, {len(failed)} group(s) failed")
    print("\nNot fetchable by any script — maintain these by hand:")
    for sid, why in MANUAL_ONLY.items():
        print(f"    {sid}: {why}")

    if not args.write:
        return 0
    if not fetched:
        print("\nnothing to write")
        return 1

    backup = SEED.with_suffix(".json.bak")
    if SEED.exists():
        shutil.copy2(SEED, backup)
        print(f"\nbacked up -> {backup.relative_to(ROOT)}")

    for sid, (obs, prov, note) in fetched.items():
        entry = existing.setdefault(sid, {})
        # Union rather than replace. Upstream windows move — MOFCOM's TSF mirror
        # in particular serves a rolling window — so overwriting wholesale silently
        # truncates history that was previously fetched. Newer values win on dates
        # both cover, since those are genuine revisions.
        prior = {d: v for d, v in entry.get("observations", []) if v is not None}
        merged = {**prior, **{d: v for d, v in obs}}
        kept = len(prior) - len(set(prior) & set(d for d, _ in obs))
        entry["observations"] = [[d, v] for d, v in sorted(merged.items())]
        if len(merged) > len(obs):
            print(f"    {sid}: kept {kept} earlier observation(s) upstream no longer returns "
                  f"({len(obs)} fetched -> {len(merged)} total)")
        entry["provenance"] = prov
        if note:
            entry["notes"] = note
        entry.setdefault("unit", "%")
        entry.setdefault("freq", "D" if "-" in str(obs[0][0]) and len(str(obs[0][0])) == 10 else "M")

    seed.setdefault("meta", {})["generated"] = TODAY
    seed["meta"]["note"] = (f"Refreshed {TODAY} by scripts/refresh_data.py via akshare. "
                            "Series not listed as refreshed retain their earlier provenance.")
    SEED.write_text(json.dumps(seed, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {SEED.relative_to(ROOT)}  ({len(existing)} series)")
    print("\nnow run:  python3 scripts/build_app_data.py && python3 scripts/make_standalone.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
