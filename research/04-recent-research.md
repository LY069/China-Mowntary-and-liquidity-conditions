# New Developments in Monetary and Liquidity Conditions Analysis, 2021–2026, with a China Focus

*Note 04 — Recent research and framework change. Drafted 13 September 2026.*

---

## 0. Purpose, method, and what "verified" means in this note

This note scans what has genuinely **changed** since roughly 2021 — with heavy weight on 2024–2026 — in (a) how China's monetary policy framework actually works, and (b) how economists measure monetary and liquidity conditions. The object is to feed the monitoring tool: which series now carry signal, which have become noise or worse, and what new constructions are worth building.

### 0.1 Methodological caveat — please read before relying on anything here

**Outbound page-fetching was blocked in this session.** Every attempt to open a primary document returned `EGRESS_BLOCKED` from the network proxy, for every domain tried: `bis.org`, `bofit.fi`, `bbvaresearch.com`, `econstor.eu`, `pbc.gov.cn`. Shell-level network access was unavailable by construction.

Consequently **all grounding below comes from web-search result snippets and metadata, not from reading the source documents.** The URLs in this note are real URLs returned by search engines and the titles are as returned; the documents behind them were **not opened and read line-by-line in this session**. This is the same limitation flagged in note 01.

Three verification tiers are used throughout, and every substantive claim carries one:

- **[S]** — *Confirmed from search-result content this session.* A search returned text asserting this, together with a URL. The claim is corroborated at the level of a search snippet, not a primary read.
- **[S²]** — As above, but asserted consistently by **two or more independent sources** returned by different searches. Higher confidence.
- **[BK]** — *Background knowledge, not verified this session.* Asserted from prior knowledge, flagged so the team can check it. **Treat as unverified.**

Where a number or attribution could not be pinned down at all, it says **unverified** in the text. Section 7 collects the open items. Nothing in this note should go into a published product without a primary-source check.

### 0.2 Structure

§1 the PBoC framework reform in detail, with dates. §2 new and improved indicators in the research literature. §3 transmission research. §4 the **NEW INDICATORS TO INCORPORATE** table. §5 **WHAT CHANGED — implications for indicator design**. §6 China-specific data plumbing notes. §7 gaps and unverified items. §8 Bibliography.

---

## 1. The PBoC monetary policy framework reform, 2024–2026

This is the single most consequential development for anyone monitoring Chinese monetary conditions. Between June 2024 and mid-2026 the PBoC moved decisively from a **multi-rate, quantity-anchored, corridor-less** operating framework toward something structurally recognisable as an advanced-economy **single-policy-rate, narrow-corridor, price-based** framework — while simultaneously acquiring a government-bond-trading capability and a set of new liquidity tools. Almost every heuristic a China monetary monitor used before 2024 needs re-examination against this.

### 1.1 The pivot: Pan Gongsheng's Lujiazui Forum speech, June 2024

Governor Pan Gongsheng's keynote at the 15th Lujiazui Forum, delivered in **June 2024** (the forum ran 19–20 June 2024 **[BK]**), is the reference text. Its title as archived is "China's Current Monetary Policy Stance and Evolution of Monetary Policy Framework in the Future" ([PBoC English speech archive](https://www.pbc.gov.cn/en/3688110/3688175/2025080817533718827/index.html); [BIS Review r240621c](https://bis.org/review/r240621c.htm), [PDF](https://bis.org/review/r240621c.pdf)).

What the speech set out, per search-returned summaries **[S²]**:

1. The framework should be **based more on interest rates** and less on quantities.
2. The PBoC should focus on **a single main policy rate** rather than a set of policy rates at different tenors — and that rate should be the **7-day reverse repo (OMO) rate**.
3. The **interest-rate corridor should be appropriately narrowed** ("适当收窄利率走廊宽度").
4. Money and credit aggregates should be **de-emphasised** as intermediate targets, because structural change in the financial system has broken their relationship with activity.
5. The PBoC should develop **government bond trading in open market operations** as a base-money supply channel.
6. The statistical definition of **M1** should be revisited to reflect modern payments.

