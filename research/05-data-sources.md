# China Monetary & Liquidity Tracker — Data Sourcing Manual

**Purpose.** This is the operational companion to `data/seed/series.json`. It tells you, for every indicator in `data/registry_monetary.json`, `data/registry_liquidity.json` and `data/registry_context.json`, **who publishes it, at exactly what URL, whether a machine-readable endpoint exists, what the series ID is, the frequency, the release lag, and how far back the history goes** — plus authentication, rate limits and redistribution constraints.

**Date of compilation:** 13 September 2026.

---

## 0. How to read this document

### 0.1 Verification legend

| Mark | Meaning |
|---|---|
| ✅ **verified** | The string (series ID, endpoint, parameter, date) was read this session out of a retrieved source — a search-engine result page that quoted the publisher, or source code retrieved from GitHub. |
| 🟡 **code-verified, not live-tested** | The endpoint URL and its parameters were read verbatim out of a working open-source client's source code (almost always `akshare`). The URL string is real and is what that library calls in production. **This session could not issue the request**, so the live response shape is not confirmed. |
| ⚠️ **unverified** | Plausible, and in most cases the practitioner-standard answer, but **not** confirmed against any source this session. Do not build on it without checking. |

### 0.2 Environment constraint that shaped this document

**The sandbox in which this manual (and `series.json`) was built has no usable outbound network.** The egress proxy returns 403 for essentially every macro-data host. Verified as blocked this session: `fred.stlouisfed.org` (both the HTML pages and the CSV endpoint). Previously recorded as blocked when `series.json` was built: NBS, PBoC, ChinaBond, CFETS, BIS, IMF, World Bank, East Money.

Consequences you must understand:

1. **Do not attempt `curl` from this sandbox.** It will fail, and the failure tells you nothing about whether the endpoint is good.
2. Only two channels worked: a **web search tool** (returns publisher-quoted snippets) and **direct file reads from `github.com` / `raw.githubusercontent.com`**.
3. That is why so much below is marked 🟡 rather than ✅: the most reliable way to learn China's real data endpoints from inside this box was to **read the source code of the Python clients that call them**. That is a genuinely good source for the *URL string and parameter names* and a bad source for *whether the service is up today*.
4. **Anyone productionising this should open every URL in this document once, by hand, before wiring a scraper.**

### 0.3 The one structural fact that drives everything

China has **no single machine-readable macro API**. The authoritative publishers (PBoC, NBS, CFETS, ChinaBond, MOF) publish through **HTML tables, PDFs and Excel files intended for human readers**. The machine-readable endpoints that exist are either (a) undocumented internal JSON/CSV feeds behind those pages, (b) international mirrors (FRED/IMF/BIS/World Bank) that are slower, shorter and sometimes discontinued, or (c) commercial aggregators (Wind, CEIC, Bloomberg) that cost money and forbid redistribution.

**The highest-value series in this tracker — the weighted average lending rate and the excess reserve ratio — exist nowhere except a quarterly PDF.** Plan for that.

---

## 1. Source-by-source reference

### 1.1 People's Bank of China (PBoC) — 中国人民银行

The primary publisher for money, credit, TSF, policy rates, RRR, the central-bank balance sheet, and open market operations.

**Root:** https://www.pbc.gov.cn/ · English: https://www.pbc.gov.cn/en/3688006/index.html

**Machine-readable endpoint: none.** ✅ There is no public PBoC API. Everything is HTML or PDF. Budget for an HTML/PDF parser.

#### 1.1.1 Survey & Statistics Department (调查统计司) — the statistics hub

| Item | URL | Notes |
|---|---|---|
| Statistics hub (all years) | https://www.pbc.gov.cn/diaochatongjisi/116219/116319/index.html | ✅ Entry point. Year-by-year subtrees. |
| 货币统计概览 (Monetary statistics overview) 2025 | https://www.pbc.gov.cn/diaochatongjisi/116219/116319/5570903/5570886/index.html | ✅ Contains 货币当局资产负债表, 其他存款性公司资产负债表, 货币供应量 (M0/M1/M2). |
| 货币统计概览 2024 | https://www.pbc.gov.cn/diaochatongjisi/116219/116319/5225358/5225360/index.html | ✅ |
| 货币统计概览 2019 | https://www.pbc.gov.cn/diaochatongjisi/116219/116319/3750274/3750284/index.html | ✅ Shows the URL pattern is a per-year numeric node — **there is no stable slug**, you must crawl the hub each year. |
| 货币统计概览 (further year node) | https://www.pbc.gov.cn/diaochatongjisi/116219/116319/4780803/4780805/index.html | ✅ |
| 社会融资规模 (TSF) landing | https://www.pbc.gov.cn/diaochatongjisi/116219/116319/3959050/3959051/index.html | ✅ |
| 社会融资规模存量统计表 (example XLS/PDF asset) | https://www.pbc.gov.cn/eportal/fileDir/diaochatongjisi/resource/cms/2022/04/2022041816440579530.pdf | ✅ Unit 万亿元. Shows the `eportal/fileDir/...` asset path convention. |
| 货币当局资产负债表 (example PDF, Dec 2025) | https://www.pbc.gov.cn/diaochatongjisi/attachDir/2025/12/2025121517172659799.pdf | ✅ Unit 亿元. **This is where 政府存款 (fiscal deposits) lives.** |
| 货币当局资产负债表 (legacy HTML, 2009) | https://www.pbc.gov.cn/eportal/fileDir/defaultCurSite/resource/cms/2015/07/2009s04.htm | ✅ Older years are HTML tables, newer are PDF — your parser needs both paths. |
| 2024 年社会融资规模存量统计数据报告 | http://www.pbc.gov.cn/diaochatongjisi/116219/116225/5565443/index.html | ✅ Annual TSF stock report. |

#### 1.1.2 Monthly financial statistics release (金融统计数据报告)

Published under 沟通交流 → 新闻发布, path prefix `goutongjiaoliu/113456/113469/`.

| Example | URL | Release date |
|---|---|---|
| 2025年11月金融统计数据报告 | https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2025121215073692061/index.html | ✅ 2025-12-12 |
| 2026年5月数据报告 | https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2026061214273613328/index.html | ✅ 2026-06-12 |

- **Contents:** M0/M1/M2 (level + YoY), new RMB loans, deposits, TSF flow and TSF stock YoY.
- **Frequency:** monthly. **Release lag:** ✅ the two verified examples both landed on the **12th of the following month**. Practitioner convention is that the print arrives between the 10th and the 15th, sometimes with no pre-announced time. ⚠️ There is no reliable published minute-level calendar; treat the window as 9th–15th and poll.
- **History:** the monthly report series runs back well over a decade on this site; ⚠️ exact earliest node not verified.

#### 1.1.3 Monetary Policy Report (中国货币政策执行报告, "MPR") — the sole source for two indicators

**This is the only publisher of the weighted average lending rate on general loans (一般贷款加权平均利率) and of the excess reserve ratio (超额准备金率).** Neither appears in any monthly statistical release, any NBS table, FRED, BIS, IMF or the World Bank. If you want those two series, you parse this PDF. There is no alternative. ✅ (This is also exactly how the current `walr_general` and `excess_reserve_ratio` series in `series.json` were built.)

- **English index:** https://www.pbc.gov.cn/en/3688229/index.html ✅
- **Chinese PDFs** live under `goutongjiaoliu/113456/113469/<node>/<file>.pdf`, and older ones under `zhengcehuobisi/125207/125227/125957/...`. ✅ There is **no stable URL template** — you must crawl the index and follow the link.

Verified direct PDF URLs (useful as parser fixtures):

| Quarter | PDF | Published |
|---|---|---|
| 2026 Q2 | https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2026081218034520348/2026081218031050203.pdf | ✅ 2026-08-12 |
| 2026 Q1 | https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2026051118520164705/2026051118500062162.pdf | ✅ 2026-05-11 |
| 2025 Q3 | https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/5896222/2025111111175096136.pdf | ✅ 2025-11-11 |
| 2024 Q4 | https://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125957/5347949/ad0bc3efe0234fed8cc6260a134a6e95/2025022618190099812.pdf | ✅ 2025-02-13 |
| 2025 Q2 (provincial mirror) | https://xining.pbc.gov.cn/goutongjiaoliu/113456/113469/2025092212554814094/2025081819132397368.pdf | ✅ 2025-08-15 |
| 2025 Q1 (provincial mirror) | https://xining.pbc.gov.cn/zhengcehuobisi/125207/125227/125957/f5c4690f2cbd40918bf24c2d39ac58af/2025091218344076234/2025081517321679368.pdf | ✅ 2025-05-09 |
| 2024 Q2 | http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/5427706/2025081217013923839.pdf | ✅ 2024-08-09 |

- **Release lag:** ✅ consistently **~6 weeks after quarter end** (Q1 → early/mid May; Q2 → 9–15 Aug; Q3 → ~11 Nov; Q4 → ~13 Feb).
- **Useful trick:** ✅ PBoC **provincial branch sites** (e.g. `xining.pbc.gov.cn`) mirror the same PDFs, and so do MOFCOM (`cif.mofcom.gov.cn`) and Shanghai's financial bureau (`jrj.sh.gov.cn`) — see `research/03-liquidity-indicators.md` §Sources. If the head office site is unreachable or rate-limits you, the mirrors usually are not.
- **What to extract:** 一般贷款加权平均利率, 企业贷款加权平均利率, 个人住房贷款利率, 超额准备金率, 社会融资规模存量 and its YoY, 同业存单发行加权平均利率, core CPI commentary, nominal GDP in 万亿元.
- **Caveat that bit the seed build:** from 2024 Q4 the MPR moved the lending-rate numbers from prose into a table, so a regex tuned on the prose silently stops matching. ✅ (documented in the `walr_general` notes in `series.json`).

#### 1.1.4 Open market operations

| Item | URL |
|---|---|
| 公开市场业务交易公告 (daily OMO trade announcements) | https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/index.html ✅ |
| 公开市场业务公告 (notices) | https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125469/index.html ✅ |
| OMO, English | https://www.pbc.gov.cn/en/3688241/3688765/index.html ✅ |
| DR007 definition, English | https://www.pbc.gov.cn/en/3688006/3689169/3753752/index.html ✅ |

- Each announcement gives the **operation type, tenor, volume and (where published) winning rate**, plus same-day maturities. This is the raw material for `omo_7d`, `net_injection_3m` and `outright_repo`.
- **Frequency:** every business day, typically posted in the morning (⚠️ exact time unverified).
- **Structural warning:** since the 2024–26 framework changes the **MLF and outright reverse repo no longer publish a winning rate** (multi-price tender), so `mlf_1y` has no live level to scrape. See §5.

**Authentication / rate limits:** none published; it is an open website. ⚠️ No documented rate limit, but scrape politely (≤1 req/sec) — the site is known to be flaky under load. **Licensing:** ⚠️ no explicit open-data licence; standard practice is attribution to the PBoC. Assume a government-copyright regime and cite the source.

---

### 1.2 National Bureau of Statistics (NBS) — 国家统计局

Authoritative for CPI, core CPI, PPI, GDP (real and nominal), and all activity data.

**Root:** https://www.stats.gov.cn/ · Database: https://data.stats.gov.cn/

#### 1.2.1 The `easyquery.htm` endpoint — the one real Chinese macro API

This is the JSON backend behind the National Data (国家数据) portal. It is undocumented but stable and widely used.

- **Base URL:** `https://data.stats.gov.cn/easyquery.htm` (Chinese) · `http://data.stats.gov.cn/english/easyquery.htm` (English) ✅

**Query parameters** (✅ read verbatim from the `khaeru/data` reference implementation, `cn_nbs.py`):

