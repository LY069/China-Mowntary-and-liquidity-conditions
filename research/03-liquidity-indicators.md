# China Liquidity Conditions — Definitive Indicator Catalogue

**Scope.** Short-horizon availability and price of settlement balances and funding in the Chinese banking system and money markets: interbank and exchange repo, unsecured interbank lending, bank wholesale funding (NCD), central-bank liquidity supply, autonomous liquidity factors, and market/financial liquidity. Medium-term *monetary and credit conditions* (TSF, M2, LPR, loan pricing, credit impulse) are **out of scope** — covered separately by a colleague.

**Date of compilation:** 12 September 2026. **Author:** rates & money-market strategy.

**Verification convention used throughout:**
- Facts with a URL in `## Sources` were obtained from that source.
- `⚠️ unverified` = plausible/practitioner-standard but **not** confirmed against a primary source in this research pass. Do not quote externally without checking.
- Threshold bands labelled *"judgemental"* are strategist calibration, not official policy numbers.

**Research-access caveat.** Direct page fetches to `pbc.gov.cn`, `chinamoney.com.cn`, `chinabond.com.cn`, `bis.org`, `rba.gov.au`, `arxiv.org` and most vendor sites were blocked by this environment's network egress proxy. All primary URLs below were surfaced and cross-checked via search, and the URLs are correct entry points, but the underlying pages were **not** rendered in this session. Anyone productionising this catalogue should open each source URL once to confirm the exact table/series layout before wiring a scraper.

---

## 0. The framework: how Chinese liquidity actually works

Chinese money-market liquidity is the interaction of **four** blocks. Getting the mental model right matters more than any single series.

### 0.1 The banking-system reserve identity

Excess reserves (超额准备金, the actual settlement balances banks hold at the PBoC) are the ultimate scarce commodity. Their change decomposes as:

```
Δ Excess reserves
  = Δ PBoC lending to banks        (OMO reverse repo + MLF + outright reverse repo
                                    + SLF + PSL + structural relending tools)
  + Δ PBoC net bond purchases      (国债买卖, since Aug 2024)
  + Δ FX position (外汇占款)
  + Δ Treasury cash deposits placed at commercial banks (国库现金定存)
  − Δ Currency in circulation (M0)
  − Δ Government deposits at the PBoC (财政存款)
  − Δ Required reserves            (deposit growth × RRR, less any RRR cut)
  ± other (bond issuance settlement timing, etc.)
```

Everything in **Group C** is the PBoC's discretionary supply; everything in **Group D** is the autonomous factor set the PBoC must forecast and offset. **Group A** is the *price* that clears the resulting balance; **Group B** is how that price propagates into bank term funding.

### 0.2 The policy-rate architecture (post-2024 reform)

| Layer | Instrument | Rate (latest confirmed) | Role |
|---|---|---|---|
| **Policy rate** | 7-day OMO reverse repo (逆回购) | **1.40%** (cut from 1.50% eff. 8 May 2025) | *The* policy rate since the 2024 reform |
| **Corridor ceiling (formal)** | 7-day SLF (常备借贷便利) | 2.40% (O/N 2.25%, 1M 2.75%) after May 2025 cut | OMO + 100bp; rarely binding |
| **Corridor ceiling (de facto)** | Temporary overnight **reverse repo** | 7d OMO **+25bp** since 17 Jun 2026 (was +50bp from Jul 2024) | Narrow de facto ceiling |
| **Corridor floor (de facto)** | Temporary overnight **repo** (drain) | 7d OMO **−25bp** since 17 Jun 2026 (was −20bp from Jul 2024) | Narrow de facto floor |
| **New O/N OMO** | Overnight reverse repo OMO | Debut 29 Jun 2026, **1.25%** (rate not officially published) | Direct lever on the O/N segment |
| **Quantity tool, 1Y** | MLF (中期借贷便利) | **No published rate** since Mar 2025 (multi-price tender) | Pure quantity tool now |
| **Quantity tool, 3–6M** | Outright reverse repo (买断式逆回购) | Multi-price tender, rate unpublished | Fills the 1M–1Y gap |

The **corridor was narrowed from 70bp to 50bp on 17 June 2026** at the Lujiazui Forum — the single most important structural change for anyone calibrating "normal" ranges on DR007. Any threshold band estimated on pre-June-2026 data is now too wide.

### 0.3 Why the 2024–26 reforms changed the indicator set

1. **MLF stopped being a price signal.** From the 25 March 2025 operation the MLF moved to *fixed-quantity, variable-rate, multiple-price* tendering and the PBoC stopped publishing a winning rate. The "1Y NCD minus 1Y MLF" spread — for a decade the canonical bank-liability-pressure gauge — **no longer has a live denominator**. It must be re-based (see B.3).
2. **The PBoC gained a 3–6M quantity tool** (outright reverse repo, Oct 2024) and a **bond-buying tool** (Aug 2024). Net-injection accounting that only nets OMO + MLF is now badly incomplete.
3. **The PBoC gained a direct O/N lever** (June 2026). Since overnight repo is **>80% of money-market turnover**, this materially compresses the tail of the DR001/R001 distribution.
4. Because the MLF rate is gone and the corridor is narrower, **the DR007 – 7d OMO spread has become an even purer, and a lower-variance, signal.** Sensitivity thresholds must tighten accordingly.

---

## A. Money-market rates — the core

### A.1 DR007 — the single most important number

| Field | Detail |
|---|---|
| **English** | Depository-institutions 7-day pledged repo weighted-average rate |
| **Chinese** | 存款类金融机构间利率债质押式回购加权平均利率（7天），简称 DR007 |
| **Definition** | Volume-weighted average rate on 7-day **pledged** repo transactions in the interbank market where **both counterparties are deposit-taking institutions** and the collateral is **interest-rate bonds only** (CGBs, policy-bank bonds, PBoC bills). The "D" is the depository-institution restriction; the interest-rate-bond collateral restriction is what strips out credit-quality noise. |
| **Publisher** | CFETS / National Interbank Funding Center (中国外汇交易中心暨全国银行间同业拆借中心) |
| **Frequency** | Daily (business days); intraday weighted averages also disseminated |
| **Release lag** | Same day, post-close (exact publication time ⚠️ unverified) |
| **Source** | ChinaMoney fixing/repo pages: https://www.chinamoney.com.cn/chinese/bkfrr/ (CN) and https://iftp.chinamoney.com.cn/english/bmkfrr/ (EN). PBoC concept page: https://www.pbc.gov.cn/en/3688006/3689169/3753752/index.html |
| **Series IDs** | CEIC: "Interbank Bond Collateral Repo Rate: Weighted Avg: Depository Institution: (DR007) 7 Day" — https://www.ceicdata.com/en/china/national-interbank-funding-centre-nibfc-interbank-offered-rate-daily/cn-interbank-bond-collateral-repo-rate-weighted-avg-depository-institution-dr007-7-day · MacroMicro series 5899 — https://en.macromicro.me/series/5899/cn-dr007 · Wind: `DR007.IB` ⚠️ unverified |
| **History start** | **15 December 2014** (first official publication by CFETS) |
| **Typical range (2025–26)** | Anchored close to the 1.40% 7d OMO rate; DR007 ≈ **1.37%** on 5 Aug 2026 |

**Why the PBoC prefers it.** Three properties, in order of importance: (i) **collateralised** — so it prices liquidity, not credit; (ii) **bank-only counterparties** — so it is not contaminated by non-bank counterparty risk premia or by NBFI balance-sheet stress; (iii) **interest-rate-bond collateral only** — so collateral-quality repricing does not leak into the rate. The result is the cleanest available read on *settlement-balance scarcity in the banking system*. Governor-level PBoC communication has repeatedly framed DR as the benchmark-cultivation target, and the PBoC's own definitional page says DR007 "lower[s] the credit risks of counterparties and mitigate[s] the disturbance of collateral quality on the pricing of interest rates, better reflect[s] the situation of banking liquidity."

**How to read it — the DR007 – 7d OMO spread is THE gauge.**

| DR007 − 7d OMO | Read (judgemental, recalibrated for the 50bp corridor) |
|---|---|
| **< −10bp** | Very loose / excess reserves abundant; PBoC likely draining or about to; often precedes bond-market froth warnings |
| **−10 to +10bp** | **Normal.** Policy transmission working; PBoC comfortable |
| **+10 to +30bp** | **Watch.** Funding tightening — check tax month, bond supply, quarter-end |
| **+30 to +50bp** | **Stress.** Approaching the temporary O/N reverse repo ceiling; expect PBoC offset |
| **> +50bp sustained** | **Acute.** Ceiling breached in substance; historically resolved by RRR cut, large outright RR, or MLF over-rollover |

**Caveats.**
- DR007 is a *weighted average over the whole day and the whole market*. A benign average can hide a violent afternoon tail. Always pair with the intraday max and the R007 gap (A.5, A.8).
- 7-day repo done on a Thursday spans the weekend differently from a Monday trade; the tenor is calendar-7d, so the day-of-week composition shifts the average modestly.
- Month-end, quarter-end and pre-holiday prints are mechanically elevated and **should be excluded or dummied** before estimating a "normal" band.
- Since the Jun-2026 corridor narrowing and the O/N OMO, realised DR007 volatility is structurally lower. Do **not** reuse 2019–2024 z-score parameters.

### A.2 DR001

Same construction, overnight tenor. `DR001` — 存款类机构隔夜质押式回购加权利率. Same publisher/source/history (15 Dec 2014). DR001 carries the bulk of turnover and is the rate the new O/N OMO targets directly.

- **Read:** DR001 − 7d OMO is noisier than DR007 but faster. A DR001 that sits persistently *above* DR007 is an inverted funding curve — a classic acute-squeeze tell.
- **Threshold (judgemental):** DR001 > DR007 for 3+ consecutive sessions = stress flag. DR001 spiking above the temporary O/N reverse repo rate (OMO+25bp = 1.65% at a 1.40% OMO) = the de facto ceiling is not holding.

### A.3 R007 / R001 — all-market pledged repo

| Field | Detail |
|---|---|
| **English** | Interbank pledged repo weighted-average rate, all institutions, 7-day / overnight |
| **Chinese** | 银行间质押式回购加权平均利率（7天 / 隔夜），R007 / R001 |
| **Definition** | Volume-weighted average across **all** interbank repo participants — banks **plus** securities firms, fund managers, insurers, wealth-management subsidiaries, trusts — and **all** collateral types, including credit bonds. |
| **Publisher** | CFETS / NIFC |
| **Frequency / lag** | Daily, same-day |
| **Source** | https://www.chinamoney.com.cn/chinese/bkfrr/ ; CEIC NIFC daily repo family |
| **History** | Longer than DR (interbank repo rates published from the mid-2000s; exact start ⚠️ unverified) |
| **Series** | Wind `R007.IB`, `R001.IB` ⚠️ unverified |

**Read:** R007 is the rate the *marginal leveraged non-bank* actually pays. It is the right rate for valuing a leveraged bond carry trade; DR007 is the right rate for judging PBoC stance. Use both.

### A.4 R007 − DR007 spread — non-bank funding stress / leverage-in-the-system

This is the second-most-valuable single series in the whole catalogue and the cheapest early-warning indicator available.

**Construction:** R007 − DR007, daily, in bp. (Equivalently R001 − DR001 for the faster version.)

**Mechanism.** Banks are the ultimate cash providers; non-banks the ultimate cash takers. The spread is the price banks charge non-banks for balance sheet and counterparty risk. It widens when (a) banks' own reserves are scarce so they ration lending down the credit ladder, (b) non-bank leverage is high so demand is inelastic, or (c) a credit event makes non-bank counterparties suspect.

| R007 − DR007 | Read (judgemental) |
|---|---|
| 0–15bp | Normal |
| 15–40bp | Watch — non-banks paying up; check repo turnover and O/N share |
| 40–80bp | Stress — balance-sheet rationing; leveraged carry trades under pressure |
| > 80bp, or > 150bp intraday spike | Acute — this is the shape that preceded the Nov–Dec 2022 WMP redemption spiral and the 2016Q4 / 2013Q2 episodes |

**Caveats.** The spread is mechanically wide on quarter-end dates (MPA + LCR window-dressing, see B.6) — a 100bp quarter-end print is often noise; the same print mid-month is a genuine signal. Always compare to the same calendar position in prior quarters.

### A.5 GC007 / GC001 — exchange-traded repo, and the GC-vs-R gap

| Field | Detail |
|---|---|
| **English** | Shanghai Stock Exchange government-bond pledged repo, 7-day (and overnight) |
| **Chinese** | 上交所国债逆回购（7天）GC007；隔夜 GC001；深交所对应品种 R-007 / R-001 |
| **Ticker** | SSE **204007** (GC007), 204001 (GC001); SZSE 131800-series |
| **Publisher** | Shanghai Stock Exchange / Shenzhen Stock Exchange |
| **Frequency** | Continuous intraday, 09:30–15:00; daily OHLC and weighted average |
| **Source** | https://www.sse.com.cn/assortment/bonds/repo/repoinfo/basic/index.shtml?BOND_CODE=204007 ; product hub https://www.sse.com.cn/assortment/bonds/repo/ |
| **Fixing variants** | **FRGC001 / FRGC007** — fixings computed from trades between 09:30 and 15:00, weighted-average and adjusted for actual accrual days, which removes the "Thursday effect" distortion present in the headline GC quote |

**Why it matters.** The exchange repo market is the **retail and small-institution** funding venue — cash is supplied largely by retail investors and corporate treasuries parking money, demand comes from brokers and leveraged equity/bond accounts. It is **segmented** from the interbank market: the arbitrage between GC007 and R007 requires an institution with access to both plus available balance sheet. So **GC007 − R007 is a market-segmentation / balance-sheet-scarcity indicator**, not a redundant repo rate.

**Quarter-end behaviour.** GC rates spike far harder than interbank rates at quarter-ends and before long holidays, driven by the "+0 available, +1 withdrawable" settlement convention (the "Thursday effect") and by the quarter-end cash bid. Documented extreme: on **27 December 2016** GC007 printed a maximum annualised **8.5%** while the Shenzhen 7-day repo (R-007) reached 6.65%.

| GC007 − R007 at quarter-end | Read (judgemental) |
|---|---|
| < 50bp | Benign quarter-end |
| 50–200bp | Normal Chinese quarter-end friction |
| > 300bp, or GC007 > 5% | Genuine segmentation stress; balance sheet unwilling to arbitrage |

**Caveat.** Do not use raw GC007 in a composite index — its holiday/quarter-end kurtosis will dominate everything. Use either the FRGC fixing, a median-of-month, or the GC−R gap.

