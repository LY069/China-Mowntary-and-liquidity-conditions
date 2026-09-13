# 06 — Implications: Reading China's Monetary & Liquidity Conditions into Growth, Inflation and Policy

**Purpose.** Colleagues are cataloguing *what* the indicators are. This note is the **transmission and interpretation layer**: for each indicator, the causal chain to activity and prices, the lead/lag, the level/change heuristics, what it does to the PBoC's reaction function, and when it lies.

**Vintage:** 12 September 2026. Data references are to the latest prints available as of this date.

---

## Evidence labelling convention

Every non-trivial claim below carries one of:

| Tag | Meaning |
|---|---|
| **[E]** | Empirically documented relationship with a citation in the Sources section |
| **[P]** | Standard practitioner heuristic — widely used on desks, not formally estimated, or estimated by sell-side without published methodology |
| **[J]** | My own judgement / inference — reasoned from the mechanism and the cited data, not itself a documented result |

**Method note and evidence-quality caveat.** Direct page retrieval (WebFetch) was blocked by this environment's network egress proxy for essentially every source domain attempted — imf.org, elibrary.imf.org, bis.org, pbc.gov.cn, uscc.gov, tradingeconomics.com, newyorkfed.org, think.ing.com and others. The grounding below therefore rests on **web-search result summaries plus their URLs**, not on full-text reads of the primary documents. Figures are attributed to the source that surfaced them and should be **re-verified against the primary document before external publication**. Where a number is well known to me but could not be re-verified in this session, it is marked *[unverified in-session]* rather than asserted. No statistic or citation here is invented; where I could not stand up a number, I say so and reason qualitatively instead.

---

## 0. The configuration right now — and why the standard China deflation note is out of date

The framing most desks carried through 2024–25 was: *nominal easing, deflation, rising real rates, broken transmission*. Half of that has now changed, and the half that changed is the half most notes have not updated.

**What has changed [E]:**