Sources: [BIS Review r240621c](https://bis.org/review/r240621c.htm); [PBoC speech page](https://www.pbc.gov.cn/en/3688110/3688175/2025080817533718827/index.html); contemporaneous reporting at [Asia Society](https://asiasociety.org/policy-institute/china-sets-stage-third-plenum-unveiling-financial-reforms-and-monetary-policy-direction) and [Peking Ensight](https://pekingensight.substack.com/p/key-takeaways-from-lujiazui-forum); analytical framing at [BOFIT Weekly 2024/36](https://www.bofit.fi/en/monitoring/weekly/2024/vw202436_1/) and [ING THINK](https://think.ing.com/articles/what-to-expect-from-chinas-coming-monetary-policy-framework-reform/).

**Analytical significance for the tool:** a speech is not an institutional change, but in this case essentially every item on the list was implemented within 24 months. It is the best available statement of the PBoC's own reaction function design intent, and it is the right document to re-read when a series behaves unexpectedly.

### 1.2 The 7-day reverse repo rate becomes the sole primary policy rate — July 2024

Two mechanical changes made the designation real, not rhetorical:

- **The 7-day OMO rate was designated the policy rate explicitly and publicly.** The PBoC's Q4 2024 *China Monetary Policy Report* states that the Bank "明示" (explicitly made public) that the open-market 7-day reverse repo operation rate **is the current policy rate** **[S]** ([MPR Q4 2024, Chinese PDF, published 13 Feb 2025](https://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125957/5347949/ad0bc3efe0234fed8cc6260a134a6e95/2025022618190099812.pdf)).
- **The tender method changed to fixed-rate, quantity tendering (固定利率、数量招标).** The same report describes the operating method being "调整为固定利率、数量招标" **[S]**. This is the load-bearing mechanical change: the PBoC now posts a rate and fully accommodates demand at it, rather than auctioning a quantity and discovering a rate. A fixed-rate full-allotment operation is what makes a policy rate a *policy* rate.

The first cut under the new designation: the 7-day reverse repo rate was lowered **10bp from 1.80% to 1.70% in July 2024** **[S²]** ([FXStreet, 22 July 2024](https://www.fxstreet.com/amp/analysis/china-cuts-seven-day-reverse-repo-rate-and-loan-prime-rates-in-move-to-support-growth-202407220918); [Nomura Connects](https://www.nomuraconnects.com/focused-thinking-posts/china-a-major-step-to-modernizing-the-pbocs-policymaking/)). LPR quotes followed the OMO rate down the same day **[BK]** — the sequencing was the signal.

**Implication:** the correct "China policy rate" series in any dashboard from July 2024 onward is the **7-day OMO reverse repo rate**, not the 1-year MLF rate. Historical splices need a break flag at July 2024.

### 1.3 The demotion of the MLF — July 2024, then March 2025

The MLF's downgrade happened in two visible steps:

- **July 2024:** MLF operations were **rescheduled to take place after the LPR quotation**, rather than before it **[S]** ([Central Banking](https://www.centralbanking.com/central-banks/monetary-policy/operating-framework/7972581/pboc-tweaks-lending-facility-as-framework-reform-continues)). Under the old framework the MLF rate was set first and the LPR was quoted as a spread over it; reversing the calendar severed that anchoring publicly.
- **March 2025:** MLF operations switched from a **unified-price (single-rate) tender** to a **fixed-quantity, multiple-price (variable-rate) tender** — "variable-rate tenders with a fixed quantity in the form of multiple-price auction" **[S²]**. Qualified banks now pay *different* rates on the same operation. Announced 24–25 March 2025 ([Bloomberg, 24 Mar 2025](https://www.bloomberg.com/news/articles/2025-03-24/pboc-to-auction-62-billion-one-year-loans-to-banks-on-tuesday); [Forexlive, 25 Mar 2025](https://www.forexlive.com/centralbank/pboc-is-changing-how-it-issues-its-one-year-medium-term-lending-facility-mlf-loans-20250325/); [Central Banking](https://www.centralbanking.com/central-banks/monetary-policy/operating-framework/7972581/pboc-tweaks-lending-facility-as-framework-reform-continues)).

The interpretive point, as reported: **because there is no longer a unified bid rate, "the policy attribute of the MLF rate has been completely phased out"** **[S]** ([Yicai Global](https://www.yicaiglobal.com/news/pbocs-mlf-no-longer-has-policy-oriented-role-after-removal-of-unified-price-bidding-system-expert-says)).

**Critical consequence for data plumbing: from March 2025 there is no single published "MLF rate" with policy meaning.** Any dashboard still plotting a flat MLF line is plotting a fossil. The MLF survives as a *quantity* tool — for example, it ran **ten consecutive months of net injection through December 2025, with 2025 net injection of about RMB1,161bn** **[S]** (per a market summary returned in search; [MacroMicro corridor collection](https://en.macromicro.me/collections/31/cn-finance-relative/109608/cn-interest-rate-corridor-new) — *treat the precise figure as unverified*). Track **MLF net injection volumes**, not the MLF rate.

### 1.4 The interest-rate corridor: 245bp → 70bp (July 2024) → 50bp (June 2026)

This is arguably the most under-appreciated change, and it directly governs how much information a money-market rate deviation carries.

**Before July 2024.** The nominal corridor ran from the **excess-reserve remuneration rate as floor to the SLF rate as ceiling**, a width of roughly **245bp** **[S]**, far too wide to constrain anything. Practically, DR007 wandered.

**July 2024 — temporary overnight repo and reverse repo.** On **8 July 2024** the PBoC announced it would conduct, as needed and in an afternoon window, **temporary overnight repo and temporary overnight reverse repo operations**, priced as spreads to the 7-day OMO rate:

- temporary overnight **repo** (drains liquidity) at **OMO rate − 20bp** → effective **floor**
- temporary overnight **reverse repo** (injects liquidity) at **OMO rate + 50bp** → effective **ceiling**

This created a **de facto 70bp corridor**, down from ~245bp **[S²]** ([Bloomberg, 8 July 2024](https://www.bloomberg.com/news/articles/2024-07-08/pboc-to-conduct-temporary-repos-depending-on-market-conditions); [Yicai Global](https://www.yicaiglobal.com/news/pbocs-temporary-repo-reverse-repo-operations-to-help-stabilize-market-experts-say); [Finadium](https://finadium.com/pboc-to-add-overnight-reverse-repo-and-rmb-repo-facility/); [BBVA Research, "Stocktaking China's new toolkit", July 2025](https://www.bbvaresearch.com/wp-content/uploads/2025/07/202507-Stocktaking-China-new-toolkit-in-its-monetary-policy-framework.pdf)). The Q4 2024 MPR describes the purpose as to "框住货币市场利率波动范围" — to box in the range of money-market rate fluctuation — and to "逐步理顺由短及长的利率传导关系" **[S]** ([MPR Q4 2024](https://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125957/5347949/ad0bc3efe0234fed8cc6260a134a6e95/2025022618190099812.pdf)).

Note the asymmetry: −20/+50 is **not** symmetric, and it is not symmetric in the direction one would naively expect from a bank that wants low rates. The tighter floor is a leaning-against-excess-easing device. **[BK, interpretive]**

**A complication:** the Q1 2025 MPR still refers to "发挥SLF利率作为利率走廊上限的作用" — the SLF rate playing the role of the corridor ceiling **[S]** ([MPR Q1 2025, 9 May 2025](https://cif.mofcom.gov.cn/cif/html/upload/20250512102012618_2025%E5%B9%B4%E7%AC%AC%E4%B8%80%E5%AD%A3%E5%BA%A6%E4%B8%AD%E5%9B%BD%E8%B4%A7%E5%B8%81%E6%94%BF%E7%AD%96%E6%89%A7%E8%A1%8C%E6%8A%A5%E5%91%8A.pdf)). So there are arguably **two ceilings** — a de jure SLF ceiling and a de facto temporary-reverse-repo ceiling — and the tool should probably plot both. This tension is worth resolving against the primary text.

**June 2026 — narrowed to 50bp, and the anchor moves to DR001.** On **17 June 2026** the PBoC adjusted the temporary overnight repo/reverse repo rates to **±25bp** around the 7-day OMO rate, narrowing the corridor **from 70bp to 50bp**, and stated that **DR001** — overnight interbank collateralised repo among depository institutions — will be permitted to trade within ±25bp of the policy rate **[S²]** ([Trivium China, 19 June 2026](https://triviumchina.com/2026/06/19/pboc-exerts-greater-control-over-overnight-lending-rates/); [MacroMicro corridor collection](https://en.macromicro.me/collections/31/cn-finance-relative/109608/cn-interest-rate-corridor-new)).

**The operating target has shifted from the 7-day tenor to the overnight tenor.** The **Q1 2026 MPR** explicitly aims to "guide the overnight rate to operate near the policy rate," formally designating **DR001 as the core money-market anchor**; the Q1 2026 average DR001 was reported at **1.33%** **[S]** ([BigGo Finance summary of PBoC Q1 2026 MPR](https://finance.biggo.com/news/h8P7HJ4B2jrwCtgly29e); corroborating framing at [BigGo, second piece](https://finance.biggo.com/news/gHXeHJ4BYH_ypPqO0PcK); [Standard Chartered view via VT Markets](https://www.global-vtrader.com/en/live-updates/standard-chartered-sees-chinas-pboc-shifting-liquidity-operations-towards-dr001-foreshadowing-overnight-rate-anchor/) reports the PBoC began using DR001 from May 2025 to track deviation from policy).

**This is a live and important change for the monitoring tool.** DR007-minus-OMO has been the workhorse China liquidity spread for a decade. From 2026 the *policy-relevant* deviation measure is **DR001 − 7d OMO rate**, bounded at ±25bp, with breaches of that band now a genuinely informative event rather than routine noise. Build both; weight DR001 from 2026.

### 1.5 New liquidity instruments

**(a) Outright reverse repo (买断式逆回购) — announced 28 October 2024.** The PBoC added outright (title-transferring) reverse repos to the toolkit, to be conducted **monthly with primary dealers, at tenors of no more than one year**, expected to cover **3-month and 6-month** tenors **[S²]** ([gov.cn, 28 Oct 2024](https://english.www.gov.cn/news/202410/28/content_WS671f2a63c6d0868f4e8ec5d2.html); [Bloomberg](https://www.bloomberg.com/news/articles/2024-10-28/pboc-adds-outright-reverse-repo-to-monetary-policy-toolbox); [Central Banking](https://www.centralbanking.com/central-banks/monetary-policy/operating-framework/7962591/pboc-launches-new-reverse-repo-operations); [Finadium](https://finadium.com/china-central-bank-introduces-outright-reverse-repos-amid-year-end-liquidity-concerns/)).

Rationale as reported: it **fills the gap in the liquidity toolbox between one month and one year** — the maturity zone previously served only by the MLF **[S]**. Immediate context: **RMB2.9trn of MLF was maturing in November–December 2024, around 40% of the outstanding MLF balance** **[S]** ([Reuters via US News](https://money.usnews.com/investing/news/articles/2024-10-31/chinas-central-bank-conducts-500-billion-yuan-of-outright-reverse-repos-in-october)).

First operation: **RMB500bn in October 2024, at 6-month tenor** **[S]** (same source). Operations have since become large and routine — e.g. **RMB1.0trn announced 5 September 2025** and **RMB1.1trn announced 30 September 2025** **[S]** ([gov.cn 5 Sep 2025](https://english.www.gov.cn/news/202509/05/content_WS68ba20cbc6d0868f4e8f558c.html); [gov.cn 30 Sep 2025](https://english.www.gov.cn/news/202509/30/content_WS68dbdafbc6d00ca5f9a0690b.html)).

**Crucially, outright reverse repos are conducted as fixed-quantity, multiple-price (variable-rate) tenders with no announced policy rate [BK — unverified].** If that is right, they inject liquidity without emitting a rate signal, which is precisely the design intent: separate the quantity function from the price signal. **Verify this before relying on it.**

**(b) Government bond trading (国债买卖) — from August 2024.** See §1.6 below; it is both a liquidity tool and a yield-curve tool.

**(c) Announced June 2026, not yet operational at time of writing [S]:** a **renminbi repo facility for foreign and international monetary authorities**, and a **macroprudential liquidity support tool for non-bank financial institutions** to be deployed "under specific circumstances" ([Pan Gongsheng, 2026 Lujiazui keynote, BIS Review r260622q](https://www.bis.org/review/r260622q.htm); [gov.cn, six new financial policy measures, 17 June 2026](https://english.www.gov.cn/news/202606/17/content_WS6a324210c6d00ca5f9a0ba94.html); [China Daily](http://europe.chinadaily.com.cn/a/202607/06/WS6a4b0978a310986e2b463ad1.html)). The NBFI facility is the more important of the two for liquidity monitoring: it implies the PBoC now regards **non-bank** funding stress as a policy object, which is consistent with §1.9 and §6.2 below.

### 1.6 PBoC government bond trading: August 2024 start, January 2025 suspension, late-2025 resumption

A compact timeline, all **[S²]** unless noted:

| Date | Event |
|---|---|
| Oct 2023 | Central Financial Work Conference calls for "gradually increasing the central bank's trading of treasuries in open market operations" **[S]** |
| **30 Aug 2024** | First "Government Bond Trading Business Announcement." **Net purchase RMB100bn in August**; the PBoC **bought short-dated and sold long-dated** bonds — a deliberate curve-steepening operation, not QE ([Bloomberg](https://www.bloomberg.com/news/articles/2024-08-30/china-s-pboc-sells-long-term-bonds-buys-short-end-debt); [Central Banking](https://www.centralbanking.com/central-banks/financial-stability/7962167/pboc-starts-trading-chinese-government-bonds); [Business Standard](https://www.business-standard.com/amp/world-news/china-s-central-bank-starts-trading-govt-bonds-to-influence-yield-curve-124083000779_1.html); [Caixin](https://www.caixinglobal.com/2024-09-07/weekly-preview-gao-zhanjun-how-to-interpret-the-central-banks-buying-and-selling-of-government-bonds-102234543.html)) |
| Aug–Dec 2024 | **Cumulative net purchases of RMB1trn.** PBoC government bond holdings rise to **RMB2.88trn at end-2024, 6.5% of total assets** ([Anbound](http://www.anbound.com/Section/ArticleView_35692_1.htm)) |
| **Jan 2025** | **Suspension announced**, citing "persistent excess demand" for government bonds; PBoC says it will resume "at an appropriate time" depending on supply–demand ([SCIO](http://english.scio.gov.cn/m/pressroom/2025-01/15/content_117666228.html); [SCMP](https://www.scmp.com/economy/china-economy/article/3294282/record-low-yields-prompt-suspension-government-bond-purchases-chinas-central-bank); [Central Banking](https://www.centralbanking.com/central-banks/currency/7963600/pboc-suspends-government-bond-purchases)) |
| Jan–May 2025 | Holdings run down to **RMB2.4trn, ~5.4% of assets** ([Anbound](http://www.anbound.com/Section/ArticleView_35692_1.htm)) |
| Sep 2025 | Caixin: "China's central bank taps the brakes on bond buying" / debate on resumption ([Caixin](https://www.caixinglobal.com/2025-09-09/chinas-central-bank-taps-the-brakes-on-bond-buying-102360733.html)) |
| Oct–Nov 2025 | **Resumption.** On **4 November 2025** the PBoC disclosed a **net RMB20bn purchase of CGBs in October** ([Trivium China](https://triviumchina.com/2025/11/05/pboc-resumes-bond-trading-to-smooth-yield-curve/); [Bloomberg](https://www.bloomberg.com/news/articles/2025-10-28/pboc-seen-resuming-bond-purchases-as-it-steps-back-into-market); [Trading Economics](https://tradingeconomics.com/china/government-bond-yield/news/496556)) |

**The interpretive rule this establishes, and it is a strong one:** PBoC bond operations in China are **not** a quantitative-easing signal and should not be read as one. The January 2025 suspension was a *tightening-adjacent* act taken because yields were **too low**. The Bank treats the operation as a **two-sided yield-curve and financial-stability instrument**, not a balance-sheet-expansion instrument. Contemporaneous PBoC bond-market warnings reinforce this: the Bank warned about bubble risk in the bond market in 2024 **[S]** ([Business Standard, Aug 2024](https://www.business-standard.com/world-news/pboc-studies-plan-to-narrow-rate-fluctuation-range-warns-over-bond-risks-124080901646_1.html)) and by July 2025 was supporting banks' "moderate" bond buying while flagging excessive risk-taking, noting that a **30bp rise in 30-year yields implies a >5% price fall** with amplified losses for leveraged holders **[S]** ([Bloomberg, 14 July 2025](https://www.bloomberg.com/news/articles/2025-07-14/pboc-supports-banks-moderate-bond-buying-flags-excessive-risk)).

**Indicator design consequence:** the correct construction is a **signed monthly net-purchase series** (positive = net buy) *plus a separate maturity-composition flag*. "PBoC bought bonds" with no maturity split is uninformative; buying bills while selling 30s is a steepening operation and a mild liquidity injection, not easing of the stance.

### 1.7 De-emphasis of M2 and TSF quantity targets

The PBoC has systematically downgraded aggregates from *intermediate targets* to *observational variables*.

- Framework language: aggregates are to be treated as **"observational, reference, and expectation indicators"** rather than targets, "creating conditions for rate-based adjustment" **[S]**; Pan Gongsheng has "repeatedly emphasised 淡化数量目标 — downplaying quantitative targets" **[S]** ([Jiemian, CEWC interpretation](https://m.jiemian.com/article/13751817.html); [Xinhua interview with Pan, Jan 2026](https://www.news.cn/fortune/20260122/89868f9a1c0b463b89e4bcefccc1b087/c.html); [PBoC Monetary Policy Department interview, Financial News](https://www.pbc.gov.cn/en/3688006/5876310/5877235/index.html)).
- The **Q3 2025 MPR carries a dedicated section on "scientifically viewing total financial indicators" (科学看待金融总量指标)** **[S]** ([MPR Q3 2025, 11 Nov 2025](https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/5896222/2025111111175096136.pdf)). Its argument, as summarised: as the base expands, aggregate growth rates naturally decline, consistent with the shift from high-speed to high-quality growth **[S]**.
- **The structural justification is the collapse of bank loans' share of financing flow.** Per Pan's June 2026 Lujiazui speech: in 2025, **bond and equity financing combined were 47% of the TSF flow, versus 45% for bank loans — the first time bonds+equity exceeded loans** **[S]** ([BIS Review r260622q](https://www.bis.org/review/r260622q.htm); [China Daily](http://europe.chinadaily.com.cn/a/202607/06/WS6a4b0978a310986e2b463ad1.html); market write-up at [A-Share Insights](https://ashareinsights.com/the-lujiazui-forum-2026-1/)). A separate Chinese-language source gives **bond net financing of RMB16trn = 46% of the TSF increase in 2025**, and states **new loans were under 50% of the TSF increase in 2025** **[S]** ([Xinhua interview with Pan](https://www.news.cn/fortune/20260122/89868f9a1c0b463b89e4bcefccc1b087/c.html)). *These two framings are close but not identical (46% bonds alone vs 47% bonds+equity); the discrepancy is unresolved here and should be checked against the primary speech text.*

**Indicator design consequence.** Two, and they point in opposite directions:
1. **The PBoC's own reaction function no longer keys off M2/TSF growth**, so M2/TSF are far weaker as *policy-forecasting* variables. Do not run a Taylor-style rule on aggregate deviations and expect it to predict PBoC moves.
2. But aggregates remain *macro* variables. The problem is that the **composition** has changed so much that headline TSF growth mixes a shrinking loan channel, an expanding government-bond channel, and an expanding corporate-bond channel with very different transmission. **The composition split is now more informative than the headline.**

### 1.8 "Moderately loose" (适度宽松) — Central Economic Work Conference, December 2024

At the CEWC of **9–12 December 2024** China adopted a **"moderately loose" (适度宽松) monetary policy stance for 2025 — the first use of that formulation since 2010** **[S²]** ([CNBC, 9 Dec 2024](https://www.cnbc.com/2024/12/09/china-vows-more-active-fiscal-stimulus-measures-moderately-looser-monetary-policy-next-year-.html); [gov.cn, 14 Dec 2024](https://english.www.gov.cn/news/202412/14/content_WS675cbb55c6d0868f4e8edf12.html); [Conference Board](https://www.conference-board.org/publications/China-Policy-Brief-China-2024-Central-Economic-Work-Conference); [APCO](https://apcoworldwide.com/blog/chinas-2024-central-economic-work-conference-six-key-takeaways/); [Lombard Odier](https://www.lombardodier.com/insights/2024/december/china-s-woes-drive-shift-to.html); [RFA](https://www.rfa.org/english/china/2024/12/11/china-monetary-loosening-policy-explained/)). Content as reported: "reasonable money supply, low interest rates, and a relatively loose monetary and credit environment," alongside RRR and rate cuts and a wider fiscal deficit **[S]**.

**This is a genuinely codable variable.** China's official stance vocabulary is a small, ordered, persistent set — 从紧 / 适度从紧 / 稳健 / 适度宽松 / 宽松 (tight / moderately tight / prudent / moderately loose / loose) **[BK]**. The shift from 稳健 (held since 2011) to 适度宽松 in December 2024 is a discrete, dateable regime marker and belongs in the tool as an **ordinal stance dummy**, not as colour commentary. The stance was reaffirmed for 2026 **[S]** ([Xinhua](https://www.news.cn/fortune/20260122/89868f9a1c0b463b89e4bcefccc1b087/c.html); [PBoC "Highlights of Monetary Policies in H1 2025"](https://www.pbc.gov.cn/en/3688229/3688353/3688362/5846652/index.html)).

### 1.9 The January 2025 M1 redefinition

**Announced December 2024; effective with January 2025 statistics [S²].** The revised **M1 = M0 + corporate demand deposits + personal demand deposits + customer reserve funds held at non-bank payment institutions** ([Global Times, Dec 2024](https://www.globaltimes.cn/page/202412/1324233.shtml)).

Rationale as stated: personal bank cards and mobile payment did not exist when M1 was defined; personal demand deposits now support transfer and payment directly, and prepaid balances at non-bank payment institutions are directly spendable and highly liquid **[S]**.

**Magnitude of the level break: M1 moves from roughly RMB67trn (December 2024, old basis) to roughly RMB112trn (January 2025, new basis)** — i.e. the new series is **~1.67×** the old one. **[S — but sourced only to a single low-authority blog](https://sagarbaniya.substack.com/p/chinas-m1-money-supply-surge-a-statistical); treat the exact figures as unverified and check against [PBoC Financial Statistics Reports](https://www.pbc.gov.cn/en/3688247/3688978/3709137/5810171/index.html).**

**Indicator design consequences — this one is a trap:**
- Any M1 growth-rate series spanning the break is **wrong** unless back-cast. The PBoC published a back-cast history **[BK — unverified, must check]**; if it exists, use it, and if not, the M1 yoy series before/after Jan 2025 must be treated as two different series.
- The famous **"M1−M2 scissors" (剪刀差)** indicator — long used as a proxy for corporate willingness to deploy cash versus hoard it — **changes meaning under the new definition.** Old M1 was essentially *corporate* transaction balances; new M1 folds in household demand deposits and payment-platform float, so the M1−M2 gap now mixes a corporate-activity signal with a household-portfolio signal. **The historical mapping from the scissors gap to industrial activity should be re-estimated on the new basis, not assumed.** **[Interpretive, BK]**
- Offsetting benefit: the new M1 is a **better** measure of economy-wide transaction balances and should in principle be a cleaner nominal-demand proxy going forward.

### 1.10 The 2024 crackdown on manual interest supplementation (手工补息) and idle-funds circulation (资金空转)

In **April 2024** the **Market Interest Rate Pricing Self-Discipline Mechanism** (市场利率定价自律机制) issued an initiative banning banks from paying **supplementary interest ("manual interest supplementation") above the authorised deposit-rate ceiling** — the practice of promising large corporate depositors a top-up beyond the posted rate **[S²]** ([China Banking News](https://www.chinabankingnews.com/p/china-struggles-to-boost-lending); [Caixin opinion, 4 Sep 2024](https://opinion.caixin.com/2024-09-04/102233243.html); [Huxiu](https://m.huxiu.com/article/2895285.html?type=text)).

Stated purpose: **stabilising bank liability costs** **[S]**. The PBoC subsequently described a broader programme: rectifying illegal manual interest subsidies, guiding non-bank institutions to adjust demand-deposit rates in line with policy-rate changes, establishing a reporting mechanism for deposit bidding rates, and standardising corporate deposit service agreements **[S]** ([PBoC Monetary Policy Department interview](https://www.pbc.gov.cn/en/3688006/5876310/5877235/index.html)).

The parallel campaign against **资金空转** ("empty circulation of funds") sought to "wring the water out" of the aggregates — to stop credit being created and immediately redeposited or recycled through arbitrage rather than financing activity **[S]** ([China Banking News](https://www.chinabankingnews.com/p/china-wrings-the-water-out-of-the)).

**Effects, and why this matters enormously for indicator interpretation [S, with interpretive extension]:**
- Corporate deposits **disintermediated** — they left banks for wealth-management products, money funds and other non-bank vehicles once the top-up was banned.
- This mechanically **depressed M1 and M2 growth in 2024** without any corresponding tightening of monetary conditions, and mechanically **inflated non-bank deposits**.
- Therefore: **a large part of the 2024 slump in Chinese money growth was a measurement/regulatory artefact, not a monetary-conditions signal.** A monitoring tool that treated the 2024 M1 collapse as evidence of savage tightening was reading a regulatory reclassification.

**This is the single best cautionary example in the whole note of why raw Chinese aggregates need a regulatory-event overlay.**

### 1.11 Policy-rate and RRR actions, 2024–2026 (timeline for the tool)

| Date | Action | Source tier |
|---|---|---|
| Jul 2024 | 7-day OMO reverse repo **1.80% → 1.70%** (−10bp); LPRs cut alongside | **[S²]** |
| 8 Jul 2024 | Temporary overnight repo/reverse repo introduced at −20bp / +50bp | **[S²]** |
| 30 Aug 2024 | Government bond trading begins, net RMB100bn | **[S²]** |
| Sep 2024 | Broad support package announced at PBoC/NFRA/CSRC press conference (RRR cut, policy-rate cut, mortgage-rate measures) | **[S]** ([CNBC](https://www.cnbc.com/2024/09/24/chinas-central-bank-chief-set-to-hold-press-conference-days-after-fed-rate-cut.html)) |
| 28 Oct 2024 | Outright reverse repo (买断式逆回购) introduced | **[S²]** |
| 8 Nov 2024 | NPCSC approves **RMB10trn** LGFV debt-swap package | **[S²]** |
| 9–12 Dec 2024 | CEWC: **"moderately loose"** stance for 2025 | **[S²]** |
| Jan 2025 | Government bond purchases **suspended**; M1 redefinition takes effect | **[S²]** |
| Mar 2025 | MLF switches to **fixed-quantity, multiple-price** tender | **[S²]** |
| 7 May 2025 | Package announced: 7-day OMO **1.50% → 1.40%** (effective 8 May); **RRR −50bp** (effective 15 May, ~RMB1trn released); structural tool rates cut | **[S²]** ([CNBC](https://www.cnbc.com/2025/05/07/china-to-cut-key-lending-rates-by-10-points-bank-reserve-requirement-ratio-by-50-points-.html); [gov.cn rate](https://english.www.gov.cn/news/202505/07/content_WS681af03ec6d0868f4e8f250c.html); [gov.cn RRR](https://english.www.gov.cn/news/202505/07/content_WS681af001c6d0868f4e8f2509.html)) |
| May 2025 → | 7-day OMO **held at 1.40%** through at least early 2026 | **[S²]** |
| Oct/Nov 2025 | Government bond trading **resumes** (net RMB20bn in Oct, disclosed 4 Nov) | **[S²]** |
| Jan 2026 | **Structural monetary policy tool rates cut 25bp**; 1-year relending **1.50% → 1.25%**, 3-month to 1.2%, 6-month to 1.4% | **[S²]** ([SCIO](http://english.scio.gov.cn/pressroom/2026-01/16/content_118283341.html); [Trading Economics](https://tradingeconomics.com/china/news/news/517507)) |
| Q1 2026 MPR | **DR001 designated the overnight anchor**; explicit "cut RRR and rates" language dropped in favour of "flexibly using a variety of tools"; **imported inflation** newly flagged; **multi-benchmark loan pricing system** floated | **[S²]** |
| 17 Jun 2026 | Corridor narrowed to **±25bp (50bp wide)**; DR001 band formalised; RMB repo facility for foreign monetary authorities and NBFI macroprudential liquidity tool announced | **[S²]** |

**A structurally important 2026 item: the "multi-benchmark loan pricing system."** The Q1 2026 MPR floats moving **away from sole reliance on the LPR** toward a loan-pricing framework that **also references sovereign bond yields and other rates** **[S]** ([BigGo](https://finance.biggo.com/news/76mIRJ4BpwxG186NnABM)). The motivation is bank margin pressure: **aggregate commercial bank NIM fell to 1.40% at end-Q1 2026, a record low** **[S²]** (same source; [Seeking Alpha on NIMs near a "critical point"](https://seekingalpha.com/article/4792302-chinese-banks-nims-near-critical-point); [S&P Global](https://www.spglobal.com/market-intelligence/en/news-insights/articles/2025/3/worlds-largest-lender-expects-net-interest-margin-decline-to-slow-in-2025-88193366)). LPR quotes have been static — **1-year 3.00%, 5-year 3.50%, unchanged for 11–12 consecutive months into April 2026** **[S²]** ([CNBC, 20 Apr 2026](https://www.cnbc.com/2026/04/20/china-keeps-benchmark-lending-rates-unchanged-as-economic-growth-revs-up-amid-mounting-middle-east-risk-mount-.html); [CNBC, 20 Jan 2026](https://www.cnbc.com/2026/01/20/china-lending-rates-lpr-slowing-economic-growth.html)).

**If LPR ceases to be the sole loan benchmark, the LPR series loses much of its remaining value as a monetary-conditions indicator, and the *actual weighted-average new loan rate* published in the MPR becomes the only reliable measure of lending-rate conditions.** Build the tool that way now.

### 1.12 Structural monetary policy tools: a second, parallel policy rate stack

Alongside the single headline policy rate sits a growing set of **structural tools** with their own administered rates: relending for agriculture and small business, sci-tech innovation and technical transformation relending, service-consumption and elderly-care relending, and others **[S²]** ([SCIO](http://english.scio.gov.cn/pressroom/2026-01/16/content_118283341.html); [CF40 Research](https://cf40research.substack.com/p/how-to-understand-the-pbocs-eight); [BBVA Research](https://www.bbvaresearch.com/wp-content/uploads/2025/07/202507-Stocktaking-China-new-toolkit-in-its-monetary-policy-framework.pdf); [PBoC H1 2025 highlights](https://www.pbc.gov.cn/en/3688229/3688353/3688362/5846652/index.html)). Reported quotas include **RMB500bn for agriculture and small business**, **RMB400bn for sci-tech innovation and technical transformation**, and **RMB500bn for service consumption and elderly care** **[S]**.

**Design implication:** "the policy rate" is now *nominally* singular and *effectively* plural. A **quota-weighted average structural-tool rate**, plus **total outstanding structural-tool balance as a share of PBoC assets**, captures a channel of easing that the headline OMO rate completely misses. This is the Chinese analogue of a TLTRO/funding-for-lending adjustment to the stance measure. Note the January 2026 episode is diagnostic: **the PBoC cut structural rates by 25bp while leaving the headline rate unchanged, and this was read as easing that "reduced the immediate need for broader rate cuts"** **[S]**.

---

## 2. New and improved indicators in the research literature, 2021–2026

### 2.1 Shadow / proxy policy rates and high-frequency monetary policy shocks for China

The honest summary: **I found no well-established, actively maintained China shadow-rate series analogous to Wu–Xia for the US.** Wu and Xia's own page states they are **not currently updating** the shadow rate and will resume when the ZLB returns **[S]** ([Jing Cynthia Wu — shadow rates](https://sites.google.com/view/jingcynthiawu/shadow-rates); [Fan Dora Xia](https://sites.google.com/site/fandoraxia/wx-data); [Atlanta Fed Wu–Xia page](https://www.atlantafed.org/cqer/research/wu-xia-shadow-federal-funds-rate)). A methodological caution on shadow rates generally is worth reading before building one: *"A Note of Caution on Shadow Rate Estimates"* (Journal of Money, Credit and Banking, 2020) **[S]** ([RePEc](https://ideas.repec.org/a/wly/jmoncb/v52y2020i4p951-962.html)).

**What has replaced it, and is better suited to China, is high-frequency shock identification.** This is the most usable new-methods development:

- **IMF Working Paper 2024/224, "A New Dataset of High-Frequency Monetary Policy Shocks"** **[S]** ([IMF eLibrary](https://www.elibrary.imf.org/view/journals/001/2024/224/article-A001-en.xml)) — a cross-country high-frequency shock dataset. Whether China is covered and how was **not verified**.
- **"Monetary policy in China: High-frequency shocks and the signaling effects"**, *China Economic Review* (2025) **[S]** ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1043951X25001798); [ResearchGate](https://www.researchgate.net/publication/394868080_Monetary_policy_in_China_High-frequency_shocks_and_the_signaling_effects)). Identifies China MP shocks from **treasury-futures surprises in narrow windows around PBoC announcements**, and separates a **signalling** component.
- **"Can you hear me now? Identifying the effect of Chinese monetary policy announcements"**, *Journal of International Money and Finance* (2024) **[S]** ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0261560624000652)).
- **A daily shock measure from granular interbank borrowing costs.** A seminar paper, "A High-Frequency Measure of Chinese Monetary Policy Shocks," constructs a **daily** China MP shock from granular variation in the **weighted average cost of interbank borrowing**, capturing both quantity- and rate-based policy changes — explicitly motivated by the absence of a reliable single stance proxy in an EM with a multi-dimensional toolkit **[S]** ([University of Macau FSS-DECO seminar](https://fss.um.edu.mo/fss-deco-seminar-a-high-frequency-measure-of-chinese-monetary-policy-shocks/)).
- **A public code/data repository exists:** [github.com/wtsong/china_mpshocks](https://github.com/wtsong/china_mpshocks), described as "High-frequency monetary policy shocks for China" **[S]**. **Not inspected this session** — contents, coverage, licence and update cadence all **unverified**. This is a high-value, low-cost thing to check first.

**Assessment for the tool.** The *granular interbank-cost* approach is conceptually the right one for China, because it does not require a single announced rate to move — it picks up quantity operations, window guidance and structural tools through their effect on realised funding costs. That is exactly the property you want in a framework where the headline rate has been static since May 2025 while structural rates, RRR, outright reverse repos and bond operations have all been moving.

### 2.2 r* for China

Findings, all **[S]**:

- **BIS Working Paper 949, "The natural interest rate in China"** ([BIS](https://www.bis.org/publ/work949.htm)); an accessible companion at [SUERF Policy Note](https://www.suerf.org/publications/suerf-policy-notes-and-briefs/the-natural-interest-rate-in-china/). **Authors not verified this session.** Headline estimates: China's natural rate averaged roughly **3–5% between 1995 and 2010**, declining to about **2% by end-2019**. **Slightly more than half of the decline is attributed to lower potential output growth**, with the remainder from demography, financial development and saving-preference shifts.
- **"Demographic change and natural interest rate of China"**, *Finance Research Letters* ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1544612323011844)) — over the past 20 years the dominant driver was the **falling mortality rate**; more recently falling **fertility and TFP growth** have depressed r* again.
- **"Measuring the natural rate of real interest for the Chinese economy"** (2026) ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1059056026002637)) — a **dissenting** result: finds **no continually near-zero natural rates** for China in the recent decade, i.e. the decline may have stabilised rather than continued toward zero.
- Broader methodological scepticism: **IMF WP 2024/161, "The Mirage of Falling R-stars"** ([IMF eLibrary](https://www.elibrary.imf.org/view/journals/001/2024/161/article-A001-en.xml)); **NBER WP 31949, "Natural and Neutral Real Interest Rates"** ([NBER PDF](https://www.nber.org/system/files/working_papers/w31949/w31949.pdf)); and NY Fed President Williams's 2025 speech **"All the Stars We Cannot See"** ([NY Fed](https://www.newyorkfed.org/newsevents/speeches/2025/wil250825)).

**Assessment.** The **level** of China r* is contested and the confidence bands are wide enough that a point estimate is nearly useless. But the **direction and rough magnitude of the decline are robust across methods**, and that is enough for the tool's actual need. **Recommendation: carry an r* *band* (say 1.5–2.5% real) rather than a point, and report the real-rate gap as a band, explicitly, rather than manufacturing false precision.**

### 2.3 Financial conditions indices: the methods have moved to time-varying factor models

The China FCI literature 2024–2025 has converged on **TVP-FAVAR** and machine-learning variants rather than fixed-weight indices. Papers located **[S]**:

- **"Macro-Financial Condition Index Construction and Forecasting Based on Machine Learning Techniques: Empirical Evidence from China"**, *Symmetry* 17(6):904, 2025 ([DOI](https://doi.org/10.3390/sym17060904)). Reported to build China's FCI from **33 key financial indicators across six major Chinese financial markets** plus **25 external macro variables from China and the US**, monthly, **January 2002 – June 2024**.
- **"Research on Dynamic Measurement and Early Warning of Systemic Financial Risk in China Based on TVP-FAVAR and Deep Learning Model"**, *Systems* 13(8):720, 2025 ([DOI](https://doi.org/10.3390/systems13080720)) — TVP-FAVAR combined with Markov regime-switching, monthly 2010–2024.
- **"Construction and Analysis of Chinese Macro-Financial Stability Index"**, *Computational Economics*, 2024 ([Springer](https://link.springer.com/article/10.1007/s10614-024-10767-2)) — a **TVP-KFAVAR** with kernel-density PCA, monthly January 2002 – June 2024.
- Earlier methodological anchor: **"Constructing dynamic financial conditions indexes by TVP-FAVAR model"** ([ResearchGate](https://www.researchgate.net/publication/315925237_Constructing_a_dynamic_financial_conditions_indexes_by_TVP-FAVAR_model)).
- Application: **"The dynamic impact mechanism of China's financial conditions on real economy and international crude oil market"**, *Heliyon* ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2405844023082932); [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10597845/)).

**Assessment — and a warning.** These are mostly **mid-tier journals**, and none was read this session; quality is **unverified**. But the **methodological message is robust and is the actionable takeaway: fixed-weight FCIs are obsolete for China specifically because the weights are unstable.** When the loan share of financing falls from a majority to 45% in a decade (§1.7), and the policy instrument changes identity in 2024–2026, a constant-weight index is estimating a relationship that no longer exists. **Recommendation: a time-varying-parameter factor model, or at minimum a rolling-window re-weighting with an explicit break at July 2024.** The regime-switching angle in the *Systems* paper is attractive because China's monetary conditions plausibly do switch regime rather than drift.

### 2.4 Text- and LLM-based measures of central bank tone — the clearest new capability

This is where the newest and most directly buildable methods sit.

- **IMF Working Paper 2025/109, "From Text to Quantified Insights: A Large-Scale LLM Analysis of Central Bank Communication"** (June 2025) **[S²]** ([IMF page](https://www.imf.org/en/publications/wp/issues/2025/06/06/from-text-to-quantified-insights-a-large-scale-llm-analysis-of-central-bank-communication-567522); [PDF](https://www.imf.org/-/media/files/publications/wp/2025/english/wpiea2025109-print-pdf.pdf); [RePEc](https://ideas.repec.org/p/imf/imfwpa/2025-109.html)). A multilingual corpus of **74,882 documents from 169 central banks, 1884–2025**, classified along **four dimensions — topic, communication stance, sentiment, and audience** — using a fine-tuned LLM, with a **directional communication index** capturing signals about future rate changes and unconventional measures.
- **"Current stance vs. future guidance: LLM evidence on how PBC communication shapes the yield curve"**, *Economics Letters* vol. 259 (2026) **[S²]** ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0165176525006184); [RePEc](https://ideas.repec.org/a/eee/ecolet/v259y2026ics0165176525006184.html)). **This is the single most on-point paper found.** It compiles PBC communication from the official website for **2005–2024** across **three channels — Monetary Policy Implementation Reports, press releases, and meeting minutes** — and separates **current stance** from **forward guidance**, tracing each to the yield curve.
- **"The Tone of Central Bank Communications and the Market Response: A Cross-Country Analysis Using an AI-Based Monetary Sentiment Index"** ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0939362526000609)).
- Methodological template from another EM: **"Reading Copom's Tone: A Weighted LLM Framework for Hawkish-Dovish Sentiment, Forward Guidance, and Uncertainty"** ([Pith](https://pith.science/paper/2608.07251)).

**Assessment.** The quarterly *中国货币政策执行报告* is unusually well-suited to this treatment: it is long, formulaic, quarterly, bilingual, and its **boilerplate phrase changes are the actual policy signal** — the drop of "cutting the RRR and interest rates" in favour of "flexibly using a variety of monetary policy tools" in the Q1 2026 report (§1.11) is exactly the kind of change a diff-based tone index catches automatically and a human reader misses. **Recommendation: build a PBoC MPR tone index with (a) a rule-based phrase-diff layer over a fixed dictionary of stance formulations, and (b) an LLM stance/guidance classifier, separating current stance from forward guidance per the Economics Letters design.** The rule-based layer is cheap, auditable and probably captures most of the signal; the LLM layer adds nuance. **The boxes/columns (专栏) are the highest-signal section** — they are where the PBoC explains framework changes, and §1 of this note is largely built from them.

### 2.5 Credit impulse refinements

The state of play **[S]**:

- The NY Fed's **"Gauging the Strength of China's Economy in Uncertain Times"** (Liberty Street Economics, April 2025) reports the credit impulse **dipped modestly negative in late 2024 and turned up through Q1 2025**, with increases **smaller than in previous credit cycles**, reflecting caution on local-government borrowing and reluctance to repeat "flood-style" expansion ([Liberty Street Economics](https://libertystreeteconomics.newyorkfed.org/2025/04/gauging-the-strength-of-chinas-economy-in-uncertain-times/)).
- The market standard has moved to an **augmented credit impulse: TSF including local government bonds**, with sell-side variants adding local government bond issuance explicitly to capture both the bank/shadow-lending channel and the fiscal channel ([PipDigest overview](https://piphawk.com/guides/china-credit-impulse-and-aggregate-financing); [Zins Capital](https://zinscapital.substack.com/p/macro-101-leading-indicators-chinas)) — *both are commentary sources, so treat the attribution of specific house methodologies as **unverified***.
- TSF composition as defined: RMB loans, FX loans, entrusted loans, trust loans, undiscounted bankers' acceptances, corporate bonds, local government special-purpose bonds, and domestic equity financing by non-financial firms **[S]**.

**Assessment and a specific recommendation.** Two refinements matter more than the standard ones in the 2024–2026 environment:

1. **Net out the LGFV debt swap.** The RMB10trn swap (§3.3) converts hidden LGFV debt into explicit local government bonds. Those bonds **enter TSF**; the LGFV debt they replace was largely **already in TSF** as loans or bonds, or in some cases outside it. The swap therefore injects a **large refinancing flow with no new spending power** into the credit impulse. **An impulse that treats swap bonds as new credit will systematically overstate stimulus through 2025–2028.** A swap-adjusted TSF series is, in my judgement, the **highest-value single indicator improvement available** for China credit monitoring right now.
2. **Split the impulse by end-use channel** — government bonds, corporate bonds, household loans, corporate loans — because their multipliers now differ enormously and their shares are moving fast (§1.7).

### 2.6 BIS global liquidity indicators and China spillovers

Data confirmed available **[S²]**: the BIS publishes **quarterly Global Liquidity Indicators** alongside the International Banking Statistics. Release pages located: [end-June 2025](https://www.bis.org/statistics/gli2510.htm), [end-March 2025](https://www.bis.org/statistics/gli2507.htm), [end-December 2024](https://www.bis.org/statistics/gli2504.htm), [end-September 2024](https://bis.org/statistics/gli2501.htm), [end-June 2024](https://bis.org/statistics/gli2410.htm); statistical commentaries at [end-June 2025](https://www.bis.org/statistics/rppb2510.htm), [end-September 2025](https://www.bis.org/publications/202601-commentary-ibs-gli), [end-December 2025](https://www.bis.org/statistics/rppb2604.htm).

China-relevant readings reported in search **[S]**:
- **Bank credit to emerging Asia-Pacific contracted by $6bn in Q2 2025, driven by a $36bn decline in credit to borrowers in China.**
- **Cross-border credit to China contracted 15% yoy in Q4 2025.**
- Global backdrop: **dollar credit to non-bank borrowers outside the US accelerated to 6% yoy in Q2 2025 from 3% in Q4 2024**, alongside dollar depreciation and expected Fed easing; the resident/non-resident growth ranking **reversed in Q1 2025** after running the other way from Q2 2020 to Q4 2024.

**Assessment.** Renminbi credit to non-residents was **not** confirmed as a published GLI series; the GLIs principally track **USD, EUR and JPY** credit to non-residents **[S]**. So the "RMB internationalisation as global liquidity" angle is **not** directly available from the GLIs — **unverified whether BIS publishes an RMB series**; check the GLI dataset structure directly.

The genuinely useful China signal here is the **opposite** of the usual framing: **cross-border credit to China is contracting sharply (−15% yoy in Q4 2025)** while domestic policy is "moderately loose." That is an external-tightening offset to domestic easing, and it is invisible in any purely domestic indicator set. **Recommendation: add BIS cross-border claims on China, yoy, as an external-liquidity component of the overall conditions index.** Quarterly and heavily lagged, so it is a confirming series, not a leading one.

### 2.7 Measures of credit misallocation

The most usable recent quantification **[S]**: a **Dallas Fed** analysis (2025) finds the **share of assets of all Chinese non-financial firms held by zombie firms rose from 5% to 16% between 2018 and 2024**, with **real estate rising from 6% to 40%** and **manufacturing from a 2020 low of 4% to 11% in 2024** ([Dallas Fed](https://www.dallasfed.org/research/economics/2025/1223)).

Academic work located **[S]**: *"Zombie firms, misallocation and manufacturing capacity utilization rate: Evidence from China"* (*Economics of Transition and Institutional Change*, 2024, [Wiley](https://onlinelibrary.wiley.com/doi/10.1111/ecot.12398)); *"Zombie firms, state subsidies and aggregate productivity"* (*Economica*, 2025, [Wiley](https://onlinelibrary.wiley.com/doi/10.1111/ecca.12569)); *"Curbing zombie firms: Evidence from China's fair competition review system"* ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0264999326001823)); *"How do zombie firms affect labor mobility"* ([RePEc](https://ideas.repec.org/a/pal/palcom/v12y2025i1d10.1057_s41599-025-05711-0.html)). The reported channels: zombies crowd out normal firms' investment, **reduce healthy firms' capacity utilisation in the same industry and along supply chains**, and suppress innovation efficiency **[S]**.

The World Bank makes the aggregate version of the point: **returns on capital have declined as the capital stock has grown, with a continuously rising capital–output ratio indicating misallocation and diminishing investment productivity** **[S]** ([World Bank China Economic Update, December 2025](https://thedocs.worldbank.org/en/doc/600cd53e2bb24d516b8c3489e5d2c187-0070012025/original/CEU-December-2025-EN.pdf)).

**Assessment.** A zombie share is not a monthly indicator and cannot be. **But the tool needs one misallocation variable, because it is the bridge between "credit conditions are easy" and "credit is not producing growth."** The tractable monthly/quarterly proxies are: **the gap between loan growth to industry and industrial value-added growth**; **the interest-coverage distribution from listed-company filings**; and **the incremental capital–output ratio**. The zombie-share estimates are the annual benchmark against which those proxies should be sanity-checked.

### 2.8 Balance-sheet-recession indicators

The framing has become mainstream rather than fringe. The evidence **[S]**:

- **IMF 2025 Article IV** (published as **IMF Country Report 2026/044**) warns that **prolonged deflation may raise real debt burdens, depress collateral values, and amplify bank and NBFI balance-sheet stress**, and estimates that a **severe negative shock could trigger prolonged deflation reducing the GDP level by 5.4% relative to baseline over five years** ([IMF eLibrary](https://www.elibrary.imf.org/view/journals/002/2026/044/article-A001-en.xml); [Staff report PDF](https://www.imf.org/-/media/files/publications/cr/2026/english/1chnea2026001-source-pdf.pdf); [Executive Board press release, 18 Feb 2026](https://www.imf.org/en/news/articles/2026/02/18/pr-26053-china-imf-executive-board-concludes-2025-article-iv-consultation); [staff mission release, 10 Dec 2025](https://www.imf.org/en/news/articles/2025/12/10/pr-25415-china-imf-staff-completes-2025-article-iv-mission-to-the-peoples-republic-of-china)).
- **Households and LGFVs have both deleveraged over 2020–2025**, with **consumer loans and household business loans showing significant negative growth** **[S]** ([East Asia Forum](https://eastasiaforum.org/2025/09/20/chinas-debt-reckoning/)).
- **Producer prices have fallen for more than three years and the GDP deflator has been negative for ten consecutive quarters** **[S]** (same source, and consistent with IMF framing).
- Practitioner debate: [Allianz GI](https://www.allianzgi.com/en/insights/is-china-getting-into-balance-sheet-recession), [BNP Paribas AM](https://viewpoint.bnpparibas-am.com/should-investors-fret-over-talk-of-china-heading-for-a-balance-sheet-recession/), [China Banking News](https://www.chinabankingnews.com/p/how-china-plans-to-avoid-a-japanese).

**Assessment — the design consequence is severe.** In a balance-sheet recession, **credit demand is the binding constraint, not credit supply.** Every supply-side indicator — policy rate, RRR, reserve balances, banks' lending capacity, quota guidance — can register maximum ease while nothing transmits. **A monitoring tool built only from supply-side series will read "very loose" precisely when the economy is most constrained.** The tool must carry at least one demand-side variable. The candidates: **mortgage prepayment volumes** (§3.2 — the purest revealed-preference measure of households choosing debt reduction over consumption), **household deposit growth relative to income**, **the corporate deposit-to-loan ratio**, and the PBoC's own **quarterly loan-demand index** from its banker survey **[BK — availability unverified]**.

### 2.9 A transferable idea: reserve-ampleness measurement

Not China research, but directly portable and worth flagging. The NY Fed now **publishes a monthly Reserve Demand Elasticity (RDE)** measuring how much the policy rate responds to shifts in reserve supply — a real-time read on whether reserves are ample or approaching scarcity **[S²]** ([NY Fed press release, Oct 2024](https://www.newyorkfed.org/newsevents/news/research/2024/20241017); ["Tracking Reserve Ampleness in Real Time Using Reserve Demand Elasticity"](https://libertystreeteconomics.newyorkfed.org/2024/10/tracking-reserve-ampleness-in-real-time-using-reserve-demand-elasticity); ["When Are Central Bank Reserves Ample?"](https://libertystreeteconomics.newyorkfed.org/2024/08/when-are-central-bank-reserves-ample/); [Fed FEDS Note, "Market-Based Indicators on the Road to Ample Reserves", 31 Jan 2025](https://www.federalreserve.gov/econres/notes/feds-notes/market-based-indicators-on-the-road-to-ample-reserves-20250131.html); [St. Louis Fed Review, May 2025](https://www.stlouisfed.org/-/media/project/frbstl/stlouisfed/publications/review/pdfs/2025/may/monetary-policy-implementation-with-ample-reserves.pdf); [ECB conference paper, Anbil](https://www.ecb.europa.eu/press/conferences/shared/pdf/ANBIL%20SRIYA%20-%20A%20Tale%20of%20Demand%20and%20Supply%20for%20Central%20Bank%20Reserves.pdf)).

A 2025 caution from the same literature is important: standard regressions of rates on aggregate reserves **mainly identify non-bank supply elasticity rather than bank reserve demand** when trading is dominated by non-bank lenders, which **reframes "reserve scarcity" as distributional rather than aggregate** **[S]**.

**Assessment.** A **China RDE** — the elasticity of DR001 (or DR007) to excess reserves — is buildable and would be genuinely novel. **It is now much more interpretable than before**, because a narrow corridor (§1.4) gives the elasticity a well-defined meaning: inside a ±25bp band, a rising elasticity is an early-warning signal of funding scarcity that the level of DR001 will not show until the band is breached. The distributional caveat applies with force in China, where **small and rural banks** face different funding conditions from the big five **[BK]**.

---

## 3. Transmission research

### 3.1 Post-LPR-reform transmission potency

The LPR reform (August 2019) linked bank lending rates to the MLF via bank quotes; the 2024–2026 reform has broken the MLF anchor without yet replacing it cleanly. Findings **[S]**:

- **Transmission is asymmetric and incomplete**, with reported pass-through efficiency of roughly **40–60%** ([summarised across sources including CEP](https://www.cepweb.org/monetary-policy-reloaded-towards-a-new-growth-path-in-china/)). *The specific 40–60% figure came from a search summary without a clean primary attribution — **treat as unverified**.*
- **NIM compression is the binding constraint on further transmission.** LPR reform has pushed NIMs steadily down; **over 50% of lenders report lending rates at or below the LPR** **[S]** ([BBVA China Banking Monitor 2025](https://www.bbvaresearch.com/wp-content/uploads/2025/04/China-banking-monitor-2025.pdf)). Aggregate NIM hit **1.40% at end-Q1 2026**, a record low **[S²]**.
- The **deposit side** is where the PBoC has intervened most aggressively — the 手工补息 ban (§1.10), deposit-rate self-discipline, and guidance to non-banks on demand-deposit pricing are all **liability-cost management to preserve transmission capacity** **[S]** ([PBoC Monetary Policy Department interview](https://www.pbc.gov.cn/en/3688006/5876310/5877235/index.html)).
- **NBER WP 31396, "Deposit Regulation and Monetary Transmission in China"** ([NBER PDF](https://www.nber.org/system/files/working_papers/w31396/w31396.pdf)) is the relevant academic treatment **[S]**.
- **NBER WP 34056 (2025), "A Trade-off Between Monetary Policy Transmission and Systemic Risk in China"** ([NBER](https://www.nber.org/papers/w34056); [RePEc](https://ideas.repec.org/p/nbr/nberwo/34056.html)): **access to interbank wholesale funding amplifies transmission of easing to lending by non-state banks, but heightens their vulnerability to systemic risk in downturns** **[S]**. This is an important and underappreciated result for indicator design — it says **the interbank funding position of small and non-state banks is a transmission variable, not just a stability variable.**
- Structural background: **NBER WP 27763**, "Monetary Stimulus Amidst the Infrastructure Investment Spree" ([NBER](https://www.nber.org/papers/w27763)), finds infrastructure investment **weakened** transmission to private-firm credit while **reinforcing** it for SOE loans; **NBER WP 22650**, "Impacts of Monetary Stimulus on Credit Allocation and the Macroeconomy" ([NBER](https://www.nber.org/papers/w22650)), finds post-2008 transmission ran disproportionately through real estate and heavy industry.

**Design implication:** a single economy-wide pass-through coefficient is the wrong object. **Transmission in China is ownership- and sector-conditional, and the conditioning variables (SOE vs private, large bank vs small bank, wholesale-funded vs deposit-funded) are themselves observable.** At minimum the tool should carry the **large-bank vs small-bank funding spread** and the **weighted-average new corporate loan rate** separately from the LPR.

### 3.2 The property channel

The channel is structurally impaired, and the mechanism is now well documented **[S]**:

- **Mortgage rates in China are set as LPR plus a fixed local margin**, where the LPR component **resets only annually** and **the margin is fixed for the life of the loan** ([ABFER 2025 conference paper, "Rigid Mortgage Rates and Monetary Policy Transmission"](https://www.abfer.org/media/abfer-events-2025/annual-conference/papers-household-finance/AC25P7048_Rigid-Mortgage-Rates-and-Monetary-Policy-Transmission.pdf)). Policy easing therefore reaches the **existing mortgage stock** slowly and incompletely.
- The revealed household response to easing has been **prepayment, not new borrowing**: **total prepayments in 2022 reached RMB4.7trn, about 12% of outstanding mortgage loans** **[S]** (same source; see also [VoxChina, "Mortgage Prepayment in China"](https://voxchina.org/show-3-424.html)).
- Conditions as of Q4 2025: average mortgage rates **flat** across most Chinese cities, and **new lending activity weakened in Q4 2025 despite stabilised mortgage costs and improved affordability** **[S]** ([Global Property Guide](https://www.globalpropertyguide.com/asia/china/price-history)).
- Policy has been explicitly bent toward property and regional deleveraging **[S]** ([China Banking News](https://www.chinabankingnews.com/p/china-pressgangs-monetary-policy)).

**This is the balance-sheet-recession mechanism made concrete**: rate cuts produce **deleveraging** rather than **releveraging**. **Indicator recommendation: track mortgage prepayment (or, as a proxy, the gap between gross mortgage origination and net mortgage stock growth) as a first-class monetary-conditions variable, with the sign convention that high prepayment = tight effective conditions despite low rates.**

### 3.3 The LGFV channel and the debt swap

The **RMB10trn package approved by the NPC Standing Committee on 8 November 2024** **[S²]**: a **RMB6trn increase in the local government debt ceiling over three years** for replacing hidden debt, **plus RMB800bn per year of local government special bonds over five years (RMB4trn)** ([CGTN](https://news.cgtn.com/news/2024-11-08/China-s-top-legislature-approves-bill-to-raise-local-govt-debt-ceiling-by-6-trillion-yuan-1ymH5tCk18I/p.html); [CNN](https://www.cnn.com/2024/11/08/business/china-economy-hidden-debt-intl-hnk); [NBC](https://www.nbcnews.com/news/world/china-announces-14-trillion-five-years-tackle-local-governments-hidden-rcna179269); [Beijing Review](http://www.bjreview.com/Business/202411/t20241118_800384310.html)).

Scale of the problem: **hidden debt of RMB14.3trn at end-2023, targeted to fall to RMB2.3trn by 2028** **[S]**.

Assessments diverge sharply, which is itself informative:
- **Bank-balance-sheet benefit is real and quantified**: swapped exposures move to special-bond investments with a **20% risk weight**, versus **75–100%** for the loans they replace, and provisioning expense falls **[S]** ([S&P Global](https://www.spglobal.com/market-intelligence/en/news-insights/articles/2024/11/china-s-12-trillion-yuan-debt-swap-to-ease-local-debt-pressure-bank-margins-86126459)).
- **Macro impact is contested**: Carnegie characterises it as "**a 10 trillion RMB accounting exercise**" ([Carnegie](https://carnegieendowment.org/posts/2024/11/a-10-trillion-rmb-accounting-exercise?lang=en)); the Atlantic Council frames it as "**extend and pretend**" ([Atlantic Council](https://www.atlanticcouncil.org/blogs/econographics/beijing-extends-and-pretends-to-deal-with-its-mountain-of-local-government-debt/)).

**Design implication, restating §2.5.1 because it is the most important single adjustment in this note:** the swap **inflates TSF and government-bond issuance without creating new spending power**, while **freeing bank risk capacity**. It therefore **raises measured credit growth and lowers measured credit quality risk simultaneously, for reasons that have nothing to do with the monetary stance.** Build the swap-adjusted series.

### 3.4 The right deflator for China's real policy rate

This is unresolved in the literature and the tool should treat it as a **judgement parameter, not a fact**.

What is confirmed about the price data **[S²]**:
- **Headline CPI averaged 0% in 2025**; **core inflation picked up modestly**; **the GDP deflator continued to decline** ([IMF Executive Board press release, Feb 2026](https://www.imf.org/en/news/articles/2026/02/18/pr-26053-china-imf-executive-board-concludes-2025-article-iv-consultation)).
- **The GDP deflator has been negative for ten consecutive quarters, and PPI has fallen for more than three years** **[S]** ([East Asia Forum](https://eastasiaforum.org/2025/09/20/chinas-debt-reckoning/)).
- **Real interest rates stayed relatively high and credit demand remained subdued in early 2025 despite easing measures** **[S]** ([World Bank China Economic Update, June 2025](https://thedocs.worldbank.org/en/doc/8ae5ce818673952a85fee1ee57c3e933-0070012025/original/CEU-June-2025-EN.pdf)).
- The PBoC's Q1 2026 MPR newly flags **imported inflation** risk from commodity prices **[S]**.

**I did not find a paper this session that adjudicates the deflator choice for China's real policy rate. That is a genuine gap.** What follows is **[BK, interpretive — flagged as the author's reasoning, not a literature finding]**:

- **CPI** understates the real burden on **producers and borrowers**. It is weighted toward food and services and has been held near zero partly by administered and supply-side factors. A real rate deflated by CPI (1.40% − 0.0% ≈ **+1.4%**) understates tightness for the corporate sector.
- **PPI** overstates the burden on **households and services firms** and is dominated by global commodities and domestic overcapacity. A PPI-deflated real rate is very high and very volatile, and attributes to monetary policy what is mostly an industrial-overcapacity phenomenon.
- **The GDP deflator** is the theoretically correct economy-wide price of domestic output and is the right deflator for a **debt-burden** interpretation — nominal GDP growth is what services nominal debt. It is quarterly, revised, and in China carries measurement concerns **[BK]**.
- **Core CPI** is best for the **demand-pressure** interpretation but is the narrowest.

**Recommendation: report the real policy rate as a fan across all four deflators rather than choosing one, and make the GDP-deflator version the headline for debt-sustainability and balance-sheet-recession questions, core CPI the headline for demand questions.** The spread between the CPI-deflated and GDP-deflator-deflated real rate is itself a useful indicator — it widens exactly when the "China isn't that tight" and "China is brutally tight" camps disagree most, which is when the tool should flag ambiguity rather than produce a number.

---

## 4. NEW INDICATORS TO INCORPORATE

Build difficulty assumes the team already has CEIC/Wind-class access to Chinese data plus the PBoC website. "Easy" ≈ days; "Medium" ≈ weeks; "Hard" ≈ a project.

| Indicator | Rationale | Source | Data availability | Build difficulty |
|---|---|---|---|---|
| **DR001 − 7d OMO rate** (with ±25bp corridor bands) | From Q1 2026 the PBoC's declared operating target is the **overnight** rate held within ±25bp of the policy rate. This is now the primary real-time read of whether the PBoC is delivering its intended stance. | [PBoC Q1 2026 MPR summary](https://finance.biggo.com/news/h8P7HJ4B2jrwCtgly29e); [Trivium](https://triviumchina.com/2026/06/19/pboc-exerts-greater-control-over-overnight-lending-rates/); rates from [CFETS/ChinaMoney](https://www.chinamoney.org.cn/english/bmkfrr/) | DR001/DR007 daily via CFETS and [PBoC DR007 page](https://www.pbc.gov.cn/en/3688006/3689169/3753752/index.html); corridor bands must be hand-coded by regime | **Easy** |
| **Corridor width and position** (temporary O/N repo & reverse repo bounds; SLF ceiling plotted separately) | Corridor went 245bp → 70bp (Jul 2024) → 50bp (Jun 2026). The *same* 15bp DR deviation means something completely different in each regime. Normalise deviations by corridor width. | [Bloomberg 8 Jul 2024](https://www.bloomberg.com/news/articles/2024-07-08/pboc-to-conduct-temporary-repos-depending-on-market-conditions); [Trivium Jun 2026](https://triviumchina.com/2026/06/19/pboc-exerts-greater-control-over-overnight-lending-rates/); [MacroMicro](https://en.macromicro.me/collections/31/cn-finance-relative/109608/cn-interest-rate-corridor-new) | Regime dates known; SLF rate published by PBoC | **Easy** |
| **Swap-adjusted TSF / credit impulse** (strip LGFV debt-swap bond issuance) | RMB10trn of swap bonds enter TSF as refinancing with no new spending power. Unadjusted impulse **systematically overstates stimulus 2025–2028**. Highest-value single fix. | [CGTN](https://news.cgtn.com/news/2024-11-08/China-s-top-legislature-approves-bill-to-raise-local-govt-debt-ceiling-by-6-trillion-yuan-1ymH5tCk18I/p.html); [Carnegie](https://carnegieendowment.org/posts/2024/11/a-10-trillion-rmb-accounting-exercise?lang=en); [NY Fed](https://libertystreeteconomics.newyorkfed.org/2025/04/gauging-the-strength-of-chinas-economy-in-uncertain-times/) | TSF components monthly (PBoC); refinancing/swap bond split needs MoF issuance data and judgement | **Medium** |
| **TSF composition shares** (loans / govt bonds / corporate bonds / equity) | Loans fell below ~45–50% of TSF flow in 2025 for the first time; headline growth now averages channels with very different multipliers. The mix is more informative than the level. | [Pan, 2026 Lujiazui, BIS Review](https://www.bis.org/review/r260622q.htm); [Xinhua interview](https://www.news.cn/fortune/20260122/89868f9a1c0b463b89e4bcefccc1b087/c.html) | Monthly from PBoC TSF release | **Easy** |
| **PBoC net government bond purchases, signed, with maturity split** | Not QE. Two-sided curve/stability tool; suspended Jan 2025 *because yields were too low*. Only interpretable with the buy-short/sell-long split. | [Central Banking](https://www.centralbanking.com/central-banks/financial-stability/7962167/pboc-starts-trading-chinese-government-bonds); [SCIO](http://english.scio.gov.cn/m/pressroom/2025-01/15/content_117666228.html); [Trivium](https://triviumchina.com/2025/11/05/pboc-resumes-bond-trading-to-smooth-yield-curve/) | Monthly PBoC "Government Bond Trading Business Announcement"; **maturity split is not always disclosed — partial** | **Medium** |
| **Outright reverse repo (买断式逆回购) outstanding & monthly gross** | The new 1m–1y liquidity channel that replaced the MLF's quantity role. Missing it means missing most of the medium-term liquidity provision post-2024. | [gov.cn 28 Oct 2024](https://english.www.gov.cn/news/202410/28/content_WS671f2a63c6d0868f4e8ec5d2.html); operation announcements e.g. [Sep 2025](https://english.www.gov.cn/news/202509/30/content_WS68dbdafbc6d00ca5f9a0690b.html) | Monthly PBoC announcements from Oct 2024; short history | **Easy** |
| **MLF net injection (volume, not rate)** | The MLF rate lost policy meaning in Mar 2025; the MLF survives as a quantity tool with material net injections. Plotting the rate is plotting a fossil. | [Yicai](https://www.yicaiglobal.com/news/pbocs-mlf-no-longer-has-policy-oriented-role-after-removal-of-unified-price-bidding-system-expert-says); [Central Banking](https://www.centralbanking.com/central-banks/monetary-policy/operating-framework/7972581/pboc-tweaks-lending-facility-as-framework-reform-continues) | Monthly PBoC operation announcements | **Easy** |
| **Quota-weighted structural-tool rate + structural balance / PBoC assets** | A second, parallel policy-rate stack. Jan 2026: structural rates cut 25bp with the headline rate unchanged — easing invisible to a headline-rate monitor. | [SCIO Jan 2026](http://english.scio.gov.cn/pressroom/2026-01/16/content_118283341.html); [CF40](https://cf40research.substack.com/p/how-to-understand-the-pbocs-eight); [BBVA](https://www.bbvaresearch.com/wp-content/uploads/2025/07/202507-Stocktaking-China-new-toolkit-in-its-monetary-policy-framework.pdf) | Rates announced; **balances disclosed quarterly in MPR annexes, coverage incomplete** | **Medium** |
| **PBoC MPR tone index** (phrase-diff layer + LLM stance/guidance classifier) | Framework changes are announced in MPR 专栏 columns and in boilerplate diffs (e.g. dropping "cut RRR and rates" in Q1 2026). Separating *current stance* from *forward guidance* has demonstrated yield-curve predictive content. | [*Economics Letters* 259 (2026)](https://www.sciencedirect.com/science/article/abs/pii/S0165176525006184); [IMF WP 2025/109](https://www.imf.org/en/publications/wp/issues/2025/06/06/from-text-to-quantified-insights-a-large-scale-llm-analysis-of-central-bank-communication-567522) | Full MPR archive public, Chinese + English, quarterly back to 2001 ([PBoC](https://www.pbc.gov.cn/en/3688229/3688353/3688356/5624504/5846668/index.html)) | **Medium** |
| **Official stance ordinal** (稳健 → 适度宽松, dated regime dummy) | Discrete, persistent, dateable regime marker; changed Dec 2024 for the first time since 2010. Cheap and genuinely informative. | [CNBC 9 Dec 2024](https://www.cnbc.com/2024/12/09/china-vows-more-active-fiscal-stimulus-measures-moderately-looser-monetary-policy-next-year-.html); [gov.cn](https://english.www.gov.cn/news/202412/14/content_WS675cbb55c6d0868f4e8edf12.html) | CEWC communiqués + MPRs, hand-coded once | **Easy** |
| **Real policy rate fan** (CPI / core CPI / PPI / GDP deflator) + the CPI-vs-deflator spread | No settled answer on the right deflator; the four disagree by several percentage points. The spread itself flags when the "how tight is China" debate is unresolvable. | [IMF Feb 2026](https://www.imf.org/en/news/articles/2026/02/18/pr-26053-china-imf-executive-board-concludes-2025-article-iv-consultation); [World Bank Jun 2025](https://thedocs.worldbank.org/en/doc/8ae5ce818673952a85fee1ee57c3e933-0070012025/original/CEU-June-2025-EN.pdf) | CPI/PPI monthly (NBS); GDP deflator quarterly, revised | **Easy** |
| **r\* band (not a point) and the real-rate gap as a band** | Estimates cluster ~2–3% with wide bands and at least one 2026 dissent; a point estimate manufactures false precision. | [BIS WP 949](https://www.bis.org/publ/work949.htm); [SUERF note](https://www.suerf.org/publications/suerf-policy-notes-and-briefs/the-natural-interest-rate-in-china/); [2026 dissent](https://www.sciencedirect.com/science/article/pii/S1059056026002637) | Published estimates are periodic and sparse; own estimation is a project | **Hard** |
| **Mortgage prepayment proxy** (gross origination − net stock growth) | Purest revealed-preference measure of households choosing deleveraging over spending. Rate cuts have produced prepayment, not new borrowing. Sign convention: high prepayment = tight *effective* conditions. | [ABFER 2025](https://www.abfer.org/media/abfer-events-2025/annual-conference/papers-household-finance/AC25P7048_Rigid-Mortgage-Rates-and-Monetary-Policy-Transmission.pdf); [VoxChina](https://voxchina.org/show-3-424.html) | **Prepayment not directly published**; proxy needs PBoC household loan stock + origination estimates | **Medium/Hard** |
| **Non-bank deposits and WMP balances** (level, growth, share of M2) | Post-手工补息, funds migrate between bank deposits and NBFI vehicles, mechanically moving M1/M2 with no change in conditions. NBFI deposits ~RMB30trn ≈10% of M2 (Feb 2025); WMPs RMB30.67trn (Jun 2025). | [Miao Yanliang via East Is Read](https://www.eastisread.com/p/miao-yanliang-explains-chinas-large); [SSE/Yicai](https://english.sse.com.cn/news/newsrelease/voice/c/c_20250522_10779736.shtml) | Non-bank deposits monthly in PBoC financial statistics; WMP balances semi-annual from the WMP registration centre | **Easy/Medium** |
| **Regulatory-event overlay** (手工补息 Apr 2024; 资金空转; M1 redefinition Jan 2025; deposit self-discipline) | A large share of the 2024 money-aggregate slump was a regulatory artefact. Without a dated overlay the tool will read reclassification as tightening. | [China Banking News](https://www.chinabankingnews.com/p/china-struggles-to-boost-lending); [Caixin](https://opinion.caixin.com/2024-09-04/102233243.html); [Global Times](https://www.globaltimes.cn/page/202412/1324233.shtml) | Hand-coded event list; permanent maintenance item | **Easy** |
| **Excess reserve ratio (超额准备金率)** | The cleanest published measure of genuine banking-system liquidity slack. 1.0% end-Mar 2025 → 1.4% end-Jun 2025. | [PBoC MPR Q2 2025](http://www.pbc.gov.cn/en/3688229/3688353/3688356/5624504/5846668/index.html) | **Quarterly only**, published in the MPR text | **Easy** |
| **China Reserve Demand Elasticity** (sensitivity of DR001 to excess reserves) | Rising elasticity signals approaching funding scarcity *before* the rate level shows it — and a narrow corridor makes it interpretable. Novel for China. | Method: [NY Fed RDE](https://libertystreeteconomics.newyorkfed.org/2024/10/tracking-reserve-ampleness-in-real-time-using-reserve-demand-elasticity); [Fed FEDS Note](https://www.federalreserve.gov/econres/notes/feds-notes/market-based-indicators-on-the-road-to-ample-reserves-20250131.html) | Needs daily DR001 + reserve proxies; **quarterly excess-reserve ratio is a binding constraint** | **Hard** |
| **Time-varying-parameter FCI** (TVP-FAVAR, or rolling re-weighted, with a Jul 2024 break) | Fixed weights estimate a relationship that no longer exists once the instrument changes identity and the financing mix shifts. | [*Symmetry* 17(6):904](https://doi.org/10.3390/sym17060904); [*Systems* 13(8):720](https://doi.org/10.3390/systems13080720); [*Computational Economics* 2024](https://link.springer.com/article/10.1007/s10614-024-10767-2) | Inputs all available; estimation is the work | **Hard** |
| **High-frequency MP shock series for China** (interbank-cost or treasury-futures based) | Picks up quantity operations, window guidance and structural tools that a static headline rate misses entirely — essential when the OMO rate hasn't moved since May 2025. | [*China Economic Review* 2025](https://www.sciencedirect.com/science/article/abs/pii/S1043951X25001798); [*JIMF* 2024](https://www.sciencedirect.com/science/article/pii/S0261560624000652); [UM seminar](https://fss.um.edu.mo/fss-deco-seminar-a-high-frequency-measure-of-chinese-monetary-policy-shocks/); possible code at [github.com/wtsong/china_mpshocks](https://github.com/wtsong/china_mpshocks) | Needs intraday treasury-futures or granular interbank data; **check the GitHub repo first — may be free** | **Hard** (Medium if the repo is usable) |
| **BIS cross-border claims on China, yoy** | External liquidity tightening (−15% yoy Q4 2025) offsetting domestic ease — invisible in any domestic series. | [BIS GLI releases](https://www.bis.org/statistics/gli2510.htm); [statistical commentary](https://www.bis.org/statistics/rppb2604.htm) | Quarterly, ~3-month lag; free from BIS | **Easy** |
| **Misallocation proxy** (industrial loan growth − IVA growth; listed-firm interest-coverage distribution; ICOR) | Bridges "conditions are easy" and "credit isn't producing growth." Zombie asset share rose 5%→16% 2018–2024 (real estate 6%→40%). | [Dallas Fed 2025](https://www.dallasfed.org/research/economics/2025/1223); [World Bank Dec 2025](https://thedocs.worldbank.org/en/doc/600cd53e2bb24d516b8c3489e5d2c187-0070012025/original/CEU-December-2025-EN.pdf) | Loan/IVA monthly; firm-level annual; zombie shares are an annual benchmark only | **Medium** |
| **Weighted-average new loan rate** (corporate and mortgage, from the MPR) | If LPR ceases to be the sole benchmark under a multi-benchmark system, this becomes the *only* reliable lending-conditions measure. | [BigGo on Q1 2026 MPR](https://finance.biggo.com/news/76mIRJ4BpwxG186NnABM); rates published in MPR | **Quarterly**, in MPR text; occasionally reported in press conferences | **Easy** |
| **Large-bank vs small-bank funding spread** | NBER WP 34056: wholesale funding access amplifies transmission to non-state banks *and* their downturn vulnerability. It is a transmission variable, not only a stability variable. | [NBER WP 34056](https://www.nber.org/papers/w34056) | NCD issuance rates by bank tier, daily/weekly via CFETS/Wind | **Medium** |

---

## 5. WHAT CHANGED — implications for indicator design

1. **The policy rate changed identity, and the series must change with it.** From July 2024 the **7-day OMO reverse repo rate** is the sole primary policy rate, set by **fixed-rate, quantity tendering**. From March 2025 the **MLF rate has no policy attribute at all**. Any chart still showing an "MLF policy rate" line after March 2025 is showing an artefact. **Track MLF volumes; drop the MLF rate.** **[S²]**

2. **The corridor is now narrow enough that money-market deviations mean something — and the meaning changes by regime.** 245bp → 70bp (Jul 2024) → 50bp (Jun 2026). A 15bp DR007 deviation was noise in 2023 and is a third of the corridor in 2026. **Normalise all money-market deviations by the contemporaneous corridor width**, or the series is not comparable through time. **[S²]**

3. **The operating target moved from the 7-day to the overnight tenor.** Q1 2026 MPR designates **DR001** as the anchor, bounded ±25bp. **DR007−OMO, the decade-long workhorse spread, is being demoted in favour of DR001−OMO.** Build both; weight DR001 from 2026 forward. **[S²]**

4. **M2 and TSF have been formally demoted from targets to "observational indicators," so they no longer forecast the PBoC's own behaviour** — but they remain macro variables. The failure mode to avoid is treating aggregate weakness as a predictor of easing. **The information has migrated from the level to the composition**: loans fell below ~45–50% of TSF flow in 2025, so headline TSF now averages channels with materially different multipliers. **Composition shares become first-class indicators; headline TSF growth becomes a weak summary.** **[S²]**

5. **A large part of the 2024 money-aggregate slump was a regulatory artefact, not tightening.** The April 2024 手工补息 ban pushed corporate deposits out of banks into NBFI vehicles, mechanically depressing M1 and M2 while inflating non-bank deposits. **Aggregates in China now require a dated regulatory-event overlay as a permanent feature of the tool, not a footnote.** **[S²]**

6. **M1 has a structural break in January 2025 and the "M1−M2 scissors" indicator has changed meaning.** The new M1 adds household demand deposits and non-bank payment float, roughly 1.67× the old level. The scissors gap used to be a fairly clean corporate-cash-activation signal; it now mixes corporate and household portfolio behaviour. **Any historical mapping from the scissors gap to industrial activity must be re-estimated, not assumed to carry over.** **[S, with the multiple unverified]**

7. **PBoC bond buying is not QE and must never be scored as easing.** The January 2025 suspension happened **because yields were too low**; the Bank operates the tool two-sidedly, bought short and sold long in its first operation, and has repeatedly warned about bond-market bubble risk. **A signed net-purchase number without a maturity split is close to uninformative, and a naive "central bank bought bonds = easing" rule would have been wrong at almost every turn since August 2024.** **[S²]**

8. **The policy rate has been static since May 2025 while the stance has kept moving — so the headline rate is no longer sufficient to measure the stance.** Easing since May 2025 has come through structural-tool rate cuts (25bp in January 2026), RRR, outright reverse repos, MLF net injections and bond operations. **The tool needs a composite stance measure — quota-weighted structural rates plus balance-sheet quantities plus a high-frequency shock series — or it will report "no change" through a year of continuous easing.** **[S²]**

9. **Supply-side liquidity indicators have become actively misleading in a balance-sheet recession.** With households prepaying mortgages (RMB4.7trn in 2022, ~12% of the stock), corporates and LGFVs deleveraging, and the GDP deflator negative for ten quarters, **every supply-side series can print "maximum ease" while nothing transmits.** The tool must carry at least one **demand-side** variable — mortgage prepayment proxy, household deposit growth vs income, or the PBoC loan-demand survey. Without one it will be systematically wrong in exactly the state of the world that matters. **[S² on facts; interpretive on the design conclusion]**

10. **The LGFV debt swap contaminates every credit aggregate for the 2025–2028 window.** RMB10trn of refinancing enters TSF and government bond issuance with no new spending power, while freeing bank risk capacity (risk weight 20% vs 75–100%). **It raises measured credit growth and lowers measured credit risk simultaneously, for reasons unrelated to the monetary stance. A swap-adjusted TSF is the highest-value single indicator fix available.** **[S²]**

11. **The LPR is losing its status as the lending benchmark.** It has been frozen (1yr 3.00%, 5yr 3.50%) for ~12 months into 2026 while the PBoC floats a **multi-benchmark loan pricing system** referencing sovereign bond yields, driven by record-low NIMs (1.40%). **The LPR series is becoming a policy-signalling variable rather than a conditions variable; the MPR's weighted-average new loan rate is the series to promote in its place.** **[S²]**

12. **Fixed-weight financial conditions indices are obsolete for China specifically.** The instrument changed identity in 2024–2026 and the financing mix shifted from loan-dominated to bond-plus-equity-majority within a decade. **Constant weights estimate a relationship that no longer exists. Move to TVP-FAVAR or at minimum rolling re-weighting with an explicit break at July 2024.** **[S on the literature; interpretive on the conclusion]**

13. **Transmission is ownership- and bank-tier-conditional, and the conditioning variables are observable.** Wholesale-funding access amplifies easing transmission to non-state banks while raising their downturn fragility (NBER WP 34056). **The large-bank vs small-bank funding spread is a transmission indicator, not merely a stability indicator, and belongs in the monetary-conditions block rather than the risk block.** **[S]**

14. **Real-rate measurement is genuinely unresolved and should be presented as such.** CPI ≈ 0%, PPI negative for three years, GDP deflator negative for ten quarters, core CPI modestly positive — the four implied real policy rates differ by several percentage points. **Report a fan, not a number, and treat the CPI-vs-GDP-deflator spread as an ambiguity flag: when it is wide, the tool should say "the stance is not identified," not print a false point estimate.** **[S² on the price facts; interpretive on the design rule]**

15. **The PBoC has begun treating non-bank liquidity as a policy object.** The June 2026 announcement of a macroprudential liquidity support tool for NBFIs, together with NBFI deposits at ~10% of M2 and WMPs above RMB30trn, means **bank-only liquidity measures now miss a material and growing share of the system.** Add NBFI deposits and WMP balances to the liquidity block. **[S²]**

---

## 6. China data plumbing notes

**6.1 Primary sources worth wiring up directly.** The quarterly *China Monetary Policy Report* is the single richest document and is published in both languages, roughly: Q4 in mid-February, Q1 in early May, Q2 in mid-August, Q3 in mid-November **[S, from the observed publication dates below]**. Direct PDFs located this session:

- [MPR Q3 2024 (8 Nov 2024, EN)](https://www.pbc.gov.cn/en/3688229/3688353/3688356/5188141/5528500/2024120610084889993.pdf)
- [MPR Q4 2024 (13 Feb 2025, EN)](http://www.pbc.gov.cn/en/3688229/3688353/3688356/5188141/5621959/2025051222522191967.pdf) · [Chinese](https://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125957/5347949/ad0bc3efe0234fed8cc6260a134a6e95/2025022618190099812.pdf)
- [MPR Q1 2025 (9 May 2025, EN)](https://wuhan.pbc.gov.cn/en/3688229/3688353/3688356/5624504/2025120609594943547/2025061614254988376.pdf) · [Chinese](https://cif.mofcom.gov.cn/cif/html/upload/20250512102012618_2025%E5%B9%B4%E7%AC%AC%E4%B8%80%E5%AD%A3%E5%BA%A6%E4%B8%AD%E5%9B%BD%E8%B4%A7%E5%B8%81%E6%94%BF%E7%AD%96%E6%89%A7%E8%A1%8C%E6%8A%A5%E5%91%8A.pdf)
- [MPR Q2 2025 (15 Aug 2025, EN)](http://www.pbc.gov.cn/en/3688229/3688353/3688356/5624504/5846668/index.html) · [Chinese](https://cif.mofcom.gov.cn/cif/html/upload/20250818093335312_%E4%B8%AD%E5%9B%BD%E8%B4%A7%E5%B8%81%E6%94%BF%E7%AD%96%E6%89%A7%E8%A1%8C%E6%8A%A5%E5%91%8A2025%E5%B9%B4%E7%AC%AC%E4%BA%8C%E5%AD%A3%E5%BA%A6.pdf)
- [MPR Q3 2025 (11 Nov 2025, EN)](https://www.pbc.gov.cn/en/attachDir/2025/12/20251217.pdf) · [Chinese](https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/5896222/2025111111175096136.pdf)
- [MPR Q4 2025 (10 Feb 2026, Chinese)](https://cif.mofcom.gov.cn/cif/html/upload/20260211143114167_2025%E5%B9%B4%E7%AC%AC%E5%9B%9B%E5%AD%A3%E5%BA%A6%E4%B8%AD%E5%9B%BD%E8%B4%A7%E5%B8%81%E6%94%BF%E7%AD%96%E6%89%A7%E8%A1%8C%E6%8A%A5%E5%91%8A.pdf)

Note that the **provincial PBoC mirrors (wuhan., xining., etc.) and MOFCOM's CIF site host copies** — useful redundancy when the main site is slow or blocked. Also: [PBoC Financial Statistics Reports](https://www.pbc.gov.cn/en/3688247/3688978/3709137/5810171/index.html), [Required Reserves announcements](https://www.pbc.gov.cn/en/3688229/3688335/3730270/index.html), [MLF tender announcements](https://www.pbc.gov.cn/en/3688229/3688335/3730273/3730282/2025112115000019205/index.html), [PBoC speeches archive](https://www.pbc.gov.cn/en/3688110/3688175/index.html), and [CFETS fixing repo rates](https://www.chinamoney.org.cn/english/bmkfrr/).

**6.2 A caution about excess reserves.** The excess reserve ratio is **quarterly only** and appears in MPR body text rather than as a clean time series **[S]**. This is the binding constraint on building a China Reserve Demand Elasticity (§2.9) at useful frequency. A higher-frequency proxy would need to be constructed from the PBoC balance sheet ("deposits of other depository corporations" less an estimate of required reserves from the RRR schedule and the deposit base) — doable, but the RRR schedule is tiered by bank size and carries targeted exemptions, so the estimate is noisy **[BK]**.

**6.3 Aggregation warning.** The monetary aggregates now have at least three distinct discontinuities in an 18-month span: the 手工补息 ban (April 2024), the 资金空转 campaign (2024), and the M1 redefinition (January 2025). **Any yoy or 3m/3m transformation crossing these dates is suspect.** The regulatory-event overlay in §4 is not an optional nicety.

---

## 7. Gaps, unverified items, and what to check first

**Could not be verified this session at all:**

1. **Authorship of BIS Working Paper 949** ("The natural interest rate in China") — the paper exists at the URL given, but authors were not returned.
2. **Whether the PBoC published a back-cast history for the redefined M1.** This determines whether an M1 growth series spanning January 2025 is usable at all. **Check first — it is the highest-consequence unknown in this note.**
3. **The exact old/new M1 levels (RMB67trn → RMB112trn).** Sourced only to a low-authority blog.
4. **Whether outright reverse repos are conducted as multiple-price tenders with no announced rate.** Asserted from background knowledge. If they *do* emit a rate, that rate is a second price signal and belongs in the tool.
5. **Whether the BIS publishes a renminbi-denominated credit-to-non-residents series in the GLIs.** Search suggested the GLIs cover USD/EUR/JPY only.
6. **The "40–60% pass-through efficiency" figure** — no clean primary attribution.
7. **The credit-to-GDP "194% (2024)" figure** — returned only from a low-quality aggregator site. Use the [BIS credit-to-GDP statistics](https://www.bis.org/statistics/rppb2604.htm) instead.
8. **The "2025 MLF net injection of RMB1,161bn" figure** — single weak source.
9. **Contents, coverage and licence of [github.com/wtsong/china_mpshocks](https://github.com/wtsong/china_mpshocks)** — potentially the cheapest route to a China high-frequency shock series, and entirely unchecked.
10. **The SLF-ceiling vs temporary-reverse-repo-ceiling tension** (§1.4) — two ceilings coexist in PBoC language and the resolution matters for corridor construction.
11. **The 46% vs 47% discrepancy** in bond/equity share of 2025 TSF flow (§1.7).
12. **No paper found adjudicating the deflator choice for China's real policy rate** (§3.4). If the team knows of one, it supersedes the reasoning there.

**Searches that came back thin, i.e. likely genuine gaps in the literature rather than gaps in this scan:**

- **No maintained, published China shadow policy rate.** Wu–Xia is not updated and is not China. This may be a real opportunity rather than a research failure — but note that a shadow rate is arguably *less* useful for China than for the US, since China never hit the ZLB and its unconventional policy works through quantities and structural tools rather than through a constrained short rate. The high-frequency shock literature (§2.1) is the better substitute.
- **No BIS or IMF working paper found that specifically evaluates the 2024–2026 PBoC framework reform.** The best available synthesis appears to be the **BBVA Research stocktake** ([July 2025](https://www.bbvaresearch.com/wp-content/uploads/2025/07/202507-Stocktaking-China-new-toolkit-in-its-monetary-policy-framework.pdf)), which is sell-side research, not peer-reviewed. **This is a genuine hole in the academic literature as of this scan.** Worth re-checking in six months; also worth checking the BOFIT Discussion Paper series directly, since search coverage of it was poor.
- **BOFIT yielded less than expected.** The one 2025 item confirmed is **BOFIT Discussion Paper 2/2025, Burdekin & Siklos, "Combating crises and deflation in China's central bank: Modeling post-pandemic monetary policymaking"** — Taylor and McCallum rules for the PBoC over 2001–2023, finding policy responsive to output and inflation gaps with a close actual-vs-predicted fit ([econstor](https://www.econstor.eu/bitstream/10419/315478/1/1922835005.pdf); [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5212662); [RePEc](https://ideas.repec.org/p/zbw/bofitp/315478.html)), with a journal version at [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0264999326001574). **Note this paper's sample ends in 2023 and therefore predates the entire framework reform** — it is useful as a pre-reform benchmark reaction function, and explicitly not as a guide to current policy. The [BOFIT Discussion Papers index](https://www.bofit.fi/en/publications/discussion-papers/) should be browsed directly.

---

## 8. Bibliography

All URLs below were returned by web search in this session. **None of the underlying documents was opened**, because outbound fetching was blocked (§0.1). Titles are as returned by search.

### PBoC primary sources
- Pan Gongsheng, "China's Current Monetary Policy Stance and Evolution of Monetary Policy Framework in the Future," 15th Lujiazui Forum, June 2024 — https://www.pbc.gov.cn/en/3688110/3688175/2025080817533718827/index.html
- Same speech, BIS Review r240621c — https://bis.org/review/r240621c.htm · PDF https://bis.org/review/r240621c.pdf
- Pan Gongsheng, "The evolution of financial structure and the modernization of financial markets in China," 2026 Lujiazui Forum, 17 June 2026, BIS Review r260622q — https://www.bis.org/review/r260622q.htm
- Pan Gongsheng, "A few observations on global financial governance," BIS Review r250630e — https://www.bis.org/review/r250630e.htm
- PBoC speeches archive (English) — https://www.pbc.gov.cn/en/3688110/3688175/index.html
- "Steady Progress in Monetary Policy Framework Transformation Bolsters High-Quality Development" — interview with the Head of the PBoC Monetary Policy Department, *Financial News* — https://www.pbc.gov.cn/en/3688006/5876310/5877235/index.html
- China Monetary Policy Report Q3 2024 (EN) — https://www.pbc.gov.cn/en/3688229/3688353/3688356/5188141/5528500/2024120610084889993.pdf
- China Monetary Policy Report Q3 2024 (CN) — https://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125957/5347949/afbfa5df25ee45889d916a2819b60a43/2024110815410752868.pdf
- China Monetary Policy Report Q4 2024 (EN) — http://www.pbc.gov.cn/en/3688229/3688353/3688356/5188141/5621959/2025051222522191967.pdf
- China Monetary Policy Report Q4 2024 (CN) — https://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125957/5347949/ad0bc3efe0234fed8cc6260a134a6e95/2025022618190099812.pdf
- China Monetary Policy Report Q1 2025 (EN) — https://wuhan.pbc.gov.cn/en/3688229/3688353/3688356/5624504/2025120609594943547/2025061614254988376.pdf
- China Monetary Policy Report Q1 2025 (CN) — https://cif.mofcom.gov.cn/cif/html/upload/20250512102012618_2025%E5%B9%B4%E7%AC%AC%E4%B8%80%E5%AD%A3%E5%BA%A6%E4%B8%AD%E5%9B%BD%E8%B4%A7%E5%B8%81%E6%94%BF%E7%AD%96%E6%89%A7%E8%A1%8C%E6%8A%A5%E5%91%8A.pdf
- Shanghai municipal reprint of MPR Q1 2025 — https://jrj.sh.gov.cn/SCGK194/20250512/f0ae149093614c04ab6b911c5df2c80b.html
- China Monetary Policy Report Q2 2025 (EN landing page) — http://www.pbc.gov.cn/en/3688229/3688353/3688356/5624504/5846668/index.html
- China Monetary Policy Report Q2 2025 (EN PDF) — https://wuhan.pbc.gov.cn/en/3688229/3688353/3688356/5624504/2025120609594987919/2025091916245444294.pdf · alternate mirror https://xining.pbc.gov.cn/en/3688229/3688353/3688356/2025/2025120609594987919/2025091916245444294.pdf
- China Monetary Policy Report Q2 2025 (CN) — https://cif.mofcom.gov.cn/cif/html/upload/20250818093335312_%E4%B8%AD%E5%9B%BD%E8%B4%A7%E5%B8%81%E6%94%BF%E7%AD%96%E6%89%A7%E8%A1%8C%E6%8A%A5%E5%91%8A2025%E5%B9%B4%E7%AC%AC%E4%BA%8C%E5%AD%A3%E5%BA%A6.pdf
- China Monetary Policy Report Q3 2025 (EN) — https://www.pbc.gov.cn/en/attachDir/2025/12/20251217.pdf
- China Monetary Policy Report Q3 2025 (CN) — https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/5896222/2025111111175096136.pdf · mirror https://cif.mofcom.gov.cn/cif/html/upload/20251124101800795_%E4%B8%AD%E5%9B%BD%E8%B4%A7%E5%B8%81%E6%94%BF%E7%AD%96%E6%89%A7%E8%A1%8C%E6%8A%A5%E5%91%8A2025%E5%B9%B4%E7%AC%AC%E4%B8%89%E5%AD%A3%E5%BA%A6.pdf
- China Monetary Policy Report Q4 2025 (CN) — https://cif.mofcom.gov.cn/cif/html/upload/20260211143114167_2025%E5%B9%B4%E7%AC%AC%E5%9B%9B%E5%AD%A3%E5%BA%A6%E4%B8%AD%E5%9B%BD%E8%B4%A7%E5%B8%81%E6%94%BF%E7%AD%96%E6%89%A7%E8%A1%8C%E6%8A%A5%E5%91%8A.pdf
- "Highlights of Monetary Policies in H1 2025" — https://www.pbc.gov.cn/en/3688229/3688353/3688362/5846652/index.html
- PBoC DR007 page — https://www.pbc.gov.cn/en/3688006/3689169/3753752/index.html
- PBoC Required Reserves page — https://www.pbc.gov.cn/en/3688229/3688335/3730270/index.html · "PBOC to Cut Required Reserve Ratio" — http://www.pbc.gov.cn/en/3688229/3688335/3730270/5701513/index.html
- Announcement on MLF Tenders in July 2025 — https://www.pbc.gov.cn/en/3688229/3688335/3730273/3730282/2025112115000019205/index.html
- Financial Statistics Report (July 2025) — https://www.pbc.gov.cn/en/3688247/3688978/3709137/5810171/index.html · (Q1–Q3 2025) https://www.pbc.gov.cn/en/3688247/3688978/3709137/5870352/index.html · (November 2025) https://www.pbc.gov.cn/en/3688247/3688978/3709137/2025122410193371772/index.html
- PBoC English home — https://www.pbc.gov.cn/en/3688006/index.html
- CFETS fixing repo rates — https://www.chinamoney.org.cn/english/bmkfrr/
- Xinhua interview with Pan Gongsheng, January 2026 — https://www.news.cn/fortune/20260122/89868f9a1c0b463b89e4bcefccc1b087/c.html
- 潘功胜：构建科学稳健的货币政策体系和覆盖全面的宏观审慎管理体系, NBD, Dec 2025 — https://www.nbd.com.cn/articles/2025-12-04/4167489.html
- 潘功胜最新讲话！7个政策信号值得关注 — https://c.m.163.com/news/a/KNC3ROM40539LWQ1.html
- 央行行长潘功胜详解2025年适度宽松货币政策 — https://www.zgzzs.com.cn/index.php/article/detail/id/127760.html
- 金融时报：中国货币政策框架或将进入转型时刻 (June 2024) — https://app.dahecube.com/nweb/news/20240624/203509n3718b93319c.htm?artid=203509

### Chinese government / official
- STATISTICAL COMMUNIQUÉ on 2025 National Economic and Social Development, NBS — https://www.stats.gov.cn/english/PressRelease/202602/t20260228_1962661.html
- "China's central bank introduces new liquidity tool" (outright reverse repo), 28 Oct 2024 — https://english.www.gov.cn/news/202410/28/content_WS671f2a63c6d0868f4e8ec5d2.html
- "China to well implement moderately loose monetary policy: senior official," 14 Dec 2024 — https://english.www.gov.cn/news/202412/14/content_WS675cbb55c6d0868f4e8edf12.html
- "China's central bank outlines monetary priorities for 2025," 5 Jan 2025 — https://english.www.gov.cn/news/202501/05/content_WS6779bfbcc6d0868f4e8ee850.html
- "China to cut policy rate by 0.1 percentage points from Thursday," 7 May 2025 — https://english.www.gov.cn/news/202505/07/content_WS681af03ec6d0868f4e8f250c.html
- "China to cut reserve requirement ratio by 0.5 percentage points from May 15," 7 May 2025 — https://english.www.gov.cn/news/202505/07/content_WS681af001c6d0868f4e8f2509.html
- "China to conduct 400-bln-yuan MLF operation on Friday," July 2025 — https://english.www.gov.cn/news/202507/24/content_WS688232d0c6d0868f4e8f468b.html
- "China's central bank to conduct 1-trillion-yuan outright reverse repo operation," 5 Sep 2025 — https://english.www.gov.cn/news/202509/05/content_WS68ba20cbc6d0868f4e8f558c.html
- "China to conduct 1.1-trillion-yuan outright reverse repo operation," 30 Sep 2025 — https://english.www.gov.cn/news/202509/30/content_WS68dbdafbc6d00ca5f9a0690b.html
- "China to conduct 400-bln-yuan MLF operation on Thursday," Dec 2025 — https://english.www.gov.cn/news/202512/24/content_WS694bcfb0c6d00ca5f9a0842f.html
- "China's central bank unveils six new financial policy measures," 17 June 2026 — https://english.www.gov.cn/news/202606/17/content_WS6a324210c6d00ca5f9a0ba94.html
- "China's vision for deeper financial opening-up highlighted at Shanghai Lujiazui Forum," 19 June 2025 — https://english.www.gov.cn/news/202506/19/content_WS68534817c6d0868f4e8f3736.html
- SCIO: "PBC: Bond buying suspension meant to address market risks," 15 Jan 2025 — http://english.scio.gov.cn/m/pressroom/2025-01/15/content_117666228.html
- SCIO: "PBOC cuts rates on targeted monetary tools," 16 Jan 2026 — http://english.scio.gov.cn/pressroom/2026-01/16/content_118283341.html
- CGTN: "10 trillion yuan: China raises debt swap ceiling," 8 Nov 2024 — https://news.cgtn.com/news/2024-11-08/China-s-top-legislature-approves-bill-to-raise-local-govt-debt-ceiling-by-6-trillion-yuan-1ymH5tCk18I/p.html
- Beijing Review: "China deploys one of its largest-ever fiscal initiatives," Nov 2024 — http://www.bjreview.com/Business/202411/t20241118_800384310.html
- China Daily: "China building more diversified, innovative financial system," July 2026 — http://europe.chinadaily.com.cn/a/202607/06/WS6a4b0978a310986e2b463ad1.html
- China Daily: "RRR cut to spur further monetary easing," 13 May 2025 — https://www.chinadaily.com.cn/a/202505/13/WS68229d46a310a04af22bee78.html
- People's Daily Online: "China cuts RRR for first time in 2025," 16 May 2025 — https://en.people.cn/n3/2025/0516/c90000-20315656.html
- Shanghai Stock Exchange / China Daily: "2026 Lujiazui Forum to focus on global governance and financial cooperation" — https://english.sse.com.cn/news/newsrelease/voice/c/c_20260615_10821917.shtml
- Shanghai Stock Exchange / Yicai: "China's Wealth Management Market Hits Record USD4.31 Trillion," 22 May 2025 — https://english.sse.com.cn/news/newsrelease/voice/c/c_20250522_10779736.shtml
- Global Times: "China's central bank revises statistical scope of M1," Dec 2024 — https://www.globaltimes.cn/page/202412/1324233.shtml

### International institutions
- IMF, People's Republic of China: 2025 Article IV Consultation (Country Report 2026/044) — https://www.elibrary.imf.org/view/journals/002/2026/044/article-A001-en.xml · staff report PDF https://www.imf.org/-/media/files/publications/cr/2026/english/1chnea2026001-source-pdf.pdf · issue PDF https://www.elibrary.imf.org/view/journals/002/2026/044/002.2026.issue-044-en.pdf
- IMF, "Executive Board Concludes 2025 Article IV Consultation with China," 18 Feb 2026 — https://www.imf.org/en/news/articles/2026/02/18/pr-26053-china-imf-executive-board-concludes-2025-article-iv-consultation
- IMF, "Staff Completes 2025 Article IV Mission to China," 10 Dec 2025 — https://www.imf.org/en/news/articles/2025/12/10/pr-25415-china-imf-staff-completes-2025-article-iv-mission-to-the-peoples-republic-of-china
- IMF, 2025 China Article IV press conference remarks — https://www.imf.org/en/news/articles/2025/12/10/sp121025-md-remarks-2025-china-article-iv-consultation-press-conference
- IMF, "How China's Economy Can Pivot to Consumption-led Growth," Feb 2026 — https://www.imf.org/en/news/articles/2026/02/18/cf-how-chinas-economy-can-pivot-to-consumption-led-growth
- IMF WP 2025/109, "From Text to Quantified Insights: A Large-Scale LLM Analysis of Central Bank Communication" — https://www.imf.org/en/publications/wp/issues/2025/06/06/from-text-to-quantified-insights-a-large-scale-llm-analysis-of-central-bank-communication-567522 · PDF https://www.imf.org/-/media/files/publications/wp/2025/english/wpiea2025109-print-pdf.pdf · RePEc https://ideas.repec.org/p/imf/imfwpa/2025-109.html
- IMF WP 2024/224, "A New Dataset of High-Frequency Monetary Policy Shocks" — https://www.elibrary.imf.org/view/journals/001/2024/224/article-A001-en.xml
- IMF WP 2024/161, "The Mirage of Falling R-stars" — https://www.elibrary.imf.org/view/journals/001/2024/161/article-A001-en.xml
- IMF WP 2024/238, "China's Path to Sustainable and Balanced Growth" — https://www.imf.org/-/media/files/publications/wp/2024/english/wpiea2024238-print-pdf.pdf
- IMF, "Interest Rate Transmission in a New Monetary Policy Framework," ch. 7 of *Modernizing China* — https://www.elibrary.imf.org/display/book/9781513539942/ch07.xml
- IMF China Monitor — https://www.imfconnect.org/content/dam/imf/News%20and%20Generic%20Content/GMM/Special%20Features/China%20Monitor.pdf
- BIS WP 949, "The natural interest rate in China" — https://www.bis.org/publ/work949.htm
- BIS global liquidity indicators: end-June 2025 https://www.bis.org/statistics/gli2510.htm · end-March 2025 https://www.bis.org/statistics/gli2507.htm · end-December 2024 https://www.bis.org/statistics/gli2504.htm · end-September 2024 https://bis.org/statistics/gli2501.htm · end-June 2024 https://bis.org/statistics/gli2410.htm · end-June 2023 https://www.bis.org/statistics/gli2310.htm
- BIS IBS/GLI statistical releases: end-June 2025 https://www.bis.org/statistics/rppb2510.htm · end-September 2025 https://www.bis.org/publications/202601-commentary-ibs-gli and https://www.bis.org/statistics/rppb2601.htm · end-December 2025 https://www.bis.org/statistics/rppb2604.htm
- World Bank, China Economic Update, June 2025 ("Unlocking Consumption") — https://thedocs.worldbank.org/en/doc/8ae5ce818673952a85fee1ee57c3e933-0070012025/original/CEU-June-2025-EN.pdf
- World Bank, China Economic Update, December 2025 — https://thedocs.worldbank.org/en/doc/600cd53e2bb24d516b8c3489e5d2c187-0070012025/original/CEU-December-2025-EN.pdf
- SUERF Policy Note, "The Natural Interest Rate in China" — https://www.suerf.org/publications/suerf-policy-notes-and-briefs/the-natural-interest-rate-in-china/

### Central bank research (non-China) — transferable methods
- NY Fed, "Gauging the Strength of China's Economy in Uncertain Times," Liberty Street Economics, April 2025 — https://libertystreeteconomics.newyorkfed.org/2025/04/gauging-the-strength-of-chinas-economy-in-uncertain-times/
- NY Fed, "Tracking Reserve Ampleness in Real Time Using Reserve Demand Elasticity," Oct 2024 — https://libertystreeteconomics.newyorkfed.org/2024/10/tracking-reserve-ampleness-in-real-time-using-reserve-demand-elasticity
- NY Fed, "When Are Central Bank Reserves Ample?", Aug 2024 — https://libertystreeteconomics.newyorkfed.org/2024/08/when-are-central-bank-reserves-ample/
- NY Fed press release on Reserve Demand Elasticity, 17 Oct 2024 — https://www.newyorkfed.org/newsevents/news/research/2024/20241017
- NY Fed, Liberty Street "ample reserves" tag — https://libertystreeteconomics.newyorkfed.org/tag/ample-reserves
- NY Fed, Williams, "All the Stars We Cannot See," 25 Aug 2025 — https://www.newyorkfed.org/newsevents/speeches/2025/wil250825
- NY Fed, "Balance Sheet Reduction and Ample Reserves," 29 Sep 2025 — https://www.newyorkfed.org/newsevents/speeches/2025/rem250929
- Federal Reserve Board, "Market-Based Indicators on the Road to Ample Reserves," FEDS Note, 31 Jan 2025 — https://www.federalreserve.gov/econres/notes/feds-notes/market-based-indicators-on-the-road-to-ample-reserves-20250131.html
- St. Louis Fed Review, "Monetary Policy Implementation with Ample Reserves," May 2025 — https://www.stlouisfed.org/-/media/project/frbstl/stlouisfed/publications/review/pdfs/2025/may/monetary-policy-implementation-with-ample-reserves.pdf
- ECB conference paper, Anbil, "A Tale of Demand and Supply for Central Bank Reserves" — https://www.ecb.europa.eu/press/conferences/shared/pdf/ANBIL%20SRIYA%20-%20A%20Tale%20of%20Demand%20and%20Supply%20for%20Central%20Bank%20Reserves.pdf
- Dallas Fed, "China debt overhang leads to rising share of 'zombie' firms," 23 Dec 2025 — https://www.dallasfed.org/research/economics/2025/1223
- Atlanta Fed, Wu–Xia Shadow Federal Funds Rate — https://www.atlantafed.org/cqer/research/wu-xia-shadow-federal-funds-rate
- Jing Cynthia Wu, shadow rates page — https://sites.google.com/view/jingcynthiawu/shadow-rates · Fan Dora Xia — https://sites.google.com/site/fandoraxia/wx-data
- BOFIT Weekly 2024/36, "China's central bank overhauls monetary policy operating framework and starts trading in government bonds" — https://www.bofit.fi/en/monitoring/weekly/2024/vw202436_1/
- BOFIT Weekly 2024/51, "China lays out economic policy framework for 2025" — https://www.bofit.fi/en/monitoring/weekly/2024/vw202451_2/
- BOFIT Forecast for China 2024–2026 — https://www.bofit.fi/en/forecasting/latest-forecast-for-china/ · press release https://www.suomenpankki.fi/en/news-and-topical/press-releases-and-news/releases/2024/bofit-forecast-for-china-20242026-productivity-gains-key-to-china-maintaining-growth/
- BOFIT Discussion Papers index — https://www.bofit.fi/en/publications/discussion-papers/ · BOFIT publications — https://www.bofit.fi/en/publications/ · peer-reviewed research — https://www.bofit.fi/en/publications/peer-reviewed-research/
- BOFIT Policy Brief 17/2025, Kaaresvirta & Nuutilainen — https://publications.bof.fi/bitstream/handle/10024/54271/bpb2517.pdf

### Academic papers and working papers
- Burdekin & Siklos, "Combating crises and deflation in China's central bank: Modeling post-pandemic monetary policymaking," BOFIT DP 2/2025 — https://www.econstor.eu/bitstream/10419/315478/1/1922835005.pdf · SSRN https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5212662 · RePEc https://ideas.repec.org/p/zbw/bofitp/315478.html · journal version https://www.sciencedirect.com/science/article/pii/S0264999326001574
- NBER WP 34056, "A Trade-off Between Monetary Policy Transmission and Systemic Risk in China" (2025) — https://www.nber.org/papers/w34056 · RePEc https://ideas.repec.org/p/nbr/nberwo/34056.html
- NBER WP 31396, "Deposit Regulation and Monetary Transmission in China" — https://www.nber.org/system/files/working_papers/w31396/w31396.pdf
- NBER WP 27763, "Monetary Stimulus Amidst the Infrastructure Investment Spree: Evidence from China's Loan-Level Data" — https://www.nber.org/papers/w27763 · PDF https://www.nber.org/system/files/working_papers/w27763/w27763.pdf
- NBER WP 22650, "Impacts of Monetary Stimulus on Credit Allocation and the Macroeconomy: Evidence from China" — https://www.nber.org/papers/w22650
- NBER WP 24230, "Risks in China's Financial System" (Song) — https://www.nber.org/system/files/working_papers/w24230/w24230.pdf
- NBER WP 31949, "Natural and Neutral Real Interest Rates" — https://www.nber.org/system/files/working_papers/w31949/w31949.pdf
- "Current stance vs. future guidance: LLM evidence on how PBC communication shapes the yield curve," *Economics Letters* 259 (2026) — https://www.sciencedirect.com/science/article/abs/pii/S0165176525006184 · RePEc https://ideas.repec.org/a/eee/ecolet/v259y2026ics0165176525006184.html
- "Monetary policy in China: High-frequency shocks and the signaling effects," *China Economic Review* (2025) — https://www.sciencedirect.com/science/article/abs/pii/S1043951X25001798 · ResearchGate https://www.researchgate.net/publication/394868080_Monetary_policy_in_China_High-frequency_shocks_and_the_signaling_effects
- "Can you hear me now? Identifying the effect of Chinese monetary policy announcements," *JIMF* (2024) — https://www.sciencedirect.com/science/article/pii/S0261560624000652
- "China's monetary policy surprises and corporate real investment," *China Economic Review* — https://www.sciencedirect.com/science/article/abs/pii/S1043951X22001511
- "A High-Frequency Measure of Chinese Monetary Policy Shocks" (seminar) — https://fss.um.edu.mo/fss-deco-seminar-a-high-frequency-measure-of-chinese-monetary-policy-shocks/
- China high-frequency MP shocks repository — https://github.com/wtsong/china_mpshocks
- "The Tone of Central Bank Communications and the Market Response: A Cross-Country Analysis Using an AI-Based Monetary Sentiment Index" — https://www.sciencedirect.com/science/article/abs/pii/S0939362526000609
- "Reading Copom's Tone: A Weighted LLM Framework for Hawkish-Dovish Sentiment, Forward Guidance, and Uncertainty" — https://pith.science/paper/2608.07251
- "Measuring the natural rate of real interest for the Chinese economy" (2026) — https://www.sciencedirect.com/science/article/pii/S1059056026002637
- "Demographic change and natural interest rate of China," *Finance Research Letters* — https://www.sciencedirect.com/science/article/abs/pii/S1544612323011844
- "A Note of Caution on Shadow Rate Estimates," *JMCB* 52(4), 2020 — https://ideas.repec.org/a/wly/jmoncb/v52y2020i4p951-962.html
- "Macro-Financial Condition Index Construction and Forecasting Based on Machine Learning Techniques: Empirical Evidence from China," *Symmetry* 17(6):904 (2025) — https://doi.org/10.3390/sym17060904
- "Research on Dynamic Measurement and Early Warning of Systemic Financial Risk in China Based on TVP-FAVAR and Deep Learning Model," *Systems* 13(8):720 (2025) — https://doi.org/10.3390/systems13080720
- "Construction and Analysis of Chinese Macro-Financial Stability Index," *Computational Economics* (2024) — https://link.springer.com/article/10.1007/s10614-024-10767-2
- "Constructing dynamic financial conditions indexes by TVP-FAVAR model" — https://www.researchgate.net/publication/315925237_Constructing_a_dynamic_financial_conditions_indexes_by_TVP-FAVAR_model
- "Financial Conditions Indexes for the United States and Euro Area" — https://www.researchgate.net/publication/228317573_Financial_Conditions_Indexes_for_the_United_States_and_Euro_Area
- "The dynamic impact mechanism of China's financial conditions on real economy and international crude oil market," *Heliyon* — https://www.sciencedirect.com/science/article/pii/S2405844023082932 · PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC10597845/
- "Rigid Mortgage Rates and Monetary Policy Transmission," ABFER 2025 Annual Conference — https://www.abfer.org/media/abfer-events-2025/annual-conference/papers-household-finance/AC25P7048_Rigid-Mortgage-Rates-and-Monetary-Policy-Transmission.pdf
- VoxChina, "Mortgage Prepayment in China" — https://voxchina.org/show-3-424.html
- "China's interest rate pass-through after the interest rate liberalization: Evidence from a nonlinear ARDL model" — https://www.sciencedirect.com/science/article/abs/pii/S1059056020303178
- "Shadow Funding and Economic Growth: Evidence from China," *JMCB* (2024) — https://onlinelibrary.wiley.com/doi/10.1111/jmcb.13008
- "Shadow banking, investment and interest rate transmission: Evidence from macroprudential policy in China" — https://www.sciencedirect.com/science/article/abs/pii/S0313592623002953
- "Zombie firms, misallocation and manufacturing capacity utilization rate: Evidence from China," *Economics of Transition and Institutional Change* (2024) — https://onlinelibrary.wiley.com/doi/10.1111/ecot.12398
- "Zombie firms, state subsidies and aggregate productivity," *Economica* (2025) — https://onlinelibrary.wiley.com/doi/10.1111/ecca.12569
- "Curbing zombie firms: Evidence from China's fair competition review system" — https://www.sciencedirect.com/science/article/abs/pii/S0264999326001823
- "How do zombie firms affect labor mobility: city-level empirical evidence from China" (2025) — https://ideas.repec.org/a/pal/palcom/v12y2025i1d10.1057_s41599-025-05711-0.html
- "Regional Effects of Monetary Policy in China" — https://ideas.repec.org/p/fds/dpaper/202401.html

### Market, think-tank and press
- BBVA Research, "Stocktaking China's new toolkit in its monetary policy framework," July 2025 — https://www.bbvaresearch.com/wp-content/uploads/2025/07/202507-Stocktaking-China-new-toolkit-in-its-monetary-policy-framework.pdf
- BBVA Research, China Banking Monitor 2025, April 2025 — https://www.bbvaresearch.com/wp-content/uploads/2025/04/China-banking-monitor-2025.pdf
- Nomura Connects, "China: A Major Step to Modernizing the PBoC's Policymaking" — https://www.nomuraconnects.com/focused-thinking-posts/china-a-major-step-to-modernizing-the-pbocs-policymaking/
- ING THINK, "What to expect from China's monetary policy framework reforms" — https://think.ing.com/articles/what-to-expect-from-chinas-coming-monetary-policy-framework-reform/
- Trivium China, "PBoC resumes bond trading to smooth yield curve," 5 Nov 2025 — https://triviumchina.com/2025/11/05/pboc-resumes-bond-trading-to-smooth-yield-curve/
- Trivium China, "PBoC exerts greater control over overnight lending rates," 19 June 2026 — https://triviumchina.com/2026/06/19/pboc-exerts-greater-control-over-overnight-lending-rates/
- Central Banking, "PBoC starts trading Chinese government bonds" — https://www.centralbanking.com/central-banks/financial-stability/7962167/pboc-starts-trading-chinese-government-bonds
- Central Banking, "PBoC suspends government bond purchases" — https://www.centralbanking.com/central-banks/currency/7963600/pboc-suspends-government-bond-purchases
- Central Banking, "PBoC launches new reverse repo operations" — https://www.centralbanking.com/central-banks/monetary-policy/operating-framework/7962591/pboc-launches-new-reverse-repo-operations
- Central Banking, "PBoC tweaks lending facility as framework reform continues" — https://www.centralbanking.com/central-banks/monetary-policy/operating-framework/7972581/pboc-tweaks-lending-facility-as-framework-reform-continues
- Central Banking, "PBoC cuts rates and lowers reserve requirement ratios" — https://www.centralbanking.com/central-banks/monetary-policy/7972834/pboc-cuts-rates-and-lowers-reserve-requirement-ratios
- Central Banking, "Chinese policy-makers warm to PBoC bond trading" — https://www.centralbanking.com/central-banks/monetary-policy/operating-framework/7961188/chinese-policy-makers-warm-to-pboc-bond-trading
- Risk.net PBoC coverage index — https://www.risk.net/organisations/people%E2%80%99s-bank-of-china-pboc
- Bloomberg, "China's Central Bank Takes More Control Over Rates by Adding Temporary Repos," 8 Jul 2024 — https://www.bloomberg.com/news/articles/2024-07-08/pboc-to-conduct-temporary-repos-depending-on-market-conditions
- Bloomberg, "China's PBOC Sells Long-Term Bonds, Buys Short End Debt," 30 Aug 2024 — https://www.bloomberg.com/news/articles/2024-08-30/china-s-pboc-sells-long-term-bonds-buys-short-end-debt
- Bloomberg, "PBOC Adds Outright Reverse Repo to Monetary Policy Toolbox," 28 Oct 2024 — https://www.bloomberg.com/news/articles/2024-10-28/pboc-adds-outright-reverse-repo-to-monetary-policy-toolbox
- Bloomberg, "PBOC Unveils New Method to Auction Its One-Year Loans to Banks," 24 Mar 2025 — https://www.bloomberg.com/news/articles/2025-03-24/pboc-to-auction-62-billion-one-year-loans-to-banks-on-tuesday
- Bloomberg, "PBOC Supports Banks' Moderate Bond Buying, Flags Excessive Risk," 14 Jul 2025 — https://www.bloomberg.com/news/articles/2025-07-14/pboc-supports-banks-moderate-bond-buying-flags-excessive-risk
- Bloomberg, "China's PBOC Seen Resuming Bond Purchases," 28 Oct 2025 — https://www.bloomberg.com/news/articles/2025-10-28/pboc-seen-resuming-bond-purchases-as-it-steps-back-into-market
- Reuters via US News, "China's Central Bank Injects Cash Via New Outright Reverse Repos in October," 31 Oct 2024 — https://money.usnews.com/investing/news/articles/2024-10-31/chinas-central-bank-conducts-500-billion-yuan-of-outright-reverse-repos-in-october
- Reuters via Tiger, "PBOC activates open market outright reverse repo operations facility" — https://www.itiger.com/hans/news/2478711975
- CNBC, "China vows 'more proactive' fiscal stimulus, 'moderately' looser monetary policy," 9 Dec 2024 — https://www.cnbc.com/2024/12/09/china-vows-more-active-fiscal-stimulus-measures-moderately-looser-monetary-policy-next-year-.html
- CNBC, "China central bank releases slate of support measures," 24 Sep 2024 — https://www.cnbc.com/2024/09/24/chinas-central-bank-chief-set-to-hold-press-conference-days-after-fed-rate-cut.html
- CNBC, "China announces sweeping measures to ease policy," 7 May 2025 — https://www.cnbc.com/2025/05/07/china-to-cut-key-lending-rates-by-10-points-bank-reserve-requirement-ratio-by-50-points-.html
- CNBC, LPR unchanged, 21 Jul 2025 — https://www.cnbc.com/2025/07/21/china-july-2025-key-lending-rates-lpr-interest-rate-pboc.html
- CNBC, LPR steady for a seventh month, 22 Dec 2025 — https://www.cnbc.com/2025/12/22/china-lpr-1-year-5-year-property-market-weak-economic-data-.html
- CNBC, LPR unchanged, 20 Jan 2026 — https://www.cnbc.com/2026/01/20/china-lending-rates-lpr-slowing-economic-growth.html
- CNBC, LPR unchanged, 20 Apr 2026 — https://www.cnbc.com/2026/04/20/china-keeps-benchmark-lending-rates-unchanged-as-economic-growth-revs-up-amid-mounting-middle-east-risk-mount-.html
- Yicai Global, "PBOC's MLF No Longer Has Policy-Oriented Role After Removal of Unified Price Bidding System" — https://www.yicaiglobal.com/news/pbocs-mlf-no-longer-has-policy-oriented-role-after-removal-of-unified-price-bidding-system-expert-says
- Yicai Global, "PBOC's Temporary Repo, Reverse Repo Operations to Help Stabilize Market" — https://www.yicaiglobal.com/news/pbocs-temporary-repo-reverse-repo-operations-to-help-stabilize-market-experts-say
- Caixin Global, "Will China's Central Bank Resume Government Bond Buying," 9 Sep 2025 — https://www.caixinglobal.com/2025-09-09/chinas-central-bank-taps-the-brakes-on-bond-buying-102360733.html
- Caixin Global, Gao Zhanjun on the central bank in the government bond market, 7 Sep 2024 — https://www.caixinglobal.com/2024-09-07/weekly-preview-gao-zhanjun-how-to-interpret-the-central-banks-buying-and-selling-of-government-bonds-102234543.html
- Caixin opinion, 叫停"手工补息"对银行业有何持续性影响, 4 Sep 2024 — https://opinion.caixin.com/2024-09-04/102233243.html
- Huxiu, 银行手工补息高息揽储行为被禁 — https://m.huxiu.com/article/2895285.html?type=text
- Jiemian, M2和社融淡出，结构性降息概率更大 — CEWC interpretation — https://m.jiemian.com/article/13751817.html
- China Banking News, "China struggles to boost lending as households deleverage" — https://www.chinabankingnews.com/p/china-struggles-to-boost-lending
- China Banking News, "China 'wrings the water' out of the money supply in May" — https://www.chinabankingnews.com/p/china-wrings-the-water-out-of-the
- China Banking News, "How China plans to avoid a Japanese-style balance sheet recession" — https://www.chinabankingnews.com/p/how-china-plans-to-avoid-a-japanese
- China Banking News, "China pressgangs monetary policy in service of property market, regional deleveraging" — https://www.chinabankingnews.com/p/china-pressgangs-monetary-policy
- China Banking News, "Chinese economists clash over dovish monetary policy" — https://www.chinabankingnews.com/p/chinese-economists-clash-over-dovish
- China Banking News, "Why China needs to keep monetary policy loose for the next decade" — https://www.chinabankingnews.com/p/why-china-needs-to-keep-monetary
- China Banking News, "Chinese central bank continues to normalise treasury transactions" — https://www.chinabankingnews.com/p/chinese-central-bank-continues-to
- East Is Read, "Miao Yanliang explains China's large monetary injection yet blocked transmission" — https://www.eastisread.com/p/miao-yanliang-explains-chinas-large
- CF40 Research, "How to Understand the PBOC's Eight Supportive Monetary Policy Measures and December 2025 TSF" — https://cf40research.substack.com/p/how-to-understand-the-pbocs-eight
- Carnegie Endowment, "A 10 Trillion RMB Accounting Exercise," Nov 2024 — https://carnegieendowment.org/posts/2024/11/a-10-trillion-rmb-accounting-exercise?lang=en
- Atlantic Council, "Beijing extends and pretends to deal with its mountain of local government debt" — https://www.atlanticcouncil.org/blogs/econographics/beijing-extends-and-pretends-to-deal-with-its-mountain-of-local-government-debt/
- S&P Global, "China's 12 trillion yuan debt swap to ease local debt pressure, bank margins," Nov 2024 — https://www.spglobal.com/market-intelligence/en/news-insights/articles/2024/11/china-s-12-trillion-yuan-debt-swap-to-ease-local-debt-pressure-bank-margins-86126459
- S&P Global, "World's largest lender expects net interest margin decline to slow in 2025" — https://www.spglobal.com/market-intelligence/en/news-insights/articles/2025/3/worlds-largest-lender-expects-net-interest-margin-decline-to-slow-in-2025-88193366
- Asia Society Policy Institute, "China Sets the Stage for the Third Plenum" — https://asiasociety.org/policy-institute/china-sets-stage-third-plenum-unveiling-financial-reforms-and-monetary-policy-direction
- Peking Ensight, "Key takeaways from Lujiazui Forum on China's new financial policy moves" — https://pekingensight.substack.com/p/key-takeaways-from-lujiazui-forum
- Conference Board, "China Policy Brief: China's 2024 Central Economic Work Conference" — https://www.conference-board.org/publications/China-Policy-Brief-China-2024-Central-Economic-Work-Conference
- APCO Worldwide, "China's 2024 Central Economic Work Conference: 6 Key Takeaways" — https://apcoworldwide.com/blog/chinas-2024-central-economic-work-conference-six-key-takeaways/
- Lombard Odier, "China's woes drive shift to looser monetary policy," Dec 2024 — https://www.lombardodier.com/insights/2024/december/china-s-woes-drive-shift-to.html
- RFA, "EXPLAINED: How China hopes to kickstart its flagging economy," 11 Dec 2024 — https://www.rfa.org/english/china/2024/12/11/china-monetary-loosening-policy-explained/
- Asia News Network, "China's 'moderately loose' monetary policy expected to deliver policy shift" — https://asianews.network/chinas-moderately-loose-monetary-policy-expected-to-deliver-policy-shift/
- CNN, "Beijing approves $1.4 trillion debt package," 8 Nov 2024 — https://www.cnn.com/2024/11/08/business/china-economy-hidden-debt-intl-hnk
- NBC News, "China announces $1.4 trillion over five years to tackle local governments' hidden debt" — https://www.nbcnews.com/news/world/china-announces-14-trillion-five-years-tackle-local-governments-hidden-rcna179269
- East Asia Forum, "China's debt reckoning," 20 Sep 2025 — https://eastasiaforum.org/2025/09/20/chinas-debt-reckoning/
- Allianz Global Investors, "Is China getting into balance sheet recession?" — https://www.allianzgi.com/en/insights/is-china-getting-into-balance-sheet-recession
- BNP Paribas AM, "Should investors fret over talk of China heading for a 'balance sheet recession'?" — https://viewpoint.bnpparibas-am.com/should-investors-fret-over-talk-of-china-heading-for-a-balance-sheet-recession/
- CEPS/CEP, "Monetary Policy Reloaded. Towards a New Growth Path in China" — https://www.cepweb.org/monetary-policy-reloaded-towards-a-new-growth-path-in-china/
- Anbound, "Resuming Government Bond Trading Requires the PBoC to Be in Tune with the Market" — http://www.anbound.com/Section/ArticleView_35692_1.htm
- BigGo Finance, "PBOC Q1 Report Signals Three Shifts: Anchoring Overnight Rate, Watching Imported Inflation, Elevating Bond Market's Strategic Role" — https://finance.biggo.com/news/h8P7HJ4B2jrwCtgly29e
- BigGo Finance, "China's Central Bank Signals Policy Shift: Near-Term RRR Cuts Unlikely, Overnight Rate Becomes Anchor" — https://finance.biggo.com/news/gHXeHJ4BYH_ypPqO0PcK
- BigGo Finance, "China's LPR Unchanged for 12th Straight Month as PBOC Signals Loan Pricing Overhaul" — https://finance.biggo.com/news/76mIRJ4BpwxG186NnABM
- Macrostream, "Market Eyes PBOC's Overnight Reverse Repo Debut" — https://www.macrostream.ai/articles/6a430ac23c80f748cb62270c · https://www.macrostream.ai/articles/6a323d088f2442d7215507d5
- VT Markets, "Standard Chartered sees China's PBoC shifting liquidity operations towards DR001" — https://www.global-vtrader.com/en/live-updates/standard-chartered-sees-chinas-pboc-shifting-liquidity-operations-towards-dr001-foreshadowing-overnight-rate-anchor/
- A-Share Insights, "Lujiazui Forum 2026: Six Capital Market Shifts for Global Allocators" — https://ashareinsights.com/the-lujiazui-forum-2026-1/
- Business Standard, "PBOC studies plan to narrow rate fluctuation range, warns over bond risks," Aug 2024 — https://www.business-standard.com/world-news/pboc-studies-plan-to-narrow-rate-fluctuation-range-warns-over-bond-risks-124080901646_1.html
- Business Standard, "China's central bank starts trading govt bonds to influence yield curve," 30 Aug 2024 — https://www.business-standard.com/amp/world-news/china-s-central-bank-starts-trading-govt-bonds-to-influence-yield-curve-124083000779_1.html
- SCMP, "Record low yields prompt suspension of government bond purchases by China's central bank" — https://www.scmp.com/economy/china-economy/article/3294282/record-low-yields-prompt-suspension-government-bond-purchases-chinas-central-bank
- Forexlive, "PBOC is changing how it issues its one-year MLF loans," 25 Mar 2025 — https://www.forexlive.com/centralbank/pboc-is-changing-how-it-issues-its-one-year-medium-term-lending-facility-mlf-loans-20250325/ · TradingView mirror https://www.tradingview.com/news/forexlive:6d686dff4094b:0-pboc-is-changing-how-it-issues-its-one-year-medium-term-lending-facility-mlf-loans/
- Finadium, "PBOC to add overnight reverse repo and RMB repo facility" — https://finadium.com/pboc-to-add-overnight-reverse-repo-and-rmb-repo-facility/
- Finadium, "China central bank introduces outright reverse repos amid year-end liquidity concerns" — https://finadium.com/china-central-bank-introduces-outright-reverse-repos-amid-year-end-liquidity-concerns/
- The Edge Malaysia, "China's central bank plans overnight reverse repo in next stage of policy shift" — https://theedgemalaysia.com/node/808226
- FXStreet, "China cuts seven-day reverse repo rate and loan prime rates," 22 Jul 2024 — https://www.fxstreet.com/amp/analysis/china-cuts-seven-day-reverse-repo-rate-and-loan-prime-rates-in-move-to-support-growth-202407220918
- Investing.com Factbox, "The Chinese central bank's policy arsenal" — https://investing.com/news/economy-news/factboxthe-chinese-central-banks-policy-arsenal-3594525
- MacroMicro, China Interest Rate Corridor — https://en.macromicro.me/collections/31/cn-finance-relative/109608/cn-interest-rate-corridor-new · DR007 series https://en.macromicro.me/series/5899/cn-dr007 · TSF growth https://en.macromicro.me/collections/31/cn-finance-relative/132361/chinasocial-financing-monthly-increase-seasonal · PBoC balance sheet liabilities https://en.macromicro.me/collections/31/cn-finance-relative/17672/cn-major-liabilities-of-pboc-balance-sheets
- Trading Economics: [China Loan Prime Rate](https://tradingeconomics.com/china/interest-rate) · [7-day reverse repo rate](https://tradingeconomics.com/china/reverse-repo-rate) · [1-year MLF rate](https://tradingeconomics.com/china/1-year-mlf-rate) · [TSF](https://tradingeconomics.com/china/total-social-financing) · ["PBoC to Resume Treasury Bond Trading"](https://tradingeconomics.com/china/government-bond-yield/news/496556) · ["PBOC to Lower Sector-Specific Rates"](https://tradingeconomics.com/china/news/news/517507) · ["PBoC Cuts RRR, Lowers 7-day Reverse Repo"](https://tradingeconomics.com/china/reverse-repo-rate/news/457774)
- Seeking Alpha, "Chinese Banks' NIMs Near 'Critical Point'" — https://seekingalpha.com/article/4792302-chinese-banks-nims-near-critical-point
- Global Property Guide, "China's Residential Property Market Analysis 2026" — https://www.globalpropertyguide.com/asia/china/price-history
- Zins Capital, "Macro 101: China's Credit Impulse" — https://zinscapital.substack.com/p/macro-101-leading-indicators-chinas
- PipDigest, "China's Credit Impulse: Reading Total Social Financing for Global Turns" — https://piphawk.com/guides/china-credit-impulse-and-aggregate-financing
- Sagar Baniya, "China's M1 Money Supply Surge: A Statistical Adjustment, Not a Liquidity Boom" — https://sagarbaniya.substack.com/p/chinas-m1-money-supply-surge-a-statistical *(low-authority source; used only for the M1 level figures, flagged unverified)*
- Deloitte China, "Outlook of macro economy and industries in 2026" — https://www.deloitte.com/cn/en/our-thinking/research/issue101.html
- China Briefing, "China Unveils 10-Point Monetary Package to Stabilize Market Expectations" — https://www.china-briefing.com/news/china-10-point-monetary-package-market-stabilization/
- MNI, "PBOC May Have Another RRR Cut In 2025," 15 May 2025 — https://www.mnimarkets.com/articles/pboc-may-have-another-rrr-cut-in-2025-1747275215791
- Bank of Singapore, "People's Bank of China cuts rates" — https://www.bankofsingapore.com/research/peoples-bank-of-china-cuts-rates.html
- J.P. Morgan Asset Management, "China PBoC — Navigating the Imbalances" — https://am.jpmorgan.com/us/en/asset-management/liq/insights/liquidity-insights/updates/china-pboc-navigating-the-imbalances/
- IEU Monitoring, "IMF urges China to shift decisively toward consumption-led growth" — https://ieu-monitoring.com/editorial/imf-urges-china-to-shift-decisively-toward-consumption-led-growth-amid-structural-headwinds/864478
- PANews, "PBoC releases fourth-quarter 2025 monetary policy implementation report" — https://www.panewslab.com/en/articles/019c4751-daa5-7059-8261-e68e55b40ea5
- InsuranceNewsNet reprint, China Monetary Policy Report Q4 2025 — https://insurancenewsnet.com/oarticle/china-monetary-policy-report-q4-2025
- "Steps towards Rate Liberalization and RMB Internationalization," 18 June 2026 — https://cdn.prod.website-files.com/67cb23eaf0c6c4d4080e059a/6a3355ec916c7c620fb21f23_20260618_Steps%20towards%20Rate%20Liberalization%20and%20RMB%20Internationalization.pdf

---

*End of note 04.*
