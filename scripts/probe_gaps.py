#!/usr/bin/env python3
"""
Third probe pass. What the first two settled, and what is left.

SETTLED
  cgb_1y 2015-06   ChinaBond returns exactly the 21 values we hold (mean
                   1.7727). Our data is a faithful mirror; the gate's warning
                   is an artefact of comparing monthly means.
  cfets            cm-u-bk-fx/RmbIdxHis serves the index as JSON, but only a
                   rolling ~1-year window: all nine parameter spellings and six
                   sibling routes returned the same 54 records.
  household_...    The year node's fourth PDF is 金融机构人民币信贷收支表 and
                   carries all twelve months of the year in one file.

OPEN — what this pass asks
  1. mtn_aa_3y     The first observation of every fetch batch is ~65bp below
                   the other two, four times over. _ncd_records reads vals[2]
                   (到期收益率) but never checks vals[1] (期限), trusting the
                   termId parameter to constrain the response. Dump the raw
                   records with the term field visible.
  2. corp_mlt      Is the 117.89万亿 figure the 企事业单位 medium-and-long-term
                   balance, or the 各项贷款 one? Print section 一 verbatim.
  3. household_... How are prior years' nodes addressed? The hub yields no
                   per-year links and the 2025 node guessed from the 2026
                   pattern 404s.
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


def get(url, *, referer=None, binary=False, label=None):
    import requests
    h = {"User-Agent": UA, "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"}
    if referer:
        h["Referer"] = referer
    tag = label or url
    try:
        r = requests.get(url, headers=h, timeout=TIMEOUT)
    except Exception as exc:
        print(f"  FAIL  {tag}\n        {type(exc).__name__}: {exc}")
        return None
    print(f"  {r.status_code:3}   {tag}  ({len(r.content)} bytes)")
    if r.status_code != 200 or not r.content:
        return None
    if binary:
        return r.content
    r.encoding = r.apparent_encoding or "utf-8"
    return r.text


# --------------------------------------------------------------------------
# 1. The mtn_aa_3y batch-boundary bug
# --------------------------------------------------------------------------
def probe_curve_term():
    rule("mtn_aa_3y — why is the first row of every batch ~65bp low?")

    import requests
    # CYCC82D is 中短期票据(AA+), resolved by label match on the live curve map.
    # One calendar month, exactly as the fetcher requests it.
    for code, term, what in (("CYCC82D", "3", "中短期票据(AA+) 3y — the broken one"),
                             ("CYCCJ0D", "1", "AAA NCD 1y — the one that looks fine")):
        print(f"\n[{what}]  bondType={code} termId={term}")
        try:
            r = requests.get(
                "https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/ClsYldCurvHis",
                params={"lang": "CN", "reference": "1,2,3", "bondType": code,
                        "startDate": "2026-09-01", "endDate": "2026-09-11",
                        "termId": term, "pageNum": "1", "pageSize": "50"},
                headers={"User-Agent": UA}, timeout=TIMEOUT)
            j = r.json() or {}
            recs = j.get("records") or []
            print(f"        {len(recs)} records")
            if recs:
                print(f"        keys of record 0: {list(recs[0])}")
            # Print every record in full. The whole question is what sits in
            # the field the fetcher ignores.
            for i, rec in enumerate(recs):
                clean = {k: v for k, v in rec.items() if k != "newDateValue"}
                print(f"        [{i}] {json.dumps(clean, ensure_ascii=False)}")
        except Exception:
            traceback.print_exc()


# --------------------------------------------------------------------------
# 2. corp_mlt — is 117.89万亿 the corporate cut or the all-loans cut?
# --------------------------------------------------------------------------
def probe_loan_section():
    rule("corp_mlt_loans_yoy — print section 一 verbatim")

    for label, url in (
        ("PBoC 2025 Q3",
         "https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/5877760/index.html"),
        ("gov.cn 2025 Q1",
         "https://www.gov.cn/lianbo/bumen/202505/content_7025931.htm"),
    ):
        print(f"\n[{label}]")
        html = get(url)
        if not html:
            continue
        text = re.sub(r"<[^>]+>", "", html)
        text = re.sub(r"[ \t\r\n　]+", "", text)
        # Everything from the 企事业单位 heading to the next numbered heading.
        m = re.search(r"一、企[事业]*单位贷款.{0,700}?(?=二、)", text)
        print("        --- section 一 verbatim ---")
        print("       ", m.group(0) if m else "(heading pattern did not match)")
        # And the totals, so the ratio can be sanity-checked by eye.
        for pat, name in ((r"各项贷款余额[\d.]+万亿元", "各项贷款余额"),
                          (r"企[事业]*单位贷款余额[\d.]+万亿元", "企事业单位贷款余额")):
            for mm in re.finditer(pat, text):
                print(f"        {name}: {mm.group(0)}")


# --------------------------------------------------------------------------
# 3. household — how are prior years addressed?
# --------------------------------------------------------------------------
def probe_pboc_years():
    rule("household_time_deposit_share — finding prior years")

    hub = "https://www.pbc.gov.cn/diaochatongjisi/116219/116319/index.html"
    print("\n[1] Every link on the statistics hub that looks like a node")
    html = get(hub, label="statistics hub")
    if html:
        links = sorted(set(re.findall(r'href="([^"]+)"', html)))
        interesting = [l for l in links
                       if re.search(r"(ntjsj|xdsz|1163|1162|20\d\d)", l)]
        print(f"        {len(links)} links, {len(interesting)} plausible nodes")
        for l in interesting[:45]:
            print("          ", l)

    print("\n[2] Year-node spellings, tried directly")
    for y in (2026, 2025, 2024, 2023):
        for pat in (f"https://www.pbc.gov.cn/diaochatongjisi/116219/116319/{y}ntjsj/jrjgxdsztj/index.html",
                    f"https://www.pbc.gov.cn/diaochatongjisi/116219/116319/{y}ntjsj/index.html"):
            body = get(pat, label=f"{y}: {pat.split('116319/')[1]}")
            if body:
                pdfs = sorted(set(re.findall(r"[^\"']*attachDir[^\"']*\.pdf", body)))
                print(f"          -> {len(pdfs)} PDFs")

    print("\n[3] Does the current-year PDF carry finished years too?")
    # The 2025-11 asset held 2023 data, so the archive is addressed by
    # publication date rather than by content year. Walk a few months back.
    for ym in ("2026/08", "2026/02", "2025/11", "2025/05", "2024/11"):
        node = (f"https://www.pbc.gov.cn/diaochatongjisi/116219/116319/"
                f"2026ntjsj/jrjgxdsztj/index.html")
        _ = ym  # the node is the only index we have; see [2] results
    print("        (deferred — depends on what [1] and [2] return)")


PROBES = {
    "curve_term": probe_curve_term,
    "loan_section": probe_loan_section,
    "pboc_years": probe_pboc_years,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", choices=sorted(PROBES))
    args = ap.parse_args()
    for n in (args.only or list(PROBES)):
        try:
            PROBES[n]()
        except Exception:
            traceback.print_exc()
    print("\nprobe complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
