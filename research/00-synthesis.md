# China's monetary and liquidity conditions
### Lead economist's synthesis

*Prepared 13 September 2026. This note answers the six questions put to the team and points to the
detailed working papers behind each. Read the [provenance warning](#a-warning-about-the-data) before
using any number.*

---

## 1. The two concepts, and why the distinction is the whole point

**Monetary conditions** are the stance of policy *as transmitted to households and firms*: the price of
credit, the quantity of credit, and the exchange rate. Horizon: quarters to years. Object: the real
economy. The question it answers is *is money cheap and available to people who might spend it?*

**Liquidity conditions** are the availability and price of settlement balances and short-term funding
*inside the financial system*. Horizon: days to weeks. Object: banks and non-banks. The question it
answers is *can financial institutions fund themselves, and at what cost relative to the policy rate?*

The words are used interchangeably in market commentary. They should not be. A central bank can drive
repo rates to the floor while credit conditions for a private manufacturer remain punishing, because the
banks receiving those reserves cannot find creditworthy borrowers who want to borrow. **Loose liquidity
with tight money is not a contradiction — it is the signature of impaired transmission**, and detecting
it is the main job of the tracker built alongside this note.

Three features make the gap wider in China than in developed markets: a bank-dominated system in which
property collateral drives credit supply; capital controls that let domestic and external conditions
diverge; and a policy framework that was, until 2024, quantity-based rather than price-based.

One further distinction matters, because "liquidity" carries four separate meanings that are routinely
conflated: central bank reserve liquidity, bank funding liquidity, market liquidity (depth and
bid-ask), and global/macro liquidity. They can move in opposite directions at the same time.

→ Full treatment: [`01-definitions-framework.md`](01-definitions-framework.md)

---

## 2. Key indicators

The full catalogues run to about 40 indicators each, with Chinese names, sources, release lags,
thresholds and failure modes. The headline sets:

**Monetary conditions — the ones that carry the signal**

| Indicator | Why it earns its place |
|---|---|
| Real weighted-average lending rate | The only measure of the true, transacted, inflation-adjusted price of credit. Shows China restrictive while every nominal rate says otherwise. |
| Credit impulse, ideally ex-government bonds | The acceleration of credit — what actually moves activity, 2–3 quarters ahead. |
| TSF stock growth minus nominal GDP growth | The PBoC's own stated benchmark, expressed as a stance variable. |
| 7-day reverse repo rate | The primary policy rate since 2024. The unambiguous statement of intent. |
| Corporate medium & long-term loan growth | The highest-quality credit series: real capex financing, immune to bill-financing quota-stuffing. |
| GDP deflator | The denominator that turns nominal easing into real tightening. |
| M1 and the M1−M2 scissors gap | The corporate animal-spirits read. |
| Weighted-average RRR, and headroom to the ~5% floor | The loudest easing signal, with dwindling room. |
| BIS broad REER | The external leg of the stance. |
| Household time-deposit share | The behavioural read on whether easy money circulates or is hoarded. |

**Liquidity conditions — the ones that carry the signal**

| Indicator | Why it earns its place |
|---|---|
| DR007 minus the 7-day OMO rate | The PBoC's own target variable. The single cleanest gauge of interbank conditions. |
| R007 minus DR007 | Catches non-bank and leverage stress that never touches DR007. The best early warning of a 2022-style unwind. |
| 1y AAA NCD minus the policy rate | The price of marginal bank *term* funding. Replaces the now-dead NCD–MLF spread. |
| Excess reserve ratio | The *stock* of liquidity — how much cushion exists, not what it costs. |
| Net PBoC injection, duration-weighted | The supply side, aggregated across OMO, MLF, outright reverse repo, PSL and bond purchases. |
| Overnight share of repo turnover | The crowded-carry gauge. Above ~88% the system is one bad funding day from a forced unwind. |
| Fiscal deposits at the PBoC | The largest China-specific autonomous drain. |
| Net government bond settlement | The only genuinely forward-looking item — a supply calendar you can build four weeks ahead. |
| 10y CGB minus the policy rate | How little cushion leveraged carry has. |
| Overnight CNH HIBOR | The offshore liquidity and FX-defence gauge — independent information from onshore. |

A deliberate omission: SHIBOR overnight and 1-week are quoted, not transacted, and are strictly
dominated by DR001/DR007.

→ Full catalogues: [`02-monetary-indicators.md`](02-monetary-indicators.md) ·
[`03-liquidity-indicators.md`](03-liquidity-indicators.md)

---

## 3. What has changed in how these conditions are measured

The 2024–26 PBoC framework overhaul has made several long-standing indicators misleading and promoted
others. The practical consequences for anyone building a monitor:

- **The 7-day reverse repo rate is now the single primary policy rate.** Reading an MLF move as a
  stance change is a category error.
- **The MLF has been demoted to a liquidity tool**, and from March 2025 is priced by multi-price
  bidding — so there is no single announced MLF rate any more. The conventional **NCD−MLF spread is
  therefore dead** and must be replaced by NCD versus the policy rate. (This build does exactly that.)
- **Quantity targets for M2 and TSF have been de-emphasised**, so a miss versus nominal GDP growth no
  longer mechanically triggers action.
- **M1 was redefined in January 2025**, adding household demand deposits and non-bank payment
  institutions' client reserves. Pre- and post-2025 M1 are different aggregates. The 2024 crackdown on
  manual interest supplementation (手工补息) separately distorted 2024 readings. Any M1 z-score spanning
  those breaks is meaningless.
- **New instruments changed where base money comes from**: outright reverse repo (October 2024) and
  secondary-market government bond trading (August 2024). With the RRR near its floor, aggregate net
  injection matters more than any single instrument.
- **The operating target has moved from the 7-day to the overnight tenor.** The Q1 2026 Monetary
  Policy Report designates **DR001** as the core money-market anchor, and the June 2026 corridor
  narrowing (to ±25bp, 50bp wide, from 70bp) formalised a band around it. **DR007 minus OMO — the
  workhorse China liquidity spread for a decade — is being demoted in favour of DR001 minus OMO.**
  Because that band is explicit and narrow, a breach is now genuinely informative rather than noise.
  Track both; weight DR001 from 2026.
- **A multi-benchmark loan pricing system referencing sovereign yields is being floated**, which would
  strip the LPR of most of its remaining value as a conditions indicator. Worth watching closely.
- **The right deflator is now contested and consequential** — see the next section.

The single highest-value new indicator to construct is a **swap-adjusted TSF**. The roughly RMB 10trn
LGFV hidden-debt swap injects refinancing that creates no new spending power while inflating measured
credit, and it will overstate apparent stimulus for years. No official adjusted series exists.

→ Literature scan and the full 23-row new-indicator table: [`04-recent-research.md`](04-recent-research.md)

---

## 4. Time series

Roughly 37 series are assembled and charted in the tracker, most running 2015–2026, with derived
spreads, real rates, the credit impulse and two composite indices computed from them. Coverage,
frequency and confidence are declared per series inside the app.

→ Sourcing manual and retrieval routes: [`05-data-sources.md`](05-data-sources.md)

---

## 5. Implications for growth, inflation and policy

Every indicator carries a transmission mechanism, a lead/lag, threshold heuristics, its effect on the
PBoC's reaction function, and — most usefully — its **failure modes**, documented in the implications
note and surfaced in the app under "where it misleads". The recurring China-specific traps:

- TSF inflated by government bond issuance rather than private credit demand.
- Loan growth flattered by bill financing at quarter-ends.
- A falling 10-year CGB yield read as easy policy when it is the market pricing a worse nominal path.
- A low DR007 read as aggressive easing when it reflects absent credit demand.
- Level series (M2 stock) and seasonal flows (monthly TSF) z-scored as if they were conditions.

### The call, as of September 2026

**The standard China note is out of date, and the half that changed is the half most desks have not
updated.** The 2023–25 framing — nominal easing, deflation, rising real rates, broken transmission —
is now only half right.

What changed: the **GDP deflator turned positive in Q2 2026** after twelve consecutive negative
quarters; **PPI reflated hard** to around +4% year-on-year; and the **FX constraint inverted**, with
the renminbi through 7.00 and the PBoC showing little resistance to appreciation.

What did not change, and in places got worse: **credit growth is the weakest on record**, carried by
government bonds while private lending decelerates; **property investment is still contracting at a
double-digit rate**; growth is slowing; and the **LPR has been frozen for more than ten months**.

The arithmetic that reframes everything: the same 3.00% one-year LPR is simultaneously **negative in
real terms for industry** (PPI-deflated), **mildly restrictive economy-wide** (GDP-deflator), and
**clearly restrictive for households** (CPI-deflated) — a spread of roughly 300 basis points across
deflators. China has delivered several hundred basis points of real easing to its industrial sector
without moving the policy rate at all, and it did so with a *supply-side administrative* instrument —
the "anti-involution" (反内卷) capacity campaign — not a monetary one.

**The strategic implication: anyone still running "China must ease because of deflation" is fighting
the last war.** The live configuration is prices reflating from the supply side while demand
decelerates — a mildly stagflationary mix that *weakens* the internal case for a cut precisely when
growth needs one. The PBoC's easing trigger has moved from PPI to **core CPI and the labour market**.

This is a judgement call built on the team's sourced evidence, not a mechanical output of the
indices — and it is exactly the kind of call the tracker exists to let you re-examine as the data moves.

→ Full transmission analysis, read-across matrix, scenario map and monitoring playbook:
[`06-implications.md`](06-implications.md)

---

## 6. The tracker

An interactive web app monitoring the indicator set, with a Monetary Conditions Index, a Liquidity
Conditions Index and the transmission gap between them, plus per-indicator detail, the read-across
matrix and full method documentation. See the [repository README](../README.md) to run it.

---

## A warning about the data

The dataset was assembled inside a sandbox whose egress policy blocked **every** macroeconomic data
host, so fetched values came from third-party mirrors rather than primary publishers. A scheduled
GitHub Actions workflow now closes that gap by pulling from the publishers' own endpoints on a runner
with unrestricted network; until it has run, treat the committed values as mirror-sourced.

They are not, however, unchecked. An independent audit made 178 observation-level comparisons against
PBoC and NBS sources; 175 matched ([`07-data-validation.md`](07-data-validation.md)). The six Monetary
Policy Report series were audited by full census — `walr_general`, which carries 30% of the monetary
index, matched 33/33. Two series failed and are flagged `suspect` in the app, shown with the problem
stated and no loose/tight reading: `nominal_gdp_level_cum` mixes pre- and post-census GDP vintages, and
`core_cpi_yoy` mislabels year-to-date averages as single quarters.

The two policy-rate series entered by hand have since been corroborated against an independent Wind
export: 12/12 overlapping OMO change dates and 14/14 MLF dates agree exactly.

A caution that generalises beyond this project: the second sourcing pass found a repository shipping
**synthetic "demo" data** dressed as a real DR007 history — 221 of 230 days wrong by up to 58 basis
points. It was caught by diffing against an independent source before anything was merged. Mirror data
is worth having; it is not worth trusting without a second opinion.

38 of 59 defined indicators carry data. The remainder are defined and documented, and the app names
each one and what its absence costs rather than averaging over the hole.
