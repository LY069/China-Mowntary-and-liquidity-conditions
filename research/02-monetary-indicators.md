# China Monetary Conditions — Definitive Indicator Catalogue

**Scope:** the *medium-term policy stance transmitted to the real economy*. Short-term interbank liquidity (DR007, R007, NCD rates, OMO net injection, excess-reserve tightness, month-end/quarter-end funding squeezes) is deliberately **out of scope** — covered separately.

**Compiled:** 2026-09-12.

---

## 0. Reader's guide, conventions and a data-access caveat

### 0.1 Data-access caveat (important, read first)

This session's network egress was restricted at the organisation gateway: **direct fetches to `pbc.gov.cn`, `bis.org`/`data.bis.org`, `fred.stlouisfed.org`, `chinamoney.com.cn`, `stats.gov.cn`, `chinabond.com.cn` and most other hosts were refused (HTTP 403 at the CONNECT stage).** Everything below is therefore grounded in web-search retrieval of those pages' contents plus reputable secondary sources, with the canonical URLs cited so a user with normal network access can pull the primary series directly.

Consequences you must respect when using this document:
- Every **URL** below appeared in retrieved search results and is believed live, but page contents were not read end-to-end in all cases.
- Where a number, series ID, spread or date could not be confirmed from retrieved material, it is explicitly marked **`[unverified]`**. Do not propagate `[unverified]` items into a production dashboard without checking the primary source.
- **No series ID, statistic or endpoint in this document is invented.** Items I could not confirm are flagged rather than guessed. Wind codes in particular are flagged throughout as `[unverified]` — I had no Wind access.

### 0.2 Sign convention used throughout

Unless a row says otherwise:

> **`+` = LOOSER monetary conditions** (more accommodative stance transmitted to the real economy).

This means several indicators must be **sign-flipped** before being combined into any composite: real lending rates, the policy rate, the RRR, and the REER all have to be entered with a negative weight (a rise in each is *tighter*). The shortlist in §7 states the convention explicitly per line.

### 0.3 The single most important framing for China in 2024–2026

China's *nominal* monetary indicators look easy and its *real* ones look tight. The policy rate is at a record low (7-day OMO 1.40% since May 2025), LPRs are at record lows (3.00%/3.50%), the weighted-average lending rate is at a record low (~3.1–3.5%), and yet the GDP deflator was negative for roughly twelve consecutive quarters through Q1 2026 (2025 full-year deflator ≈ **−1%**), only turning positive (+1.6%) in Q2 2026. The IMF's 2025 Article IV (Board concluded 13 Feb 2026) states plainly that "**financial conditions remain tight overall amid high real interest rates, and credit growth to the private sector has continued to decline**."

**Practical rule: never read China's stance off a nominal rate.** Deflate by the GDP deflator (best), PPI (best for industrial borrowers) or core CPI. A 3.1% corporate loan rate against a −1% deflator is a **~4.1% real** corporate borrowing cost in an economy whose natural rate estimates are around 2% or lower — i.e. restrictive, not accommodative. This is the central analytical point of the whole catalogue.

### 0.4 Release calendar at a glance

| Release | Publisher | Freq | Typical timing | Lag |
|---|---|---|---|---|
| Financial Statistics Report (M0/M1/M2, new RMB loans, deposits) | PBoC 调查统计司 | Monthly | Usually between the 9th and the 15th; NBS documents the standard as **within 15 days of month-end** | ~10–15 days |
| Aggregate Financing to the Real Economy — flow (社会融资规模增量) | PBoC | Monthly | Same release as above | ~10–15 days |
| AFRE — stock (社会融资规模存量) | PBoC | Monthly | Same release | ~10–15 days |
| China Monetary Policy Report (货币政策执行报告, contains WALR) | PBoC | Quarterly | ~5–7 weeks after quarter-end (e.g. Q2 2025 report dated **15 Aug 2025**; Q3 2025 report dated **11 Nov 2025**) | ~6 weeks |
| LPR fixing | NIFC/CFETS under PBoC | Monthly | **09:00 CST on the 20th** (next business day if a holiday) | 0 |
| Monetary Authority Balance Sheet (货币当局资产负债表) — base money, 外汇占款 | PBoC | Monthly | With the statistics-department upload, typically later in the following month | ~3–5 weeks |
| Depository Corporations Survey (存款性公司概览) | PBoC | Monthly | As above | ~3–5 weeks |
| FX reserves | SAFE/PBoC | Monthly | ~7th of following month | ~7 days |
| CFETS RMB Index | CFETS | Weekly (Friday) + month-end | Friday evening; month-end summary early in the new month | days |
| BIS effective exchange rates | BIS | Monthly | ~mid-month | ~2–6 weeks |
| BIS credit-to-GDP gap | BIS | Quarterly | ~2 quarters lag | ~5–6 months |
| NIFD macro leverage ratio (宏观杠杆率) | NIFD/CNBS | Quarterly | ~3–4 weeks after quarter-end | ~1 month |

**Caveat:** the PBoC does not commit to a fixed day-of-month for the financial statistics release. It appears on the SDDS advance-release calendar and is frequently pushed to the 12th–15th, occasionally later. Combined Jan–Feb releases and Chinese New Year timing routinely shift it. Treat "the 10th" as a habit, not a rule. `[exact day-of-month rule unverified]`

---

## A. Quantity of Money

### A.1 M0 — Currency in circulation

| Field | Detail |
|---|---|
| English | Currency in circulation |
| Chinese | 流通中现金 |
| Abbrev. | M0 |
| Definition | Banknotes and coin held outside the banking system (i.e. excluding vault cash of depository institutions). |
| Publisher | PBoC, Survey & Statistics Department (调查统计司) |
| Frequency / lag | Monthly, within ~15 days of month-end |
| Source | 货币统计概览 — e.g. 2025: https://www.pbc.gov.cn/diaochatongjisi/116219/116319/5570903/5570886/index.html ; 2024: https://www.pbc.gov.cn/diaochatongjisi/116219/116319/5225358/5225360/index.html ; English Financial Statistics Reports: https://www.pbc.gov.cn/en/3688247/3688978/3709137/ |
| FRED | M0 for China appears in FRED's IMF-IFS-derived China block (see M2 entry for the family) `[exact M0 series ID unverified]` |
| History | Monthly from 1999 on PBoC site; longer annual back-history in the China Financial Yearbook |
| How to read | Weak signal for the *stance*. M0 growth is dominated by CNY seasonality (Chinese New Year cash demand), rural/informal-sector cash intensity and, structurally downward, mobile-payment substitution. A sustained M0 acceleration outside CNY sometimes flags precautionary cash hoarding or rural stimulus transfers. |
| Distortions | **Severe CNY seasonality** — always compare same-lunar-position months or use a Jan+Feb combined reading. Long-run downtrend from digital payments means the *level* trend is not informative. e-CNY is counted in M0 — its scale-up mechanically shifts composition, not the total `[treatment confirmation unverified]`. |

### A.2 M1 — Narrow money, and the January 2025 redefinition

| Field | Detail |
|---|---|
| English | Narrow money |
| Chinese | 狭义货币 |
| Abbrev. | M1 |
| **Definition from Jan 2025** | **M0 + corporate demand deposits + household (personal) demand deposits + client provisions (reserve funds) held at non-bank payment institutions** |
| **Definition before Jan 2025** | M0 + corporate (non-financial enterprise) demand deposits **only** |
| Publisher | PBoC 调查统计司 |
| Frequency / lag | Monthly, ~10–15 days |
| Source | As A.1. English releases: https://www.pbc.gov.cn/en/3688247/3688978/3709137/ |
| FRED | `MYAGM1CNM189N` — "M1 for China", IMF IFS, national currency, monthly NSA: https://fred.stlouisfed.org/series/MYAGM1CNM189N ; also `MANMM101CNM189S` (OECD MEI, M1 for China, SA) https://fred.stlouisfed.org/series/MANMM101CNM189S — **note both are legacy/discontinued-vintage series running only through ~2018–2019** and therefore useless for current monitoring. Use PBoC/CEIC/Wind for live data. |
| CEIC | China money supply block under the PBoC source; see https://www.ceicdata.com/en/china (series names of the form "CN: Money Supply: M1") `[exact CEIC code unverified]` |
| History | Old-basis monthly back to 1999 (annual to 1952 in yearbooks). **New-basis monthly starts January 2024** — the PBoC restated only 2024 on a comparable basis when it introduced the new caliber. |

#### The January 2025 M1 redefinition — what happened and how to splice

**What changed.** The PBoC announced in **December 2024** that, beginning with the **January 2025** statistics (first published early February 2025), M1 would be broadened from `M0 + corporate demand deposits` to `M0 + corporate demand deposits + household demand deposits + non-bank payment institutions' client provisions (客户备付金)`. The rationale is convergence with international practice: Chinese household demand deposits and Alipay/WeChat Pay balances are transactionally indistinguishable from corporate sight money in a mobile-payment economy, so excluding them had made M1 a progressively worse measure of spendable money.

**Scale of the break.** The level roughly **doubles**: old-basis M1 was approximately **RMB 67 trillion** at end-December 2024 versus roughly **RMB 112 trillion** on the new basis. `[the 112tn figure appeared in secondary commentary; verify against the PBoC's own restated table before publishing]`

**How to splice — recommended procedure.**

1. **Do not splice levels.** A doubling in level is a pure definitional artefact; a spliced level series is meaningless and will corrupt any ratio (M1/GDP, M1/M2, money multiplier variants).
2. **Splice growth rates, not levels.** The PBoC published **restated new-basis month-end balances and YoY growth rates for all of 2024**. That gives you 12 months of overlap on the new basis (Jan 2024 → Dec 2024) and a clean new-basis YoY series from **January 2025** onwards.
3. **For history before Jan 2024**, maintain **two parallel series**:
   - `M1_old_yoy` — old caliber, 1999→Dec 2024 (PBoC stopped publishing it after the switch).
   - `M1_new_yoy` — new caliber, Jan 2024→present.
   Plot both; never concatenate them into one line without a vertical break marker.
4. **If you must have a single long series for regression work**, the defensible approach is a **backcast**: reconstruct new-basis M1 for history by adding household demand deposits (published in the 金融机构人民币信贷收支表 / depository corporations survey, available monthly for decades) to old-basis M1. Non-bank payment client provisions are small relative to household demand deposits and are only centrally-held from the 2017–2019 centralisation reform onwards, so set them to zero pre-2017 and note the approximation. **Label this clearly as an author reconstruction, not official data.**
5. **Level-shift dummies** in any model spanning the break; or better, model the growth rate directly.

**Why it matters for stance reading.** The new M1 is **less volatile and less cyclical** than the old one. Old M1 was almost pure corporate sight money — an exceptionally sharp read on corporate transaction demand and property-sales cash flow. New M1 dilutes that with household demand deposits, which move with savings-allocation behaviour and deposit-rate arbitrage rather than with the business cycle. **The new series is a better money measure and a worse animal-spirits proxy.** For the corporate-activity read, continue tracking **corporate demand deposits directly** from the credit-and-deposit table rather than relying on headline M1.

### A.3 M2 — Broad money

| Field | Detail |
|---|---|
| English | Broad money |
| Chinese | 广义货币 |
| Abbrev. | M2 |
| Definition | M1 + household time and savings deposits + corporate time deposits + other deposits (incl. certain non-depository financial institution deposits, margin/security deposits, housing provident fund deposits). IMF's IFS description: "M1 plus time and savings deposits in national currency of resident non-bank financial corporations and non-bank non-government sectors with the PBC and banking institutions." |
| Publisher | PBoC 调查统计司 |
| Frequency / lag | Monthly, ~10–15 days |
| Source | https://www.pbc.gov.cn/diaochatongjisi/116219/116319/5570903/5570886/index.html ; English: https://www.pbc.gov.cn/en/3688247/3688978/3709137/ ; NBS indicator note on money supply compilation: https://www.stats.gov.cn/zs/tjws/zytjzbqs/hbgyl/202410/t20241025_1957180.html |
| FRED | `MYAGM2CNM189N` — "M2 for China", IMF IFS, monthly NSA, **Dec 1998 – Aug 2019 (stale)**: https://fred.stlouisfed.org/series/MYAGM2CNM189N . ALFRED vintages: https://alfred.stlouisfed.org/series?seid=MYAGM2CNM189N |
| CEIC / Wind | CEIC "CN: Money Supply: M2"; Wind EDB code `[unverified]` |
| History | Monthly 1999→; annual back to 1952 |
| Reference levels | End-Dec 2024: **RMB 313.53tn, +7.3% YoY**. End-2025: **+8.5% YoY**. Jan 2026: **+9.0% YoY**. Jul 2026: **+7.7% YoY** (down from 8.0% in June). |
| How to read | The PBoC's stated intermediate-target language is that **M2 and AFRE growth should be "basically in line with nominal economic growth"** (与名义经济增速基本匹配). So the operative statistic is not M2 growth itself but **M2 growth minus nominal GDP growth**. Positive gap = money growing faster than the economy = accommodative; negative = passive tightening. In the deflation years 2023–2025 the gap was *large and positive* (M2 8%+ vs nominal GDP ~4%), which reads as loose — but this is exactly the reading that misleads, because the excess money was being absorbed into time deposits rather than circulating (see A.5 and the velocity caveat). |
| Typical range | 8–14% YoY over 2015–2022; 7–9% over 2024–2026. Sub-8% is historically very weak; double-digit prints now require deliberate stimulus. |
| Distortions | (i) **Fiscal-deposit timing** — government deposits at the PBoC are *outside* M2; heavy bond issuance drains M2 until the proceeds are spent, creating spurious monthly swings. (ii) **Wealth-management product (WMP) migration** — money rotating between bank deposits and off-balance-sheet WMPs moves M2 without any change in monetary conditions. The 2022 and 2024 bond-fund rallies pulled deposits out; the 2023 rate-cut cycle pushed them back in. (iii) **Crackdown on 手工补息 (manual supplementary interest) from April 2024** mechanically shrank corporate deposits and depressed M1 and M2 growth for roughly a year — a *regulatory* distortion, not a monetary tightening. (iv) **Local-government debt swap programmes** convert LGFV loans into government bonds, reshuffling AFRE composition and deposit flows. (v) 2018 addition of non-depository-financial-institution deposits to M2 `[precise scope-change history unverified]`. |

### A.4 M1–M2 growth gap — the "scissors gap" (剪刀差)

