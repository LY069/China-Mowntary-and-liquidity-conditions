# Monetary Conditions vs Liquidity Conditions: A Conceptual Framework, with Application to China

*Note 01 — Definitions and framework. Drafted 12 September 2026.*

---

## 0. Purpose, scope and a methodological caveat

This note fixes the vocabulary for the rest of the project. "Monetary conditions" and "liquidity conditions" are used interchangeably in a great deal of market commentary on China, and the conflation is not harmless: it is precisely the wedge between the two that carries the information. A statement such as "the PBoC has eased" can mean four mutually independent things — the policy rate fell, settlement balances in the interbank system rose, bank funding spreads compressed, or credit to the real economy accelerated — and in China these four have repeatedly moved in opposite directions for quarters at a time.

The note proceeds: (1) monetary conditions and the MCI tradition; (2) the four distinct senses of "liquidity"; (3) the core conceptual distinction and a typology of divergence, with China episodes; (4) the China institutional specifics that make the distinction sharper than in developed markets; (5) a practical taxonomy table; (6) financial conditions indices as the superset, and why China FCIs are built differently.

**Methodological caveat — please read.** In this session outbound page-fetching was blocked at the network egress proxy for every domain attempted (bis.org, imf.org, pbc.gov.cn and its provincial mirrors, rba.gov.au, bbvaresearch.com, federalreserve.gov, wikipedia.org, bofit.fi). All grounding below therefore comes from web-search result summaries and metadata, not from reading the primary PDFs directly. URLs are real and were returned by search; the documents behind them were **not** opened and verified line-by-line. Where a specific number or date matters and I could not corroborate it, I flag it inline as **[unverified]** or **[from prior knowledge, not verified in session]**. Section 8 collects the open items that should be checked against primary sources before this note is used for anything load-bearing.

---

## 1. Monetary conditions

### 1.1 The standard definition

**Monetary conditions** are the *stance of monetary policy as actually transmitted to the real economy* — that is, the combined restrictiveness or accommodation delivered by the price and quantity of money and credit and by the exchange rate, measured against some neutral benchmark, and assessed over the horizon on which monetary policy affects aggregate demand (roughly two to eight quarters).

Three features of that definition are doing work:

1. **Stance, not instrument.** Monetary conditions are not the policy rate. They are what the policy rate (plus everything else the central bank does, plus the endogenous response of markets) *delivers*. A central bank that holds its policy rate constant while the real neutral rate falls has tightened monetary conditions without moving an instrument.
2. **Real-economy horizon.** The relevant metric is the effect on aggregate demand and, through it, on inflation. This is a months-to-years object.
3. **Relative to neutral.** "Tight" and "loose" are only meaningful against a counterfactual — r*, a trend real exchange rate, a credit-to-GDP trend. This is where most of the measurement difficulty lives.

### 1.2 The MCI tradition: Bank of Canada, Freedman (1994)

