#!/usr/bin/env python3
"""
Probe candidate data sources and report what they actually return.

The sandbox this project is developed in cannot reach any macro data host, so
endpoint behaviour can only be established by running somewhere with real
network. This script is the instrument for that: it calls each candidate,
prints the shape, columns, date range and a sample row, and never fails the
build. Run it on a CI runner and read the log.

It doubles as a source health check on the weekly refresh: when an upstream
renames a column or drops a series, this says so before the fetchers silently
start returning nothing.

    python3 scripts/probe_sources.py            # probe everything
    python3 scripts/probe_sources.py --only gdp central_bank
"""
from __future__ import annotations

import argparse
import sys
import traceback

# name -> (callable-name, kwargs, what gap it would close)
PROBES = [
    ("central_bank_balance", "macro_china_central_bank_balance", {},
     "fiscal_deposits — the PBoC balance sheet carries 政府存款"),
    ("gdp", "macro_china_gdp", {},
     "nominal_gdp_yoy + gdp_deflator_yoy — 绝对值 is nominal, 同比增长 is real"),
    ("rmb_deposit", "macro_rmb_deposit", {},
     "household_time_deposit_share — needs a time/demand split, may not be present"),
    ("rmb_loan", "macro_rmb_loan", {},
     "corp_mlt_loans_yoy — needs a maturity split, may not be present"),
    ("new_financial_credit", "macro_china_new_financial_credit", {},
     "corp_mlt_loans_yoy / credit detail"),
    ("shrzgm", "macro_china_shrzgm", {},
     "tsf_ex_govt_yoy — which TSF components are broken out"),
    ("rmb_index", "macro_china_rmb", {},
     "cfets — the trade-weighted renminbi index"),
    ("bond_public", "macro_china_bond_public", {},
     "govt_bond_issuance — forward issuance announcements"),
    ("curve_map", "bond_china_close_return_map", {},
     "credit_spread_aa — enumerate every curve CFETS publishes"),
    ("treasure_issue", "bond_treasure_issue_cninfo",
     {"start_date": "20250101", "end_date": "20261231"},
     "govt_bond_issuance — treasury issuance detail"),
    ("local_govt_issue", "bond_local_government_issue_cninfo",
     {"start_date": "20250101", "end_date": "20261231"},
     "govt_bond_issuance — local government special bonds"),
    ("repo_fixings", "repo_rate_hist",
     {"start_date": "20260801", "end_date": "20260831"},
     "dr001 — confirm FDR001/FR001 are in the same response"),
]


def describe(df, sample_rows=2):
    import pandas as pd
    if df is None:
        return "    returned None"
    if not isinstance(df, pd.DataFrame):
        return f"    returned {type(df).__name__}: {str(df)[:300]}"
    if df.empty:
        return "    EMPTY DataFrame"
    out = [f"    rows={len(df)}  cols={len(df.columns)}"]
    out.append(f"    columns: {list(df.columns)}")
    # any column that looks like a date, to report coverage
    for c in df.columns:
        s = df[c].astype(str)
        if s.str.match(r"^\d{4}[-/年]").any():
            try:
                out.append(f"    range on {c!r}: {s.min()} .. {s.max()}")
            except Exception:                      # noqa: BLE001
                pass
            break
    head = df.head(sample_rows).to_dict("records")
    for r in head:
        out.append(f"    sample: { {k: str(v)[:26] for k, v in list(r.items())[:9]} }")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", nargs="*", metavar="NAME", help="probe only these")
    args = ap.parse_args()

    try:
        import akshare as ak
    except ImportError:
        print("akshare not installed — see the README for the install recipe", file=sys.stderr)
        return 0                                   # never fail the build

    ok = failed = 0
    for name, fnname, kwargs, why in PROBES:
        if args.only and name not in args.only:
            continue
        print(f"\n{'=' * 70}\n### {name}  ->  ak.{fnname}({', '.join(f'{k}={v!r}' for k, v in kwargs.items())})")
        print(f"    would close: {why}")
        fn = getattr(ak, fnname, None)
        if fn is None:
            print(f"    MISSING from akshare {getattr(ak, '__version__', '?')}")
            failed += 1
            continue
        try:
            print(describe(fn(**kwargs)))
            ok += 1
        except Exception as e:                     # noqa: BLE001
            failed += 1
            print(f"    FAILED: {type(e).__name__}: {e}")
            tb = traceback.format_exc().strip().splitlines()
            print(f"           {tb[-2].strip() if len(tb) > 1 else ''}")

    print(f"\n{'=' * 70}\n{ok} probe(s) returned data, {failed} failed")
    return 0                                       # informational only


if __name__ == "__main__":
    raise SystemExit(main())
