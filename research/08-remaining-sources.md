# 08 — Sourcing the ten remaining unsourced indicators

**Compiled:** 13 September 2026.
**Scope:** the ten indicators in `data/registry_*.json` that are *not* already served by `akshare`.
Everything already fetched successfully (DR007/R007/DR001/R001, SHIBOR, CNH HIBOR, the ChinaBond CGB
curve, the AAA NCD curve, LPR, RRR, M1/M2, TSF total flow) is out of scope and is not discussed here.

**Companion documents:** `research/05-data-sources.md` (the general sourcing manual) and
`research/07-data-validation.md`. This file supersedes §5 of `05-data-sources.md` for these ten series.

---

## 0. Verification legend

Same convention as `05-data-sources.md`:

| Mark | Meaning |
|---|---|
| ✅ **verified** | The string was read this session out of a retrieved source — a search result that quoted the publisher verbatim, or source code / documentation retrieved from GitHub. |
| 🟡 **code-verified, not live-tested** | The URL and its parameters were read verbatim out of a working open-source client's source code. The string is real and is what that client sends in production. **This session could not issue the request** (the egress proxy 403s every macro host — re-confirmed this session for `chinamoney.com.cn`, `iftp.chinamoney.com.cn`, `chinamoney.org.cn`, `yield.chinabond.com.cn`), so the live response shape is not confirmed. |
| ⚠️ **unverified** | Plausible and in most cases the practitioner-standard answer, but not confirmed against any source this session. **Do not build on it without checking.** |

Environment note: the only channels that worked this session were **web search** and
**`github.com` / `raw.githubusercontent.com` over git+curl**. A great deal below therefore comes from
reading the source code of Python clients that call these endpoints in production — an excellent
source for *URL strings and parameter names*, a poor source for *whether the service responds today*.

---

## 1. Summary table — ranked by (value × ease)

Build top-down. "Value" is the indicator's weight in the liquidity/monetary narrative; "Ease" is how
close a confirmed machine-readable route is.

| # | Indicator | Machine-readable route? | Feasibility | Value | Build order |
|---|---|---|---|---|---|
| 1 | `fiscal_deposits` | **Yes — Sina JSONP mirror of the full 货币当局资产负债表** 🟡 | **Easy** | High | **1** |
| 2 | `outright_repo` | No API, but a *dedicated* PBoC announcement column with ~2 posts/month since Oct-2024 ✅ | **Easy–Medium** | High | **2** |
| 3 | `net_injection_3m` | No API. Daily PBoC announcement crawl; static HTML since 2025 ✅ | **Medium** | Very high | **3** |
| 4 | `credit_spread_aa` | **Yes — two JSON/form endpoints** (CFETS `ClsYldCurvHis`; ChinaBond `searchYc`) 🟡; exact curve label still to confirm | **Medium** | High | **4** |
| 5 | `tsf_ex_govt_yoy` | No API. PBoC monthly HTML report + PDF stock table ✅ | **Medium** | High | **5** |
| 6 | `corp_mlt_loans_yoy` | No API. Quarterly HTML report (easy) or monthly PDF table (harder) ✅ | **Medium** | High | **6** |
| 7 | `govt_bond_issuance` | No API. Derivable from the TSF **increment** table's 政府债券 line ✅ | **Medium** | Medium-High | **7** |
| 8 | `cfets` | No public JSON found. HTML page + article parse ✅ | **Medium** | Medium | **8** |
| 9 | `household_time_deposit_share` | **PDF parse only** for the monthly series ✅ | **Medium–Hard** | Medium-High | **9** |
| 10 | `overnight_repo_share` | **Not machine-readable** from the primary publisher. Quarterly ratio is a sentence in a PDF; a daily *exchange-repo* proxy exists ✅ | **Hard / Not machine-readable** | Medium | **10** |

**One-line verdict.** Four are genuinely buildable now (`fiscal_deposits`, `outright_repo`,
`net_injection_3m`, `credit_spread_aa`). Five need an HTML/PDF parser but are tractable. One
(`overnight_repo_share`) has no free machine-readable primary source at all.

---

## 2. Indicator-by-indicator

### 2.1 `fiscal_deposits` — government deposits at the PBoC

**Confirmed:** yes, this is the **政府存款** line of the **货币当局资产负债表** (Balance Sheet of
Monetary Authority). ✅

| Field | Value |
|---|---|
| **Official publisher** | 中国人民银行 调查统计司 (PBoC Survey & Statistics Department) |
| **Official page** | Statistics hub: `https://www.pbc.gov.cn/diaochatongjisi/116219/116319/index.html` ✅ → per-year 货币统计概览 node, e.g. 2025: `https://www.pbc.gov.cn/diaochatongjisi/116219/116319/5570903/5570886/index.html` ✅ |
| **Exact table name** | 货币当局资产负债表 (English header on the same sheet: *Balance Sheet of Monetary Authority*). Unit 亿元. The liability side carries 储备货币 / 其中：货币发行、金融性公司存款、其他存款性公司存款、**政府存款**、自有资金、其他负债. ⚠️ exact sub-line spellings not re-read this session |
| **Sister table** | 存款性公司概览 and 其他存款性公司资产负债表 sit on the same 货币统计概览 node |
| **Frequency** | Monthly (annual only 1994–1999; **monthly from 2000**) ✅ |
| **Lag** | PBoC publishes the monetary statistics release "within 15 days of month end" ✅; in practice the balance sheet lands **mid-month**, i.e. a few days after the 金融统计数据报告 (which itself has landed on the 12th in both verified 2025/2026 examples) |
| **Primary format** | Recent years: **PDF** under `https://www.pbc.gov.cn/diaochatongjisi/attachDir/YYYY/MM/<timestamp>.pdf` ✅ (example: `.../2025/12/2025121517172659799.pdf`). Older years: HTML tables under `eportal/fileDir/...` ✅. **Neither is a stable slug — you must crawl the year node.** |

**Machine-readable route — YES, and it is the single best one in this document.**

Sina Finance mirrors the *entire* monetary-authority balance sheet as a paginated JSONP feed.
`akshare` calls it as `ak.macro_china_central_bank_balance()`; the function body is 🟡:

```
GET https://quotes.sina.cn/mac/api/jsonp_v3.php/SINAREMOTECALLCALLBACK1601651495761/MacPage_Service.get_pagedata
    ?cate=fininfo&event=8&from=0&num=31&condition=
```

- Paginate by stepping `from` in increments of `num` (=31); total rows are in `count`,
  so `page_num = ceil(count / 31)`.
- The response is JSONP; strip to the first `{` and drop the trailing `);` before JSON-decoding
  (akshare uses `demjson`).
- **Column names are not hard-coded** — they come back in `config.all` as `[code, label]` pairs, and
  akshare assigns `df.columns = [item[1] for item in data_json["config"]["all"]]`. 🟡
  So the fetcher should look up the column whose label is `政府存款` at runtime rather than
  positionally. ⚠️ The exact Chinese label string in Sina's `config.all` was **not** read this
  session — print the column list once before wiring it.
- Human-readable mirror of the same table: `https://finance.sina.com.cn/mac/#fininfo-8-0-31-2` ✅

The `cate=fininfo` family on the same endpoint also serves `event=1` (货币供应量),
`event=5` (外汇储备/黄金), `event=19` (保险业经营情况) 🟡 — useful cross-checks.

**Reliability of the mirror.** Sina's macro feed is a scrape of PBoC, refreshed with a lag of days
and with no SLA. It has historically gone stale on individual tables. **Cross-check the latest two
observations against the PBoC PDF** before trusting a print, and keep the PBoC PDF path as a
fallback. Do not treat Sina as the system of record.

**Feasibility verdict: Easy.** Single GET, paginated, full history, no auth.

---

### 2.2 `net_injection_3m` — PBoC net open-market liquidity injection, 3-month sum

