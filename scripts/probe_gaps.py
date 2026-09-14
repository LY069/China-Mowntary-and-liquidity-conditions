#!/usr/bin/env python3
"""
Probe the specific endpoints behind the three remaining reachable indicators,
plus re-fetch the 2015 CGB curve the sanity gate flags.

This is a reconnaissance instrument, not a fetcher. It answers four questions
that cannot be answered from the development sandbox, because every host below
is egress-blocked there:

  1. cfets                       — does chinamoney.com.cn serve the RMB index
                                   through a machine-readable route at all?
  2. household_time_deposit_share— is pbc.gov.cn reachable from a runner, and
     + corp_mlt_loans_yoy (B)      does the credit-balance PDF parse?
  3. corp_mlt_loans_yoy (A)      — does the quarterly loan-direction report
                                   parse out of HTML, on PBoC or its mirrors?
  4. cgb_1y 2015-06              — does ChinaBond still return the 1.77% the
                                   gate flags, i.e. is our stored value a
                                   faithful mirror or a parse artifact?

It never raises and never fails the job. Read the log.

    python3 scripts/probe_gaps.py           # everything
    python3 scripts/probe_gaps.py --only cfets cgb
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import traceback

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
TIMEOUT = 45


def rule(title):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def get(url, *, referer=None, headers=None, binary=False, label=None):
    """Fetch a URL and report what came back. Returns the body or None."""
    import requests
    h = {"User-Agent": UA, "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"}
    if referer:
        h["Referer"] = referer
    if headers:
        h.update(headers)
    tag = label or url
    try:
        r = requests.get(url, headers=h, timeout=TIMEOUT)
    except Exception as exc:
        print(f"  FAIL  {tag}\n        {type(exc).__name__}: {exc}")
        return None
    ct = r.headers.get("Content-Type", "?")
    n = len(r.content)
    print(f"  {r.status_code:3}   {tag}\n        {n} bytes · {ct}")
    if r.status_code != 200 or n == 0:
        return None
    if binary:
        return r.content
    # chinamoney and pbc both serve utf-8; fall back rather than throw
    r.encoding = r.apparent_encoding or "utf-8"
    return r.text


# --------------------------------------------------------------------------
# 1. cfets — the CFETS RMB exchange-rate index
# --------------------------------------------------------------------------
def probe_cfets():
    rule("cfets — CFETS RMB exchange-rate index (chinamoney.com.cn)")

    page_url = "https://www.chinamoney.com.cn/chinese/bkrmbidx/"
    print("\n[1] The index landing page")
    html = get(page_url)

    # The point of fetching the page is to read the endpoints OUT of it rather
    # than guessing them. CFETS drives its tables from /ags/ms/... XHR routes
    # and /r/cms/.../data/... static files; both appear as literals in the page
    # or in the scripts it pulls.
    if html:
        found = sorted(set(
            re.findall(r"/ags/ms/[A-Za-z0-9_\-/]+", html)
            + re.findall(r"/r/cms/[A-Za-z0-9_\-/.]+\.(?:csv|json)", html)
        ))
        print(f"\n    endpoint literals in the page itself: {len(found)}")
        for f in found[:40]:
            print("      ", f)

        scripts = re.findall(r'<script[^>]+src="([^"]+)"', html)
        print(f"\n    page pulls {len(scripts)} scripts; scanning the local ones")
        hits = set()
        for s in scripts[:25]:
            if s.startswith("//"):
                s = "https:" + s
            elif s.startswith("/"):
                s = "https://www.chinamoney.com.cn" + s
            elif not s.startswith("http"):
                continue
            if "chinamoney" not in s:
                continue
            body = get(s, referer=page_url, label=f"      script {s[-60:]}")
            if body:
                hits |= set(re.findall(r"/ags/ms/[A-Za-z0-9_\-/]+", body))
        if hits:
            print("\n    endpoint literals found inside scripts:")
            for h in sorted(hits):
                print("      ", h)

    # Candidate machine-readable routes, by analogy with the LPR/FDR CSVs that
    # research/08 confirmed exist for other series on this host.
    print("\n[2] Candidate machine-readable routes")
    candidates = [
        # the known-good analogue, to prove the pattern works from this runner
        ("https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/LprChrtCSV"
         "?startDate=2024-01-01", "KNOWN-GOOD analogue (LPR CSV)"),
        ("https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/"
         "rmb-index.csv", "guess: fx/rmb-index.csv"),
        ("https://www.chinamoney.com.cn/ags/ms/cm-u-bk-fx/RmbIdxHis"
         "?startDate=2024-01-01&endDate=2026-09-01", "guess: RmbIdxHis"),
        ("https://www.chinamoney.com.cn/ags/ms/cm-u-bk-ccpr/RmbFxIdx",
         "guess: RmbFxIdx"),
    ]
    for url, why in candidates:
        body = get(url, referer=page_url, label=f"{why}\n        {url}")
        if body:
            print("        first 300 chars:", repr(body[:300]))

    # The documented fallback: the weekly article list.
    print("\n[3] Documented fallback — the weekly index article list")
    get("https://www.chinamoney.com.cn/chinese/bmkidxrud/", label="bmkidxrud list")


# --------------------------------------------------------------------------
# 2. pbc.gov.cn reachability + the credit-balance PDF
# --------------------------------------------------------------------------
def probe_pboc_pdf():
    rule("household_time_deposit_share — PBoC 金融机构人民币信贷收支表 (PDF)")

    print("\n[1] Is pbc.gov.cn reachable from this runner at all?")
    for url in [
        "https://www.pbc.gov.cn/diaochatongjisi/116219/116319/index.html",
        "https://camlmac.pbc.gov.cn/diaochatongjisi/116219/116319/index.html",
    ]:
        get(url)

    print("\n[2] The verified credit-balance PDF asset")
    pdf_url = ("https://www.pbc.gov.cn/diaochatongjisi/attachDir/2025/11/"
               "2025111817164135629.pdf")
    blob = get(pdf_url, binary=True)
    if blob:
        print(f"        magic: {blob[:8]!r}  (want b'%PDF')")
        try:
            import pdfplumber, io
            with pdfplumber.open(io.BytesIO(blob)) as pdf:
                print(f"        pages: {len(pdf.pages)}")
                text = pdf.pages[0].extract_text() or ""
                print("        --- page 1 text, first 1500 chars ---")
                print(_indent(text[:1500]))
                tables = pdf.pages[0].extract_tables()
                print(f"        tables on page 1: {len(tables)}")
                for t in tables[:1]:
                    for row in t[:25]:
                        print("        ", row)
        except ImportError:
            print("        pdfplumber not installed — skipped parse")
        except Exception:
            traceback.print_exc()

    print("\n[3] The per-year node, for crawling the PDF slug")
    for url in [
        "https://www.pbc.gov.cn/diaochatongjisi/116219/116319/2026ntjsj/"
        "jrjgxdsztj/index.html",
        "https://www.pbc.gov.cn/diaochatongjisi/116219/116319/2025ntjsj/"
        "jrjgxdsztj/index.html",
    ]:
        html = get(url)
        if html:
            pdfs = sorted(set(re.findall(r"[^\"']*attachDir[^\"']*\.pdf", html)))
            print(f"        attachDir PDFs linked: {len(pdfs)}")
            for p in pdfs[:12]:
                print("          ", p)


# --------------------------------------------------------------------------
# 3. corp_mlt_loans_yoy — the quarterly loan-direction report (HTML)
# --------------------------------------------------------------------------
def probe_loan_direction():
    rule("corp_mlt_loans_yoy — 金融机构贷款投向统计报告 (quarterly HTML)")

    targets = [
        ("PBoC 2025 Q3",
         "https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/5877760/index.html"),
        ("gov.cn mirror",
         "https://www.gov.cn/lianbo/bumen/202505/content_7025931.htm"),
    ]
    # The number lives in running prose, so the test is whether the sentence
    # template survives extraction — not whether a table parses.
    pat = re.compile(r"中长期贷款余额[^。]{0,80}")
    for label, url in targets:
        print(f"\n[{label}]")
        html = get(url)
        if not html:
            continue
        text = re.sub(r"<[^>]+>", "", html)
        text = re.sub(r"\s+", "", text)
        hits = pat.findall(text)
        print(f"        中长期贷款余额 sentences found: {len(hits)}")
        for h in hits[:6]:
            print("          ", h)

    print("\n[list] The 新闻发布 column, for enumerating past quarters")
    html = get("https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/index.html")
    if html:
        arts = sorted(set(re.findall(r'href="(/goutongjiaoliu/[^"]+/index\.html)"', html)))
        print(f"        article links: {len(arts)}")
        for a in arts[:10]:
            print("          ", a)


# --------------------------------------------------------------------------
# 4. cgb_1y 2015-06 — is the flagged value what ChinaBond actually publishes?
# --------------------------------------------------------------------------
def probe_cgb_2015():
    rule("cgb_1y 2015-06 — re-fetch what the gate flags as a suspect print")

    # What we currently hold, for a like-for-like comparison.
    stored = {}
    try:
        with open("data/seed/series.json", encoding="utf-8") as fh:
            S = json.load(fh)["series"]
        for key in ("cgb_1y", "cgb_3y"):
            stored[key] = {d: v for d, v in S[key]["observations"]
                           if d.startswith("2015-06")}
        print(f"  stored cgb_1y 2015-06: {len(stored['cgb_1y'])} obs, "
              f"mean {sum(stored['cgb_1y'].values())/len(stored['cgb_1y']):.4f}")
    except Exception:
        traceback.print_exc()

    print("\n[1] akshare bond_china_yield for June 2015")
    try:
        import akshare as ak
        df = ak.bond_china_yield(start_date="20150601", end_date="20150630")
        print(f"        shape {df.shape}")
        print(f"        columns: {list(df.columns)}")
        print(_indent(df.head(8).to_string()))

        # Compare, row by row, against what we hold.
        col_1y = [c for c in df.columns if "1年" in str(c)]
        curve = [c for c in df.columns if "曲线名称" in str(c)]
        if col_1y and curve:
            gov = df[df[curve[0]].astype(str).str.contains("国债")]
            print(f"\n        国债 rows: {len(gov)}")
            print("\n        date        ours     theirs    diff")
            datecol = df.columns[0]
            for _, r in gov.iterrows():
                d = str(r[datecol])[:10]
                theirs = r[col_1y[0]]
                ours = stored.get("cgb_1y", {}).get(d)
                if ours is None:
                    print(f"        {d}  (not held)  {theirs}")
                else:
                    print(f"        {d}  {ours:7.4f}  {theirs:7.4f}  "
                          f"{float(theirs)-ours:+7.4f}")
    except ImportError:
        print("        akshare not installed — skipped")
    except Exception:
        traceback.print_exc()

    print("\n[2] ChinaBond's own endpoint, as an independent check")
    get("https://yield.chinabond.com.cn/cbweb-mn/yield_main", label="ChinaBond yield_main")


def _indent(s, pad="        "):
    return "\n".join(pad + line for line in str(s).splitlines())


PROBES = {
    "cfets": probe_cfets,
    "pboc_pdf": probe_pboc_pdf,
    "loan_direction": probe_loan_direction,
    "cgb": probe_cgb_2015,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", choices=sorted(PROBES))
    args = ap.parse_args()
    names = args.only or list(PROBES)
    for n in names:
        try:
            PROBES[n]()
        except Exception:
            # A probe that blows up must not take the others down with it.
            traceback.print_exc()
    print("\nprobe complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