| Param | Meaning | Values |
|---|---|---|
| `m` | method | `QueryData` for observations; `getTree` for the indicator tree |
| `dbcode` | database | `hgyd` national monthly · `hgjd` national quarterly · `hgnd` national annual · `fsyd` provincial monthly · `fsjd` provincial quarterly · `fsnd` provincial annual |
| `rowcode` | dimension on rows | `zb` (indicator) for national queries · `reg` (region) for provincial |
| `colcode` | dimension on columns | `sj` (time) — effectively always |
| `wds` | fixed/locked dimensions, **JSON array** | `[]` for national; `[{"wdcode":"reg","valuecode":"110000"}]` to lock a province |
| `dfwds` | the selection filter, **JSON array** | `[{"wdcode":"zb","valuecode":"A01010101"},{"wdcode":"sj","valuecode":"LAST36"}]` |
| `k1` | cache-buster | epoch milliseconds |

- **Time selectors** accept `LAST<N>` (e.g. `LAST10`, `LAST36`) as well as explicit periods. ✅
- **Response shape** ✅: a JSON object containing
  - `wdnodes` — dimension metadata, one node per `wdcode` (`zb`, `sj`, `reg`), each listing its member `nodes` with `code` and `cname`;
  - `datanodes` — the observations; each has a `wds` array mapping dimension codes to member codes, and a `data` object carrying `hasdata` (boolean) and `data` (the number). **Always check `hasdata` — missing periods come back as `hasdata:false` with `data:0`, and treating that as a zero is the classic way to corrupt a China series.**

**Operational notes:** ⚠️ NBS requires a session cookie and is sensitive to `User-Agent`; TLS negotiation against `data.stats.gov.cn` is historically awkward from some clients. `zb` indicator codes must be discovered via `m=getTree` — ⚠️ **do not guess them, and do not copy an indicator code out of a blog post without re-checking it against the tree**, because NBS renumbers.

#### 1.2.2 Human-readable pages and the release calendar

| Item | URL |
|---|---|
| 数据发布 (latest releases) | https://www.stats.gov.cn/sj/zxfb/ ✅ |
| 发布日程 (release calendar) | https://www.stats.gov.cn/sj/fbrc/ ✅ |
| 发布日程表 (annual schedule) | https://www.stats.gov.cn/xxgk/sjfb/fbrcb/ ✅ |
| CPI 和 PPI hub | https://www.stats.gov.cn/hd/lyzx/zxgk/cpippi/ ✅ |
| 数据解读 (interpretation) | https://www.stats.gov.cn/sj/sjjd/ ✅ |
| English statistical data | https://www.stats.gov.cn/english/Statisticaldata/ ✅ |

- **CPI / PPI release lag:** ✅ **the 9th of the following month** — verified: August 2026 CPI and PPI were released on 2026-09-09. NBS states the CPI/PPI/PMI release timings are held constant year to year. ✅
- **GDP release lag:** ⚠️ mid-month following quarter end (~17th); not verified this session.
- **History start:** CPI and PPI monthly series in `easyquery` go back to the 1990s; ⚠️ exact first period unverified.

**Authentication:** none. **Rate limits:** ⚠️ none published; NBS throttles aggressively in practice — serialise requests. **Licensing** ✅: NBS asserts copyright over all site content, and permits reprint/quotation of database contents "reasonably and in good will" for news and free information, **provided the source is clearly indicated as "Source: National Bureau of Statistics"**. Terms: https://www.stats.gov.cn/english/nbs/200701/t20070104_59236.html ✅ · National Data disclaimer: https://data.stats.gov.cn/english/login.htm?m=toDisclimer ✅ — note this points at a *login/disclaimer* page, so re-read it before commercial redistribution.

---

### 1.3 CFETS / China Foreign Exchange Trade System — 中国货币网 (chinamoney.com.cn)

The single most valuable source for money-market and curve data, and **it has real JSON and CSV endpoints**.

**Root:** https://www.chinamoney.com.cn/ · English: https://www.chinamoney.com.cn/english/ · mirror host `iftp.chinamoney.com.cn`

#### 1.3.1 Verified machine-readable endpoints

All of the following were read verbatim out of `akshare`'s source (🟡 code-verified, not live-tested this session). They are what a widely-used library calls in production.

| Endpoint | What it returns | akshare wrapper |
|---|---|---|
| `https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/FrrHis` | **Repo fixing rate history**: `date, FR001, FR007, FR014, FDR001, FDR007, FDR014` over a start/end date range | `ak.repo_rate_hist(start_date, end_date)` 🟡 |
| `https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/currency/frr-chrt.csv` | FR001/FR007/FR014 chart CSV (headerless) | `ak.repo_rate_query("回购定盘利率")` 🟡 |
| `https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/currency/fdr-chrt.csv` | FDR001/FDR007/FDR014 chart CSV (headerless) | `ak.repo_rate_query("银银间回购定盘利率")` 🟡 |
| `https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/ClsYldCurvHis` | **Closing yield-curve history.** Params: `symbol` (curve name, e.g. `国债`, `同业存单(AAA)`), `period` (`0.1`, `0.5`, `1` — years of maturity point), `start_date`, `end_date`. Returns `日期, 期限, 到期收益率, 即期收益率, 远期收益率` | `ak.bond_china_close_return(symbol, period, start_date, end_date)` 🟡 |
| `https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/ClsYldCurvCurvGO` | **Curve-name → code map.** Call this first to discover every available curve. | `ak.bond_china_close_return_map()` 🟡 |
| `https://www.chinamoney.com.cn/ags/ms/cm-u-bk-shibor/IfccHis` | Interest-rate swap curve history: `日期, 曲线名称, 时刻, 价格类型, 1M…10Y` | `ak.macro_china_swap_rate(start_date, end_date)` 🟡 |
| `https://www.chinamoney.com.cn/ags/ms/cm-u-bond-an/bnBondEmit` | Bond **issuance announcements**: `债券全称, 债券类型, 发行日期, 计息方式, 价格, 债券期限, 计划发行量, 债券评级` | `ak.macro_china_bond_public()` 🟡 |
| `http://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/rfx-sp-quot.json` | CNY FX **spot** quotes | `ak.fx_spot_quote()` 🟡 |
| `http://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/rfx-sw-quot.json` | CNY FX **swap** quotes | `ak.fx_swap_quote()` 🟡 |

**Critical operational detail** 🟡: these `ags/ms/...` endpoints require a **session cookie**. `akshare` bootstraps it by first issuing a plain `GET` to
`https://www.chinamoney.com.cn/chinese/bkcurvclosedyhis/?bondType=CYCC000&reference=1`
with browser-like headers, then reusing that `requests.Session`. A cold request with no cookie will not work. Replicate this handshake.

#### 1.3.2 Human-readable pages

| Page | URL |
|---|---|
| Fixing repo rate (EN) | https://iftp.chinamoney.com.cn/english/bmkfrr/ ✅ |
| 回购定盘利率 FR007/FDR007 (CN) | https://www.chinamoney.com.cn/chinese/bkfrr/ ✅ |
| **Pledged repo quotes — DR001 / DR007 / DR014** | https://www.chinamoney.com.cn/english/mdtqapprp/ ✅ |
| **CFETS RMB Index** | https://www.chinamoney.com.cn/english/bmkidxrud/ ✅ (mirror https://iftp.chinamoney.com.cn/english/bmkidxrud/) |
| CNY central parity rate | https://www.chinamoney.com.cn/english/bmkcpr/ ✅ |
| 人民币汇率中间价 (CN) | https://iftp.chinamoney.com.cn/chinese/bkccpr/ ✅ |
| SHIBOR page | https://www.chinamoney.com.cn/chinese/bkshibor/ ✅ |
| Closing yield curve history (the page behind `ClsYldCurvHis`) | https://www.chinamoney.com.cn/chinese/bkcurvclosedyhis/ ✅ |
| Bond info query | https://www.chinamoney.com.cn/chinese/scsjzqxx/ ✅ |
| Business & services (incl. paid iData / CMDS feeds) | https://www.chinamoney.com.cn/english/ausbas/ ✅ |

**CFETS RMB Index specifics** ✅: published on `bmkidxrud` as dated articles giving the **month-end** index value. Verified example article URLs: `…/20251103/3224255.html` (end-Oct 2025), `…/20251201/3241786.html` (end-Nov 2025), `…/20260506/3333002.html` (end-Apr 2026) — i.e. posted within the first few business days of the following month. CFETS also publishes BIS-basket and SDR-basket RMB indices alongside it. ✅ ⚠️ CFETS historically also published a *weekly* index value; whether the weekly cadence still runs was not verified — the monthly article cadence is what is confirmed.

**DR007 vs FDR007 — do not confuse these.** ✅ DR007 is the **weighted average** of all depository-institution 7-day pledged repo trades struck between 09:00 and 11:30 against rate-bond collateral. FDR007 is the **fixing** (定盘) — a single published reference rate. They track each other closely but they are different numbers with different conventions. The `dr007` series in `series.json` is documented as a *monthly average of daily DR007 fixings*; if you repopulate it from `FrrHis` you will be getting **FDR007**, which is a methodology change. Label it.

**Authentication:** none for the public endpoints (session cookie ≠ auth). The genuinely comprehensive feeds (**CFETS Market Data Service / CMDS / iFTP / iData**) are commercial, contract-only, interbank-participant products. ✅ **Rate limits:** ⚠️ none published; these are internal page-backing endpoints, so be conservative. **Licensing:** ⚠️ no open licence. CFETS asserts rights over its market data and the commercial feeds are explicitly licensed. **Scraping the public pages for internal research is normal practice; redistributing the values is a licensing question you should take to counsel.**

---

### 1.4 ChinaBond / CCDC — 中央国债登记结算 (yield.chinabond.com.cn)

**The authoritative source for the China Government Bond yield curve**, which is what `cgb_1y`, `cgb_10y` and `term_spread` need.

| Item | URL | Mark |
|---|---|---|
| **Curve history query (the machine route)** | `https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/historyQuery?startDate=2019-02-07&endDate=2020-02-04&gjqx=0&qxId=ycqx&locale=cn_ZH` | 🟡 |
| akshare wrapper | `ak.bond_china_yield(start_date="YYYYMMDD", end_date="YYYYMMDD")` | 🟡 |
| Yield curve main page | https://yield.chinabond.com.cn/cbweb-mn/yield_main?locale=en_US | ✅ |
| More curves | https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/more?locale=en_US | ✅ |
| Historical data page | https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/showHistory?locale=en_US | ✅ |
| MOF–ChinaBond CGB yield curve | https://yield.chinabond.com.cn/cbweb-czb-web/czb/moreInfo?locale=en_US&nameType=1 | ✅ |
| ChinaBond indices (multi-index query) | https://yield.chinabond.com.cn/cbweb-mn/indices/multi_index_query?locale=en_US | ✅ |
| ChinaBond single index query | `https://yield.chinabond.com.cn/cbweb-mn/indices/singleIndexQueryResult` · `…/single_index_query` | 🟡 |

**Hard constraint** 🟡: `akshare`'s docstring states explicitly that **`end_date − start_date` must be less than one year** for `historyQuery`. To build a 2015→today history you must **loop in ≤12-month windows** and concatenate. Budget ~12 requests for a decade.

- `gjqx=0` and `qxId=ycqx` ⚠️: these select the curve and maturity set. `ycqx` is the 国债收益率曲线 (CGB yield curve) and `gjqx=0` appears to mean "all standard maturities", but **this reading is unverified** — confirm against the page's own form controls before relying on it.
- **Frequency:** daily (business days). **Release lag:** same-day, published after close (⚠️ exact time unverified). **History:** ⚠️ the CGB curve is widely cited as running from 2002 for key tenors and the 10Y from March 2006; not verified this session.