| Field | Detail |
|---|---|
| English | M1–M2 growth differential / money growth scissors |
| Chinese | M1-M2 剪刀差 (货币增速剪刀差) |
| Construction | `Gap_t = M1_yoy_t − M2_yoy_t`, in percentage points. |
| Source | Derived from A.2/A.3. Charted at TrendForce DataTrack: https://datatrack.trendforce.com/Chart/content/2928/china-money-supply-m1-m2 |
| History | Back to the 1990s on old-basis M1; **on the new (post-Jan-2025) M1 basis only from Jan 2024** — this is a genuine break in the most-watched sentiment indicator in Chinese macro. |
| How to read | **Positive and rising gap = money moving from savings buckets into transaction buckets = firms and households converting idle balances into spendable cash = pre-cursor to capex, restocking, property transactions.** Classically leads PPI and industrial profits by roughly 3–6 months and has been the market's favourite "animal spirits" proxy. **Negative and widening = 定期化 (termification) — the shift into time deposits — signalling that the private sector sees no attractive use of funds and is locking in yield instead.** |
| Typical range | Historically ±10pp at cycle extremes (e.g. +10pp or more in 2009–10 and 2016 property booms; around −10pp at the 2024 trough on the old basis). On the **new** basis the amplitude is structurally compressed because household demand deposits are now inside M1 and they co-move with M2. |
| Reference reading | **Q2 2026: −3.1pp**, narrowing from −3.6pp — still firmly negative, i.e. termification remains entrenched and corporate demand-deposit momentum has not recovered. |
| Key thresholds | Crossing from negative to positive is the classic regime-change marker. A gap sustained below −5pp on the new basis signals deep balance-sheet-recession behaviour. |
| Caveats | (1) **Do not compare post-2024 gap levels to pre-2024 history** — the redefinition changed the mean and the amplitude. Rebase to a z-score computed on the new basis only, or reconstruct a backcast new-basis M1 (A.2 step 4). (2) The gap is contaminated by deposit-rate arbitrage: when time-deposit rates are cut aggressively (as through 2023–2025), households shift into demand deposits *for yield-indifference reasons*, flattering the gap without any improvement in animal spirits. (3) Property-sales cash flow is the dominant driver of corporate demand deposits; the gap is therefore substantially a property-transaction indicator in disguise. |

### A.5 Deposits: household vs corporate, time vs demand, and "excess savings"

| Field | Detail |
|---|---|
| English | Deposits by sector and maturity |
| Chinese | 住户存款 / 非金融企业存款; 定期存款 / 活期存款 |
| Source table | 金融机构人民币信贷收支表 (Sources & Uses of Funds of Financial Institutions, RMB) and 存款性公司概览 (Depository Corporations Survey), both under PBoC 调查统计司: https://www.pbc.gov.cn/diaochatongjisi/116219/116319/ |
| Frequency / lag | Monthly; the headline household/corporate deposit split comes with the main statistics release (~10–15 days); the fuller credit-and-deposit table lags a few weeks more |
| History | Monthly from the late 1990s |
| Key derived series | (a) **Household deposit YoY growth**; (b) **household time-deposit share of household deposits** (the termification ratio); (c) **corporate demand deposits YoY** (the clean animal-spirits proxy now that M1 is diluted); (d) **"excess savings"** = cumulative household deposit flow since a pre-shock baseline (typically end-2019) *minus* the counterfactual from the pre-2020 trend. |
| How to read | Rising household deposit growth **with** a rising time-deposit share = precautionary saving = contractionary for demand even if M2 is strong. This is the "flushed with cash, starved of demand" configuration that has characterised China since 2022. A **fall** in the time-deposit share alongside rising corporate demand deposits is the genuine easing signal. |
| Structural fact | Household deposits have accumulated far faster than corporate deposits since the pandemic — a structural imbalance that explains why high M2 growth has not produced nominal demand. |
| Caveats | **"Excess savings" is a construct, not a published series** — the answer depends entirely on the counterfactual trend chosen (linear vs log-linear, pre-2020 window length). Publish the assumption alongside the number. Also: the April 2024 手工补息 ban shifted deposits between corporate and non-bank categories and out of the banking system into WMPs, breaking the sector split for roughly four quarters. Finally, deposit *migration* into WMPs/money funds is not dissaving — do not read a household deposit slowdown as a consumption pickup without checking WMP AUM. |

### A.6 Base money (储备货币) and the money multiplier

| Field | Detail |
|---|---|
| English | Reserve money / monetary base; money multiplier |
| Chinese | 储备货币 (基础货币); 货币乘数 |
| Definition | **Base money** = currency issued (货币发行) + deposits of depository corporations at the PBoC (required + excess reserves) + (historically) deposits of non-financial institutions. It is the liability side of the **Monetary Authority Balance Sheet (货币当局资产负债表)**. **Money multiplier** = `M2 / Base money`. |
| Publisher | PBoC 调查统计司, 货币当局资产负债表 |
| Frequency / lag | Monthly, ~3–5 weeks |
| Source | https://www.pbc.gov.cn/diaochatongjisi/116219/116319/ (Monetary Authority Balance Sheet under each year's 货币统计概览) |
| History | Monthly from 1999 |
| How to read | **The multiplier is now the dominant driver of M2, not base money.** Since the FX-inflow era ended (~2014), the PBoC has expanded money mainly by *lowering the RRR* and lending via MLF/relending/repo — i.e. by raising the multiplier rather than by injecting base money. So: **rising multiplier = looser** (more M2 per unit of base money, usually because the RRR was cut or excess reserves were run down). Base money growth alone can be near zero or negative while monetary conditions ease. |
| Reference | The multiplier reached a **record ~7.15** in a recent late-July reading, versus roughly 3.8 in Dec 2008 and a 5.2 peak in May 2006 pre-crisis. `[the 7.15 figure's exact reference date is unverified — treat as "around 7, record high"]` |
| Key thresholds | A multiplier above ~7 with a weighted-average RRR near 6% means the quantity instrument is close to exhausted — remaining RRR headroom is small, which is why the PBoC has shifted toward outright reverse repos and government-bond trading to supply base money. |
| Caveats | (i) **The multiplier is an identity, not a behavioural parameter** — do not read it as "bank lending appetite". (ii) It is mechanically lifted by every RRR cut, so a rising multiplier during an RRR-cut cycle is tautological. (iii) The base-money definition changed over time as the PBoC reclassified non-financial institution deposits `[precise dates unverified]`. (iv) Month-end fiscal deposit swings distort base money badly; use 3-month averages. |
| Related balance-sheet line | **外汇占款 (Funds outstanding for foreign exchange / PBoC FX position)** — see §E.5. |

---

## B. Credit and Aggregate Financing

### B.1 Total Social Financing / Aggregate Financing to the Real Economy

