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
    """Normalise whatever akshare returns for a date into 'YYYY-MM'."""
    s = str(value).strip()
    for fmt in ("%Y-%m-%d", "%Y%m%d", "%Y-%m", "%Y年%m月份", "%Y年%m月"):
        try:
            return datetime.strptime(s, fmt).strftime("%Y-%m")
        except ValueError:
            continue
    if len(s) >= 7 and s[4] in "-/年":
        return s[:4] + "-" + s[5:7].zfill(2)
    return None


def as_day(value) -> str | None:
    s = str(value).strip()
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
            out.append([m, round(float(v) * scale, 4)])
        except (TypeError, ValueError):
            continue
    return sorted({m: v for m, v in out}.items())


def daily(df, datecol, valcol):
    out = []
    for _, row in df.iterrows():
        d = as_day(row[datecol])
        v = row[valcol]
        if d is None or v is None:
            continue
        try:
            out.append([d, round(float(v), 4)])
        except (TypeError, ValueError):
            continue
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
    for sid, col, real in [("dr007", "FDR007", "DR007"), ("r007", "FR007", "R007")]:
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
    for sid, *names in [("cgb_1y", "1年", "1Y"), ("cgb_10y", "10年", "10Y")]:
        # "1年" is a substring of "10年 " in some layouts, so exact match must win;
        # pick() tries exact first, which is why 10y resolves correctly.
        try:
            col = pick(df, *names)
        except KeyError as e:
            print(f"    skip {sid}: {e}")
            continue
        out[sid] = (daily(df, dcol, col), prov, "ChinaBond closing yield curve, maturity point.")
    return out


def fetch_ncd(ak, start):
    df = ak.bond_china_close_return(symbol="同业存单(AAA)", period="1",
                                    start_date=start.replace("-", "") + "01",
                                    end_date=TODAY.replace("-", ""))
    dcol = pick(df, "日期", "date")
    vcol = pick(df, "到期收益率", "收益率")
    prov = {"source_name": "CFETS closing yield curve, AAA NCD (ClsYldCurvHis) via akshare",
            "source_url": f"{CFETS}/ags/ms/cm-u-bk-currency/ClsYldCurvHis",
            "retrieved": TODAY, "confidence": "partial"}
    return {"ncd_1y_aaa": (daily(df, dcol, vcol), prov,
                           "1-year maturity point of the AAA negotiable CD curve. Run "
                           "ak.bond_china_close_return_map() first to confirm the curve label.")}


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
        out[sid] = (obs, prov,
                    "Step series keyed on the EFFECTIVE date (生效时间), not the announcement "
                    "date. Reconcile against PBoC announcements before relying on it — the "
                    "seed series was truncated precisely because a mirror had incomplete "
                    "change dates.")
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


FETCHERS = {
    "money":     (fetch_money_supply, ["m1_yoy", "m2_yoy", "m2_level"]),
    "tsf":       (fetch_tsf,          ["tsf_flow"]),
    "lpr":       (fetch_lpr,          ["lpr_1y", "lpr_5y"]),
    "repo":      (fetch_repo_fixings, ["dr007", "r007"]),
    "cgb":       (fetch_cgb_curve,    ["cgb_1y", "cgb_10y"]),
    "ncd":       (fetch_ncd,          ["ncd_1y_aaa"]),
    "interbank": (fetch_interbank,    ["shibor_3m", "cnh_hibor_on"]),
    "rrr":       (fetch_rrr,          ["rrr_large", "rrr_small"]),
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
        entry["observations"] = obs
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