**Alternative for the same numbers:** CFETS `ClsYldCurvHis` with `symbol="国债"` (§1.3.1) returns the closing CGB curve including 到期收益率 at a chosen maturity `period`. Having two independent routes to the CGB curve is useful for cross-validation — and cross-validation is exactly what `series.json` was unable to do.

**Authentication:** none. **Rate limits:** ⚠️ unpublished; the 1-year window cap is the effective throttle. **Licensing:** ⚠️ CCDC asserts rights over ChinaBond curves and indices; the ChinaBond indices in particular are licensed products. Internal use is normal; redistribution is not clearly permitted.

---

### 1.5 SHIBOR / National Interbank Funding Centre (NIFC) — 全国银行间同业拆借中心

**Root:** https://www.shibor.org/ ✅ · 报价页 https://www.shibor.org/chinese/llshibor/ ✅

- **What:** 8 tenors — O/N, 1W, 2W, 1M, 3M, 6M, 9M, 1Y. Feeds `shibor_3m`.
- **Mechanics** ✅: NIFC is authorised to calculate and publish SHIBOR; quotes are collected from an 18-bank panel and the fixing is **published at 11:00 each business day**.
- **History:** ✅ data available from 2006 (SHIBOR's launch) through various platforms.
- **Machine-readable endpoint:** ⚠️ the site offers data download pages, but no documented public API was confirmed this session. **Use one of these instead:**
  - `ak.rate_interbank(market="上海银行同业拆借市场", symbol="Shibor人民币", indicator="3月")` 🟡 — see §1.11;
  - `tushare.pro` `shibor` interface — see §1.12.
- Related: panel banks https://www.shibor.net.cn/shibor/panelbanks/ ✅ · code of conduct https://www.shibor.sh.cn/shibor/codeofconduct/ ✅

**Licensing:** ⚠️ no open licence; SHIBOR is a published benchmark, redistribution of the full history is typically licensed.

---

### 1.6 Ministry of Finance (MOF) — 财政部

Needed for `govt_bond_issuance` and as context for `fiscal_deposits`.

| Item | URL |
|---|---|
| 政府债券管理 (hub) | https://gks.mof.gov.cn/ztztz/guozaiguanli/ ✅ |
| 记账式国债(含特别国债)发行 | https://gks.mof.gov.cn/ztztz/guozaiguanli/gzfxzjs/ ✅ |
| 储蓄国债发行 | https://gks.mof.gov.cn/ztztz/guozaiguanli/gzfxdzs/ ✅ |
| 国债管理工作动态 | https://gks.mof.gov.cn/ztztz/guozaiguanli/gzfxgzdt/ ✅ |
| 债务管理司 (**monthly local-government bond issuance & debt balance reports**) | https://zwgls.mof.gov.cn/ ✅ |
| 信息公开 | https://www.mof.gov.cn/gkml/ ✅ |

- **Frequency:** issuance announcements are per-auction (several per week); the 债务管理司 local-government-debt report is **monthly**. ✅
- **Release lag:** ⚠️ the monthly local-debt report runs roughly a month behind (2026 reports for Jan–Mar were available as of this search); not precisely verified.
- **Machine-readable endpoint:** ⚠️ none — HTML announcements only. The practical alternative for *forward* issuance is CFETS `bnBondEmit` (§1.3.1), which gives 发行日期 and 计划发行量 per bond and can be aggregated.

---

### 1.7 FRED (Federal Reserve Bank of St. Louis)

**Read this section before you rely on FRED for China.** FRED is excellent infrastructure wrapped around **mostly stale China data**. Several of the obvious series are discontinued.

#### 1.7.1 Verified China series IDs

| Series ID | Title | Source | Coverage | Verdict |
|---|---|---|---|---|
| `MYAGM2CNM189N` | M2 for China | IMF | ✅ Dec 1998 – **Aug 2019** | ❌ **DISCONTINUED.** Useless for a live tracker. |
| `MYAGM1CNM189N` | M1 for China | ⚠️ IMF (assumed) | ⚠️ not verified | ⚠️ Series exists ✅; assume the same 2019 truncation until you check. |
| `CHNCPIALLMINMEI` | Consumer Price Index: Total for China (COICOP 1999) | OECD | ✅ Jan 1993 – **Apr 2025** | ⚠️ Apparently ended Apr 2025 — verify before use. Index level, **not** YoY. |
| `CHNPIEATI01GYM` | Producer Prices Index: Economic Activities: Industrial Activities: Total for China, **growth rate same period previous year**, monthly, NSA | OECD | ✅ Jan 1999 – **Dec 2022** | ❌ **DISCONTINUED.** |
| `CHNPIEATI01GYQ` | Same, quarterly | OECD | ⚠️ | ❌ Same family. |
| `INTDSRCNM193N` | Interest Rates, Discount Rate for China | IMF | ✅ Mar 1990 – **Jun 2025** | ⚠️ Near-current but this is the *rediscount* rate, **not** the 7-day OMO policy rate. Do not map it to `omo_7d`. |
| `DEXCHUS` | Chinese Yuan Renminbi to U.S. Dollar Spot Exchange Rate | Board of Governors | ✅ 1981-01-02 – **2026-09-04**, daily, NSA | ✅ **The one genuinely good FRED China series.** Use it for `usd_cny`. |
| `CCRETT01CNQ661N` | Real Effective Exchange Rates: CPI Based for China | ⚠️ OECD (assumed) | ⚠️ quarterly | ⚠️ Quarterly only — BIS (§1.8) is the better REER source. |

⚠️ **No FRED series ID for China M0 was found or verified.** Do not guess one.

**The general lesson:** FRED's China coverage is largely a *mirror of IMF IFS and OECD MEI*, both of which stopped receiving several Chinese series. **For China money, credit and prices, FRED is a cross-check, not a primary source.** ✅ `DEXCHUS` is the exception.

Find more: https://fred.stlouisfed.org/tags/series?t=china%3Bcpi · https://fred.stlouisfed.org/tags/series?t=china%3Bppi ✅

#### 1.7.2 Access route A — the no-key CSV endpoint

```
https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES_ID>
```
Multiple series in one file: `?id=DEXCHUS,INTDSRCNM193N`. Optional `&cosd=YYYY-MM-DD` (start) and `&coed=YYYY-MM-DD` (end).

⚠️ **UNVERIFIED IN THIS SESSION.** `fred.stlouisfed.org` was blocked by the egress proxy, so the request could not be issued and the search tool did not return an official page documenting this exact URL form. It is a long-standing, widely-used pattern and FRED's own help pages document CSV download from a graph ✅, but **treat the precise parameter names as unconfirmed and test once before wiring it in.** Also note: a CSV pulled this way carries no metadata, no vintage and no revision history.

Related, also unverified: `https://fred.stlouisfed.org/data/<SERIES_ID>.txt` returns a plain-text table with a header block (search surfaced `https://fred.stlouisfed.org/data/CHNPIEATI01GYM.txt` ✅ as a real URL, so this route very likely works).

#### 1.7.3 Access route B — the keyed JSON API (preferred for production)

```
https://api.stlouisfed.org/fred/series/observations
    ?series_id=DEXCHUS
    &api_key=<32-char key>
    &file_type=json
    &observation_start=2015-01-01
```
Other endpoints: `/fred/series`, `/fred/series/search`, `/fred/category/series`, `/fred/release/dates`.

- **Authentication** ✅: a free 32-character API key, obtained by registering. No paid tier.
- **Rate limit** ✅: **120 requests per minute per key**; no monthly quota beyond that.
- **Docs:** https://fred.stlouisfed.org/docs/api/fred/ ✅
- **Vintages:** ALFRED (https://alfred.stlouisfed.org/series?seid=MYAGM2CNM189N ✅) serves point-in-time vintages — the only easy way to get *as-first-published* China data, which matters because NBS revises GDP.

**Licensing** ✅: use is governed by the FRED API Terms of Use (https://fred.stlouisfed.org/docs/api/terms_of_use.html) and the Bank's Legal Notices (https://fred.stlouisfed.org/legal). Crucially, **the terms apply to redistribution, and individual series inherit their original source's copyright** — a China series sourced from the IMF or OECD carries IMF/OECD terms, not a public-domain licence. Check the source note on each series before republishing values.

---

### 1.8 BIS Data Portal — REER and the credit-to-GDP gap

The right source for `reer` and for the credit-to-GDP gap that contextualises the credit impulse.

- **Portal:** https://data.bis.org/ ✅
- **SDMX REST API docs:** https://stats.bis.org/api-doc/v1/ ✅
- **Spec:** SDMX REST **v1.4.0**; formats **JSON, XML and CSV**; ✅ **no authentication required.**

**URL pattern** ✅:
```
https://stats.bis.org/api/v1/data/{DATASET}/{KEY}/all?startPeriod=YYYY&endPeriod=YYYY&detail=full
```

**Verified working example** ✅:
```
https://stats.bis.org/api/v1/data/WS_EER_M/M.N.B.CH/all?startPeriod=2000&endPeriod=2000&detail=full
```

- `WS_EER_M` = **Effective exchange rates, monthly**. ✅
- The key `M.N.B.CH` decomposes as `FREQ.EER_TYPE.BASKET.REF_AREA` = Monthly · Nominal · Broad · China. ⚠️ **This decomposition is my reading, not a verified statement.** The conventional way to request the **real** broad EER is to swap `N` → `R` (i.e. `M.R.B.CH`) — ⚠️ **unverified, test it.** Pull the dataset's DSD first (`https://stats.bis.org/api/v1/datastructure/BIS/BIS_EER` ⚠️ unverified path) rather than assuming.
- `WS_CREDIT_GAP` = **credit-to-GDP gap** dataset ✅ — provides the credit-to-GDP ratio, its long-run HP-filter trend, and the gap, quarterly, per country. ⚠️ The exact key layout was not verified.

**Frequency / lag / history:** ⚠️ BIS EER is monthly with roughly a 3–5 week lag and history from the 1960s–90s depending on country; credit gap is quarterly with a longer lag. Not verified this session.

**Licensing** ✅ — the most permissive of any source here. Per https://www.bis.org/terms_statistics.htm and https://data.bis.org/help/legal: **use is unrestricted provided that** (1) the BIS is cited as the source when statistics are reproduced, (2) any translation carries a statement that it is not an official BIS translation, and (3) the use is not misleading, e.g. by implying BIS endorsement or affiliation. **This means BIS data is safe to redistribute inside a published tracker with attribution** — a materially better position than PBoC/CFETS/ChinaBond.

---

### 1.9 IMF

- **New API base:** `https://api.imf.org/external/sdmx/3.0` ✅
- **Legacy SDMX 2.0 service:** `http://dataservices.imf.org/REST/SDMX_XML.svc/` ✅
- **Method pattern** ✅: three calls in sequence —
  1. `…/Dataflow` → list datasets, find the `KeyFamilyID` (for International Financial Statistics it is `IFS` ✅);
  2. `…/DataStructure/IFS` → the dimension order for that dataset;
  3. `…/CompactData/{DB}/{dim1 items}.{dim2 items}…?startPeriod=&endPeriod=` ✅ — e.g. for IFS the key is conventionally `{freq}.{country}.{indicator}`.
- **Format:** SDMX-JSON / SDMX-XML. ✅
- **Hard cap** ✅: **a response may not exceed 3,000 series** — split larger requests.
- **Authentication:** ⚠️ historically none for the legacy service; the 3.0 service's auth requirements were not verified.
- **Data help:** https://datahelp.imf.org/knowledgebase/articles/2005918-api-response ✅

⚠️ **Warning:** the IMF has been migrating from the legacy `dataservices.imf.org` service to `api.imf.org`, and the legacy endpoint has been intermittently deprecated. **Verify which base URL is live before building.** Also, IMF IFS is the upstream of FRED's stale China monetary series — so it inherits the same staleness. **Use the IMF for cross-checks and for FX reserves, not as your China money supply source.**

**Licensing:** ⚠️ IMF data terms require attribution and restrict commercial redistribution; not verified in detail this session.

---

### 1.10 World Bank

- **Indicators API v2:** `https://api.worldbank.org/v2/country/CHN/indicator/{INDICATOR_CODE}?format=json&per_page=1000` ✅
- **Authentication** ✅: **none — API keys are explicitly not required.**
- **Docs:** https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation ✅ · call structures https://datahelpdesk.worldbank.org/knowledgebase/articles/898581-api-basic-call-structures ✅
- **Newer portal API:** https://data360.worldbank.org/en/api ✅
- **Pagination** ✅: `per_page` (the docs' own example is `?per_page=25`); the response is a 2-element JSON array — `[metadata, [observations]]` — and **forgetting the metadata element is the classic parsing bug.** ⚠️
- **Coverage:** ⚠️ **annual only** for almost everything. That makes it useless for every series in this tracker except long-run context. ⚠️ Indicator codes (e.g. `FP.CPI.TOTL.ZG` for inflation, `NY.GDP.MKTP.CD` for nominal GDP) were **not verified this session** — look them up rather than trusting these from memory.
- **Licensing** ✅: most World Bank indicator data is **CC-BY 4.0** under the Open Data terms — https://datacatalog.worldbank.org/public-licenses ✅. The most redistribution-friendly source here alongside BIS.

**Verdict:** use the World Bank for decade-scale context and nothing else.

---

### 1.11 akshare (Python)

Open-source (MIT), no key, no registration. **In practice this is the single fastest way for someone with normal internet access to populate most of this tracker**, because it wraps the Chinese endpoints and does the cookie handshakes for you.

```
pip install akshare --upgrade
```
Repo: https://github.com/akfamily/akshare ✅ · docs https://akshare.akfamily.xyz/ ⚠️

#### 1.11.1 Functions verified against akshare source this session

| Function | Upstream it calls | Serves |
|---|---|---|
| `ak.macro_china_money_supply()` | `https://data.eastmoney.com/cjsj/hbgyl.html` ✅ | **M0, M1, M2 levels and YoY** → `m1_yoy`, `m2_yoy`, `m2_level` |
| `ak.macro_china_shrzgm()` | `https://data.mofcom.gov.cn/gnmy/shrzgm.shtml` ✅ | **TSF monthly increment** → `tsf_flow`. ⚠️ **This is MOFCOM's republication of the PBoC headline and it runs 2–3 months behind** — it is exactly why `tsf_flow` in `series.json` stops at 2026-04 while the monthly series reach 2026-06. |
| `ak.rate_interbank(market, symbol, indicator)` | `https://datacenter-web.eastmoney.com/api/data/v1/get` ✅ | **SHIBOR, CHIBOR, HIBOR, LIBOR, EURIBOR, SIBOR** → `shibor_3m`, `cnh_hibor_on` |
| `ak.repo_rate_hist(start_date, end_date)` | chinamoney `FrrHis` ✅ | FR001/007/014 + **FDR001/FDR007/FDR014** → proxy for `dr007`, `r007` |
| `ak.repo_rate_query(symbol)` | chinamoney `frr-chrt.csv` / `fdr-chrt.csv` ✅ | Same, chart-window CSV |
| `ak.bond_china_yield(start_date, end_date)` | ChinaBond `historyQuery` ✅ | **Full CGB curve** → `cgb_1y`, `cgb_10y`, `term_spread`. ⚠️ ≤1-year windows. |
| `ak.bond_china_close_return(symbol, period, start_date, end_date)` | chinamoney `ClsYldCurvHis` ✅ | **`symbol="同业存单(AAA)"` → `ncd_1y_aaa`**; `symbol="国债"` → CGB curve |
| `ak.bond_china_close_return_map()` | chinamoney `ClsYldCurvCurvGO` ✅ | Enumerate available curve names — **call this first** |
| `ak.macro_china_swap_rate(start_date, end_date)` | chinamoney `IfccHis` ✅ | FR007 IRS curve (1M–10Y) |
| `ak.macro_china_bond_public()` | chinamoney `bnBondEmit` ✅ | Forward bond issuance → `govt_bond_issuance` |
| `ak.fx_spot_quote()` / `ak.fx_swap_quote()` | chinamoney `rfx-sp-quot.json` / `rfx-sw-quot.json` ✅ | CNY spot / swap → `usdcny` |

`rate_interbank` parameter domains ✅ (read verbatim from `akshare/interest_rate/interbank_rate_em.py`):
- `market`: `上海银行同业拆借市场`, `中国银行同业拆借市场`, `伦敦银行同业拆借市场`, `欧洲银行同业拆借市场`, `香港银行同业拆借市场`, `新加坡银行同业拆借市场`
- `symbol`: `Shibor人民币`, `Chibor人民币`, `Libor英镑`, `Libor欧元`, `Libor美元`, `Libor日元`, `Euribor欧元`, `Hibor美元`, `Hibor人民币`, `Hibor港币`, `Sibor星元`, `Sibor美元`
- `indicator`: `隔夜`, `1周`, `2周`, `3周`, `1月`, `2月`, `3月`, `4月`, `5月`, `6月`, `7月`, `8月`, `9月`, `10月`, `11月`, `1年`

#### 1.11.2 Other `macro_china_*` functions relevant to this tracker

The following names appear in `akshare/__init__.py` ✅ (the names are real exports). ⚠️ **Their upstreams and signatures were not individually verified** — check each docstring.

- **Money & credit:** `macro_china_money_supply`, `macro_china_supply_of_money`, `macro_china_m2_yearly`, `macro_china_new_financial_credit`, `macro_china_shrzgm`, `macro_china_bank_financing`, `macro_china_central_bank_balance`
- **Policy:** `macro_china_lpr`, `macro_china_reserve_requirement_ratio` → `lpr_1y`, `lpr_5y`, `rrr_large`, `rrr_small`
- **Prices:** `macro_china_cpi_monthly`, `macro_china_cpi_yearly`, `macro_china_ppi_yearly`
- **Activity:** `macro_china_gdp`, `macro_china_gdp_yearly`, `macro_china_urban_unemployment`, `macro_china_consumer_goods_retail`, `macro_china_gyzjz`
- **External:** `macro_china_fx_reserves_yearly`, `macro_china_foreign_exchange_gold`, `macro_china_rmb`, `macro_china_hgjck`
- **Rates / markets:** `macro_china_shibor_all`, `macro_china_swap_rate`, `macro_china_bond_public`
- **NBS passthrough:** `macro_china_nbs_nation`

⚠️ **Caution on the `*_yearly` / `*_monthly` family:** many of these (`macro_china_gdp_yearly`, `macro_china_cpi_yearly`, `macro_china_cpi_monthly`, `macro_china_ppi_yearly`) are documented in akshare's own tutorial as coming from **金十数据 (jin10.com)**, a *news/event* feed ✅ — they return event-style records (actual / forecast / previous) rather than a clean revised statistical series. **For a tracker, prefer `macro_china_money_supply` / NBS / PBoC over the jin10-backed functions.**

**Licensing / risk:** akshare is MIT-licensed, but **it is a scraper**. The data it returns carries the upstream publisher's terms, not akshare's. Interfaces break regularly — akshare's changelog is a continuous stream of "fix: fix X interface" entries ✅ (`macro_china_shrzgm` and `rate_interbank` both appear repeatedly). **Pin the version, monitor for schema drift, and never let an akshare call silently return an empty frame into your pipeline.**

---

### 1.12 tushare (Python)

Registration-gated, points-based. https://tushare.pro/ ✅ · docs https://tushare.pro/document/2 ⚠️

```python
import tushare as ts
pro = ts.pro_api('<token>')
df = pro.shibor(start_date='20150101', end_date='20260913')
```

| Interface | Serves | Access |
|---|---|---|
| `shibor` | SHIBOR all tenors | ✅ **120 points**; ✅ max **2,000 rows per call**, unlimited total |
| `shibor_lpr` | LPR (贷款基础利率) | ✅ **120 points**; ✅ max **4,000 rows per call**, unlimited total |
| `shibor_quote` | Panel-bank SHIBOR quotes | ⚠️ points unverified |
| `cn_m` | M0 / M1 / M2 | ⚠️ "2,000 or 5,000+ points" per the docs summary — unverified |
| `cn_cpi`, `cn_ppi` | CPI, PPI | ⚠️ same |
| `cn_gdp` | GDP | ⚠️ same |
| `cn_pmi` | PMI | ⚠️ same |

- **Authentication** ✅: free registration yields a token; **120 points is effectively free** (registering and setting a nickname grants it ✅), which is enough for `shibor` and `shibor_lpr`. The `cn_*` macro interfaces sit behind materially higher point thresholds, which in practice means a paid/contributed account.
- **Rate limits:** ⚠️ per-minute call caps apply per interface and scale with points; not verified.
- **Licensing:** ⚠️ tushare's terms restrict redistribution. It is a convenience layer over the same public sources.

**Verdict:** tushare is the **best free route to a clean, long SHIBOR and LPR history**. For everything else akshare is less encumbered.

---

### 1.13 Scraping routes — East Money, Sina, Investing.com

These are **not authoritative**, and every value currently in `series.json` traces back to one of them. Use them for gap-filling and cross-checks, never as your system of record.

| Route | Endpoint / page | Notes |
|---|---|---|
| **East Money datacenter (JSON)** | `https://datacenter-web.eastmoney.com/api/data/v1/get` ✅ with params `reportName`, `columns`, `filter`, `pageNumber`, `pageSize`, `sortColumns`, `sortTypes`, `source`, `client` ✅ | The backbone of akshare's China macro coverage. ⚠️ **`reportName` values are undocumented and change**; discover them from browser devtools or from akshare's source. |
| East Money legacy | `https://datacenter.eastmoney.com/api/data/get` ✅ | Older variant, still live. |
| East Money human pages | `https://data.eastmoney.com/cjsj/hbgyl.html` (money supply) ✅ ; `https://data.eastmoney.com/cjsj/` (macro hub) ⚠️ | |
| **Sina Finance** | `https://hq.sinajs.cn/list=...` ⚠️ ; `https://money.finance.sina.com.cn/...` ⚠️ | ⚠️ Endpoints unverified this session. Sina now enforces a `Referer: https://finance.sina.com.cn` header on `hq.sinajs.cn` ⚠️ — a bare request 403s. |
| **Investing.com** | https://www.investing.com/rates-bonds/shibor-1-year-historical-data ✅ | Convenient history pages for SHIBOR, CGB yields, USDCNY. |

**Fragility.** ⚠️ All three are undocumented internal APIs backing a webpage. They change without notice, they have no versioning, they have no SLA, and they return HTTP 200 with an empty or error payload rather than a proper status code — so **a naive pipeline will silently write nulls**. Assert on row counts and date coverage after every pull.

**Terms-of-service risk.** ⚠️ **Investing.com's terms prohibit automated scraping and systematic data extraction**, and it actively rate-limits and blocks. East Money and Sina likewise assert rights over their site content. Redistributing values scraped from any of these — in a public dashboard, a paper, or a commercial product — is a genuine legal exposure, entirely separate from the question of whether the numbers are right. **Where a primary publisher offers the same number, use the primary publisher. It is both safer and more accurate.**

---

## 2. Indicator → source matrix

Primary = what you should use. Fallback = cross-check or gap-filler. Codes in the first column are the registry keys in `data/registry_*.json`.

### 2.1 Monetary block

| Key | Indicator | Freq | Primary source | Machine route | Lag | History |
|---|---|---|---|---|---|---|
| `m1_yoy` | M1 growth | M | PBoC 金融统计数据报告 / 货币统计概览 | `ak.macro_china_money_supply()` 🟡 | ~12th | 1990s ⚠️ |
| `m2_yoy`, `m2_level` | M2 growth & level | M | PBoC, same release | `ak.macro_china_money_supply()` 🟡 · FRED `MYAGM2CNM189N` ❌ dead after Aug 2019 | ~12th | 1990s ⚠️ |
| `m1_m2_gap` | Scissors gap | M | **derived** = `m1_yoy − m2_yoy` | — | — | — |
| `tsf_stock_yoy` | TSF stock YoY | M | PBoC 社会融资规模存量统计数据报告 | HTML/PDF parse ✅ | ~12th | 2002 ⚠️ |
| `tsf_flow` | TSF monthly increment | M | PBoC 社会融资规模增量 | `ak.macro_china_shrzgm()` 🟡 (**MOFCOM mirror, 2–3m lag**) | ~12th primary / 2–3m via MOFCOM ✅ | 2002 ⚠️ |
| `new_loans` | New RMB loans | M | PBoC, same release | `ak.macro_china_money_supply()` family 🟡 | ~12th | 1990s ⚠️ |
| `credit_impulse` | Credit impulse | M | **derived** from `tsf_flow` + nominal GDP | — | — | — |
| `omo_7d` | 7-day reverse repo policy rate | D | **PBoC 公开市场业务交易公告** ✅ | HTML parse; no API | same day | 2012 ⚠️ |
| `mlf_1y` | 1-year MLF rate | M | PBoC OMO announcements | HTML parse | same day | Sep 2014 ⚠️ — **⚠️ no published rate since the Mar 2025 multi-price switch** |
| `lpr_1y`, `lpr_5y` | Loan Prime Rate | M (20th) | PBoC / NIFC LPR fixing | `tushare.shibor_lpr` ✅ · `ak.macro_china_lpr()` ⚠️ | same day, ~09:15 ⚠️ | 1y from Oct 2013; 5y from Aug 2019 ✅ |
| `walr_general` | Weighted avg lending rate, general loans | Q | **PBoC MPR PDF — sole source** ✅ | PDF parse only | ~6 weeks ✅ | 2008 ⚠️ |
| `real_policy_rate`, `real_lending_rate` | Real rates | — | **derived** (nominal − deflator) | — | — | — |
| `rrr_large`, `rrr_small` | Reserve requirement ratios | STEP | PBoC announcements | `ak.macro_china_reserve_requirement_ratio()` ⚠️ | same day | 1985 ⚠️ |
| `usdcny` | USD/CNY | D | CFETS central parity ✅ / **FRED `DEXCHUS`** ✅ | `fredgraph.csv?id=DEXCHUS` ⚠️ or keyed API ✅ | T+1 | ✅ 1981-01-02 |
| `cfets` | CFETS RMB index | M (month-end) | **CFETS `bmkidxrud`** ✅ | HTML parse | first days of following month ✅ | Dec 2015 ⚠️ |
| `reer` | Real effective exchange rate | M | **BIS `WS_EER_M`** ✅ | SDMX REST ✅ | 3–5 weeks ⚠️ | 1960s–90s ⚠️ |

### 2.2 Liquidity block

| Key | Indicator | Freq | Primary source | Machine route | Lag | History |
|---|---|---|---|---|---|---|
| `dr007` | DR007 | D | **CFETS pledged repo** ✅ | `ak.repo_rate_hist()` → **FDR007** 🟡 (≠ DR007, see §1.3.2) | same day | 15 Dec 2014 ✅ |
| `dr007_omo_spread` | DR007 − 7d OMO | D | **derived** | — | — | — |
| `r007` | R007 | D | CFETS pledged repo ✅ | `ak.repo_rate_hist()` → **FR007** 🟡 | same day | ⚠️ |
| `r_dr_spread` | R007 − DR007 | D | **derived** | — | — | — |
| `ncd_1y_aaa` | 1Y AAA NCD rate | D | **CFETS `ClsYldCurvHis`, `symbol="同业存单(AAA)"`, `period="1"`** 🟡 | JSON ✅ | same day | ⚠️ |
| `ncd_mlf_spread` | 1Y NCD − 1Y MLF | D | **derived** — ⚠️ **denominator dead since Mar 2025** | — | — | — |
| `excess_reserve_ratio` | Excess reserve ratio | Q | **PBoC MPR PDF — sole source** ✅ | PDF parse only | ~6 weeks ✅ | 2001 ⚠️ |
| `net_injection_3m` | PBoC net injection, 3m sum | M | **derived** from PBoC OMO announcements ✅ | HTML parse + aggregate | same day | 2012 ⚠️ |
| `outright_repo` | Outright reverse repo | M | PBoC OMO announcements ✅ | HTML parse | monthly summary ⚠️ | ✅ Oct 2024 (new tool) |
| `fiscal_deposits` | Govt deposits at PBoC, change | M | **PBoC 货币当局资产负债表**, 政府存款 line ✅ | PDF/HTML parse | ~6 weeks ⚠️ | 1999 ⚠️ |
| `govt_bond_issuance` | Government bond issuance | M | MOF 国库司 + 债务管理司 ✅ | HTML parse; or CFETS `bnBondEmit` 🟡 | per-auction / monthly ✅ | ⚠️ |
| `cgb_10y`, `cgb_1y` | CGB yields | D | **ChinaBond `historyQuery`** 🟡 | JSON, ≤1yr windows 🟡 | same day, post-close | 10Y from Mar 2006 ⚠️ |
| `term_spread` | 10y − 1y CGB | D | **derived** | — | — | — |
| `credit_spread_aa` | AA credit spread | D | ChinaBond corporate curve ⚠️ / CFETS `ClsYldCurvHis` 🟡 | JSON | same day | ⚠️ |
| `cnh_hibor_on` | CNH HIBOR overnight | D | TMA (Hong Kong) ⚠️ | `ak.rate_interbank(market="香港银行同业拆借市场", symbol="Hibor人民币", indicator="隔夜")` ✅ | same day | Jun 2013 ⚠️ |
| `shibor_3m` | 3-month SHIBOR | D | **SHIBOR / NIFC, 11:00 fixing** ✅ | `tushare.shibor` ✅ · `ak.rate_interbank(..., indicator="3月")` ✅ | same day 11:00 ✅ | 2006 ✅ |

### 2.3 Context block

| Key | Indicator | Freq | Primary source | Machine route | Lag | History |
|---|---|---|---|---|---|---|
| `cpi_yoy` | CPI | M | **NBS** ✅ | `easyquery` `dbcode=hgyd` ✅ | **9th** ✅ | 1990s ⚠️ |
| `core_cpi_yoy` | Core CPI | M | **NBS** ✅ (monthly; the MPR only quotes it occasionally) | `easyquery` ✅ | 9th ✅ | ⚠️ |
| `ppi_yoy` | PPI | M | **NBS** ✅ | `easyquery` ✅ | **9th** ✅ | 1990s ⚠️ |
| `gdp_deflator_yoy` | GDP deflator | Q | **derived** = nominal GDP YoY − real GDP YoY, NBS for both | `easyquery` `dbcode=hgjd` ✅ | ~17th after quarter ⚠️ | ⚠️ |
| `real_gdp_yoy` | Real GDP | Q | **NBS** ✅ | `easyquery` `dbcode=hgjd` ✅ | ~17th ⚠️ | 1992 ⚠️ |
| `nominal_gdp_yoy` | Nominal GDP | Q | **NBS** ✅ (MPR quotes cumulative levels in 万亿元) | `easyquery` ✅ | ~17th ⚠️ | ⚠️ |
| `fx_reserves` | FX reserves | M | SAFE ✅ (https://www.safe.gov.cn/en/) / PBoC | `ak.macro_china_fx_reserves_yearly()` ⚠️ | ~7th ⚠️ | 1990s ⚠️ |

---

## 3. Release calendar

| Day of month | What lands | Source | Mark |
|---|---|---|---|
| ~7th | FX reserves | SAFE / PBoC | ⚠️ |
| **9th** | **CPI, PPI** | NBS | ✅ verified (Aug-2026 data released 2026-09-09) |
| **10th–15th (12th observed twice)** | **M0/M1/M2, new loans, TSF flow, TSF stock** | PBoC 金融统计数据报告 | ✅ verified (2025-12-12, 2026-06-12) |
| ~15th–17th | Industrial production, FAI, retail sales; **GDP in Jan/Apr/Jul/Oct** | NBS | ⚠️ |
| **20th** | **LPR fixing** | PBoC / NIFC | ⚠️ |
| Every business day 11:00 | SHIBOR fixing | NIFC | ✅ |
| Every business day, morning | OMO announcement | PBoC | ✅ |
| Every business day, post-close | CGB curve, closing yield curves, repo fixings | ChinaBond / CFETS | ⚠️ |
| First business days of month | CFETS RMB index (month-end value) | CFETS | ✅ |
| **~6 weeks after quarter end** (≈9–15 Feb / 9–15 May / ~11 Aug / ~11 Nov) | **Monetary Policy Report → `walr_general`, `excess_reserve_ratio`, quarterly TSF stock, core CPI commentary, nominal GDP** | PBoC | ✅ verified across 7 reports |

Official calendars: NBS https://www.stats.gov.cn/sj/fbrc/ ✅ · https://www.stats.gov.cn/xxgk/sjfb/fbrcb/ ✅. ⚠️ **The PBoC does not publish a binding advance calendar for the monthly financial statistics release** — it is announced same-day. Poll, don't schedule.

---

## 4. Recommended production pull strategy

This is the concrete, ranked plan for someone with **normal internet access** to populate the full dataset from scratch. Do it in this order; each phase is independently useful and the later phases are progressively more work per series.

### Phase 0 — Preparation (half a day)

1. **Open every URL in §8 by hand, once.** Confirm each page still exists and note where the table/anchor sits. Non-negotiable: several routes in this document are 🟡 and have never been live-tested.
2. `pip install akshare --upgrade` and register a free tushare account (nickname → 120 points). Register a free FRED API key.
3. Decide your **storage contract up front**: every observation gets `(series_id, period, value, source_name, source_url, retrieved_at, is_primary)`. The single worst property of the current `series.json` is that mirror-sourced values sit in the same shape as primary ones.
4. Build the **assertion harness before the pullers**: row count > 0, last period within expected lag, no NaN run longer than N, YoY within a sane band. Every scraping route in §1.13 returns HTTP 200 on failure, so silence is the failure mode you must design against.

### Phase 1 — The free, reliable, machine-readable core (1 day)

Pull these first because they need no scraping and no judgement.

| Order | Series | Route |
|---|---|---|
| 1 | `usdcny` | **FRED `DEXCHUS`** via keyed API. Longest, cleanest, best-licensed daily series in the whole tracker. |
| 2 | `reer` | **BIS SDMX** `WS_EER_M`. Redistributable with attribution. |
| 3 | Credit-to-GDP gap (context for `credit_impulse`) | **BIS SDMX** `WS_CREDIT_GAP`. |
| 4 | `shibor_3m`, `cnh_hibor_on` | **tushare `shibor`** (long clean history) + `ak.rate_interbank` for HIBOR. |
| 5 | `lpr_1y`, `lpr_5y` | **tushare `shibor_lpr`**. Then reconcile against the published LPR change history — `series.json` notes its LPR history already reproduces the published record exactly, so use the existing series as the regression fixture. |

### Phase 2 — The Chinese primary-source core via akshare (1–2 days)

Use akshare as the *transport* but record the **upstream publisher** as the source, and reconcile against the publisher's own page for at least three spot dates per series.

| Order | Series | Route |
|---|---|---|
| 6 | `m1_yoy`, `m2_yoy`, `m2_level`, `new_loans` | `ak.macro_china_money_supply()` → then **spot-check against the PBoC 金融统计数据报告** for 3 dates. |
| 7 | `cpi_yoy`, `core_cpi_yoy`, `ppi_yoy` | **NBS `easyquery` directly** (`dbcode=hgyd`), not akshare's jin10-backed wrappers. Discover `zb` codes with `m=getTree` — do not hardcode codes from a blog. |
| 8 | `real_gdp_yoy`, `nominal_gdp_yoy` | **NBS `easyquery`** (`dbcode=hgjd`). Pull nominal and real for the *same* periods — this is precisely what the seed build could not do. |
| 9 | `gdp_deflator_yoy` | **Derive** from 8. Do not source it; it does not exist as a published series. |
| 10 | `cgb_1y`, `cgb_10y`, `term_spread` | `ak.bond_china_yield()` looping in ≤12-month windows, 2015→today. Cross-check the 10Y against CFETS `ClsYldCurvHis` with `symbol="国债"`. |
| 11 | `ncd_1y_aaa` | `ak.bond_china_close_return(symbol="同业存单(AAA)", period="1", …)`. **Call `bond_china_close_return_map()` first** to confirm the exact curve label. |
| 12 | `dr007`, `r007`, `r_dr_spread` | `ak.repo_rate_hist()`. **Label them FDR007/FR007 unless you have true DR007**, and if you want true DR007 scrape CFETS `mdtqapprp`. |
| 13 | `rrr_large`, `rrr_small` | `ak.macro_china_reserve_requirement_ratio()`, then **reconcile every change date against PBoC announcements** — the seed's step history was truncated precisely because a mirror's change dates were incomplete. |
| 14 | `fx_reserves` | akshare or SAFE. |

### Phase 3 — The PDF-only quarterlies (1 day, then 4×/year forever)

| Order | Series | Route |
|---|---|---|
| 15 | `walr_general`, `excess_reserve_ratio` | **Parse the PBoC MPR PDFs.** There is no alternative source. Build the parser against the seven verified PDF URLs in §1.1.3 as fixtures. **Handle both the pre-2024Q4 prose layout and the post-2024Q4 table layout.** |
| 16 | Quarterly TSF stock level & YoY, nominal GDP levels, NCD issuance WAR | Same PDFs, same pass. |

Schedule the job for the **6th week after each quarter end**, and alert if the expected report has not appeared within 8 weeks.

### Phase 4 — The HTML-scrape tail (2–3 days)

| Order | Series | Route |
|---|---|---|
| 17 | `omo_7d` | **PBoC 公开市场业务交易公告**, full crawl of the announcement archive. Build a *step series of dated rate changes*, then forward-fill. Anything less produces exactly the failure documented in `meta.gaps`. |
| 18 | `net_injection_3m`, `outright_repo` | Same crawl, different fields (volume in, maturities out, by instrument). Remember the post-2024 toolkit: OMO + MLF + outright reverse repo + PSL + bond purchases. Netting only OMO+MLF is now badly wrong. |
| 19 | `fiscal_deposits` | **PBoC 货币当局资产负债表** monthly PDFs, 政府存款 line, first-differenced. |
| 20 | `govt_bond_issuance` | MOF 国库司 announcements + 债务管理司 monthly local-debt reports; or aggregate CFETS `bnBondEmit`. |
| 21 | `cfets` | CFETS `bmkidxrud` article list, parse the month-end value out of each post. |
| 22 | `mlf_1y` | PBoC announcements up to **Mar 2025**, then **stop** — see §5. |
| 23 | `credit_spread_aa` | ChinaBond / CFETS corporate curves. |

### Phase 5 — Validation before you trust any of it

- **Two-source rule:** every series that has two independent routes must agree on every overlapping point before you promote it. `series.json` applied this to M2, CPI, PPI, TSF-stock YoY and GDP and it caught nothing — which is the point: it earns the confidence.
- **Reconcile against the MPR's own prose.** The MPR states period-on-period deltas ("下降 X 个百分点"); check your levels reproduce them. This is the internal-consistency test the excess-reserve series already passes.
- **Respect the documented breaks.** The **January 2025 M1 redefinition** and the **2024 手工补息 crackdown** are genuine discontinuities. A refreshed M1 series is *not* comparable across them — carry the break flag into the new dataset.
- **Never forward-fill a step series across an unknown change.** The reason `omo_7d`, `mlf_1y`, `rrr_large` and `rrr_small` are omitted or truncated in the seed is that partial change histories produce confidently wrong levels. Keep that discipline.

### Budget summary

| Phase | Effort | Yields |
|---|---|---|
| 1 | 1 day | 5 series, fully licensed, zero scraping |
| 2 | 1–2 days | ~14 series, the analytic core |
| 3 | 1 day | 4 series obtainable no other way |
| 4 | 2–3 days | ~7 series, the fragile tail |
| **Total** | **~1 working week** | **the complete tracker** |

---

## 5. Known gaps and how to close them

This section walks `meta.gaps` in `data/seed/series.json` item by item. For each, the specific source and retrieval route that closes it.

### 5.1 `omo_7d` — 7-day reverse repo policy rate (OMITTED)

**Why it's missing.** Only four anchors were verifiable from MPR text (2.55% through 2019Q1–Q3; 1.50% at 2025-03; a cut 1.5%→1.4% in 2025Q4; 1.40% at 2026-03). Forward-filling four anchors across 2019–2026 would inject wrong levels through every intervening cut (2020, 2022, 2023, 2024), so nothing was emitted.

**How to close it.** Crawl **PBoC 公开市场业务交易公告**: https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/index.html ✅ — every daily announcement states the operation tenor, volume and winning rate. Paginate the archive back to 2015, extract `(date, tenor=7D, rate)`, keep only the rows where the rate *changes*, and emit a STEP series to be forward-filled. Cross-check the resulting change dates against the gov.cn English policy announcements and the rate table in `research/03-liquidity-indicators.md` §0.2 (which already records 1.40% effective 8 May 2025 ✅). **This is a pure HTML-crawl job with no API — budget half a day.**

**Secondary route:** `ak.macro_china_reserve_requirement_ratio()`-style East Money mirrors and TradingEconomics carry an OMO rate series ⚠️, but a mirror is exactly what produced the failure being fixed. Use it only to validate the crawl.

### 5.2 `mlf_1y` — 1-year MLF rate (OMITTED)

**Why it's missing.** MPR text describes MLF moves qualitatively ("down 20bp") without a dated level series.

**How to close it — and the honest answer about what "closed" means.** Crawl the same PBoC OMO announcement archive for MLF operations back to **September 2014**; each historical announcement carries the operation rate. **But you can only rebuild the series through March 2025.** ✅ From the 25 March 2025 operation the MLF moved to fixed-quantity, variable-rate, **multiple-price** tendering and **the PBoC stopped publishing a winning rate** — the rate does not exist to be scraped. So: emit `mlf_1y` as a complete step series 2014→2025-03 and then **terminate it deliberately**, with a note. Do not let it forward-fill past March 2025.

**Consequence for `ncd_mlf_spread`:** that composite's denominator is dead. Re-base it (e.g. NCD − 7d OMO) or retire it. See `research/03-liquidity-indicators.md` §B.3.

### 5.3 `r007` — all-market 7-day repo rate (no data at any frequency)

**How to close it.** Two routes, in preference order:

1. **CFETS `FrrHis`** — `https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/FrrHis` 🟡, via `ak.repo_rate_hist(start_date, end_date)`. Returns `FR001, FR007, FR014` alongside the FDR series in one call. **Caveat:** FR007 is the *fixing*, not the full-market weighted average R007. Label it accurately.
2. **True R007** (weighted average) from the CFETS pledged-repo page https://www.chinamoney.com.cn/english/mdtqapprp/ ✅ — HTML parse.

Remember the session-cookie handshake in §1.3.1.

### 5.4 `ncd_1y_aaa` — 1-year AAA NCD rate (not obtainable; only a quarterly proxy supplied)

**This is the cleanest win in this list.** The current `ncd_issuance_war` is explicitly a different, lower-level measure (all-tenor, all-issuer *issuance* WAR from the MPR) and is flagged as a directional proxy only.

**How to close it.** `ak.bond_china_close_return(symbol="同业存单(AAA)", period="1", start_date=..., end_date=...)` 🟡, which calls `https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/ClsYldCurvHis`. This is the **CFETS closing yield curve for the AAA NCD curve at the 1-year point** — exactly the series the registry asks for, at daily frequency. Call `ak.bond_china_close_return_map()` (→ `ClsYldCurvCurvGO`) first to confirm the exact curve label string, since the Chinese label must match. Keep `ncd_issuance_war` as a separate quarterly series; do not merge them.

### 5.5 `cgb_1y` — 1-year CGB yield (no data; only the 10Y point was reachable)

**How to close it.** `ak.bond_china_yield(start_date, end_date)` 🟡 → `https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/historyQuery?...&gjqx=0&qxId=ycqx&locale=cn_ZH`. This returns the **whole curve**, not a single tenor, so it closes `cgb_1y`, backfills `cgb_10y`, and gives you `term_spread` for free. **Loop in ≤12-month windows** (the ≤1-year constraint is explicit in akshare's docstring 🟡). Cross-validate against CFETS `ClsYldCurvHis` with `symbol="国债"`.

### 5.6 `cfets_rmb_index` — CFETS RMB index (no data)

**How to close it.** CFETS publishes it at https://www.chinamoney.com.cn/english/bmkidxrud/ ✅ as one dated article per month carrying the **month-end** value — verified article URLs `…/20251103/3224255.html`, `…/20251201/3241786.html`, `…/20260506/3333002.html` ✅. Crawl the article list, parse the value and the reference month. The same page also carries the BIS-basket and SDR-basket RMB indices, which are useful cross-checks. History runs from the index's December 2015 launch ⚠️.

**Fallback:** BIS `WS_EER_M` broad nominal EER for China ✅ is not the same index but is highly correlated and is properly licensed — use it if you need something redistributable.

### 5.7 `usd_cny` — monthly average (no series; one spot value only)

**How to close it — trivially.** **FRED `DEXCHUS`** ✅: daily CNY-per-USD from **1981-01-02 to 2026-09-04**, sourced from the Federal Reserve Board. Pull the full daily history via the keyed API (`https://api.stlouisfed.org/fred/series/observations?series_id=DEXCHUS&api_key=…&file_type=json`) ✅ and take monthly means yourself. This is the single easiest gap in the file to close and the result is better than any China-hosted route, because it is long, clean, revision-free and redistributable-with-attribution.

**Primary-source alternative** if you specifically need the CFETS central parity rather than the Fed's noon rate: https://www.chinamoney.com.cn/english/bmkcpr/ ✅ or `ak.fx_spot_quote()` 🟡.

### 5.8 `gdp_deflator_yoy` and `nominal_gdp_yoy` (not emitted)

**Why they're missing.** Deriving a deflator requires nominal *and* real growth for the **same periods**, and only 7 sparse nominal *level* points (from MPR prose, in 万亿元) were verified.

**How to close it.** Pull both legs from **NBS `easyquery`** with `dbcode=hgjd` (national quarterly) ✅:
- real GDP cumulative and single-quarter YoY,
- nominal GDP (current-price) level, cumulative and single-quarter.

Then `gdp_deflator_yoy = nominal_gdp_yoy − real_gdp_yoy`, computed on matched single-quarter (not cumulative) series. Discover the `zb` indicator codes via `m=getTree` — do not hardcode them.

⚠️ **Two warnings.** (1) NBS **revises** GDP, including benchmark revisions that restate years of history; store `retrieved_at` and consider ALFRED-style vintaging. (2) The registry itself flags the deflator as quarterly and noisy — use a 4-quarter average for the trend, as `registry_context.json` instructs.

### 5.9 Government bond net issuance and fiscal deposits (no data)

**`fiscal_deposits`.** The series is Δ政府存款 (government deposits at the PBoC). It lives in the **货币当局资产负债表 (Balance Sheet of Monetary Authority)**, published monthly by the PBoC 调查统计司 — verified example PDF https://www.pbc.gov.cn/diaochatongjisi/attachDir/2025/12/2025121517172659799.pdf ✅ (unit 亿元), with older years as HTML at `…/eportal/fileDir/defaultCurSite/resource/cms/2015/07/2009s04.htm` ✅. Route: crawl the yearly 货币统计概览 nodes under https://www.pbc.gov.cn/diaochatongjisi/116219/116319/index.html ✅, pull the balance sheet for each month, extract the 政府存款 line, first-difference it. ⚠️ Your parser must handle both the PDF (recent) and HTML (legacy) layouts.

**`govt_bond_issuance`.** Two complementary routes: (a) **MOF** — 记账式国债 issuance announcements https://gks.mof.gov.cn/ztztz/guozaiguanli/gzfxzjs/ ✅ for central government, plus the 债务管理司 https://zwgls.mof.gov.cn/ ✅ **monthly local-government bond issuance and debt-balance reports** (local government bonds are the larger and more cyclically important leg); (b) **CFETS `bnBondEmit`** 🟡 → `https://www.chinamoney.com.cn/ags/ms/cm-u-bond-an/bnBondEmit`, which gives `债券全称, 债券类型, 发行日期, 债券期限, 计划发行量, 债券评级` and can be filtered to 国债/地方政府债 and aggregated to a monthly gross issuance figure. For **net** issuance you must also subtract maturities — ⚠️ no single verified source for the maturity schedule; derive it from the outstanding-bond register on ChinaBond or from the issuance history you have accumulated.

### 5.10 `dr007` ends 2024-12

**How to close it.** Re-pull the whole series from **CFETS** rather than extending the third-party research-repo file: `ak.repo_rate_hist(start_date="20150101", end_date="<today>")` 🟡 for FDR007, or the CFETS pledged-repo page https://www.chinamoney.com.cn/english/mdtqapprp/ ✅ for true DR007 (history from **15 Dec 2014** ✅). **Do not splice a CFETS pull onto the existing monthly-average file** — the existing values are monthly means of daily fixings from a mirror, and mixing conventions mid-series is worse than a shorter series. Rebuild from scratch and keep the daily grain, aggregating to monthly only at read time.

### 5.11 `cgb_10y` starts 2024-08 only

Closed by the same ChinaBond `historyQuery` loop as §5.5 — pull 2015→today in 12-month windows. Note the existing values are **monthly averages of daily fixings**, with partial first and last months; rebuild daily and re-aggregate.

### 5.12 The quarterly-only cluster

`tsf_stock_yoy`, `tsf_stock_level`, `walr_general`, `excess_reserve_ratio`, `core_cpi_yoy`, `ncd_issuance_war` are quarterly **only because the MPR PDF was the sole reachable source**. Of these:

- **`tsf_stock_yoy` becomes monthly** via the PBoC 社会融资规模存量统计数据报告 ✅ (monthly release, ~12th) — http://www.pbc.gov.cn/diaochatongjisi/116219/116225/5565443/index.html ✅ and the 社会融资规模 landing page https://www.pbc.gov.cn/diaochatongjisi/116219/116319/3959050/3959051/index.html ✅. This is a real upgrade in frequency.
- **`core_cpi_yoy` becomes monthly** via NBS `easyquery` ✅ — NBS publishes core CPI (扣除食品和能源) monthly. The 5 sparse quarterly observations exist only because the seed could reach nothing but MPR prose. **This is the second-cheapest win in the file.**
- **`walr_general` and `excess_reserve_ratio` stay quarterly forever.** ✅ There is no higher-frequency publication. Accept it.
- **`ncd_issuance_war` stays quarterly** and remains a distinct series from `ncd_1y_aaa` (§5.4).

### 5.13 `rrr_large` / `rrr_small` truncated to 2022-04-25 … 2025-05-15

**Why.** The mirror's earlier points were an incomplete step history (it jumps from 2018-10-15 straight onward, missing the 2019 and 2021 change dates), so earlier points were withheld rather than forward-filled wrongly.

**How to close it.** Rebuild the **full change history from PBoC announcements** — the RRR cuts are announced as 公告 under 货币政策司 and mirrored on gov.cn in English (several verified announcement URLs are already listed in `research/03-liquidity-indicators.md` §Sources, e.g. the May 2025 cut ✅). Take `ak.macro_china_reserve_requirement_ratio()` ⚠️ as a *candidate* change list, then **verify every single date against a PBoC or gov.cn announcement before accepting it**. RRR is a step series where one missing change corrupts every subsequent month.

### 5.14 `tsf_flow` ends 2026-04

**Why.** It comes from MOFCOM's republication (`data.mofcom.gov.cn/gnmy/shrzgm.shtml`), which lags the PBoC headline by 2–3 months ✅.

**How to close it.** Take `tsf_flow` from the **PBoC monthly release directly** (~12th of the following month ✅) instead of the MOFCOM mirror, and demote `ak.macro_china_shrzgm()` to a backfill/cross-check role. That removes a 2–3 month lag from your most cyclically-informative credit series.

### 5.15 The environment constraint itself

Not a data gap but the root cause of all of them: this sandbox's egress proxy 403s every macro-data host. **Re-run the entire acquisition on a machine with normal internet access.** Nothing in §4 requires paid data.

---

## 6. Provenance warning

> **Every single value currently in `data/seed/series.json` came from a third-party GitHub mirror. Not one value was fetched from a primary publisher's own domain.**

This is stated plainly in the file's own `meta.note` and `meta.gaps`, and it is repeated here because it is the most important fact about the dataset.

Specifically, the two source families are:

1. **`openecon-data`** — a curated China macro snapshot with an `AS_OF` date of **2026-07-19**, itself mirroring PBoC and NBS releases *via the East Money datacenter*. This is a mirror of a mirror. It supplies M1, M2, new RMB loans, CPI, PPI, LPR, real GDP, FX reserves and the 10Y CGB point.
2. **The full quarterly text of the PBoC 货币政策执行报告, 2018Q1–2026Q1**, mirrored as cleaned text on GitHub, from which quarterly figures were extracted verbatim by regex. This family is *primary-source wording*, but still **retrieved from a mirror, not from pbc.gov.cn**.

Plus two smaller mirrors: a research repo (`Hosen760/Asset-allocation`) for monthly DR007, and `lightfor.github.io` for the RRR step series and single-quarter GDP.

**What was done well, and should be preserved:** nothing was estimated, interpolated or recalled from memory; series that could not be verified were **omitted and listed in `gaps` rather than filled**; cross-mirror agreement was checked on every overlapping point for M2, CPI, PPI, TSF-stock YoY and GDP; the LPR change history reproduces the published record exactly; and the MPR's own stated period-on-period deltas reconcile with its excess-reserve levels. The dataset is internally honest.

**What that does not buy you.** Mirror agreement is not primary verification — two mirrors can share one upstream and one error. An `AS_OF 2026-07-19` snapshot is already stale. Mirrors do not carry revisions, so an NBS GDP benchmark revision will never reach you. And mirrors silently drop or truncate series, which is exactly what produced the incomplete RRR step history and the 2024-12 end of DR007.

> **Re-pulling every series from its primary publisher is the first task for anyone taking this into production.** Treat `series.json` as a well-documented scaffold and a regression fixture — its LPR history, its cross-checked M2/CPI/PPI values and its MPR-derived quarterlies are excellent test cases for a new pipeline — **not as a system of record.** Until that re-pull happens, do not publish any value from it externally, and do not attribute any value in it to the PBoC or NBS directly.

---

## 7. Licensing and redistribution summary

| Source | Auth | Rate limit | Redistribution | Mark |
|---|---|---|---|---|
| **BIS** | None | ⚠️ none published | ✅ **Unrestricted with citation of BIS as source**; translations must be marked unofficial; must not imply endorsement | ✅ Best-licensed source here |
| **World Bank** | ✅ None ("API keys no longer necessary") | ⚠️ unpublished | ✅ Mostly **CC-BY 4.0** | ✅ |
| **FRED** | ✅ Free 32-char key (JSON API); none for CSV | ✅ **120 req/min/key** | ⚠️ Governed by FRED Terms of Use; **each series inherits its original source's copyright** (IMF/OECD for most China series) | ✅ |
| **IMF** | ⚠️ Legacy: none | ✅ **≤3,000 series per response** | ⚠️ Attribution required; commercial redistribution restricted | ⚠️ |
| **NBS** | None | ⚠️ unpublished; throttles in practice | ✅ Reprint/quotation permitted "reasonably and in good will" for news and free information, **must cite "Source: National Bureau of Statistics"** | ✅ |
| **PBoC** | None | ⚠️ unpublished | ⚠️ No explicit licence; government copyright assumed; attribute | ⚠️ |
| **CFETS / chinamoney** | Session cookie (not auth); **CMDS/iData feeds are commercial contracts** | ⚠️ unpublished | ⚠️ Rights asserted over market data; internal research normal, redistribution is a legal question | ⚠️ |
| **ChinaBond / CCDC** | None | ⚠️ ≤1-year query window | ⚠️ Curves and indices are licensed products | ⚠️ |
| **SHIBOR / NIFC** | None | ⚠️ unpublished | ⚠️ Benchmark; full-history redistribution typically licensed | ⚠️ |
| **MOF** | None | ⚠️ unpublished | ⚠️ Government copyright; attribute | ⚠️ |
| **akshare** | None (MIT library) | n/a | ⚠️ Library is MIT; **the data carries the upstream publisher's terms** | ✅ |
| **tushare** | ✅ Token + points | ⚠️ per-interface caps | ⚠️ Terms restrict redistribution | ⚠️ |
| **East Money / Sina** | None | ⚠️ unpublished, blocks aggressively | ⚠️ Rights asserted over site content | ⚠️ |
| **Investing.com** | None | ⚠️ blocks scrapers | ⚠️ **ToS prohibits automated extraction** | ⚠️ |

**Practical rule.** If the tracker will be published: source `reer`, the credit-to-GDP gap and `usdcny` from **BIS / World Bank / FRED** (redistributable with attribution), cite **NBS** for prices and GDP with the required wording, and for PBoC/CFETS/ChinaBond-derived series **publish the chart and the analysis, not the underlying value series**, unless you have cleared redistribution.

---

## 8. Sources

**PBoC — 中国人民银行**
- Root: https://www.pbc.gov.cn/ · English: https://www.pbc.gov.cn/en/3688006/index.html
- 调查统计司 statistics hub: https://www.pbc.gov.cn/diaochatongjisi/116219/116319/index.html
- 货币统计概览 2025: https://www.pbc.gov.cn/diaochatongjisi/116219/116319/5570903/5570886/index.html
- 货币统计概览 2024: https://www.pbc.gov.cn/diaochatongjisi/116219/116319/5225358/5225360/index.html
- 货币统计概览 2019: https://www.pbc.gov.cn/diaochatongjisi/116219/116319/3750274/3750284/index.html
- 货币统计概览 (further node): https://www.pbc.gov.cn/diaochatongjisi/116219/116319/4780803/4780805/index.html
- 社会融资规模: https://www.pbc.gov.cn/diaochatongjisi/116219/116319/3959050/3959051/index.html
- 2024年社会融资规模存量统计数据报告: http://www.pbc.gov.cn/diaochatongjisi/116219/116225/5565443/index.html
- 社会融资规模存量统计表 (PDF example): https://www.pbc.gov.cn/eportal/fileDir/diaochatongjisi/resource/cms/2022/04/2022041816440579530.pdf
- 货币当局资产负债表 (PDF example, Dec 2025): https://www.pbc.gov.cn/diaochatongjisi/attachDir/2025/12/2025121517172659799.pdf
- 货币当局资产负债表 (legacy HTML): https://www.pbc.gov.cn/eportal/fileDir/defaultCurSite/resource/cms/2015/07/2009s04.htm
- 2025年11月金融统计数据报告: https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2025121215073692061/index.html
- 2026年5月金融统计数据报告: https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2026061214273613328/index.html
- 公开市场业务交易公告: https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/index.html
- 公开市场业务公告: https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125469/index.html
- Open market operations (EN): https://www.pbc.gov.cn/en/3688241/3688765/index.html
- DR007 definition (EN): https://www.pbc.gov.cn/en/3688006/3689169/3753752/index.html
- Monetary Policy Reports (EN index): https://www.pbc.gov.cn/en/3688229/index.html
- MPR 2026 Q2 PDF: https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2026081218034520348/2026081218031050203.pdf
- MPR 2026 Q1 PDF: https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2026051118520164705/2026051118500062162.pdf
- MPR 2025 Q3 PDF: https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/5896222/2025111111175096136.pdf
- MPR 2025 Q2 PDF (provincial mirror): https://xining.pbc.gov.cn/goutongjiaoliu/113456/113469/2025092212554814094/2025081819132397368.pdf
- MPR 2025 Q1 PDF (provincial mirror): https://xining.pbc.gov.cn/zhengcehuobisi/125207/125227/125957/f5c4690f2cbd40918bf24c2d39ac58af/2025091218344076234/2025081517321679368.pdf
- MPR 2024 Q4 PDF: https://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125957/5347949/ad0bc3efe0234fed8cc6260a134a6e95/2025022618190099812.pdf
- MPR 2024 Q2 PDF: http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/5427706/2025081217013923839.pdf

**NBS — 国家统计局**
- Root: https://www.stats.gov.cn/ · English: https://www.stats.gov.cn/english/
- National Data database: https://data.stats.gov.cn/
- easyquery endpoint: https://data.stats.gov.cn/easyquery.htm · http://data.stats.gov.cn/english/easyquery.htm
- 数据发布: https://www.stats.gov.cn/sj/zxfb/
- 发布日程: https://www.stats.gov.cn/sj/fbrc/ · 发布日程表: https://www.stats.gov.cn/xxgk/sjfb/fbrcb/
- CPI/PPI hub: https://www.stats.gov.cn/hd/lyzx/zxgk/cpippi/
- 数据解读: https://www.stats.gov.cn/sj/sjjd/
- English statistical data: https://www.stats.gov.cn/english/Statisticaldata/
- Terms of service: https://www.stats.gov.cn/english/nbs/200701/t20070104_59236.html
- National Data disclaimer: https://data.stats.gov.cn/english/login.htm?m=toDisclimer
- Reference easyquery client (parameter structure): https://github.com/khaeru/data/blob/master/cn_nbs.py
- Other easyquery clients: https://github.com/xiancode/STATS_HG_DATA/blob/master/get_cs_stats_data.py · https://github.com/Wchaos/national_data_spider

**CFETS / 中国货币网**
- Root: https://www.chinamoney.com.cn/ · English: https://www.chinamoney.com.cn/english/ · mirror: https://iftp.chinamoney.com.cn/english/
- Fixing repo rate (EN): https://iftp.chinamoney.com.cn/english/bmkfrr/ · (CN) https://www.chinamoney.com.cn/chinese/bkfrr/
- Pledged repo quotes (DR001/DR007/DR014): https://www.chinamoney.com.cn/english/mdtqapprp/
- CFETS RMB Index: https://www.chinamoney.com.cn/english/bmkidxrud/ · https://iftp.chinamoney.com.cn/english/bmkidxrud/
- CFETS RMB Index article examples: https://www.chinamoney.com.cn/english/bmkidxrud/20251103/3224255.html · https://www.chinamoney.com.cn/english/bmkidxrud/20251201/3241786.html · https://www.chinamoney.com.cn/english/bmkidxrud/20260506/3333002.html
- CNY central parity: https://www.chinamoney.com.cn/english/bmkcpr/ · (CN) https://iftp.chinamoney.com.cn/chinese/bkccpr/
- SHIBOR page: https://www.chinamoney.com.cn/chinese/bkshibor/
- Closing yield curve history page: https://www.chinamoney.com.cn/chinese/bkcurvclosedyhis/
- Bond info query: https://www.chinamoney.com.cn/chinese/scsjzqxx/ · bond market quotes: https://www.chinamoney.com.cn/chinese/mkdatabond/ · FX market quotes: http://www.chinamoney.com.cn/chinese/mkdatapfx/
- Business & services (CMDS / iData / iFTP, commercial): https://www.chinamoney.com.cn/english/ausbas/
- JSON/CSV endpoints: `https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/FrrHis` · `…/cm-u-bk-currency/ClsYldCurvHis` · `…/cm-u-bk-currency/ClsYldCurvCurvGO` · `…/cm-u-bk-shibor/IfccHis` · `…/cm-u-bond-an/bnBondEmit` · `https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/currency/frr-chrt.csv` · `…/currency/fdr-chrt.csv` · `http://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/rfx-sp-quot.json` · `…/fx/rfx-sw-quot.json`

**ChinaBond / CCDC**
- Yield curve main: https://yield.chinabond.com.cn/cbweb-mn/yield_main?locale=en_US
- Curve history query: https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/historyQuery?startDate=2019-02-07&endDate=2020-02-04&gjqx=0&qxId=ycqx&locale=cn_ZH
- More curves: https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/more?locale=en_US
- Historical data: https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/showHistory?locale=en_US
- MOF–ChinaBond CGB curve: https://yield.chinabond.com.cn/cbweb-czb-web/czb/moreInfo?locale=en_US&nameType=1
- Indices: https://yield.chinabond.com.cn/cbweb-mn/indices/multi_index_query?locale=en_US · https://yield.chinabond.com.cn/cbweb-mn/indices/singleIndexQueryResult · https://yield.chinabond.com.cn/cbweb-mn/indices/single_index_query
- Root: https://www.chinabond.com.cn/

**SHIBOR / NIFC**
- https://www.shibor.org/ · 报价: https://www.shibor.org/chinese/llshibor/
- Panel banks: https://www.shibor.net.cn/shibor/panelbanks/ · Code of conduct: https://www.shibor.sh.cn/shibor/codeofconduct/

**MOF — 财政部**
- 政府债券管理: https://gks.mof.gov.cn/ztztz/guozaiguanli/
- 记账式国债(含特别国债)发行: https://gks.mof.gov.cn/ztztz/guozaiguanli/gzfxzjs/
- 储蓄国债发行: https://gks.mof.gov.cn/ztztz/guozaiguanli/gzfxdzs/
- 国债管理工作动态: https://gks.mof.gov.cn/ztztz/guozaiguanli/gzfxgzdt/
- 债务管理司 (monthly local government bond reports): https://zwgls.mof.gov.cn/
- 信息公开: https://www.mof.gov.cn/gkml/

**FRED / ALFRED**
- Series: https://fred.stlouisfed.org/series/MYAGM2CNM189N · https://fred.stlouisfed.org/series/MYAGM1CNM189N · https://fred.stlouisfed.org/series/CHNCPIALLMINMEI · https://fred.stlouisfed.org/series/CHNPIEATI01GYM · https://fred.stlouisfed.org/series/CHNPIEATI01GYQ · https://fred.stlouisfed.org/series/INTDSRCNM193N · https://fred.stlouisfed.org/series/DEXCHUS · https://fred.stlouisfed.org/series/CCRETT01CNQ661N
- Table data example: https://fred.stlouisfed.org/data/CHNPIEATI01GYM.txt · https://fred.stlouisfed.org/data/INTDSRCNM193N
- Tag browsers: https://fred.stlouisfed.org/tags/series?t=china%3Bcpi · https://fred.stlouisfed.org/tags/series?t=china%3Bppi · https://fred.stlouisfed.org/tags/series?t=china%3Bmonthly%3Bppi
- API docs: https://fred.stlouisfed.org/docs/api/fred/ · Terms of use: https://fred.stlouisfed.org/docs/api/terms_of_use.html · Legal: https://fred.stlouisfed.org/legal
- Download help: https://fredhelp.stlouisfed.org/category/fred/data/downloading/
- ALFRED vintages: https://alfred.stlouisfed.org/series?seid=MYAGM2CNM189N

**BIS**
- Data Portal: https://data.bis.org/ · Tools: https://data.bis.org/help/tools · Legal: https://data.bis.org/help/legal
- SDMX API docs: https://stats.bis.org/api-doc/v1/
- Example query: https://stats.bis.org/api/v1/data/WS_EER_M/M.N.B.CH/all?startPeriod=2000&endPeriod=2000&detail=full
- Terms of permitted use of BIS statistics: https://www.bis.org/terms_statistics.htm · https://www.bis.org/terms_conditions.htm#Copyright_and_Permissions
- Third-party API notes: https://fgeerolf.com/data/bis/api.html · https://github.com/api-evangelist/bis

**IMF**
- New API base: https://api.imf.org/external/sdmx/3.0
- Legacy SDMX service: http://dataservices.imf.org/REST/SDMX_XML.svc/Dataflow
- API response notes: https://datahelp.imf.org/knowledgebase/articles/2005918-api-response
- Guides: https://bd-econ.com/imfapi1.html · https://fgeerolf.com/data/imf/api.html

**World Bank**
- Indicators API: https://api.worldbank.org/v2/country/CHN/indicator/{CODE}?format=json&per_page=1000
- About the Indicators API: https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation
- Basic call structures: https://datahelpdesk.worldbank.org/knowledgebase/articles/898581-api-basic-call-structures
- Data360 API: https://data360.worldbank.org/en/api
- Licensing: https://datacatalog.worldbank.org/public-licenses

**Python libraries**
- akshare repo: https://github.com/akfamily/akshare · docs: https://akshare.akfamily.xyz/
- akshare source files verified this session: `akshare/__init__.py` · `akshare/economic/macro_china.py` · `akshare/interest_rate/interbank_rate_em.py` · `akshare/rate/repo_rate.py` · `akshare/bond/bond_china_money.py` · `akshare/bond/bond_china.py` · `akshare/bond/bond_cbond.py` · `akshare/fx/cons.py` · `akshare/fx/fx_quote.py` · `docs/tutorial.md` · `docs/changelog.md`
- tushare: https://tushare.pro/ · docs: https://tushare.pro/document/2 · legacy shibor docs: http://tushare.org/shibor.html

**Scraping routes (use with caution)**
- East Money datacenter API: https://datacenter-web.eastmoney.com/api/data/v1/get · https://datacenter.eastmoney.com/api/data/get
- East Money money supply page: https://data.eastmoney.com/cjsj/hbgyl.html
- MOFCOM TSF republication: https://data.mofcom.gov.cn/gnmy/shrzgm.shtml
- Investing.com SHIBOR 1Y history: https://www.investing.com/rates-bonds/shibor-1-year-historical-data

**Related documents in this repository**
- `research/01-definitions-framework.md` — definitions and the analytical framework
- `research/02-monetary-indicators.md` — monetary indicator catalogue
- `research/03-liquidity-indicators.md` — liquidity indicator catalogue (its `## Sources` section carries an extensive list of PBoC/CFETS/ChinaBond/policy-announcement URLs that complements this document)
- `research/06-implications.md` — reading the indicators
- `data/seed/series.json` — the seed dataset this manual is the companion to; read its `meta.note` and `meta.gaps` first