| Field | Value |
|---|---|
| **Official publisher** | 中国人民银行 公开市场业务操作室 |
| **Official page (daily)** | 公开市场业务交易公告: `https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/index.html` ✅ |
| **Parent column** | 公开市场业务: `https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/index.html` ✅ |
| **Sibling column** | 公开市场业务公告 (notices, not trades): `https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125469/index.html` ✅ |
| **Exact series name** | 公开市场业务交易公告 [YYYY]第N号 ✅ |
| **Frequency** | Every trading day (numbered sequentially within the year; 2026 was already at 第78号 by 24 April ✅) |
| **Lag** | Same day — the announcement for day *T*'s operation is posted on day *T*, typically ~09:20 Beijing |
| **Format** | **HTML parse only.** No JSON, no CSV, no Excel. |

**Structure of the crawl (all ✅, read out of `openakita/openakita`'s production fetcher
`plugins/fin-pulse/finpulse_fetchers/pbc_omo.py`):**

- **In 2025 PBoC dropped the `.../17081/` subfolder** that used to front this index and now serves
  the listing **directly from `.../125475/index.html` as plain static HTML**. The old
  `atob(...)` JavaScript-redirect obfuscation is **gone** — no headless browser, no PyExecJS. ✅
  This is the single most important fact for anyone who tried this before 2025 and gave up.
- Listing anchors look like:
  `<a href="/zhengcehuobisi/125207/125213/125431/125475/202604240851xxxxxxxx/index.html" onclick="void(0)" target="_blank" title="公开市场业务交易公告 [2026]第78号" istitle="true">` ✅
- The date sits in a nearby `<span class="hui12">2026-04-24</span>` ✅
- Historical pagination (older archive) uses `.../125475/17081-{page}.html` ✅
  (from `ericxuzhesheng/Bond-Futures-Data-Monitor`). Archive reaches back to at least **2008** —
  duplicate posts exist for some 2008 announcements, so dedupe on the announcement number. ✅
- The index carries the same URL twice (mobile + desktop markup) — dedupe within a single fetch. ✅
- PBoC's subtree has historically been GB2312/GBK; modern pages are UTF-8. Pin the charset and
  handle both. ✅

**Each announcement body** states the operation type, tenor, volume, winning rate, and the amount
maturing that day. Net injection = Σ(operations) − Σ(maturities). **Post-Oct-2024 the toolkit is
OMO + MLF + 买断式逆回购 + PSL + 国债买卖 — netting only OMO and MLF is now materially wrong**
(see §2.3). `net_injection_3m` must sum across instruments.

**Third-party structured mirror — one existed and is now dead.** CFETS ran a structured table at
`https://www.chinamoney.com.cn/chinese/yhgkscczh/` ("央行公开市场操作") backed by:

```
POST https://www.chinamoney.com.cn/ags/ms/cm-u-bond-publish/TicketHandle
  form: pageSize=15, pageNo=<n>
  headers: Referer: https://www.chinamoney.com.cn/chinese/yhgkscczh/
           X-Requested-With: XMLHttpRequest
           Content-Type: application/x-www-form-urlencoded; charset=UTF-8
  → data.pageTotal, data.resultList  →  操作日期, 期限, 交易量, 中标利率, 正/逆回购
```