### A.6 SHIBOR — O/N, 1W, 3M

| Field | Detail |
|---|---|
| **English** | Shanghai Interbank Offered Rate |
| **Chinese** | 上海银行间同业拆放利率 |
| **Definition** | A **quoted, not transacted**, unsecured interbank offer rate. Computed from submissions by an **18-bank panel**; the top 4 and bottom 4 quotes are discarded and the remaining 10 averaged. **Eight tenors**: O/N, 1W, 2W, 1M, 3M, 6M, 9M, 1Y. |
| **Publisher** | National Interbank Funding Center (全国银行间同业拆借中心), under PBoC |
| **Frequency / lag** | Each business day, same-day |
| **Source** | https://www.shibor.org/ ; https://www.chinamoney.com.cn/chinese/bkshibor/ |
| **History** | Official launch January 2007 (trial from late 2006) ⚠️ exact start unverified |
| **Series** | CEIC SHIBOR family — https://www.ceicdata.com/en/china/national-interbank-funding-centre-nifc-interbank-offered-rate ; TradingEconomics 3M https://tradingeconomics.com/china/interbank-rate ; Wind `SHIBORON.IR`, `SHIBOR1W.IR`, `SHIBOR3M.IR` ⚠️ unverified |

**Declining relevance — be explicit about this.** SHIBOR O/N and 1W are *quotes* that track the repo market with a lag and essentially no independent information; the PBoC's benchmark-cultivation effort has explicitly moved to **DR**. Concretely:
- **Do not** use SHIBOR O/N or 1W as a liquidity gauge. They are strictly dominated by DR001/DR007.
- **Do** keep **3M SHIBOR**: at the 3M tenor there is genuine term-premium and bank-credit information, it is the floating leg of a large IRS market, and it remains a usable term-funding benchmark.
- SHIBOR retains historical value precisely because of its length — the 2013 crunch is legible in it (see A.9) whereas DR barely existed.

### A.7 IBO001 / IBO007 — unsecured interbank offered (transacted)

| Field | Detail |
|---|---|
| **English** | Interbank offered (unsecured lending) weighted-average rate, O/N and 7-day |
| **Chinese** | 银行间同业拆借加权平均利率（隔夜 / 7天），IBO001 / IBO007 |
| **Definition** | Volume-weighted average of **actual transacted** unsecured interbank loans, all participant types. Contrast with SHIBOR (quoted) and with R/DR (secured). |
| **Publisher** | CFETS / NIFC |
| **Frequency / lag** | Daily, same-day |
| **Source** | CEIC NIFC Interbank Offered Rate family — https://www.ceicdata.com/en/china/national-interbank-funding-centre-nifc-interbank-offered-rate ; ChinaMoney money-market pages |
| **Series** | Wind `IBO001.IB`, `IBO007.IB` ⚠️ unverified |

**Read.** **IBO007 − R007 is a pure unsecured-vs-secured (i.e. credit) spread** — the closest Chinese analogue to a LIBOR-OIS or FRA-OIS. It is the right series to isolate *counterparty* concern from *collateral/balance-sheet* scarcity, because both legs are transacted, both cover the whole market, and only the collateralisation differs. Turnover in unsecured lending is small relative to repo, so the series is noisier; use a 5-day moving average.

### A.8 Rate dispersion, intraday distribution, and repo turnover

These are the **quantity and distribution** companions to the rate levels, and they usually turn *before* the averages do.

**(a) Daily interbank pledged-repo turnover — 银行间质押式回购成交量**

| Field | Detail |
|---|---|
| **Definition** | Total daily transaction value of pledged repo in the interbank market (all tenors, all participants) |
| **Publisher** | CFETS / NIFC (daily); ChinaBond / SHCH for settlement views |
| **Frequency / lag** | Daily, same-day |
| **Source** | CEIC NIFC daily repo turnover family — https://www.ceicdata.com/en/china/national-interbank-funding-centre-nibfc-interbank-bond-turnover ; Statista compiled series https://www.statista.com/statistics/456767/china-interbank-market-pledged-repo-trading-volume/ |

**Why it is a leverage gauge.** Bond-market leverage is built by *rolling overnight repo to fund longer bonds*. Each turn of leverage mechanically generates a repo trade every single day. So turnover is close to a direct read on the stock of rolled leverage — when institutions are levering up, daily turnover rises even with no change in the underlying bond stock.

**The "RMB 7–8trn" heuristic — use with care.** The level is a *moving target*, because the market has grown structurally:

| Period | Daily pledged-repo turnover | Source context |
|---|---|---|
| Apr 2020 | ~4.8trn average; record 5.3trn on 7 Apr 2020 | "leverage is back" commentary |
| Dec 2021 | ~6trn+ | flagged as "biggest risk point in the bond market" |
| Jun 2022 | >6trn for 9 consecutive sessions — treated as a warning signal | |
| Aug 2022 | broke **7trn** on 4 Aug 2022; 6.88trn on 5 Aug | |

So: 7–8trn was a genuine red line **in 2022**. By 2026 the structural baseline is materially higher. **Do not use a fixed level.** Use instead: (i) turnover as a % of its own trailing 250-day median, (ii) turnover scaled by outstanding interbank bond stock, or (iii) the O/N share below. ⚠️ The specific "7–8trn = high leverage" number as a *current* threshold is unverified and, in my judgement, stale.

**(b) Overnight repo share of total turnover — the carry/leverage-crowding signal**

| Definition | R001 (or DR001) turnover ÷ total pledged-repo turnover, daily, % |
|---|---|
| **Why** | The share tells you *how short* the market has funded itself. A high share means the entire leveraged complex is rolling overnight — maximum sensitivity to a single bad funding day. This is the canonical "crowded carry" tell. |
| **Observed history** | ~80% in Apr 2020 (R001 daily avg 4.2trn of 4.8trn total). **90.3% average in 2022**, with R001 daily average 6.17trn. In 2026, overnight repo is reported at **>80% of money-market turnover**. |

| O/N share | Read (judgemental) |
|---|---|
| < 80% | Normal |
| 80–88% | Watch — carry trade building |
| > 88–90% sustained | **Crowded.** The system is maximally exposed to a funding shock; historically the configuration that precedes disorderly deleveraging |

**(c) Rate dispersion / intraday distribution**

- **Intraday high−low on DR007 and R007** (available from CFETS intraday dissemination) is the cleanest volatility measure. A widening high−low with a flat daily average is a *deteriorating* signal that the average conceals.
- **Realised volatility**: 20-day standard deviation of daily DR007, in bp. Post-June-2026 corridor narrowing this should run structurally lower; a regime break upward is meaningful.
- **R007 − DR007 *intraday max*** rather than the weighted averages catches the late-afternoon scramble that is the true stress moment.
- ⚠️ Full intraday tick distributions are a paid CFETS/Wind product; the free ChinaMoney pages give daily weighted averages and high/low only.

### A.9 Historical extremes — calibration anchors

| Episode | What happened | Use |
|---|---|---|
| **June 2013 ("钱荒" / Shibor Shock)** | O/N SHIBOR jumped from 7.66% (19 Jun) to **13.44%** (20 Jun); repo rates traded above 10% mid-June and printed record **25–30%** on 20 June, settling to 5–8% by 25 June. Trigger set: rapid loan growth, corporate income-tax deadline, required-reserve payment, and Dragon Boat Festival cash demand — with the PBoC deliberately withholding liquidity | The absolute upper bound of Chinese money-market stress; also the textbook illustration of Group D autonomous factors all hitting at once |
| **Q4 2016 – 2017 deleveraging** | Sustained R−DR widening, GC007 8.5% print on 27 Dec 2016 | Quarter-end segmentation extreme |
| **Nov–Dec 2022 WMP spiral** | Funds and WMPs dumped a record **RMB 1.3trn** of interbank bonds in November 2022; 7,722 of 13,582 WMPs (59.3%) fell below par; regulators asked banks to report on short-term liquidity | The NBFI-liquidity-feedback template (see E.6) |

---

## B. Bank funding and the term structure

### B.1 NCD / interbank certificate of deposit rates — 同业存单