The Monetary Conditions Index was the first serious attempt to make "stance" a single observable number. The Bank of Canada was the first central bank to compute an MCI, from the early 1990s, with the rationale set out by Charles Freedman ([Bank of Canada, "The role of monetary conditions and the monetary conditions index," 1994/1995](https://www.bankofcanada.ca/wp-content/uploads/2010/06/r954c.pdf); see also Freedman's chapter ["The Use of Indicators and of the Monetary Conditions Index in Canada," in *Frameworks for Monetary Stability*, IMF](https://www.elibrary.imf.org/display/book/9781557754196/ch018.xml)).

The construction is deliberately minimal:

> MCI_t = w_r (r_t − r_base) + w_e (e_t − e_base)

where r is a short-term interest rate (Canada used the 90-day commercial paper rate) and e is the log of an effective exchange rate index. The weights w are not statistical; they are **structural elasticities**, taken from simulations of the central bank's own macro model, quantifying the effect on GDP or final demand of a given change in each variable. In Canada's case the exchange rate carried roughly one-third the weight of the interest rate — the canonical "3:1" MCI ([Bank of Canada MCI background](https://www.bankofcanada.ca/wp-content/uploads/2010/06/r954c.pdf); [Bank of Canada archived MCI page, 2006](https://www.collectionscanada.gc.ca/eppp-archive/100/201/301/bank_can_review/2006/spring/cover/en/rates/mci2.html); the Bank still publishes a "monetary conditions" key-variables page, [Bank of Canada](https://www.bankofcanada.ca/rates/indicators/key-variables/monetary-conditions/)).

The logic is a small-open-economy IS curve: demand responds both to the domestic cost of borrowing and to competitiveness, so a stance measure that ignores the exchange rate mis-states policy in exactly the situations where getting it right matters most (a commodity shock, a global risk-off episode).

The MCI spread quickly. The Reserve Bank of New Zealand went furthest, adopting the MCI not merely as an indicator but as the **operating target** from mid-1997 — the RBNZ published desired MCI paths and the market moved short rates to deliver them. The RBNZ abandoned this in March 1999 in favour of the Official Cash Rate; its MCI series is now archived as discontinued ([RBNZ, "MCI (B2) — discontinued"](https://www.rbnz.govt.nz/statistics/discontinued-statistics/mci-b2); [RBNZ discontinued statistics hub](https://www.rbnz.govt.nz/hub/statistics/discontinued/mci)). The retrospective judgement is unkind: implementing policy via the MCI through the Asian crisis "shaped the response in a way that probably contributed to the fall in output and added unnecessary interest rate volatility" ([McDermott & Williams, "Inflation Targeting in New Zealand: An Experience in Evolution," RBA Conference 2018](https://www.rba.gov.au/publications/confs/2018/mcdermott-williams.html)). Svensson's independent review for the NZ Treasury covers the same ground ([*Independent Review of the Operation of Monetary Policy in New Zealand*, NZ Treasury, 2001](https://www.treasury.govt.nz/sites/default/files/2007-11/indrevopmonpol.pdf)).

### 1.3 What an MCI does and does not measure

**Does measure:** a model-weighted summary of the two transmission channels that a small open economy's central bank can plausibly claim to influence at a two-to-six quarter horizon. It is a *communication device* and a *cross-check*: it prevents the mistake of declaring policy unchanged when the currency has moved 10%.

**Does not measure:**

- **Credit quantities or credit standards.** An MCI is silent on whether banks are willing to lend at the posted rate. In a credit crunch the MCI can be at its loosest reading on record while the marginal borrower cannot get a loan.
- **Risk premia and the term structure.** A single short rate misses term premium and credit spread moves — which since 2008 have done much of the work of transmission.
- **Asset prices and collateral values.** Housing and equity wealth/collateral channels are absent.
- **Anything about the financial system's own plumbing** — settlement balances, repo functioning, dealer capacity.
- **The neutral benchmark.** An MCI is an index relative to an arbitrary base period, not relative to r*. Levels are uninterpretable; only changes carry (contested) meaning.

### 1.4 The critiques

Four distinct critiques, which are often run together but should not be:

**(i) Weight instability and model dependence.** The weights come from one macro model at one point in time. Different models, different samples, different specifications give materially different ratios. The Ericsson et al. work demonstrates the sensitivity directly: the Canadian MCI evaluated at alternative relative weights produces visibly different histories of "conditions" ([Ericsson, Jansen, Kerbeshian & Nymoen, "Interpreting a Monetary Conditions Index in Economic Policy," *Topics in Monetary Policy Modelling*, BIS Conference Papers Vol. 6, 1998, pp. 237–254](https://www.bis.org/publ/confp06i.pdf); volume: [BIS Conference Papers Vol. 6](https://www.bis.org/publ/confp06.pdf); working-paper predecessor, [Ericsson et al., "Hazards in Implementing a Monetary Conditions Index," Federal Reserve IFDP, October 1996](https://www.federalreserve.gov/econres/ifdp/hazards-in-implementing-a-monetary-conditions-index.htm)).

**(ii) The Ericsson–Jansen–Kerbeshian–Nymoen (1998) result proper.** Their conclusion is stronger than "the weights are uncertain." They evaluate the sensitivity of MCIs to an *inherent* source of uncertainty in their calculation and conclude that this uncertainty "typically renders MCIs uninformative for their ostensible purposes." The deeper objection is that an MCI is a linear combination imposed *outside* any structural model with stable microfoundations; its stability and predictive power are therefore not guaranteed by anything, and it is vulnerable to the Lucas critique. Summary and abstract: [ResearchGate record](https://www.researchgate.net/publication/228560144_Interpreting_a_Monetary_Conditions_Index_in_Economic_Policy).

**(iii) Endogeneity / shock-identification.** This is the critique that killed the MCI operationally. The correct policy response to an exchange rate move depends entirely on *why* the exchange rate moved. A depreciation driven by a terms-of-trade/demand shock (New Zealand 1997–98) calls for *easier* policy; an MCI mechanically reads the depreciation as easing and calls for *tighter* policy. The index cannot distinguish a shock to the IS curve from a shock to UIP. Glenn Stevens made exactly this argument contemporaneously ([RBA, "Pitfalls in the Use of Monetary Conditions Indexes," speech, 16 July 1998](https://www.rba.gov.au/speeches/1998/sp-ag-160798.html); see also [RBA Bulletin, August 1998](https://www.rba.gov.au/publications/bulletin/1998/aug/pdf/bu-0898-2.pdf), and [Central Bank of Ireland, "A Discussion of the Monetary Conditions Index"](https://www.centralbank.ie/docs/default-source/publications/quarterly-bulletins/quarterly-bulletin-signed-articles/discussion-of-the-monetary-con-index.pdf?sfvrsn=3df6d11d_7)).

**(iv) The Lucas critique in its operational form.** Once an MCI becomes an operating target, market participants trade the index rather than the economy, and the reduced-form relationship between the index and demand — the very relationship used to derive the weights — changes. New Zealand is the worked example. This is why the MCI survives today as a *dashboard item* and not as a target.

The taxonomy of critiques matters for us because critiques (i) and (iii) apply with *greater* force to China (a managed float, a partially administered rate structure, and an economy where credit quantities matter more than rates), while critique (iv) applies with *less* force (nobody targets a China MCI).

### 1.5 From MCI to FCI: Goodhart & Hofmann

The natural repair is to add the missing channels. Goodhart and Hofmann proposed broadening the MCI into a **Financial Conditions Index** by adding real house prices and real equity prices to the short rate and real exchange rate, with weights again derived from reduced-form demand equations and from impulse responses of an identified VAR, estimated for the G7 ([Goodhart & Hofmann, "Asset Prices, Financial Conditions, and the Transmission of Monetary Policy," prepared for the conference on Asset Prices, Exchange Rates, and Monetary Policy, Stanford University, 2–3 March 2001, FRBSF](https://www.frbsf.org/wp-content/uploads/0103conf6.pdf); conference overview, [FRBSF Economic Letter, "Asset Prices, Exchange Rates, and Monetary Policy"](https://www.frbsf.org/research-and-insights/publications/economic-letter/asset-prices-exchange-rates-and-monetary-policy/); related, [Goodhart & Hofmann, "Asset Prices and the Conduct of Monetary Policy," 2002](http://repec.org/res2002/Goodhart.pdf)). Their headline finding is that **house prices in particular add information about future inflationary pressure** beyond the MCI components.

The post-crisis generation of FCIs (Section 6) abandons the structural-weight approach for factor extraction. Note that this is a genuine methodological fork, not a refinement: structural-weight indices answer "how much demand impulse," factor indices answer "what is the common financial factor." They are not the same object and should not be compared casually.

---

## 2. Liquidity conditions: four different things wearing one word

"Liquidity" in macro-financial usage denotes at least four distinct objects. They are related but analytically independent, and the interesting China questions almost always live in the gaps between them.

### 2.1 (a) Central bank / reserve liquidity — the settlement-balance sense

**Definition.** The quantity and price of central bank money (settlement balances / reserves) available to the banking system to settle interbank obligations and meet reserve requirements.

This is the narrowest and most precise sense. The relevant objects are:

- **Quantity:** the level of banks' deposits at the central bank in excess of required reserves, plus the maturity profile of outstanding central bank operations.
- **Price:** the secured overnight/short-term interbank rate at which those balances trade, relative to the policy rate.
- **Drivers:** the central bank's own operations (repo/reverse repo, reserve requirement changes, outright purchases) *plus* **autonomous factors** — items on the central bank balance sheet that move reserves without any policy decision: banknotes in circulation, government deposits at the central bank, and foreign exchange intervention.

In China the operating target is explicitly the short interbank secured rate. The framework is a chain: **policy rate → market benchmark rate → market rates**, implemented as **7-day OMO reverse repo rate → DR007 → money market rates**. DR007 is the 7-day collateralised repo rate *between depository institutions only*; R007 is the same tenor across *all* financial institutions, i.e. including non-banks (see discussion in [Keynes Watch, "China's Interest Rate Corridor: FDR007, SHIBOR, SLF, IOER & OMO"](https://keyneswatch.com/cn/shibor) and [MacroMicro, China interest rate corridor](https://en.macromicro.me/collections/31/cn-finance-relative/109608/cn-interest-rate-corridor-new)). The distinction is not pedantic: **R007 − DR007 is the cleanest available China proxy for the price of the bank/non-bank liquidity boundary**, i.e. it is where sense (a) meets sense (b).

**Key point:** central-bank liquidity is a *system-level* quantity that the central bank controls essentially exactly, if it wishes to. Its level tells you almost nothing about credit to the real economy.

### 2.2 (b) Funding liquidity — of banks and non-banks

**Definition.** The ease with which an individual institution can raise cash against its future obligations — "the ease of raising cash by selling new obligations to investors" ([BIS, "About global liquidity indicators"](https://www.bis.org/statistics/dataportal/gli.htm)). Formally: the ability to meet obligations as they fall due without fire-selling assets.

This is an *institution-level, distributional* concept. System-wide reserve abundance is consistent with acute funding stress at particular institutions, because reserves do not redistribute themselves — they redistribute only through a functioning interbank market, and that market is a network with credit limits, collateral haircuts and counterparty tiering.

China indicators: NCD (negotiable certificate of deposit, 同业存单) issuance rates and issuance success ratios by bank tier; the spread of joint-stock and city/rural commercial bank NCD rates over large-bank NCD rates; R007 − DR007; non-bank repo volumes and haircuts; the loan-to-deposit and liquidity coverage positions of smaller banks.

The academic anchor is [Brunnermeier & Pedersen, "Market Liquidity and Funding Liquidity," *Review of Financial Studies* 22(6), 2009, pp. 2201–2238](https://academic.oup.com/rfs/article-abstract/22/6/2201/1592184) ([NBER WP 12939](https://www.nber.org/papers/w12939)): traders supply market liquidity, their capacity to do so depends on their funding, and their funding depends in turn on the market liquidity of the assets they post as collateral. Under identifiable conditions margins are destabilising and the two liquidities are mutually reinforcing, producing **liquidity spirals**. This is the mechanism that links senses (b) and (c).

### 2.3 (c) Market liquidity

**Definition.** The ease of raising cash by selling an *asset* — or equivalently, the cost of immediacy. The standard decomposition is into **tightness** (bid-ask spread, the cost of a round trip), **depth** (size executable without moving price), and **resilience** (speed of price recovery after an uninformed trade). *[This tripartite decomposition is conventionally attributed to Kyle (1985), "Continuous Auctions and Insider Trading," Econometrica 53(6). I could not verify a URL for it in this session — cited from standard knowledge.]*

China indicators: CGB and policy-bank bond bid-ask spreads and turnover, on-the-run/off-the-run spreads, credit bond turnover ratios (which are structurally very low outside the top tier), the size of the gap between exchange-traded and interbank pricing, and — importantly for China — the behaviour of the wealth management product (WMP, 银行理财) and bond mutual fund complex, which is the marginal price-setter in credit bonds. On the determinants of Chinese credit-bond liquidity see [Chen et al., "What drives liquidity in the Chinese credit bond markets?" (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S2405918824000242); on the fragility of the WMP investor base see ["Investors awaken: Fragility in China's wealth management product market" (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S0927539826000319) and ["China's debt market: Evolution, regulation, and global integration" (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S0927538X25000885).

### 2.4 (d) "Macro liquidity" / global liquidity — the BIS definition

**Definition (BIS/CGFS).** Global liquidity is **the ease of financing in global financial markets**. It is explicitly *not* a money aggregate. The BIS decomposes it into ([BIS, "About global liquidity indicators"](https://www.bis.org/statistics/dataportal/gli.htm); [BIS data glossary, "Global liquidity"](https://data.bis.org/help/glossary?item=Global+liquidity)):

- **Official liquidity** — created by central banks through conventional and unconventional policy; the means of final settlement of claims through monetary authorities.
- **Private liquidity** — created by financial institutions, largely through cross-border operations of banks and through international bond markets.

The canonical statement is [CGFS Papers No. 45, *Global liquidity — concept, measurement and policy implications*, November 2011](https://www.bis.org/publ/cgfs45.htm) ([PDF](https://www.bis.org/publ/cgfs45.pdf); [press release](https://www.bis.org/press/p111113.htm)), prepared by an ad-hoc group chaired by Jean-Pierre Landau. Two of its conclusions matter here: first, the term's ambiguity "can lead to unfounded and potentially destabilising policy initiatives" — an explicit warning against exactly the conflation this note is trying to prevent; second, private liquidity is the destabilising component, both in its own right and because it *amplifies cyclical movements in domestic financial conditions*.

The BIS's operational measure — the **Global Liquidity Indicators (GLIs)** — deliberately proxies ease of financing by *credit to non-bank borrowers*: bank loans plus international debt securities, with the headline focus on **foreign-currency credit denominated in USD, EUR and JPY to borrowers outside the respective currency areas** ([BIS GLI methodology](https://www.bis.org/statistics/gli/gli_methodology.pdf); [BIS Quarterly Review, "Global liquidity indicators: background and interpretation," March 2015](https://www.bis.org/publ/qtrpdf/r_qt1503u.htm); latest release, [BIS GLIs at end-June 2025](https://www.bis.org/statistics/gli2510.htm); conceptual background, [BIS Working Paper 402, *Understanding Global Liquidity*](https://www.bis.org/publ/work402.pdf)). Parallel treatments: [IMF, *Global Liquidity — Credit and Funding Indicators*, July 2013](https://www.imf.org/external/np/pp/eng/2013/071613b.pdf); [ECB Monthly Bulletin, October 2012](https://www.ecb.europa.eu/pub/pdf/other/art1_mb201210en_pp55-68en.pdf); [ECB Financial Stability Review, December 2011](https://www.ecb.europa.eu/pub/pdf/fsr/art/ecb.fsrart201112_03.en.pdf).

**Note the trap.** "Global liquidity" in the BIS sense is a *credit* concept, whereas "global liquidity" in common market usage often means the sum of G4 central bank balance sheets — i.e. official liquidity only. These behave very differently. For China specifically, the BIS GLI framing is the more useful one, because China's exposure to global liquidity runs primarily through USD credit to Chinese non-bank borrowers (offshore bond issuance, trade finance) and through the CNH market, not through PBoC reserve balances.

### 2.5 How the four interact — and where they decouple

**Interactions (the normal case).**

- (a) → (b): central bank reserve provision relieves bank funding pressure, *provided* the interbank distribution mechanism works.
- (b) ↔ (c): the Brunnermeier–Pedersen spiral. Dealers and leveraged funds cannot make markets without funding; funding is collateralised against assets whose haircuts depend on market liquidity.
- (a)+(b)+(c) → (d): domestic official and private liquidity conditions in reserve-currency jurisdictions determine the global supply of cross-border credit.
- (d) → (a) in China: dollar liquidity conditions and the CNY/CNH basis feed back into the PBoC's room to set domestic rates (Section 4.3).

**Decoupling — the cases that matter.**

1. **(a) ample, (b) tight — the distribution failure.** Aggregate reserves are abundant but counterparty limits, collateral eligibility or regulatory ratios stop them reaching the institutions that need them. In China this is the classic large-bank/small-bank split: the big five are structurally net lenders in repo, and when they retrench, DR007 can stay near the policy rate while smaller banks' NCD rates blow out. China's money market is genuinely *segmented*, which is the central finding of the literature on the 2013 episode ([Fan & Zhang / arXiv, "The transmission of liquidity shocks via China's segmented money market"](https://arxiv.org/pdf/1811.08949)).
2. **(b) ample, (c) tight — the market-structure failure.** Everyone has cash, nobody will make a price. Credit bonds in China exhibit this chronically: turnover in lower-rated credit is thin even in easy funding regimes, because the natural holders (WMPs, bank treasury books) are buy-and-hold and the dealer balance sheet is small.
3. **(c) collapses while (a) is being expanded — the spiral.** November–December 2022: the reopening-driven bond sell-off met a WMP investor base that had only just been forced onto mark-to-market NAV accounting by the asset management rules, producing a redemption cascade. Managers of domestic mutual funds and WMPs offloaded roughly RMB1.3 trillion of bonds from the interbank market in November 2022, reportedly the most on record; the 10-year CGB yield rose about 24bp in the month and credit saw its worst sell-off in five years; financial products held around RMB35.7 trillion of China bonds at end-November, roughly 28% of the interbank market ([Bloomberg via Yahoo Finance, "Chinese Funds Dump Record Amount of Bonds Amid Redemptions"](https://finance.yahoo.com/news/chinese-funds-dump-record-amount-075434239.html); [Caixin, "Behind the Massive Sell-Off in Chinese Wealth Management Products"](https://caixinchinawatch.substack.com/p/cx-daily-behind-the-massive-sell)). Central bank liquidity was not the binding constraint; the redemption channel was.
4. **(a),(b),(c) all ample, but monetary conditions tight.** The deflationary case: nominal easing that does not deliver a lower *real* rate or any credit expansion. This is Section 3.

---

## 3. The key conceptual distinction

### 3.1 The distinction stated

| | **Monetary conditions** | **Liquidity conditions** |
|---|---|---|
| **What it is** | The medium-term policy stance as transmitted to aggregate demand | The short-horizon availability and price of settlement balances and funding |
| **Horizon** | Months to years (2–8 quarters) | Days to weeks (intraday to one quarter) |
| **Domain** | The real economy — investment, consumption, inflation | The financial system — banks, non-banks, dealers |
| **Core variables** | Real policy rate vs r*, real lending rate, credit growth vs nominal GDP, REER | Excess reserves, DR007/R007 vs policy rate, NCD spreads, repo volumes |
| **Who controls it** | The central bank *jointly with* banks' risk appetite, borrowers' demand, fiscal policy, and the external environment | The central bank, essentially unilaterally, subject to autonomous factors |
| **Failure mode** | Stance mis-measured because r* or credit demand shifted | Stance delivered but does not reach the marginal borrower |

The single most useful way to hold the distinction: **liquidity conditions are about the central bank's liability side and the interbank market's ability to redistribute it; monetary conditions are about the banking system's asset side and the private sector's willingness to use it.** The central bank fully controls the first. It only influences the second.

### 3.2 When and why they diverge

There are four canonical divergences.

**(i) Loose liquidity, tight credit — "pushing on a string."** The central bank floods reserves; banks hold them or buy government bonds; credit to the real economy does not expand. Keynes's liquidity trap in its modern, credit-channel form. The binding constraint is either borrower demand (balance-sheet repair, weak expected returns) or bank willingness (capital, NPL recognition, risk appetite).

**(ii) Loose liquidity, tight *monetary* conditions.** Distinct from (i) and more insidious: nominal rates are cut, interbank funding is cheap, credit even grows — but *inflation falls faster than the nominal rate*, so the ex-post real rate rises. Monetary conditions tighten while every liquidity gauge loosens. This is the central analytical issue for China 2023–2026 and the reason the MCI/FCI framing must be run in real terms.

**(iii) Tight liquidity, loose credit.** The deliberate macroprudential configuration: keep interbank funding expensive to punish leverage and maturity transformation in the financial sector, while directing bank credit to the real economy through window guidance and structural tools. China 2016–2018 is the textbook case; the PBoC's own vocabulary for it is squeezing out **资金空转** (funds circulating idly within the financial system).

**(iv) Tight liquidity, tight everything — the crunch.** Money market stress that transmits to credit because banks' funding costs rise and they ration lending. China June 2013.

**The Chinese market's own vocabulary is superior to the English here**, and we should adopt it. Chinese sell-side research works with an explicit **货币–信用框架** ("money–credit framework"), crossing two binary states:

- **宽货币** (*kuan huobi*, "loose money") — the monetary authority creates an easy monetary environment and releases easing signals: low policy rates, ample interbank liquidity, RRR cuts. This is **liquidity conditions**.
- **宽信用** (*kuan xinyong*, "loose credit") — effective credit expansion in the real economy, reflected in the willingness, availability and capacity of real-economy sectors to finance. This is (most of) **monetary conditions**.

The framework's own statement of the point is exactly ours: control of 宽货币 rests with the monetary authority, whereas control of 宽信用 is more complex — it involves commercial banks as credit intermediaries *and* the leverage decisions of the borrowing entities themselves; hence "宽货币紧信用" (loose money, tight credit) and "紧货币宽信用" (tight money, loose credit) are both observable states ([理清宽货币和宽信用的基本内涵](https://credit.bjdx.gov.cn/xyxc/detail/81e35e3e5dcf4aa99dccf88938c3973d); [从宽货币传导到宽信用：三部曲之理论篇, Sina Finance](https://finance.sina.cn/china/gncj/2019-04-29/detail-ihvhiqax5771553.d.html); [「货币-信用框架」深度解析, 36Kr](https://www.36kr.com/p/2125384897560321); [关于宽货币向宽信用传导的基本逻辑探究, Sina Finance](https://finance.sina.cn/stock/qz/2022-05-05/detail-imcwiwst5650653.d.html?from=wap)).

The four-quadrant 宽/紧货币 × 宽/紧信用 map is, in practice, the most tractable framework for China asset allocation, and it is precisely the monetary-vs-liquidity distinction operationalised.

### 3.3 China episodes of divergence

**June 2013 — the 钱荒 ("cash crunch"): tight liquidity, no change in monetary stance.**
Overnight SHIBOR jumped from 7.66% on 19 June to 13.44% on 20 June 2013, with 7-day repo printing far higher intraday; rates settled back to a still-elevated 5–8% range by 25 June. The PBoC's own account attributed it to rapid loan growth, corporate income tax payments, required reserve payments and holiday cash demand; market participants read it as the PBoC deliberately withholding liquidity to discipline shadow-bank maturity transformation ([BIS Quarterly Review, "Interbank volatility in China," September 2013](https://www.bis.org/publ/qtrpdf/r_qt1309u.htm); [Wikipedia, "Chinese Banking Liquidity Crisis of 2013"](https://en.wikipedia.org/wiki/Chinese_Banking_Liquidity_Crisis_of_2013); [Bruegel, "Has the Chinese central bank really taken a hard line on liquidity?"](https://www.bruegel.org/blog-post/has-chinese-central-bank-really-taken-hard-line-liquidity); [Rhodium Group, "China's Interbank Squeeze"](https://rhg.com/research/chinas-interbank-squeeze-understanding-the-2013-drama-and-anticipating-2014/); on segmentation as the transmission mechanism, [arXiv 1811.08949](https://arxiv.org/pdf/1811.08949)).
*Diagnosis:* an extreme sense-(a)/(b) event with no change in the medium-term stance. Benchmark deposit and lending rates were untouched; credit growth was barely dented. Anyone reading this as "the PBoC tightened monetary policy" mis-read it.

**2016–2018 — the deleveraging campaign: tight liquidity by design, credit redirected not withdrawn.**
From mid-2016 the authorities ran a deliberate wedge. The PBoC lengthened the maturity of its OMO provision (reintroducing 14-day reverse repos from August 2016) to raise the cost of carrying leveraged bond positions; off-balance-sheet WMPs were brought into the Macro Prudential Assessment framework around December 2016; OMO rates were raised from January 2017; and in August 2017 the NCD "bonds payable" loophole was closed ([CSIS, *Timeline of China's Deleveraging Campaign*](https://features.csis.org/timeline-of-chinas-deleveraging-campaign/); [Rhodium Group, *Grasping Shadows: The Politics of China's Deleveraging Campaign*](https://rhg.com/research/grasping-shadows/) and [CSIS version](https://www.csis.org/analysis/grasping-shadows-politics-chinas-deleveraging-campaign); [SUERF, "Recent developments in Chinese shadow banking"](https://www.suerf.org/wp-content/uploads/2023/11/f_673271cc47c1a4e77f57e239ed4d28a7_1697_suerf.pdf)). *[The precise month-by-month sequence above should be re-checked against the CSIS timeline; I could not open it.]*
*Diagnosis:* liquidity conditions were tightened hard while the *intent* on real-economy credit was neutral-to-supportive. The campaign nonetheless ended up cutting overall credit growth materially — evidence that the wedge is hard to sustain, because shadow credit *was* real-economy credit.

**Q3 2022 — loose liquidity, dead credit demand.**
The PBoC's own report puts DR007 at **1.52%** on average in Q3 2022, down 20bp from Q2 and 65bp year-on-year ([PBoC, *China Monetary Policy Report Q3 2022*, 16 November 2022](https://www.pbc.gov.cn/en/3688229/3688353/3688356/4583781/4773672/2023011810581221413.pdf)). That is far *below* the prevailing 7-day reverse repo policy rate *[which I believe was 2.00% after the August 2022 cut — from prior knowledge, not verified in session]*. Money market rates trading persistently through the policy rate floor is the signature of reserve abundance meeting no loan demand: banks could not deploy funds, so they lent them to each other at any price.
*Diagnosis:* textbook 宽货币紧信用. The MCI-style read ("rates are low, policy is loose") and the credit read ("the private sector is not borrowing") point in opposite directions.

**2024 — the statistical divergence: 手工补息 and the collapse in M1.**
In April 2024 the Market Interest Rate Pricing Self-Discipline Mechanism (市场利率定价自律机制) banned banks from paying **手工补息** ("manual interest supplementation") — discretionary top-up interest paid outside the authorised deposit-rate ceiling, typically to large corporate depositors. Banks lost around RMB3.92 trillion of deposits in April 2024 alone; new RMB deposits in Jan–Apr 2024 fell roughly 51% year-on-year to RMB7.32 trillion; M1 growth turned negative in the spring of 2024, and corporate money migrated to WMPs ([China Banking News, "China struggles to boost lending as households deleverage"](https://www.chinabankingnews.com/p/china-struggles-to-boost-lending); [China Banking News, "Chinese bank deposits shrink after PBOC's rate cut"](https://www.chinabankingnews.com/p/chinese-bank-deposits-shrink-after); [Asia Times, "Unleashed bank deposits misused in Chinese economy"](https://asiatimes.com/2024/05/unleashed-bank-deposits-misused-in-chinese-economy/); [Yicai, "China Logs Record Low M1, M2 Money Supply Growth in June"](https://www.yicaiglobal.com/news/growth-of-chinas-key-money-supply-indicators-shrink-to-record-low-in-june)).
Governor Pan Gongsheng's framing is the key sentence for this note: the regulatory measures had the effect of **"squeezing water"** out of the financial aggregates but **did not represent a shift in the monetary policy stance** ([Pan Gongsheng, keynote at the 15th Lujiazui Forum, June 2024 — BIS Review](https://www.bis.org/review/r240621c.htm); [PBoC English text](https://www.pbc.gov.cn/en/3688110/3688175/2025080817533718827/index.html)). The stated aims were improving transmission efficiency, smoothing credit growth, reducing resource misallocation and easing **资金空转** — funds circulating for arbitrage rather than financing activity.
*Diagnosis:* a *measurement* divergence, distinct from the others. The monetary aggregates tightened sharply while neither liquidity nor stance did. Any China MCI or FCI that loads on M1/M2 broke in 2024 for purely definitional reasons.

**2025–2026 — the persistent state: ample liquidity, weak credit, structural tools doing the work.**
The stance has been officially **适度宽松** ("moderately loose") since the December 2024 Central Economic Work Conference — the first time since 2010 that the formulation moved away from "prudent" ([Central Banking, "China shifts to 'moderately loose' monetary policy stance"](https://www.centralbanking.com/central-banks/monetary-policy/7963471/china-shifts-to-moderately-loose-monetary-policy-stance); [CNBC, 9 December 2024](https://www.cnbc.com/2024/12/09/china-vows-more-active-fiscal-stimulus-measures-moderately-looser-monetary-policy-next-year-.html); [APCO, "China's 2024 CEWC: Six Key Takeaways"](https://apcoworldwide.com/blog/chinas-2024-central-economic-work-conference-six-key-takeaways/)). Yet the credit side has not responded: new RMB bank loans in 2025 totalled about RMB16.27 trillion, reportedly the lowest since 2018, and TSF growth was around 7.7% year-on-year in May 2026; in late May 2026 the PBoC resorted to window guidance, instructing major state banks to boost lending as credit weakness persisted ([Reuters via US News, "PBOC Tells Chinese Banks to Boost May Lending as Credit Weakness Persists," 28 May 2026](https://money.usnews.com/investing/news/articles/2026-05-28/exclusive-pboc-tells-chinese-banks-to-boost-may-lending-as-credit-weakness-persists-sources-say); [Trading Economics, China new bank loans](https://tradingeconomics.com/china/new-bank-loans/news/509549)). In June 2026 the PBoC reportedly cut its daily OMO size to zero for the first time in nearly two years, explicitly to push idle bank cash toward the real economy ([The Standard, "China's PBOC shuts liquidity tap for first time in 2 years, nudging idle cash into economy"](https://www.thestandard.com.hk/finance/article/333678/Chinas-PBOC-shuts-liquidity-tap-for-first-time-in-2-years-nudging-idle-cash-into-economy)).
The "liquidity trap" label is contested but widely applied ([Capital Economics, "Is China caught in a 'liquidity trap'?"](https://www.capitaleconomics.com/clients/publications/china-economics/china-watch/is-china-caught-in-a-liquidity-trap); [China Banking News, "How China hopes to escape a liquidity trap using central bank credit guidance"](https://www.chinabankingnews.com/p/how-china-hopes-to-escape-a-liquidity)). Miao Yanliang (CICC Chief Strategist, formerly SAFE Chief Economist) frames it as a transmission blockage requiring fiscal–monetary coordination rather than further monetary injection — "ample funding, scarce demand" ([East Is Read, "Miao Yanliang explains China's large monetary injection yet blocked transmission"](https://www.eastisread.com/p/miao-yanliang-explains-chinas-large); [Pekingnology, "Miao Yanliang: how did China's low inflation come about?"](https://www.pekingnology.com/p/miao-yanliang-how-did-chinas-low)).
*Diagnosis:* divergence types (i) and (ii) simultaneously. Liquidity ample, credit weak, and — because of the price level — real monetary conditions arguably tighter than the nominal rate path suggests.

---

## 4. China institutional specifics: why the distinction bites harder than in DM

### 4.1 Quantity-based vs price-based: a transition still in progress

The PBoC has historically operated a **hybrid** framework, in which quantity instruments did the heavy lifting:

- **Window guidance (窗口指导)** — informal, usually verbal, directives to commercial banks on the volume and destination of lending. Formalised around 1998, and still in use: in 2007 lending was virtually frozen by window guidance; in 2008 and 2010 quarterly and monthly lending quotas were imposed; from around 2014 the practice was progressively folded into the Macro Prudential Assessment (MPA) system ([Grokipedia, "Window guidance"](https://grokipedia.com/page/Window_guidance); [Wikipedia, "Window guidance"](https://en.wikipedia.org/wiki/Window_guidance); [China Policy, "Beijing swaps credit quotas for market rules"](https://chinapolicy.substack.com/p/beijing-swaps-credit-quotas-for-market); [Capital Economics, "PBOC window guidance"](https://www.capitaleconomics.com/clients/publications/china-economics/china-economics-weekly/pboc-window-guidance-census-data-gems)). It remains live in 2026 (Section 3.3).
- **Credit quotas (信贷额度)** and mandated lending targets for priority borrower classes (SMEs, agriculture, green, tech).
- **The reserve requirement ratio (存款准备金率, RRR)** — used both as a structural sterilisation tool during the FX-accumulation era and, latterly, as the principal medium-term liquidity injection tool. RRR is **differentiated by institution type**. As of January 2026 the vice-governor put the *weighted average* RRR at about **6.3%** with further room to cut, while the headline large-bank ratio was around **7.5%** in early 2026 ([China Daily, "China still has room for RRR and interest rate cuts, central bank says," 15 January 2026](https://global.chinadaily.com.cn/a/202601/15/WS6968a0e8a310d6866eb33f31.html); [gov.cn, 22 January 2026](https://english.www.gov.cn/news/202601/22/content_WS69720cd8c6d00ca5f9a08b8c.html); [SCMP, "China's central bank signals reserve ratio, interest rate cuts in 2026"](https://www.scmp.com/economy/china-economy/article/3339018/chinas-central-bank-signals-reserve-ratio-interest-rate-cuts-2026); [CEIC, China RRR](https://www.ceicdata.com/en/indicator/china/reserve-requirement-ratio); [PBoC, Required Reserves](https://www.pbc.gov.cn/en/3688229/3688335/3730270/index.html)). *[The 6.3% weighted-average vs 7.5% large-bank figures come from different reports and are not inconsistent, but the exact current values should be re-confirmed.]*
- **Quantity intermediate targets.** The numerical M2 growth target disappeared from the Government Work Report from 2018, on the explicit grounds that M2's relationship with GDP and with credit had deteriorated as shadow financing spawned new channels ([Caixin, "Whither M2? Money Supply Target Falls Out of Favor," March 2019](https://www.caixinglobal.com/2019-03-05/whither-m2-money-supply-target-falls-out-of-favor-101388006.html)). The replacement is a *qualitative* formulation: the growth of aggregate financing and money supply should be "basically in line with nominal economic growth," or more recently "matched to the expected targets for economic growth and the general price level" (同经济增长和价格水平预期目标相匹配) ([Xinhua, 24 December 2025](https://english.news.cn/20251224/2f8fe826e6a34b5aaa1b833760e225e3/c.html); [gov.cn, 24 December 2025](https://english.www.gov.cn/news/202512/24/content_WS694bf171c6d00ca5f9a0843e.html)). The inclusion of the *price level* in that formula is analytically important: it is an implicit commitment to let nominal credit growth absorb a deflationary shock.

Background on the transition: [Kim & Chen, "From a Quantity to an Interest Rate-Based Framework" (Atlanta Fed workshop, 2019)](https://www.atlantafed.org/-/media/documents/news/conferences/2019/0919-workshop-on-chinas-economy/papers/kim-chen_from-a-quantity-to-an-interest-rate-based-framework.pdf); [IMF WP 18/244, *China's Monetary Policy Communication*](https://www.imf.org/-/media/Files/Publications/WP/2018/wp18244.ashx); [RBA Bulletin, "China's Monetary Policy Framework and Financial Market Transmission," April 2024](https://www.rba.gov.au/publications/bulletin/2024/apr/chinas-monetary-policy-framework-and-financial-market-transmission.html); [Yi Gang, "China's monetary policy framework," BIS Review, 2019](https://www.bis.org/review/r190130b.htm).

**Implication for us:** where the operative instrument is a *quantity of credit administratively allocated*, the price of interbank liquidity is a much weaker summary statistic for the policy stance than in a DM inflation-targeting regime. Monetary and liquidity conditions are institutionally separated in China in a way they are not in the US or euro area.

### 4.2 The dual-track interest rate system and LPR reform (2019)

Until 2019 China ran a **利率双轨制** ("dual-track interest rate system"): market-determined rates in the money and bond markets on one track, and PBoC-set benchmark deposit and lending rates (基准利率) anchoring bank pricing on the other. Policy rate changes in the money market did not reliably pass through to loan pricing because banks priced off the benchmark, often at a floor multiple of it.

The reform slogan was **两轨合一轨** ("merging the two tracks into one"). On 17 August 2019 the PBoC designated the reformed **Loan Prime Rate (贷款市场报价利率, LPR)** as the pricing benchmark for new household and corporate loans, replacing the benchmark 1-year lending rate. The LPR is a trimmed weighted average of quotations from a panel of (initially 18) banks, submitted monthly on the 20th, quoted as a spread over the PBoC's medium-term policy rate ([CNBC, 17 August 2019](https://www.cnbc.com/2019/08/17/pboc-unveils-rate-reform-to-lower-borrowing-cost-for--chinese-firms.html); [RBA, "Recent reforms to lending rates in China," SMP box, November 2019](https://www.rba.gov.au/publications/smp/2019/nov/pdf/box-a-recent-reforms-to-lending-rates-in-china.pdf); [gov.cn, "China's LPR reform yields fruitful results"](https://english.www.gov.cn/statecouncil/ministries/202006/01/content_WS5ed4f106c6d0b3f0e9499398.html); [Pekingnology, "Central bank reports its progress of interest rate liberalization since 2017"](https://www.pekingnology.com/p/central-bank-reports-its-progress)).

**Why this matters for the monetary/liquidity distinction:** LPR reform was an attempt to *close* the gap between liquidity conditions (money market) and monetary conditions (loan pricing). It partially succeeded — lending rates now move with policy — but the transmission remains administered at the margin, since the LPR is a submitted quotation subject to self-discipline-mechanism guidance rather than a traded rate. As of August 2026 the 1-year LPR stood at 3.00% and the 5-year-plus at 3.50%, unchanged for 15 consecutive months ([BigGo Finance summary of LPR fixings](https://finance.biggo.com/news/448d1250-6cdf-4651-b95a-6c85fe5fda9e)). *[Levels from a secondary aggregator; confirm against the PBoC/NIFC fixing.]*

A live complication: the 5-year LPR anchors mortgages, and repricing conventions mean policy rate cuts reach the existing mortgage stock only with long and administratively determined lags. The stance transmitted to household balance sheets is therefore materially different from the stance transmitted to new corporate borrowing.

### 4.3 Capital controls, the impossible trinity, and the exchange rate as a constraint

China's historical resolution of the trilemma was to run a managed exchange rate and an autonomous domestic monetary policy, purchased with capital controls ([CEPII WP 2011-27, *The Impossible Trinity Revised: An Application to China*](https://www.cepii.fr/PDF_PUB/wp/2011/wp2011-27.pdf); [Sun & Payette, "China and the Impossible Trinity," *CCPS*](https://icaps.nsysu.edu.tw/var/file/131/1131/img/2375/CCPS2(3)-Sun-Payette.pdf); [Wikipedia, "Impossible trinity"](https://en.wikipedia.org/wiki/Impossible_trinity)).

Two amendments to that story:

- **The controls are porous.** Large and variable cross-border flows — trade mis-invoicing, the offshore CNH market, Bond Connect and Stock Connect, corporate FX conversion decisions — mean the constraint binds in practice even though it does not bind de jure ([Euromoney, "Capital controls in China are broken; Beijing faces a new 'impossible trinity'"](https://www.euromoney.com/article/27bjsstsqxhkmh0wsdjj4/foreign-exchange/capital-controls-in-china-are-broken-beijing-faces-a-new-impossible-trinity/)).
- **Rey's dilemma.** Given the scale of the global financial cycle driven by US monetary policy, the trilemma collapses to a *dilemma*: independent monetary policy is available only if capital flows are managed, irrespective of the exchange rate regime ([summarised in Wikipedia, "Impossible trinity"](https://en.wikipedia.org/wiki/Impossible_trinity)). China's answer is to manage flows *and* the rate, which buys autonomy at the cost of periodic episodes in which FX defence overrides domestic liquidity objectives.

**The operational consequence — and this is the central China-specific reason monetary and liquidity conditions diverge.** When CNY is under depreciation pressure and the US–China rate differential is wide, the PBoC has repeatedly kept **onshore liquidity deliberately tight** (and CNH liquidity tighter still, by draining offshore RMB) even while the *stance* was officially easing. Tight liquidity is then an FX-defence instrument, not a monetary-policy signal. Reading DR007 or CNH HIBOR as a stance indicator in such periods is a category error.

The IMF's 2025 Article IV makes the corresponding recommendation: greater exchange rate flexibility would both absorb external shocks and **improve the transmission of monetary policy**, and monetary easing should be part of a package rather than pursued in isolation ([IMF Executive Board concludes 2025 Article IV Consultation with China, 18 February 2026](https://www.imf.org/en/news/articles/2026/02/18/pr-26053-china-imf-executive-board-concludes-2025-article-iv-consultation); [staff report landing page](https://www.imf.org/en/publications/cr/issues/2026/02/17/peoples-republic-of-china-2025-article-iv-consultation-press-release-staff-report-and-574028); [PDF](https://www.imf.org/-/media/files/publications/cr/2026/english/1chnea2026001-source-pdf.pdf); [staff mission conclusion, 10 December 2025](https://www.imf.org/en/news/articles/2025/12/10/pr-25415-china-imf-staff-completes-2025-article-iv-mission-to-the-peoples-republic-of-china)). The IMF also urges communicating a medium-term inflation objective as an anchor — i.e. giving monetary conditions an explicit target, which China currently lacks.

### 4.4 Fiscal deposits at the PBoC (the TSA) as an autonomous liquidity factor

Chinese government deposits are held at the PBoC under the treasury single account arrangement and appear as **政府存款 / 财政存款** on the liability side of the PBoC balance sheet ([MacroMicro, PBoC balance sheet liabilities](https://en.macromicro.me/charts/17672/cn-major-liabilities-of-pboc-balance-sheets); [MacroMicro, PBoC deposits of government](https://en.macromicro.me/series/5821/cn-pboc-deposits-of-government); [INET, "A PBoC balance sheet primer"](https://www.ineteconomics.org/perspectives/blog/a-pboc-balance-sheet-primer)).

Mechanically this is a pure **autonomous factor**: a rise in fiscal deposits drains bank reserves one-for-one and a fall injects them, with no monetary policy decision involved. The China-specific amplification is that the flows are large, lumpy and seasonal:

- **Tax payment months** (January, April, May, July, October) drain reserves sharply. The PBoC's own explanation of the June 2013 crunch cited the concentration of corporate income tax payments.
- **Government bond issuance** — including special CGBs and local government special bonds — drains reserves between the settlement date and the point at which proceeds are actually spent. In an era of very large issuance, the *fiscal issuance calendar has become a first-order driver of interbank liquidity*.
- **Year-end fiscal expenditure** releases a large injection in December.

Fiscal deposits rose by about RMB2.04 trillion in the first eleven months of 2025 ([PBoC Financial Statistics Report, November 2025](https://www.pbc.gov.cn/en/3688247/3688978/3709137/2025122410193371772/index.html)).

**Analytical point:** movements in DR007 driven by the TSA carry *no* information about monetary conditions. Any China liquidity monitor must decompose reserve changes into policy operations vs autonomous factors (currency, fiscal deposits, FX position) before drawing stance inferences — the standard practice at the ECB and Fed, and one that China coverage frequently skips.

### 4.5 Structural / targeted relending (再贷款) and PSL — quasi-fiscal monetary policy

The PBoC operates an extensive menu of **结构性货币政策工具** (structural monetary policy tools), which lend central bank money to banks at subsidised rates conditional on the banks' on-lending to designated sectors ([PBoC, "Introduction to Structural Monetary Policy Instruments"](http://www.pbc.gov.cn/en/3688229/3688335/4738114/5241677/index.html); critical assessment: [Guo, "China's Structural Monetary Policy Tools: Objectives, Limitations, Unintended Consequences," CEP, 2022](https://www.cepweb.org/wp-content/uploads/2022/11/Guo-2022_Structural-Monetary-Policy-Tools-_PBC.pdf); [CEP, "Monetary Policy Reloaded: Towards a New Growth Path in China"](https://www.cepweb.org/monetary-policy-reloaded-towards-a-new-growth-path-in-china/)).

Categories in current use include agricultural and small-business relending (支农/支小再贷款), relending for technological innovation and technical transformation, the carbon emission reduction facility, affordable housing relending, and — since late 2024 — relending for share buybacks and shareholding increases.

**Pledged Supplementary Lending (抵押补充贷款, PSL)** is the largest and most quasi-fiscal. Launched in 2014, it provides medium- to long-term low-cost funds to the three policy banks (CDB, ADBC, CEXIM) for shantytown redevelopment, underground pipe networks, major water conservancy and "going global" projects. It was reactivated in December 2023–January 2024 with an additional RMB500 billion for the "three major projects" (三大工程: affordable housing, urban village redevelopment, dual-use public infrastructure) ([Caixin, January 2024](https://www.caixinglobal.com/2024-01-20/preview-of-the-weekly-the-central-bank-releases-mortgage-supplementary-loans-for-the-third-time-supporting-three-major-projects-with-dual-significance-in-policy-signals-102158781.html); [MacroMicro, PSL balance](https://en.macromicro.me/charts/93846/china-pboc-mortgage-supplementary-loan-balance)).

The September–October 2024 capital-market tools are the same species applied to asset markets: the **Securities, Funds and Insurance companies Swap Facility (SFISF)**, allowing non-banks to swap bonds/ETFs/CSI 300 constituents for central bank-provided high-quality collateral to fund equity purchases (initial scale at least RMB500 billion), and a **RMB300 billion relending facility for share buybacks and shareholding increases**, refinanced by the PBoC at 100% of principal at 1.75% ([Caixin, "Four Things to Know About PBOC's New Swap Facility"](https://www.caixinglobal.com/2024-10-11/three-things-to-know-about-pbocs-new-swap-facility-to-boost-stocks-102243884.html); [People's Daily](https://en.people.cn/n3/2024/1018/c90000-20231167.html); [cbonds, "PBOC Officially Initiates the SFISF Operations"](https://cbonds.com/news/3122631/); [CEP, "China's Monetary Stimulus: Aggregate and Structural Implications"](https://www.cepweb.org/chinas-monetary-stimulus-aggregate-and-structural-implications/)).

**Why this breaks the standard taxonomy.** These instruments simultaneously:
- inject central bank liquidity (sense (a)) — they expand base money;
- alter *funding* conditions for a designated subset of borrowers (sense (b));
- in the SFISF case, directly target *market* liquidity in equities (sense (c));
- and change monetary conditions for target sectors **without changing the policy rate at all** — an interest rate subsidy delivered through the central bank balance sheet.

A rate-and-exchange-rate MCI is structurally blind to all of this. Any credible China monetary conditions measure must include the stock of structural tools outstanding and their subsidy element. The quasi-fiscal character is the substantive critique: these are targeted credit subsidies financed by central bank seigniorage, with the allocation decided administratively — which means "monetary conditions" in China contain a distributional and industrial-policy component absent from DM definitions.

### 4.6 The 2024–2026 framework overhaul

The most consequential set of changes since LPR reform, announced by Governor Pan Gongsheng at the 15th Lujiazui Forum in June 2024 ([BIS Review r240621c](https://www.bis.org/review/r240621c.htm); [PBoC English text](https://www.pbc.gov.cn/en/3688110/3688175/2025080817533718827/index.html); commentary: [Central Banking, "Interpreting the PBoC's slew of policy reforms"](https://www.centralbanking.com/central-banks/monetary-policy/operating-framework/7962151/interpreting-the-pbocs-slew-of-policy-reforms); [BOFIT Weekly 2024/36](https://www.bofit.fi/en/monitoring/weekly/2024/vw202436_1/); [Nomura, "China: A Major Step to Modernizing the PBoC's Policymaking"](https://www.nomuraconnects.com/focused-thinking-posts/china-a-major-step-to-modernizing-the-pbocs-policymaking/); [ING, "What to expect from China's monetary policy framework reforms"](https://think.ing.com/articles/what-to-expect-from-chinas-coming-monetary-policy-framework-reform/); [BBVA Research, "Stocktaking China's new toolkit in its monetary policy framework," June/July 2025](https://www.bbvaresearch.com/en/publicaciones/china-stocktaking-chinas-new-toolkit-in-its-monetary-policy-framework/), [PDF](https://www.bbvaresearch.com/wp-content/uploads/2025/07/202507-Stocktaking-China-new-toolkit-in-its-monetary-policy-framework.pdf)).

**(a) A single short-term policy rate.** The **7-day OMO reverse repo rate (7天期逆回购利率)** is designated as *the* policy rate, with the PBoC controlling only the short end and letting the market determine medium and long rates. The 1-year MLF was demoted; from July 2024 the framework treats the 7-day reverse repo rate as the policy anchor, and the MLF's unified-price bidding was removed, which commentators read as completing the removal of its policy-rate character ([Yicai, "PBOC's MLF No Longer Has Policy-Oriented Role After Removal of Unified Price Bidding System"](https://www.yicaiglobal.com/news/pbocs-mlf-no-longer-has-policy-oriented-role-after-removal-of-unified-price-bidding-system-expert-says)). Current level: **1.40%**, unchanged since the May 2025 cut ([Trading Economics, China reverse repo rate](https://tradingeconomics.com/china/reverse-repo-rate); [CEIC, 7-day reverse repo rate](https://www.ceicdata.com/en/china/open-market-operation-daily/cn-reverse-repurchase-rate-central-bank-7-day)).

**(b) Corridor narrowing — but later than the brief assumes.** This is a correction worth flagging. China has two corridors:
 - The **formal corridor**: ceiling = 7-day SLF rate (常备借贷便利), floor = the interest rate on excess reserves (超额准备金利率). This has historically been extremely wide — a spread of around **245bp** at times, versus 25–50bp in advanced economies — which is precisely why it never constrained anything. The 7-day SLF rate was 2.70% as of July 2024 ([gov.cn, "China cuts interest rates on standing lending facility," 22 July 2024](https://english.www.gov.cn/news/202407/22/content_WS669e08fdc6d0868f4e8e9555.html); [CEIC, SLF 7-day rate](https://www.ceicdata.com/en/china/lending-facility/cn-standing-lending-facility-slf-rate-7-day)). *[The excess reserve rate is, from prior knowledge, 0.35% following an April 2020 cut from 0.72%; one search summary in this session cited 0.72%, which I believe refers to the pre-2020 level. Verify.]*
 - The **de facto corridor**: temporary overnight repo and reverse repo operations (临时正/逆回购), introduced in **July 2024** at **−20bp / +50bp** around the 7-day reverse repo rate — a 70bp band ([Central Banking, "PBoC launches new reverse repo operations"](https://www.centralbanking.com/central-banks/monetary-policy/operating-framework/7962591/pboc-launches-new-reverse-repo-operations); [Finadium](https://finadium.com/pboc-to-add-overnight-reverse-repo-and-rmb-repo-facility/)).
 - The **actual narrowing to ±25bp (a 50bp band)** was announced by Pan at the Lujiazui Forum on **17 June 2026**, alongside making the overnight operations regular rather than temporary, with debut operations on 29–30 June 2026 ([Caixin, "China Tweaks Short-Term Rates to Better Steer Markets," 17 June 2026](https://www.caixinglobal.com/2026-06-17/china-tweaks-short-term-rates-to-better-steer-markets-102455144.html); [Pan Gongsheng, "The evolution of financial structure and the modernization of financial markets in China," BIS Review r260622q](https://www.bis.org/review/r260622q.htm); [Central Banking, "Overnight reverse repos are for managing liquidity, says PBoC"](https://www.centralbanking.com/central-banks/monetary-policy/operating-framework/7976383/overnight-reverse-repos-are-for-managing-liquidity-says-pboc)). **So: intention signalled June 2024, delivered June 2026.** Treat any claim that the corridor was narrowed in 2024 as wrong.

**(c) De-emphasis of quantity targets.** The PBoC has adopted qualitative formulations ("basically in line with nominal economic growth"; "matched to the expected targets for economic growth and the general price level") in place of numerical M2/AFRE growth targets, and has said aggregates should be read with an awareness of their declining information content as the financial structure changes ([Pan, Lujiazui 2024](https://www.bis.org/review/r240621c.htm); [Xinhua, December 2025](https://english.news.cn/20251224/2f8fe826e6a34b5aaa1b833760e225e3/c.html)).

**(d) Secondary-market government bond trading (国债买卖).** The PBoC began trading CGBs in the secondary market in **August 2024**, initially buying short and selling long — a net purchase of about RMB100 billion in August — with the explicit aim of maintaining a steep yield curve and containing risks from concentrated long-duration CGB holdings at city/rural commercial banks and non-banks. Regulators investigated four rural commercial banks for alleged price manipulation ([CNBC/NBC, "China's bond market intervention reveals financial stability worries"](https://www.nbcnewyork.com/news/business/money-report/chinas-bond-market-intervention-reveals-financial-stability-worries/5706806/); [Carnegie, "What Is Driving China's Long-Dated Bonds?" August 2024](https://carnegieendowment.org/posts/2024/08/what-is-driving-chinas-long-dated-bonds?lang=en); [Business Standard, "China's central bank starts trading govt bonds to influence yield curve"](https://www.business-standard.com/world-news/china-s-central-bank-starts-trading-govt-bonds-to-influence-yield-curve-124083000779_1.html)). Purchases were **suspended on 10 January 2025** on grounds of "persistent excess demand" for bonds ([Central Banking, "PBoC suspends government bond purchases"](https://www.centralbanking.com/central-banks/currency/7963600/pboc-suspends-government-bond-purchases)), and **resumed in October 2025** after a nine-month pause with an initial RMB20 billion ([Bloomberg, 27–28 October 2025](https://www.bloomberg.com/news/articles/2025-10-28/pboc-seen-resuming-bond-purchases-as-it-steps-back-into-market); [Caixin, September 2025](https://www.caixinglobal.com/2025-09-09/chinas-central-bank-taps-the-brakes-on-bond-buying-102360733.html)).
This is the sharpest available illustration of the framework's ambiguity: **bond purchases are simultaneously a liquidity operation (sense (a)), a yield-curve / monetary-conditions operation, and a financial-stability intervention in market liquidity (sense (c))** — and the PBoC has used them for all three, sometimes in the same month, buying the short end while selling the long end.

**(e) Outright reverse repo (买断式逆回购).** Added to the toolbox on **28 October 2024**: monthly operations with primary dealers, tenor of no more than one year, conducted on a fixed-quantity, interest-rate-bid, multiple-price basis. It fills the one-month-to-one-year gap in the liquidity toolkit and substitutes for MLF, whose maturities were heavily concentrated — about RMB2.9 trillion maturing in November–December 2024, roughly 40% of the then-outstanding stock. The debut October 2024 operation was RMB500 billion at six months ([gov.cn, "China's central bank introduces new liquidity tool," 28 October 2024](https://english.www.gov.cn/news/202410/28/content_WS671f2a63c6d0868f4e8ec5d2.html); [Xinhua](https://english.news.cn/20241028/3462d35ae57d4e629fc45efee21f61fe/c.html); [Yicai](https://www.yicaiglobal.com/news/chinas-central-bank-introduces-new-monetary-tool-to-manage-liquidity); [Reuters via US News](https://money.usnews.com/investing/news/articles/2024-10-31/chinas-central-bank-conducts-500-billion-yuan-of-outright-reverse-repos-in-october)). Operations have since scaled up substantially — RMB1.1 trillion operations reported in September 2025 and January 2026 ([gov.cn, 30 September 2025](https://english.www.gov.cn/news/202509/30/content_WS68dbdafbc6d00ca5f9a0690b.html); [China Daily, 8 January 2026](https://global.chinadaily.com.cn/a/202601/08/WS695f13bca310d6866eb32a03.html)).
The **crucial technical point**: "outright" (买断式) means title to the collateral passes to the PBoC, unlike pledged repo (质押式) where it is merely encumbered. The dealer can therefore re-use the securities. This is a *collateral-supply* operation as much as a reserve operation — it eases funding liquidity (sense (b)) and bond market liquidity (sense (c)) through a channel that reserve quantities alone do not capture.

**(f) Current stance (as of September 2026).** Policy rate 1.40% (since May 2025), LPR 3.00%/3.50% (since June 2025), weighted-average RRR around 6.2–6.3%, stance officially "moderately loose," with the PBoC signalling remaining room for both RRR and rate cuts. Commentary describes policy as being in an "observation period," leaning on structural tools ([BigGo summary of LPR commentary](https://finance.biggo.com/news/Lnz-rp0Bga3fZL9MG8ny); [China Daily, January 2026](https://global.chinadaily.com.cn/a/202601/15/WS6968a0e8a310d6866eb33f31.html)). *[Rate levels are from secondary aggregators; confirm against PBoC releases.]*

### 4.7 资金空转 ("idle funds") and the 2024 手工补息 crackdown

**资金空转** (*zijin kongzhuan*) — literally "funds spinning in the air" — is the PBoC's term for money that circulates within the financial system generating deposits, financial-institution balance sheet growth and arbitrage profits without financing any real activity. The canonical mechanism in 2023–24: a corporate borrows at a subsidised loan rate and redeposits the proceeds as a structured or interest-supplemented deposit paying more than the loan costs, inflating loans, deposits and M1/M2 with zero real-economy content.

The **手工补息** ban (April 2024, by the 市场利率定价自律机制) removed the deposit leg of that trade. Consequences (Section 3.3): RMB3.92 trillion of deposits lost in April 2024, a ~51% year-on-year fall in Jan–Apr new deposits, M1 growth turning negative, and a migration of corporate money into WMPs and other non-deposit vehicles.

Three analytical consequences we must carry forward:

1. **The 2024 break in the aggregates is definitional, not economic.** M1, M2, loan growth and TSF all fell for reasons unconnected to monetary conditions. Pan's "squeezing water" language is the official acknowledgement ([BIS Review r240621c](https://www.bis.org/review/r240621c.htm); [PBoC, "Highlights of Monetary Policies in the First Three Quarters of 2024"](https://www.pbc.gov.cn/en/3688229/3688353/3688362/2025080817514243079/index.html)).
2. **The migration from deposits to WMPs shifts credit intermediation from the banking system to the NAV-marked asset management system** — which increases the sensitivity of *market* liquidity (sense (c)) to redemption dynamics, as November 2022 demonstrated. Squeezing out 资金空转 improved the honesty of the aggregates while increasing the system's fragility along a different dimension.
3. **Any econometric work spanning 2024 needs a dummy.** Aggregate-based China FCIs estimated through this period will misattribute a regulatory measurement change to a tightening of financial conditions.

### 4.8 The January 2025 M1 redefinition

Announced around **2 December 2024** and effective with the **January 2025** data (published early February 2025, with a back-series from January 2024) ([China Daily, "China broadens M1 money supply measure," 2 December 2024](https://www.chinadaily.com.cn/a/202412/02/WS674db6cda310f1265a1d0a4e.html); [PBoC Financial Statistics Reports](https://www.pbc.gov.cn/en/3688247/3688978/3709137/2025122410193371772/index.html)).

- **Old M1 (狭义货币)** = M0 (currency in circulation) + corporate/institutional demand deposits (单位活期存款).
- **New M1** = M0 + corporate demand deposits + **household demand deposits (个人活期存款)** + **client reserve funds of non-bank payment institutions (非银行支付机构客户备付金)**.

The stated rationale is alignment with the practice of other major economies. The substantive rationale is that the old definition had become badly mismeasured: household demand deposits are, in a mobile-payments economy, fully transactable, and the balances sitting in Alipay/WeChat Pay client reserve accounts are transaction money in everything but statistical classification. The old M1 therefore understated transaction balances and overstated their volatility, and its cyclical signal had degraded ([analysis: "China's M1 Money Supply Surge: A Statistical Adjustment, Not a Liquidity Boom"](https://sagarbaniya.substack.com/p/chinas-m1-money-supply-a-statistical)).

*[Note: I was unable to open the PBoC's original Chinese notice on the revision (完善货币供应量统计口径). The component list above matches multiple secondary reports but should be checked against the PBoC statistical department's notice.]*

**Consequences for us:** (i) the M1 level and growth rate are not comparable across the break other than via the PBoC's own back-series from January 2024; (ii) the widely-used **M1−M2 growth gap** as a proxy for corporate "activity money" changes meaning entirely, because the new M1 now contains a large household component that behaves differently; (iii) note that China's **M2** has always included household savings deposits, so the China M1/M2 pair was never comparable with US or euro area aggregates in the first place.

---

## 5. Practical taxonomy

| # | Concept (EN / 中文) | What it measures | Horizon | Who controls it | Headline China indicator(s) |
|---|---|---|---|---|---|
| 1 | **Monetary conditions** / 货币条件 | Policy stance as transmitted to aggregate demand: price + quantity of money and credit + FX | 2–8 quarters | PBoC jointly with banks, borrowers, fiscal policy, external environment | Real 7-day OMO rate vs estimated r*; weighted average lending rate on new corporate loans (PBoC MPR); TSF/AFRE growth vs nominal GDP; credit impulse; CFETS REER |
| 1a | **Credit conditions** / 信用条件, 宽信用 | Willingness and ability of the real economy to borrow, and of banks to lend | Quarters | Banks + borrowers (PBoC only indirectly, via window guidance) | New RMB loans; TSF ex-government bonds; PBoC bankers/entrepreneurs survey loan demand index; medium-long-term corporate loan share |
| 2 | **Central bank / reserve liquidity** / 银行体系流动性, 基础货币, 宽货币 | Quantity and price of settlement balances | Days–weeks | PBoC, essentially unilaterally, net of autonomous factors | **DR007 vs 7-day OMO rate**; excess reserve ratio (超额准备金率); OMO net injection; outright reverse repo (买断式逆回购) balance; RRR |
| 2a | *Autonomous factors* / 自主性因素 | Non-policy drivers of reserves | Days–weeks | Nobody (MoF, public, FX flows) | Fiscal deposits at PBoC (财政存款); currency in circulation; CGB/LGB issuance and settlement calendar; PBoC FX position (外汇占款) |
| 3 | **Funding liquidity** / 融资流动性 | Ease of an institution raising cash by issuing new obligations | Days–months | Markets + counterparty risk appetite; PBoC only indirectly | **R007 − DR007**; NCD (同业存单) issuance rates by bank tier and issuance success rate; non-bank repo volumes and haircuts; CNH HIBOR for offshore RMB |
| 4 | **Market liquidity** / 市场流动性 | Ease of raising cash by selling assets: tightness, depth, resilience | Intraday–weeks | Dealers, asset managers, market structure | CGB and CDB bond bid-ask spreads; interbank cash bond turnover; on/off-the-run spreads; credit bond turnover ratio; WMP (银行理财) and bond fund net flows/redemptions |
| 5 | **Macro / global liquidity** / 全球流动性 | Ease of financing in global markets = official + private liquidity (BIS/CGFS) | Quarters–years | G4 central banks + global banks + international bond markets | BIS GLIs (FX credit to non-residents); USD credit to Chinese non-bank borrowers; CNH–CNY basis; Bond Connect / Stock Connect net flows; SAFE cross-border flow data |
| 6 | **Financial conditions** / 金融条件 | The superset: 1 + 2 + 3 + 4 + asset prices + risk premia | Quarters | Everyone | China FCIs (GS, sell-side, academic); PBoC's de facto dashboard of AFRE + M2 + weighted average lending rate |

**Reading the table.** Rows 2–4 are all "liquidity." Row 1 is "monetary conditions." Row 6 is the superset. The most common analytical error in China commentary is to take a row 2 indicator (DR007, RRR, OMO injections) and report it as a row 1 conclusion.

---

## 6. Financial conditions indices as the superset — and why China FCIs differ

### 6.1 The FCI concept

An FCI is the MCI generalised: a summary of *all* financial variables that influence future economic activity — policy rate, term structure, credit spreads, equity valuations, exchange rate, house prices, credit quantities, lending standards. It is the superset that nests monetary conditions (row 1) and asset-market/liquidity conditions (rows 2–4).

Two construction methodologies, answering different questions:

- **Weighted-sum / structural:** weights from reduced-form demand equations or identified VARs, calibrated to each variable's cumulative contribution to GDP growth over 3–4 quarters. Goodhart & Hofmann's original FCI is of this type, as is the Goldman Sachs family. Interpretable in growth-impulse units; sensitive to all the MCI critiques of Section 1.4.
- **Factor / principal-component:** extract the common factor from a large panel of financial variables, typically after purging the endogenous response to past economic activity. Hatzius, Hooper, Mishkin, Schoenholtz & Watson is the reference implementation — an unbalanced-panel factor approach over a broad set of quantity and survey indicators as well as prices, giving a series back to 1970 ([NBER WP 16150, 2010](https://www.nber.org/papers/w16150); [PDF](https://www.nber.org/system/files/working_papers/w16150/w16150.pdf); [Princeton copy](https://www.princeton.edu/~mwatson/papers/USMPF-2010.pdf)). The Fed's own FCI-G is a later, more structural variant ([Federal Reserve, "A New Index to Measure U.S. Financial Conditions," FEDS Note, 30 June 2023](https://www.federalreserve.gov/econres/notes/feds-notes/a-new-index-to-measure-us-financial-conditions-20230630.html)). See also [IMF WP 08/161, *A U.S. Financial Conditions Index: Putting Credit Where Credit Is Due*](https://www.imf.org/external/pubs/ft/wp/2008/wp08161.pdf); [ECB WP 1743](https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp1743.en.pdf); [ECB WP 3193, a new FCI for the euro area](https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp3193~9db57822d4.en.pdf); [Federal Reserve, "Assessing and Combining Financial Conditions Indexes," FEDS 2013-39](https://www.federalreserve.gov/pubs/feds/2013/201339/).

**Critical caveat that applies to every FCI:** the index contains variables that are *endogenous to expected growth*. A falling equity market loosens nothing; it forecasts weakness. Unpurged FCIs are therefore partly a restatement of the growth outlook rather than an independent driver of it. This problem is *more* acute in China, where the equity market's correlation with the real economy is weak and where policy explicitly intervenes in asset prices (SFISF, buyback relending), making equity prices a policy *output* rather than a financial *condition*.

### 6.2 Why China FCIs are built differently

**(i) Goldman Sachs's China FCI.** Per the ADB survey, the Goldman construction for China follows Kim et al. (2004, 2007) using a vector error correction model with three domestic factors — the real 3-month interbank rate, the 10-year-less-3-month slope as a yield-curve proxy, and the spread between private borrowing cost and risk-free domestic rates — and two external factors — CDS spreads and the real effective exchange rate; weights come from a VAR exercise computing the cumulative impact on GDP growth after 3–4 quarters ([ADB Economics Working Paper 333, *Financial Conditions Indexes for Asian Economies*](https://www.adb.org/sites/default/files/publication/30163/economics-wp333-financial-conditions-indexes.pdf); [ADB landing page](https://www.adb.org/publications/financial-conditions-indexes-asian-economies)). The general GS FCI methodology weights policy rate, long-term government yields, credit spreads, equity valuations and the trade-weighted exchange rate by estimated GDP contribution. *[This description is from the ADB survey and general GS methodology notes; I could not obtain current, China-specific published weights, and GS has revised its FCI methodology since. Treat the component list as indicative, not current.]*

**(ii) Chinese academic and domestic FCIs add the money aggregate.** The distinguishing feature of the Chinese-language FCI literature is that, alongside the standard interest rate / exchange rate / equity price / house price set, **money supply is included as an index component** — explicitly justified on the grounds that the money aggregate was the intermediate target of Chinese monetary policy. Methods are typically principal components or dynamic factor models; the post-crisis generation uses time-varying-parameter VARs, and finds that time-varying weights outperform fixed weights. The consistent empirical claim is that the FCI leads GDP and CPI better than any single financial variable ([Emerald, "Construction of China's financial conditions index in the post-crisis era," *China Political Economy*](https://www.emerald.com/insight/content/doi/10.1108/CPE-10-2019-0025/full/html); ["Financial Conditions Index's Construction and its Application on Financial Monitoring and Economic Forecasting," ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1877050914004190); ["Construction of China's Financial Condition Index and Analysis," ACM](https://dl.acm.org/doi/pdf/10.1145/3481127.3481173); ["The dynamic impact mechanism of China's financial conditions on real economy," PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10597845/)).

**(iii) The PBoC does not publish an FCI.** It publishes an *aggregate financing view* instead. **社会融资规模 / Aggregate Financing to the Real Economy (AFRE, TSF)** is the broadest official measure of credit supplied by the financial system to non-financial corporates and households, spanning RMB loans, FX loans, entrusted loans, trust loans, undiscounted bankers' acceptances, corporate bonds, government bonds and equity financing — i.e. bank *and* shadow channels ([PBoC AFRE statistics, Chinese](http://www.pbc.gov.cn/diaochatongjisi/116219/116319/5225358/5225359/index.html); [PBoC AFRE stock report, English](http://www.pbc.gov.cn/en/3688247/3688978/3709140/4339074/index.html); [PBoC AFRE stock table PDF](https://www.pbc.gov.cn/eportal/fileDir/diaochatongjisi/resource/cms/2022/04/2022041816440579530.pdf); [MacroMicro, TSF monthly increase](https://en.macromicro.me/charts/8685/cn-total-social-financing)). Data are compiled from the PBoC, the financial and securities regulators, CCDC and NAFMII.

The PBoC's de facto financial-conditions dashboard is therefore a *quantity-led* triplet — AFRE growth, M2 growth, and the weighted-average interest rate on new loans — assessed against the qualitative benchmark of "matching nominal economic growth and the expected price level." This is a philosophically different object from a Western FCI. It is:
- **quantity-weighted rather than price-weighted**, reflecting a bank-dominated, quota-influenced financial system;
- **not benchmarked to a neutral level** — there is no published r* and no numerical inflation target, so "tight" and "loose" have no quantitative referent;
- **not asset-price-inclusive**, since equity and property prices are policy objects.

**(iv) Four reasons why importing a DM FCI to China mis-measures.**
1. **Administered price components.** The LPR is a guided quotation, deposit rates are capped by a self-discipline mechanism, and mortgage rates reprice on administrative schedules. Rate variables are partly policy dummies, not market prices.
2. **Quantity dominance.** With credit allocation influenced by window guidance and structural relending, the *quantity* and *direction* of credit carries information that no price variable captures.
3. **Structural breaks in the inputs.** The 2018 removal of the M2 target, the 2019 LPR reform, the 2024 手工补息 crackdown, and the 2025 M1 redefinition each break the input series. An index estimated across them will attribute definitional changes to conditions.
4. **The exchange rate is a managed, discontinuous variable.** REER moves partly reflect the counter-cyclical management of the fix rather than market pressure, so the FX term in an MCI-style index is not a clean conditions signal.

**Practical recommendation for this project:** do not build a single China FCI. Build **two indices plus a wedge** — a *liquidity conditions index* over rows 2–4 (DR007−OMO spread, R007−DR007, NCD tier spreads, excess reserve ratio, PBoC net injection adjusted for autonomous factors) and a *monetary/credit conditions index* over row 1 (real policy rate vs r*, real weighted-average lending rate, credit impulse, REER) — and treat the **gap between them** as the primary signal. The two-index construction is the direct empirical implementation of the 货币–信用 quadrant framework and preserves exactly the information a single composite destroys.

---

## 7. Operational summary

1. **Never infer stance from DR007.** DR007 versus the 7-day OMO rate is a liquidity gauge; it is driven by fiscal deposits, the bond issuance calendar and FX defence at least as much as by intent.
2. **Always decompose reserve changes** into policy operations versus autonomous factors (fiscal deposits, currency, FX position) before drawing any conclusion.
3. **Run monetary conditions in real terms.** With the GDP deflator and PPI where they have been, the nominal rate path systematically overstates easing.
4. **Watch R007 − DR007 and NCD tier spreads** for the bank/non-bank and large/small bank funding boundaries — these are where China liquidity stress actually appears, not in the headline repo rate.
5. **Treat structural tools as a separate stance dimension.** PSL, relending and the SFISF change monetary conditions for targeted sectors without touching the policy rate.
6. **Dummy out 2024–2025 in any aggregate-based work** (手工补息 ban; M1 redefinition).
7. **Use the 货币–信用 quadrant** as the reporting frame. It is what the domestic market uses, and it encodes the distinction correctly.

---

## 8. Uncertainty register — items to verify against primary sources

Flagged because I could not open any primary document in this session (Section 0).

1. **Excess reserve remuneration rate.** I believe it is 0.35% (cut from 0.72% in April 2020). One search summary cited 0.72%. **Verify against PBoC.**
2. **Current SLF rates and therefore the formal corridor width.** The 2.70% 7-day SLF figure is from July 2024, before subsequent policy rate cuts.
3. **Exact date of the ±25bp corridor narrowing.** My reading is 17 June 2026 (Lujiazui), with operations from 29–30 June 2026, versus a June 2024 statement of intent. The brief assumed 2024. **This should be confirmed — it changes the framework timeline materially.**
4. **Q3 2022 policy rate level.** DR007 at 1.52% is from the PBoC MPR Q3 2022; the contemporaneous 7-day OMO rate (2.00% after the August 2022 cut) is from memory.
5. **Current rate levels** (7-day OMO 1.40%, LPR 3.00%/3.50%, average RRR ~6.2–6.3%) come from secondary aggregators.
6. **The PBoC's original Chinese notice on the M1 redefinition** (完善货币供应量统计口径) — component list not verified against the source.
7. **Month-by-month sequencing of the 2016–18 deleveraging measures.**
8. **Goldman Sachs China FCI current methodology and weights** — the description is from a 2013-vintage ADB survey and may be out of date.
9. **Kyle (1985)** for the tightness/depth/resilience decomposition — cited from standard knowledge, no URL verified.
10. **The June 2026 "OMO to zero"** report is from a single secondary outlet and should be corroborated.

---

## Sources

**Monetary conditions and the MCI tradition**
- Bank of Canada (Freedman), *The role of monetary conditions and the monetary conditions index* — https://www.bankofcanada.ca/wp-content/uploads/2010/06/r954c.pdf
- Freedman, "The Use of Indicators and of the Monetary Conditions Index in Canada," in *Frameworks for Monetary Stability* (IMF) — https://www.elibrary.imf.org/display/book/9781557754196/ch018.xml
- Bank of Canada, archived Monetary Conditions Index page (2006) — https://www.collectionscanada.gc.ca/eppp-archive/100/201/301/bank_can_review/2006/spring/cover/en/rates/mci2.html
- Bank of Canada, Monetary conditions (key variables) — https://www.bankofcanada.ca/rates/indicators/key-variables/monetary-conditions/
- Ericsson, Jansen, Kerbeshian & Nymoen (1998), "Interpreting a Monetary Conditions Index in Economic Policy," BIS Conference Papers Vol. 6 — https://www.bis.org/publ/confp06i.pdf
- BIS Conference Papers Vol. 6, *Topics in Monetary Policy Modelling* (1998) — https://www.bis.org/publ/confp06.pdf
- ResearchGate record, "Interpreting a Monetary Conditions Index in Economic Policy" — https://www.researchgate.net/publication/228560144_Interpreting_a_Monetary_Conditions_Index_in_Economic_Policy
- Ericsson et al. (1996), "Hazards in Implementing a Monetary Conditions Index," Federal Reserve IFDP — https://www.federalreserve.gov/econres/ifdp/hazards-in-implementing-a-monetary-conditions-index.htm
- Stevens (RBA, 1998), "Pitfalls in the Use of Monetary Conditions Indexes" — https://www.rba.gov.au/speeches/1998/sp-ag-160798.html
- RBA Bulletin, August 1998 — https://www.rba.gov.au/publications/bulletin/1998/aug/pdf/bu-0898-2.pdf
- Central Bank of Ireland, "A Discussion of the Monetary Condition Index" — https://www.centralbank.ie/docs/default-source/publications/quarterly-bulletins/quarterly-bulletin-signed-articles/discussion-of-the-monetary-con-index.pdf?sfvrsn=3df6d11d_7
- RBNZ, MCI (B2) — discontinued — https://www.rbnz.govt.nz/statistics/discontinued-statistics/mci-b2
- RBNZ, discontinued statistics hub (MCI) — https://www.rbnz.govt.nz/hub/statistics/discontinued/mci
- McDermott & Williams (2018), "Inflation Targeting in New Zealand: An Experience in Evolution," RBA Conference — https://www.rba.gov.au/publications/confs/2018/mcdermott-williams.html
- NZ Treasury (2001), *Independent Review of the Operation of Monetary Policy in New Zealand* — https://www.treasury.govt.nz/sites/default/files/2007-11/indrevopmonpol.pdf
- Wikipedia, "Monetary conditions index" — https://en.wikipedia.org/wiki/Monetary_conditions_index

**From MCI to FCI**
- Goodhart & Hofmann (2001), "Asset Prices, Financial Conditions, and the Transmission of Monetary Policy," Stanford/FRBSF conference — https://www.frbsf.org/wp-content/uploads/0103conf6.pdf
- FRBSF Economic Letter, "Asset Prices, Exchange Rates, and Monetary Policy" — https://www.frbsf.org/research-and-insights/publications/economic-letter/asset-prices-exchange-rates-and-monetary-policy/
- Goodhart & Hofmann (2002), "Asset Prices and the Conduct of Monetary Policy" — http://repec.org/res2002/Goodhart.pdf
- Hatzius, Hooper, Mishkin, Schoenholtz & Watson (2010), "Financial Conditions Indexes: A Fresh Look after the Financial Crisis," NBER WP 16150 — https://www.nber.org/papers/w16150 ; PDF — https://www.nber.org/system/files/working_papers/w16150/w16150.pdf ; Princeton copy — https://www.princeton.edu/~mwatson/papers/USMPF-2010.pdf
- Federal Reserve, "A New Index to Measure U.S. Financial Conditions" (FCI-G), FEDS Note, 30 June 2023 — https://www.federalreserve.gov/econres/notes/feds-notes/a-new-index-to-measure-us-financial-conditions-20230630.html
- Federal Reserve, "Assessing and Combining Financial Conditions Indexes," FEDS 2013-39 — https://www.federalreserve.gov/pubs/feds/2013/201339/
- IMF WP 08/161, *A U.S. Financial Conditions Index* — https://www.imf.org/external/pubs/ft/wp/2008/wp08161.pdf
- ECB WP 1743, *Measuring Financial Conditions* — https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp1743.en.pdf
- ECB WP 3193, a new Financial Conditions Index for the euro area — https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp3193~9db57822d4.en.pdf
- ADB Economics WP 333, *Financial Conditions Indexes for Asian Economies* — https://www.adb.org/sites/default/files/publication/30163/economics-wp333-financial-conditions-indexes.pdf ; landing page — https://www.adb.org/publications/financial-conditions-indexes-asian-economies

**Liquidity concepts**
- Brunnermeier & Pedersen (2009), "Market Liquidity and Funding Liquidity," *RFS* 22(6) — https://academic.oup.com/rfs/article-abstract/22/6/2201/1592184 ; NBER WP 12939 — https://www.nber.org/papers/w12939
- CGFS Papers No. 45 (2011), *Global liquidity — concept, measurement and policy implications* — https://www.bis.org/publ/cgfs45.htm ; PDF — https://www.bis.org/publ/cgfs45.pdf ; press release — https://www.bis.org/press/p111113.htm
- BIS, "About global liquidity indicators" — https://www.bis.org/statistics/dataportal/gli.htm
- BIS data glossary, "Global liquidity" — https://data.bis.org/help/glossary?item=Global+liquidity
- BIS, GLI methodology — https://www.bis.org/statistics/gli/gli_methodology.pdf
- BIS Quarterly Review (March 2015), "Global liquidity indicators: background and interpretation" — https://www.bis.org/publ/qtrpdf/r_qt1503u.htm
- BIS, Global liquidity indicators at end-June 2025 — https://www.bis.org/statistics/gli2510.htm
- BIS Working Paper 402, *Understanding Global Liquidity* — https://www.bis.org/publ/work402.pdf
- IMF (2013), *Global Liquidity — Credit and Funding Indicators* — https://www.imf.org/external/np/pp/eng/2013/071613b.pdf
- ECB Monthly Bulletin (Oct 2012), global liquidity — https://www.ecb.europa.eu/pub/pdf/other/art1_mb201210en_pp55-68en.pdf
- ECB Financial Stability Review (Dec 2011), global liquidity — https://www.ecb.europa.eu/pub/pdf/fsr/art/ecb.fsrart201112_03.en.pdf

**China: framework, rates, plumbing**
- Pan Gongsheng, 15th Lujiazui Forum keynote, June 2024 (BIS Review r240621c) — https://www.bis.org/review/r240621c.htm ; PBoC English text — https://www.pbc.gov.cn/en/3688110/3688175/2025080817533718827/index.html
- Pan Gongsheng, "The evolution of financial structure and the modernization of financial markets in China" (BIS Review r260622q, June 2026) — https://www.bis.org/review/r260622q.htm
- Caixin, "China Tweaks Short-Term Rates to Better Steer Markets," 17 June 2026 — https://www.caixinglobal.com/2026-06-17/china-tweaks-short-term-rates-to-better-steer-markets-102455144.html
- Central Banking, "Interpreting the PBoC's slew of policy reforms" — https://www.centralbanking.com/central-banks/monetary-policy/operating-framework/7962151/interpreting-the-pbocs-slew-of-policy-reforms
- Central Banking, "PBoC launches new reverse repo operations" — https://www.centralbanking.com/central-banks/monetary-policy/operating-framework/7962591/pboc-launches-new-reverse-repo-operations
- Central Banking, "Overnight reverse repos are for managing liquidity, says PBoC" — https://www.centralbanking.com/central-banks/monetary-policy/operating-framework/7976383/pboc-overnight-reverse-repos-are-for-managing-liquidity-says-pboc
- Finadium, "PBOC to add overnight reverse repo and RMB repo facility" — https://finadium.com/pboc-to-add-overnight-reverse-repo-and-rmb-repo-facility/
- BOFIT Weekly 2024/36, "China's central bank overhauls monetary policy operating framework and starts trading in government bonds" — https://www.bofit.fi/en/monitoring/weekly/2024/vw202436_1/
- Nomura, "China: A Major Step to Modernizing the PBoC's Policymaking" — https://www.nomuraconnects.com/focused-thinking-posts/china-a-major-step-to-modernizing-the-pbocs-policymaking/
- ING, "What to expect from China's monetary policy framework reforms" — https://think.ing.com/articles/what-to-expect-from-chinas-coming-monetary-policy-framework-reform/
- BBVA Research, "Stocktaking China's new toolkit in its monetary policy framework" (2025) — https://www.bbvaresearch.com/en/publicaciones/china-stocktaking-chinas-new-toolkit-in-its-monetary-policy-framework/ ; PDF — https://www.bbvaresearch.com/wp-content/uploads/2025/07/202507-Stocktaking-China-new-toolkit-in-its-monetary-policy-framework.pdf
- RBA Bulletin (April 2024), "China's Monetary Policy Framework and Financial Market Transmission" — https://www.rba.gov.au/publications/bulletin/2024/apr/chinas-monetary-policy-framework-and-financial-market-transmission.html
- Yi Gang, "China's monetary policy framework" (BIS Review, 2019) — https://www.bis.org/review/r190130b.htm
- Kim & Chen, "From a Quantity to an Interest Rate-Based Framework" (Atlanta Fed, 2019) — https://www.atlantafed.org/-/media/documents/news/conferences/2019/0919-workshop-on-chinas-economy/papers/kim-chen_from-a-quantity-to-an-interest-rate-based-framework.pdf
- IMF WP 18/244, *China's Monetary Policy Communication* — https://www.imf.org/-/media/Files/Publications/WP/2018/wp18244.ashx
- MacroMicro, China interest rate corridor — https://en.macromicro.me/collections/31/cn-finance-relative/109608/cn-interest-rate-corridor-new ; https://en.macromicro.me/charts/15742/cn-interest-rate-corridor
- Keynes Watch, "China's Interest Rate Corridor: FDR007, SHIBOR, SLF, IOER & OMO" — https://keyneswatch.com/cn/shibor
- gov.cn, "China cuts interest rates on standing lending facility," 22 July 2024 — https://english.www.gov.cn/news/202407/22/content_WS669e08fdc6d0868f4e8e9555.html
- CEIC, China SLF 7-day rate — https://www.ceicdata.com/en/china/lending-facility/cn-standing-lending-facility-slf-rate-7-day
- CEIC, China 7-day reverse repo rate — https://www.ceicdata.com/en/china/open-market-operation-daily/cn-reverse-repurchase-rate-central-bank-7-day
- Trading Economics, China reverse repo rate — https://tradingeconomics.com/china/reverse-repo-rate
- PBoC, Required Reserves — https://www.pbc.gov.cn/en/3688229/3688335/3730270/index.html
- CEIC, China Reserve Requirement Ratio — https://www.ceicdata.com/en/indicator/china/reserve-requirement-ratio

**China: 2024–26 tools and operations**
- gov.cn, "China's central bank introduces new liquidity tool" (outright reverse repo), 28 October 2024 — https://english.www.gov.cn/news/202410/28/content_WS671f2a63c6d0868f4e8ec5d2.html
- Xinhua, "China Focus: China's central bank introduces new liquidity tool" — https://english.news.cn/20241028/3462d35ae57d4e629fc45efee21f61fe/c.html
- Yicai, "China's Central Bank Adds New Monetary Tool: Outright Reverse Repos" — https://www.yicaiglobal.com/news/chinas-central-bank-introduces-new-monetary-tool-to-manage-liquidity
- Reuters via US News, "China's Central Bank Injects Cash Via New Outright Reverse Repos in October" — https://money.usnews.com/investing/news/articles/2024-10-31/chinas-central-bank-conducts-500-billion-yuan-of-outright-reverse-repos-in-october
- gov.cn, "China to conduct 1.1-trillion-yuan outright reverse repo operation," 30 September 2025 — https://english.www.gov.cn/news/202509/30/content_WS68dbdafbc6d00ca5f9a0690b.html
- China Daily, "China's central bank to conduct 1.1t yuan outright reverse repo operation," 8 January 2026 — https://global.chinadaily.com.cn/a/202601/08/WS695f13bca310d6866eb32a03.html
- Yicai, "PBOC's MLF No Longer Has Policy-Oriented Role After Removal of Unified Price Bidding System" — https://www.yicaiglobal.com/news/pbocs-mlf-no-longer-has-policy-oriented-role-after-removal-of-unified-price-bidding-system-expert-says
- Central Banking, "PBoC suspends government bond purchases" — https://www.centralbanking.com/central-banks/currency/7963600/pboc-suspends-government-bond-purchases
- Bloomberg, "PBOC Seen Resuming Bond Purchases as It Steps Back Into Market," 28 October 2025 — https://www.bloomberg.com/news/articles/2025-10-28/pboc-seen-resuming-bond-purchases-as-it-steps-back-into-market
- Caixin, "China's Central Bank Taps the Brakes on Bond Buying," 9 September 2025 — https://www.caixinglobal.com/2025-09-09/chinas-central-bank-taps-the-brakes-on-bond-buying-102360733.html
- Carnegie Endowment, "What Is Driving China's Long-Dated Bonds?" August 2024 — https://carnegieendowment.org/posts/2024/08/what-is-driving-chinas-long-dated-bonds?lang=en
- CNBC/NBC, "China's bond market intervention reveals financial stability worries" — https://www.nbcnewyork.com/news/business/money-report/chinas-bond-market-intervention-reveals-financial-stability-worries/5706806/
- Business Standard, "China's central bank starts trading govt bonds to influence yield curve" — https://www.business-standard.com/world-news/china-s-central-bank-starts-trading-govt-bonds-to-influence-yield-curve-124083000779_1.html
- Caixin, "Four Things to Know About PBOC's New Swap Facility to Boost Stocks" — https://www.caixinglobal.com/2024-10-11/three-things-to-know-about-pbocs-new-swap-facility-to-boost-stocks-102243884.html
- cbonds, "PBOC Officially Initiates the SFISF Operations" — https://cbonds.com/news/3122631/
- People's Daily, "China's central bank launches re-lending facility and swap program" — https://en.people.cn/n3/2024/1018/c90000-20231167.html

**China: structural tools, PSL, window guidance**
- PBoC, "Introduction to Structural Monetary Policy Instruments" — http://www.pbc.gov.cn/en/3688229/3688335/4738114/5241677/index.html
- Guo (2022), "China's Structural Monetary Policy Tools: Objectives, Limitations, Unintended Consequences," CEP — https://www.cepweb.org/wp-content/uploads/2022/11/Guo-2022_Structural-Monetary-Policy-Tools-_PBC.pdf
- CEP, "Monetary Policy Reloaded: Towards a New Growth Path in China" — https://www.cepweb.org/monetary-policy-reloaded-towards-a-new-growth-path-in-china/
- CEP, "China's Monetary Stimulus: Aggregate and Structural Implications" — https://www.cepweb.org/chinas-monetary-stimulus-aggregate-and-structural-implications/
- Caixin, "The Central Bank Reactivates Pledged Supplementary Lending With Additional 500 Billion Yuan," January 2024 — https://www.caixinglobal.com/2024-01-20/preview-of-the-weekly-the-central-bank-releases-mortgage-supplementary-loans-for-the-third-time-supporting-three-major-projects-with-dual-significance-in-policy-signals-102158781.html
- MacroMicro, PBoC PSL balance — https://en.macromicro.me/charts/93846/china-pboc-mortgage-supplementary-loan-balance
- Wikipedia, "Window guidance" — https://en.wikipedia.org/wiki/Window_guidance ; Grokipedia — https://grokipedia.com/page/Window_guidance
- China Policy, "Beijing swaps credit quotas for market rules" — https://chinapolicy.substack.com/p/beijing-swaps-credit-quotas-for-market
- Capital Economics, "PBOC window guidance, census data gems" — https://www.capitaleconomics.com/clients/publications/china-economics/china-economics-weekly/pboc-window-guidance-census-data-gems
- Reuters via US News, "PBOC Tells Chinese Banks to Boost May Lending as Credit Weakness Persists," 28 May 2026 — https://money.usnews.com/investing/news/articles/2026-05-28/exclusive-pboc-tells-chinese-banks-to-boost-may-lending-as-credit-weakness-persists-sources-say

**China: LPR and interest rate liberalisation**
- CNBC, "China PBOC announcement is basically a rate cut: analysts," 17 August 2019 — https://www.cnbc.com/2019/08/17/pboc-unveils-rate-reform-to-lower-borrowing-cost-for--chinese-firms.html
- RBA, "Recent Reforms to Lending Rates in China," SMP Box A, November 2019 — https://www.rba.gov.au/publications/smp/2019/nov/pdf/box-a-recent-reforms-to-lending-rates-in-china.pdf
- gov.cn, "Central bank: China's LPR reform yields fruitful results" — https://english.www.gov.cn/statecouncil/ministries/202006/01/content_WS5ed4f106c6d0b3f0e9499398.html
- Pekingnology, "Central bank reports its progress of interest rate liberalization since 2017" — https://www.pekingnology.com/p/central-bank-reports-its-progress
- BigGo Finance, China LPR fixings summary (August 2026) — https://finance.biggo.com/news/448d1250-6cdf-4651-b95a-6c85fe5fda9e
- BigGo Finance, "China's LPR Holds Steady... Monetary Policy Enters 'Observation Period'" — https://finance.biggo.com/news/Lnz-rp0Bga3fZL9MG8ny

**China: aggregates, M1 revision, idle funds**
- China Daily, "China broadens M1 money supply measure," 2 December 2024 — https://www.chinadaily.com.cn/a/202412/02/WS674db6cda310f1265a1d0a4e.html
- PBoC, Financial Statistics Report (November 2025) — https://www.pbc.gov.cn/en/3688247/3688978/3709137/2025122410193371772/index.html
- "China's M1 Money Supply Surge: A Statistical Adjustment, Not a Liquidity Boom" — https://sagarbaniya.substack.com/p/chinas-m1-money-supply-a-statistical
- Caixin, "Whither M2? Money Supply Target Falls Out of Favor," March 2019 — https://www.caixinglobal.com/2019-03-05/whither-m2-money-supply-target-falls-out-of-favor-101388006.html
- PBoC, Aggregate Financing to the Real Economy (Chinese) — http://www.pbc.gov.cn/diaochatongjisi/116219/116319/5225358/5225359/index.html
- PBoC, Report on Aggregate Financing to the Real Economy (English) — http://www.pbc.gov.cn/en/3688247/3688978/3709140/4339074/index.html
- PBoC, AFRE stock table (PDF) — https://www.pbc.gov.cn/eportal/fileDir/diaochatongjisi/resource/cms/2022/04/2022041816440579530.pdf
- MacroMicro, China Total Social Financing — https://en.macromicro.me/charts/8685/cn-total-social-financing
- China Banking News, "China struggles to boost lending as households deleverage" (手工补息) — https://www.chinabankingnews.com/p/china-struggles-to-boost-lending
- China Banking News, "Chinese bank deposits shrink after PBOC's rate cut" — https://www.chinabankingnews.com/p/chinese-bank-deposits-shrink-after
- Asia Times, "Unleashed bank deposits misused in Chinese economy," May 2024 — https://asiatimes.com/2024/05/unleashed-bank-deposits-misused-in-chinese-economy/
- Yicai, "China Logs Record Low M1, M2 Money Supply Growth in June" — https://www.yicaiglobal.com/news/growth-of-chinas-key-money-supply-indicators-shrink-to-record-low-in-june
- PBoC, "Highlights of Monetary Policies in the First Three Quarters of 2024" — https://www.pbc.gov.cn/en/3688229/3688353/3688362/2025080817514243079/index.html
- PBoC, "Highlights of Monetary Policies in H1 2025" — https://www.pbc.gov.cn/en/3688229/3688353/3688362/5846652/index.html
- PBoC, "Steady Progress in Monetary Policy Framework Transformation" (interview) — https://www.pbc.gov.cn/en/3688006/5876310/5877235/index.html
- The Standard, "China's PBOC shuts liquidity tap for first time in 2 years, nudging idle cash into economy" — https://www.thestandard.com.hk/finance/article/333678/Chinas-PBOC-shuts-liquidity-tap-for-first-time-in-2-years-nudging-idle-cash-into-economy
- Trading Economics, China new bank loans — https://tradingeconomics.com/china/new-bank-loans/news/509549

**China: PBoC Monetary Policy Reports (货币政策执行报告)**
- Q3 2022 (16 November 2022) — https://www.pbc.gov.cn/en/3688229/3688353/3688356/4583781/4773672/2023011810581221413.pdf
- Q1 2024 (10 May 2024) — https://www.pbc.gov.cn/en/3688229/3688353/3688356/5188141/5385741/2024070415211316142.pdf
- Q3 2024 (8 November 2024) — https://www.pbc.gov.cn/en/3688229/3688353/3688356/5188141/5528500/2024120610084889993.pdf
- Q2 2025 (15 August 2025) — https://wuhan.pbc.gov.cn/en/3688229/3688353/3688356/5624504/2025120609594987919/2025091916245444294.pdf
- Q3 2025 (11 November 2025) — https://www.pbc.gov.cn/en/attachDir/2025/12/20251217.pdf

**China: episodes**
- BIS Quarterly Review (Sept 2013), "Interbank volatility in China" — https://www.bis.org/publ/qtrpdf/r_qt1309u.htm
- Wikipedia, "Chinese Banking Liquidity Crisis of 2013" — https://en.wikipedia.org/wiki/Chinese_Banking_Liquidity_Crisis_of_2013
- Bruegel, "Has the Chinese central bank really taken a hard line on liquidity?" — https://www.bruegel.org/blog-post/has-chinese-central-bank-really-taken-hard-line-liquidity
- Rhodium Group, "China's Interbank Squeeze: Understanding the 2013 Drama" — https://rhg.com/research/chinas-interbank-squeeze-understanding-the-2013-drama-and-anticipating-2014/
- arXiv 1811.08949, "The transmission of liquidity shocks via China's segmented money market" — https://arxiv.org/pdf/1811.08949
- CSIS, *Timeline of China's Deleveraging Campaign* — https://features.csis.org/timeline-of-chinas-deleveraging-campaign/
- Rhodium Group, *Grasping Shadows: The Politics of China's Deleveraging Campaign* — https://rhg.com/research/grasping-shadows/ ; CSIS version — https://www.csis.org/analysis/grasping-shadows-politics-chinas-deleveraging-campaign
- SUERF, "Recent developments in Chinese shadow banking" — https://www.suerf.org/wp-content/uploads/2023/11/f_673271cc47c1a4e77f57e239ed4d28a7_1697_suerf.pdf
- Bloomberg via Yahoo Finance, "Chinese Funds Dump Record Amount of Bonds Amid Redemptions" (Nov 2022) — https://finance.yahoo.com/news/chinese-funds-dump-record-amount-075434239.html
- Caixin, "Behind the Massive Sell-Off in Chinese Wealth Management Products" — https://caixinchinawatch.substack.com/p/cx-daily-behind-the-massive-sell
- ScienceDirect, "Investors awaken: Fragility in China's wealth management product market" — https://www.sciencedirect.com/science/article/pii/S0927539826000319
- ScienceDirect, "What drives liquidity in the Chinese credit bond markets?" — https://www.sciencedirect.com/science/article/pii/S2405918824000242
- ScienceDirect, "China's debt market: Evolution, regulation, and global integration" — https://www.sciencedirect.com/science/article/pii/S0927538X25000885

**China: stance, liquidity trap, policy debate**
- Central Banking, "China shifts to 'moderately loose' monetary policy stance" — https://www.centralbanking.com/central-banks/monetary-policy/7963471/china-shifts-to-moderately-loose-monetary-policy-stance
- CNBC, "China vows 'more proactive' fiscal stimulus measures, 'moderately' looser monetary policy," 9 December 2024 — https://www.cnbc.com/2024/12/09/china-vows-more-active-fiscal-stimulus-measures-moderately-looser-monetary-policy-next-year-.html
- APCO, "China's 2024 Central Economic Work Conference: Six Key Takeaways" — https://apcoworldwide.com/blog/chinas-2024-central-economic-work-conference-six-key-takeaways/
- Xinhua, "China's central bank will maintain ample liquidity that aligns with growth, price targets," 24 December 2025 — https://english.news.cn/20251224/2f8fe826e6a34b5aaa1b833760e225e3/c.html ; gov.cn version — https://english.www.gov.cn/news/202512/24/content_WS694bf171c6d00ca5f9a0843e.html
- China Daily, "China still has room for RRR and interest rate cuts, central bank says," 15 January 2026 — https://global.chinadaily.com.cn/a/202601/15/WS6968a0e8a310d6866eb33f31.html
- gov.cn, "China's central bank signals further RRR, interest rate cuts to bolster growth," 22 January 2026 — https://english.www.gov.cn/news/202601/22/content_WS69720cd8c6d00ca5f9a08b8c.html
- SCMP, "China's central bank signals reserve ratio, interest rate cuts in 2026" — https://www.scmp.com/economy/china-economy/article/3339018/chinas-central-bank-signals-reserve-ratio-interest-rate-cuts-2026
- Capital Economics, "Is China caught in a 'liquidity trap'?" — https://www.capitaleconomics.com/clients/publications/china-economics/china-watch/is-china-caught-in-a-liquidity-trap
- China Banking News, "How China hopes to escape a liquidity trap using central bank credit guidance" — https://www.chinabankingnews.com/p/how-china-hopes-to-escape-a-liquidity
- East Is Read, "Miao Yanliang explains China's large monetary injection yet blocked transmission" — https://www.eastisread.com/p/miao-yanliang-explains-chinas-large
- Pekingnology, "Miao Yanliang: how did China's low inflation come about?" — https://www.pekingnology.com/p/miao-yanliang-how-did-chinas-low
- Yaru Investments, "China Liquidity: Ample Money" — https://yaruinvestments.substack.com/p/china-liquidity-ample-money

**China: exchange rate and the trilemma**
- CEPII WP 2011-27, *The Impossible Trinity Revised: An Application to China* — https://www.cepii.fr/PDF_PUB/wp/2011/wp2011-27.pdf
- Sun & Payette, "China and the Impossible Trinity," *Contemporary Chinese Political Economy* — https://icaps.nsysu.edu.tw/var/file/131/1131/img/2375/CCPS2(3)-Sun-Payette.pdf
- Euromoney, "Capital controls in China are broken; Beijing faces a new 'impossible trinity'" — https://www.euromoney.com/article/27bjsstsqxhkmh0wsdjj4/foreign-exchange/capital-controls-in-china-are-broken-beijing-faces-a-new-impossible-trinity/
- Wikipedia, "Impossible trinity" — https://en.wikipedia.org/wiki/Impossible_trinity

**IMF Article IV**
- IMF, "IMF Executive Board Concludes 2025 Article IV Consultation with China," 18 February 2026 — https://www.imf.org/en/news/articles/2026/02/18/pr-26053-china-imf-executive-board-concludes-2025-article-iv-consultation
- IMF, *People's Republic of China: 2025 Article IV Consultation* (staff report landing page) — https://www.imf.org/en/publications/cr/issues/2026/02/17/peoples-republic-of-china-2025-article-iv-consultation-press-release-staff-report-and-574028 ; PDF — https://www.imf.org/-/media/files/publications/cr/2026/english/1chnea2026001-source-pdf.pdf
- IMF, "IMF Staff Completes 2025 Article IV Mission to China," 10 December 2025 — https://www.imf.org/en/news/articles/2025/12/10/pr-25415-china-imf-staff-completes-2025-article-iv-mission-to-the-peoples-republic-of-china
- IMF elibrary record — https://www.elibrary.imf.org/view/journals/002/2026/044/article-A001-en.xml

**China: PBoC balance sheet and fiscal deposits**
- MacroMicro, PBoC balance sheet liabilities — https://en.macromicro.me/charts/17672/cn-major-liabilities-of-pboc-balance-sheets
- MacroMicro, PBoC deposits of government — https://en.macromicro.me/series/5821/cn-pboc-deposits-of-government
- INET, "A PBoC balance sheet primer" — https://www.ineteconomics.org/perspectives/blog/a-pboc-balance-sheet-primer

**China: 货币–信用 framework (Chinese-language)**
- 理清宽货币和宽信用的基本内涵 — https://credit.bjdx.gov.cn/xyxc/detail/81e35e3e5dcf4aa99dccf88938c3973d
- 从宽货币传导到宽信用：三部曲之理论篇 (新浪财经) — https://finance.sina.cn/china/gncj/2019-04-29/detail-ihvhiqax5771553.d.html
- 关于宽货币向宽信用传导的基本逻辑探究 (新浪财经) — https://finance.sina.cn/stock/qz/2022-05-05/detail-imcwiwst5650653.d.html?from=wap
- 寒来暑往，秋收冬藏——「货币-信用框架」深度解析 (36氪) — https://www.36kr.com/p/2125384897560321

**China FCI literature**
- Emerald / *China Political Economy*, "Construction of China's financial conditions index in the post-crisis era" — https://www.emerald.com/insight/content/doi/10.1108/CPE-10-2019-0025/full/html
- ScienceDirect, "Financial Conditions Index's Construction and its Application on Financial Monitoring and Economic Forecasting" — https://www.sciencedirect.com/science/article/pii/S1877050914004190
- ACM, "Construction of China's Financial Condition Index and Analysis" — https://dl.acm.org/doi/pdf/10.1145/3481127.3481173
- PMC, "The dynamic impact mechanism of China's financial conditions on real economy and international crude oil market" — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10597845/

*Uncited but consulted for context: [Atlantis Press, "China's Monetary Policy Framework"](https://www.atlantis-press.com/article/126010689.pdf).*
