#!/usr/bin/env python3
"""
Fourth probe. Two failures from the refresh dry run that guessing cannot fix.

  1. ClsYldCurvHis returned 403 on every 2015 window once pageSize went from
     50 to 1000. Is that the page size, the request rate, or the age of the
     window? The previous dataset only ever held four recent months, which
     hints the endpoint does not serve deep history at all — but that was
     never established, only inferred from an already-broken fetcher.

  2. The 贷款投向 crawl found 15 articles and none was the report. The list
     page yields only the most recent items, so either pagination is spelled
     differently or the report lives in another column.
"""
from __future__ import annotations

import json
import re
import sys
import time
import traceback

import requests

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
H = {"User-Agent": UA, "Accept-Language": "zh-CN,zh;q=0.9"}


def rule(t):
    print("\n" + "=" * 72 + f"\n{t}\n" + "=" * 72)


def curve(page_size, start, end, pause=0.0):
    if pause:
        time.sleep(pause)
    try:
        r = requests.get(
            "https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/ClsYldCurvHis",
            params={"lang": "CN", "reference": "1,2,3", "bondType": "CYCC82D",
                    "startDate": start, "endDate": end, "termId": "3",
                    "pageNum": "1", "pageSize": str(page_size)},
            headers=H, timeout=30)
    except Exception as exc:
        return f"EXC {type(exc).__name__}"
    if r.status_code != 200:
        return f"HTTP {r.status_code}"
    try:
        recs = (r.json() or {}).get("records") or []
    except Exception:
        return "unparseable JSON"
    if not recs:
        return "200, 0 records"
    dates = sorted({str(x.get("newDateValueCN")) for x in recs})
    return f"200, {len(recs)} records, {dates[0]} .. {dates[-1]}"


def probe_curve_limits():
    rule("ClsYldCurvHis — is the 403 about page size, rate, or window age?")

    print("\n[1] Same recent window, increasing page size (1s apart)")
    for ps in (50, 100, 200, 500, 1000):
        print(f"  pageSize={ps:<5} -> {curve(ps, '2026-09-01', '2026-09-11', pause=1.0)}")

    print("\n[2] Same page size (50), walking backwards in time (1s apart)")
    for y in (2026, 2025, 2024, 2022, 2020, 2018, 2015):
        print(f"  {y}-03 -> {curve(50, f'{y}-03-01', f'{y}-03-31', pause=1.0)}")

    print("\n[3] Rate: ten rapid identical calls, no pause")
    for i in range(10):
        res = curve(50, "2026-08-01", "2026-08-31")
        print(f"  call {i+1:>2} -> {res}")
        if res.startswith("HTTP 403"):
            print("        -> 403 appeared after "
                  f"{i+1} rapid calls; this is rate limiting, not page size")
            break


def probe_loan_listing():
    rule("贷款投向 — where does the report actually live?")

    known = "https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/5877760/index.html"
    print(f"\n[1] The known 2025 Q3 report is reachable: ", end="")
    try:
        r = requests.get(known, headers=H, timeout=30)
        print(f"HTTP {r.status_code}, {len(r.content)} bytes")
    except Exception as exc:
        print(f"FAIL {exc}")

    print("\n[2] Pagination spellings on column 113469")
    base = "https://www.pbc.gov.cn/goutongjiaoliu/113456/113469"
    for spell in ("index_1.html", "index_2.html", "index1.html",
                  "index.html?page=2", "index_1.htm"):
        url = f"{base}/{spell}"
        try:
            r = requests.get(url, headers=H, timeout=30)
            n = len(set(re.findall(
                r'href="(/goutongjiaoliu/113456/113469/[^"]+/index\.html)"', r.text)))
            print(f"  {spell:<22} HTTP {r.status_code}, {len(r.content):>7} bytes, {n} article links")
        except Exception as exc:
            print(f"  {spell:<22} FAIL {exc}")

    print("\n[3] Is 贷款投向 in column 113469 at all? Open every listed article.")
    try:
        r = requests.get(f"{base}/index.html", headers=H, timeout=30)
        r.encoding = r.apparent_encoding or "utf-8"
        arts = sorted(set(re.findall(
            r'href="(/goutongjiaoliu/113456/113469/[^"]+/index\.html)"', r.text)))
    except Exception as exc:
        print(f"  list failed: {exc}")
        arts = []
    print(f"  {len(arts)} articles listed")
    for a in arts[:20]:
        try:
            rr = requests.get("https://www.pbc.gov.cn" + a, headers=H, timeout=30)
            rr.encoding = rr.apparent_encoding or "utf-8"
            t = re.sub(r"<[^>]+>", "", rr.text)
            t = re.sub(r"[ \t\r\n　]+", "", t)
            title = re.search(r"(.{0,40}统计报告|.{0,40}数据报告|.{0,30}公告)", t)
            print(f"    {a.split('/')[-2]:<22} "
                  f"{'HAS 贷款投向' if '贷款投向' in t else '           '} "
                  f"{title.group(0)[:38] if title else ''}")
        except Exception as exc:
            print(f"    {a}: {exc}")

    print("\n[4] PBoC site search for the report")
    for url in ("https://www.pbc.gov.cn/search/whitepaper?keyword=%E8%B4%B7%E6%AC%BE%E6%8A%95%E5%90%91",
                "http://www.pbc.gov.cn/zhengwugongkai/4081330/4081344/4081395/4081132/index.html"):
        try:
            r = requests.get(url, headers=H, timeout=30)
            print(f"  HTTP {r.status_code}, {len(r.content)} bytes  {url[:70]}")
        except Exception as exc:
            print(f"  FAIL {exc}  {url[:70]}")


def main():
    for f in (probe_curve_limits, probe_loan_listing):
        try:
            f()
        except Exception:
            traceback.print_exc()
    print("\nprobe complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