- The **GDP deflator turned positive in Q2 2026 at +1.6%**, ending **12 consecutive negative quarters**; Q1 2026 was about −0.1%. Nominal GDP growth rose to **5.9%** in Q2 2026. ([China Daily HK](https://www.chinadailyhk.com/hk/article/636329); [China.org.cn](http://www.china.org.cn/2026-07/13/content_118596094.shtml); [BigGo Finance](https://finance.biggo.com/news/c1efd22b-d31b-48d1-8e4b-4dbf158e5642))
- **PPI has reflated hard**: +4.1% y/y in Q2 2026, a near four-year high, and **+3.8% y/y in August 2026** ([TrendForce DataTrack](https://datatrack.trendforce.com/blog/content/60585/chinas-q2-2026-ppi-yoy-growth-rises-to-41-ending-deflation-and-hitting-a-nearly-four-year-high); [CNBC, 9 Sep 2026](https://www.cnbc.com/2026/09/09/china-cpi-ppi-august-oil-prices-tech-manufacturing-.html)).
- **CPI +0.8% y/y in August 2026** (July +0.5%), **core +1.0%** (July +0.9%) ([CNBC](https://www.cnbc.com/2026/09/09/china-cpi-ppi-august-oil-prices-tech-manufacturing-.html)).
- **The FX constraint has inverted.** CNY has traded through 7.00 and the CFETS basket is up ~4.8% YTD, with the PBoC showing little resistance to appreciation — in sharp contrast to its resistance to depreciation in prior years ([ING](https://think.ing.com/articles/cny-at-a-glance-tightening-our-forecast-band-for-2h26/); [ING](https://think.ing.com/articles/cny-at-a-glance-whats-next-as-the-cny-moves-below-the-critical-7-threshold/)).

**What has *not* changed, and has in places got worse [E]:**

- **Credit is the weakest on record.** TSF stock growth was **7.4% y/y in June 2026 — the slowest on record**, versus a ~13% average in the five pre-COVID years. RMB loans to the real economy were **+5.6%** (RMB 276.9tn) while **government bonds were +15.6%** (RMB 99.37tn) ([USCC China Bulletin, 23 Jul 2026](https://www.uscc.gov/trade-bulletins/china-bulletin-july-23-2026); [CGTN](https://news.cgtn.com/news/2026-05-14/China-s-April-total-social-financing-grows-at-7-8--1N8P0FFSzC0/p.html)).
- **Demand-side activity is decelerating.** Q2 2026 real GDP **4.3%**, the weakest since Q4 2022, after 5.0% in Q1 ([FocusEconomics](https://www.focus-economics.com/countries/china/news/gdp/china-national-accounts-17-07-2026-economic-growth-decelerates-in-the-second-quarter-of-2026/); [IndexBox/ING](https://www.indexbox.io/blog/china-q2-2026-gdp-growth-slows-to-43-weakest-since-q4-2022/)). In July 2026, **IP 4.5%** (June 5.3%), **retail sales +0.6%**, and **FAI −6.7% y/y** in Jan–Jul ([Trading Economics](https://tradingeconomics.com/china/government-bond-yield/news/575767)).
- **Property is still in free-fall.** Development investment **−16.2% y/y in Jan–May 2026** ([Pomegra](https://pomegra.io/news/china-property-investment-sinks-162-in-janmay-2026)); consensus sees ~**−20%** for the full year, with sales −10.8% by floor area and −13.5% by value ([Reuters via Yahoo Finance](https://finance.yahoo.com/real-estate/articles/china-home-prices-seen-falling-062042122.html)).
- **Liquidity is abundant to the point of inversion.** The 7-day OMO rate is **1.40%**, while **DR007 printed 1.3726% in early September 2026 — below the policy rate**. The 10y CGB is **~1.68%**, a one-year low ([MacroMicro](https://en.macromicro.me/collections/31/cn-finance-relative/109608/cn-interest-rate-corridor-new); [BigGo](https://finance.biggo.com/news/133289e3-abc1-4e72-b95b-7337b28af25e); [Trading Economics](https://tradingeconomics.com/china/government-bond-yield/news/575767)).
- **LPR has been frozen** at 3.00% / 3.50% for ten-plus consecutive months ([Trading Economics](https://tradingeconomics.com/china/interest-rate)).

### The one arithmetic fact that reframes everything

Using the verified inputs above, the **same 3.00% 1y LPR** is simultaneously:

| Deflator | Real 1y LPR | Reads as |
|---|---|---|
| PPI (+3.8%) | **−0.8%** | Deeply stimulative for the tradable/industrial sector |
| GDP deflator (+1.6%) | **+1.4%** | Mildly restrictive economy-wide |
| CPI (+0.8%) | **+2.2%** | Clearly restrictive for the household sector |

**[J]** This ~300bp spread across deflators is *the* story of H2 2026. Through mid-2025 PPI was in sustained deflation, so the PPI-deflated corporate real rate was firmly positive; it is now negative. **China has delivered several hundred basis points of real easing to its industrial sector without moving the policy rate one basis point** — and it did so with a *supply-side administrative* instrument (the "anti-involution" 反内卷 capacity campaign launched July 2025), not a monetary one ([T. Rowe Price](https://www.troweprice.com/en/be/insights/will-chinas-anti-involution-policy-succeed); [China Industry Brief](https://www.chinaindustrybrief.com/en/articles/china-economy-2026-rebalancing-industry-path)).

**[J] The strategic implication:** anyone still running "China must ease because of deflation" is fighting the last war. The live question is the opposite and harder one — **prices are reflating from the supply side while demand decelerates**. That is a mildly stagflationary mix for China, it *weakens* the internal case for a rate cut precisely when growth needs one, and it means the PBoC's easing trigger has moved from the PPI to the **CPI/core-CPI and the labour market**.

---

# PART I — Indicator-by-indicator transmission

---

## 1. M1, M2 and the M1−M2 gap

### 1.1 Transmission mechanism

**[J]** In China's bank-dominated system, M2 is close to a *supply* measure of bank balance-sheet expansion (loans create deposits), while **M1 is a measure of the willingness to hold money in transaction-ready form**. The distinction matters more in China than elsewhere because there is no deep money-market fund/short-bond alternative for corporates of the US kind; the choice is essentially demand deposit vs. time deposit vs. wealth-management product.

The chain runs: firm decides to spend/invest → converts time deposits to demand deposits → M1 rises → capex, inventory build, wage payments → IP, FAI, PPI. **M1 is therefore a *revealed preference* indicator of corporate spending intent**, which is why it leads production and producer prices rather than coinciding with them.

The **M1−M2 gap** is the cleanest expression of this: it strips out the balance-sheet-expansion component common to both and isolates the *velocity/transaction* component. A negative and widening gap means money is being created (M2 up) but parked (M1 flat) — the classic signature of a liquidity trap or a balance-sheet recession.

**[J] China-specific amplifier:** property. Housing pre-sales convert *household* savings deposits (M2, not M1 on the old definition) into *developer* demand deposits (M1). The old M1 series was therefore substantially a **property-sales proxy**. This is the single most important thing to understand about M1's historical predictive power — and the reason that power decayed as property sales collapsed.

### 1.2 Lead/lag

- **[E/P] M1 leads PPI by roughly 10 months; the M2−M1 scissors gap leads the GDP deflator by around a year** — estimate published by China Galaxy Securities (中国银河证券) ([Sina Finance](https://finance.sina.com.cn/stock/hkstock/hkgg/2024-12-03/doc-incyekxt4844435.shtml)). Treat as a **sell-side estimate without published methodology**, not a peer-reviewed result.
- **[P] M1 vs equities:** the standard desk heuristic is that M1 acceleration leads the CSI 300 by roughly two quarters, the mechanism being that the same corporate liquidity that funds capex also funds risk-taking. MacroMicro maintains the canonical chart pairing ([MacroMicro M1 & M2 vs CSI 300](https://en.macromicro.me/charts/260/cn-china-m1-m2)). **Stylised — I would not trade a fixed lag off it.**
- **[J]** M1's lead on *retail sales* is much weaker than on IP/PPI, because household consumption in China is financed out of income and precautionary-savings decisions, not out of corporate transaction balances.

### 1.3 Sign / threshold heuristics

**[P] / [J]**

| Reading | Interpretation |
|---|---|
| M1−M2 gap **> 0 and widening** | Genuine reflation; money is moving. Historically coincides with property/equity upcycles. **Upgrade growth, PPI and equities.** |
| M1−M2 gap **negative, narrowing** | Early-stage repair. Current state. |
| M1−M2 gap **negative, widening** | Deepening balance-sheet recession. Highest-conviction easing signal in the entire toolkit. |
| M2 growth high **while** M1 flat | Credit is being created but not spent — pushing on a string. Argues for *fiscal*, not monetary, response. |

**Current [E]:** M1 +5.1% y/y in Q1 2026; the M1−M2 gap was **−3.1% in Q2 2026**, narrowing from −3.6% — still deeply negative ([shiqiv.com](https://shiqiv.com/2026/04/10/m1-vs-m2-gap-in-china/); [TrendForce DataTrack](https://datatrack.trendforce.com/Chart/content/2928/china-m1-m2)). **[J] Read:** transaction-money preference is repairing but has not turned. Consistent with the observed split — industrial reflation, consumer stagnation.

### 1.4 What the PBoC reacts to

**[J]** The PBoC does not target M2 any more in practice — it dropped numerical money-supply targets from the Work Report years ago and now frames the goal as credit growth "broadly matching" nominal GDP growth. But the M1−M2 gap is **a direct read on whether its easing is working**, and a widening negative gap is the strongest internal argument for structural tools (which push money to *specific* borrowers) over broad rate cuts (which don't work if the problem is demand, not price).

### 1.5 False signals — this is the most contaminated series on the list

1. **[E] The 手工补息 (manual interest supplementation) crackdown, April 2024.** The Market Interest Rate Pricing Self-Disciplinary Mechanism banned banks from paying supplementary interest above the deposit-rate ceiling, with compliance required by 30 April 2024 ([BBT News](https://www.bbtnews.com.cn/2024/0410/510477.shtml); [JRJ analysis](https://m.jrj.com.cn/madapter/bank/2024/05/30131940829499.shtml)). The result was a mechanical exodus of corporate demand deposits into WMPs and non-bank products — **M1 collapsed for reasons that had nothing to do with corporate spending intent** ([China Banking News](https://www.chinabankingnews.com/p/china-wrings-the-water-out-of-the)). Anyone who read the 2024 M1 collapse as a demand signal over-forecast the downturn.
2. **[E] The January 2025 redefinition.** From the January 2025 data, the PBoC's revised M1 adds **personal demand deposits and non-bank payment institutions' customer reserve balances** to the old M0-plus-corporate-demand-deposits definition ([21 Jingji](https://www.21jingji.com/article/20241203/herald/973ef0b60da3acfe1f4b5f9eb4dc6c91.html); [China Fund](https://www.chnfund.com/article/ARd59cf17e-bd43-35d0-4794-3a169990619b)). New-caliber M1 printed **+0.4% in January 2025 after nine consecutive negative months** on the old basis ([Sina Finance](https://finance.sina.com.cn/test/2025-02-14/doc-ineknmew7075518.shtml)). **[J] Consequence: any M1 lead/lag estimated on pre-2025 data is estimated on a different series.** The new M1 is structurally less volatile and less property-levered — which means it is *less* informative about the property cycle and *more* informative about consumer payment activity. The old 10-month PPI lead should be treated as unproven on the new caliber until re-estimated.
3. **[J] Deposit-rate-cut artefacts.** Each round of deposit-rate cuts under the self-discipline mechanism changes the time-vs-demand deposit spread and therefore mechanically shifts money between M1 and M2. Always check whether an M1 move coincides with a deposit-rate action before interpreting it.
4. **[J] Fiscal deposits.** Government deposits at the PBoC are excluded from M2. Heavy bond issuance drains M2 into fiscal deposits; heavy fiscal spending releases it. A "weak M2" print in a heavy-issuance month can be pure Treasury-account timing.

---

## 2. TSF / AFRE — stock growth, flow, and the credit impulse

### 2.1 Transmission mechanism

**[J]** TSF was designed in 2011 to capture what bank loans alone missed — trust loans, entrusted loans, undiscounted acceptances, corporate bonds, equity raising. It has since been broadened to include **local and central government bonds**, and that inclusion has changed what the series means. TSF today is best understood as **total non-financial-sector debt issuance, public and private combined**.

The transmission chain to activity in the historical Chinese model was tight and specific: TSF flow → LGFV and developer financing → land purchase and construction starts → steel, cement, machinery demand → IP and PPI → employment and wages → retail sales. **Property and infrastructure were the transmission belt.** Credit was inflationary because it financed *construction demand*.

**[J] The critical structural break:** state-directed credit allocation has since pivoted toward manufacturing, "new productive forces" and technology. Credit that finances **factory capacity adds supply**; credit that financed **construction added demand**. A given TSF growth rate is therefore *less* inflationary — arguably *disinflationary* — today than the identical number was in 2016. This is the mechanical reason the 2023–25 credit expansion coexisted with PPI deflation, and it is the single most under-appreciated point in most China credit analysis. It also explains why ending PPI deflation ultimately required an *administrative supply cut* (anti-involution) rather than more credit.

### 2.2 Lead/lag

- **[P] Credit impulse (change in the flow of new credit as a share of GDP) leads activity by roughly 9–12 months, i.e. 2–3 quarters**; some practitioners argue 12–17 months ([Zins Capital](https://zinscapital.substack.com/p/macro-101-leading-indicators-chinas); [MindGrowth](https://mindgrowth.io/post/china-credit-impulse-a-leading-indicator); [PipDigest](https://piphawk.com/guides/china-credit-impulse-and-aggregate-financing)). These are **practitioner sources, not peer-reviewed estimates** — the 2–3 quarter figure is the desk consensus and should be quoted as such.
- **[P] Credit impulse and global manufacturing:** a close relationship with the global manufacturing PMI new-orders component, with a similar 9–12 month lead, reflecting China's weight in global industrial demand ([Saxo](https://www.home.saxo/content/articles/macro/chart-of-the-week-china-credit-impulse-vs-australian-gdp-02092019); [Zins Capital](https://zinscapital.substack.com/p/macro-101-leading-indicators-chinas)).
- **[J] Within that 2–3 quarter window the ordering is:** property/land sales and construction starts first (1–2 quarters), then FAI and IP (2–3 quarters), then PPI (3–4 quarters), then CPI and retail sales (4–6 quarters, weakly and unreliably).
- **[J] I believe the lead has lengthened and weakened since 2021.** The transmission belt (property) is broken, so credit now takes longer to reach activity and much of it never does. Treat the 2–3 quarter prior as an upper bound on signal quality, not a mechanical rule.

### 2.3 Sign / threshold heuristics

**[P] / [J]**

- The benchmark is **TSF stock growth vs nominal GDP growth**. TSF growth > nominal GDP = leverage rising = net credit easing. TSF < nominal GDP = active deleveraging.
- **Current [E]:** TSF **7.4%** vs nominal GDP **5.9%** → a ~1.5pp wedge. **[J]** Leverage is *still rising*, but at the narrowest wedge in the modern series. Historically this wedge ran 4–7pp. A wedge below ~1pp would be outright deleveraging and, in my view, would force a policy response within a quarter.
- **Credit impulse** is a *second derivative*: it can be negative while credit growth is positive. It is the right variable for turning points, the wrong one for levels. **[J]** Use the impulse for direction, the TSF-minus-nominal-GDP wedge for stance.
- **[P]** Loose: impulse > +2% of GDP. Neutral: −1% to +1%. Tight: < −2%.

### 2.4 What the PBoC reacts to

**[J]** The PBoC's operative framing is credit growth "broadly matching" nominal GDP growth plus the price target — which, read literally, means TSF growth should be *falling* as nominal GDP falls. This is the crux of the criticism the IMF levels: the framing is **procyclical in a disinflation**. The IMF's 2025 Article IV found that financial conditions **remain tight overall** and that recent policy-rate cuts have delivered **only limited support to growth and inflation** ([IMF Press Release 26/053](https://www.imf.org/en/news/articles/2026/02/18/pr-26053-china-imf-executive-board-concludes-2025-article-iv-consultation)).

**[J] Reaction-function read:** a TSF miss on its own rarely moves the PBoC — it moves the *fiscal* authorities and the credit-quota guidance channel first. What moves the PBoC is a TSF miss **driven by the loan component** while government bonds carry the aggregate, because that is evidence its own transmission is failing rather than that fiscal is slow. That is exactly the current composition.

### 2.5 False signals

1. **[E] TSF inflated by government bonds, not private credit.** The current expansion is dominated by government paper: **government bonds +15.6% vs loans to the real economy +5.6%**, and roughly **83% of what is officially described as "direct financing" is government bonds, over 70% of which sit on commercial bank balance sheets; just 3% is equity** ([USCC China Bulletin, 23 Jul 2026](https://www.uscc.gov/trade-bulletins/china-bulletin-july-23-2026)). **[J] Always decompose TSF into (government bonds) vs (everything else) before forming a view.** The ex-government TSF growth rate is the private-sector credit cycle; the headline is a fiscal indicator wearing a monetary costume.
2. **[J] Government bonds in TSF double-count fiscal stimulus.** When the strategist adds "TSF is accelerating" to "fiscal is expanding," they are frequently counting the same yuan twice.
3. **[E/J] The LGFV debt swap (化债) contaminates both directions.** See Section B.
4. **[J] Equity raising and net corporate bond issuance are small and volatile**; a single large IPO window or a bond-default-driven issuance freeze can swing the monthly flow without macro content.
5. **[J] Base effects on the flow.** The monthly TSF *flow* is violently seasonal (January is enormous). Never compare flows month-on-month; compare to the same month in prior years, and prefer the 12-month rolling sum.

---

## 3. New RMB loans, and the corporate vs household medium-long-term split

### 3.1 Transmission mechanism

**[J]** The **composition** of new loans is far more informative than the total, because the four components have completely different macro content:

| Component | What it means |
|---|---|
| **Household MLT** (mortgages) | The property cycle. Directly drives construction, land sales, LGFV revenue, appliance/furniture retail. The highest-multiplier component. |
| **Household short-term** | Consumer credit and, in practice, disguised business/bridging lending. Noisy. |
| **Corporate MLT** | Genuine capex intent. The highest-quality signal of private investment demand. |
| **Corporate short-term + bill financing** | Working capital, or target-filling. Lowest information content. |

The quality ranking for forecasting purposes is: **corporate MLT ≈ household MLT >> corporate short-term > bills**.

### 3.2 Lead/lag

**[J]** Household MLT loans essentially *coincide* with property transaction volumes (they are the financing leg of the same transaction) and therefore **lead construction starts by ~1 quarter and property FAI by ~2 quarters**. Corporate MLT leads manufacturing FAI by roughly 2 quarters. I am not aware of a published Chinese estimate I can cite for these; treat as structural reasoning, not a documented result.

### 3.3 Sign / threshold heuristics

**[P] / [J]**

- **Household MLT loans negative in a month** is a red-flag print: it means mortgage repayments (including prepayments) exceeded new origination. Two or more consecutive negative months = active household deleveraging.
- **Bill financing above ~50% of new corporate loans** in a month means the print is manufactured. Discount it entirely.
- **Corporate MLT growth decelerating while total loans hold up** = the mix is rotting; the total will follow within 1–2 quarters.

**Current context [E]:** household leverage has fallen to **60.4%**, and NIFD/Caixin describe a **historic contraction in household debt** ([Yicai Global](https://www.yicaiglobal.com/news/chinas-macro-leverage-ratio-rose-to-alarming-2956-in-second-quarter-think-tank-says); [Caixin](https://www.caixinglobal.com/2025-10-29/chinas-macro-leverage-ratio-climbs-despite-household-deleveraging-102376995.html)).

### 3.4 What the PBoC reacts to

**[J]** Household MLT weakness is the trigger for **5y LPR cuts and mortgage-specific measures** (existing-mortgage repricing, minimum down-payment ratios, removal of the mortgage rate floor) rather than for the 1y LPR or the OMO rate. Corporate MLT weakness is the trigger for **structural relending facilities** targeted at tech, equipment renewal and SME lending. This split is why "will they cut?" is the wrong question — **which rate, and for whom, is the question.**

### 3.5 False signals

1. **[E] Bill financing (票据融资) window dressing.** Bankers' acceptance bills count as short-term lending under Chinese regulation, so banks buy them to hit loan targets when genuine demand is absent. In April 2022, bills accounted for most of new corporate lending even as total new lending fell ~80% from March, with bill yields collapsing to as low as **0.04%** ([Reuters via RadioUSA](https://radiousa.com/2022/05/23/china-bill-yields-plunge-as-banks-window-dress-loan-books/)). **[J] The tell is free and real-time: watch the 1-month and 6-month transfer-discount (转贴现) bill rate into month-end and quarter-end.** A collapse in the bill rate in the last five sessions of a quarter means the forthcoming loan print is padded. This is the highest-value cheap signal on this entire list.
2. **[J] Quarter-end and year-end target-filling generally.** Chinese banks are still assessed on quarter-end stock. Use quarterly, not monthly, loan data for trend; use the monthly composition for the tell.
3. **[J] Debt-swap substitution.** When an LGFV's bank loan is repaid with local government bond proceeds, new loans fall and government bonds rise — a *composition* event, not a credit contraction. See Section B.
4. **[J] Mortgage prepayment nets against new origination** in the household MLT line, so a weak print conflates "no one is buying" with "everyone is repaying." These have opposite policy implications: the first calls for demand stimulus, the second for a mortgage rate cut to stop the prepayment arbitrage.

---

## 4. Macro leverage ratio

### 4.1 Transmission mechanism and the denominator trap

**[J]** The macro leverage ratio (total non-financial debt / GDP) is **not a policy instrument reading — it is an accounting identity with a treacherous denominator.** In a disinflation, the ratio rises even if debt is flat, because nominal GDP is the denominator. Treating a rising leverage ratio as evidence of "too much credit" and responding by tightening is the exact mechanism Fisher described in 1933: *the more the debtors pay, the more they owe.*

**Current [E]:** China's macro leverage ratio rose **11.8pp to 302.3% in 2025** (NIFD), **despite** household deleveraging, because slow nominal growth passively inflated the ratio ([UPI](https://www.upi.com/Top_News/World-News/2026/06/29/debt-burden-property-sector-liabilities/6101782779696/); [Caixin](https://www.caixinglobal.com/2025-10-29/chinas-macro-leverage-ratio-climbs-despite-household-deleveraging-102376995.html); [Yicai](https://www.yicaiglobal.com/news/chinas-macro-leverage-ratio-rose-to-alarming-2956-in-second-quarter-think-tank-says)).

**[J] This is the single cleanest empirical demonstration of debt-deflation dynamics in China:** the country *deleveraged its households* and *levered up its economy* in the same year, purely through the deflator.

### 4.2 Lead/lag

**[J]** None usable. It is a slow-moving stock ratio, revised, and published with a lag. It is a *framing* variable for the policy debate, not a forecasting variable.

### 4.3 Sign / threshold heuristics

**[P]** The BIS **credit-to-GDP gap** (credit-to-GDP minus its one-sided HP-filtered trend) is the comparable warning metric; China's gap reached nearly **30pp**, a level internationally associated with subsequent banking stress ([NY Fed Liberty Street Economics](https://libertystreeteconomics.newyorkfed.org/2017/02/chinas-continuing-credit-boom/); [BIS credit gaps data](https://data.bis.org/topics/CREDIT_GAPS)). **[J] Caveat: the HP-filter gap is close to useless for a country with a 15-year credit boom**, because the filter absorbs the boom into the trend. Use the level and the composition, not the gap.

### 4.4 What the PBoC reacts to

**[J]** The macro leverage ratio is the **financial-stability mandate's headline number** and the political cover for the deleveraging objective. Its practical effect on the reaction function is to cap the *duration* of any easing cycle: easing is permitted until leverage optics deteriorate, at which point structural tools replace broad easing. **Decompose it before use:** a rise driven by *government* leverage is intended policy; a rise driven by *corporate* leverage in a disinflation is distress.

### 4.5 False signals

**[J]** (i) Denominator-driven rises read as credit excess when they are deflation. (ii) The debt swap moves debt from the corporate (LGFV) column to the government column with no change in the total — a "corporate deleveraging, government levering" headline that is pure reclassification. (iii) Cross-country comparisons are meaningless without adjusting for China's bank-intermediated structure and high savings rate, which mechanically support a higher sustainable ratio.

---

## 5. The policy rate complex: 7-day OMO, MLF, LPR 1y/5y, and the weighted average lending rate

### 5.1 Transmission mechanism

**[J]** The architecture, post the 2024 framework reform:

```
7-day OMO reverse repo rate  ←  THE policy rate
        │
        ├──► DR007 (operating target, held in a corridor)
        │
        ├──► LPR (1y, 5y) — quoted by 20 banks as a spread over the policy rate
        │        │
        │        └──► Weighted Average Lending Rate (WALR) — what borrowers actually pay
        │
        └──► NCD / MLF / bond curve ──► bank funding cost ──► NIM ──► willingness to lend
```

**[P, unverified in-session]** The important framework change of 2024–25 was the **demotion of the MLF rate from policy-rate status**, with the 7-day OMO reverse repo rate elevated to the single policy rate, LPR quotation shifted to reference the OMO rate rather than the MLF, and MLF operations moved to a multiple-price bid format — converting the MLF from a rate signal into a pure quantity/liquidity tool. This is widely reported but I could not re-verify it in this session; the corridor narrowing is verified (below). **Practical consequence: do not read the MLF rate as a policy signal any more. Read MLF *volume* as a liquidity signal.**

**[E]** In 2026 the PBoC narrowed the interest-rate corridor **from 70bp to 50bp**, setting the temporary overnight repo and reverse repo rates at ±25bp around the 7-day OMO rate ([MacroMicro](https://en.macromicro.me/collections/31/cn-finance-relative/109608/cn-interest-rate-corridor-new)). **[J]** A narrower corridor is a commitment device: it says the PBoC intends to control the overnight rate tightly and wants DR007 to be a credible operating target. That raises the informational value of every basis point of DR007 deviation.

**The WALR is the variable that actually matters for the economy.** **[J]** LPR is an administered quote; the WALR is the realised price of credit including the spread banks charge over LPR. In a period of weak demand and intense competition for the few good borrowers, the WALR can fall *faster* than the LPR (banks compete the spread away, crushing NIM). In a period of rising credit risk, the WALR can fail to fall at all despite LPR cuts. **The LPR–WALR gap is therefore a direct measure of the health of the transmission mechanism.**

### 5.2 Lead/lag

**[J]** Policy-rate changes in China transmit faster to *financial* variables and slower to *real* variables than in Western economies: essentially instantly to DR007 and the bond curve; one quarter to the LPR-linked existing loan book (most loans reprice on 1 January); two to four quarters to FAI; and only weakly ever to consumption. The IMF's finding that **recent policy-rate reductions have provided only limited support to growth and inflation** ([IMF PR 26/053](https://www.imf.org/en/news/articles/2026/02/18/pr-26053-china-imf-executive-board-concludes-2025-article-iv-consultation)) is the formal version of this.

**[J] One underrated timing point:** because the bulk of Chinese floating-rate loans reprice annually on 1 January, an LPR cut in, say, November delivers almost its entire stimulus in the following January. Cuts in Q4 are effectively Q1 policy.

### 5.3 Sign / threshold heuristics

**[J]**

- The **nominal** LPR level tells you almost nothing. Use the real rate (Section 6) and the WALR.
- **LPR–WALR spread narrowing** = banks competing, transmission working mechanically (but NIM eroding).
- **5y LPR cut > 1y LPR cut** = deliberate property-targeted easing. **1y > 5y** = liquidity/corporate-targeted, property-neutral. The asymmetry of the cut is the policy message; the size is not.
- **[E] Current:** LPR 3.00% / 3.50%, unchanged for ten-plus months as of March 2026 ([Trading Economics](https://tradingeconomics.com/china/interest-rate)). Markets price roughly **10bp of PBoC cuts for the remainder of 2026 and another 10bp in H2 2027** ([ING](https://think.ing.com/articles/cny-at-a-glance-tightening-our-forecast-band-for-2h26/)). **[J] Note how small that is: the market is pricing symbolic easing, not a cycle.**

### 5.4 What the PBoC reacts to — the reaction function, and the NIM floor

This is the heart of the note.

**The mandates (multiple and conflicting):** growth target (~5%), price stability (which since 2024 has been read as a *floor*, not a ceiling), employment, RMB exchange-rate stability "at a reasonable and balanced level," financial stability, and — uniquely and increasingly binding — **the preservation of commercial bank net interest margins.**

**[E] The NIM constraint is real and quantified.** Commercial bank NIM fell to a record low of **1.42% in June 2025**, having been below the **1.8% threshold regarded as necessary for reasonable profitability for over two years**; it was 1.43% in Q1 2025 ([Caixin](https://www.caixinglobal.com/2026-05-18/chinese-banks-net-interest-margin-hits-record-low-102444983.html); [Yicai](https://www.yicaiglobal.com/news/chinese-banks-net-interest-margin-shrinks-to-record-low); [BOC Research](https://pic.bankofchina.com/bocappd/rareport/202508/P020250814552535513010.pdf)). In **Q2 2026 NIM rose 1bp to 1.41%, the first quarterly expansion since 2022** ([IndexBox/NFRA](https://www.indexbox.io/blog/chinas-bank-net-interest-margins-see-first-quarterly-rise-since-2022/); [Caixin](https://www.caixinglobal.com/2026-02-13/china-banks-profit-edges-up-as-margins-hold-near-record-lows-102414389.html)).

**[J] The sequencing rule this implies — the most actionable rule in this note:**

> **The PBoC cannot cut the LPR without first cutting deposit rates.** With NIM at 1.41% against a 1.8% reference, an unmatched LPR cut directly impairs bank capital, which impairs credit supply, which is self-defeating. **Therefore: a deposit-rate cut announcement via the self-discipline mechanism is a leading indicator of an LPR cut, typically by days to a few weeks.** If you see deposit rates cut and no LPR cut follows within ~6 weeks, something else (FX, financial stability, a policy dispute) is binding — that is itself high-value information.

**[J] The FX constraint has inverted in 2026 — and most desks have not repriced this.** For three years, the US–China rate differential and depreciation pressure were the binding constraint on easing: cutting rates widened the differential, pressured CNY, and risked outflows. **That constraint is gone.** CNY is through 7.00, the CFETS basket is up ~4.8% YTD, and the PBoC is showing *little resistance to appreciation* ([ING](https://think.ing.com/articles/cny-at-a-glance-whats-next-as-the-cny-moves-below-the-critical-7-threshold/)). With the Fed expected to hold in 2026 and cut 50bp in 2027, the differential narrows further ([ING](https://think.ing.com/articles/cny-at-a-glance-tightening-our-forecast-band-for-2h26/)). **A stronger CNY is disinflationary and tightens monetary conditions via the REER channel — so FX has flipped from a reason *not* to cut into a reason *to* cut.**

**[J] So why hasn't the PBoC cut?** My read of the binding constraints as of September 2026, in order:

1. **PPI reflation has removed the deflation emergency.** With PPI at +3.8% and the deflator positive, the internal argument "we must ease or prices will spiral down" has lost its force — even though the *demand* side (retail +0.6%, FAI −6.7%) is worse than a year ago.
2. **Bond-market froth.** With the 10y at 1.68% and sell-side forecasts of 1.2–1.5% ([CNFIN](https://www.cnfin.com/zs-lb/detail/20251120/4338481_1.html)), the PBoC is wary of validating a duration bubble on bank balance sheets. It has historically preferred to warn about, and lean against, rapid long-end rallies. *[P, unverified in-session]*
3. **The deleveraging objective.** Easing into a 302.3% leverage ratio is politically costly.
4. **NIM**, now marginally less binding after the Q2 uptick.

**[J] Probability read-across (my judgement, not a model):** near-term policy is more likely to be **quantity-and-structure** (overnight/outright reverse repos, relending facilities, possibly an RRR cut framed as "supporting government bond issuance") than **price**. An LPR cut requires either a CPI/core rollover, a labour-market shock, or a visible credit-quality event.

### 5.5 False signals

1. **[J] Reading the MLF rate as the policy rate.** Post-2024 this is simply wrong. Read MLF volume, not rate.
2. **[J] Reading "no cut" as "tight."** With PPI-deflated real corporate rates now negative, the *stance* has eased materially without any policy action. Stance ≠ action.
3. **[J] Reading an LPR cut as broad easing when it is a targeted repair.** A 5y-only cut is a property measure. A 1y-only cut is a corporate-liquidity measure.
4. **[J] Reading a falling WALR as successful easing.** It may be banks competing themselves into insolvency for the shrinking pool of creditworthy borrowers — a *symptom of the asset shortage*, not evidence of transmission. Check it against loan volume: falling WALR **with** falling volume is demand collapse, not easing.

---

## 6. Real policy and lending rates (CPI-, PPI- and deflator-deflated)

### 6.1 Transmission mechanism

**[J]** The real rate is the actual price of credit facing a borrower, and *which* deflator is correct depends entirely on who the borrower is:

| Borrower | Correct deflator | Why |
|---|---|---|
| Industrial/manufacturing firm | **PPI** | Revenue is a factory-gate price |
| Property developer | **House prices** | Revenue is a house price — still deeply negative, so developer real rates remain punitive |
| Household/mortgagor | **CPI** (or nominal wage growth) | Debt is serviced out of nominal income |
| Local government / LGFV | **Nominal GDP / land prices** | Revenue is tax and land sales |
| Economy-wide policy stance | **GDP deflator** | The comprehensive price measure |

**[J] There is no single Chinese real rate.** Quoting one is the most common analytical error in the field. The dispersion *across* deflators is itself the signal — and right now that dispersion is ~300bp.

### 6.2 Lead/lag

**[J]** Real rates act on investment with roughly a 2–3 quarter lag, similar to the credit impulse, because they operate through the same hurdle-rate decision. But real rates are **contemporaneously observable only with a lag** (PPI/CPI are monthly with ~9-day lag; the deflator is quarterly). And they are backward-looking: what matters for investment is the *expected* real rate, which in a deflation is worse than the realised one because expectations are anchored on the recent past.

### 6.3 Sign / threshold heuristics

**[J]** The right benchmark is **r vs g** (real lending rate vs real GDP growth), or equivalently the nominal lending rate vs nominal GDP growth:

- Nominal lending rate **3.00%** vs nominal GDP growth **5.9%** → **r − g ≈ −290bp**. On this metric conditions are *accommodative* and debt dynamics are improving. **[E inputs, J calculation]**
- But nominal lending rate **3.00%** vs *property developer* revenue growth (deeply negative) → developer real rates are punitive, which is why property investment is −16% to −20%.
- And **3.00% vs household nominal income growth** — with retail sales at +0.6% and a weak labour market, household real debt service is heavy.

**[J] Rule:** compute r − g **sector by sector**. The aggregate looks fine; the distribution is the problem.

### 6.4 What the PBoC reacts to

**[E]** The IMF's 2025 Article IV explicitly finds that **real interest rates remain high**, that rate reductions have delivered **only limited support**, that financial conditions **remain tight overall**, and recommends that **an expansionary stance be maintained until deflationary pressures subside durably** ([IMF PR 26/053](https://www.imf.org/en/news/articles/2026/02/18/pr-26053-china-imf-executive-board-concludes-2025-article-iv-consultation); staff report at [IMF Country Report 2026/044](https://www.imf.org/en/publications/cr/issues/2026/02/17/peoples-republic-of-china-2025-article-iv-consultation-press-release-staff-report-and-574028)).

**[J]** The PBoC's revealed preference is to weight the **PPI and the GDP deflator** heavily in its rhetoric (the shift to describing the price objective as "promoting a reasonable rebound in prices" was a real change) but to weight **NIM and financial stability** heavily in its actions. The PPI reflation has therefore given it exactly what it needs to justify inaction.

### 6.5 False signals

1. **[J] PPI-deflated real rates flatter the stance when PPI is driven by supply cuts, not demand.** The current negative PPI-deflated real rate is a *terms-of-trade* event for industrial firms, not evidence of buoyant demand — their volumes are still weak (IP decelerating to 4.5%). **This is the single most important false signal live today.** A firm facing +3.8% output prices *because capacity was administratively cut* does not respond by investing; it responds by harvesting margin. The usual "negative real rates → capex boom" transmission does not apply.
2. **[J] Using headline CPI when food and energy dominate the move.** Core CPI at 1.0% vs headline 0.8% ([CNBC](https://www.cnbc.com/2026/09/09/china-cpi-ppi-august-oil-prices-tech-manufacturing-.html)) — use core for the policy-relevant real rate.
3. **[J] Realised vs expected inflation.** After 12 negative deflator quarters, expectations lag the data badly. Expected real rates are almost certainly higher than measured real rates, which means the effective stance is tighter than the arithmetic suggests.

---

## 7. Required reserve ratio (RRR)

### 7.1 Transmission mechanism

**[J]** An RRR cut releases long-term, zero-cost (or rather, reserve-rate-cost) base money permanently, versus OMO/MLF which lend it at a rate. Its transmission is therefore **as much a bank-profitability instrument as a liquidity instrument**: replacing MLF funding (costed) with released reserves (cheaper) directly widens NIM. Given the 1.41% NIM constraint, **the RRR is now the PBoC's preferred easing tool precisely because it eases without hurting banks.**

Secondary channel: it creates balance-sheet capacity to absorb government bond supply — which is why RRR cuts increasingly cluster around heavy issuance quarters.

### 7.2 Lead/lag

**[J]** Near-instant effect on interbank rates and bank funding costs; weak and slow effect on credit (it relieves a constraint that is not binding when the problem is demand). Effect on activity: unreliable, and in the current regime close to zero.

### 7.3 Sign / threshold heuristics

**[J]** An RRR cut is best read as a **signalling and bank-margin** event, not a stimulus event. Each 50bp cut releases roughly RMB 1tn of long-term liquidity *[order of magnitude; unverified in-session]*. The binding question is how much room is left before the effective floor (the PBoC has said it wants to keep a reserve buffer). **In a demand-constrained regime, an RRR cut is close to macro-irrelevant and is mostly a message.**

### 7.4 What the PBoC reacts to

**[J]** RRR cut probability rises with: (i) a heavy government bond issuance calendar; (ii) NCD rates pushing above the policy rate (bank liability stress); (iii) NIM deterioration; (iv) a need to signal support without cutting rates (i.e., when FX or bond-froth concerns block a rate cut). **All but (ii) are live now.** I would put a higher probability on an RRR cut than on an LPR cut over the next two quarters **[J]**.

### 7.5 False signals

**[J]** (i) An RRR cut announced alongside a big issuance program is *offsetting*, not easing — net liquidity may be unchanged. (ii) Targeted/structural RRR cuts for specific bank categories are small and largely symbolic. (iii) An RRR cut with no follow-through in DR007 means the liquidity was absorbed elsewhere — check fiscal deposits.

---

## 8. CNY, CFETS/REER

### 8.1 Transmission mechanism

**[J]** Under capital controls, the exchange rate is only a semi-free price, and the PBoC manages it through the daily fixing (the counter-cyclical factor), state-bank spot intervention, the FX RRR on bank foreign-currency deposits, the forward risk-reserve requirement, and offshore liquidity management via CNH. The channels to the macro:

- **Trade channel:** REER depreciation supports exports (large, and the main growth engine in 2025–26) and raises import prices (mildly reflationary).
- **Balance-sheet channel:** depreciation raises the local-currency cost of USD corporate debt — small for China, unlike EM peers.
- **Expectations/outflow channel:** depreciation expectations trigger exporter FX hoarding and capital flight pressure, which *tightens* domestic liquidity. This is the channel that mattered 2022–24.
- **Monetary-conditions channel:** the REER is a component of any monetary conditions index — **appreciation is tightening, and is disinflationary via import prices.**

### 8.2 Lead/lag

**[J]** REER moves pass through to export volumes with roughly 2–3 quarters' lag and to import-price-driven CPI/PPI components within 1–2 quarters. The CFETS basket, not USDCNY, is the right variable — a stable USDCNY in a falling-dollar world is a *depreciating* basket and vice versa.

### 8.3 Sign / threshold heuristics

**[P] / [J]**

- **USDCNY 7.00** and **7.30** have functioned as psychologically defended levels. Breaks are regime information.
- The **fixing vs. consensus-estimate gap** is the highest-frequency read on PBoC FX intent: a persistently stronger-than-model fix is leaning against depreciation; a weaker-than-model fix is tolerating it ([example fixing coverage](https://pro.edgex.exchange/en-US/news/article/pboc-usdcny-fixing-due-67421)).
- **CFETS YTD change** is the honest measure of the stance. **Current [E]: CFETS +4.8% YTD, ahead of the +2.6% gain versus USD** ([ING](https://think.ing.com/articles/cny-at-a-glance-chinas-yuan-moves-into-our-bullish-scenario/)).

### 8.4 What the PBoC reacts to

**[J] This is where the 2026 regime change is sharpest.** For years, "FX stability" meant *resisting depreciation*, and that constraint capped how far the PBoC could ease relative to the Fed. Now the PBoC is **not meaningfully resisting appreciation** ([ING](https://think.ing.com/articles/cny-at-a-glance-tightening-our-forecast-band-for-2h26/)). Implications:

1. **The rate-differential constraint on easing is released.** The PBoC can cut without FX consequence it cares about.
2. **Appreciation is itself a tightening of monetary conditions** — a disinflationary impulse arriving precisely as the PBoC declares victory on deflation. **[J] This is an under-priced risk to the reflation narrative.**
3. **Tolerating appreciation is a choice with a purpose** — most plausibly trade-negotiation management and inbound-portfolio-flow encouragement. It is not a costless choice for exporters, who are carrying the growth.

### 8.5 False signals

**[J]** (i) Reading USDCNY alone rather than CFETS. (ii) Reading a strong fix as bullish CNY when it is defensive management of a weak spot. (iii) Reading FX reserve stability as absence of intervention — intervention is heavily conducted through state banks' forward and spot books, which do not show in headline reserves. (iv) Reading appreciation as a vote of confidence in growth when it is a dollar-weakness artefact.

---

## 9. The interbank complex: DR007 and its spread to OMO, R007−DR007, NCD vs MLF, excess reserve ratio

### 9.1 Transmission mechanism

**[J]** This block measures **liquidity conditions** (the price and availability of reserves to banks), which is emphatically **not** the same as **monetary conditions** (the price and availability of credit to the economy). The distinction is the entire subject of Section C.

- **DR007** — depository-institution-only repo against rate bonds — is the PBoC's operating target and the cleanest measure of *bank* funding cost, stripped of credit and counterparty risk.
- **DR007 − 7d OMO spread** is the single best real-time read on the PBoC's liquidity intent, because the PBoC controls it directly.
- **R007 − DR007** captures the premium non-bank institutions (funds, brokers, WMPs) pay over banks. It is a **leverage and risk-appetite gauge**: it widens when banks stop lending to non-banks, which is the transmission mechanism of every Chinese bond-market accident.
- **1y AAA NCD rate vs the 1y policy rate** measures **structural bank liability pressure**. NCDs are marginal wholesale funding; when NCD rates exceed the policy rate persistently, banks are short of stable deposits and will either shrink assets or demand an RRR cut.
- **Excess reserve ratio (超额备付金率)** is the quantity counterpart — the buffer banks hold above required reserves. Low excess reserves with low DR007 is a high-efficiency liquidity regime; high excess reserves with low DR007 means banks are hoarding, i.e. no assets to buy.

### 9.2 Lead/lag

**[J]** These are **coincident-to-slightly-leading** financial variables, not macro leading indicators. Their value is (a) real-time policy-intent detection, (b) early warning of a funding accident, typically 1–4 weeks ahead of a forced-deleveraging event in the bond market. They tell you about the next month in markets, not the next two quarters in the economy.

### 9.3 Sign / threshold heuristics

**[P] / [J]** — these are the numbers to have on a screen:

| Metric | Loose | Neutral | Tight / flag |
|---|---|---|---|
| **DR007 − 7d OMO** | < 0bp | 0 to +15bp | > +20bp sustained 5 sessions = deliberate tightening or accident |
| **R007 − DR007** | < 10bp | 10–25bp | **> 40–50bp sustained = non-bank funding stress; reduce duration and credit risk** |
| **1y AAA NCD − 1y policy rate** | < −10bp | −10 to +10bp | **> +20bp for 2 weeks = bank liability stress → RRR cut probability rises sharply** |
| **Excess reserve ratio** | — | ~1.5% | High **and** DR007 low = asset shortage, not easing |

**Current [E]:** DR007 printed **1.3726%** in early September 2026 against a 7d OMO rate of **1.40%** — i.e. **DR007 is roughly 3bp *below* the policy rate**. The PBoC set 7-day reverse repo volumes at **zero for seven consecutive sessions from 11 August 2026, the longest such stretch since 2024**, while injecting via **overnight** reverse repos, and it conducted a **RMB 1.1tn outright reverse repo** operation ([BigGo](https://finance.biggo.com/news/133289e3-abc1-4e72-b95b-7337b28af25e); [Macrostream](https://www.macrostream.ai/articles/6a430ac23c80f748cb62270c); [BigGo](https://finance.biggo.com/news/Cljml5sBTVZqOzlnhIUF); [Archyde](https://www.archyde.com/pboc-shifts-to-equal-amount-rollover-for-3-month-outright-reverse-repos/)).

**[J] Read:** DR007 below the policy rate with the PBoC *withdrawing* 7-day operations is not the PBoC easing — it is the PBoC **mopping up a liquidity surplus it did not create**, arising from weak credit demand and heavy deposit accumulation. The shift to overnight fine-tuning and the corridor narrowing to 50bp are consistent with an operating framework being tightened up around an abundant-reserves regime.

### 9.4 What the PBoC reacts to

**[J]**
- **DR007 persistently below OMO** → the PBoC drains (reduced OMO volumes, net withdrawal, possibly bond sales). It does *not* like the policy rate being an ineffective ceiling — it undermines the corridor it just narrowed.
- **R007−DR007 blowing out** → immediate large injections, regardless of the macro stance. Financial stability dominates everything in the short run. This is the reaction that is most reliable and most tradeable.
- **NCD above policy rate persistently** → RRR cut or expanded MLF/outright reverse repo.
- **A funding accident** → the PBoC always wins the short-run fight; never fade a PBoC liquidity injection on a stress event.

### 9.5 False signals — the central one on the whole list

1. **[J] Low DR007 signals weak credit demand, not deliberate easing.** This is the most consequential misread in China macro. When banks cannot find borrowers, reserves pile up in the interbank market and the overnight rate sags below the policy rate *without the central bank doing anything*. The tell: **low DR007 accompanied by low/falling loan growth and a high excess reserve ratio = asset shortage**; low DR007 accompanied by *accelerating* loan growth = genuine easing. Today's configuration — DR007 below OMO with TSF at a record-low 7.4% — is unambiguously the former.
2. **[J] Quarter-end, tax-payment and holiday distortions.** DR007 reliably spikes at quarter-ends (MPA assessment), around the 15th–25th tax-payment window, and before Chinese New Year. Never interpret a single spike; use a 10-day moving average and compare to the same calendar window in prior years.
3. **[J] Reading R007 instead of DR007.** R007 includes non-bank and lower-quality collateral; its spikes reflect leverage in the non-bank sector, not policy.
4. **[J] Reading the MLF rate as a signal.** Post-2024 reform, read volume not rate.

---

## 10. PBoC net liquidity injection, fiscal deposits, government bond issuance

### 10.1 Transmission mechanism

**[J]** These three are a single system — the **base money accounting identity**. Reserves in the banking system change with:

```
Δ Reserves = PBoC net injection (OMO + MLF + outright RR + relending)
           + FX inflows (外汇占款)
           − Δ Government deposits at the PBoC (fiscal deposits)
           − Δ Currency in circulation
           − Δ Required reserves
```

**The critical point [J]:** when the Treasury issues bonds, the proceeds move from bank deposits into the government's account at the PBoC — **destroying bank reserves**. They are only restored when the government *spends*. So an aggressive issuance calendar is a **liquidity tightening** until the money is disbursed, and the issuance–spending lag is a genuine, recurring, and under-modelled drag in China. The PBoC routinely offsets it, which is why "PBoC injects liquidity" headlines during issuance-heavy weeks are offsetting, not easing.

**[J] Structural break worth flagging:** before 2014, base money was created primarily by FX purchases (外汇占款) as reserves accumulated. When that reversed in 2015–16, the PBoC had to *invent* replacement instruments — MLF, PSL, SLF — to create base money domestically. That is why China's operating framework looks the way it does today, and why the balance-sheet composition (lending to banks rather than FX assets) matters for understanding the PBoC's control problem.

### 10.2 Lead/lag

**[J]** Fiscal deposits lead activity by roughly one quarter: a *drawdown* in fiscal deposits means money is being spent, which shows in infrastructure FAI within one to two quarters. A build-up means issuance is running ahead of disbursement — the "money raised but not spent" problem that has characterised recent fiscal expansions.

### 10.3 Sign / threshold heuristics

**[J]**
- **Government bond issuance accelerating + fiscal deposits rising** = fiscal is *raising* but not *spending*. Liquidity drag; no growth impulse yet. **Bearish activity, bullish bonds.**
- **Fiscal deposits falling sharply** = disbursement underway. **Bullish activity, bearish bonds.** Watch this as the trigger for the infrastructure trade.
- **[E] Context:** government bonds outstanding grew **15.6% y/y** to RMB 99.37tn, and are the dominant driver of TSF expansion ([USCC](https://www.uscc.gov/trade-bulletins/china-bulletin-july-23-2026)). **[J] With over 70% of government bonds held by commercial banks** (same source), bond issuance and bank balance-sheet capacity are now the same problem — which is the structural reason RRR cuts have become the fiscal-enabling tool.

### 10.4 What the PBoC reacts to

**[J]** The PBoC has an effectively unwritten mandate to ensure government bond issuance succeeds without disrupting money markets. Expect RRR cuts, outright reverse repos of 3–6 month tenor, and MLF over-rollovers to cluster around heavy issuance quarters. **Do not read these as macro easing.** The RMB 1.1tn outright reverse repo ([BigGo](https://finance.biggo.com/news/Cljml5sBTVZqOzlnhIUF)) is better understood as plumbing than as stimulus.

### 10.5 False signals

**[J]** (i) Headline injection numbers are **gross**; always compute net of maturities. (ii) A large net injection in a tax week is neutral. (iii) Rising government bond issuance read as "stimulus" when the proceeds are refinancing existing hidden debt under the 化债 swap — that is balance-sheet repair, not new demand (Section B).

---

## 11. 10y CGB yield, the term spread, and credit spreads

### 11.1 Transmission mechanism

**[J]** In a normal economy the long bond yield is *policy expectations + term premium + inflation expectations*. In China, with capital controls and a bank-dominated buyer base, it is better modelled as:

> **10y CGB ≈ f(expected policy rate path, bank asset-allocation demand, credit demand absence, regulatory treatment)**

The *supply* of bonds is administratively set; the *demand* is dominated by banks and insurers who buy bonds **because they cannot find loans**. This makes the CGB yield much more a barometer of **credit demand weakness** than of monetary policy expectations. It is the price of the asset shortage.

**Term spread (10y−1y or 10y−2y) [J]:** flattening/inversion from the long end signals deteriorating growth and inflation expectations. But in China, a flat curve can equally reflect banks extending duration for carry with abundant short funding — a *liquidity-driven* flattening rather than a *growth-driven* one. Distinguish by checking whether the short end is pinned by ample liquidity (current case) or by policy tightening.

**Credit spreads [J]:** Chinese credit spreads are heavily distorted by implicit guarantees. The informative object is not the level but the **dispersion** — specifically the spread of weak-region LGFV bonds and private developer bonds over CGB. Compression there reflects the government's 化债 guarantee, not improving fundamentals; widening there is a genuine stress signal and the thing to actually watch.

### 11.2 Lead/lag

**[J]** The CGB yield is **coincident-to-leading on inflation expectations by roughly one to two quarters**, and its relationship with subsequent activity is weak in China because it is so heavily supply/demand-technical. I would not use it as an activity forecaster. Use it as a *market-implied read on the deflation regime*, cross-checked against breakevens (which barely exist in China) and against the M1−M2 gap.

### 11.3 Sign / threshold heuristics

**[E] Current:** 10y CGB **~1.68%**, a one-year low, with disappointing data reinforcing stimulus expectations ([Trading Economics](https://tradingeconomics.com/china/government-bond-yield/news/575767)). Sell-side 2026 outlooks have discussed a bull steepening with the 10y potentially at **1.2%–1.5%** ([CNFIN](https://www.cnfin.com/zs-lb/detail/20251120/4338481_1.html)).

**[J] Heuristics:**
- **10y CGB vs nominal GDP growth:** 1.68% vs 5.9% is an extraordinary gap. On a pure r−g basis, Chinese government debt dynamics are benign; the constraint is political and allocative, not arithmetic. **This is the strongest available argument for fiscal expansion and the strategist should make it.**
- **10y below 1.50%** → expect PBoC verbal or actual pushback on duration risk. *[P, unverified in-session, but consistent with its 2024 conduct.]*
- **Term spread steepening driven by the long end selling off while the short end is pinned** = reflation being priced. That is the trade to watch for as the regime turns.

### 11.4 What the PBoC reacts to

**[J]** The PBoC has an explicit financial-stability interest in **not** letting banks build a large unhedged duration position at record-low yields — the Silicon Valley Bank problem, with Chinese characteristics and a much larger banking system. A rapid long-end rally therefore *raises* the probability of jawboning, bond sales from the PBoC's own portfolio, or regulatory guidance to rural commercial banks — and *lowers* the probability of a policy rate cut, because a cut would validate the rally. **This is an important and counter-intuitive part of the reaction function: a bond rally can crowd out the rate cut it is pricing.**

### 11.5 False signals — the second-most consequential misread

1. **[J] Falling CGB yields signal deflation expectations and an asset shortage, not easy policy.** The 2024–26 rally happened *while the PBoC held rates*. Reading the rally as "the PBoC is easing" inverts the causality: yields fell because credit demand died and banks had nowhere else to put money. **If you must pick one line from this note: a bond rally driven by the collapse of the alternative asset is a *tightening* of monetary conditions for the real economy, not a loosening.**
2. **[J] Compressed LGFV credit spreads read as improving fundamentals** when they are the price of an explicit state guarantee under the debt swap.
3. **[J] Curve flattening read as a growth signal** when it is banks reaching for carry.

---

## 12. CNH HIBOR

### 12.1 Transmission mechanism

**[J]** Offshore CNH liquidity is small, bounded and directly manipulable by the PBoC and state banks. CNH HIBOR spikes are the classic instrument for **squeezing offshore CNY shorts**: raising the cost of borrowing CNH makes short positions uneconomic and forces covering. CNH HIBOR is therefore primarily a **policy-intent indicator on FX**, not a domestic monetary indicator.

Secondary reading: the **CNH−CNY spot basis** is the cleanest available market measure of depreciation/appreciation expectations, precisely because the offshore market is less managed.

### 12.2 Lead/lag

**[J]** Effectively real-time on FX intent, with a lead of days on FX-market direction. No usable lead on the macro.

### 12.3 Sign / threshold heuristics

**[J]** Overnight CNH HIBOR spiking to double digits = active, deliberate short squeeze; treat as an official statement that a level is being defended. Persistently *low* CNH HIBOR alongside a firm CNH = no defensive action needed, which is the current and notably relaxed configuration given CNY strength.

### 12.4 What the PBoC reacts to

**[J]** This is a tool, not a reading. Its rise in prominence maps to the depreciation episodes of 2016, 2018–19 and 2022–24. Its current quiescence is a direct corollary of appreciation pressure.

### 12.5 False signals

**[J]** (i) CNH HIBOR spikes at quarter-ends and around index rebalancing for technical reasons. (ii) Low CNH HIBOR read as "no FX stress" when the absence of stress is simply because the pressure is in the appreciation direction, which requires no liquidity defence.

---

# PART II — Cross-cutting analysis

---

## A. The deflation problem and real rates — and why the problem has changed shape

### A.1 What happened

**[E]** The GDP deflator was negative for **12 consecutive quarters**, through Q1 2026 (≈ −0.1%), before turning positive at **+1.6% in Q2 2026** ([China Daily HK](https://www.chinadailyhk.com/hk/article/636329); [BigGo](https://finance.biggo.com/news/c1efd22b-d31b-48d1-8e4b-4dbf158e5642)). Headline CPI averaged **0% in 2025** and the IMF's 2025 Article IV found **real interest rates remain high** with rate cuts providing **only limited support**, and financial conditions **tight overall** ([IMF PR 26/053](https://www.imf.org/en/news/articles/2026/02/18/pr-26053-china-imf-executive-board-concludes-2025-article-iv-consultation)).

### A.2 Why nominal easing did not deliver easy real conditions

**[J]** Three compounding reasons:

1. **The deflator moved faster than the policy rate.** Over 2023–25 the PBoC cut in 10bp and 25bp increments while the GDP deflator fell by several percentage points. Real rates *rose* through an easing cycle. The nominal easing was, arithmetically, not easing at all.
2. **The NIM floor throttled the pass-through.** With NIM at a record-low **1.42% (June 2025)** against a **1.8%** reference ([Caixin](https://www.caixinglobal.com/2026-05-18/chinese-banks-net-interest-margin-hits-record-low-102444983.html)), each LPR cut had to be preceded or matched by deposit-rate cuts, which slowed and capped the cycle. **The bank NIM is China's effective lower bound.** It is not the zero bound; it binds at a positive nominal rate, and it binds asymmetrically (it constrains lending-rate cuts more than deposit-rate cuts).
3. **The borrower did not want the loan at any price.** See A.3.

### A.3 The debt-deflation / balance-sheet-recession framing

**[P/J]** Two canonical frameworks apply, with a China-specific twist:

- **Fisher's debt-deflation** (Irving Fisher, "The Debt-Deflation Theory of Great Depressions," *Econometrica* 1(4), 1933, 337–357 — *bibliographic citation; URL not verified in this session due to blocked egress*). The core mechanism — falling prices raise the real value of debt, forcing distress selling, which lowers prices further — is visible in the Chinese data with unusual clarity: **the macro leverage ratio rose 11.8pp to 302.3% in 2025 despite a historic contraction in household debt**, purely because nominal GDP grew too slowly ([Caixin](https://www.caixinglobal.com/2025-10-29/chinas-macro-leverage-ratio-climbs-despite-household-deleveraging-102376995.html); [UPI](https://www.upi.com/Top_News/World-News/2026/06/29/debt-burden-property-sector-liabilities/6101782779696/)). **[J] That is Fisher's identity — "the more the debtors pay, the more they owe" — measured.**

- **Koo's balance-sheet recession** (Richard C. Koo, *The Holy Grail of Macroeconomics: Lessons from Japan's Great Recession*, Wiley, 2008; and *The Other Half of Macroeconomics and the Fate of Globalization*, Wiley, 2018 — *bibliographic citations; URLs not verified in this session*). The claim is that when the private sector shifts from profit-maximising to debt-minimising after an asset-price collapse, monetary policy loses traction because there is **no demand for credit at any interest rate**, and only fiscal policy can offset the private sector's financial surplus. **[J] The Chinese evidence is consistent:** households are deleveraging (leverage down to 60.4%) and prepaying mortgages while the deposit base swells, corporates are not borrowing (loans to the real economy +5.6%, the weakest on record for TSF at 7.4%), and the only thing expanding is **government borrowing (+15.6%)** — which is precisely Koo's prescription being executed, if not by that name.

**[J] The China-specific twist, and where both frameworks need amending:** Japan's balance-sheet recession followed a *private* asset bubble and was accompanied by genuine monetary impotence. China's is **partly deliberate**. The property downturn and the LGFV squeeze are the *intended results* of policy (three red lines, hidden-debt resolution). The state amputated the two channels through which credit historically reached the economy, and then observed that credit no longer reaches the economy. **The transmission mechanism is not only broken; a large part of it was decommissioned on purpose.** That is a crucial difference because it means the fix is available on demand — a political decision, not a structural impossibility.

### A.4 What this implies for the required scale of nominal easing

**[J]** Take the IMF's framing seriously: if real rates are too high and the deflator was running around zero to negative, then restoring a neutral stance required either (a) cutting the nominal policy rate by 100–200bp — impossible under the NIM constraint without a wholesale restructuring of bank funding costs — or (b) **raising the price level directly**. China chose (b), and did it with an *administrative supply cut* rather than a demand stimulus. PPI at +3.8% and a positive deflator are the result.

**[J] But (b) solves the arithmetic without solving the economics.** Supply-driven reflation lowers the measured real rate without raising the expected return on investment — because volumes are not rising. It repairs the *denominator* of the leverage ratio and the *real burden* of existing debt (genuinely valuable, and it should not be dismissed), but it does not generate new demand for credit. **My judgement: the required scale of demand-side easing has not changed; only its measurement has.** Which is why FAI is at −6.7% and retail at +0.6% in the middle of a reflation.

---

## B. Why credit growth has decoupled from GDP growth

**[J]** Four distinct forces, which must be separated because they have different implications:

### B.1 Falling credit intensity of growth — but in the wrong direction

The historic Chinese growth model consumed enormous credit per unit of GDP because it was construction-led and construction is credit-intensive. As the growth mix shifts to manufacturing, services and exports, credit intensity mechanically falls. **[J] This is genuinely healthy** and means a lower TSF growth rate is consistent with the same GDP growth. Do not read every credit slowdown as a demand failure.

**But** the current configuration is not the healthy version: TSF at **7.4%** against nominal GDP at **5.9%** means the ratio is *still rising* ([USCC](https://www.uscc.gov/trade-bulletins/china-bulletin-july-23-2026); [FocusEconomics](https://www.focus-economics.com/countries/china/news/gdp/china-national-accounts-17-07-2026-economic-growth-decelerates-in-the-second-quarter-of-2026/)). **[J] China is getting less GDP per unit of credit, not more — because the credit is going to the government and to capacity, and neither produces near-term nominal GDP.** Credit intensity has fallen in the *private* sector and risen in the *public* sector.

### B.2 The property-sector credit demand collapse

**[E]** Property development investment **−16.2% y/y in Jan–May 2026**, with consensus at ~−20% for the full year; new home sales **−10.8%** by floor area and **−13.5%** by value ([Pomegra](https://pomegra.io/news/china-property-investment-sinks-162-in-janmay-2026); [Reuters/Yahoo](https://finance.yahoo.com/real-estate/articles/china-home-prices-seen-falling-062042122.html)); S&P sees primary prices −1.5% to −2.5% and secondary −4% to −5% in 2026.

**[J]** Property was simultaneously the **largest borrower** (developers), the **largest collateral pool** (land and housing), and the **largest source of local fiscal revenue** (land sales). Its collapse removes credit demand through all three channels at once. **The collateral channel is the one most analysts underweight:** with property prices falling, the borrowing capacity of every SME owner who pledged a property, and every local government pledging land, falls regardless of the interest rate. **Lower rates cannot offset lower collateral values** — this is the financial-accelerator mechanism running in reverse (Bernanke, Gertler & Gilchrist, "The Financial Accelerator in a Quantitative Business Cycle Framework," *Handbook of Macroeconomics*, 1999 — *bibliographic citation; URL not verified in-session*).

### B.3 The LGFV debt swap (化债) mechanically shrinking measured credit

**[E]** A three-year programme launched November 2024 refinances **RMB 10tn (~USD 1.39tn)** of hidden LGFV debt into local government bonds. Officially reported hidden debt was **RMB 14.3tn at end-2023**, targeted to fall to **RMB 2.3tn by 2028**; it fell to **RMB 10.5tn by end-2024**, and the number of LGFVs on the official list shrank **71% between March 2023 and September 2025**. The IMF's own estimate of LGFV debt was far higher at **RMB 60tn, or 47.6% of GDP, at end-2023** ([Caixin](https://www.caixinglobal.com/2026-05-29/in-depth-as-chinas-hidden-local-debts-shrink-a-new-challenge-emerges-102449016.html); [Nasdaq](https://www.nasdaq.com/articles/china-unveils-837-billion-debt-swap-tackle-local-government-risks); [Atlantic Council](https://www.atlanticcouncil.org/blogs/econographics/beijing-extends-and-pretends-to-deal-with-its-mountain-of-local-government-debt/); [The Diplomat](https://thediplomat.com/2025/09/china-is-still-struggling-to-manage-local-debt-stress/)).

**[J] The mechanics matter and are widely misunderstood:**

- When an LGFV **bank loan** is repaid with local government bond proceeds, TSF's *loan* component falls and its *government bond* component rises. **TSF stock is roughly unchanged; the loan growth rate falls.** This is a pure composition shift, and it is a large part of why loans are at +5.6% while government bonds are at +15.6%.
- When **non-standard debt outside TSF** (supplier arrears, some trust and non-standard financing) is swapped, TSF *rises* with no new economic activity — a pure measurement artefact that flatters TSF.
- Either way, **new project financing is simultaneously suppressed**, because LGFVs under hidden-debt resolution are barred from new borrowing for non-priority projects. **The swap is contractionary for new credit flow even as it is expansionary for the measured government bond stock.**
- **The offsetting genuine positive [J]:** the swap replaces LGFV borrowing at 5–6% with government bonds at ~2%, cutting the interest burden materially — a real easing of debt service that appears in **no credit aggregate at all**. The Ministry of Finance quantified the expected interest saving when the programme was announced *[figure not re-verified in this session]*. A strategist should carry the interest-burden channel separately from the credit-flow channel.

### B.4 Household deleveraging and mortgage prepayment

**[E]** Household leverage fell to **60.4%**, in what NIFD and Caixin describe as a **historic contraction in household debt** ([Yicai](https://www.yicaiglobal.com/news/chinas-macro-leverage-ratio-rose-to-alarming-2956-in-second-quarter-think-tank-says); [Caixin](https://www.caixinglobal.com/2025-10-29/chinas-macro-leverage-ratio-climbs-despite-household-deleveraging-102376995.html)).

**[J]** The prepayment arbitrage is simple: with existing mortgage rates above the yield on any safe asset available to a household, and with expected house price appreciation negative, **prepaying the mortgage is the highest risk-adjusted return available to a Chinese household.** That is a rational individual decision and a macro disaster — it is Koo's debt minimisation, expressed through the mortgage book. It also explains why administrative measures to reprice *existing* mortgages have been a recurring policy tool: they are aimed squarely at killing the prepayment arbitrage, not at stimulating new purchases.

### B.5 What this means for interpreting TSF and the credit impulse *today*

**[J] Four operating rules:**

1. **Never use headline TSF.** Build **ex-government TSF** (TSF less government bonds) and track its growth rate. That is the private-sector credit cycle.
2. **Build a debt-swap-adjusted credit series** if you can — add back the swapped amount to loans, or at minimum flag months with large swap issuance.
3. **The credit impulse's historical 2–3 quarter lead was estimated in a regime where credit flowed to construction.** It should be expected to be **weaker and longer** now, and — critically — **less inflationary**, because the marginal yuan of credit now finances capacity (supply) rather than construction (demand). **[J] A credit impulse that turns positive today should be expected to raise IP and *lower* PPI, the opposite of the historical relationship.** This is the most important re-interpretation in this note.
4. **The correct "credit" variable for forecasting nominal GDP today is not TSF at all.** It is closer to **(ex-government TSF) + (government bond issuance actually disbursed)**, which requires watching fiscal deposits (Section 10).

---

## C. The divergence case: loose liquidity, tight money

### C.1 The configuration

**[E]** Simultaneously, as of September 2026:

| Liquidity conditions — **abundant** | Monetary conditions — **tight** |
|---|---|
| DR007 **1.3726%**, *below* the 1.40% policy rate | TSF growth **7.4%**, slowest on record |
| 10y CGB **1.68%**, one-year low | RMB loans to real economy **+5.6%** |
| PBoC running zero 7d reverse repos, draining | FAI **−6.7%**; property investment **−16.2%** |
| RMB 1.1tn outright reverse repo, ample reserves | Retail sales **+0.6%**; M1−M2 gap **−3.1%** |
| Banks' bond/loan ratio ~**35%**, bonds ~**25%** of assets | CPI-deflated real 1y LPR **+2.2%**; macro leverage **302.3%** |

Sources as cited above, plus bank bond-allocation data from [未央网](https://www.weiyangx.com/464625.html), [金融界](https://bank.jrj.com.cn/2026/05/25134257185840.shtml) and [国信证券 via 发现报告](https://www.fxbaogao.com/detail/5359827). *(Note: the bank bond-holding ratios are from Chinese media summaries of sell-side work and should be re-verified against the NFRA/PBoC primary data before external use.)*

### C.2 The "asset shortage" (资产荒)

**[E]** Chinese analysis of 2025–26 describes the mechanism explicitly: despite large PBoC liquidity injections, commercial banks faced acute **资产荒** pressure — **weak credit demand slowed loan growth while household and corporate deposits stayed high, widening the loan–deposit gap** and pushing banks into bonds. By end-2025 banks' bond holdings had reached roughly a quarter of total assets with a bond-to-loan ratio near 35%, and 2026 outlooks expect large maturities of high-rate deposits plus slowing credit to keep supporting bank bond demand; some houses see the 10y falling to 1.2%–1.5% ([未央网](https://www.weiyangx.com/464625.html); [金融界](https://bank.jrj.com.cn/2026/05/25134257185840.shtml); [西部证券 via Sina](https://finance.sina.com.cn/roll/2025-11-13/doc-infxhcvw5320860.shtml); [中国金融信息网](https://www.cnfin.com/zs-lb/detail/20251120/4338481_1.html)).

**[J] The asset shortage is not a bond-market phenomenon; it is a credit-demand phenomenon with a bond-market symptom.** The causal chain is:

```
Property/LGFV credit demand destroyed (partly by policy)
  → banks have deposits but no acceptable loan assets
    → banks buy bonds
      → yields collapse
        → observers mistake collapsing yields for easy policy
          → and the PBoC, seeing froth, becomes LESS likely to cut
```

**The final step is the perverse one and worth stating plainly: the asset shortage produces a bond rally that reduces the probability of the rate cut the rally is pricing.**

### C.3 Why the transmission is broken

**[J]** Five mechanisms, in order of importance:

1. **Credit is demand-constrained, not supply-constrained.** Every PBoC tool operates on bank *ability* to lend (reserves, capital, funding cost). None operates on borrower *willingness*. When willingness is the binding constraint, the entire toolkit is inert. This is Koo's point and it is correct here.
2. **The collateral channel is inverted.** Falling property prices reduce borrowing capacity faster than rate cuts increase borrowing appetite. In a collateral-based lending system, the price of credit is second-order to the value of collateral.
3. **Expected nominal income growth is too low.** A firm decides on capex against expected nominal revenue growth. With the deflator only just positive and demand-side indicators deteriorating, the expected return on new capacity is poor — and the anti-involution campaign explicitly *punishes* new capacity. **[J] The state is simultaneously trying to encourage investment (via credit tools) and discourage it (via anti-involution). These conflict, and anti-involution is winning.**
4. **The two historical credit absorbers are under administrative deleveraging mandates.** Property (three red lines and their successors) and LGFVs (hidden-debt resolution) are *prohibited* from levering up. Credit supply into those sectors is not price-elastic; it is quota-zero.
5. **Bank risk appetite is impaired.** NIM at 1.41% against rising credit costs means the marginal private-sector loan is not worth writing. State-directed allocation then routes credit to approved sectors (tech, advanced manufacturing) which are (a) less credit-hungry per unit of output and (b) capacity-additive, hence disinflationary.

### C.4 What would fix it

**[J]** In descending order of effectiveness, and none of them is monetary:

1. **Central-government fiscal transfer to households** — direct income support, consumption vouchers, expansion of the social safety net (which would also reduce precautionary saving). This is the IMF's recommendation in substance: maintain an expansionary stance until deflation subsides durably, with the burden on the central balance sheet ([IMF PR 26/053](https://www.imf.org/en/news/articles/2026/02/18/pr-26053-china-imf-executive-board-concludes-2025-article-iv-consultation)). The r−g arithmetic (10y at 1.68% vs nominal GDP at 5.9%) makes this cheap.
2. **Clear the property market** — state purchase of unsold inventory for social housing at market-clearing prices, and a credible price floor. Until buyers stop expecting further falls, no rate is low enough. Note the observed buyer psychology: *"buyers wait for floor prices"* ([Asia Times](https://asiatimes.com/2026/07/chinas-housing-market-free-falls-as-buyers-wait-for-floor-prices/)).
3. **Recognise losses and recapitalise** — write down bad LGFV and developer debt against public capital rather than extending and pretending, which the Atlantic Council argues is what is happening ([Atlantic Council](https://www.atlanticcouncil.org/blogs/econographics/beijing-extends-and-pretends-to-deal-with-its-mountain-of-local-government-debt/)). Zombie debt service absorbs cash flow that would otherwise fund activity.
4. **A credible nominal anchor** — an explicit price-level or nominal-GDP objective, which would do more to shift expectations than any feasible rate cut.
5. **Only then, monetary easing** — which would be effective *once* demand exists, and largely wasted before.

**[J] The uncomfortable conclusion:** the PBoC is not the relevant agent. Watching the PBoC for the turn in China is watching the wrong institution. **Watch the fiscal calendar, the Politburo language on property, and the fiscal deposit drawdown.**

---

## D. The read-across matrix

### D.1 Generic rules — direction of travel

**[P] / [J]** How to read a *move* in each indicator, holding others constant.

| Indicator | Move | Growth (next 2–3q) | Inflation | Policy read-across |
|---|---|---|---|---|
| **M1 growth** | ↑ | **+** (IP, FAI lead ~2q) | **+** PPI (~10m lead, [E/P]) | ↓ easing probability — it's working |
| **M1−M2 gap** | turns **positive** | **++** strongest single signal | **++** deflator | ↓↓ easing probability; risk-on |
| **M1−M2 gap** | widens **negative** | **−−** | **−−** | **↑↑ easing + structural tools + fiscal escalation** |
| **TSF stock growth vs nominal GDP** | wedge **widens** | **+** | **+** but weaker than history ([J]) | ↓ easing probability |
| **TSF ex-government** | ↓ | **−−** private cycle failing | **−** | **↑↑** — proof transmission is broken |
| **Credit impulse** | ↑ | **+** 2–3q lead [P] | **+/−** — now possibly *disinflationary* if capacity-directed [J] | ↓ easing probability |
| **Corporate MLT loans** | ↑ | **+** capex, ~2q | **+** | ↓ easing probability |
| **Household MLT loans** | **negative print** | **−−** property, ~1–2q | **−** | **↑ 5y LPR cut, mortgage measures** |
| **Bill financing share** | ↑ sharply | **0** — the print is fake | **0** | **↑** — evidence demand is absent |
| **Macro leverage ratio** | ↑ on weak nominal GDP | **−** (debt-deflation) | **−** | Ambiguous: ↑ easing need, ↓ political willingness |
| **1y/5y LPR** | ↓ | **+** weak, ~2–4q, mostly from 1 Jan repricing | **+** weak | Already eased; watch WALR follow-through |
| **WALR** | ↓ **with** falling volume | **−** demand collapse | **−** | **↑ easing + fiscal** |
| **Real rate (CPI-deflated)** | ↑ | **−−** households | **−** | **↑↑ easing** |
| **Real rate (PPI-deflated)** | ↓ *via supply cuts* | **0/+** margins, not volumes [J] | **+** but cost-push | **↓ easing probability — the false all-clear** |
| **RRR** | ↓ | **0/+** small | **0** | Signal + bank margin + bond-supply absorption; **not** stimulus |
| **CNY / CFETS** | **appreciating** | **−** exports, 2–3q | **−** imported disinflation | **↑ easing probability** (constraint released) |
| **DR007 − OMO** | **negative** | **−** if with weak loans | **−** | **↑ drain**, not ease; asset-shortage confirmation |
| **R007 − DR007** | **> 40bp** | **0** short run | **0** | **↑↑ immediate injection**; de-risk duration/credit |
| **NCD − policy rate** | **> +20bp** | **−** bank balance-sheet pressure | **0** | **↑↑ RRR cut probability** |
| **Excess reserve ratio** | **high with low DR007** | **−** | **−** | **↑ easing need; low easing efficacy** |
| **Fiscal deposits** | ↑ | **−** issuance without spending | **−** | ↑ PBoC offsetting injections; **bullish bonds** |
| **Fiscal deposits** | ↓ sharply | **++** disbursement, ~1–2q | **+** | **Bearish bonds; buy infrastructure** |
| **Govt bond issuance** | ↑ | **0 until spent** | **0 until spent** | ↑ RRR/outright RR probability |
| **10y CGB** | ↓ | **−** deflation/asset shortage | **−−** | **Ambiguous → slightly ↓ rate-cut probability** (froth concern) |
| **Term spread** | steepens via long end | **+** reflation priced | **+** | ↓ easing probability |
| **LGFV/weak credit spreads** | widen | **−−** | **−** | **↑↑ targeted support, financial-stability response** |
| **CNH HIBOR** | spikes | **0** | **0** | FX defence underway; **constrains domestic easing** |

### D.2 The live matrix — reading it today (12 September 2026)

| Indicator | Reading | Growth signal | Inflation signal | Policy implication |
|---|---|---|---|---|
| TSF growth | **7.4%**, record low | **Negative** | Negative (demand) | Easing bias; fiscal escalation |
| TSF composition | Govt bonds **+15.6%** vs loans **+5.6%** | **Very negative** for private cycle | Negative | Transmission broken → structural tools |
| M1−M2 gap | **−3.1%**, narrowing | Mildly improving | Mildly improving | Neutral; no urgency |
| Corporate real rate (PPI) | **−0.8%** | Margin-positive, volume-neutral | Cost-push positive | **Removes easing urgency** |
| Household real rate (CPI) | **+2.2%** | **Negative** | Negative | Argues for a cut that isn't coming |
| GDP deflator | **+1.6%**, first positive in 12q | Neutral | **Positive** | **↓ easing probability** |
| CPI / core | **0.8% / 1.0%** | Neutral | Weakly positive | Below any plausible target → easing *should* continue |
| Real GDP | **4.3%** Q2, weakest since Q4 2022 | **Negative** | Negative | Growth-target risk builds into Q4 |
| FAI / retail / IP | **−6.7% / +0.6% / 4.5%** | **Very negative** | Negative | Strongest easing argument on the board |
| Property investment | **−16.2%**, ~−20% expected | **Very negative** | Negative | 5y LPR cut, inventory purchase |
| DR007 − OMO | **≈ −3bp** | Negative (demand) | Negative | PBoC **draining**, not easing |
| 10y CGB | **1.68%**, 1y low | Negative | Negative | Froth concern → **crowds out the cut** |
| Bank NIM | **1.41%**, first rise since 2022 | Neutral | Neutral | **Constraint easing at the margin → widens cut window** |
| CNY / CFETS | Through 7.00, **+4.8% YTD** | Negative (exports) | **Negative (imported disinflation)** | **FX constraint released → enables a cut** |
| Macro leverage | **302.3%**, +11.8pp | Negative | Negative | Political brake on easing |
| LPR | **3.00% / 3.50%**, ~10m unchanged | — | — | Market prices only ~**10bp** in 2026 |

**[J] Net read:** growth signals are **clearly negative**; inflation signals are **positive on the supply side and negative on the demand side**; policy signals **conflict** — the two constraints that historically blocked easing (FX and NIM) have both loosened, but the two that now block it (PPI reflation removing urgency, and bond froth) have tightened. **My base case is that the PBoC does very little on price and more on quantity/structure, and that the next genuine easing trigger is a CPI/core rollover or a Q4 growth-target scare — not the credit data.**

---

## E. Scenario map

**[P/J]** Four configurations of the liquidity/money cross, with exemplar episodes. *Historical episode details are widely reported and drawn from practitioner knowledge; they were not re-verified in this session (egress blocked) and are marked accordingly.*

### E.1 Loose liquidity + loose money ("full easing")

**Signature:** DR007 below OMO, credit impulse strongly positive, M1−M2 gap positive and widening, TSF well above nominal GDP.

**Exemplar:** **2020 H1, COVID easing** — RRR and policy rate cuts, relending facilities, a TSF surge and a credit impulse spike. *[P, unverified in-session]* Also **2015–16** post-easing property reflation and the shantytown-redevelopment (PSL-funded) credit wave.

**Asset implications [J]:** bull steepening then bear steepening as reflation prices in; equities and cyclicals rally; commodities rally; CNY firm on growth. **Bonds are the worst asset in the second half of this regime.**

**Policy implications [J]:** the exit is the risk. Chinese easing cycles are short and the normalisation is abrupt.

### E.2 Loose liquidity + tight money ("pushing on a string") — **the current regime**

**Signature:** DR007 at or below OMO, bond yields at lows, banks bloated with bonds, but TSF decelerating, M1−M2 negative, real rates high for households, deflation or supply-driven-only reflation.

**Exemplars:** **2024–2026** (current). Partially **2015 H2–2016 with FX outflows** — the PBoC cut RRR repeatedly while capital outflows drained base money, so easing was partly sterilised by the balance of payments; that episode drove the invention of MLF/PSL as domestic base-money instruments to replace the collapsing 外汇占款 channel. *[P, unverified in-session]*

**Asset implications [J]:** **long duration works and keeps working** — it is the asset-shortage trade. Credit spreads compress on guarantee, not fundamentals. Equities are a barbell: policy-favoured sectors and high-dividend "bond proxies"; avoid the domestic demand complex. CNY driven by the external account and the dollar, not by rate differentials.

**Policy implications [J]:** repeated marginal easing that does not work; escalating use of structural tools; the real turn requires fiscal. **Risk: the trade is crowded and reverses violently when fiscal finally moves** (see E.4).

### E.3 Tight liquidity + tight money ("deleveraging")

**Signature:** DR007 above OMO and volatile, R007−DR007 blowing out, NCD above policy rate, credit impulse deeply negative, credit spreads widening.

**Exemplars:** **June 2013 钱荒 (cash crunch)** — the PBoC deliberately withheld liquidity to punish interbank leverage and maturity transformation; overnight rates spiked into the double digits. *[P, unverified in-session]* **2017–18 deleveraging** — the asset-management new rules (资管新规), shadow-banking crackdown and the resulting collapse in trust and entrusted lending; the credit impulse turned sharply negative and 2018 equity and credit markets were savaged, with a wave of private-sector bond defaults.

**Asset implications [J]:** bear flattening then everything sells off; credit and equities worst; the private sector underperforms the state sector violently (the 2018 signature). **Watch R007−DR007 as the early warning — it widens before the accident.**

**Policy implications [J]:** these episodes end with a capitulation and a rescue. In both 2013 and 2018 the policy pivot came within roughly two quarters of the stress peak.

### E.4 Tightening liquidity + still-loose money ("normalisation / the reversal")

**Signature:** broad credit still expanding and activity recovering, but the PBoC withdraws interbank accommodation; DR007 rises toward and through OMO; bonds sell off while equities hold.

**Exemplars:** **2020 H2 normalisation** — credit remained ample as the recovery took hold but interbank liquidity was withdrawn and the bond market sold off sharply. *[P, unverified in-session]* **November–December 2022, the WMP redemption spiral** — the reopening and property-rescue measures pushed yields up; NAV-marked wealth management products showed losses; retail redemptions forced WMPs to sell bonds; falling prices forced more redemptions. A textbook liquidity-structure accident with no change in the policy rate. *[P, unverified in-session]*

**Asset implications [J]:** **this is the most dangerous regime for the current positioning.** Long-duration CGB positions, bank bond portfolios at ~25% of assets, and WMP/fund holdings are all the same trade. A reflation surprise plus a fiscal expansion would produce simultaneous bond selling from banks, funds and retail.

**Policy implications [J]:** the PBoC has to choose between defending the bond market and validating the recovery. Its 2022 revealed preference was to inject liquidity and stabilise, and I would expect the same again — **but that is a stabilisation, not a reversal of the yield move.**

### E.5 Which scenario are we in, and what is the transition?

**[J]** We are in **E.2**, but with the first cracks of **E.4** visible: PPI is reflating, the deflator has turned, and bank duration risk is at a record. **The transition trigger is fiscal disbursement, not monetary policy.** Watch fiscal deposits. A sharp drawdown, with the 10y at 1.68% and banks at ~35% bond/loan, is the setup for a disorderly repricing.

---

## F. Monitoring playbook

### Daily

**[J]** Five minutes, in this order:

1. **DR007 and the DR007 − 7d OMO spread** (10-day MA, and vs. same calendar window last year)
2. **R007 − DR007** — the accident detector
3. **PBoC open market operations: net injection** (gross minus maturities), and *which tool* — overnight vs 7-day vs outright reverse repo. The **tool choice is the message.**
4. **10y and 30y CGB; the 10y−1y term spread**
5. **USDCNY fixing vs consensus estimate; CNH−CNY basis; CNH HIBOR O/N**

### Weekly

**[J]**

- **1y AAA NCD rate vs the 1y policy rate**, plus NCD issuance volume and completion ratio
- **Bill transfer-discount rates (转贴现) 1M and 6M** — the loan-print tell, especially in the final week of a month or quarter
- **Government bond issuance calendar** and weekly net supply
- **30-city new home sales** and second-hand listing volumes/prices
- **WMP and bond-fund flow proxies** — redemption pressure
- **Steel rebar, cement, chemical prices** — the anti-involution reflation's honesty check (are prices rising on capacity cuts with flat volumes, or on demand?)

### Monthly

**[J]** With the calendar:

| ~Date | Release | What to extract |
|---|---|---|
| 9th | CPI / PPI | **Core CPI** and PPI *momentum* (3m/3m saar), not y/y |
| 10th–15th | PBoC financial statistics | **Decompose**: TSF ex-government; loan split corporate/household × short/MLT; **bill share**; M1−M2 gap |
| 15th | Activity data | FAI by sector (property vs manufacturing vs infra); retail; IP |
| ~18th–20th | MoF fiscal data | **Fiscal deposits** — issued vs spent; land sales revenue |
| Mid-month | 70-city house prices | Primary vs secondary; tier split |
| ~20th | LPR fixing | And whether a deposit-rate action preceded it |
| Month-end | PMI | New orders minus inventories; the employment sub-index |
| Month-end | FX reserves, PBoC balance sheet | Valuation-adjusted reserve change; claims on banks vs FX assets |

### Quarterly

**[J]**

- **PBoC Monetary Policy Report (货币政策执行报告)** — read for **wording changes**, not content. The phrase describing the price objective, the description of the policy stance, and the boxes (专栏) are where policy shifts are pre-announced. Also carries the **WALR**, which is otherwise unavailable.
- **PBoC banker and entrepreneur surveys** — the **loan demand index** is the single best direct measure of the thing that is actually binding.
- **NFRA bank data** — NIM, NPLs, provisioning by bank category (rural commercial banks are the weak link)
- **NIFD macro leverage ratio** by sector
- **GDP deflator and nominal GDP**
- **BIS credit-to-GDP data** ([BIS Data Portal](https://data.bis.org/topics/CREDIT_GAPS/data))
- **IMF Article IV**, when published ([2025 Article IV](https://www.imf.org/en/publications/cr/issues/2026/02/17/peoples-republic-of-china-2025-article-iv-consultation-press-release-staff-report-and-574028))

### Tripwires — specific triggers to change the view

**[J]** Each of these should force a written re-assessment:

**Turn the view more constructive on growth/reflation:**
1. **M1−M2 gap turns positive** → upgrade growth, PPI and equities; reduce duration.
2. **Fiscal deposits fall sharply** for two consecutive months → disbursement underway; buy infrastructure, sell duration.
3. **Household MLT loans positive** for two consecutive months → property stabilising, the highest-multiplier turn.
4. **Corporate MLT loans accelerating with a bill share below 20%** → genuine capex demand.
5. **Core CPI above ~1.5%** → demand-side reflation, not just supply-side.

**Turn the view more defensive:**
6. **R007 − DR007 above 40–50bp for a week** → de-risk duration and credit immediately; a funding accident is forming.
7. **1y AAA NCD above the 1y policy rate by 20bp+ for two weeks** → bank liability stress; raise RRR-cut odds; reduce bank credit exposure.
8. **DR007 above OMO by 20bp+ for five sessions** → liquidity regime change; check whether deliberate or accidental.
9. **Weak-region LGFV spreads widening 50bp+** → the 化债 guarantee is being questioned; the biggest tail risk in Chinese credit.
10. **Household MLT loans negative for two-plus consecutive months** → prepayment wave accelerating; expect an existing-mortgage repricing measure.
11. **Bill financing above 50% of new corporate loans** → the credit print is fabricated; ignore the headline and downgrade activity.

**Policy tripwires:**
12. **A deposit-rate cut via the self-discipline mechanism** → an LPR cut is likely within ~6 weeks. **The highest-value single signal for rates positioning.**
13. **10y CGB below 1.50%** → expect PBoC pushback (jawboning, bond sales, guidance to small banks); the cut becomes *less* likely, not more.
14. **CFETS above ~+8% YTD, or USDCNY below ~6.80** → appreciation becomes a material disinflationary drag; **raises** easing probability.
15. **PPI 3m/3m momentum rolling over while core CPI stays flat** → the anti-involution reflation is failing; the full deflation-easing case rebuilds and real rates re-rise. **This is the key risk to the current reflation consensus.**
16. **Bank NIM back below 1.40%** → the NIM constraint re-binds; no LPR cut without a deposit cut first.
17. **Language change in the MPR** on the price objective or the policy stance → pre-announcement of a shift; act on wording, not on data.