🟡 (read verbatim out of the pre-removal `macro_china_gksccz()` body in an akshare fork). It covered
**2004-01-16 →** and returned all history. **However:** akshare deprecated and then deleted this
function with the note *「由于目标网站未更新数据，该接口即将移除」* ("the target site stopped updating
this data") ✅ — the whole function body is commented out upstream. **Treat this endpoint as stale.**
It is worth one probe when you have network (it costs nothing and would collapse this indicator to
Easy), but do not design around it. The page itself is still live ✅.

CFETS also republishes the PBoC announcements as articles, e.g.
`https://www.chinamoney.org.cn/chinese/scggyhywgggksccz/20250324/3075425.html` ✅ — an alternative
crawl target if pbc.gov.cn blocks you, but equally HTML-only.

**Feasibility verdict: Medium.** Pure HTML crawl, but a well-trodden one with at least six
independent open-source implementations to copy from. Budget half a day for the full archive.

---

### 2.3 `outright_repo` — outright reverse repo (买断式逆回购), monthly volumes

| Field | Value |
|---|---|
| **Official publisher** | 中国人民银行 |
| **Official page** | **公开市场买断式逆回购业务公告** — its own column: `https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/5492845/index.html` ✅ |
| **Example posts** | `[2025]第3号`: `https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/5492845/5646939/index.html` ✅ · `[2025]第5号`: `https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/5492845/5730066/index.html` ✅ |
| **Exact series name** | 公开市场买断式逆回购业务公告 [YYYY]第N号 ✅ |
| **Instrument** | Introduced **October 2024** ✅. PBoC buys bonds outright from primary dealers with an agreement to sell them back; tenor **≤ 1 year** (3-month and 6-month are the two in use) ✅ |
| **Frequency** | Roughly **monthly** operations, sometimes two a month once 3M and 6M tenors both roll ✅. Announcements are numbered sequentially within the year. |
| **Lag** | Same day / one day ahead — PBoC typically pre-announces ("6月4日公告，6月5日开展5000亿元买断式逆回购操作") ✅ |
| **Format** | **HTML parse only.** |

**Verified operation prints** (useful as parser fixtures and as a sanity check on your extraction):

- 2025-12: 6-month 买断式逆回购 6,000億元 ✅
- 2026-01-08: 3-month, **11,000億元** ✅
- 2026-06-05: **5,000億元** ✅
- 2026-06: 6-month tranche rolled **等额续作** (rolled at par) ✅
- 2026-08-14: **10,000億元**, 6-month (185 days), maturing 2027-02-15 ✅
- One 14,000億元 operation is also on record ✅

**Why this one is easy despite having no API:** the series starts in **October 2024**, so the entire
history is ~25–40 announcements on a single short column page. This is the *smallest* crawl in this
document and it closes a genuinely important post-2024 gap in `net_injection_3m`. Build it
immediately after `fiscal_deposits`.

**No third-party structured mirror was found.** East Money and Sina carry the operations only as
news articles, not as a table. ⚠️

**Feasibility verdict: Easy–Medium.** Tiny crawl, dedicated column, no pagination worth the name.

---

### 2.4 `overnight_repo_share` — overnight share of interbank pledged-repo turnover

**This is the hardest of the ten.** The ratio is published, but only as prose in a quarterly PDF; the
underlying daily turnover-by-tenor is not freely machine-readable.

| Field | Value |
|---|---|
| **Underlying series wanted** | 银行间市场质押式回购成交量，分期限 (隔夜 / 7天 / …) |
| **Primary publisher (turnover)** | 中国外汇交易中心 (CFETS) / 中国货币网 |
| **Turnover pages** | 货币市场行情 (同业拆借利率 · 质押式/买断式回购): `https://www.chinamoney.com.cn/chinese/mkdatapm/` ✅ · 日报（债券买断式质押式回购信息）: `https://www.chinamoney.org.cn/chinese/mtdexdaily/` ✅ |
| **Format** | HTML / daily report. **No public JSON endpoint was found.** ⚠️ CFETS's programmatic feeds (CMDS Pro, CSTP) are **member-institution services requiring registration and approval** ✅ — not open. |

**The ratio itself is published directly — in the 货币政策执行报告 (MPR), quarterly, as a sentence.** ✅
The MPR's 货币市场运行 section states, in each quarter, the cumulative-to-date overnight share of
both repo and interbank-lending turnover. Values read verbatim this session:

| Period | 隔夜回购占回购总量 | 隔夜拆借占拆借总量 |
|---|---|---|
| 2023 full year (Q4 MPR) | **87.5%** (+1.1pp yoy) | 89.5% (+0.3pp yoy) |
| 2024 H1 | **84.6%** (−2.2pp yoy) | 84.4% (−5.9pp yoy) |
| 2025 H1 | **83.8%** (−0.8pp yoy) | 79.4% (−5.0pp yoy) |
| 2025 Q1–Q3 | **85.1%** (+0.4pp yoy) | 81.7% (−2.3pp yoy) |

All ✅. **Note these are year-to-date cumulative shares, not the share in the quarter** — you must
un-cumulate them if you want a quarterly series, and you cannot get a monthly one at all.

MPR PDF locations ✅:
- `https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/5238308/2024030610591528512.pdf` (2023 Q4)
- `https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2026051118520164705/2026051118500062162.pdf` (2026 Q1)
- MOFCOM mirrors several quarters at `https://cif.mofcom.gov.cn/cif/html/upload/...pdf` ✅ — often
  easier to fetch than pbc.gov.cn.

**Daily proxy that IS machine-readable (use with an explicit caveat).** East Money serves
**exchange** pledged repo (上证/深证 质押式回购 — GC001/GC007/R-001/R-007 …) with per-code turnover:
`ak.bond_buy_back_em()` and `ak.bond_buy_back_hist_em(symbol=...)` (东方财富网-行情中心-债券市场-质押式回购) 🟡.
Overnight share of *exchange* repo turnover is computable daily from this and co-moves with the
interbank figure. **It is not the same series** — exchange repo is a small, retail/broker-weighted
slice of the market — so label it a proxy in the registry and never blend it with the MPR number.

**Feasibility verdict: Hard / Not machine-readable.** Quarterly YTD ratio via PDF prose extraction;
no free daily interbank turnover. If this indicator matters enough, this is the one place where a
paid feed (Wind/CEIC) is genuinely the rational answer.

---

### 2.5 `household_time_deposit_share` — 住户存款 定期 vs 活期

**Confirmed:** yes, this lives in the **金融机构人民币信贷收支表**. ✅

| Field | Value |
|---|---|
| **Official publisher** | 中国人民银行 调查统计司 |
| **Column** | 统计数据 → 金融机构信贷收支统计. Per-year node, e.g. 2011: `https://www.pbc.gov.cn/diaochatongjisi/116219/116319/116357/116514/index.html` ✅; current-year node pattern `.../116219/116319/{YYYY}ntjsj/jrjgxdsztj/index.html` ✅ (this exact path is also served on the PBoC sub-domain `camlmac.pbc.gov.cn`, which has been easier to reach than the main host ✅) |
| **Exact table names** | Two parallel tables, published together: **金融机构人民币信贷收支表** and **存款类金融机构人民币信贷收支表** ✅. (Also 本外币 variants of each ✅.) Use the **金融机构人民币** one unless you specifically want the depository-only aggregate. |
| **The lines you want** | 来源方 → 各项存款 → 境内存款 → **住户存款** → **活期存款** / **定期及其他存款** ✅ |
| **Frequency** | Monthly (Jan–Feb are combined into a single "1-2月" print ✅ — your parser must handle that, and your monthly series will have a hole at January every year) |
| **Lag** | ~mid-month following, alongside the 金融统计数据报告 ⚠️ (exact day not pinned this session) |
| **Format** | **PDF parse only** for recent years. Verified live asset URLs: 金融机构人民币信贷收支表 `https://www.pbc.gov.cn/diaochatongjisi/attachDir/2025/11/2025111817164135629.pdf` ✅ · 存款类金融机构人民币信贷收支表 `https://www.pbc.gov.cn/diaochatongjisi/attachDir/2025/11/2025111817284449935.pdf` ✅. Older vintages are HTML/PDF under `goutongjiaoliu/...`, e.g. `https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2964272/2015101616080058336.pdf` ✅ |
| **Unit** | 亿元 ✅ |

**Machine-readable mirrors — none good.**
- **NBS 国家数据** carries `金融机构人民币信贷收支(年底余额)` at `https://data.stats.gov.cn/tablequery.htm?code=AD08` ✅ — but **annual year-end only**, which is useless for a share that moves month to month.
- 国研网 (DRC) mirrors the monthly table behind a login: `https://guoyanwang.clcn.net.cn/...DocID=8189606...` ✅ — paywalled, do not build on it.
- **Sina does not appear to mirror this table.** Sina's `cate=fininfo` macro family covers 货币供应量, 货币当局资产负债, 外汇黄金, 保险 — a 信贷收支 event was **not** found. ⚠️ (worth one probe of adjacent `event=` integers when you have network, but do not assume it exists.)
- `akshare` has **no** function for this table ✅ (grepped the whole package).

**Feasibility verdict: Medium–Hard — PDF parse only.** The table is wide and bilingual; the
"来源方项目 / 余额 / 运用方项目 / 余额" two-column layout confuses naive PDF extractors. Budget real
time for the parser, and pin it with a checksum against a few known prints (e.g. 各项存款 1,378,827.50
億元 / 各项贷款 977,588.72 億元 on one verified 2015 sheet ✅).

---

### 2.6 `corp_mlt_loans_yoy` — corporate medium-and-long-term loans, stock, YoY

Two tables carry the maturity split; pick by frequency.

**Route A (recommended first) — quarterly, HTML, easy.**

| Field | Value |
|---|---|
| **Publisher** | 中国人民银行 (released via 沟通交流 → 新闻发布) |
| **Exact report name** | **金融机构贷款投向统计报告** ✅ |
| **Example URLs** | 2025 Q3: `https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/5877760/index.html` ✅ · 2023 annual: `http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/5221508/index.html` ✅ |
| **Frequency** | Quarterly ✅ |
| **Lag** | ~3–4 weeks after quarter end. 2026 Q1 report appeared 2026-04-29/30 ✅ |
| **Format** | **HTML article** — the numbers are in running prose, not a table, but the sentence structure is highly stable across quarters. |
| **What it gives** | 本外币**企事业单位**贷款余额 + 同比, and explicitly *其中*中长期贷款余额 + 同比. ✅ |
| **Verified prints** | 2023 年末: 企事业单位贷款余额 157.07 万亿元 (+12.7% yoy), 其中中长期贷款余额 **98.79 万亿元 (+15.7% yoy)** ✅ · 2025 Q4: 中长期贷款余额 118.39 万亿元 (+7.9% yoy), 全年增加 8.69 万亿元 ✅ · 2026 Q1: 中长期贷款余额 **123.81 万亿元 (+7.4% yoy)**, 一季度增加 5.42 万亿元 ✅ |

Mirrors that are often easier to fetch than pbc.gov.cn and carry the *identical* text: 中国政府网
`https://www.gov.cn/lianbo/bumen/202505/content_7025931.htm` ✅, 上海市委金融办
`https://jrj.sh.gov.cn/SCGK194/...` ✅, Sina `https://finance.sina.com.cn/money/bank/2026-04-29/doc-inhwefva7716527.shtml` ✅.

⚠️ **Caution on the 2026 Q1 figure:** 123.81 万亿元 is described in the report as the maturity split of
**各项贷款** (all loans, 280.51 万亿元 total), not specifically of 企事业单位贷款. The report uses both
cuts in adjacent sentences. **Read the full sentence, do not regex on the number alone.**

**Route B — monthly, PDF, harder.** The **金融机构人民币信贷收支表** (§2.5, same PDFs) carries
运用方 → 各项贷款 → 境内贷款 → **企（事）业单位贷款** → 短期贷款 / **中长期贷款** / 票据融资 / 各项垫款. ✅
Monthly, but PDF-only and with the Jan–Feb combined print. Use this only if you truly need monthly.

**Feasibility verdict: Medium.** Route A is quarterly HTML with a stable sentence template — a day's
work. Route B upgrades you to monthly at the cost of the §2.5 PDF parser (which you need anyway for
`household_time_deposit_share`, so build that once and reuse it).

---

### 2.7 `tsf_ex_govt_yoy` — TSF stock excluding government bonds

**Confirmed:** the component is **政府债券**, and it exists as a single line of the TSF stock table. ✅

| Field | Value |
|---|---|
| **Official publisher** | 中国人民银行 调查统计司 |
| **Exact table name** | **社会融资规模存量统计表** (English header: *Aggregate Financing to the Real Economy (Stock)*) ✅. Its sibling is 社会融资规模增量统计表 (*Flow*) ✅ |
| **Landing page** | `https://www.pbc.gov.cn/diaochatongjisi/116219/116319/3959050/3959051/index.html` ✅ |
| **Verified asset URLs** | Stock table: `https://www.pbc.gov.cn/diaochatongjisi/attachDir/2025/11/2025110511314347909.pdf` ✅ · Flow table: `https://www.pbc.gov.cn/diaochatongjisi/attachDir/2025/11/2025110511302392865.pdf` ✅ · older: `https://www.pbc.gov.cn/eportal/fileDir/diaochatongjisi/resource/cms/2022/04/2022041816440579530.pdf` ✅ |
| **Unit** | 万亿元 on the stock table ✅ (the flow table is 亿元 — **do not mix them**) |
| **Monthly narrative release** | 社会融资规模存量统计数据报告, an **HTML article** under `goutongjiaoliu/113456/113469/...` ✅ (annual example: `http://www.pbc.gov.cn/diaochatongjisi/116219/116225/5565443/index.html` ✅) |
| **Frequency** | Monthly stock since **2016**; monthly flow since 2012; quarterly since April 2011 ✅ |
| **Lag** | Released with the monthly 金融统计数据报告, i.e. ~the 12th–15th of the following month ✅ |
| **Format** | **PDF for the table; HTML for the narrative.** No CSV, no Excel, no API. |

**Methodology fact you must encode ✅:** 政府债券 as a single indicator dates from the **December 2019**
revision, when 国债 and 地方政府一般债券 were folded in with the pre-existing 地方政府专项债券. It is
recorded at **face value at the depository**. **Back-history runs to January 2017 only.** A
`tsf_ex_govt_yoy` series therefore cannot start before **Jan 2017**, and its first YoY print is
**Jan 2018**.

**Verified cross-checks for your parser ✅:** end-2024 TSF stock 408.34 万亿元 (+8.0% yoy), with
政府债券 at **19.9%** of the stock (+1.4pp yoy); end-Sep-2024 政府债券 at **21.2%** (+2.1pp yoy);
end-Apr-2026 TSF stock +7.8% yoy.

**The obvious mirror does NOT work.** `ak.macro_china_shrzgm()` hits
`POST https://data.mofcom.gov.cn/datamofcom/front/gnmy/shrzgmQuery` 🟡 — but its column set is the
**pre-2019 flow** taxonomy: 社会融资规模增量, 人民币贷款, 外币贷款, 委托贷款, 信托贷款, 未贴现银行承兑汇票,
企业债券, 非金融企业境内股票融资. **There is no 政府债券 column and no stock table.** ✅ (read out of
the akshare source). This is a real dead end — do not plan around it.

**Feasibility verdict: Medium.** Easiest tractable path: parse the monthly HTML report for the two
levels you need (TSF stock, 政府债券余额), carry 13 months, and compute
`yoy_ex_govt = (stock_t − govt_t) / (stock_{t-12} − govt_{t-12}) − 1`. Fall back to the PDF table
when the article phrasing changes.

---

### 2.8 `credit_spread_aa` — 3Y AA+ medium-term note yield (for the spread over CGB)

This is the one with the most confirmed API surface — and the one where a single string is still
missing.

**Critical structural finding: the free ChinaBond feed you already use does NOT carry AA+.** ✅
`ak.bond_china_yield()` calls
`https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/historyQuery?startDate=…&endDate=…&gjqx=0&qxId=ycqx&locale=cn_ZH` 🟡
and its documented output contains exactly three curve names:

```
中债国债收益率曲线
中债中短期票据收益率曲线(AAA)
中债商业银行普通债收益率曲线(AAA)
```
✅ (read verbatim out of akshare's own documented sample output). Columns are `曲线名称, 日期, 3月,
6月, 1年, 3年, 5年, 7年, 10年, 30年`; `start_date`→`end_date` must be **< 1 year** per call. That
`cbweb-pbc-web` path is the *PBoC column* of ChinaBond and is deliberately limited to the small set
PBoC republishes. **AA+ is not there. Stop looking for it on that endpoint.**

Also note the `qxId` / `gjqx` params generalise: a live ChinaBond URL of the form
`.../cbweb-pbc-web/pbc/historyQuery?startDate=2022-04-01&endDate=2023-03-24&gjqx=10&qxId=hzsylqx&locale=en_US` ✅
exists, so `qxId` selects the curve family and `gjqx` the tenor. ⚠️ The value of `qxId` for the MTN
family was not determined.

**Route A — CFETS `ClsYldCurvHis` (the endpoint your fetcher already works against).**

```
GET https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/ClsYldCurvHis
  params: lang=CN
          reference=1,2,3
          bondType=<curve code>
          startDate=YYYY-MM-DD
          endDate=YYYY-MM-DD
          termId=<0.1 | 0.5 | 1>          # maturity-grid spacing, NOT the tenor
          pageNum=1
          pageSize=50
  → data_json["records"] → 日期, 期限, 到期收益率, 即期收益率, 远期收益率
```
🟡 (akshare `bond_china_close_return`). `bondType` is a **code**, not the Chinese label; akshare
resolves label→code at runtime via:

```
GET https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/ClsYldCurvCurvGO
  → data_json["records"] → [{cnLabel, value}, …]     # value IS the bondType code
  headers must include Referer: https://www.chinamoney.com.cn/chinese/bkcurvclosedyhis/?bondType=CYCC000&reference=1
                       X-Requested-With: XMLHttpRequest, Origin, Host
```
🟡

**The exact Chinese curve name.** CFETS's `cnLabel` convention is **short**, without the 中债 prefix:
confirmed examples in production use are `国债`, `政策性金融债(进出口行)` ✅ and — already working in
this repo — `同业存单(AAA)`. CFETS's own description of the closing-curve family is ✅:

> 债券收盘收益率曲线包括国债、央行票据、政策性金融债、**中短期票据各信用评级**、企业债各信用评级、
> 同业存单各信用评级、商业银行普通金融债各信用评级、商业银行二级资本债各信用评级、资产支持证券各信用评级、
> 证券公司短期融资券各信用评级、定向工具各信用评级

and CFETS has published a notice titled 「关于发布证券公司短期融资券（**AAA、AA+、AA**）收盘收益率曲线的通知」 ✅
(`https://iftp.chinamoney.com.cn/chinese/rdgz/20211110/2098160.html`), confirming the parenthetical
rating suffix is CFETS's own naming.

⇒ **The AA+ medium-term-note label is almost certainly `中短期票据(AA+)`.** ⚠️ **unverified as an exact
string** — the egress proxy 403'd `chinamoney.com.cn`, `iftp.chinamoney.com.cn` and
`chinamoney.org.cn` this session, so `ClsYldCurvCurvGO` could not be read.
**Confirmation procedure (30 seconds with network):** call `ClsYldCurvCurvGO`, then
`[r for r in records if "中短期票据" in r["cnLabel"]]` and take the one ending `(AA+)`.
A search result also surfaced `bondType=CYCC41A` on a live `bkcurvclosedy` URL ✅ — the code is real,
but **which curve it maps to is unverified**; resolve it from `ClsYldCurvCurvGO`, never hard-code it.

**Hard constraint on Route A:** akshare documents that `ClsYldCurvHis`
**「只能获取近 3 个月的数据，且每次获取的数据不超过 1 个月」** — *only the last 3 months, max 1 month per
call* ✅. **You cannot backfill history from CFETS.** It is a forward-accumulating feed only.

**Route B — ChinaBond `searchYc` (this is how you get history).** A production GitHub client
(`jy-zhang-sig/bond-yield-curve`, `ci_update.py`) fetches ChinaBond curves back to **2013-01-01** via:

```
POST https://yield.chinabond.com.cn/cbweb-mn/yc/searchYc
  form: xyzSelect=txy
        workTimes=<YYYY-MM-DD>        # one POST per date
        dxbj=0
        qxll=<0 | 1>                  # 0 = 到期收益率 (YTM), 1 = 即期利率 (spot)
        yqqxN=N
        yqqxK=K
        ycDefIds=<guid>[,<guid>…]     # comma-joined curve GUIDs
        wrjxCBFlag=0
        locale=zh_CN
```
🟡 — with the curve tree discoverable at `https://yield.chinabond.com.cn/cbweb-mn/yc/queryTree` ✅.

**Verified `ycDefIds` GUIDs** (read verbatim from that client) 🟡:

| Curve | `ycDefId` |
|---|---|
| 中债国债 | `2c9081e50a2f9606010a3068cae70001` |
| 中债国开债 | `8a8b2ca037a7ca910137bfaa94fa5057` |
| 中债铁道债 | `2c9081e91b55cc84011c25e7977b4dac` |
| **中债企业债(AAA)** | `2c9081e50a2f9606010a309f4af50111` |
| **中债企业债(AA)** | `2c90818812b319130112c279222836c3` |
| **中债企业债(A)** | `2c9081e91e6a3313011e6d438a58000d` |
| 中债进出口行债 | `8a8b2ca0567e033b01567ea9c1d96af8` |
| 中债农发行债 | `2c9081e50a2f9606010a306abdde0003` |
| 中国地方政府债 | `998183ff8c00f640018c32d4721a0d16` |

⚠️ The GUID for **中债中短期票据收益率曲线(AA+)** is **not** in that list — fetch `queryTree` once and
read it off. Operational gotcha ✅: **地方政府债 must be requested on its own** — batching it into a
multi-`ycDefIds` request makes ChinaBond return only that curve and silently drop/misalign the others.

**Naming difference to keep straight:** ChinaBond labels are long (`中债中短期票据收益率曲线(AAA)`),
CFETS labels are short (`同业存单(AAA)`). They are different publishers with different curve
methodologies — ChinaBond's MTN(AAA) curve samples AAA 超短期融资券 + 短期融资券 + 中期票据 ✅.
**Do not splice a ChinaBond history onto a CFETS live tail** without documenting the join.

**Publication timing ✅:** CFETS publishes the day's closing curves at **17:15 on each business day**.
ChinaBond publishes once at end of business day.

**Cross-check value ✅:** ChinaBond MTN(AAA) 3Y = **1.94%** on 2025-08-19.

**Feasibility verdict: Medium.** One confirmed 30-second lookup (`ClsYldCurvCurvGO`) unblocks the
live series on the endpoint you already have; a second endpoint (`searchYc`) gives the history at
one POST per date.

---

### 2.9 `cfets` — CFETS RMB exchange-rate index

| Field | Value |
|---|---|
| **Official publisher** | 中国外汇交易中心 (CFETS) |
| **Official page** | **`https://www.chinamoney.com.cn/chinese/bkrmbidx/`** ✅ ("人民币汇率指数") — mirrors at `https://www.chinamoney.org.cn/chinese/bkrmbidx/` and `https://www.shibor.org/chinese/rmbsindx/` ✅ |
| **Exact index name** | **CFETS人民币汇率指数** ✅ (published alongside 参考BIS货币篮子 and 参考SDR货币篮子 indices) |
| **Frequency & lag — verified verbatim ✅** | 「交易中心于银行间外汇市场**每周首个交易日08:30发布上周最后交易日**指数数据，**每月首个交易日08:30发布上月最后交易日**指数数据」 — i.e. **weekly, published Monday 08:30 for the previous Friday**, plus a month-end value on the first trading day of the new month. The official publication channel is 中国货币网. |
| **Base** | 2014-12-31 = 100; geometric mean; basket priced off the daily 人民币汇率中间价 ✅ |
| **Basket revisions** | The basket and weights are reset periodically by announcement — most recently effective **2026-01-01** ✅ (announcement: `https://www.chinamoney.com.cn/chinese/zxpl/20251231/3260978.html` ✅). Methodology note v1.4: `https://www.chinamoney.com.cn/chinese/zxpl/20211231/2276204.html` ✅. **Your series will have level-continuous but composition-discontinuous joins at each reset — record the reset dates.** |
| **Format** | **HTML parse.** No public JSON/CSV endpoint was found. ⚠️ |

**Machine-readable route: none confirmed.** CFETS's documented programmatic offerings (**CMDS Pro**,
**CSTP**) are member-institution services requiring registration and approval ✅ — not an open API.
A GitHub-wide code search for `bkrmbidx` / `RmbIndex` / `cm-u-bk-ccpr` returned **zero** hits ✅.
`akshare` has no function for this index ✅.

**Two things worth one probe each when you have network** (both cheap, both would collapse this to Easy):
1. The `cm-u-bk-currency` family serves CSV variants for other series —
   `https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/LprChrtCSV?startDate=2019-01-01` 🟡 returns
   `data.csv`, and `frr-chrt.csv` / `fdr-chrt.csv` exist under
   `https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/currency/` 🟡. **An analogous
   `…/data/fx/` CSV for the RMB index may exist** — inspect the network tab on `bkrmbidx` once. ⚠️
2. `research/05-data-sources.md` records a `bmkidxrud` article-list route ✅ for parsing the weekly
   post — usable as the fallback.

**Third-party mirrors (flag reliability):** CEIC carries `RMB Exchange Rate Index: CFETS Currency
Basket` ✅ (paid). NDRC republished a snapshot ✅ (`https://www.ndrc.gov.cn/fgsj/tjsj/ssjj/202203/t20220331_1321467.html`)
— a one-off, not a feed. 汇率网 `https://www.huilvwang.com/CFETS.html` ✅ is an unofficial scrape;
**do not use it as a system of record.**

**Feasibility verdict: Medium.** Weekly cadence and a single number per print mean even a brittle
HTML parser is manageable; the 2015-12 start gives ~560 observations.

---

### 2.10 `govt_bond_issuance` — monthly government bond issuance (国债 + 地方政府债)

You must decide *which* of three different quantities you want. They are not interchangeable.

| Concept | Meaning | Best source |
|---|---|---|
| **Gross issuance** (发行量) | Face value sold in the month, incl. refinancing/rollover | MOF 预算司 (local) + MOF 国库司 (central); CFETS `bnBondEmit` for a forward-looking plan |
| **Net financing** (净融资) | Issuance − maturities. **This is the liquidity-relevant number.** | **PBoC TSF flow table, 政府债券 line** |
| **Special-bond quota** (专项债额度) | The annual NPC-approved ceiling and its in-year usage | MOF 预算司 monthly reports + the annual budget report |

**Recommended primary route — the TSF increment table.** ✅ The monthly
**社会融资规模增量统计表** carries a **政府债券** line which is, by construction, **net government bond
financing (国债 + 地方政府一般债 + 地方政府专项债, net of maturities)**. PBoC states it directly in the
monthly narrative — verified print ✅: 「前四个月**政府债券净融资4.45万亿元**，同比少39.9亿元」 (Jan–Apr 2026,
cumulative YTD). Table asset ✅: `https://www.pbc.gov.cn/diaochatongjisi/attachDir/2025/11/2025110511302392865.pdf`
(unit 亿元). **This is one line of a table you already have to parse for `tsf_ex_govt_yoy`** — build
both from the same parser. Note the narrative figures are **cumulative YTD**; difference them.

**Secondary routes (official, gross, per-leg):**

| Leg | Publisher & page | Notes |
|---|---|---|
| 地方政府债 | **MOF 预算司 → 地方政府债务管理 → 数据统计**: `https://yss.mof.gov.cn/zhuantilanmu/dfzgl/sjtj/` ✅ (paged: `.../sjtj/index_1.htm` ✅). Monthly report per month, e.g. `https://yss.mof.gov.cn/zhuantilanmu/dfzgl/sjtj/202503/t20250328_3960903.htm` ✅ | Title pattern: **「YYYY年M月地方政府债券发行和债务余额情况」** ✅. Gives 发行 split 新增/再融资 × 一般/专项, plus 债务余额. Verified print ✅: Feb-2026 新增地方政府债券 6,061億元 = 一般债 1,496億 + 专项债 4,565億. Lag ~3–4 weeks. **HTML.** |
| 国债 (central) | **MOF 国库司 → 统计数据**: `https://gks.mof.gov.cn/tongjishuju/` ✅ — carries「中央政府月度收支及融资数据和季度债务余额情况」✅ (the SDDS-style central-government financing release). Auction-level announcements: 记账式国债 `https://gks.mof.gov.cn/ztztz/guozaiguanli/gzfxzjs/` ✅, 储蓄国债 `https://gks.mof.gov.cn/ztztz/guozaiguanli/gzfxdzs/` ✅, 工作动态 `https://gks.mof.gov.cn/ztztz/guozaiguanli/gzfxgzdt/` ✅ | **HTML.** Monthly for the aggregate; per-auction for the detail. |
| 债务管理司 | `https://zwgls.mof.gov.cn/` ✅ | Local-government debt balance and quota reporting. |
| Both, forward-looking | **CFETS `bnBondEmit`**: `POST https://www.chinamoney.com.cn/ags/ms/cm-u-bond-an/bnBondEmit` with form `enty, bondType, bondNameCode, leadUnderwriter, pageNo, pageSize` 🟡 (= `ak.macro_china_bond_public()`). Returns 债券全称, 债券类型, 发行日期, 债券期限, 计划发行量, 债券评级 🟡 | Filter 债券类型 to 国债/地方政府债 and aggregate to monthly **gross** issuance. Page: `https://www.chinamoney.com.cn/chinese/xzjfx/` ✅ |
| Per-bond disclosure | 中国地方政府债券信息公开平台 `https://www.celma.org.cn/zqxx/index.jhtml` ✅ | Month/quarter/year data on local bonds; structure unexamined ⚠️ |

**Frequency / lag:** monthly; the TSF route lands with the 金融统计数据报告 (~12th–15th of the
following month ✅); the MOF routes land ~3–4 weeks after month end ✅.

**Feasibility verdict: Medium.** Take the net-financing definition off the TSF table (free ride on
the §2.7 parser) and treat the MOF pages as the gross/quota decomposition when you need it.

---

## 3. Exact parameters found

Everything below was read verbatim this session. **Nothing here is invented.** Marks as in §0.

### 3.1 Sina Finance — monetary authority balance sheet (→ `fiscal_deposits`)
```
GET https://quotes.sina.cn/mac/api/jsonp_v3.php/SINAREMOTECALLCALLBACK1601651495761/MacPage_Service.get_pagedata
    cate=fininfo
    event=8            # 8 = 央行货币当局资产负债 ; 1 = 货币供应量 ; 5 = 外汇储备/黄金 ; 19 = 保险业经营情况
    from=0             # step by `num`
    num=31
    condition=
```
🟡 JSONP. `count` → total rows; `page_num = ceil(count/31)`; rows in `data`;
**column labels in `config.all` as `[code, label]` pairs** — resolve `政府存款` by label at runtime.
Human page: `https://finance.sina.com.cn/mac/#fininfo-8-0-31-2` ✅

### 3.2 CFETS closing yield curves (→ `credit_spread_aa`)
```
GET https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/ClsYldCurvCurvGO
    (headers: Referer=https://www.chinamoney.com.cn/chinese/bkcurvclosedyhis/?bondType=CYCC000&reference=1,
              X-Requested-With=XMLHttpRequest, Origin=https://www.chinamoney.com.cn,
              Host=www.chinamoney.com.cn)
    → records[] = {cnLabel, value}          # `value` is the bondType code
```
```
GET https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/ClsYldCurvHis
    lang=CN
    reference=1,2,3
    bondType=<value from ClsYldCurvCurvGO>
    startDate=YYYY-MM-DD
    endDate=YYYY-MM-DD          # ≤ 1 month span; only last 3 months available at all
    termId=<0.1|0.5|1>
    pageNum=1
    pageSize=50
    → records[] → 日期, 期限, 到期收益率, 即期收益率, 远期收益率   (drop `newDateValue`)
```
🟡 both. Known-good `cnLabel` values in production: `国债` ✅, `政策性金融债(进出口行)` ✅,
`同业存单(AAA)` (already working in this repo).
**Target label: `中短期票据(AA+)` ⚠️ unverified — confirm via `ClsYldCurvCurvGO`.**
Seen-in-the-wild bondType codes: `CYCC000` ✅ (the 国债 default on the reference URL),
`CYCC41A` ✅ (curve mapping **unverified**).
Publication time: **17:15 每工作日** ✅.

### 3.3 ChinaBond — PBoC-column curve history (CGB / MTN-AAA / commercial-bank-AAA only)
```
GET https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/historyQuery
    startDate=YYYY-MM-DD
    endDate=YYYY-MM-DD      # span must be < 1 year
    gjqx=0                  # 0 → all tenors as columns; e.g. gjqx=10 seen on a live URL
    qxId=ycqx               # curve family; `qxId=hzsylqx` also seen live ✅ (mapping unverified)
    locale=cn_ZH
    → HTML; pd.read_html(...)[1]
    → 曲线名称, 日期, 3月, 6月, 1年, 3年, 5年, 7年, 10年, 30年
```
🟡. **Curve names returned: only `中债国债收益率曲线`, `中债中短期票据收益率曲线(AAA)`,
`中债商业银行普通债收益率曲线(AAA)`** ✅ — **no AA+.**

### 3.4 ChinaBond — full curve library with history (→ `credit_spread_aa` backfill)
```
GET  https://yield.chinabond.com.cn/cbweb-mn/yc/queryTree          # curve tree → ycDefIds
POST https://yield.chinabond.com.cn/cbweb-mn/yc/searchYc
     xyzSelect=txy
     workTimes=YYYY-MM-DD          # one POST per date
     dxbj=0
     qxll=0                        # 0 = 到期收益率 (YTM) ; 1 = 即期利率 (spot)
     yqqxN=N
     yqqxK=K
     ycDefIds=<guid>[,<guid>,…]
     wrjxCBFlag=0
     locale=zh_CN
     → JSON list
```
🟡. Verified `ycDefIds`:
`中债国债 2c9081e50a2f9606010a3068cae70001` ·
`中债国开债 8a8b2ca037a7ca910137bfaa94fa5057` ·
`中债铁道债 2c9081e91b55cc84011c25e7977b4dac` ·
`中债企业债(AAA) 2c9081e50a2f9606010a309f4af50111` ·
`中债企业债(AA) 2c90818812b319130112c279222836c3` ·
`中债企业债(A) 2c9081e91e6a3313011e6d438a58000d` ·
`中债进出口行债 8a8b2ca0567e033b01567ea9c1d96af8` ·
`中债农发行债 2c9081e50a2f9606010a306abdde0003` ·
`中国地方政府债 998183ff8c00f640018c32d4721a0d16`.
**Gotcha:** request `中国地方政府债` alone — batching it drops/misaligns the other curves ✅.
Working history in that client starts **2013-01-01** ✅.

### 3.5 CFETS — OMO structured table (STALE; probe only)
```
POST https://www.chinamoney.com.cn/ags/ms/cm-u-bond-publish/TicketHandle
     form: pageSize=15, pageNo=<n>
     headers: Referer=https://www.chinamoney.com.cn/chinese/yhgkscczh/
              X-Requested-With=XMLHttpRequest
              Content-Type=application/x-www-form-urlencoded; charset=UTF-8
     → data.pageTotal, data.resultList → 操作日期, 期限, 交易量, 中标利率, 正/逆回购
```
🟡. Coverage was **2004-01-16 →**. **Deprecated upstream with the note 「由于目标网站未更新数据」** ✅ —
assume stale until a live probe says otherwise. Page still live: `https://www.chinamoney.com.cn/chinese/yhgkscczh/` ✅

### 3.6 PBoC OMO crawl (→ `net_injection_3m`, `outright_repo`)
```
Daily trade announcements : https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/index.html
Archive pagination        : https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/17081-{page}.html
Outright reverse repo     : https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/5492845/index.html
Notices (non-trade)       : https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125469/index.html
Parent column             : https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/index.html
```
✅ all. Listing markup ✅:
```
anchor : <a href="/zhengcehuobisi/125207/125213/125431/125475/<digits>/index.html"
            onclick="void(0)" target="_blank" title="公开市场业务交易公告 [2026]第78号" istitle="true">
date   : <span class="hui12">2026-04-24</span>
```
**Since 2025 the index is plain static HTML — the `/17081/` subfolder and the `atob(...)` JS redirect
are gone; no headless browser needed.** ✅ Dedupe: the same URL appears in both mobile and desktop
markup ✅, and a handful of 2008 announcements are genuinely duplicated under two node ids ✅.

### 3.7 MOFCOM TSF mirror — what it does NOT contain
```
POST https://data.mofcom.gov.cn/datamofcom/front/gnmy/shrzgmQuery      (= ak.macro_china_shrzgm)
 → 月份, 社会融资规模增量, 其中-人民币贷款, 其中-委托贷款外币贷款, 其中-委托贷款,
   其中-信托贷款, 其中-未贴现银行承兑汇票, 其中-企业债券, 其中-非金融企业境内股票融资
```
🟡. **No 政府债券 column; flow only, no stock.** ✅ Unusable for `tsf_ex_govt_yoy` and for
`govt_bond_issuance`. Page: `https://data.mofcom.gov.cn/gnmy/shrzgm.shtml` ✅

### 3.8 CFETS forward bond issuance (→ `govt_bond_issuance`, gross)
```
POST https://www.chinamoney.com.cn/ags/ms/cm-u-bond-an/bnBondEmit    (= ak.macro_china_bond_public)
     form: enty, bondType, bondNameCode, leadUnderwriter, pageNo, pageSize
     → 债券全称, 债券类型, 发行日期, 债券期限, 计划发行量, 债券评级
```
🟡. Page: `https://www.chinamoney.com.cn/chinese/xzjfx/` ✅

### 3.9 NBS new-site JSON API (general-purpose fallback; annual only for the credit table)
```
GET https://data.stats.gov.cn/dg/website/publicrelease/web/external/new/queryIndexTreeAsync   ?pid=&code=<int>
GET https://data.stats.gov.cn/dg/website/publicrelease/web/external/new/queryIndicatorsByCid  ?cid=&dt=&name=
GET https://data.stats.gov.cn/dg/website/publicrelease/web/external/getDaCatalogTreeByIndicatorCid ?indicatorCid=
GET https://data.stats.gov.cn/dg/website/publicrelease/web/external/getDasByDaCatalogId       ?daCid=
GET https://data.stats.gov.cn/dg/website/publicrelease/web/external/stream/esData
    headers: Origin=https://data.stats.gov.cn
             Referer=https://data.stats.gov.cn/dg/website/page.html#/pc/national/monthData
```
🟡 (= `akshare/economic/macro_china_nbs.py`). Relevant table:
`金融机构人民币信贷收支(年底余额)` = `https://data.stats.gov.cn/tablequery.htm?code=AD08` ✅ —
**annual year-end only**, not usable for §2.5/§2.6.

### 3.10 Exchange-repo proxy (→ `overnight_repo_share`, proxy only)
```
ak.bond_buy_back_em()                 # 东方财富网-行情中心-债券市场-上证/深证 质押式回购 (spot)
ak.bond_buy_back_hist_em(symbol=…)    # 质押式回购-历史数据
```
🟡 (`akshare/bond/bond_buy_back_em.py`). **Exchange repo, not interbank — a proxy, clearly labelled.**

### 3.11 PBoC document-asset path conventions
```
Statistics hub          : https://www.pbc.gov.cn/diaochatongjisi/116219/116319/index.html
Per-year credit stats   : https://www.pbc.gov.cn/diaochatongjisi/116219/116319/{YYYY}ntjsj/jrjgxdsztj/index.html
Monetary overview 2025  : https://www.pbc.gov.cn/diaochatongjisi/116219/116319/5570903/5570886/index.html
Monetary overview 2024  : https://www.pbc.gov.cn/diaochatongjisi/116219/116319/5225358/5225360/index.html
TSF landing             : https://www.pbc.gov.cn/diaochatongjisi/116219/116319/3959050/3959051/index.html
Table assets (PDF)      : https://www.pbc.gov.cn/diaochatongjisi/attachDir/{YYYY}/{MM}/{timestamp}.pdf
Legacy assets (HTML)    : https://www.pbc.gov.cn/eportal/fileDir/.../resource/cms/{YYYY}/{MM}/{timestamp}.htm|.pdf
Monthly releases        : https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/{node}/index.html
```
✅ all. **There is no stable slug at any level — the year node ids are opaque and change annually, so
you must crawl the hub each year.** ✅ The sub-domain `camlmac.pbc.gov.cn` serves an identical
`diaochatongjisi/...` tree ✅ and is worth keeping as a fallback host.

---

## 4. What is genuinely not machine-readable

| Indicator | The blocker |
|---|---|
| `overnight_repo_share` | Interbank repo turnover **by tenor** is not published in any free machine-readable form. CFETS's programmatic feeds (CMDS Pro, CSTP) are approval-gated member services ✅. The ratio itself appears only as a **cumulative-YTD sentence in the quarterly MPR PDF**. |
| `household_time_deposit_share` | The 金融机构人民币信贷收支表 is **PDF-only** for recent vintages; NBS mirrors it annually only; no Sina/EastMoney mirror found. |
| `tsf_ex_govt_yoy` / `govt_bond_issuance` (net) | The 社会融资规模存量/增量统计表 are **PDF**, with a parallel HTML narrative. Tractable, but no structured feed exists — and the one obvious mirror (MOFCOM) is on the pre-2019 taxonomy and lacks 政府债券 entirely ✅. |
| `net_injection_3m`, `outright_repo` | HTML-only by design. The one structured mirror that existed (CFETS `TicketHandle`) is documented upstream as no longer updating ✅. |
| `cfets` | HTML-only; no public JSON found anywhere, including a zero-hit GitHub-wide code search ✅. |

---

## Sources

**PBoC — statistics**
- https://www.pbc.gov.cn/diaochatongjisi/116219/index.html
- https://www.pbc.gov.cn/diaochatongjisi/116219/116319/index.html
- https://www.pbc.gov.cn/diaochatongjisi/116219/116319/5570903/5570886/index.html
- https://www.pbc.gov.cn/diaochatongjisi/116219/116319/5225358/5225360/index.html
- https://www.pbc.gov.cn/diaochatongjisi/116219/116319/116357/116514/index.html
- https://camlmac.pbc.gov.cn/diaochatongjisi/116219/116319/2026ntjsj/jrjgxdsztj/index.html
- https://www.pbc.gov.cn/diaochatongjisi/116219/116319/3959050/3959051/index.html
- https://www.pbc.gov.cn/diaochatongjisi/attachDir/2025/12/2025121517172659799.pdf (货币当局资产负债表)
- https://www.pbc.gov.cn/diaochatongjisi/attachDir/2025/11/2025111817164135629.pdf (金融机构人民币信贷收支表)
- https://www.pbc.gov.cn/diaochatongjisi/attachDir/2025/11/2025111817284449935.pdf (存款类金融机构人民币信贷收支表)
- https://www.pbc.gov.cn/diaochatongjisi/attachDir/2025/11/2025110511314347909.pdf (社会融资规模存量统计表)
- https://www.pbc.gov.cn/diaochatongjisi/attachDir/2025/11/2025110511302392865.pdf (社会融资规模增量统计表)
- https://www.pbc.gov.cn/eportal/fileDir/diaochatongjisi/resource/cms/2022/04/2022041816440579530.pdf
- https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2964272/2015101616080058336.pdf
- http://www.pbc.gov.cn/diaochatongjisi/116219/116225/5565443/index.html

**PBoC — open market operations**
- https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/index.html
- https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/index.html
- https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125469/index.html
- https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/5630091/index.html
- https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/5492845/index.html
- https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/5492845/5646939/index.html
- https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/5492845/5730066/index.html

**PBoC — reports**
- https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/5877760/index.html (2025Q3 金融机构贷款投向统计报告)
- http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/5221508/index.html (2023 金融机构贷款投向统计报告)
- https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/5238308/2024030610591528512.pdf (2023Q4 MPR)
- https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2026051118520164705/2026051118500062162.pdf (2026Q1 MPR)
- https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/5427706/2024080916563291755.pdf (2024Q2 MPR)
- https://cif.mofcom.gov.cn/cif/html/upload/20260211143114167_2025年第四季度中国货币政策执行报告.pdf
- https://cif.mofcom.gov.cn/cif/html/upload/20250818093335312_中国货币政策执行报告2025年第二季度.pdf
- https://cif.mofcom.gov.cn/cif/html/upload/20251124101800795_中国货币政策执行报告2025年第三季度.pdf
- https://cif.mofcom.gov.cn/cif/html/upload/20250512102012618_2025年第一季度中国货币政策执行报告.pdf
- https://www.gov.cn/lianbo/bumen/202505/content_7025931.htm
- https://www.gov.cn/lianbo/bumen/202509/content_7040523.htm
- https://jrj.sh.gov.cn/SCGK194/20260430/46e28e4180c54d11b859e525b247fc40.html
- https://jrj.sh.gov.cn/SCGK194/20250115/36eace10c61a457aa2b7d9836445faa9.html
- https://finance.sina.com.cn/money/bank/2026-04-29/doc-inhwefva7716527.shtml
- https://finance.sina.com.cn/jjxw/2026-05-14/doc-inhxwenh8738944.shtml

**CFETS / 中国货币网**
- https://www.chinamoney.com.cn/chinese/bkrmbidx/
- https://www.chinamoney.com.cn/chinese/zxpl/20251231/3260978.html (basket reweight, effective 2026-01-01)
- https://www.chinamoney.com.cn/chinese/zxpl/20211231/2276204.html (index methodology v1.4)
- https://www.chinamoney.com.cn/chinese/bkcurvclosedy/
- https://www.chinamoney.org.cn/chinese/bkcurvclosedy/?bondType=CYCC41A
- https://www.chinamoney.com.cn/chinese/bkcurvclosedyhis/index.html?bondType=CYCC000&reference=1
- https://iftp.chinamoney.com.cn/chinese/bkcurvclosedy/
- https://iftp.chinamoney.com.cn/chinese/rdgz/20211110/2098160.html (证券公司短期融资券 AAA/AA+/AA curves notice)
- https://www.chinamoney.com.cn/chinese/yhgkscczh/
- https://www.chinamoney.org.cn/chinese/scggyhywgggksccz/20250324/3075425.html
- https://www.chinamoney.com.cn/chinese/mkdatapm/
- https://www.chinamoney.org.cn/chinese/mtdexdaily/
- https://www.chinamoney.com.cn/chinese/dataInterfaceService/
- https://www.chinamoney.com.cn/chinese/xzjfx/
- https://www.shibor.org/chinese/rmbsindx/

**ChinaBond**
- https://yield.chinabond.com.cn/
- https://yield.chinabond.com.cn/cbweb-pbc-web
- https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/historyQuery?startDate=2022-04-01&endDate=2023-03-24&gjqx=10&qxId=hzsylqx&locale=en_US
- https://yield.chinabond.com.cn/cbweb-mn/yield_main?locale=zh_cN
- https://www.chinabond.com.cn/zzsj/zzsj_zzjgcp/zzjgcp_cpxz/cpxz_qxxz/qxxz_zzzdqpjqx/ (中债中短期票据曲线(AAA))
- https://yield.chinabond.com.cn/cbweb-czb-web/czb/moreInfo?locale=cn_ZH&nameType=1

**MOF**
- https://gks.mof.gov.cn/tongjishuju/
- https://gks.mof.gov.cn/ztztz/guozaiguanli/
- https://gks.mof.gov.cn/ztztz/guozaiguanli/gzfxzjs/
- https://gks.mof.gov.cn/ztztz/guozaiguanli/gzfxdzs/
- https://gks.mof.gov.cn/ztztz/guozaiguanli/gzfxgzdt/
- https://yss.mof.gov.cn/zhuantilanmu/dfzgl/sjtj/
- https://yss.mof.gov.cn/zhuantilanmu/dfzgl/sjtj/index_1.htm
- https://yss.mof.gov.cn/zhuantilanmu/dfzgl/sjtj/202503/t20250328_3960903.htm
- https://zwgls.mof.gov.cn/
- https://www.celma.org.cn/zqxx/index.jhtml

**NBS / MOFCOM / other official**
- https://data.stats.gov.cn/tablequery.htm?code=AD08
- https://data.stats.gov.cn/easyquery.htm?cn=A01
- https://www.stats.gov.cn/zs/tjws/zytjzbqs/hbgyl/202410/t20241025_1957180.html
- https://www.stats.gov.cn/sj/zbjs/202302/t20230202_1897092.html
- https://data.mofcom.gov.cn/gnmy/shrzgm.shtml
- https://www.ndrc.gov.cn/fgsj/tjsj/ssjj/202203/t20220331_1321467.html

**Open-source clients read for endpoint strings**
- https://github.com/akfamily/akshare — `akshare/economic/macro_china.py`, `akshare/economic/macro_china_nbs.py`, `akshare/bond/bond_china_money.py`, `akshare/bond/bond_china.py`, `akshare/bond/bond_buy_back_em.py`, `docs/data/bond/bond.md`
- https://github.com/yuanshj1123/quant-akshare — pre-removal `macro_china_gksccz()` body (CFETS `TicketHandle`)
- https://github.com/jy-zhang-sig/bond-yield-curve — `ci_update.py` (ChinaBond `searchYc` params + `ycDefIds`)
- https://github.com/openakita/openakita — `plugins/fin-pulse/finpulse_fetchers/pbc_omo.py` (PBoC OMO listing markup, 2025 layout change)
- https://github.com/ericxuzhesheng/Bond-Futures-Data-Monitor — `bond_futures_monitor/collectors/open_market.py` (`17081-{page}.html` pagination)
- https://github.com/kampfer/various-data — `src/crawlers/python/omo.py`, `omo2.py` (archive duplicates)
- https://github.com/fzhulitov/cfets — generic `cm-u-bk-currency/<code>` client

**Third-party mirrors (reliability flagged in-text — not systems of record)**
- https://finance.sina.com.cn/mac/ · http://money.finance.sina.com.cn/mac/view/
- https://www.huilvwang.com/CFETS.html
- https://www.ceicdata.com/zh-hans/china/exchange-rate-index/cn-rmb-exchange-rate-index-cfets-currency-basket
- https://guoyanwang.clcn.net.cn/DRCNet.Mirror.Documents.Web/DocSummary.aspx?DocID=8189606&leafID=17583