| Field | Detail |
|---|---|
| English | Aggregate Financing to the Real Economy (official PBoC English) / Total Social Financing (market usage) |
| Chinese | 社会融资规模 |
| Abbrev. | AFRE / TSF; **流量 = 增量** (flow), **存量** (stock) |
| Definition | The total volume of funds the real economy (non-financial corporates, households and, since 2019, government via bonds) obtains from the financial system in a given period. Published in **two forms**: the monthly **flow** (社会融资规模增量) and the end-period **stock** (社会融资规模存量). |
| Publisher | PBoC, Survey & Statistics Department — the indicator was designed in-house (research began Nov 2010) |
| Frequency / lag | Monthly, ~10–15 days; also quarterly and by province |
| Source | PBoC 调查统计司 统计数据 (社会融资规模 tables under each year's statistics page): https://www.pbc.gov.cn/diaochatongjisi/116219/116319/ ; mirror of the increment table at MOFCOM data centre: https://data.mofcom.gov.cn/gnmy/shrzgm.shtml ; annual data reports e.g. https://cn.chinadaily.com.cn/a/201901/15/WS5c3e81bfa31010568bdc3d06.html (2018 flow) and https://cn.chinadaily.com.cn/a/201901/15/WS5c3e81bea31010568bdc3d05.html (2018 stock) |
| CEIC | https://www.ceicdata.com/en/blog/china-total-social-financing (explainer + series family) |
| History | **First quarterly national flow data published April 2011; monthly from 2012; a full monthly back-series to 2002 published September 2012.** Stock series published from 2015 onwards with history. |
| Reference levels | End-April 2026 stock: **RMB 456.89tn, +7.8% YoY**, of which RMB loans to the real economy were **60.6%** of the total. End-2025 stock growth **+8.3%** (vs M2 +8.5%). Jan 2026 stock **+8.2%**. **June 2026: +7.4% YoY — the slowest on record**, against a pre-COVID five-year average near 13%. Jan–Jul 2026 cumulative flow **RMB 22.25tn, down RMB 1.74tn YoY**. |

#### B.1.1 Components of AFRE

| Component (CN) | Component (EN) | Notes |
|---|---|---|
| 人民币贷款 | RMB loans to the real economy | Largest component (~60% of stock). **Differs from "new RMB loans"** in the money-and-banking table: AFRE excludes loans to non-bank financial institutions and includes some loans the banking table treats differently. |
| 外币贷款(折合人民币) | FX loans (RMB equivalent) | Small; driven by cross-border rate differentials and CNY expectations |
| 委托贷款 | Entrusted loans | Shadow-banking channel; heavily suppressed post-2018 |
| 信托贷款 | Trust loans | Shadow-banking channel; heavily suppressed post-2018 |
| 未贴现银行承兑汇票 | Undiscounted bankers' acceptances | Highly volatile; the classic window-dressing component |
| 企业债券 | Corporate bonds | Net financing; includes LGFV bonds |
| 政府债券 | Government bonds | **Added in stages 2018–2019 (see below)** — now a major swing factor |
| 非金融企业境内股票融资 | Domestic equity financing by non-financial enterprises | Small; IPO-policy driven |
| 存款类金融机构资产支持证券 | ABS of depository financial institutions | Added July 2018 |
| 贷款核销 | Loan write-offs | Added July 2018 |
| 其他 (含专项债、保险赔付、投资性房地产等) | Other | Residual items |

#### B.1.2 Definitional changes — the break history you must carry

| Date | Change | Effect |
|---|---|---|
| Nov 2010 – Apr 2011 | Indicator designed; first quarterly flow published Apr 2011 | Series inception |
| Sep 2012 | Monthly back-series to 2002 published | Usable history begins 2002 |
| **July 2018** | **Added "ABS of depository financial institutions" and "loan write-offs"** | Raised both stock and flow; write-offs in particular are an *accounting* addition, not new financing to the economy — a well-known criticism |
| **September 2018** | **Added "local government special bonds" (地方政府专项债券)** | Recognised that special bonds had a clear substitution effect against bank loans and corporate bonds. End-2018 special-bond balance RMB 7.27tn, +32.6% YoY; 2018 total AFRE stock RMB 200.75tn |
| **December 2019** | **Added treasury bonds (国债) and local government general bonds (地方政府一般债券)**, merged with special bonds into a single **"government bonds" (政府债券)** line | The decisive change: AFRE became a *combined* fiscal+credit aggregate. From this point, AFRE growth is no longer a pure private-credit indicator |
| 2019–2020 onward | Exchange-traded corporate ABS and other refinements | `[precise dates and scope unverified]` |

**Consequence:** any AFRE series spanning 2018–2019 has **three** upward level shifts. The PBoC publishes the revised series on a consistent basis historically, so the *published* stock is internally consistent; but **the published YoY growth rates around the change months were computed on shifting bases in real time**. Always use the latest vintage of the full history, never contemporaneous prints, for backtests.

#### B.1.3 How to read AFRE

- **Stock growth (存量同比) is the stance variable.** The PBoC's explicit intermediate-target language: AFRE and M2 growth should be "basically in line with nominal economic growth." So compute **AFRE stock growth − nominal GDP growth**. Persistently positive = leverage rising = accommodative; persistently negative = deleveraging = tight. In 2025 AFRE stock growth (8.3%) ran "notably higher" than nominal GDP growth — which the PBoC frames as supportive, but which in a deflationary economy mostly reflects the denominator collapsing.
- **Flow (增量) is the impulse variable** and feeds the credit impulse (B.4).
- **Composition is the quality read.** AFRE growth held up in 2024–2026 almost entirely on government bonds. Strip them out and the private-credit picture is far worse — see B.5.

#### B.1.4 Distortions and caveats for AFRE

1. **Government-bond dominance.** Since Dec 2019 AFRE mixes fiscal issuance with private credit. Headline AFRE can accelerate purely on a bond-issuance quota being front-loaded. Always decompose.
2. **Local-government debt swap.** The 2024–2026 hidden-debt resolution programme converts LGFV bank loans into local government bonds. This is roughly AFRE-neutral in stock but **shifts the composition from "RMB loans" to "government bonds" and depresses new-loan prints** — a pure accounting rotation that has repeatedly been misread as credit-demand collapse. This is arguably the single biggest interpretive trap in 2025–2026 Chinese credit data.
3. **Undiscounted bankers' acceptances** swing violently with bank window-dressing and with the discounting rate; they can single-handedly determine whether a monthly AFRE print beats or misses.
4. **Loan write-offs** in the stock are not financing.
5. **Seasonality is extreme** — January is 3–5x an average month. Never read a single month; use `3m annualised`, `12m rolling sum`, or `YTD cumulative vs prior-year YTD`. The PBoC itself has moved to guiding markets toward quarterly/cumulative readings and away from monthly "credit pulse chasing" (the "new normal" framing flagged in July 2026).
6. **Jan–Feb should be combined** for CNY.
7. AFRE excludes FDI, equity outside domestic listings, and offshore bond issuance — it is not total funding of the Chinese economy.

### B.2 New RMB loans (新增人民币贷款) and the loan-quality decomposition

| Field | Detail |
|---|---|
| English | New RMB loans |
| Chinese | 新增人民币贷款 |
| Publisher / freq / lag | PBoC, monthly, ~10–15 days |
| Source | PBoC Financial Statistics Report: https://www.pbc.gov.cn/en/3688247/3688978/3709137/ ; TradingEconomics mirror: https://tradingeconomics.com/china/new-bank-loans |
| History | Monthly from 1999 |
| Reference | Jan–Jul 2026 cumulative +RMB 10.38tn. **July 2026 saw an outright contraction of RMB 340bn — the second monthly contraction of 2026** (April 2026 was the first), an event essentially without precedent in the modern series. |
| **The quality decomposition** | Split new loans into: **corporate short-term**, **corporate medium-and-long-term (企业中长期贷款)**, **bill financing (票据融资)**, **household short-term (consumer)**, **household medium-and-long-term (mortgages)**. |
| How to read the decomposition | **Corporate MLT loans = genuine capex financing = the highest-quality credit signal.** **Bill financing = filler** — when banks are handed a lending target they cannot meet with real demand, they stuff the quota with discounted bills. **A month where headline new loans beat but the beat is entirely bill financing is a tightening signal, not an easing one.** **Household MLT loans = mortgages = the property-cycle read**; their collapse from 2022 is the core of China's credit-demand problem. **Household short-term** is noisy and contaminated by consumer-loan promotional pricing and by loans being recycled into mortgage prepayment. |
| Key thresholds | Bill financing exceeding ~30% of new corporate loans in a month is a reliable "quota-stuffing" flag. Negative household MLT loans (net mortgage repayment) indicates active household deleveraging. |
| Caveats | (i) Quarter-end and year-end targets produce a sawtooth: March/June/September/December are inflated and the following month is depressed. The PBoC has explicitly campaigned against 冲时点 (point-in-time inflation of loan books) since 2024, which itself **broke the seasonal pattern** and made 2024–2026 prints non-comparable to history. (ii) The debt-swap rotation (B.1.4 #2) mechanically suppresses new corporate loans. (iii) "New loans" in the money-and-banking table ≠ the "RMB loans" line inside AFRE. |

### B.3 Medium-and-long-term loans — corporate vs household

Covered in B.2 as a decomposition, but worth standing alone on a dashboard:

- **企业(事业)单位中长期贷款** — corporate MLT loans, YoY growth of the outstanding stock. Preferred transformation: **YoY % of outstanding**, not monthly flow, to strip seasonality.
- **住户中长期贷款** — household MLT loans (≈ mortgages), same transformation.
- The **ratio of corporate MLT to total new corporate loans** is a clean, seasonality-robust quality gauge.
- Source: PBoC 金融机构人民币信贷收支表 and the quarterly 金融机构贷款投向统计报告 (Loan Directional Statistics Report), PBoC 调查统计司.

### B.4 Credit impulse (信贷脉冲)

**Precise definition.** The credit impulse is the **change in the flow of new credit as a percentage of GDP** — equivalently, the **second derivative of the credit stock** (first derivative of credit-to-GDP). It measures *acceleration* of credit, which is what maps to the *level* of activity growth, whereas the *level* of credit growth maps to the *level* of the debt stock.

**Standard construction (12-month rolling, monthly frequency):**

```
Let F_t   = 12-month trailing sum of monthly AFRE flow, ending at month t
Let Y_t   = 12-month trailing sum of nominal GDP, ending at month t
            (interpolate quarterly nominal GDP to monthly, or use 4-quarter rolling GDP)

Credit-to-GDP flow ratio:   R_t  = F_t / Y_t
Credit impulse:             CI_t = ( R_t − R_{t−12} ) × 100     [percentage points of GDP]
```

Equivalently, and algebraically identical up to the GDP-denominator treatment:

```
CI_t = 100 × ( F_t − F_{t−12} ) / Y_t
```

**Variants you will encounter — state which you use:**
- **Denominator convention**: some houses divide both `F_t` and `F_{t−12}` by the *current* `Y_t` (as above, cleaner); others divide each by its contemporaneous GDP. The first is standard.
- **Credit measure**: AFRE total (broadest); **AFRE ex-government bonds** (the private-credit impulse — strongly preferred post-2019, see B.5); AFRE ex-equity; or bank loans only. Bloomberg publishes its own China Credit Impulse Index (Bloomberg Terminal; charted at https://en.macromicro.me/charts/35559/china-credit-impulse-index).
- **Smoothing**: 3-month moving average of `CI_t` is common.

**How to read it.** Positive = credit flow accelerating faster than the economy = fresh stimulus entering. Negative = stimulus being withdrawn *even if credit is still growing*. **It leads.** The empirically cited lead is roughly **6–12 months** on Chinese fixed asset investment, industrial production and PPI, and roughly **9–12 months** on the global manufacturing cycle and industrial-metals prices — China's credit impulse is one of the few genuinely global leading indicators, because Chinese credit maps to commodity-intensive construction and capex.

**Thresholds.** Sign change is the signal. Historically the amplitude has been ±5 to ±10pp of GDP at cycle extremes (2009 and 2020 spikes; 2018 and 2021–22 troughs).

**Caveats.**
1. **Post-2019 the headline AFRE impulse is largely a fiscal-issuance impulse.** Government bonds now swing it. For the private-sector transmission read, compute the impulse on **AFRE ex-government bonds**.
2. **Deflation corrupts the denominator.** With nominal GDP growth depressed by a negative deflator, the credit/GDP ratio rises mechanically and the impulse looks better than the real economy feels. Consider computing a parallel impulse against **real GDP × a stable price index**, or simply present it alongside the deflator.
3. The debt-swap rotation (B.1.4 #2) shifts the impulse between components without changing the total — another reason to decompose.
4. GDP interpolation choice matters; document it.
5. The lead relationship has weakened since ~2021 because the credit is going into debt refinancing and infrastructure with low multipliers rather than into property and new capex.

### B.5 AFRE excluding government bonds (社融剔除政府债券)

| Field | Detail |
|---|---|
| Construction | `AFRE_ex_gov_stock = AFRE stock − government bonds outstanding`; then take YoY growth. Monthly flow equivalent: `AFRE flow − government bond net financing`. All inputs are published lines in the PBoC AFRE stock and flow tables, so **this is a simple, exact subtraction from official data — not an estimate**. |
| Status | **Not published by the PBoC as a headline series**; it is a standard analyst construction from the official component table. Do not attribute the series itself to the PBoC. |
| Why it matters | Since the Dec 2019 inclusion of treasuries and general bonds, headline AFRE conflates fiscal expansion with private credit demand. Through 2024–2026 headline AFRE growth has been propped up by heavy government issuance (including the debt-swap programme) while the ex-government measure has decelerated much harder. **The gap between the two is itself the cleanest single read on "is the private sector borrowing, or is the state doing all the work?"** |
| How to read | Widening headline-minus-ex-gov gap = fiscal substitution for absent private demand = the economy is being carried, not recovering. Convergence (ex-gov growth catching up) is the genuine turn signal. |
| Related | The IMF's **"augmented" fiscal and debt aggregates** (Article IV staff reports) perform the complementary exercise from the fiscal side, consolidating LGFV activity: https://www.imf.org/en/publications/cr/issues/2026/02/17/peoples-republic-of-china-2025-article-iv-consultation-press-release-staff-report-and-574028 |

### B.6 Credit-to-GDP gap — BIS / Basel III countercyclical buffer measure

| Field | Detail |
|---|---|
| English | Credit-to-GDP gap |
| Definition | `Gap = (Credit to private non-financial sector / GDP) − long-run trend of that ratio`, where the trend is a **one-sided (real-time, backward-looking) Hodrick–Prescott filter** with smoothing parameter λ = 400,000 (quarterly). Basel III designates this as the reference guide for setting the **countercyclical capital buffer (CCyB)**. |
| Publisher | Bank for International Settlements |
| Frequency / lag | Quarterly; ~2 quarters lag |
| Source | Topic page: https://data.bis.org/topics/CREDIT_GAPS ; data: https://data.bis.org/topics/CREDIT_GAPS/data ; **China gap series key `Q.CN.P.A.C`**: https://data.bis.org/topics/CREDIT_GAPS/BIS,WS_CREDIT_GAP,1.0/Q.CN.P.A.C ; **China actual ratio `Q.CN.P.A.A`**: https://data.bis.org/topics/CREDIT_GAPS/BIS,WS_CREDIT_GAP,1.0/Q.CN.P.A.A ; dataflow `BIS,WS_CREDIT_GAP,1.0` is SDMX-accessible via the BIS Data Portal API. Overview of the underlying credit series: https://www.bis.org/statistics/totcredit.htm |
| FRED mirror | `CRDQCNAPABIS` — "Total Credit to Private Non-Financial Sector, Adjusted for Breaks, for China", **Q4 1985 –** : https://fred.stlouisfed.org/series/CRDQCNAPABIS ; BIS/China tag listing: https://fred.stlouisfed.org/tags/series?t=bis%3Bchina |
| History | Credit gaps dataset covers 44 economies, starting as early as 1961; China's credit series from **Q4 1985**. |
| Reference | China's private non-financial sector credit was **201.4% of GDP as of Q3 2025** — the highest among the major economies BIS tracks. |
| How to read | **This one is sign-inverted relative to the rest of the catalogue.** A *high positive* gap means credit has run far above trend — historically a **financial-stability warning** (Basel's calibration puts the CCyB at its maximum when the gap exceeds ~10pp). It does **not** mean "loose current policy": a large positive gap accumulated in the past is entirely consistent with a savagely tight *current* impulse. A *negative* gap means active deleveraging relative to trend. |
| Caveats | (i) **The HP filter is badly behaved for China** — after three decades of near-monotonic credit expansion, the "trend" is itself a rising line, so the gap understates the level of leverage and can even turn negative while debt/GDP is at record highs. The BIS acknowledges the one-sided-HP critique generally. (ii) BIS credit measures have **historically diverged from Chinese domestic (NIFD/CNBS) measures** on LGFV and shadow-credit treatment, though NIFD has noted convergence in BIS data toward the domestic measure. (iii) The denominator is nominal GDP — deflation inflates the ratio. (iv) Two-quarter lag makes it unusable as a timing tool; it is a structural/vulnerability gauge. |

### B.7 Macro leverage ratio (宏观杠杆率) — NIFD/CNBS and BIS

| Field | Detail |
|---|---|
| English | Macro leverage ratio (total non-financial-sector debt / nominal GDP) |
| Chinese | 宏观杠杆率 |
| Publishers | **NIFD / CNBS** (国家金融与发展实验室 / 国家资产负债表研究中心, under CASS) — the domestic authority; and **BIS** (total credit to the non-financial sector). |
| Frequency / lag | Quarterly; NIFD ~3–4 weeks after quarter-end (fast); BIS ~2 quarters |
| Source (NIFD) | https://www.nifd.cn/ — quarterly series report 《NIFD季报·宏观杠杆率》, e.g. https://www.nifd.cn/Uploads/SeriesReport/ed943d77-8f0a-46bb-9087-4d7542c0276f.pdf (Apr 2025 edition); Q2 2020 example https://www.nifd.cn/Paper/Details/2223 ; Q1 2026 press coverage https://news.10jqka.com.cn/20260421/c676158127.shtml |
| Source (BIS) | https://www.bis.org/statistics/totcredit.htm ; FRED `CRDQCNAPABIS` for the private-sector component |
| Sector split | NIFD publishes **household / non-financial corporate / government (central + local)** and the total. This split is its main advantage over BIS. |
| History | NIFD series back to the 1990s; BIS from Q4 1985 |
| Reference | NIFD: **302.3% in Q3 2024**, +1.9pp QoQ — with the increase driven by a *falling denominator* despite a historic contraction in household debt. NIFD has continued reporting rises through Q1 2026 alongside narrowing increments as nominal growth recovered. |
| How to read | **The decomposition matters more than the level.** `Δleverage = credit growth − nominal GDP growth`. In 2024–2026 China's leverage ratio has risen **passively** — not because credit accelerated but because nominal GDP decelerated (deflation). **Passive releveraging is a symptom of tight monetary conditions, not loose ones.** This is the cleanest way to explain the China paradox to a non-specialist. |
| Caveats | (i) NIFD and BIS differ on LGFV debt, shadow credit and government scope — **do not mix the two series**. (ii) Quarterly nominal GDP revisions (especially the post-economic-census revisions) shift the whole series. (iii) The ratio is a stock/flow hybrid and is dominated by the denominator in deflation. |

---

## C. Price of Money — Policy and Market Rates

### C.1 7-day reverse repo rate (OMO rate) — **the primary policy rate**

| Field | Detail |
|---|---|
| English | 7-day open-market reverse repo rate |
| Chinese | 公开市场7天期逆回购操作利率 (逆回购利率) |
| Abbrev. | 7d OMO / 7d RRP |
| Status | **Since June/July 2024, the PBoC's primary policy rate.** Governor **Pan Gongsheng** set this out at the **Lujiazui Forum on 19 June 2024**, stating that the 7-day reverse repo rate would become the main policy rate and other policy rates would gradually "soften their role"; implementation followed in **July 2024**, when the operation was switched to a **fixed-rate, quantity-tender** basis so the announced rate is unambiguous. |
| Publisher | PBoC, open market operations announcements (daily) |
| Frequency / lag | Daily operations; rate changes are discrete policy events, announced same-day, no lag |
| Source | PBoC monetary policy page: https://www.pbc.gov.cn/en/3688006/index.html ; TradingEconomics mirror: https://tradingeconomics.com/china/reverse-repo-rate |
| History | 7-day reverse repo operations since 2012–13; as *designated policy rate* only since July 2024 |
| Current level | **1.40%**, cut by 10bp in **May 2025** (the first cut since September 2024) and unchanged through 2026 to date. |
| How to read | The cleanest signal of the *intended* stance. A cut is unambiguous easing. But the level is now so low that **the marginal information content per cut is falling** — 10bp moves against a −1% deflator barely shift the real rate. Watch it jointly with the real-rate gap (C.7). |
| Typical range | 2.20% (2019) → 2.20%/2.00% (2020–22) → 1.80% (2023) → 1.70% (Jul 2024) → 1.50% (Sep 2024) → 1.40% (May 2025). Effectively a one-way ratchet down since 2019. |
| Caveats | (i) The *rate* is the policy signal; the *volume* of daily OMOs is short-term liquidity management and belongs in the colleague's liquidity note, not here. (ii) Pre-July-2024 the 7d OMO rate was a *secondary* rate — do not treat pre-2024 changes in it as equivalent policy events to post-2024 changes. (iii) Under the fixed-rate/quantity-tender regime the PBoC fully satisfies bids at the posted rate, so the rate no longer drifts with demand. |

### C.2 MLF rate — demoted

| Field | Detail |
|---|---|
| English | Medium-term Lending Facility rate |
| Chinese | 中期借贷便利(利率) |
| Abbrev. | MLF |
| Former status | From the 2019 LPR reform until 2024, the **1-year MLF rate was China's de facto medium-term policy rate** — LPR was explicitly quoted as MLF + a spread, so MLF was the anchor of the whole lending-rate structure. |
| **Demotion** | Two steps. **(1) June/July 2024:** Pan Gongsheng's Lujiazui framework announcement made the 7-day reverse repo the main policy rate and said other rates would "soften their role"; the LPR link to MLF was severed in practice (see C.3). **(2) March 2025 — the decisive step:** the PBoC changed MLF operations to **fixed-quantity, interest-rate bidding with multiple-price (multi-price) allotment**. Because winners pay their own bid, **the PBoC no longer announces a single MLF rate at all** — the facility's policy-rate attribute is formally extinguished. The first operation under the new rules was **RMB 450bn on 25 March 2025**. |
| Source | State Council announcement of the rule change: https://english.www.gov.cn/news/202503/24/content_WS67e15836c6d0868f4e8f11e9.html ; operation: https://english.www.gov.cn/news/202503/25/content_WS67e2592fc6d0868f4e8f1293.html ; analysis: https://www.centralbanking.com/central-banks/monetary-policy/operating-framework/7972581/pboc-tweaks-lending-facility-as-framework-reform-continues ; TradingEconomics legacy series https://tradingeconomics.com/china/1-year-mlf-rate |
| History | MLF created September 2014; policy-rate status ~2019–2024; rate series ends with the March 2025 change |
| How to read now | **MLF is now a quantity tool, not a price signal.** Monitor the **net MLF injection/maturity** (still announced monthly) as a medium-term base-money supply indicator, and note that the IMF reported the **annual-average MLF balance down 25% YoY (≈ RMB 1.7tn) as of November 2025**, offset by the new outright-reverse-repo and bond-trading facilities. Rising MLF outstanding = the PBoC choosing to supply term base money at a cost, which is mildly tighter than an RRR cut (which supplies it free). |
| Caveats | **Do not use the old MLF rate as a policy-rate proxy in any post-2024 model.** Many vendor databases still carry a stale "China 1-year MLF rate" line; it is no longer a policy instrument. |

### C.3 Loan Prime Rate (LPR), 1-year and 5-year+

| Field | Detail |
|---|---|
| English | Loan Prime Rate |
| Chinese | 贷款市场报价利率 |
| Abbrev. | LPR (1Y LPR, 5Y LPR) |
| Definition | A quoted rate: a panel of commercial banks submits its best rate offered to prime customers; the top and bottom quotes are trimmed and the rest arithmetically averaged, rounded to the nearest 5bp. Published in two tenors: **1-year** (benchmark for most corporate and short-term household borrowing) and **over-5-year** (benchmark for mortgages). |
| Publisher | **National Interbank Funding Center (NIFC) / CFETS** on behalf of the PBoC |
| Frequency / timing | **Monthly, 09:00 CST on the 20th** (quotes submitted before 09:00; next business day if the 20th is a holiday). Zero lag. |
| Source | https://www.chinamoney.com.cn/english/bmklpr/ ; TradingEconomics mirror https://tradingeconomics.com/china/interest-rate |
| History | **From 20 August 2019** under the reformed mechanism (a predecessor LPR existed from Oct 2013 but was effectively a mirror of the benchmark lending rate and is not comparable). |
| Panel | Reformed in Aug 2019 to **18 quoting banks** (broadened from the original 10 to include city commercial, rural commercial, foreign and private banks); subsequently 20 `[panel size change date unverified]`. |
| **2019 reform** | Made LPR the pricing reference for all new loans, replacing the PBoC benchmark lending rate (基准贷款利率), and required quotes to be **expressed as a spread over the 1-year MLF rate** — which is what elevated MLF to policy-rate status. |
| **2024 change** | With the framework reform, **LPR quotes are no longer anchored to MLF**. Banks are now expected to quote off their **actual marginal funding cost and their best customers' rates, referencing the short-term policy rate (7-day reverse repo)** as the anchor of the rate structure. In practice through 2024–2026 the LPR has moved when the 7-day OMO moved, in equal or larger increments. |
| Current levels | **1Y LPR 3.00%, 5Y LPR 3.50%** — unchanged for a **15th consecutive month as of August 2026** (last cut May 2025, alongside the 7d OMO cut to 1.40%). |
| How to read | LPR is the *administered* price of credit and moves in discrete 5–25bp steps. **Its information content is low relative to the WALR (C.6)** because actual loans are priced at large and varying spreads *below* LPR. The **5Y LPR specifically is the property-policy dial**: in 2022 and 2024 the PBoC cut 5Y by more than 1Y precisely to target mortgages, breaking the historical parallel movement. |
| Key derived series | **1Y-minus-5Y LPR spread** — narrowing = deliberate property support. |
| Caveats | (i) LPR is a *floor-ish reference*, not a transacted rate; by 2025–26 a large share of new corporate loans price **below** 1Y LPR (WALR for new corporate loans ~3.1% vs LPR 3.00% — essentially at or through it). When the transacted rate sits at or below the reference, the reference has stopped binding and LPR loses signal value entirely. (ii) The 2024 de-anchoring means **a pre-2024 LPR-minus-MLF spread series is not continuable**. (iii) Existing mortgage repricing happens on fixed annual reset dates (typically 1 January), so a 5Y LPR cut transmits to household cash flow with up to a 12-month lag — except where the PBoC has ordered bulk repricing of existing mortgages (as in 2023 and Oct 2024). |

### C.4 The interest-rate corridor: SLF ceiling, IOER floor, and the July 2024 temporary overnight facilities

| Field | Detail |
|---|---|
| **Standing Lending Facility (SLF)** | 常备借贷便利. On-demand collateralised lending to banks at a penalty rate → **corridor ceiling**. Tenors: overnight, 7-day, 1-month. Rates move with the policy rate; the overnight SLF has historically sat roughly **100bp above** the 7-day reverse repo rate. `[current SLF levels unverified in this session — check https://www.pbc.gov.cn/en/3688006/index.html]` |
| **Excess reserve rate (IOER)** | 超额存款准备金利率. Interest paid on banks' excess reserves at the PBoC → **corridor floor**. Cut to **0.35%** in April 2020 and unchanged since. `[level widely reported; not re-verified in this session]` |
| **Classic corridor width** | With SLF O/N as ceiling and IOER as floor, the corridor was **~245bp** — far too wide to anchor money-market rates, which is precisely the defect the 2024 reform addressed. |
| **July 2024 temporary facilities** | On **8 July 2024** the PBoC announced **temporary overnight repo and temporary overnight reverse repo operations** (临时正回购/临时逆回购), conducted **between 16:00 and 16:20 on working days**, i.e. *after* the main OMO window and after the interbank market's main trading session. Pricing: **temporary overnight repo (liquidity withdrawal) at the 7-day reverse repo rate − 20bp**; **temporary overnight reverse repo (liquidity injection) at the 7-day reverse repo rate + 50bp**. This creates a de facto corridor of width **70bp** around the policy rate — down from ~245bp. |
| **Possible 2026 recalibration** | Secondary sources report a subsequent adjustment to **±25bp around the 7-day reverse repo rate, narrowing the corridor from 70bp to 50bp**. `[**unverified** — the announcement date and whether this is in force could not be confirmed. Verify against PBoC announcements before using.]` |
| Source | https://finadium.com/pboc-to-add-overnight-reverse-repo-and-rmb-repo-facility/ ; https://www.yicaiglobal.com/news/pbocs-temporary-repo-reverse-repo-operations-to-help-stabilize-market-experts-say ; corridor tracker https://en.macromicro.me/collections/31/cn-finance-relative/109608/cn-interest-rate-corridor-new |
| How to read | The corridor is a **framework** indicator: a narrowing corridor signals the PBoC is committing to price-based control and to keeping DR007 pinned near the policy rate. Because the temporary facilities are *optional* and used sparingly, the effective corridor is soft. **Where DR007 sits within the corridor is a liquidity question (colleague's remit); the corridor's width and the policy-rate level are the stance questions and belong here.** |
| Caveat | Do not conflate corridor narrowing with easing. Narrowing is a *regime* improvement (better transmission), sign-neutral for the stance. |

### C.5 Deposit rate self-discipline mechanism and deposit-rate marketisation

| Field | Detail |
|---|---|
| English | Market Interest Rate Pricing Self-Disciplinary Mechanism |
| Chinese | 市场利率定价自律机制 (存款利率自律机制) |
| What it is | An industry body of Chinese financial institutions, **overseen by the PBoC**, which sets **ceilings on deposit rates** and issues binding "self-disciplinary initiatives" (自律倡议). Since the formal abolition of administered deposit-rate ceilings in 2015, this is the actual mechanism by which deposit rates are controlled — it is **a monetary policy instrument in all but name**. |
| Why it belongs in a stance catalogue | Bank net interest margins are the binding constraint on how far lending rates can fall. The PBoC has repeatedly used the self-discipline mechanism to **push deposit costs down first, creating NIM room for subsequent LPR/lending-rate cuts.** A self-discipline initiative on deposit rates is therefore a **leading indicator of a lending-rate cut**, typically by weeks to a couple of months. This is one of the highest-value, least-watched indicators in the whole catalogue. |
| Key actions to track | **April 2024** — initiative banning **手工补息** (manual supplementary interest, i.e. banks paying above-ceiling rates to large corporate depositors off-system); reported to save commercial banks **over RMB 800bn a year** in interest expense, and the proximate cause of the 2024–25 corporate deposit and M1 contraction. **December 2024 (effective 1 Dec 2024)** — two initiatives: (a) **non-bank interbank deposit rates to be benchmarked against the 7-day reverse repo rate** — a direct extension of the new policy-rate anchor into a market the PBoC previously could not reach; (b) mandatory **"interest rate adjustment floor clauses" (利率调整兜底条款)** in deposit service agreements, allowing banks to reprice existing long-dated deposits downward when policy rates fall. |
| Source | https://www.chinadaily.com.cn/a/202411/30/WS674a7d41a310f1265a1d05fb.html ; https://finance.caixin.com/2025-01-04/102275506.html ; RBA overview of the mechanism within China's framework: https://www.rba.gov.au/publications/bulletin/2024/apr/chinas-monetary-policy-framework-and-financial-market-transmission.html |
| How to read | A new deposit-rate self-discipline initiative = **looser conditions coming**, with a lag. Conversely, evidence of banks circumventing the ceilings (deposit "migration" to WMPs, structured deposits, interbank certificates) = transmission blockage. |
| Caveats | Not a published time series — it is an **event calendar**. Build it as a dated event list, not a number. The deposit-rate ceilings themselves are not officially published as a series; market estimates of the listed-bank posted rates are the usable proxy. `[no official published ceiling series]` |

### C.6 Weighted Average Lending Rate (WALR) — **the true price of credit**

| Field | Detail |
|---|---|
| English | Weighted average interest rate on loans |
| Chinese | 贷款加权平均利率 |
| Abbrev. | WALR |
| Definition | The volume-weighted average contracted interest rate on **loans newly extended during the quarter** (not the stock). Published as: **overall WALR**, **general loans (一般贷款)**, **corporate/enterprise loans (企业贷款)**, **bill financing (票据融资)**, and **personal housing loans (个人住房贷款)**. |
| Publisher | PBoC, in the quarterly **China Monetary Policy Report (货币政策执行报告)** — normally in the box/appendix on interest rates. Some series are also released in the monthly/quarterly PBoC press conferences. |
| Frequency / lag | **Quarterly**, ~5–7 weeks after quarter-end |
| Source | Monetary Policy Report index: https://www.pbc.gov.cn/en/3688229/3688353/3688356/ ; e.g. Q2 2025 report https://www.pbc.gov.cn/en/3688229/3688353/3688356/5624504/5846668/index.html and PDF mirror https://wuhan.pbc.gov.cn/en/3688229/3688353/3688356/5624504/2025120609594987919/2025091916245444294.pdf ; Q3 2025 PDF https://www.pbc.gov.cn/en/attachDir/2025/12/20251217.pdf |
| CEIC | "China Lending Rate: Weighted Average" https://www.ceicdata.com/en/china/rediscount-and-lending-rate/cn-lending-rate-weighted-average ; "…: General Loan" https://www.ceicdata.com/en/china/rediscount-and-lending-rate/cn-lending-rate-weighted-average-general-loan ; "…: General Loan: Enterprise" https://www.ceicdata.com/zh-hans/china/rediscount-and-lending-rate/cn-lending-rate-weighted-average-general-loan-enterprise ; "…: Bill Financing" https://www.ceicdata.com/en/china/rediscount-and-lending-rate/cn-lending-rate-weighted-average-bill-financing |
| MacroMicro | https://en.macromicro.me/charts/16113/cn-loan-interest-rate |
| History | Quarterly from ~2008 (earlier on some components) |
| Reference levels | **Overall WALR 3.15% in December 2025** (record low). **General loan rate 3.54% in March 2026** (record low), from 3.55% in Dec 2025. **New corporate loans ~3.1% in April 2026**, ~20bp lower YoY; **new personal housing loans 3.1% in April 2026**, 6bp lower YoY. November 2025 new corporate loans 3.1%, ~30bp lower YoY. |
| **Why this is the best single price-of-credit indicator** | It is the only series that captures **actual transacted spreads over the reference rate**, bank risk appetite, competitive pressure and credit rationing simultaneously. Policy rates and LPR tell you what the PBoC *intends*; WALR tells you what borrowers *pay*. In 2024–2026 the WALR fell faster than the LPR — evidence of intense bank competition for the shrinking pool of creditworthy borrowers ("卷"), i.e. genuine easing beyond the policy signal. Conversely, if WALR ever stops falling while LPR falls, transmission has broken. |
| Key derived series | **WALR − LPR spread** (transmission gauge); **corporate WALR − mortgage WALR** (sectoral allocation of credit); **WALR minus inflation** (the real cost of credit, C.7). |
| Caveats | (i) **Quarterly and lagged ~6 weeks** — too slow for tactical use; it is a confirmation, not a signal. (ii) It is a rate on *new* loans, so it reflects the *marginal* price, not the average cost of the outstanding stock (which falls much more slowly and is what actually determines household and corporate cash flow). (iii) **Composition bias**: the mix has shifted toward low-risk state-owned and policy-directed lending, which mechanically drags the average down without any improvement in access for private SMEs. A falling WALR can therefore coexist with *worse* credit availability for the marginal private borrower. (iv) The PBoC has at times published some sub-components irregularly or dropped them from a given quarter's report. |

### C.7 Real rates — the critical read for China

**Construction.** For any nominal rate `i` and any price index with inflation `π`:

```
Real rate (ex-post)  = i_t − π_t
Real rate (ex-ante)  = i_t − E_t[π_{t+4q}]     (survey or model expectation)
```

Compute the panel below and present **all** of them — the divergence between deflators is itself information.

| Nominal rate | Deflated by | What it measures | Notes |
|---|---|---|---|
| **WALR, general loans** | **GDP deflator** | The economy-wide real cost of borrowing | **The single best real-rate measure for China.** The GDP deflator is the only index covering the whole nominal-income base against which debt is serviced. |
| **WALR, corporate loans** | **PPI** | Real borrowing cost for the industrial/manufacturing borrower | The most punishing measure. With PPI deeply negative through 2023–2025, real industrial borrowing costs were in high single digits. |
| **1Y LPR** | **Core CPI** | Household/consumer-facing real reference rate | Core CPI hovered near zero 2023–2025 |
| **7d OMO** | **Headline CPI** | Real policy rate | The "monetary policy stance" number in cross-country comparison |
| **5Y LPR** | **GDP deflator** | Real mortgage reference rate | The property-affordability real rate |
| **10Y CGB yield** | **GDP deflator** | Long real rate / real term structure | Useful for r* comparison |

**Inflation inputs and sources.** CPI and PPI: NBS monthly, ~9th of following month (https://www.stats.gov.cn/). GDP deflator: derived as `nominal GDP growth − real GDP growth` from NBS quarterly GDP, ~15–18 days after quarter-end; also published by TradingEconomics (https://tradingeconomics.com/china/gdp-deflator) and in IMF WEO.

**Reference values.** GDP deflator **≈ −1% for full-year 2025**; IMF projects **−0.7% for 2026**. Headline CPI averaged **0% in 2025**, projected **0.9% in 2026**. The deflator **turned positive at +1.6% in Q2 2026 — the first positive print after twelve quarters of contraction** — and Q2 2026 PPI rose **+3.6% YoY**, its first positive reading since Q4 2022.

**Why the real read is far tighter than the nominal read — the arithmetic.**

With the new-corporate-loan WALR at ~3.1% and the GDP deflator at −1.0%, the **real corporate borrowing cost is ~4.1%**. Against PPI at roughly −2% to −3% in 2024–25, the real industrial borrowing cost was **5–6%**. Meanwhile estimates of China's natural rate (C.8) put r* at roughly **2% or below** and falling. So even at record-low nominal rates, the real policy-relevant rate sat **200–400bp above r*** — a materially restrictive stance. This is the arithmetic behind the IMF's conclusion that "financial conditions remain tight overall amid high real interest rates."

**The deflation doom-loop.** Because debt is nominal, a negative deflator raises the real debt burden and the real interest cost simultaneously, which suppresses borrowing, which suppresses demand, which deepens deflation. The IMF explicitly warns that a negative deflator in 2026 would be "aggravating adverse debt dynamics." **Every nominal easing measure must be assessed against whether it moves the deflator; if it does not, it is not easing.**

**Caveats.** (i) Ex-post real rates are backward-looking; use the ex-ante version with survey expectations where available, but Chinese inflation-expectation surveys are thin `[no well-established public series identified]`. (ii) The GDP deflator is quarterly and revised. (iii) PPI is the right deflator only for industrial borrowers; using it economy-wide overstates tightness. (iv) Q2 2026's positive deflator may be a base effect from anti-involution supply-side measures rather than a demand recovery — do not declare the deflation over on one print.

### C.8 Natural rate (r*) and the real-rate gap

| Field | Detail |
|---|---|
| Concept | `r*` — the real short rate consistent with output at potential and stable inflation. **Stance gauge = real policy rate − r\***: positive = restrictive, negative = accommodative. |
| Key reference | **Sun & Rees (2021), "The Natural Interest Rate in China", BIS Working Paper** — the standard reference. Summary: https://www.suerf.org/publications/suerf-policy-notes-and-briefs/the-natural-interest-rate-in-china/ |
| Findings | China's natural rate **averaged 3–5% from the late 1990s through the 2010s, then declined to around 2% by end-2019**. Somewhat more than half the decline is attributed to lower potential output growth. |
| Other work | Laubach-Williams-style and HP/bandpass estimates; see the recent literature e.g. https://www.sciencedirect.com/science/article/pii/S1059056026002637 and the NBER natural-vs-neutral distinction https://www.nber.org/system/files/working_papers/w31949/w31949.pdf |
| How to read | Given r* ≈ 2% and falling with potential growth, and a real corporate borrowing rate ~4%, the gap is **~+200bp restrictive** — consistent with the IMF assessment. **The policy implication is that nominal cuts of 10bp at a time cannot close a 200bp real gap while the deflator is negative; only a regime shift in nominal demand (fiscal, or a credible reflation commitment) closes it.** |
| Caveats | r* is unobservable, model-dependent, and estimates for China are wide and infrequently updated. **No official PBoC r* estimate exists.** Use it as a framing device and a rough calibration, never as a precise threshold. Treat any single point estimate as ±100bp at best. |

---

## D. Reserve Requirements and the Quantity Instrument

### D.1 Reserve Requirement Ratio (RRR)

| Field | Detail |
|---|---|
| English | Reserve requirement ratio / required reserve ratio |
| Chinese | 存款准备金率 |
| Abbrev. | RRR |
| Structure | **Tiered**: large national banks; medium-sized/joint-stock banks; small and rural institutions (county-level rural credit cooperatives and village banks sit at a statutory floor, reported as **5%**, which the PBoC has said it will not go below `[floor statement unverified]`). The PBoC also publishes a **weighted average RRR (加权平均存款准备金率)** which is the headline stance number. |
| Publisher | PBoC — announcements under 货币政策/存款准备金: https://www.pbc.gov.cn/en/3688229/3688335/3730270/index.html (Required Reserves page); example announcement https://www.pbc.gov.cn/en/3688229/3688335/3730270/5701513/index.html |
| Frequency | Event-driven (discrete announcements), usually announced days-to-weeks before the effective date |
| Data mirrors | CEIC https://www.ceicdata.com/en/indicator/china/reserve-requirement-ratio and https://www.ceicdata.com/en/china/required-reserve-ratio ; MacroMicro https://en.macromicro.me/charts/262/cn-required-deposit-reserve-ratio ; TradingEconomics https://tradingeconomics.com/china/cash-reserve-ratio |
| History | From 1985; actively used as a stabilisation tool from 2007. Peak large-bank RRR **21.5%** (2011), since cut roughly two dozen times. |
| Recent actions | **May 2025**: cut **50bp**, the first of 2025, releasing about **RMB 1tn** of long-term liquidity (alongside the 7d OMO cut to 1.40%). **A further 50bp cut effective 6 September** `[year ambiguous in retrieved sources — most likely 2025; verify]`. **January 2026**: PBoC signalled further RRR and rate cuts to come; Pan Gongsheng: "There is still room for further RRR and interest rate cuts this year." |
| Current levels | **Weighted average RRR 6.2%** as reported for 11 December 2025 (CEIC). **Large banks 7.50%** as reported for February 2026 (CEIC/TradingEconomics). `[These two vendor readings imply substantial cuts after mid-2025; cross-check against the PBoC Required Reserves page before publishing a current level.]` |
| **Liquidity released per cut — rule of thumb** | A **50bp cut across the board releases roughly RMB 1.0–1.2tn** of long-term liquidity at current deposit base; **25bp ≈ RMB 500–600bn**. The PBoC states the figure in each announcement — **always use the stated figure rather than the rule of thumb**, because targeted cuts (excluding certain institution types) release materially less. |
| How to read | **A cut is unambiguous easing** and is the cheapest form of it: it replaces costly MLF/repo funding with free permanent reserves, directly widening bank NIMs and enabling lending-rate cuts. **The signalling content usually exceeds the mechanical liquidity content** — an RRR cut is the PBoC's loudest "we are easing" megaphone, which is exactly why it is deployed around Politburo meetings and data disappointments. |
| Key thresholds | With the weighted average around 6% and a statutory-ish floor near 5% for the smallest institutions, **remaining RRR headroom is limited — of the order of 100–150bp of weighted-average cuts**. This is *the* structural reason the PBoC built the outright reverse repo and government-bond-trading tools in late 2024: it is running out of RRR. Track "remaining RRR headroom" as a policy-space indicator. |
| Caveats | (i) The **weighted average** is the only cross-time-comparable number; the "large bank" headline misses targeted cuts. (ii) An RRR cut that merely offsets maturing MLF is **liquidity-neutral and stance-neutral** — always net it against the MLF/outright-repo maturity schedule. (iii) Announcement date ≠ effective date (typically 10–20 days apart); date your event study on the announcement. (iv) The FX-deposit RRR (E.6) is a completely separate instrument aimed at the currency — **do not confuse the two**. |

### D.2 Structural and targeted tools (结构性货币政策工具)

These are **quantity instruments with a subsidised price**, aimed at directing credit to policy-favoured sectors. Collectively they are the PBoC's answer to "we cannot cut rates much further, so we will cut them selectively."

| Tool | Chinese | Introduced | Mechanism / terms | Notes |
|---|---|---|---|---|
| **Relending / re-discount** | 再贷款 / 再贴现 | Long-standing | PBoC lends to banks at a below-market relending rate against qualifying loan books; quotas set per programme | The base of the whole structural family. Quotas and balances published in the quarterly Monetary Policy Report appendix |
| **PSL — Pledged Supplementary Lending** | 抵押补充贷款 | 2014 | Long-tenor PBoC lending to the three policy banks (CDB, ADBC, EximBank) against pledged assets; funded shantytown redevelopment 2015–18 and urban village renovation/affordable housing more recently | **The classic "quasi-QE"/quasi-fiscal indicator.** A PSL balance expansion is a strong easing signal because it funds construction directly. Monthly balance published by the PBoC. **A resumption of large net PSL is one of the highest-signal events on this entire list.** |
| **Carbon emission reduction facility** | 碳减排支持工具 | Nov 2021 | Relending against qualifying green loans at a concessional rate; extended multiple times | Green-directed credit |
| **Sci-tech innovation and technological transformation relending** | 科技创新和技术改造再贷款 | 2024 | Relending supporting tech-innovation and equipment-upgrade lending | A 2024 priority; merged/expanded from earlier tech relending |
| **Affordable housing relending** | 保障性住房再贷款 | 2024 | Funds local SOEs purchasing completed unsold housing for conversion to affordable housing | **Take-up has been persistently far below quota** — a key indicator that the transmission blockage is demand-side, not supply-side |
| **SFISF — Securities, Funds and Insurance companies Swap Facility** | 证券、基金、保险公司互换便利 | **Oct 2024** | Eligible **non-bank** financial institutions swap holdings of bonds, ETFs and CSI 300 constituents for **high-liquidity assets (government bonds, PBoC bills)**; proceeds must be used for equity/ETF investment or market-making | **A structural break: the PBoC extending liquidity support to non-banks for the express purpose of supporting the equity market.** Conducted twice by end-Jan 2025: **RMB 50bn (Oct 2024)** and **RMB 55bn (Jan 2025)**; headline programme capacity discussed up to **RMB 1.5tn** in aggregate `[the 1.5tn ceiling is an indicative/expandable figure, not a committed quota]` |
| **Share buyback and shareholding-increase relending** | 股票回购增持再贷款 | **Oct 2024** | PBoC relending to banks to fund listed companies' and major shareholders' share buybacks and stake increases. Scale **RMB 300bn** | Same category of innovation as SFISF — monetary policy aimed at asset prices |
| **Service consumption and elderly care relending** | 服务消费与养老再贷款 | 2025 | Consumption-directed relending | Part of the 2025 pivot toward consumption |
| Rate cuts on structural tools | — | **January 2026** | PBoC cut the rates on targeted/structural monetary tools | http://english.scio.gov.cn/pressroom/2026-01/16/content_118283341.html |

**Source for balances and quotas:** the **structural monetary policy tools table (结构性货币政策工具情况表)** published in the appendix of each quarterly China Monetary Policy Report — https://www.pbc.gov.cn/en/3688229/3688353/3688356/ . Also: https://www.pbc.gov.cn/en/3688110/3688172/5552468/2025092319411497296/index.html (Pan Gongsheng NPC press conference).

**How to read the structural block.**
- **Aggregate outstanding balance of all structural tools** is the headline. Rising = targeted easing; the IMF noted that **structural relending balances have generally declined since 2023**, i.e. this channel has been *shrinking*, not expanding — a quietly contractionary fact that headline rate cuts obscure.
- **Take-up versus quota** is the transmission gauge. Persistent under-use (affordable housing relending being the canonical example) is evidence that the constraint is borrower demand, not lender funding — which is the single most important diagnostic in the current Chinese cycle.
- **Caveats:** quotas are announced with fanfare and drawn down slowly or never; a quota announcement is a *signal*, a balance increase is *actual easing*. Programmes are frequently merged, renamed and re-based, breaking continuity of the balance series.

### D.3 Other quantity instruments now carrying the base-money load

| Tool | Chinese | Since | Role |
|---|---|---|---|
| **Outright reverse repo** | 买断式逆回购 | **Oct 2024** | Monthly, tenor **≤1 year** (3M and 6M used in practice), fixed-quantity multiple-price tender against treasury/local-government collateral, ownership transferred outright. Now a **major** medium-term base-money channel replacing MLF. Recent operations: RMB 1.0tn (Sep 2025, Dec 2025), RMB 1.1tn (Sep 2025 and Jan 2026 rollovers), RMB 500bn 6-month (Aug 2025), RMB 400bn (Jun 2025). Sources: https://english.www.gov.cn/news/202601/07/content_WS695e55b5c6d00ca5f9a0878c.html , https://english.www.gov.cn/news/202509/30/content_WS68dbdafbc6d00ca5f9a0690b.html , https://en.people.cn/n3/2025/0815/c90000-20353404.html ; TradingEconomics series https://tradingeconomics.com/china/outright-reverse-repo |
| **Government bond trading** | 国债买卖 | **Aug 2024** | Outright purchases/sales of CGBs in the secondary market — China's closest analogue to conventional balance-sheet policy. **Suspended in January 2025** (announced 10 Jan 2025) citing "persistent excess demand" for bonds after yields hit record lows — in practice a yield-curve/currency-defence decision. **Subsequently resumed**, announced by Governor Pan Gongsheng; the IMF notes **net purchases under the bond trading programmes** partly offsetting the MLF runoff as of late 2025. Sources: https://www.centralbanking.com/central-banks/currency/7963600/pboc-suspends-government-bond-purchases ; http://english.scio.gov.cn/m/pressroom/2025-01/15/content_117666228.html ; https://tradingeconomics.com/china/government-bond-yield/news/496556 |

**Why these matter for the stance:** they are how the PBoC now supplies base money as the RRR approaches its floor. **The monthly net of (outright reverse repo + MLF + bond purchases + PSL − maturities) is the true "balance sheet impulse"** and is a better medium-term quantity gauge than any single instrument. A month of heavy net injection through these channels is easing even with no rate change.

---

## E. Exchange Rate Channel

### E.1 CNY/USD spot (onshore CNY and offshore CNH)

| Field | Detail |
|---|---|
| Chinese | 人民币兑美元即期汇率 |
| Publisher | CFETS (onshore CNY, 09:30–23:00 CST band); offshore CNH trades freely in HK/global markets |
| Source | https://www.chinamoney.com.cn/english/ |
| Trading band | Onshore CNY may move **±2%** around the daily fixing (widened to ±2% in March 2014) |
| How to read | A **weaker CNY is looser** monetary conditions (it eases via net exports and imported-price reflation) — but in China the causality usually runs the other way: the currency is *managed*, so CNY weakness typically reflects the PBoC *permitting* easing rather than causing it. **CNH–CNY spread** is the depreciation-pressure gauge: CNH weaker than CNY = offshore selling pressure the PBoC is resisting onshore. |
| Caveats | Because the currency is managed, spot moves understate the underlying pressure. Read spot jointly with the fixing bias (E.3) and the CNH basis. |

### E.2 CFETS RMB Index (trade-weighted) and the BIS/SDR baskets

| Field | Detail |
|---|---|
| English | CFETS RMB Exchange Rate Index |
| Chinese | CFETS人民币汇率指数 |
| Publisher | **China Foreign Exchange Trade System (CFETS)** — launched December 2015 |
| Methodology | **Geometric mean** of the RMB's bilateral rates against basket currencies; weights are **international trade weights adjusted for re-export (entrepôt) trade**; the currency value input is the **daily CNY central parity rate (中间价)**. **Base date 31 December 2014 = 100.** Weights recalibrated periodically (announced 31 December for the following year). |
| Basket | **25 currencies as of 1 January 2025**, with **USD 18.903%, EUR 17.902%, JPY 8.584%, KRW 8.368%**. The 2025 recalibration reduced KRW (−0.68pp), USD (−0.56pp) and JPY (−0.38pp), and raised HKD (+0.49pp), AUD (+0.47pp) and RUB (+0.30pp). |
| Companion indices | CFETS also publishes an **RMB index against the BIS currency basket** and an **RMB index against the SDR basket**, adjusting each to the official BIS/SDR baskets. The RMB's **SDR weight was raised from 10.92% to 12.28% effective 1 August 2022**. |
| Frequency | Weekly (Friday) plus month-end; daily values available |
| Source | Index releases: https://www.chinamoney.com.cn/english/bmkidxrud/ (e.g. Dec 2025: https://www.chinamoney.com.cn/english/bmkidxrud/20260105/3260816.html ); basket rule announcements: https://www.chinamoney.com.cn/english/svcnrl/20161229/2049.html and https://www.chinamoney.com.cn/english/svcnrl/20191231/1496901.html ; CEIC https://www.ceicdata.com/en/china/exchange-rate-index/cn-rmb-exchange-rate-index-cfets-currency-basket and BIS-basket version https://www.ceicdata.com/en/china/exchange-rate-index/cn-rmb-exchange-rate-index-bis-currency-basket ; explainer: https://www.conference-board.org/publications/CFETS-Basket-and-RMB-Valuation |
| History | From **31 December 2014** (base) / published from December 2015 |
| How to read | **The CFETS index is the PBoC's own stated objective variable** — "keeping the RMB basically stable at a reasonable and balanced level" is operationalised against the basket, not against USD. **A falling CFETS index = looser** (trade-weighted depreciation = stimulus). Critically, CNY can weaken sharply against USD while the CFETS index is *flat* (if USD is broadly strong) — in which case there has been **no easing at all** through the FX channel. Anyone reading China's FX stance off USD/CNY alone will be systematically wrong. |
| Typical range | Roughly 90–108 since inception; ~100 is the psychologically important round number the PBoC has historically defended. |
| Caveats | (i) Built off the **fixing**, not market spot — so it embeds the PBoC's own guidance and is partly an instrument, not an observation. (ii) Weight recalibrations each January create small discontinuities. (iii) The index is nominal — for the competitiveness read use the REER (E.4). |

### E.3 Daily fixing (中间价) and the counter-cyclical factor

| Field | Detail |
|---|---|
| English | Central parity rate / daily fixing; counter-cyclical factor |
| Chinese | 人民币汇率中间价; 逆周期因子 |
| Mechanism | Each morning ~09:15 CST, market makers submit quotes based on **the previous day's close plus overnight moves in a basket of currencies**; CFETS trims and averages. The PBoC may apply a **counter-cyclical factor** — a discretionary adjustment — to lean against what it deems excessive or herd-driven moves. |
| History | Counter-cyclical factor **introduced 26 May 2017**; suspended January 2018; **reinstated August 2018**; use has been intermittent and is **never officially quantified**. |
| Source | https://www.chinamoney.com.cn/english/ ; https://www.yicaiglobal.com/news/pboc-takes-aim-at-yuan-depreciation-by-restoring-counter-cyclical-factor ; https://www.business-standard.com/amp/article/reuters/china-resumes-use-of-counter-cyclical-factor-in-yuan-midpoint-fixing-mechanism-sources-118082400688_1.html ; academic: https://www.sciencedirect.com/science/article/abs/pii/S1042443125000344 and https://www.sciencedirect.com/science/article/abs/pii/S1043951X26000386 |
| **The key derived indicator: fix-vs-model deviation** | Construct a **"fixing bias"** = `actual fixing − a model fixing`, where the model fixing replicates the published formula (previous close + basket-implied overnight move). The residual is the counter-cyclical factor plus noise. Convention: compute in **pips** and take a 5- or 20-day moving average. A persistent residual on the **strong side** of the model = PBoC resisting depreciation = **de facto tightening** of monetary conditions. A persistent residual on the **weak side** = PBoC resisting appreciation = **de facto easing**. Many banks (Reuters and major sell-side FX desks) publish a daily "fixing vs consensus estimate" which is a ready-made version of this. |
| Current regime | Through most of 2015–2024 the factor was used to **push back against depreciation**. **Toward the end of 2025 this reversed: the PBoC began using fixings to push back — cautiously — against *appreciation*.** This is a significant regime change: it means the FX channel flipped from a constraint on easing to a (mild) source of tightening pressure the PBoC is actively trying to offset. |
| Caveats | The counter-cyclical factor's parameters are **not published**; every estimate of it is a residual from a model of the fixing formula and is therefore noisy. The PBoC neither confirms nor denies its use in any given period. Treat the fixing bias as a directional signal, never a precise measurement. |

### E.4 Real Effective Exchange Rate (REER)

| Field | Detail |
|---|---|
| English | Real effective exchange rate (broad) |
| Chinese | 实际有效汇率 |
| Definition | **NEER adjusted for relative consumer prices.** NEER is a **geometric trade-weighted average of bilateral exchange rates**; weights derive from **manufacturing trade flows, double-weighted** to capture both direct bilateral trade and third-market competition. BIS deflates with CPI. |
| Publisher | **BIS** (the standard); also IMF (INS database) and Bruegel |
| Coverage | **Broad indices: 64 economies. Narrow: 26 (nominal) / 27 (real).** Use **broad** for China. |
| Frequency / lag | Monthly, ~2–6 weeks |
| Source | BIS overview: https://www.bis.org/statistics/eer.htm ; methodology paper: https://www.bis.org/publ/qtrpdf/r_qt0603e.pdf ; **FRED `RBCNBIS`** — "Real Broad Effective Exchange Rate for China": https://fred.stlouisfed.org/series/RBCNBIS ; vintages https://alfred.stlouisfed.org/series?seid=RBCNBIS ; CEIC https://www.ceicdata.com/en/china/bank-for-international-settlements-bis-effective-exchange-rate-index/cn-effective-exchange-rate-index-bis-nominal |
| History | **Monthly from January 1994** (through at least June 2026 on FRED) |
| How to read | **A falling REER = looser monetary conditions.** For China specifically, the REER carries extra weight because **deflation means the REER falls more slowly than the NEER, or even rises while the NEER falls** — China's domestic prices falling relative to trading partners' should *depreciate* the real rate, which is a genuine (if painful) easing/competitiveness channel. Track **REER minus NEER** to isolate the relative-price contribution. |
| **The critical China-specific caveat** | In 2023–2026, China's REER depreciation has been substantially *deflation-driven* rather than nominal-depreciation-driven. This is the "internal devaluation" channel: it improves external competitiveness (and indeed export volumes have held up remarkably) **while simultaneously tightening domestic monetary conditions** via the real interest rate. **The REER can therefore signal "looser" at exactly the moment domestic conditions are tightest.** Never read the REER as a stance indicator in isolation for China — it must be paired with the real rate, which is why the MCI (F.1) combines them. |
| Other caveats | (i) CPI-deflated REER understates China's competitiveness gain because Chinese export prices have fallen far more than CPI — a PPI- or unit-labour-cost-deflated REER tells a more dramatic story `[BIS does not publish a ULC-deflated REER for China]`. (ii) BIS revises weights every three years, creating small chained discontinuities. (iii) Broad vs narrow baskets give visibly different levels — state which you use. |

### E.5 FX reserves and the PBoC's FX position (外汇占款)

| Field | Detail |
|---|---|
| **FX reserves** | 外汇储备. Published monthly by **SAFE**, ~7th of the following month. https://www.safe.gov.cn/ . Headline level ~USD 3.2tn for years. **Low signal value**: dominated by valuation effects (USD index moves and bond mark-to-market), which routinely swamp actual flow. **Always compute valuation-adjusted flow** before drawing any inference. |
| **外汇占款 — Funds outstanding for foreign exchange** | The PBoC's domestic-currency claims arising from FX purchases, i.e. the **FX asset line on the Monetary Authority Balance Sheet (货币当局资产负债表)**. This is the true measure of **PBoC intervention that creates or destroys base money.** Monthly, ~3–5 weeks lag. Source: https://www.pbc.gov.cn/diaochatongjisi/116219/116319/ |
| How to read 外汇占款 | Rising = PBoC buying FX = **injecting base money** = looser (this was the dominant money-creation channel 2001–2014). Falling = PBoC selling FX = draining base money = tighter. Since 2015 the line has been broadly flat, confirming the PBoC has largely stepped back from *direct* intervention. |
| **The backdoor-intervention caveat** | Since ~2015 much intervention has been conducted **through the large state banks' own FX books and forward positions rather than through the PBoC balance sheet** — so a flat 外汇占款 line does **not** mean no intervention. Cross-check with (a) the **SAFE data on banks' FX settlement and sales (结售汇)**, (b) state banks' net foreign asset positions, and (c) the PBoC's **forward book / other foreign assets**. See the Council on Foreign Relations work on this: https://www.cfr.org/articles/the-pboc-the-state-banks-and-backdoor-intervention |

### E.6 FX macroprudential instruments

| Instrument | Chinese | Mechanism | History |
|---|---|---|---|
| **FX risk reserve requirement on forward FX sales** | 远期售汇业务外汇风险准备金率 | Banks must deposit a percentage of the **previous month's forward FX sale contract volume** with the PBoC, **frozen for one year, interest-free**. Raising it makes hedging depreciation expensive → **supports the CNY**. Lowering it → **permits depreciation / slows appreciation**. | **20%** from 15 Oct 2015 → **0%** Oct 2020 → **20%** effective 28 Sep 2022 → **0% effective 2 March 2026** (announced 27 Feb 2026, the first change in nearly three and a half years, **explicitly to slow the RMB's rapid appreciation**) |
| **FX deposit reserve ratio** | 外汇存款准备金率 | RRR applied to banks' **foreign-currency deposits**. Raising it locks up USD onshore → supports CNY. Cutting it releases USD → permits depreciation. | Raised to **7%** (15 Jun 2021), **9%** (15 Dec 2021); cut to **8%** (15 May 2022), **6%** (15 Sep 2022). Further cuts reported subsequently `[post-2022 levels unverified]` |
| Sources | https://english.www.gov.cn/statecouncil/ministries/202209/26/content_WS63313f45c6d0a757729e0870.html ; http://english.scio.gov.cn/pressroom/2026-02/27/content_118349478.html ; https://news.cgtn.com/news/2026-02-27/China-scraps-risk-reserve-ratio-for-forward-forex-sales-1L6lKHNHDyg/p.html ; https://www.yicaiglobal.com/news/chinas-scrapping-forward-forex-risk-reserve-ratio-aims-to-slow-yuans-rapid-appreciation-analysts-say ; https://www.centralbanking.com/central-banks/reserves/7975446/pboc-reserve-ratio-cut-spurs-short-term-fx-hedging ; https://english.www.gov.cn/statecouncil/ministries/202106/01/content_WS60b589b0c6d0df57f98da813.html | | |
| **How to read both** | These are **event indicators, not time series to average.** A change is a loud, deliberate policy signal about the desired direction of the currency. **The Feb 2026 cut to 0% is particularly informative: it is the PBoC leaning against RMB *strength*, confirming the regime flip identified in E.3 and implying the FX channel has become a tightening force the PBoC now has to offset.** Other instruments in this family include the **cross-border macroprudential adjustment parameter (跨境融资宏观审慎调节参数)** and administrative guidance on outbound flows `[current parameter value unverified]`. |

---

## F. Composite Measures

### F.1 Monetary Conditions Index (MCI) for China

**Standard construction.** An MCI is a linear combination of a **real short-term interest rate** and the **real effective exchange rate**, each expressed as a deviation from a base period, with weights reflecting their relative effect on aggregate demand:

```
MCI_t = w_r × (r_t − r_base) + w_e × (reer_t − reer_base)
```

with `w_r + w_e` typically normalised to 1 and the weights estimated from an aggregate-demand or inflation equation. Conventional ratio for small open economies is roughly **3:1** interest rate to exchange rate.

**China-specific: the credit-augmented MCI.** The reference study is the **HKMA (2005) working paper, "A monetary conditions index for Mainland China"** — https://www.hkma.gov.hk/media/eng/publication-and-research/quarterly-bulletin/qb200506/fa1.pdf (also https://ideas.repec.org/p/hkg/wpaper/0501.html ). Its key contribution is that, **because bank credit is a dominant transmission channel in China, the conventional two-variable MCI is inadequate and must be extended with a quantity/credit-availability variable.** The paper's estimated MCI implied that a particular episode's tightening was equivalent to a **rise in real interest rates of about 4.6 percentage points** — an illustration of how much of Chinese monetary tightening operates through quantity rather than price.

**Recommended China MCI for a modern dashboard (author's construction — label it as such):**

```
MCI_China = −0.5 × z(real WALR general loans, deflated by GDP deflator)
            −0.2 × z(BIS broad REER)
            +0.3 × z(credit impulse, AFRE ex-government bonds, % of GDP)
```
with all terms as z-scores over a rolling 10-year window, **positive = looser**. Weights are indicative and should be re-estimated against nominal GDP growth or the output gap before production use. **The credit term is essential for China; a two-variable MCI will mislead.**

**Who publishes an MCI for China:** no major official or widely-used commercial MCI for China is in continuous public publication. The HKMA paper is academic and historical. **In practice, market participants use financial conditions indices (F.2) instead.** `[no live, publicly available China MCI identified]`

### F.2 Financial Conditions Indices for China

| Index | Publisher | Methodology | Availability |
|---|---|---|---|
| **GS China Financial Conditions Index (GS China-FCI)** | Goldman Sachs Global Investment Research | The GS FCI family uses a **dynamic macroeconomic model to derive weights** on **five inputs: a policy/short rate, a long-term riskless bond yield, a corporate credit spread, an equity-valuation measure, and a trade-weighted exchange rate.** The China index was introduced by **Kim Sun-Bae et al.** — catalogue record: https://www.econbiz.de/Record/introducing-the-goldman-sachs-china-financial-conditions-index-gs-china-fci-kim-sun-bae/10002570976 . Calibration illustration: a 100bp hawkish Fed surprise tightens the GS FCI in China by roughly 70bp. | **Bloomberg Terminal / GS Marquee (`GSCNFCI`-family tickers `[exact ticker unverified]`); clients only.** The most widely cited China FCI in markets. |
| **Bloomberg China Credit Impulse Index** | Bloomberg | Credit impulse as % of GDP (see B.4) | Bloomberg Terminal; charted publicly at https://en.macromicro.me/charts/35559/china-credit-impulse-index . Bloomberg also runs a **China Credit Tracker**: https://www.bloomberg.com/graphics/china-credit-tracker/ |
| **IIF China financial conditions / debt monitor** | Institute of International Finance | Global Debt Monitor and country FCI work | https://www.iif.com/ — members only `[China-specific FCI methodology unverified]` |
| **NIFD / CASS China Financial Conditions Index (中国金融条件指数)** | 国家金融与发展实验室 (NIFD), CASS | Domestic Chinese FCI published in NIFD's series reports alongside the macro leverage ratio | https://www.nifd.cn/ `[**methodology and current publication status unverified** — I was unable to confirm from retrieved sources that NIFD publishes a continuously updated FCI under this name. Verify before citing.]` |
| **Tsinghua PBCSF indices** | 清华大学五道口金融学院 | Various financial-conditions and financial-cycle indices | https://www.pbcsf.tsinghua.edu.cn/ `[**unverified** — no specific index, methodology or publication series confirmed from retrieved sources]` |
| **Academic Chinese FCIs** | Various | PCA/dynamic-factor constructions over interest rates, credit, equity, property and FX | e.g. https://www.sciencedirect.com/science/article/pii/S1877050914004190/pdf ; ADB regional work https://www.adb.org/sites/default/files/publication/30163/economics-wp333-financial-conditions-indexes.pdf ; ECB WP 1743 https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp1743.en.pdf |
| **Conceptual references** | BIS / Fed | BIS Bulletin 80 on monetary policy and financial conditions https://www.bis.org/publ/bisbull80.pdf ; Fed's new US FCI-G note (a good template for a China analogue) https://www.federalreserve.gov/econres/notes/feds-notes/a-new-index-to-measure-us-financial-conditions-20230630.html |

**How to read any FCI for China — the health warning.** Standard FCIs are **equity- and spread-heavy**, which makes them a poor guide to the *real-economy* stance in China because: (a) the A-share market is retail-driven and policy-supported (see SFISF and buyback relending in D.2 — the PBoC now directly targets equity prices, so an FCI containing equities becomes partly circular); (b) Chinese credit spreads are compressed by implicit guarantees and do not price risk; (c) FX enters as a level, which as shown in E.4 can mislead in deflation. **A China FCI can print "easy" while the real-rate and credit-impulse measures print "tight" — and the latter are right about the real economy.** Prefer a purpose-built MCI (F.1) over an off-the-shelf FCI for stance work; use the FCI for market/asset-price questions.

---

## G. Recommended Shortlist — 12 Headline Indicators

Ranked by signal value for a monetary-conditions monitoring dashboard. **Sign convention: `+` = LOOSER unless stated.**

| # | Indicator | Preferred transformation | Sign | One-line rationale |
|---|---|---|---|---|
| **1** | **Real WALR on general loans** (贷款加权平均利率 − GDP deflator) | **Level, in %, plus gap to r\* (~2%)** | **− = looser** (a *fall* in the real rate is easing) | The single best measure of the true, transacted, inflation-adjusted price of credit — and the one that shows China is restrictive while every nominal rate says the opposite. |
| **2** | **Credit impulse on AFRE ex-government bonds** | **12m rolling flow / 12m nominal GDP, 12m change, in pp of GDP; 3m MA** | **+ = looser** | The cleanest leading indicator of private-sector activity, 6–12 months ahead, with the fiscal distortion stripped out. |
| **3** | **AFRE stock growth minus nominal GDP growth** | **YoY % minus YoY %, in pp** | **+ = looser** | The PBoC's own stated intermediate target, expressed as the stance variable it actually implies. |
| **4** | **7-day reverse repo rate (OMO)** | **Level, %; plus cumulative change over 12m** | **− = looser** | The primary policy rate since July 2024 — the unambiguous statement of intent; everything else is transmission. |
| **5** | **Corporate medium-and-long-term loans** | **YoY % of outstanding stock** (not monthly flow) | **+ = looser** | The highest-quality credit series: real capex financing, immune to bill-financing quota-stuffing and to seasonality. |
| **6** | **GDP deflator** | **YoY %, quarterly, level** | **+ = looser** (reflation loosens real conditions) | The denominator that turns every nominal easing measure into real tightening; the variable that must turn for the stance to actually change. |
| **7** | **Weighted-average RRR** | **Level, %; plus "remaining headroom to ~5% floor"** | **− = looser** | The loudest easing signal the PBoC has, and its dwindling headroom is a hard constraint on the quantity channel. |
| **8** | **New M1 growth, and corporate demand deposits YoY separately** | **YoY %; plus M1−M2 gap in pp, z-scored on post-Jan-2024 data only** | **+ = looser** | Transaction-money momentum — the animal-spirits read; keep corporate demand deposits separate because the 2025 redefinition diluted M1's cyclical signal. |
| **9** | **BIS broad REER for China** | **z-score of level, 5y window; plus REER−NEER to isolate the price effect** | **− = looser** (depreciation is easing) | The external channel, and the only place where China's deflation is visibly doing something helpful. |
| **10** | **PBoC balance-sheet impulse**: net (outright reverse repo + MLF + bond purchases + PSL − maturities) | **3m rolling net injection, RMB tn** | **+ = looser** | With the RRR near its floor, this is where base-money supply now actually happens; more informative than any single instrument. |
| **11** | **Household time-deposit share of household deposits** (termification) | **Level %, plus 12m change** | **− = looser** (a *falling* time share is easing) | The behavioural read on whether easy money is circulating or being hoarded — the difference between the nominal and effective stance. |
| **12** | **Fixing bias vs model fixing** (counter-cyclical factor residual) | **20-day MA, in pips** | **weak-side bias = looser** | The only high-frequency read on whether the PBoC is permitting or resisting the FX channel — now flipped to resisting *appreciation*, a 2025–26 regime change. |

**On the bench (add if you have the bandwidth):** structural-tool aggregate outstanding balance and take-up-vs-quota (the transmission diagnostic); WALR−LPR spread (transmission gauge); 5Y-minus-1Y LPR spread (property dial); deposit-rate self-discipline initiative event log (leads lending-rate cuts); NIFD macro leverage ratio decomposed into credit-growth vs nominal-GDP contributions (shows passive releveraging); bill financing share of new corporate loans (quota-stuffing flag).

**Composite suggestion:** run the shortlist as a **z-score heatmap with the sign convention applied** so every cell reads "+ = looser", plus the three-term MCI in F.1 as a single headline line. Resist the urge to average all twelve into one number — the *divergence* between the nominal block (4, 7, 10) and the real block (1, 2, 6, 11) is the actual finding.

---

## H. Master list of distortions, breaks and traps

1. **The Jan 2025 M1 redefinition** — level roughly doubles; new-basis history only from Jan 2024; the scissors gap's mean and amplitude both changed. Never splice levels.
2. **The 2018–2019 AFRE definitional additions** (ABS + write-offs Jul 2018; local special bonds Sep 2018; treasuries + general bonds Dec 2019) — three level shifts, and the Dec 2019 change converted AFRE from a credit aggregate into a credit-plus-fiscal aggregate.
3. **The local-government debt swap (2024–2026)** — rotates credit from "RMB loans" into "government bonds" with no change in total financing. **The commonest misreading in current China macro.**
4. **The April 2024 手工补息 ban** — a regulatory action that shrank corporate deposits, M1 and M2 for roughly a year and was widely misread as monetary tightening or demand collapse.
5. **The anti-冲时点 campaign (2024–)** — the PBoC's suppression of quarter-end loan-book inflation broke the decades-old seasonal pattern in new loans, making 2024+ prints non-comparable to history.
6. **The July 2024 policy-rate switch** — pre-2024 MLF-rate changes and post-2024 OMO-rate changes are **not** comparable policy events. Any reaction-function estimated across the break is misspecified.
7. **The March 2025 MLF tender change** — there is no longer a single announced MLF rate. Vendor databases carrying a stale "1-year MLF rate" line are showing a dead instrument.
8. **The 2024 LPR de-anchoring** — the LPR-minus-MLF spread series ends in 2024 and cannot be continued.
9. **Deflation in denominators** — nominal GDP in the denominator of credit/GDP, leverage, and credit impulse is depressed by the negative deflator, mechanically flattering every credit ratio while the real economy tightens.
10. **Chinese New Year** — always combine January and February for M0, loans, AFRE and deposits.
11. **Fiscal-deposit timing** — government deposits sit outside M2; bond-issuance surges drain M2 until spent.
12. **WMP/deposit migration** — money moving between deposits and wealth-management products changes M2 without changing monetary conditions.
13. **Backdoor FX intervention** — a flat 外汇占款 line does not mean no intervention; state banks' books carry it.
14. **Equity-heavy FCIs are partly circular in China** now that the PBoC directly funds buybacks and non-bank equity purchases (SFISF, buyback relending).
15. **Quota announcements ≠ easing.** Only drawn balances are easing. Affordable-housing relending is the standing example of a large quota with minimal take-up.
16. **Structural-tool balances have been *shrinking* since 2023** (per IMF) even as headline rates fell — a contractionary fact hidden behind easing headlines.
17. **Vendor level disagreements** — CEIC's reported weighted-average RRR (6.2%, Dec 2025) and large-bank RRR (7.50%, Feb 2026) should be reconciled against the PBoC's own Required Reserves page before being published as current levels.
18. **The corridor width question** — the July 2024 temporary facilities implied a 70bp corridor (−20bp/+50bp); a reported subsequent move to ±25bp (50bp corridor) is **unverified**.

---

## Sources

**Primary — PBoC**
- PBoC Survey & Statistics Department, statistics portal (货币统计概览, money supply, monetary authority balance sheet, credit-and-deposit tables, AFRE tables): https://www.pbc.gov.cn/diaochatongjisi/116219/116319/ — 2025: https://www.pbc.gov.cn/diaochatongjisi/116219/116319/5570903/5570886/index.html — 2024: https://www.pbc.gov.cn/diaochatongjisi/116219/116319/5225358/5225360/index.html
- PBoC Financial Statistics Reports (English, monthly): https://www.pbc.gov.cn/en/3688247/3688978/3709137/ — e.g. Nov 2025 https://www.pbc.gov.cn/en/3688247/3688978/3709137/2025122410193371772/index.html ; H1 2025 https://www.pbc.gov.cn/en/3688247/3688978/3709137/2025080817512797346/index.html ; Q1–Q3 2025 https://www.pbc.gov.cn/en/3688247/3688978/3709137/5870352/index.html
- PBoC China Monetary Policy Report (货币政策执行报告) index: https://www.pbc.gov.cn/en/3688229/3688353/3688356/ — Q2 2025 https://www.pbc.gov.cn/en/3688229/3688353/3688356/5624504/5846668/index.html (PDF: https://wuhan.pbc.gov.cn/en/3688229/3688353/3688356/5624504/2025120609594987919/2025091916245444294.pdf) — Q3 2025 PDF https://www.pbc.gov.cn/en/attachDir/2025/12/20251217.pdf
- PBoC, "Steady Progress in Monetary Policy Framework Transformation Bolsters High-Quality Development" (interview with the head of the Monetary Policy Department): https://www.pbc.gov.cn/en/3688006/5876310/5877235/index.html
- PBoC Required Reserves page: https://www.pbc.gov.cn/en/3688229/3688335/3730270/index.html ; RRR cut announcement example: https://www.pbc.gov.cn/en/3688229/3688335/3730270/5701513/index.html
- PBoC Monetary Policy Committee meetings: https://www.pbc.gov.cn/en/3688229/3688311/3688329/index.html — Q4 2024 meeting https://www.pbc.gov.cn/en/3688229/3688311/3688329/2025080817522520537/index.html
- Governor Pan Gongsheng, NPC press conference: https://www.pbc.gov.cn/en/3688110/3688172/5552468/2025092319411497296/index.html
- PBoC main monetary policy page: https://www.pbc.gov.cn/en/3688006/index.html ; FX policy page: https://www.pbc.gov.cn/en/3688006/3689169/3753763/index.html

**Primary — other official**
- NBS, statistical indicator note on money supply compilation and publication (documents the "within 15 days of month-end" standard): https://www.stats.gov.cn/zs/tjws/zytjzbqs/hbgyl/202410/t20241025_1957180.html
- CFETS / ChinaMoney LPR page: https://www.chinamoney.com.cn/english/bmklpr/
- CFETS RMB Index releases: https://www.chinamoney.com.cn/english/bmkidxrud/ — Dec 2025 https://www.chinamoney.com.cn/english/bmkidxrud/20260105/3260816.html — Nov 2025 https://www.chinamoney.com.cn/english/bmkidxrud/20251201/3241786.html — Sep 2025 https://www.chinamoney.com.cn/english/bmkidxrud/20251009/3205477.html
- CFETS basket rule announcements: https://www.chinamoney.com.cn/english/svcnrl/20161229/2049.html ; https://www.chinamoney.com.cn/english/svcnrl/20191231/1496901.html
- MOFCOM data centre mirror of the AFRE increment table: https://data.mofcom.gov.cn/gnmy/shrzgm.shtml
- State Council / gov.cn: MLF rule change https://english.www.gov.cn/news/202503/24/content_WS67e15836c6d0868f4e8f11e9.html ; MLF operation https://english.www.gov.cn/news/202503/25/content_WS67e2592fc6d0868f4e8f1293.html ; outright reverse repo operations https://english.www.gov.cn/news/202601/07/content_WS695e55b5c6d00ca5f9a0878c.html , https://english.www.gov.cn/news/202509/30/content_WS68dbdafbc6d00ca5f9a0690b.html , https://english.www.gov.cn/news/202509/05/content_WS68ba20cbc6d0868f4e8f558c.html , https://english.www.gov.cn/news/202506/13/content_WS684c1551c6d0868f4e8f351f.html ; FX forward reserve raise 2022 https://english.www.gov.cn/statecouncil/ministries/202209/26/content_WS63313f45c6d0a757729e0870.html ; FX deposit RRR raise 2021 https://english.www.gov.cn/statecouncil/ministries/202106/01/content_WS60b589b0c6d0df57f98da813.html ; RRR/rate-cut signalling 2026 https://english.www.gov.cn/news/202601/22/content_WS69720cd8c6d00ca5f9a08b8c.html ; loan data Jan–Jul 2026 https://english.www.gov.cn/archive/statistics/202608/14/content_WS6a7f162dc6d00ca5f9a0c9d2.html ; LPR unchanged https://english.www.gov.cn/archive/statistics/202605/20/content_WS6a0d5ceec6d00ca5f9a0b1f1.html
- SCIO: FX risk reserve scrapped 2026 http://english.scio.gov.cn/pressroom/2026-02/27/content_118349478.html ; bond-buying suspension explanation http://english.scio.gov.cn/m/pressroom/2025-01/15/content_117666228.html ; structural tool rate cuts Jan 2026 http://english.scio.gov.cn/pressroom/2026-01/16/content_118283341.html

**International institutions**
- BIS, Credit-to-GDP gaps: https://data.bis.org/topics/CREDIT_GAPS ; data https://data.bis.org/topics/CREDIT_GAPS/data ; China gap `Q.CN.P.A.C` https://data.bis.org/topics/CREDIT_GAPS/BIS,WS_CREDIT_GAP,1.0/Q.CN.P.A.C ; China ratio `Q.CN.P.A.A` https://data.bis.org/topics/CREDIT_GAPS/BIS,WS_CREDIT_GAP,1.0/Q.CN.P.A.A ; tables/dashboards https://data.bis.org/topics/CREDIT_GAPS/tables-and-dashboards
- BIS, Credit to the non-financial sector: https://www.bis.org/statistics/totcredit.htm
- BIS, Effective exchange rates: https://www.bis.org/statistics/eer.htm ; methodology https://www.bis.org/publ/qtrpdf/r_qt0603e.pdf
- BIS, Pan Gongsheng, "The evolution of financial structure and the modernization of financial markets in China": https://www.bis.org/review/r260622q.htm
- BIS Bulletin 80, Monetary policy and financial conditions: https://www.bis.org/publ/bisbull80.pdf
- Sun & Rees, "The Natural Interest Rate in China" (summary): https://www.suerf.org/publications/suerf-policy-notes-and-briefs/the-natural-interest-rate-in-china/
- IMF, 2025 Article IV Consultation with China (Board concluded 13 Feb 2026): https://www.imf.org/en/news/articles/2026/02/18/pr-26053-china-imf-executive-board-concludes-2025-article-iv-consultation ; staff report https://www.imf.org/en/publications/cr/issues/2026/02/17/peoples-republic-of-china-2025-article-iv-consultation-press-release-staff-report-and-574028 ; PDF https://www.imf.org/-/media/files/publications/cr/2026/english/1chnea2026001-source-pdf.pdf ; eLibrary https://www.elibrary.imf.org/view/journals/002/2026/044/article-A001-en.xml
- IMF, People's Republic of China: Selected Issues (2021, LPR/framework background): https://www.imf.org/-/media/files/publications/cr/2021/english/1chnea2021002.pdf
- IMF, RMB SDR basket: https://www.imf.org/en/News/Articles/2016/09/30/AM16-PR16440-IMF-Launches-New-SDR-Basket-Including-Chinese-Renminbi

**FRED / data vendors**
- FRED `MYAGM2CNM189N` M2 for China: https://fred.stlouisfed.org/series/MYAGM2CNM189N (ALFRED vintages https://alfred.stlouisfed.org/series?seid=MYAGM2CNM189N)
- FRED `MYAGM1CNM189N` M1 for China: https://fred.stlouisfed.org/series/MYAGM1CNM189N
- FRED `MANMM101CNM189S` M1 for China (OECD MEI): https://fred.stlouisfed.org/series/MANMM101CNM189S
- FRED `RBCNBIS` Real Broad Effective Exchange Rate for China: https://fred.stlouisfed.org/series/RBCNBIS (vintages https://alfred.stlouisfed.org/series?seid=RBCNBIS)
- FRED `CRDQCNAPABIS` Total Credit to Private Non-Financial Sector, China: https://fred.stlouisfed.org/series/CRDQCNAPABIS ; BIS-China tag listing https://fred.stlouisfed.org/tags/series?t=bis%3Bchina
- CEIC: Total Social Financing explainer https://www.ceicdata.com/en/blog/china-total-social-financing ; WALR https://www.ceicdata.com/en/china/rediscount-and-lending-rate/cn-lending-rate-weighted-average ; WALR general loan https://www.ceicdata.com/en/china/rediscount-and-lending-rate/cn-lending-rate-weighted-average-general-loan ; WALR general loan enterprise https://www.ceicdata.com/zh-hans/china/rediscount-and-lending-rate/cn-lending-rate-weighted-average-general-loan-enterprise ; WALR bill financing https://www.ceicdata.com/en/china/rediscount-and-lending-rate/cn-lending-rate-weighted-average-bill-financing ; RRR https://www.ceicdata.com/en/indicator/china/reserve-requirement-ratio and https://www.ceicdata.com/en/china/required-reserve-ratio ; CFETS index https://www.ceicdata.com/en/china/exchange-rate-index/cn-rmb-exchange-rate-index-cfets-currency-basket ; BIS-basket RMB index https://www.ceicdata.com/en/china/exchange-rate-index/cn-rmb-exchange-rate-index-bis-currency-basket ; BIS NEER https://www.ceicdata.com/en/china/bank-for-international-settlements-bis-effective-exchange-rate-index/cn-effective-exchange-rate-index-bis-nominal
- MacroMicro: interest-rate corridor https://en.macromicro.me/collections/31/cn-finance-relative/109608/cn-interest-rate-corridor-new ; RRR https://en.macromicro.me/charts/262/cn-required-deposit-reserve-ratio ; WALR https://en.macromicro.me/charts/16113/cn-loan-interest-rate ; Bloomberg China Credit Impulse Index https://en.macromicro.me/charts/35559/china-credit-impulse-index ; TSF https://en.macromicro.me/charts/8685/cn-total-social-financing ; PBoC policy timeline https://en.macromicro.me/time_line?id=9
- TradingEconomics: LPR/interest rate https://tradingeconomics.com/china/interest-rate ; reverse repo rate https://tradingeconomics.com/china/reverse-repo-rate ; 1-year MLF (legacy) https://tradingeconomics.com/china/1-year-mlf-rate ; cash reserve ratio https://tradingeconomics.com/china/cash-reserve-ratio ; new bank loans https://tradingeconomics.com/china/new-bank-loans ; TSF https://tradingeconomics.com/china/total-social-financing ; outright reverse repo https://tradingeconomics.com/china/outright-reverse-repo ; GDP deflator https://tradingeconomics.com/china/gdp-deflator
- TrendForce DataTrack, M1–M2 scissors gap: https://datatrack.trendforce.com/Chart/content/2928/china-money-supply-m1-m2 ; M1 https://datatrack.trendforce.com/Chart/content/782/china-money-supply-m1
- Bloomberg China Credit Tracker: https://www.bloomberg.com/graphics/china-credit-tracker/

**Research, commentary and event reporting**
- HKMA (2005), "A monetary conditions index for Mainland China": https://www.hkma.gov.hk/media/eng/publication-and-research/quarterly-bulletin/qb200506/fa1.pdf ; RePEc https://ideas.repec.org/p/hkg/wpaper/0501.html
- RBA Bulletin (Apr 2024), "China's Monetary Policy Framework and Financial Market Transmission": https://www.rba.gov.au/publications/bulletin/2024/apr/chinas-monetary-policy-framework-and-financial-market-transmission.html
- RBA SMP (Nov 2019) Box A, "Recent Reforms to Lending Rates in China": https://www.rba.gov.au/publications/smp/2019/nov/box-a-recent-reforms-to-lending-rates-in-china.html
- BBVA Research (Jul 2025), "Stocktaking China's new toolkit in its monetary policy framework": https://www.bbvaresearch.com/wp-content/uploads/2025/07/202507-Stocktaking-China-new-toolkit-in-its-monetary-policy-framework.pdf
- ING THINK, "What to expect from China's monetary policy framework reforms": https://think.ing.com/articles/what-to-expect-from-chinas-coming-monetary-policy-framework-reform/ ; CNY outlooks https://think.ing.com/articles/cny-at-a-glance-chinas-yuan-moves-into-our-bullish-scenario/ and https://think.ing.com/articles/cny-at-a-glance-tightening-our-forecast-band-for-2h26/
- Central Banking: MLF tweak https://www.centralbanking.com/central-banks/monetary-policy/operating-framework/7972581/pboc-tweaks-lending-facility-as-framework-reform-continues ; bond-purchase suspension https://www.centralbanking.com/central-banks/currency/7963600/pboc-suspends-government-bond-purchases ; rate and RRR cuts https://www.centralbanking.com/central-banks/monetary-policy/7972834/pboc-cuts-rates-and-lowers-reserve-requirement-ratios ; FX reserve-ratio cut https://www.centralbanking.com/central-banks/reserves/7975446/pboc-reserve-ratio-cut-spurs-short-term-fx-hedging ; all-tools pledge https://www.centralbanking.com/central-banks/monetary-policy/7972296/china-to-make-use-of-all-monetary-tools-to-boost-growth
- Finadium on the July 2024 temporary overnight facilities: https://finadium.com/pboc-to-add-overnight-reverse-repo-and-rmb-repo-facility/
- Yicai Global: temporary repo/reverse repo https://www.yicaiglobal.com/news/pbocs-temporary-repo-reverse-repo-operations-to-help-stabilize-market-experts-say ; counter-cyclical factor https://www.yicaiglobal.com/news/pboc-takes-aim-at-yuan-depreciation-by-restoring-counter-cyclical-factor ; FX risk reserve to zero https://www.yicaiglobal.com/news/chinas-scrapping-forward-forex-risk-reserve-ratio-aims-to-slow-yuans-rapid-appreciation-analysts-say ; LPR at record lows https://www.yicaiglobal.com/news/china-holds-key-lending-rates-steady-at-record-lows-watches-stimulus-impact ; direct financing and TSF https://www.yicaiglobal.com/news/direct-financing-fuels-chinas-social-financing-growth-despite-weak-household-demand
- China Daily: M1 broadening https://www.chinadaily.com.cn/a/202412/02/WS674db6cda310f1265a1d0a4e.html ; deposit rates from Dec 1 https://www.chinadaily.com.cn/a/202411/30/WS674a7d41a310f1265a1d05fb.html ; AFRE and M2 growth https://www.chinadaily.com.cn/a/202511/13/WS6915c262a310d6866eb295b1.html ; outright reverse repo https://global.chinadaily.com.cn/a/202601/08/WS695f13bca310d6866eb32a03.html ; M1–M2 scissors gap background http://www.chinadaily.com.cn/m/drc/2017-04/05/content_28798465.htm ; 2018 AFRE flow report https://cn.chinadaily.com.cn/a/201901/15/WS5c3e81bfa31010568bdc3d06.html ; 2018 AFRE stock report https://cn.chinadaily.com.cn/a/201901/15/WS5c3e81bea31010568bdc3d05.html
- Xinhua: FX risk reserve scrapped https://english.news.cn/20260227/b8d675262ced409fbfc1347273f76202/c.html ; LPR unchanged https://english.news.cn/20260420/9f960bcc869b4a12b6e519f3deaab095/c.html ; outright reverse repo https://english.news.cn/20260107/7fec73917f1a40b993760a3f0ab768ae/c.html ; AFRE Q1 2026 http://www.news.cn/20260414/df9a1b3cb6bf46e597ceae07d42e0dc9/c.html ; FX risk reserve (Chinese) https://www.news.cn/money/20260228/74fadefbcb9142ebbd61b3cbdd056224/c.html
- CGTN, FX risk reserve scrapped: https://news.cgtn.com/news/2026-02-27/China-scraps-risk-reserve-ratio-for-forward-forex-sales-1L6lKHNHDyg/p.html
- Caixin: macro leverage ratio Q3 2024 https://www.caixinglobal.com/2025-10-29/chinas-macro-leverage-ratio-climbs-despite-household-deleveraging-102376995.html ; credit growth and PBoC "new normal" https://www.caixinglobal.com/2026-07-16/china-credit-growth-misses-forecasts-as-pboc-flags-new-normal-102464812.html ; rate self-discipline mechanism https://finance.caixin.com/2025-01-04/102275506.html
- NIFD quarterly macro leverage ratio reports: https://www.nifd.cn/ — https://www.nifd.cn/Paper/Details/2223 ; https://www.nifd.cn/Uploads/SeriesReport/ed943d77-8f0a-46bb-9087-4d7542c0276f.pdf ; https://www.nifd.cn/Uploads/SeriesReport/93995818-31dc-40c5-b9a7-df114b7b6224.pdf ; Q1 2026 coverage https://news.10jqka.com.cn/20260421/c676158127.shtml
- CEIBS / Sheng Songcheng on AFRE design and government bonds: https://cn.ceibs.edu/new-papers-columns/17283 ; https://cliif.ceibs.edu/article/19961 ; https://cliif.ceibs.edu/article/19671
- Wuhan municipal financial bureau summary of the Nov 2020 AFRE caliber refinement: https://jrj.wuhan.gov.cn/ynzx_57/xwzx/202011/t20201119_1506720.shtml
- Shanghai municipal financial committee, 2024 AFRE stock report: https://jrj.sh.gov.cn/SCGK194/20250115/36eace10c61a457aa2b7d9836445faa9.html
- Reuters via Business Standard, counter-cyclical factor resumption 2018: https://www.business-standard.com/amp/article/reuters/china-resumes-use-of-counter-cyclical-factor-in-yuan-midpoint-fixing-mechanism-sources-118082400688_1.html
- CNBC: 2019 LPR reform https://www.cnbc.com/2019/08/20/china-economy-pboc-reforms-loan-prime-rate-bank-lending-rates.html ; bond-buying halt https://www.cnbc.com/2025/01/10/why-chinas-central-bank-has-stopped-bond-purchases.html ; LPR holds 2026 https://www.cnbc.com/2026/04/20/china-keeps-benchmark-lending-rates-unchanged-as-economic-growth-revs-up-amid-mounting-middle-east-risk-mount-.html and https://www.cnbc.com/2026/02/24/china-central-bank-pboc-loan-prime-rates-yuan-strength-growth-slows.html
- Investing.com / Reuters, July 2026 loan contraction: https://www.investing.com/news/economy-news/china-july-bank-loans-contract-for-second-time-in-2026-on-weak-demand-4860112
- Global Times, RRR cut May 2025: https://www.globaltimes.cn/page/202505/1334184.shtml
- US-China Economic and Security Review Commission, China Bulletin (23 Jul 2026) on record-low TSF growth: https://www.uscc.gov/trade-bulletins/china-bulletin-july-23-2026
- Rhodium Group on credit dynamics: https://rhg.com/research/magical-credit-machine/ ; https://rhg.com/research/chinas-financial-and-fiscal-decay/
- Council on Foreign Relations, PBoC/state-bank backdoor intervention: https://www.cfr.org/articles/the-pboc-the-state-banks-and-backdoor-intervention
- BOFIT Weekly on Chinese price pressures: https://www.bofit.fi/en/monitoring/weekly/2026/vw202608_2/
- OCBC FX Note on CFETS calibration (Jan 2025 weights): https://www.ocbc.com/iwov-resources/sg/ocbc/gbc/pdf/FX%20Outlook/DFO/FX%20Note%20-%20CFETS%20Calibration%203%20Jan%202025.pdf
- US Treasury FX Report (June 2025): https://home.treasury.gov/system/files/136/June-2025-FX-Report.pdf
- Conference Board, CFETS basket and RMB valuation: https://www.conference-board.org/publications/CFETS-Basket-and-RMB-Valuation
- Goldman Sachs China FCI catalogue record (Kim Sun-Bae et al.): https://www.econbiz.de/Record/introducing-the-goldman-sachs-china-financial-conditions-index-gs-china-fci-kim-sun-bae/10002570976
- Federal Reserve FEDS Note, "A New Index to Measure U.S. Financial Conditions": https://www.federalreserve.gov/econres/notes/feds-notes/a-new-index-to-measure-us-financial-conditions-20230630.html
- ECB WP 1743, Measuring financial conditions: https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp1743.en.pdf
- ADB WP 333, Financial Conditions Indexes for Asian Economies: https://www.adb.org/sites/default/files/publication/30163/economics-wp333-financial-conditions-indexes.pdf
- Academic: natural rate for China https://www.sciencedirect.com/science/article/pii/S1059056026002637 ; NBER natural vs neutral rates https://www.nber.org/system/files/working_papers/w31949/w31949.pdf ; counter-cyclical factor effects https://www.sciencedirect.com/science/article/abs/pii/S1042443125000344 and https://www.sciencedirect.com/science/article/abs/pii/S1043951X26000386 ; China monetary policy through deflation https://www.sciencedirect.com/science/article/pii/S0264999326001574
- Pekingnology / Miao Yanliang on the origins of China's low inflation: https://www.pekingnology.com/p/miao-yanliang-how-did-chinas-low ; https://www.eastisread.com/p/miao-yanliang-explains-chinas-large

---

*Prepared for the China Monetary & Liquidity Conditions project. Short-term interbank liquidity indicators are deliberately excluded — see the companion liquidity note. Items marked `[unverified]` require confirmation against the primary source before publication.*
