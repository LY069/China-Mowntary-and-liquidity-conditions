#!/usr/bin/env python3
"""
Fifth probe. One question left: can the quarterly 贷款投向 reports be enumerated?

The parser works — it was verified verbatim against 2025 Q3 and 2025 Q1. What
is missing is a list of report URLs. PBoC's own column is a dead end: the
fifteen articles it lists are JavaScript shells that render only site chrome,
index_1.html and friends 404, and index.html?page=2 returns the same fifteen.

gov.cn republishes the identical text and is server-rendered, so this asks
whether its search or its monthly archives can produce the list PBoC will not.
"""
from __future__ import annotations

import json
import re
import sys
import traceback

import requests

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
H = {"User-Agent": UA, "Accept-Language": "zh-CN,zh;q=0.9"}
KEY = "贷款投向"


def show(url, **kw):
    try:
        r = requests.get(url, headers=H, timeout=30, **kw)
    except Exception as exc:
        print(f"  FAIL {type(exc).__name__}: {str(exc)[:80]}  {url[:88]}")
        return None
    print(f"  {r.status_code}  {len(r.content):>8} bytes  {url[:88]}")
    if r.status_code != 200:
        return None
    r.encoding = r.apparent_encoding or "utf-8"
    return r.text


def main():
    print("=" * 72 + "\n[1] gov.cn search API\n" + "=" * 72)
    # gov.cn's public search backend. If it answers with JSON carrying titles
    # and URLs, the whole enumeration problem collapses.
    for url in (
        "https://sousuo.www.gov.cn/search-gov/data"
        "?t=zhengcelibrary_bm&q=%E8%B4%B7%E6%AC%BE%E6%8A%95%E5%90%91&n=20&p=1",
        "https://sousuo.www.gov.cn/search-gov/data"
        "?t=paper&q=%E8%B4%B7%E6%AC%BE%E6%8A%95%E5%90%91&n=20",
        "https://sousuo.www.gov.cn/sousuo/search.shtml"
        "?code=17da70961a7&searchWord=%E8%B4%B7%E6%AC%BE%E6%8A%95%E5%90%91",
    ):
        body = show(url)
        if not body:
            continue
        snippet = body[:400]
        print(f"        {snippet!r}")
        try:
            j = json.loads(body)
            # Walk for anything that looks like a result list.
            def walk(o, path=""):
                if isinstance(o, dict):
                    for k, v in o.items():
                        walk(v, f"{path}.{k}")
                elif isinstance(o, list) and o and isinstance(o[0], dict):
                    print(f"        list at {path}: {len(o)} items, "
                          f"keys {list(o[0])[:10]}")
                    for it in o[:5]:
                        t = str(it.get("title") or it.get("titleO") or "")[:40]
                        u = it.get("url") or it.get("link") or ""
                        print(f"          {KEY in t and '*' or ' '} {t}  {u[:70]}")
            walk(j)
        except Exception:
            pass

    print("\n" + "=" * 72 + "\n[2] gov.cn monthly archives\n" + "=" * 72)
    # The known mirror sits at /lianbo/bumen/202505/content_7025931.htm, so the
    # month node is the obvious place a quarterly report would be listed.
    for ym in ("202505", "202508", "202502", "202411"):
        body = show(f"https://www.gov.cn/lianbo/bumen/{ym}/")
        if not body:
            continue
        links = sorted(set(re.findall(r'href="(/lianbo/bumen/\d{6}/content_\d+\.htm)"', body)))
        print(f"        {len(links)} content links")
        print(f"        mentions {KEY} on the index page: {KEY in body}")

    print("\n" + "=" * 72 + "\n[3] The PBoC article ID neighbourhood\n" + "=" * 72)
    # The reports live at short numeric IDs (2025 Q3 = 5877760, 2023 annual =
    # 5221508) while everything the column lists uses timestamp IDs. If the
    # numeric IDs are dense, they are enumerable; if sparse, they are not.
    for pid in (5877760, 5221508, 5877761, 5877759, 5877700):
        body = show(f"https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/{pid}/index.html")
        if body:
            t = re.sub(r"<[^>]+>", "", body)
            t = re.sub(r"[ \t\r\n　]+", "", t)
            title = re.search(r"(.{0,30}(?:统计报告|数据报告|公告|通知))", t)
            print(f"        {KEY in t and 'HAS 贷款投向' or '            '}  "
                  f"{title.group(0)[:40] if title else '(no title found)'}")

    print("\nprobe complete")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(0)