| Field | Detail |
|---|---|
| **English** | Negotiable / interbank certificate of deposit issuance and secondary yields |
| **Chinese** | 同业存单 (NCD) |
| **Definition** | Tradable fixed-term deposit certificates issued by depository institutions in the interbank market. Tenors 1M, 3M, 6M, 9M, 1Y. Quoted by issuer rating (AAA / AA+ / AA) and issuer type (state-owned 国有行, joint-stock 股份行, city commercial 城商行, rural 农商行). |
| **Publisher** | CFETS/ChinaMoney (issuance, primary rates); ChinaBond (CCDC) secondary yield curves; Shanghai Clearing House (registration/depository) |
| **Frequency / lag** | Daily rates; issuance daily, with weekly/monthly aggregates |
| **Source** | ChinaMoney NCD pages (https://www.chinamoney.com.cn/) ; ChinaBond curves https://yield.chinabond.com.cn/cbweb-mn/yield_main?locale=en_US ; Bond Connect NCD primer https://www.chinabondconnect.com/en/Northbound/Services/Ncd-Subscription.html |
| **History start** | NCD market launched **December 2013**. Balance RMB 9.8trn end-2018; **RMB 14.8trn end-2021 = 5.7% of bank total liabilities** |
| **Series** | CEIC NCD turnover — https://www.ceicdata.com/en/china/national-interbank-funding-centre-nibfc-interbank-bond-turnover/cn-turnover-interbank-bond-spot-negotiable-certificate-of-deposit ; Wind `CDB*` family ⚠️ unverified |

**The headline tenor: 1Y AAA joint-stock bank NCD.** Joint-stock banks (股份制银行) are the right issuer cohort because they are large enough to be liquid and price-transparent, but — unlike the Big Six state banks — they are genuinely **liability-constrained** and must bid for wholesale funding. Their 1Y AAA NCD rate is therefore the cleanest market price of *marginal bank term funding*.

**Levels to anchor on:**
- Late Feb 2025: NCD issuance rates **above** the then-MLF rate, with the term inversion at a record.
- 5 Mar 2025: 1Y AAA NCD near the MLF level; spread to 1Y CGB at the **94.5th percentile**. Banks' 2025 NCD issuance quotas were raised ~RMB 3.5trn vs 2024 (large SOE + joint-stock banks ~RMB 3.2trn of that), reflecting the loss of non-bank deposits after the Dec 2024 regulatory change. March 2025 maturity wall: RMB 2.95trn.
- May 2026: 1Y AAA NCD around **1.45%**, near historic lows. 18 Mar 2026: 1Y SOE/joint-stock NCD under 1.55%, close to the 1.40% average interbank demand-deposit rate.
- 2026: cumulative NCD issuance exceeded **RMB 12trn in the first five months**.

### B.2 NCD net issuance and issuance success rate

| Indicator | Chinese | Definition | Read |
|---|---|---|---|
| **NCD net issuance** | 同业存单净融资额 | Gross issuance − maturities, weekly/monthly | Large positive net issuance into a rising rate = genuine funding pressure. Large positive net issuance into a *falling* rate = opportunistic pre-funding, benign |
| **Issuance success rate** | 发行成功率 | Amount actually placed ÷ amount planned, per auction; aggregated weekly | The **quantity-side** stress gauge. Rates can be capped by issuer discipline; the success rate then falls instead. A rate that looks calm with a collapsing success rate is a false all-clear |
| **Registered quota usage** | 备案额度使用率 | Issuance vs the annual registered quota | Quota exhaustion is a hard constraint that shows up as forced payment-up in Q4 |

⚠️ **Unverified:** I could not confirm an official published aggregate "success rate" series. In practice this is computed by sell-side desks and by Wind from ChinaMoney auction-by-auction data. Treat the 90%/80% bands often quoted as desk convention, not official.

**Practitioner bands (judgemental):** success rate >95% normal; 85–95% watch; <80% stress.

### B.3 The bank-liability-pressure spread — and how to rebuild it post-MLF-reform

**The classic gauge:** `1Y AAA NCD − 1Y MLF rate`.
- Logic: MLF is the PBoC's 1Y funding to banks. If banks will pay *more* than MLF in the open market, the PBoC's supply of 1Y money is insufficient and banks are liability-constrained — historically a reliable precursor to RRR cuts or MLF over-rollover. Sustained *negative* spread = comfortable.

**The problem.** Since the **25 March 2025** operation the MLF has been a **fixed-quantity, variable-rate, multiple-price** tender and **the PBoC no longer publishes a winning rate**. The MLF's "policy rate function has now entirely gone." The classic spread has no live denominator.

**Recommended replacements (in preference order):**

| Replacement | Formula | Comment |
|---|---|---|
| **1** | `1Y AAA NCD − 7d OMO rate` | Cleanest surviving version. Mixes a term premium into the signal, but the 7d OMO is a live, published, genuine policy rate |
| **2** | `1Y AAA NCD − 1Y CGB yield` | Pure bank-credit-plus-liquidity premium; percentile-ranked (this is what Chinese sell-side quotes as the "94.5th percentile" style statistic) |
| **3** | `1Y AAA NCD − 1Y IRS (repo-linked, FR007-based)` | Isolates bank funding premium from the expected path of policy — the most analytically correct, most data-intensive |
| **4** | `1Y AAA NCD − 1Y AAA CDB bond yield` | Bank vs policy-bank funding; cleanest on tax treatment |

**Judgemental bands for replacement #1 (`1Y AAA NCD − 7d OMO`), at a 1.40% OMO:**
| Spread | Read |
|---|---|
| < 0bp | Very comfortable; banks awash |
| 0–25bp | Normal |
| 25–50bp | Watch — liability pressure building |
| > 50bp | Stress — expect PBoC term supply (outright RR / MLF over-rollover) or an RRR cut |

### B.4 3M SHIBOR vs 3M NCD

**Construction:** `3M SHIBOR − 3M AAA NCD yield`, in bp.

**Read.** Both are 3M bank funding, but SHIBOR is a *quote* from a privileged 18-bank panel and NCD is a *transacted* price paid by the marginal bank. The gap therefore measures (a) how stale/administered the SHIBOR panel quote is, and (b) the tiering between panel banks and everyone else. In episodes of genuine funding stress, **3M NCD rises through 3M SHIBOR** — SHIBOR panel banks under-quote because the panel is dominated by liquidity-rich institutions. A persistent negative `SHIBOR − NCD` gap is a small-bank-tiering signal.

⚠️ Precise historical distribution of this spread unverified in this pass.

### B.5 Loan-to-deposit ratio and the deposit–loan funding gap

| Field | Detail |
|---|---|
| **English / Chinese** | Loan-to-deposit ratio / 存贷比; funding gap / 存贷差 |
| **Definition** | LDR = total loans ÷ total deposits, banking system or by bank cohort. Funding gap = loans − deposits (or its flow, Δloans − Δdeposits) |
| **Publisher** | NFRA (National Financial Regulatory Administration) supervisory statistics; PBoC depository-corporation survey |
| **Frequency / lag** | Quarterly (NFRA); monthly (PBoC credit/deposit aggregates, ~10–15 days) |
| **Source** | NFRA supervisory statistics https://www.nfra.gov.cn/en/view/pages/ItemDetail.html?docId=1222165 ; PBoC financial statistics https://www.pbc.gov.cn/en/3688247/3688978/3709137/5870352/index.html |

**Regulatory status.** The **75% statutory LDR cap was abolished** by amendment to the Commercial Bank Law, effective **1 October 2015**; LDR is now a *liquidity-monitoring* indicator only, not a binding constraint. So do not read a rising LDR as a regulatory constraint — read it as a **structural driver of NCD demand**: when loans grow faster than deposits, the gap must be plugged with wholesale funding, which shows up directly in NCD net issuance and NCD rates.

**Context (2025):** credit and deposit growth both ~7% in 2025; new bank loans fell to a 7-year low of RMB 16.27trn in 2025. Shadow/wholesale funding reliance is expected to rise modestly at smaller banks as interbank rates fall.

**Read for a liquidity dashboard:** use the **flow** version — 12m rolling (Δloans − Δdeposits) — as a *leading* indicator of NCD supply 1–2 quarters out. Overlaps with the credit analyst's territory; keep strictly to the funding-gap interpretation.

### B.6 Excess reserve ratio (超额准备金率, "超储率")

**The single best measure of how much settlement liquidity actually exists.**

| Field | Detail |
|---|---|
| **English** | Excess reserve ratio of financial institutions |
| **Chinese** | 金融机构超额准备金率（超储率） |
| **Definition** | Excess reserves (deposits at the PBoC beyond the required minimum) ÷ total RMB deposits of financial institutions, % |
| **Publisher** | PBoC, in the quarterly **China Monetary Policy Report** (货币政策执行报告) |
| **Frequency** | **Quarterly** |
| **Release lag** | ~5–6 weeks after quarter-end (Q1 2026 MPR published 11 May 2026; Q4 2025 MPR published 10 Feb 2026; Q3 2025 MPR published 11 Nov 2025) |
| **Source** | PBoC MPR index (EN): https://www.pbc.gov.cn/en/3688229/index.html ; mirrored CN PDFs, e.g. Q1 2026 https://jrj.sh.gov.cn/cmsres/5a/5ae23d4703d4409b8c2b2c325c40b774/b0233b6bfdbe3826e365a66f35d86f83.pdf ; Q4 2025 https://cif.mofcom.gov.cn/cif/html/upload/20260211143114167_2025年第四季度中国货币政策执行报告.pdf ; Q3 2025 https://cif.mofcom.gov.cn/cif/html/upload/20251124101800795_中国货币政策执行报告2025年第三季度.pdf ; Q2 2026 summary https://jrj.sh.gov.cn/ZXYW178/20260813/1b25ff83c27549d3af0244230130f351.html |
| **Recent readings** | **1.50% at 1 Dec 2025** (i.e. end-Q4 2025 vintage), up from **1.40% at 1 Sep 2025** |

**Why ~1.5% is the comfort threshold.** With the weighted-average RRR now around 6.2%, banks' total reserves are ~7.5–8% of deposits, of which only the excess portion is usable for settlement. Historically the system has functioned smoothly at ~1.5–2.0% and shown stress below ~1.0–1.2%. The ratio has trended structurally *down* over two decades (payment-system efficiency, better liquidity forecasting, the corridor) so the "comfort" level itself drifts lower — treat 1.5% as a **soft, drifting** threshold, not a constant. ⚠️ The specific 1.5% comfort level is practitioner convention, not an official PBoC threshold.

| 超储率 | Read (judgemental) |
|---|---|
| > 2.0% | Very ample (typically year-end fiscal release) |
| 1.3–2.0% | Normal |
| 1.0–1.3% | Watch |
| < 1.0% | Tight — expect DR007 to trade persistently above OMO |

**Nowcasting it monthly.** The quarterly frequency and 6-week lag make the published series nearly useless for live monitoring. Rebuild it monthly from the PBoC balance sheet and the depository-corporation survey using the Section 0.1 identity:

```
Excess reserves_t ≈ [Reserve money (储备货币)]
                   − [Currency in circulation (货币发行)]
                   − [Required reserves ≈ applicable deposit base × weighted RRR]

超储率_t ≈ Excess reserves_t ÷ Total RMB deposits_t
```

All inputs are monthly: PBoC balance sheet (货币当局资产负债表, ~1 month lag), the weighted-average RRR (published at each RRR change), and deposits from the monthly financial statistics. Then **flow-check** the nowcast against the Group C + Group D flows for the month — the two should reconcile. Calibrate the level against each new quarterly official print.

⚠️ Caveat: the deposit base to which RRR applies excludes some items (e.g. certain non-bank deposits) and differs by institution tier (large vs small banks, plus targeted discounts), so the required-reserve estimate carries real error. Expect ±10–20bp of nowcast error on the ratio — enough to matter at these levels. Use the *change*, not the level, for signals.

### B.7 LCR / NSFR and the MPA quarter-end effect

| Field | Detail |
|---|---|
| **Indicators** | Liquidity Coverage Ratio (流动性覆盖率, LCR); Net Stable Funding Ratio (净稳定资金比例, NSFR); also Liquidity Matching Ratio (流动性匹配率) and High-Quality Liquid Asset Adequacy Ratio (优质流动性资产充足率) for smaller banks |
| **Publisher** | NFRA (aggregate, quarterly); individual banks (Pillar 3, quarterly) |
| **Frequency / lag** | Quarterly, ~6–10 weeks |
| **Source** | NFRA https://www.nfra.gov.cn/en/view/pages/ItemDetail.html?docId=1222165 ; bank Pillar 3, e.g. BOC https://pic.bankofchina.com/bocappd/report/202510/P020251028595147627739.pdf |
| **Latest confirmed** | Commercial banks **LCR 149.25%** and **NSFR 127.59%** at end-Q2 2025 (LCR +3.05pp q/q, NSFR +0.02pp q/q). BOC Q3 2025: LCR 138.29%, NSFR 127.89%. A Risk Quantum study found China led a global LCR retreat in 2025 |

**The MPA (宏观审慎评估) quarter-end effect — why quarter-ends are different.**

The PBoC's **Macro Prudential Assessment**, introduced at the start of 2016, scores banks 0–100 across **16 indicators in seven categories** at **quarter-end**, with consequences for reserve remuneration and differentiated requirements. Combined with the NFRA's quarter-end LCR/NSFR reporting points, this produces a predictable and mechanical behaviour pattern:

1. In the final ~2 weeks of each quarter, banks shrink interbank asset exposure, cut lending to non-banks, and hoard HQLA and reserves.
2. Consequence: **R007 − DR007 widens**, **GC007 spikes**, **NCD rates rise at the short tenors**, and bond-market leverage is forced down.
3. Reverses within 1–3 business days of quarter-end.

**Practical rule:** build a `quarter_end` dummy for the last 10 business days of March/June/September/December, and a separate `year_end` dummy for December (which stacks MPA + annual audit + fiscal-spending timing). **Never** compare a quarter-end print to a mid-month print; compare like-for-like against the same day-count-to-quarter-end in prior quarters. Recent PBoC communication has emphasised re-orienting the MPA toward supporting monetary-policy transmission, which should *reduce* but not eliminate the effect.

---

## C. Central bank liquidity operations — the supply side

### C.1 Daily OMO reverse repo (公开市场逆回购操作)

| Field | Detail |
|---|---|
| **English / Chinese** | Open-market reverse repo operations / 公开市场业务（逆回购） |
| **Definition** | PBoC lends to primary dealers against pledged collateral. Standard tenors 7-day (the policy-rate tenor) and 14-day (used around Chinese New Year and quarter-ends). **Fixed-rate, quantity tender** at the policy rate since 2024. **Overnight** added June 2026 (see C.7) |
| **Publisher** | PBoC Open Market Operations Office |
| **Frequency / lag** | **Every business day**; announcement same morning (~09:20 Beijing ⚠️ unverified), result same day |
| **Source** | PBoC OMO announcements: https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/index.html (CN) ; EN OMO section https://www.pbc.gov.cn/en/3688241/3688765/index.html ; TradingEconomics https://tradingeconomics.com/china/reverse-repo-rate |
| **History** | Reverse repo OMOs since the late 1990s; daily operation cadence since 2013 ⚠️ exact start unverified |

**The number that matters: NET injection.** `Gross operation − maturing operations = net injection (净投放) / net drain (净回笼)`. Published daily and reported by every wire.

**Read.**
- Large net injections cluster predictably: **tax-payment weeks** (mid-month, especially Jan/Apr/May/Jul/Oct), **quarter-ends**, **pre-Chinese-New-Year**, and **heavy government-bond-settlement weeks**.
- A *persistent* daily drain with DR007 stable = the PBoC is comfortable; a drain with DR007 rising = deliberate tightening signal.
- **Caveat:** in 2026 the 7-day OMO has repeatedly printed tiny amounts (e.g. CNY 5bn, CNY 7bn) and even zero for consecutive sessions, because the **overnight tool has taken over** the fine-tuning role. Reading "zero 7-day OMO" as tightening in 2026 is a **serious misread** — you must aggregate across the 7d and O/N tools.

### C.2 MLF — Medium-term Lending Facility (中期借贷便利)

| Field | Detail |
|---|---|
| **Definition** | 1-year collateralised lending to banks. Since the **25 March 2025** operation: **fixed-quantity, variable-rate, multiple-price (多重价位) tender**; the PBoC **no longer publishes a winning rate**. The operation date was also moved (the PBoC now conducts it later in the month, separated from the LPR fixing) |
| **Publisher / freq** | PBoC; **monthly** |
| **Source** | PBoC OMO announcements; gov.cn notices, e.g. https://english.www.gov.cn/news/202605/22/content_WS6a10675ec6d00ca5f9a0b307.html ; https://english.www.gov.cn/news/202512/24/content_WS694bcfb0c6d00ca5f9a0842f.html ; TradingEconomics https://tradingeconomics.com/china/liquidity-injections-via-mlf |
| **Key structural change** | The move to multiple-price bidding removed MLF's policy-rate function entirely — it is now a **pure quantity tool** whose purpose is to lower bank liability costs and ease NIM pressure |

**Recent operations (confirmed):**

| Date | Gross | Maturing | Net |
|---|---|---|---|
| Nov 2024 | 900bn | — | — |
| Jan 2026 (23rd) | 900bn | 200bn | **+700bn** |
| May 2026 (22nd) | 600bn | 500bn | **+100bn** |
| Jul 2026 (24th) | 400bn | — | — |
| Aug 2026 | — | — | **−100bn** (net drain); balance fell to **7.4trn** |
| H1 2026 total | **3.5trn** gross; outstanding **7.4trn** at end-June 2026, **+1.15trn YTD** | | |

**Read.** With no published rate, the **only** information in an MLF operation is the **net quantity** and the **outstanding balance path**. Over-rollover (net positive) into a month with heavy NCD maturities is a deliberate signal that the PBoC is capping bank liability costs. The PBoC's own "lowest winning MLF rate" occasionally leaks to the press (e.g. reported to have hit a new low in May 2026) — treat such reports as market colour, not data.

### C.3 Outright reverse repo (买断式逆回购) — the 2024 addition

| Field | Detail |
|---|---|
| **English / Chinese** | Outright (buyout) reverse repo / 买断式逆回购 |
| **Announced** | **28 October 2024** |
| **Definition** | The PBoC buys securities outright from primary dealers with an agreement to resell — **collateral title transfers to the PBoC's account** rather than merely being pledged. **Fixed-quantity, interest-rate bidding with multiple winning price levels**; primary dealers only; conducted generally **once a month**; tenor **up to one year**, in practice **3-month and 6-month** |
| **Why it was created** | It filled a genuine **1-month-to-1-year gap** in the PBoC's toolkit — between 7/14-day OMO and 1-year MLF there was nothing. Immediate motivation: offsetting the very heavy concentration of MLF maturities at end-2024 without having to over-roll MLF (which would have signalled on price) |
| **Publisher / freq** | PBoC; monthly (sometimes twice, for the two tenors) |
| **Source** | gov.cn https://english.www.gov.cn/news/202410/28/content_WS671f2a63c6d0868f4e8ec5d2.html ; series https://tradingeconomics.com/china/outright-reverse-repo ; examples http://www.ecns.cn/cns-wire/2026-08-05/detail-ihfhziqh0061381.shtml , http://english.scio.gov.cn/pressroom/2026-08/14/content_118647130.html , https://english.www.gov.cn/news/202509/05/content_WS68ba20cbc6d0868f4e8f558c.html |
| **History start** | **October 2024** (first operation: **RMB 500bn, 6-month**) |

**Operation history (confirmed points):**

| Period | Operation |
|---|---|
| Oct 2024 | 500bn, 6M — first ever |
| Sep 2025 | 1trn operation announced |
| Feb 2026 | 1,000bn |
| Mar 2026 | 500bn |
| Jul 2026 | **1.4trn, 6-month — largest on record for this tool**, timed for tax payments + debt issuance |
| Aug 2026 | 500bn (3M continued net injection) |
| Sep 2026 | Shifted to **equal-amount rollover** for 3M: 500bn injected against 500bn maturing |
| 2024–2026 average | ~1,122bn per operation |

**Read.**
- The **net** (gross − maturing) is what matters, and because tenors are 3M and 6M you must build a maturity ladder to compute it. This is the most commonly mis-tracked item in China net-liquidity models.
- A shift from **net injection → equal-amount rollover** (as in Sep 2026) is a genuine stance signal: the PBoC has stopped adding term liquidity.
- Because collateral title transfers, outright reverse repo **frees the collateral from the dealer's balance sheet** — it is more balance-sheet-efficient for dealers than pledged repo and supports bond-market liquidity, not just reserves.
- ⚠️ Rates are not published (multi-price), so this tool carries **no price signal** — quantity only.

### C.4 PBoC government bond trading (国债买卖)

| Field | Detail |
|---|---|
| **Definition** | Outright secondary-market purchases and sales of CGBs by the PBoC — permanent reserve creation/destruction, distinct from repo |
| **Started** | **August 2024**; first monthly disclosure 30 Aug 2024 reporting a **net purchase of RMB 100bn face value** |
| **Publisher / freq** | PBoC; **monthly**, disclosed in the first days of the following month |
| **Source** | PBoC OMO section; https://www.business-standard.com/world-news/china-s-central-bank-starts-trading-govt-bonds-to-influence-yield-curve-124083000779_1.html ; suspension http://english.scio.gov.cn/m/pressroom/2025-01/15/content_117666228.html ; resumption https://triviumchina.com/2025/11/05/pboc-resumes-bond-trading-to-smooth-yield-curve/ |

**Full timeline (this is the part people get wrong):**

| Month | Net |
|---|---|
| Aug 2024 | +100bn |
| Sep 2024 | +200bn |
| Oct 2024 | +200bn |
| Nov 2024 | +200bn |
| Dec 2024 | +300bn |
| **Aug–Dec 2024 total** | **+1.0trn**; PBoC CGB holdings **RMB 2.88trn at end-2024 = 6.5% of total assets** |
| **Jan 2025** | **SUSPENDED** (announced 10 Jan 2025). Stated reason: demand exceeded supply in the CGB market and market risks were accumulating; widely also read as yuan defence at a 16-month low. Holdings drifted down to **RMB 2.4trn by May 2025 (~5.4% of assets)** as bonds ran off |
| **Oct 2025** | **RESUMED** after a 10-month pause — Governor Pan Gongsheng signalled in late Oct 2025 that conditions had improved. **Net +20bn in October**, disclosed 4 Nov 2025 |
| **Nov 2025** | Second consecutive month of net buying, ~USD 7bn equivalent |

**Read.** Because this tool is *permanent* reserve creation, a RMB 100bn net purchase is worth far more than a RMB 100bn 7-day reverse repo. Weight it accordingly in any net-liquidity aggregate (see C.8). The suspension/resumption decisions are also the PBoC's clearest **yield-curve and FX** signals: the PBoC buys when it wants reserves and a steeper curve, and stops when it judges long yields too low or the yuan under pressure.

### C.5 PSL — Pledged Supplementary Lending (抵押补充贷款)

| Field | Detail |
|---|---|
| **Definition** | Long-tenor, low-cost collateralised lending by the PBoC to the three policy banks (CDB, EximBank, ADBC), earmarked for shantytown/affordable housing, urban village redevelopment and infrastructure |
| **Publisher / freq** | PBoC; **monthly** balance and net change |
| **Source** | PBoC structural-tools page http://www.pbc.gov.cn/en/3688229/3688335/4738114/5241677/index.html ; series https://www.ceicdata.com/en/china/lending-facility/balance-of-pledged-supplementary-lending-psl ; https://en.macromicro.me/series/30903/china-pboc-mortgage-supplementary-loan-balance |
| **Confirmed points** | Reactivated Dec 2023 with **+350bn**, taking the balance from RMB 2.902trn (Nov 2023) to **RMB 3.252trn (end-Dec 2023)**; **+150bn in Jan 2024 → RMB 3.4trn**. ⚠️ 2025–26 monthly path unverified in this pass |

**Read.** PSL is *base money creation with a fiscal purpose*. It is the most policy-signalling of the quantity tools: a PSL restart is a near-unambiguous signal of a property/infrastructure support push. For a pure liquidity dashboard, the monthly **net** change belongs in the net-injection aggregate; the *level* belongs to the credit analyst.

### C.6 SLF and the corridor ceiling

| Field | Detail |
|---|---|
| **English / Chinese** | Standing Lending Facility / 常备借贷便利 |
| **Definition** | On-demand collateralised lending at the bank's initiative, O/N, 7-day and 1-month. Forms the **formal corridor ceiling** (7d SLF = 7d OMO + 100bp) |
| **Publisher / freq** | PBoC; rates announced on change; monthly usage volumes published |
| **Source** | https://english.www.gov.cn/news/202407/22/content_WS669e08fdc6d0868f4e8e9555.html ; https://english.www.gov.cn/news/202505/07/content_WS681af03ec6d0868f4e8f250c.html ; CEIC https://www.ceicdata.com/en/china/lending-facility/cn-standing-lending-facility-slf-rate-7-day |
| **Latest confirmed rates** | After the May 2025 cut: **O/N 2.25%, 7D 2.40%, 1M 2.75%** |

**Read.** SLF *usage volume* (monthly) is the real signal, not the rate: non-trivial SLF drawdown means some institutions could not fund in the market at all. The rate itself is now largely decorative — the **temporary O/N reverse repo at OMO+25bp is the binding ceiling**, 65bp below the 7d SLF.

### C.7 The temporary overnight repo / reverse repo corridor, and the 2026 overnight OMO

**July 2024 — creation of the de facto narrow corridor.**
The PBoC announced it would conduct **temporary overnight repo (正回购, a drain) and temporary overnight reverse repo (逆回购, an injection)** "depending on market conditions," priced at:
- Temporary O/N **repo** = 7d OMO **− 20bp** → **floor**
- Temporary O/N **reverse repo** = 7d OMO **+ 50bp** → **ceiling**
→ a **70bp** de facto corridor, replacing the ~245bp IOER-to-SLF corridor. This was the concrete step that made the 7-day OMO rate *the* policy rate and made DR007 the variable being steered.

**17 June 2026 — narrowing to 50bp (Lujiazui Forum).**
Governor Pan Gongsheng announced six measures, of which two are directly liquidity-relevant:
1. The temporary O/N repo and reverse repo rates are reset to **±25bp** around the 7d OMO rate, narrowing the corridor from **70bp to 50bp**.
2. The PBoC will **expand the OMO toolkit with overnight reverse repo operations** to meet short-term liquidity demand.

(The other four: an RMB repo facility for foreign and international monetary authorities; study of a **macro-prudential liquidity support tool for non-bank financial institutions** under specific circumstances — directly relevant to the R−DR spread, since it would put a backstop under NBFI funding; an offshore-RMB FX trading pilot in the Shanghai FTZ; and a Shanghai offshore-finance action plan.)

**29–30 June 2026 — the overnight reverse repo debut.**
- **29 Jun 2026:** first-ever overnight reverse repo OMO, **RMB 300bn**, at **1.25%** — **the rate was not disclosed in the official statement**; 1.25% was reported via sources and is **10bp below** the median analyst forecast of 1.35% and **15bp below** the 7d OMO rate of 1.40%.
- **30 Jun 2026:** **RMB 600bn** — nearly RMB 1trn of overnight funding in two days.
- **14 Aug 2026:** first *mid-month* (rather than quarter-end) overnight reverse repo — evidence the tool is becoming routine fine-tuning, not just turn-of-quarter smoothing.
- Market read: Standard Chartered argued a rate at or below 1.25% constitutes a **de facto rate cut**; Citi and StanChart pulled forward LPR-cut calls. The PBoC's choice **not to publish the rate** appears deliberate — preserving ambiguity so the market does not price a concentrated release of easing expectations.

**Why this matters for the indicator set.** Overnight repo is **>80% of money-market turnover**, so a direct O/N lever is the most powerful short-rate instrument the PBoC has ever had. Practical implications:
1. Monitor the **daily O/N reverse repo amount** as a first-class series alongside 7d OMO.
2. The **unpublished rate** must be **inferred** — back it out from DR001 behaviour on operation days, or from wire "sources" reporting. Treat any inferred rate as ⚠️ unverified.
3. Expect structurally **lower DR001/DR007 volatility** and a **compressed right tail**. Recalibrate all volatility-based stress triggers on post-June-2026 data only.

### C.8 RRR cuts — quantifying long-term liquidity released

| Field | Detail |
|---|---|
| **English / Chinese** | Reserve requirement ratio / 存款准备金率 |
| **Publisher / freq** | PBoC; ad hoc (announced days before effect) |
| **Source** | https://english.www.gov.cn/news/202505/07/content_WS681af001c6d0868f4e8f2509.html ; https://english.www.gov.cn/news/202505/15/content_WS68254f59c6d0868f4e8f2902.html ; CEIC https://www.ceicdata.com/en/indicator/china/reserve-requirement-ratio |

**Confirmed levels and quantifications:**

| Event | Detail |
|---|---|
| Sep 2024 cut | Weighted-average RRR to **6.6%** |
| **7 May 2025 announcement / 15 May 2025 effective** | **−50bp**, releasing **~RMB 1trn** of long-term liquidity — the first 2025 cut, part of a 10-point package with a 10bp policy-rate cut |
| Jan 2026 | Weighted-average RRR **~6.3%** |
| Jun 2026 | Weighted-average RRR **6.2%** |

**Rule of thumb:** at current deposit levels a **50bp RRR cut ≈ RMB 1trn** of permanent liquidity. Scale linearly for other sizes; the PBoC states the figure explicitly in each announcement, so use the announced number rather than your own estimate.

**Read.** RRR-released funds are **permanent and free** — qualitatively different from repo. In a net-liquidity aggregate, RRR cuts should either (a) be entered as a one-off flow in the effective month, or (b) be handled by tracking **required reserves** directly in the Section 0.1 identity, which is cleaner because it also captures the ongoing drag from deposit growth. Do not double-count.

### C.9 Aggregate: a net liquidity injection measure

**Recommended construction, weekly and monthly:**

```
Net PBoC liquidity (flow, RMB bn)
  =  net 7-day/14-day OMO reverse repo
  +  net overnight reverse repo OMO                 (new, from Jun 2026)
  +  net temporary O/N repo/reverse repo            (sign: reverse repo +, repo −)
  +  net MLF                     (gross − maturing)
  +  net outright reverse repo   (gross − maturing; needs a 3M/6M maturity ladder)
  +  net PSL
  +  net SLF usage
  +  net PBoC CGB purchases      (国债买卖; weight UP — permanent money)
  +  net treasury cash deposits placed at banks     (国库现金定存; gross − maturing)
  +  RRR-equivalent              (one-off in the effective month, or via Δrequired reserves)

Then, for the true settlement-balance picture, subtract the autonomous drains (Group D):
  −  Δ government deposits at the PBoC (财政存款)
  −  Δ currency in circulation (M0)
  −  Δ required reserves from deposit growth
  +  Δ FX position (外汇占款)
```

**Design notes.**
1. **Weight by permanence.** A reasonable (judgemental) scheme: outright CGB purchases and RRR cuts = 1.0; PSL and MLF = 0.8; 6M outright reverse repo = 0.5; 3M outright reverse repo = 0.35; 7d OMO = 0.1; O/N OMO = 0.03 (roughly, weight ≈ tenor ÷ 1 year, with permanent tools at 1.0). This "duration-weighted net injection" correlates far better with DR007 than the raw sum.
2. **Publish two versions:** the raw *gross* net injection (what the wires report) and the duration-weighted one (what actually drives rates).
3. **Cross-check** the monthly total against the change in the nowcast excess reserve ratio (B.6). Persistent divergence means your maturity ladder is wrong — almost always the outright reverse repo ladder.
4. ⚠️ The PBoC does not publish a single consolidated net-liquidity number; every such series (Wind, CEIC, sell-side) is a vendor construction with different tool coverage. Know which tools your source includes before comparing across vendors.

---

## D. Autonomous liquidity factors — what drains/adds outside PBoC control

This is where China differs most from DM money markets, and where most forecasting error lives.

### D.1 Government/fiscal deposits at the PBoC (财政存款) — the biggest China-specific driver

| Field | Detail |
|---|---|
| **English / Chinese** | Government deposits at the central bank / 政府存款（财政存款） |
| **Definition** | Treasury and government balances held at the PBoC. **A rise is a pure drain of bank reserves** — money leaves the commercial banking system entirely and sits on the central bank's balance sheet |
| **Publisher / freq** | PBoC; **monthly** (PBoC balance sheet 货币当局资产负债表; also the monthly financial statistics "财政性存款" line) |
| **Release lag** | ~3–5 weeks |
| **Source** | PBoC statistics https://www.pbc.gov.cn/en/3688247/3688978/3709137/5870352/index.html ; balance-sheet views https://en.macromicro.me/collections/31/cn-finance-relative/17672/cn-major-liabilities-of-pboc-balance-sheets ; https://keyneswatch.com/cn/balance_sheet |

**The seasonal pattern — memorise it.**
- **Tax-payment months: January, April, May, July, October.** These are the months containing quarterly corporate-tax settlement deadlines (and the January annual settlement). Fiscal deposits *rise*, reserves *drain*, and the drain concentrates in the **mid-month tax window (roughly the 15th–25th)**. The PBoC reliably pre-injects into these windows — e.g. the RMB 1.4trn 6M outright reverse repo in July 2026 was explicitly framed around tax payments and debt issuance.
- **Fiscal-spending release: late in each quarter and overwhelmingly in December.** Year-end expenditure pushes fiscal deposits sharply *down*, flooding banks with reserves. This is why the excess reserve ratio jumps at year-end (1.50% at end-2025) and why December often ends loose despite MPA.
- **Bond-issuance interaction:** when the Treasury or local governments issue bonds, the proceeds move from bank reserves into government deposits at the PBoC *until spent*. Issuance and spending are not synchronised — the gap between them is a drain.

**Read (judgemental):** a month-on-month rise in fiscal deposits above ~RMB 800bn–1trn in a tax month is a large drain requiring PBoC offset; the April and October prints are typically the largest single-month drains of the year.

### D.2 Government bond net issuance (CGB + local government special bonds)

| Field | Detail |
|---|---|
| **English / Chinese** | Central government bond / 国债; local government bonds / 地方政府债, of which special-purpose bonds / 地方政府专项债; ultra-long special CGBs / 超长期特别国债 |
| **Definition** | Gross issuance minus redemptions. Settlement moves reserves from banks to the government's account at the PBoC — a **supply shock to bank reserves** on settlement date |
| **Publisher / freq** | MOF issuance calendars; ChinaBond/CCDC settlement data; provincial finance bureaux for LGBs. Weekly/monthly aggregates |
| **Source** | https://en.macromicro.me/series/28914/china-local-government-bond-special-bond-issuance ; https://en.macromicro.me/collections/31/cn-finance-relative/75563/china-local-government-bonds ; ChinaBond https://yield.chinabond.com.cn/ |

**2026 scale (confirmed):**
- Local government bond issuance reached **RMB 2.2trn by late February 2026, +22% y/y** — a deliberately front-loaded calendar.
- Of new bonds, ~RMB 600bn were special bonds for direct project investment (as of that point).
- Local special-purpose bond quota rising from **RMB 4.4trn (2025) to ~RMB 5trn (2026)**.
- Ultra-long special CGBs: **RMB 1.3trn proposed in the work report**, with expectations of ~RMB 2trn in 2026 (vs RMB 1trn in 2024).
- China's government debt is projected to grow by roughly USD 1trn in 2026.

**Read.** Build a **weekly net-settlement calendar** — this is the highest-value piece of manual data work in China rates. A week with >RMB 400–500bn of net government bond settlement and no offsetting PBoC operation will show up directly in DR007 within 1–2 days. Front-loaded issuance (Q1 2026) means the drain is concentrated early in the year, which is precisely when the PBoC compensates with outright reverse repo.

⚠️ Caveat: settlement date ≠ auction date; use settlement. And local government **refinancing/swap** bonds that replace existing debt are largely reserve-neutral — separate them from genuinely *new* net issuance.

### D.3 Currency in circulation (M0) — the Chinese New Year cash cycle

| Field | Detail |
|---|---|
| **English / Chinese** | Currency in circulation / 流通中现金 (M0); on the PBoC balance sheet, 货币发行 |
| **Publisher / freq** | PBoC; monthly (M0 in the money-supply release); the PBoC balance-sheet "currency issue" line |
| **Release lag** | ~10–15 days for M0 |
| **Source** | https://www.pbc.gov.cn/en/3688247/3688978/3709137/5870352/index.html |

**The CNY cycle.** Cash demand has a very sharp, very predictable seasonal: a large withdrawal in the **2–4 weeks before Chinese New Year** (red packets, cash gifting, holiday spending) and a near-complete return over the **4–8 weeks after**. A pre-CNY cash drain of several hundred billion to over a trillion yuan is normal. The PBoC routinely runs large 14-day reverse repo operations specifically to bridge it, and RRR cuts have historically been timed to the window.

**Read.** Because the CNY date moves (late Jan to late Feb), **never compare January or February y/y without date-aligning to the festival**. Use a "days to/from CNY" alignment. The cash return in March is a mechanical easing force that is often misread as policy easing.

### D.4 FX position / funds outstanding for foreign exchange (外汇占款)

| Field | Detail |
|---|---|
| **English / Chinese** | Funds outstanding for foreign exchange / 外汇占款 (PBoC) and the broader "FX purchases by financial institutions" series |
| **Definition** | RMB created by the PBoC when it buys foreign assets. When the PBoC accumulates reserves it credits banks' reserve balances — an injection; when reserves fall, a drain |
| **Publisher / freq** | PBoC (balance sheet and the FX-purchase position of financial institutions); **monthly**. Related BoP/settlement data from SAFE |
| **Source** | PBoC balance sheet; SAFE https://www.safe.gov.cn/en/ ; https://en.macromicro.me/collections/31/cn-finance-relative/17671/cn-major-assets-of-pboc-balance-sheets |

**Read.** This was *the* dominant base-money channel from 2002 to 2014, when the PBoC sterilised massive FX inflows. Since the 2015 EM crisis it has been a **small and mostly flat** line — the PBoC now creates base money through lending tools instead. Monitor it for **regime change**, not month-to-month noise: a sustained re-acceleration (large inflows, a strengthening yuan and PBoC accumulation) would mechanically loosen liquidity and reduce the need for RRR cuts. A sustained decline (capital outflow) is a structural drain that historically forced RRR cuts to offset.

⚠️ Caveat: the PBoC balance-sheet 外汇占款 line and the "FX purchases of financial institutions" line are different series with different coverage; state which you are using.

### D.5 Required-reserve changes from deposit growth

**Definition:** `Δ required reserves ≈ Δ (applicable deposit base) × weighted-average RRR`, plus any level change from an RRR cut.

**Why it matters:** it is a **silent, continuous drain**. With deposits ~RMB 300trn+ and a weighted RRR of 6.2%, every RMB 1trn of deposit growth locks up ~RMB 62bn of reserves permanently. Over a year of ~7% deposit growth this is a multi-trillion drag that must be offset by PBoC injections or RRR cuts. This is the structural reason China runs a recurring RRR-cut cycle rather than a steady-state balance sheet.

**Read:** monthly, from the deposit aggregates and the known weighted RRR. Include it in the Section 0.1 identity.

⚠️ Caveat: the applicable deposit base excludes certain categories and differs across bank tiers (large vs small banks, plus targeted incentives), so this is an estimate.

### D.6 Treasury cash management deposits at commercial banks (国库现金定存)

| Field | Detail |
|---|---|
| **English / Chinese** | Central Treasury cash management time deposits with commercial banks / 中央国库现金管理商业银行定期存款 |
| **Definition** | The MOF moves Treasury demand deposits **out of the PBoC and into term deposits at commercial banks** via auction, which **releases base money** for the life of the deposit. Auctioned jointly by the MOF and PBoC by interest-rate bidding, historically **single-price** award, more recently also **multiple-price** (both formats used in Dec 2025) |
| **Publisher / freq** | MOF + PBoC; irregular (multiple "issues" per year — e.g. at least 14 issues in 2025) |
| **Release lag** | Tender results published same/next day |
| **Source** | PBoC tender results, e.g. Issue 13 2025 https://www.pbc.gov.cn/en/3688241/3688765/3688753/2026010414034515582/index.html and Issue 14 2025 https://www.pbc.gov.cn/en/3688241/3688765/3688753/2026010414084370345/index.html ; index https://www.pbc.gov.cn/en/3688241/3688765/3688753/index.html |

**Read.** Small in scale relative to OMO but useful for two reasons: (i) the **auction rate** is a genuine, published market-clearing price of bank term funding to a risk-free depositor — a good cross-check on NCD rates; (ii) it is the mechanism by which fiscal-deposit drains are partially recycled back to banks, so it belongs in the net-injection aggregate with a maturity ladder like the outright reverse repo.

**Also watch:** local treasury cash deposits (地方国库现金定存), run by provincial finance bureaux — smaller, more fragmented, and a genuine funding source for city and rural commercial banks.

---

## E. Market liquidity / broader financial liquidity

### E.1 CGB yield curve and the term spread

| Field | Detail |
|---|---|
| **English / Chinese** | China Government Bond yield curve / 中债国债收益率曲线 |
| **Definition** | ChinaBond (CCDC) fits a **Hermite interpolation** model to market-maker quotes from both the exchange and interbank markets, broker quotes, and trade/settlement prices. Sample bonds: Treasury coupon bonds and Treasury discount bonds. Key tenors: 1y, 2y, 3y, 5y, **10y**, 30y |
| **Publisher** | China Central Depository & Clearing Co. (中央国债登记结算有限责任公司, CCDC) — "ChinaBond". The MOF-China Government Bond Yield Curve is a separate, related publication |
| **Frequency / lag** | Daily, end-of-day |
| **Source** | Main curve https://yield.chinabond.com.cn/cbweb-mn/yield_main?locale=en_US ; CGB curve page https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/more?locale=en_US ; **historical data** https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/showHistory?locale=en_US ; MOF curve https://yield.chinabond.com.cn/cbweb-czb-web/czb/moreInfo?locale=en_US&nameType=1 |
| **Series** | CEIC 10y — https://www.ceicdata.com/en/china/pbc--ccdc-treasury-bond-and-other-bond-yield-daily/bond-yield-treasury-bond-10-year (daily, **from March 2006**, ~5,133 obs to Sep 2026) ; Wind `CGB10Y` / `S0059749` ⚠️ unverified |
| **Key levels** | Long-run average **3.266%** (Mar 2006 – Sep 2026); all-time high **4.722% (20 Nov 2013)**; **record low 1.596% (6 Feb 2025)**; ~**1.68%** mid-Aug 2026 and **1.680%** in Sep 2026 |

**The 10y−1y term spread.** Construction: CGB 10y yield − CGB 1y yield, in bp.

**How to read it in a liquidity context — the key interpretive point.** A *flattening/inverting* front end usually means money-market tightness pushing the 1y up; a *steepening* driven by a falling 1y means liquidity easing. But the 2024–25 collapse in CGB yields was **not primarily a liquidity story** — it was an **asset-shortage and growth-expectations story**: excess bank and insurance demand for duration against insufficient safe-asset supply, in an environment of weak nominal growth. That is exactly why the PBoC (i) warned repeatedly on long-bond risk, (ii) **suspended bond buying in January 2025**, and (iii) later resumed in October 2025 "to smooth the yield curve." **Do not treat a falling 10y as evidence of loosening money-market liquidity.** Use the front end (1y–2y) for liquidity; the 10y+ for growth/asset-shortage.

### E.2 10y CGB yield vs the policy rate

**Construction:** `CGB 10y − 7d OMO rate` (the MLF version is dead — see B.3/C.2).

At a 1.40% OMO and a ~1.68% 10y, this spread is ~28bp — historically extremely compressed. **Read:** a very low or negative spread signals (a) entrenched expectations of further easing, (b) severe asset shortage, and (c) a bond market vulnerable to a violent unwind if funding costs rise — because leveraged carry has almost no cushion. **This is the single best "how fragile is the bond market to a funding shock" gauge.** Pair with the O/N repo share (A.8b): compressed carry + >88% overnight share = the 2022-style configuration.

### E.3 Credit spreads

| Indicator | Chinese | Construction | Source |
|---|---|---|---|
| **AAA / AA+ 3y MTN spread** | 中期票据（中票）信用利差 | ChinaBond Medium & Short Term Note (AAA / AA+) 3y yield − CGB 3y yield | ChinaBond curves https://yield.chinabond.com.cn/cbweb-mn/yield_main?locale=en_US ; CEIC MTN family https://www.ceicdata.com/en/china/pbc--ccdc-treasury-bond-and-other-bond-yield-daily/bond-yield-medium--short-term-note-aaa-5-year |
| **Urban investment bond spread** | 城投债信用利差 | LGFV bond yield − CGB, by province and rating; also the province-level dispersion | ChinaBond / Wind; academic literature on the implicit-guarantee component |
| **Indices** | | ChinaBond publishes ~1,000 yield curves across ratings; cbonds mirrors e.g. AAA corporate 5y https://cbonds.com/indexes/87207/ | ChinaBond indices https://yield.chinabond.com.cn/cbweb-mn/indices/multi_index_query?locale=en_US |

**Anchors:** ChinaBond Medium & Short Term Note (AAA) 5y hit a **record low 1.793% in January 2025** and was **1.976% on 21 January 2026**. 2025 primary market saw AAA/AA+ MTNs printing at record-low coupons (e.g. 1.93–1.99%).

**Read in a liquidity frame.** Chinese credit spreads are only partly credit — a large component is **liquidity and leverage**. Spreads compress when leveraged carry is being added (abundant cheap repo) and gap wider in funding squeezes, because credit bonds are the *least* repo-able collateral (they are excluded from DR-eligible interest-rate-bond collateral entirely). So **a widening AAA-3y MTN spread with a stable DR007 is a leverage-unwind signal**, not a credit-quality signal. For **城投债**, remember that the spread is heavily contaminated by the implicit-guarantee component, which repricing on policy news dominates; use it for *policy* risk and for provincial dispersion, not for system liquidity.

### E.4 CDB (policy bank) bonds and the CDB–CGB spread

| Field | Detail |
|---|---|
| **English / Chinese** | China Development Bank bonds / 国开债; policy financial bonds / 政策性金融债 |
| **Definition** | Quasi-sovereign bonds from CDB, EximBank and ADBC. Together with CGBs they make up >65% of the Bloomberg China Aggregate Index |
| **Source** | ChinaBond curves (a separate CDB/policy-bank curve is published) https://yield.chinabond.com.cn/cbweb-mn/yield_main?locale=en_US |

**Why the CDB–CGB spread is a *liquidity/tax* gauge, not a credit gauge.**
1. **Tax:** CGB coupon income is tax-exempt for most onshore institutional holders; CDB bonds are **fully taxable**. So the raw CDB−CGB spread is mostly the **tax wedge** (historically the bulk of it), plus a small credit/liquidity residual.
2. **Liquidity:** CDB bonds are *more* liquid than CGBs in secondary trading for many maturities — policy-bank bonds trade around **RMB 364bn (~USD 56bn) daily** — and are the preferred instrument for **leveraged** and **trading** accounts, precisely because there is no tax benefit to holding them to maturity. CDB bonds are treated by many institutions as the practical risk-free benchmark.
3. Therefore: after adjusting for the statutory tax rate, the residual **tax-adjusted CDB−CGB spread is a clean read on relative liquidity preference and on who is at the margin** — a narrowing tax-adjusted spread means trading/leveraged accounts are dominant (risk-on, carry building); a widening one means buy-and-hold (banks, insurers) are dominant and trading liquidity is thinning.

⚠️ The exact effective tax adjustment (statutory rate, VAT treatment, investor-mix weighting) differs across houses. State your assumption.

### E.5 Bond market turnover

**Definition:** cash-bond (现券) turnover in the interbank market, by instrument type (CGB, policy bank, NCD, credit) and by investor type.
**Publisher/freq:** CFETS/NIFC daily and monthly; CCDC and SHCH settlement statistics.
**Source:** https://www.ceicdata.com/en/china/national-interbank-funding-centre-nibfc-interbank-bond-turnover
**Read:** turnover collapse alongside widening bid-offer is the classic market-liquidity-evaporation signature. Investor-type breakdowns (who is buying/selling) are the highest-value cut — funds and WMPs as net sellers is the E.6 trigger. ⚠️ The detailed investor-type flow tables are mostly a paid Wind/CFETS product.

### E.6 Wealth management product (银行理财) AUM flows — the NBFI liquidity driver

| Field | Detail |
|---|---|
| **English / Chinese** | Bank wealth management products / 银行理财产品 |
| **Definition** | Outstanding AUM of bank and bank-WM-subsidiary wealth management products; plus net subscription/redemption flows |
| **Publisher / freq** | Banking Wealth Management Registration & Depository Center (银行业理财登记托管中心) — semi-annual *Chinese Banking Wealth Management Market Report*; higher-frequency estimates from Puyi/Wind |
| **Release lag** | Semi-annual report ~3–4 weeks after period end (2025 annual published 23–24 Jan 2026) |
| **Source** | Registration Center reports, summarised at https://english.www.gov.cn/archive/statistics/202504/22/content_WS680737d1c6d0868f4e8f1f61.html ; https://en.people.cn/n3/2026/0124/c90000-20418284.html |

**Levels (confirmed):**

| Date | WMP AUM |
|---|---|
| End-2025 | **RMB 33.29trn** (+11.15% YTD); 143mn investors (+14.37%); 33,400 new products raising RMB 76.33trn |
| Mar 2026 | RMB 31.9trn |
| Jun 2026 (H1) | **RMB 33.66trn** (+1.11% YTD); H1 2026 average yield 2.05% |

**The 2022 redemption spiral — the canonical case study.** Mechanism, step by step:
1. Post-2018 asset-management rules forced WMPs to **mark to market** (net-value products), removing the old smoothed "expected return" cushion.
2. In November 2022, a bond sell-off (triggered by the Covid-reopening steps and property support) pushed WMP NAVs below par — **7,722 of 13,582 products (59.3%) fell below par** within a week; 1,689 recorded losses by mid-November.
3. Retail investors redeemed. WMPs and mutual funds had to sell bonds to meet redemptions — **a record RMB 1.3trn (USD 186bn) of interbank bonds sold in November 2022**.
4. Selling pushed yields up further (some bonds +70bp), pushing more NAVs below par → more redemptions. A self-reinforcing spiral.
5. It transmitted to *money markets* because WMPs are large repo cash **takers** and, when stressed, forced sellers: the R−DR spread widened, credit spreads gapped, and regulators asked banks to report on short-term liquidity capacity.

**Monitoring rules:** (i) WMP AUM *level* is a slow structural series; (ii) the fast signal is the **share of products below par (破净率)** and **weekly net subscription flows** (Puyi/Wind, ⚠️ not an official free series); (iii) the tradeable early warning is **R007−DR007 + AAA-3y MTN spread widening together while DR007 is stable** — that is a forced-seller signature, not a policy signature. The PBoC's June 2026 study of a **macro-prudential liquidity support tool for NBFIs** is a direct policy response to exactly this channel.

### E.7 Equity market: margin financing and turnover

| Field | Detail |
|---|---|
| **English / Chinese** | Margin financing and securities lending balance / 融资融券余额 (the financing leg alone: 融资余额) |
| **Publisher / freq** | SSE and SZSE (and BSE), **daily**, published after close |
| **Source** | SSE/SZSE margin trading statistics pages; widely mirrored |

**Levels (confirmed):**

| Date | Balance |
|---|---|
| 2015 peak | RMB 2.27trn |
| 11 Aug 2025 | RMB **2.0122trn** — first time above RMB 2trn in a decade |
| 1 Sep 2025 | RMB 2.29trn — new record, above the 2015 peak |
| May 2026 | RMB **2.83trn** (USD 416bn) — record |

**Read.** Margin balance is an equity-leverage and risk-appetite gauge that matters for money markets through two channels: (i) brokers fund margin books partly in the repo market, so a rapidly rising margin balance adds to repo demand and to the GC007 bid; (ii) it is a sentiment cross-check on whether cheap funding is being channelled into risk assets. **Always scale it:** margin at RMB 2.83trn is only **~2.3% of free-float market cap**, versus **~4.7%** at the 2015 peak — the absolute record is much less alarming than it looks. Use margin/float-cap, not the raw level.

### E.8 Money market fund AUM and yields

| Field | Detail |
|---|---|
| **English / Chinese** | Money market funds / 货币市场基金; Yu'ebao / 天弘余额宝 |
| **Publisher / freq** | AMAC (中国证券投资基金业协会) monthly fund-industry statistics for aggregate MMF AUM; daily 7-day annualised yields from fund companies |
| **Source** | Tianhong Yu'ebao https://www.thfund.com.cn/en/yuebao.html ; CEIC Yu'ebao yield series https://www.ceicdata.com/en/china/yue-bao-fund-yield/cn-fund-yield-7day-avg-annualized-monetary-yue-bao |

**Yu'ebao 7-day annualised yield (confirmed):**

| Date | Yield |
|---|---|
| Jan 2024 | 2.39% |
| End-Dec 2024 | 1.24% (−48% over the year) |
| 2 May 2026 | 0.999% (AUM >RMB 700bn / ~USD 103bn; 789mn accounts) |
| May 2026 | **0.88% — record low since the 2013 launch** |
| 11 Jun 2026 | 0.836% |

**Read.** MMF yields are a **lagging, smoothed** mirror of money-market rates (MMFs hold repo, NCDs and short bonds, so the yield is a ~60-day moving average of DR/NCD). Their value is different: **MMF AUM flows are a genuine liquidity driver**. MMFs are the largest structural repo **cash providers** into the non-bank complex, so rising MMF AUM loosens non-bank funding (compresses R−DR) and falling AUM tightens it. The 2026 sub-1% Yu'ebao yield is also a *behavioural* signal — it drives retail money out of MMFs into short-duration bond funds and WMPs, which increases NBFI duration risk and the fragility documented in E.6. ⚠️ Aggregate China MMF AUM level for 2026 not verified in this pass.

### E.9 Onshore–offshore: CNH HIBOR, the CNH–CNY basis, and CIP deviations

**(a) CNH HIBOR**

| Field | Detail |
|---|---|
| **English / Chinese** | CNH Hong Kong Interbank Offered Rate / 离岸人民币香港银行同业拆息 |
| **Definition** | Estimated offer rates at which CNH deposits for the contract period are quoted to prime banks in the Hong Kong interbank market **at 11:00 a.m.** HK time |
| **Publisher** | **Treasury Markets Association (TMA)**, Hong Kong — TMA administers CNH HIBOR (and HONIA). (HKAB administers HKD HIBOR, a different benchmark — do not conflate) |
| **Frequency / lag** | Each HK business day, 11:00 fixing |
| **Source** | TMA benchmark pages (tma.org.hk); HKMA https://www.hkma.gov.hk/ ; the 26 Sep 2025 RMB Liquidity Facility enhancement circular https://brdr.hkma.gov.hk/eng/doc-ldg/docId/getPdf/20250926-4-EN/20250926-4-EN.pdf |
| **History** | First CNH HIBOR fixing rolled out in Hong Kong in 2013 ⚠️ exact date unverified |

**Read.** **O/N and 1W CNH HIBOR are the offshore yuan liquidity / FX-defence gauge.** Because the offshore CNH pool is small and finite, the PBoC (or Chinese state banks acting on its behalf) can squeeze offshore liquidity to make shorting CNH prohibitively expensive. A spike in O/N CNH HIBOR from low-single-digits to double digits is an unambiguous **yuan-defence intervention signal**, not a liquidity accident. Documented history: repeated O/N HIBOR spikes — nearly threefold in Q1 2015 — as CNH payment demand outran the CNH asset pool, and a major squeeze in 2016.

**Institutional note:** the HKMA's **RMB Liquidity Facility** (enhanced 26 Sep 2025) prices at *the average of the most recent 3 TMA overnight CNH HIBOR fixings, inclusive of same day, plus 25bp, subject to a minimum of 0.25%* — so the facility rate is itself a published ceiling-ish reference for offshore O/N funding and is worth tracking alongside the fixing.

| O/N CNH HIBOR | Read (judgemental) |
|---|---|
| < 3% | Normal, ample offshore liquidity |
| 3–6% | Watch — offshore tightening |
| 6–15% | Active squeeze / defence |
| > 15% | Acute defence episode |

**(b) CNH–CNY spread**

`USDCNH − USDCNY` in pips. Positive (CNH weaker) = offshore depreciation pressure and/or offshore liquidity tightness; the PBoC's response function is to squeeze CNH funding, which shows up in (a). Typical spread on the order of **50–200bp** of rate-equivalent divergence, driven by capital controls that segment the two pools, plus liquidity differences. The PBoC's intervention has materially more influence onshore than offshore.

**(c) FX swap implied CNY rate / CIP deviation**

**Construction:** from USDCNY spot and forward points, back out the implied CNY rate given USD rates: `implied CNY rate ≈ USD rate − (forward points / spot) × (360/days)`. Compare to onshore DR007/SHIBOR/NCD of matching tenor. The gap is the **CIP deviation**.

**Read.** In a fully open market the deviation would be ~zero. In China it is not, and the literature attributes onshore forward-market CIP deviations principally to **conversion/convertibility restrictions in the spot market** rather than to credit risk or liquidity constraints. Practical use:
- A **widening deviation with implied CNY rates below onshore rates** means the market is paying up for USD and/or expects depreciation — a *funding* and *sentiment* gauge.
- It is the correct rate for any offshore investor computing hedged carry into CGBs, and swings in it drive foreign demand for NCDs and short CGBs — a real, if second-order, onshore liquidity channel.
- ⚠️ Because of the convertibility wedge, do **not** interpret Chinese CIP deviations the way you would a DM cross-currency basis. There is no arbitrage force that closes it.

---

## F. Composite / derived indicators

### F.1 Published liquidity/stress indices — what actually exists

| Candidate | Status |
|---|---|
| **CFETS "iDeal" liquidity index** | ⚠️ **Could not verify that this exists.** CFETS operates **iDeal** (its trading/communication terminal) and **iData** (multi-dimensional data-mining products covering the interbank FX, money and bond markets, with sub-market volume/price trends, institutional behaviour analysis and performance analysis). CFETS publishes benchmarks — RMB central parity, SHIBOR, LPR, CFETS RMB Index, bond indices, yield curves — but **no publicly documented money-market liquidity index** was found. Do not cite one. See https://www.chinamoney.com.cn/english/ausbas/ |
| **ChinaBond indices** | Real and usable: ChinaBond publishes ~1,000 yield curves and a large index family, including liquidity-adjusted curve estimates. https://yield.chinabond.com.cn/cbweb-mn/indices/multi_index_query?locale=en_US |
| **Academic CISS-type indices for China** | Exist in the literature (Holló-style Composite Indicator of Systemic Stress applied to China across five segments: financial intermediaries, money markets, equity, bond, FX). Money-market components typically use a TED-style spread and GARCH volatility of the 1-month interbank rate. Not published in real time; useful as methodology |
| **Text-based financial risk indicators for China** | Emerging academic literature (news-text-based indicators) — research-grade only |
| **Sell-side liquidity indices** | Every major house runs one (CICC, CITIC, Huatai, GS, Nomura, and the "excess liquidity"/"超储率 nowcast" trackers). ⚠️ Proprietary; construction differs; do not treat as comparable across houses |
| **OFR-style official index** | No PBoC or NFRA equivalent is published |

**Conclusion: there is no authoritative published China money-market liquidity index. Build your own.**

### F.2 A simple composite liquidity index — recommended construction

**Design principles:** (i) all components signed so that **higher = tighter**; (ii) mix price *and* quantity so the index cannot be gamed by a single administered rate; (iii) z-score on a rolling window, not a fixed history, because the regime changed in 2024–26; (iv) exclude quarter-end dates or dummy them.

```
CLI_t  =  w1 · z(DR007 − OMO7d)
        + w2 · z(R007 − DR007)
        + w3 · z(NCD1Y_AAA − OMO7d)
        − w4 · z(excess reserve ratio, nowcast)
        − w5 · z(duration-weighted net PBoC injection, 4-week rolling sum)

Suggested weights:  w1 = 0.30, w2 = 0.25, w3 = 0.20, w4 = 0.15, w5 = 0.10
```

**Notes on each term**
- **w1 (DR007−OMO):** the core. Highest weight because it is the cleanest and the PBoC's own target variable.
- **w2 (R−DR):** the non-bank/leverage dimension. Critically, it captures stress that never reaches DR007.
- **w3 (NCD−OMO):** the term/bank-liability dimension; **replaces the dead NCD−MLF spread** (B.3).
- **w4 (超储率, sign −):** the stock of liquidity, not its price. Use the **monthly nowcast** (B.6); the quarterly official print is too laggy. Negative sign: higher excess reserves = looser.
- **w5 (net injection, sign −):** the policy-reaction dimension, duration-weighted per C.9. Use a 4-week rolling sum to damp daily noise. Negative sign: more injection = looser. Lowest weight because it is partly *endogenous* — the PBoC injects **because** conditions are tight, so it is a contemporaneous offset, not an independent signal. Some houses drop it entirely for this reason; that is defensible.

**Estimation window:** rolling 3 years is the usual compromise, but note the **June 2026 corridor narrowing** structurally compressed w1's variance. Either (a) re-estimate the w1 z-score on post-June-2026 data only once ~12 months are available, or (b) normalise (DR007−OMO) by the corridor half-width (25bp now, 35bp before) rather than by a rolling sd. Option (b) is cleaner and I recommend it.

**Bands (judgemental):**

| CLI | Read |
|---|---|
| < −1.0 | Very loose |
| −1.0 to +0.5 | Normal |
| +0.5 to +1.5 | Watch |
| > +1.5 | Stress |
| > +2.5 | Acute |

**Validation:** back-test against the known episodes — Jun 2013, Q4 2016–2017, Nov–Dec 2022, and the quarter-ends. If it does not light up in Nov 2022, your w2 is too low.

---

## G. Recommended dashboard — the headline 12

Signs are stated as **"+ = tighter"** throughout (so every series points the same way and can be summed).

| # | Indicator | Chinese | Transformation | Sign | Normal | Watch | Stress | Freq | Why it earns its place |
|---|---|---|---|---|---|---|---|---|---|
| **1** | **DR007 − 7d OMO** | DR007 与 7天逆回购利差 | Level, bp; 5d MA; ex-quarter-end | **+ = tighter** | −10 to +10bp | +10 to +30bp | >+30bp | Daily | The PBoC's own target variable. Collateralised, bank-only, interest-rate-bond collateral — the least contaminated read on settlement-balance scarcity |
| **2** | **R007 − DR007** | R007 与 DR007 利差 | Level, bp; 5d MA; separate quarter-end series | **+ = tighter** | 0–15bp | 15–40bp | >40bp (>80bp acute) | Daily | Catches non-bank/leverage stress that never touches DR007. Best single early warning of a 2022-style unwind |
| **3** | **1Y AAA joint-stock NCD − 7d OMO** | 1年期AAA股份行同业存单与政策利率利差 | Level, bp | **+ = tighter** | 0–25bp | 25–50bp | >50bp | Daily | The price of marginal bank *term* funding. Replaces the dead NCD−MLF spread. Leads RRR-cut decisions |
| **4** | **Excess reserve ratio (nowcast)** | 超储率（月度测算） | Level, %; nowcast monthly, calibrated to quarterly official | **− = tighter** (i.e. lower ratio = tighter) | 1.3–2.0% | 1.0–1.3% | <1.0% | Monthly (official quarterly) | The *stock* of liquidity. The only indicator that says how much cushion exists rather than what it costs |
| **5** | **Duration-weighted net PBoC injection** | 央行净投放（久期加权） | 4-week rolling sum, RMB bn; weight by tenor per C.9 | **− = tighter** (more injection = looser) | ±500bn | — | Large sustained drain | Daily→weekly | The supply side, correctly aggregated across OMO + O/N OMO + MLF + outright RR + PSL + bond buying + treasury cash + RRR |
| **6** | **Overnight share of repo turnover** | 隔夜回购成交占比 | %, 5d MA | **+ = more fragile** | <80% | 80–88% | >88–90% | Daily | The purest "crowded carry" gauge. High share = the whole system is one bad funding day from a forced unwind |
| **7** | **Pledged repo turnover** | 质押式回购成交量 | Ratio to trailing 250d median (NOT a fixed RMB level) | **+ = more leverage** | 0.85–1.15× | 1.15–1.30× | >1.30× | Daily | Direct read on rolled leverage. Must be normalised — the old 7–8trn threshold is stale |
| **8** | **Fiscal deposits at the PBoC, m/m change** | 财政存款环比变化 | RMB bn, m/m; seasonally-aligned to tax calendar | **+ = tighter** (rise = drain) | ±300bn | +500–800bn | >+1trn in a tax month | Monthly | The largest China-specific autonomous driver. Jan/Apr/May/Jul/Oct drain; December release |
| **9** | **Net government bond settlement** | 国债+地方债净缴款 | Weekly net, RMB bn, forward calendar | **+ = tighter** | <200bn/wk | 200–400bn/wk | >400–500bn/wk | Weekly (forward-looking) | The only genuinely *forward-looking* item on this list. A supply calendar you can build 4 weeks ahead |
| **10** | **CGB 10y − 7d OMO** | 10年国债与政策利率利差 | Level, bp | **− = more fragile** (compressed = fragile) | >80bp | 40–80bp | <30bp | Daily | Measures how little cushion leveraged carry has. Compressed spread + high O/N share = maximum fragility |
| **11** | **3y AAA MTN − 3y CGB spread** | 3年AAA中票信用利差 | Level, bp; and 20d change | **+ = tighter** | Stable | +15bp/20d | +30bp/20d | Daily | Credit bonds are the least repo-able collateral, so they gap first in a forced-seller event. Distinguishes leverage unwind from policy tightening |
| **12** | **O/N CNH HIBOR** | 离岸人民币隔夜拆息 | Level, %; and spike flag | **+ = tighter/defence** | <3% | 3–6% | >6% | Daily | The offshore liquidity and FX-defence gauge. Independent information: onshore can be loose while offshore is being deliberately squeezed |

**Two things deliberately NOT in the top 12, and why:**
- **SHIBOR O/N and 1W** — quoted, not transacted; strictly dominated by DR001/DR007. Keep **3M SHIBOR** on a second-tier panel only.
- **GC007 level** — its holiday/quarter-end kurtosis would swamp the dashboard. Keep **GC007 − R007 at quarter-ends** as a dedicated quarter-end segmentation gauge instead.

**Second-tier panel (worth a page, not the front page):** DR001, R001, IBO007−R007 (unsecured-secured spread), 3M SHIBOR − 3M NCD, NCD net issuance and success rate, GC007−R007 at quarter-ends, tax-adjusted CDB−CGB spread, WMP below-par ratio and weekly flows, margin balance / free-float market cap, MMF AUM flows, currency in circulation (CNY-aligned), FX position (regime-change watch), LCR/NSFR, CIP deviation / FX-swap implied CNY rate.

---

## H. Known gaps and things to verify before production use

1. **Exact publication times** for DR/R fixings, SHIBOR and the PBoC OMO announcement — all ⚠️ unverified here.
2. **History start dates** for R007/R001, IBO series, FR/FDR fixings, and CNH HIBOR — ⚠️ unverified.
3. **Wind tickers** throughout — I have given the conventional forms but flagged them unverified. Confirm in the terminal; CEIC URLs given are verified entry points.
4. **NCD issuance success rate** — no confirmed official aggregate series; it is a derived desk metric.
5. **PSL monthly path for 2025–26** — only Dec 2023/Jan 2024 confirmed here.
6. **Aggregate China MMF AUM 2026** — not verified.
7. **The inferred overnight OMO rate (1.25%)** — reported via sources; the PBoC does not publish it. Any time series of this rate is an inference.
8. **All threshold bands marked "judgemental"** are strategist calibration. They should be re-estimated empirically, and specifically **re-estimated on post-June-2026 data** for anything involving DR007 volatility, because the corridor narrowed from 70bp to 50bp.
9. **Primary-source pages were not rendered** in this research pass (egress blocked). Open each URL once before building a scraper.

---

## Sources

**PBoC — concepts, operations, reports**
- DR007 definition (PBoC, EN): https://www.pbc.gov.cn/en/3688006/3689169/3753752/index.html
- PBoC Monetary Policy Reports (EN index): https://www.pbc.gov.cn/en/3688229/index.html
- PBoC financial statistics: https://www.pbc.gov.cn/en/3688247/3688978/3709137/5870352/index.html
- PBoC open market operations (EN): https://www.pbc.gov.cn/en/3688241/3688765/index.html
- Treasury cash management tender results (Issue 13, 2025): https://www.pbc.gov.cn/en/3688241/3688765/3688753/2026010414034515582/index.html
- Treasury cash management tender results (Issue 14, 2025): https://www.pbc.gov.cn/en/3688241/3688765/3688753/2026010414084370345/index.html
- PBoC structural monetary policy instruments (incl. PSL): http://www.pbc.gov.cn/en/3688229/3688335/4738114/5241677/index.html
- China Monetary Policy Report Q1 2026 (CN PDF mirror): https://jrj.sh.gov.cn/cmsres/5a/5ae23d4703d4409b8c2b2c325c40b774/b0233b6bfdbe3826e365a66f35d86f83.pdf
- China Monetary Policy Report Q4 2025 (CN PDF mirror): https://cif.mofcom.gov.cn/cif/html/upload/20260211143114167_2025%E5%B9%B4%E7%AC%AC%E5%9B%9B%E5%AD%A3%E5%BA%A6%E4%B8%AD%E5%9B%BD%E8%B4%A7%E5%B8%81%E6%94%BF%E7%AD%96%E6%89%A7%E8%A1%8C%E6%8A%A5%E5%91%8A.pdf
- China Monetary Policy Report Q3 2025 (CN PDF mirror): https://cif.mofcom.gov.cn/cif/html/upload/20251124101800795_%E4%B8%AD%E5%9B%BD%E8%B4%A7%E5%B8%81%E6%94%BF%E7%AD%96%E6%89%A7%E8%A1%8C%E6%8A%A5%E5%91%8A2025%E5%B9%B4%E7%AC%AC%E4%B8%89%E5%AD%A3%E5%BA%A6.pdf
- China Monetary Policy Report Q2 2026 (summary): https://jrj.sh.gov.cn/ZXYW178/20260813/1b25ff83c27549d3af0244230130f351.html
- Pan Gongsheng, "The evolution of financial structure and the modernization of financial markets in China" (BIS Review, Jun 2026): https://www.bis.org/review/r260622q.htm
- Yi Gang, "China's monetary policy framework" (BIS Review, 2019): https://www.bis.org/review/r190130b.htm

**CFETS / NIFC / SHIBOR — money market benchmarks**
- CFETS fixing repo rates (EN): https://iftp.chinamoney.com.cn/english/bmkfrr/
- CFETS 回购定盘利率 FR007/FDR007 (CN): https://www.chinamoney.com.cn/chinese/bkfrr/
- CFETS SHIBOR page: https://www.chinamoney.com.cn/chinese/bkshibor/
- SHIBOR official site: https://www.shibor.org/ ; panel banks https://www.shibor.net.cn/shibor/panelbanks/ ; code of conduct https://www.shibor.sh.cn/shibor/codeofconduct/
- CFETS business and services (incl. iData): https://www.chinamoney.com.cn/english/ausbas/
- DR007 history start (15 Dec 2014): https://baike.baidu.com/item/DR007/67909401

**ChinaBond / CCDC — curves and indices**
- ChinaBond yield curves: https://yield.chinabond.com.cn/cbweb-mn/yield_main?locale=en_US
- CGB yield curve and others: https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/more?locale=en_US
- ChinaBond historical data: https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/showHistory?locale=en_US
- MOF–China Government Bond Yield Curve: https://yield.chinabond.com.cn/cbweb-czb-web/czb/moreInfo?locale=en_US&nameType=1
- ChinaBond indices: https://yield.chinabond.com.cn/cbweb-mn/indices/multi_index_query?locale=en_US
- ChinaBond Corporate Bond Yield Curve (AAA) 5Y mirror: https://cbonds.com/indexes/87207/

**Exchange repo**
- SSE GC007 (204007): https://www.sse.com.cn/assortment/bonds/repo/repoinfo/basic/index.shtml?BOND_CODE=204007
- SSE bond repo hub: https://www.sse.com.cn/assortment/bonds/repo/
- GC001/GC007 vs FR001/FR007 mechanics and the Thursday effect: https://www.zhihu.com/question/23220456/answer/24541646
- 国债逆回购 practitioner Q&A (China Securities Journal): https://www.cs.com.cn/gppd/zqxw/201712/t20171228_5644765.html

**2024–2026 policy-tool changes**
- Outright reverse repo introduced (gov.cn, 28 Oct 2024): https://english.www.gov.cn/news/202410/28/content_WS671f2a63c6d0868f4e8ec5d2.html
- Outright reverse repo, first operation and rationale (Yicai): https://www.yicaiglobal.com/news/chinas-central-bank-introduces-new-monetary-tool-to-manage-liquidity
- Outright reverse repo, Oct 2024 CNY500bn: https://money.usnews.com/investing/news/articles/2024-10-31/chinas-central-bank-conducts-500-billion-yuan-of-outright-reverse-repos-in-october
- Outright reverse repo series: https://tradingeconomics.com/china/outright-reverse-repo
- CNY1trn outright reverse repo (Aug 2026): http://english.scio.gov.cn/pressroom/2026-08/14/content_118647130.html
- CNY500bn outright reverse repo (Aug 2026): http://www.ecns.cn/cns-wire/2026-08-05/detail-ihfhziqh0061381.shtml
- CNY1trn outright reverse repo (Sep 2025): https://english.www.gov.cn/news/202509/05/content_WS68ba20cbc6d0868f4e8f558c.html
- 3M outright reverse repo shifts to equal-amount rollover: https://www.archyde.com/pboc-shifts-to-equal-amount-rollover-for-3-month-outright-reverse-repos/
- MLF multiple-price bidding, loss of policy-rate role (Yicai): https://www.yicaiglobal.com/news/pbocs-mlf-no-longer-has-policy-oriented-role-after-removal-of-unified-price-bidding-system-expert-says
- MLF tweak (Central Banking): https://www.centralbanking.com/central-banks/monetary-policy/operating-framework/7972581/pboc-tweaks-lending-facility-as-framework-reform-continues
- MLF operations (gov.cn examples): https://english.www.gov.cn/news/202605/22/content_WS6a10675ec6d00ca5f9a0b307.html ; https://english.www.gov.cn/news/202507/24/content_WS688232d0c6d0868f4e8f468b.html ; https://english.www.gov.cn/news/202512/24/content_WS694bcfb0c6d00ca5f9a0842f.html ; https://english.www.gov.cn/news/202411/25/content_WS6743e845c6d0868f4e8ed621.html
- MLF Aug 2026 net drain, balance 7.4trn (Sina): https://finance.sina.com.cn/roll/2026-08-25/doc-inippvuq2340640.shtml
- MLF series: https://tradingeconomics.com/china/liquidity-injections-via-mlf
- PBoC starts CGB trading (Aug 2024): https://www.business-standard.com/world-news/china-s-central-bank-starts-trading-govt-bonds-to-influence-yield-curve-124083000779_1.html
- Bond-buying suspension (SCIO, Jan 2025): http://english.scio.gov.cn/m/pressroom/2025-01/15/content_117666228.html
- Bond-buying suspension coverage: https://www.cnbc.com/2025/01/10/why-chinas-central-bank-has-stopped-bond-purchases.html ; https://www.centralbanking.com/central-banks/currency/7963600/pboc-suspends-government-bond-purchases ; https://www.scmp.com/economy/china-economy/article/3294282/record-low-yields-prompt-suspension-government-bond-purchases-chinas-central-bank ; https://www.globaltimes.cn/page/202501/1326637.shtml
- Bond trading resumption (Trivium, Nov 2025): https://triviumchina.com/2025/11/05/pboc-resumes-bond-trading-to-smooth-yield-curve/
- Resumption and Oct 2025 net CNY20bn: https://tradingeconomics.com/china/government-bond-yield/news/499143 ; https://tradingeconomics.com/china/government-bond-yield/news/496556
- November 2025 second month of net buying: https://www.yicaiglobal.com/news/central-bank-raises-november-liquidity-injection-to-usd7-billion
- Temporary O/N repo/reverse repo, July 2024: https://www.nomuraconnects.com/focused-thinking-posts/china-a-major-step-to-modernizing-the-pbocs-policymaking/ ; https://www.yicaiglobal.com/news/pbocs-temporary-repo-reverse-repo-operations-to-help-stabilize-market-experts-say
- PBoC studying a narrower corridor (Central Banking, 2024): https://www.centralbanking.com/central-banks/monetary-policy/7962066/pboc-looks-into-narrowing-interest-rate-corridor
- Lujiazui Forum June 2026, six measures incl. ±25bp corridor and O/N reverse repo: https://govt.chinadaily.com.cn/s/202606/18/WS6a4b0053498e23165e070722/pboc-announces-six-financial-policy-measures-at-lujiazui-forum.html ; https://english.www.gov.cn/news/202606/17/content_WS6a324210c6d00ca5f9a0ba94.html ; https://english.pudong.gov.cn/chinashftz/2026-06/18/c_1191665.htm
- Corridor narrowing analysis: https://www.yuantalks.com/pboc-enhances-short-end-interest-rate-control-and-refines-policy-corridor-under-evolving-monetary-framework/ ; https://www.capitaleconomics.com/publications/china-economics-weekly/pboc-narrow-rate-corridor-no-signs-healthier-credit
- Overnight reverse repo debut at 1.25%: https://wtvbam.com/2026/06/29/china-debuts-overnight-reverse-repos-at-1-25-sources-say/ ; https://easternherald.com/2026/06/29/pboc-overnight-reverse-repo-rate-china-monetary-policy-2026/ ; https://cryptobriefing.com/pboc-overnight-reverse-repo-operations/ ; https://cryptobriefing.com/china-pboc-liquidity-injection-reverse-repos/
- 7d OMO at 1.40%, small/zero prints as O/N tool takes over: https://cryptobriefing.com/china-pboc-reverse-repo-injection/ ; https://finance.biggo.com/news/133289e3-abc1-4e72-b95b-7337b28af25e
- SLF rate cuts: https://english.www.gov.cn/news/202407/22/content_WS669e08fdc6d0868f4e8e9555.html ; https://english.www.gov.cn/news/202505/07/content_WS681af03ec6d0868f4e8f250c.html ; https://www.ceicdata.com/en/china/lending-facility/cn-standing-lending-facility-slf-rate-7-day
- RRR cut May 2025 (~CNY1trn): https://english.www.gov.cn/news/202505/07/content_WS681af001c6d0868f4e8f2509.html ; https://english.www.gov.cn/news/202505/15/content_WS68254f59c6d0868f4e8f2902.html ; https://en.people.cn/n3/2025/0516/c90000-20315656.html ; https://www.cnbc.com/2025/05/07/china-to-cut-key-lending-rates-by-10-points-bank-reserve-requirement-ratio-by-50-points-.html
- RRR level series: https://www.ceicdata.com/en/indicator/china/reserve-requirement-ratio ; https://tradingeconomics.com/china/cash-reserve-ratio
- 2026 policy outlook / further RRR-cut signalling: https://english.www.gov.cn/news/202601/22/content_WS69720cd8c6d00ca5f9a08b8c.html ; https://www.scmp.com/economy/china-economy/article/3339018/chinas-central-bank-signals-reserve-ratio-interest-rate-cuts-2026 ; https://www.centralbanking.com/central-banks/monetary-policy/7972834/pboc-cuts-rates-and-lowers-reserve-requirement-ratios
- PSL reactivation and balances: https://www.caixinglobal.com/2024-01-20/preview-of-the-weekly-the-central-bank-releases-mortgage-supplementary-loans-for-the-third-time-supporting-three-major-projects-with-dual-significance-in-policy-signals-102158781.html ; https://www.crugroup.com/knowledge-and-insights/spotlights-blogs/2024/china-props-up-economy-with-targeted-lending/ ; https://www.centralbanking.com/central-banks/financial-stability/7960552/pboc-ramps-up-funding-support-for-policy-banks ; https://www.ceicdata.com/en/china/lending-facility/balance-of-pledged-supplementary-lending-psl ; https://en.macromicro.me/series/30903/china-pboc-mortgage-supplementary-loan-balance
- Fiscal/tax-driven liquidity operations: https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance ; https://www.business-standard.com/amp/article/international/china-s-central-bank-boosts-liquidity-ahead-of-tax-payment-surge-119102300060_1.html

**Bank funding, NCD, reserves, regulation**
- NCD primer (Bond Connect): https://www.chinabondconnect.com/en/Northbound/Services/Ncd-Subscription.html
- NCD market size and role (NBER WP 25549): https://www.nber.org/system/files/working_papers/w25549/w25549.pdf
- Handbook on China's Financial System — Chinese Bond Market: https://bfi.uchicago.edu/wp-content/uploads/2019/03/BFI-WP-2019-Handbook.pdf
- NCD quota increase and Mar 2025 pressure (Sina/CIB fixed income): https://finance.sina.com.cn/stock/stockzmt/2025-03-08/doc-inenwtru9222014.shtml
- NCD rates above MLF, record inversion (Feb 2025): https://finance.sina.com.cn/stock/relnews/cn/2025-02-27/doc-inemxvsc6275585.shtml
- NCD rate inversion commentary: https://www.stcn.com/article/detail/1534411.html ; https://www.stcn.com/article/detail/1055318.html ; https://www.stcn.com/article/detail/1544487.html
- NCD 1Y around 1.45% (2026) and deposit-rate context: https://www.21jingji.com/article/20260321/herald/e33cc8e91ee48c76e367d23ffb482744.html
- NCD issuance >12trn in 5M 2026: https://finance.biggo.com/news/uGV5bp4BaoGGrU-Iwu35 ; https://news.futunn.com/en/post/73781461/interbank-negotiable-certificate-of-deposit-ncd-issuance-is-heating-up
- NCD turnover series: https://www.ceicdata.com/en/china/national-interbank-funding-centre-nibfc-interbank-bond-turnover/cn-turnover-interbank-bond-spot-negotiable-certificate-of-deposit
- NFRA supervisory statistics (LCR 149.25%, NSFR 127.59% Q2 2025): https://www.nfra.gov.cn/en/view/pages/ItemDetail.html?docId=1222165
- Bank of China Pillar 3 Q3 2025: https://pic.bankofchina.com/bocappd/report/202510/P020251028595147627739.pdf
- Global LCR retreat led by China (Risk Quantum): https://www.risk.net/risk-quantum/7963528/china-leads-global-banks%E2%80%99-lcr-retreat-in-2025
- Loan-to-deposit 75% cap removal: https://www.business-standard.com/article/pti-stories/china-removes-75-per-cent-cap-on-loan-to-deposit-ratio-115082900634_1.html
- Banking sector conditions 2025 (AMRO): https://www.amro-asia.org/chinas-banking-landscape-strong-foundations-and-emerging-vulnerabilities
- China Banking Monitor 2025 (BBVA): https://www.bbvaresearch.com/wp-content/uploads/2025/04/China-banking-monitor-2025.pdf
- IMF 2025 Article IV, China: https://www.elibrary.imf.org/view/journals/002/2026/044/article-A001-en.xml
- Excess reserve ratio and reserve system background (Yale): https://elischolar.library.yale.edu/cgi/viewcontent.cgi?article=15460&context=ypfs-documents ; https://newbagehot.yale.edu/docs/china-reserve-requirements-gfc

**MPA / macroprudential**
- China's macroprudential management system (BIS, Nov 2025): https://www.bis.org/speeches/20251110-chinas-macroprudential-management-system-development-practice-and-future-evolution
- MPA framework background (CIGI): https://www.cigionline.org/sites/default/files/documents/Paper%20no164web_0.pdf
- MPA impact on commercial banks: https://www.scirp.org/journal/paperinformation?paperid=75229
- MPA and firms' access to credit: https://www.sciencedirect.com/science/article/abs/pii/S0167268125002306

**Money-market structure, turnover, leverage, stress episodes**
- The Chinese Interbank Repo Market (RBA Bulletin, Jun 2017): https://www.rba.gov.au/publications/bulletin/2017/jun/9.html
- China's Monetary Policy Framework and Financial Market Transmission (RBA Bulletin, Apr 2024): https://www.rba.gov.au/publications/bulletin/2024/apr/chinas-monetary-policy-framework-and-financial-market-transmission.html
- Decoding China's monetary policy machinations (J.P. Morgan AM): https://am.jpmorgan.com/us/en/asset-management/liq/insights/liquidity-insights/china-money-market-resource-centre/decoding-chinas-monetary-policy-machinations/
- Transmission of liquidity shocks via China's segmented money market: https://arxiv.org/pdf/1811.08949
- Interbank volatility in China (BIS Quarterly, Sep 2013): https://www.bis.org/publ/qtrpdf/r_qt1309u.htm
- 2013 liquidity crunch (overnight SHIBOR 13.44%): https://en.wikipedia.org/wiki/Chinese_Banking_Liquidity_Crisis_of_2013
- Repo turnover 4.8trn/day and leverage, Apr 2020: http://www.21jingji.com/2020/4-30/3NMDEzODBfMTU1NjU3NQ.html
- Repo turnover >6trn for 9 sessions, Jun 2022: https://www.chnfund.com/article/AR2022062909511926449831
- Repo turnover >7trn and 90.3% overnight share, Aug 2022: https://m.thepaper.cn/newsDetail_forward_19363821
- High-leverage repo turnover risk commentary, Dec 2021: https://www.cnfin.com/hb-lb/detail/20211201/3470723_1.html
- Interbank pledged repo turnover series: https://www.statista.com/statistics/456767/china-interbank-market-pledged-repo-trading-volume/ ; https://www.ceicdata.com/en/china/national-interbank-funding-centre-nibfc-interbank-bond-turnover
- DR007 turnover series: https://www.ceicdata.com/zh-hans/china/national-interbank-funding-centre-nifc-interbank-bond-collateral-repo-turnover-daily/cn-turnover-interbank-bond-collateral-repo-depository-institution-dr007-7-day
- DR007 vs R007 explainer: https://zhuanlan.zhihu.com/p/710641549 ; https://zhuanlan.zhihu.com/p/63823366
- Interest rate corridor chart/collection: https://en.macromicro.me/collections/31/cn-finance-relative/109608/cn-interest-rate-corridor-new ; https://en.macromicro.me/series/5899/cn-dr007 ; https://keyneswatch.com/cn/shibor
- Financial stress index methodology for China: https://hrmars.com/papers_submitted/27877/assessing-financial-stress-in-china-and-asean-4-economies.pdf ; https://www.sciencedirect.com/science/article/abs/pii/S0261560625002499

**Bond market, credit, NBFI, equity, offshore**
- CGB 10y series, history from Mar 2006, record low 1.596% (6 Feb 2025): https://www.ceicdata.com/en/china/pbc--ccdc-treasury-bond-and-other-bond-yield-daily/bond-yield-treasury-bond-10-year
- CGB 10y 2026 levels: https://tradingeconomics.com/china/government-bond-yield/news/575767 ; https://tradingeconomics.com/china/government-bond-yield
- AAA MTN 5y yields: https://www.ceicdata.com/en/china/pbc--ccdc-treasury-bond-and-other-bond-yield-daily/bond-yield-medium--short-term-note-aaa-5-year
- Policy bank bonds, liquidity and tax treatment: https://www.ubs.com/global/en/assetmanagement/insights/asset-class-perspectives/fixed-income/articles/china-bonds.html ; https://en.saif.sjtu.edu.cn/junpan/FMar_2020/slides_China_Bond.pdf ; https://asianbondsonline.adb.org/china/market-summary/
- China debt market evolution and integration: https://www.sciencedirect.com/science/article/pii/S0927538X25000885
- WMP 2022 redemption spiral: https://www.scmp.com/business/banking-finance/article/3199994/sell-offs-chinese-wealth-management-products-amplify-bond-rout-while-banks-scramble-calm-investors ; https://www.bloomberg.com/news/articles/2022-12-19/chinese-funds-dump-record-amount-of-bonds-amid-redemptions ; https://www.bloomberg.com/news/articles/2022-11-17/china-asks-banks-to-report-on-liquidity-after-bond-slump ; https://caixinchinawatch.substack.com/p/cx-daily-behind-the-massive-sell
- WMP market fragility research: https://www.sciencedirect.com/science/article/pii/S0927539826000319
- WMP AUM 2025/2026: https://en.people.cn/n3/2026/0124/c90000-20418284.html ; https://english.news.cn/20260123/506c548f773142a5bdf9e2d75c0ef9bb/c.html ; https://www.caixinglobal.com/2026-01-24/china-wealth-management-market-hits-48-trillion-despite-yield-drop-102407442.html ; https://www.caproasia.com/2026/07/29/china-wealth-management-products-increased-5-7-to-5-trillion-cny-33-7-trillion-in-2026-june-from-4-7-trillion-cny-31-9-trillion-aum-in-2026-march/ ; https://english.www.gov.cn/archive/statistics/202504/22/content_WS680737d1c6d0868f4e8f1f61.html
- Margin financing records: https://www.yicaiglobal.com/news/margin-financing-on-shanghai-shenzhen-bourses-surges-past-usd275-billion-to-hit-10-year-high ; https://money.usnews.com/investing/news/articles/2025-09-02/chinas-stock-margin-financing-hits-record-high-as-investors-chase-rally ; https://www.theasset.com/article/54937/a-share-margin-debt-hits-2-3-trillion-yuan-the-highest-since-2015 ; https://www.caixinglobal.com/2026-05-12/china-stock-margin-trading-hits-record-102443338.html
- Yu'ebao / MMF yields: https://www.thfund.com.cn/en/yuebao.html ; https://www.ceicdata.com/en/china/yue-bao-fund-yield/cn-fund-yield-7day-avg-annualized-monetary-yue-bao ; https://www.yicaiglobal.com/news/worlds-largest-money-market-fund-tianhong-yuebao-pares-yield-to-all-time-low-of-127 ; https://finance.biggo.com/news/6LC2RJ4BX0tZvRTvGsuG ; https://www.caproasia.com/2025/01/02/world-largest-100-billion-money-market-fund-china-ant-group-tianhong-yuebao-7-day-yield-decreased-48-to-1-24-yield-at-end-december-2024-from-2-39-yield-in-january-2024-launched-in-2013-for/
- Local government and special bond issuance 2026: https://www.yicaiglobal.com/news/chinas-2026-local-govt-bond-issuance-hits-usd332-billion-as-infrastructure-push-kicks-off-early ; https://english.www.gov.cn/news/202604/24/content_WS69eb336ac6d00ca5f9a0a9f9.html ; https://www.chinabankingnews.com/p/chinas-government-debt-set-to-grow ; https://en.macromicro.me/series/28914/china-local-government-bond-special-bond-issuance
- CNH HIBOR administration and squeezes: https://www.risk.net/foreign-exchange/2404499/cnh-liquidity-squeeze-drives-hibor-volatility ; https://www.theasset.com/article/20979/banks-start-to-submit-cnh-hibor-to-industry-association ; https://www.structuredretailproducts.com/insights/16643/first-cnh-hibor-fixing-to-be-rolled-out-in-hong-kong
- HKMA RMB Liquidity Facility enhancement (26 Sep 2025): https://brdr.hkma.gov.hk/eng/doc-ldg/docId/getPdf/20250926-4-EN/20250926-4-EN.pdf
- CNH–CNY pricing and CIP: https://www.bis.org/publ/work492.pdf ; https://voxchina.org/show-3-363.html ; https://www.sciencedirect.com/science/article/abs/pii/S0378426614002076 ; https://www.sciencedirect.com/science/article/pii/S1057521924002941 ; https://www.bny.com/assets/corporate/documents/content/iflow-archive/morning-briefing/MB20240808-ChinaCNH-CNYBasis.pdf
- FX position / SAFE: https://www.safe.gov.cn/en/ ; https://en.macromicro.me/collections/31/cn-finance-relative/17671/cn-major-assets-of-pboc-balance-sheets ; https://en.macromicro.me/collections/31/cn-finance-relative/17672/cn-major-liabilities-of-pboc-balance-sheets ; https://keyneswatch.com/cn/balance_sheet
- New toolkit stocktake (BBVA Research, Jul 2025): https://www.bbvaresearch.com/wp-content/uploads/2025/07/202507-Stocktaking-China-new-toolkit-in-its-monetary-policy-framework.pdf
- Six measures commentary: https://www.degroofpetercam.com/en-be/blog/cio-perspectives-china-six-measures
