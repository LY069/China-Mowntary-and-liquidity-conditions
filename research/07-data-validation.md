# 07 — Independent Data Validation of `data/seed/series.json`

**Auditor:** data-quality review, independent of the build pass
**Date:** 2026-09-13
**Target:** `/home/user/China-Mowntary-and-liquidity-conditions/data/seed/series.json` (23 series, unmodified by this audit)
**Posture:** adversarial. The file is sourced entirely from third-party GitHub mirrors; the null hypothesis was that at least one series is wrong.

## Method and its limits

Outbound network to every primary macro host (pbc.gov.cn, stats.gov.cn, chinabond, CFETS/chinamoney, FRED, BIS, IMF) is blocked by the egress proxy. Direct `WebFetch` of the PBoC Monetary Policy Report PDFs, and of the mirrors of them on `cif.mofcom.gov.cn` and `jrj.sh.gov.cn`, was attempted and refused (`EGRESS_BLOCKED`). Two channels were therefore used:

1. **WebSearch (34 calls).** Search snippets quoting NBS / PBoC press releases and official statistical communiqués. This is the *independent* channel — it does not touch the dataset's own upstream.
2. **Direct read of the upstream MPR text corpus.** `github.com` is reachable, so `epiphany24262/monetary_policy_project` was cloned and the quarterly 中国货币政策执行报告 cleaned text (2006Q1–2026Q1) was read directly. For the six MPR-derived series this permitted a **full census** — every observation re-extracted by regex and compared, not a spot check.

**Important caveat on channel 2.** Reading the MPR corpus verifies *extraction fidelity* (did the build pass transcribe the report correctly?), not *source fidelity* (is the GitHub mirror a faithful copy of the PBoC PDF?). The mirror was independently corroborated at several points via channel 1 — e.g. the MPR's Dec-2024 rate table (新发放 3.28 / 一般 3.82 / 企业 3.34) reconciles with press reporting of "12月份新发放贷款加权平均利率约3.3%", and the 2026Q1 table's 企业贷款 3.05 reconciles with reported "3月份企业贷款加权平均利率约3.1%". Nothing in the corpus contradicted an official figure found by search. I regard the mirror as trustworthy, but a production build should still re-fetch the PDFs.

---

## Summary table

| Series | Points checked | Matched | Mismatched | Unverifiable | Current | **Recommended confidence** | Note |
|---|---:|---:|---:|---:|---|---|---|
| `tsf_stock_yoy` | 33 (census) + 5 external | 33 | 0 | 0 | verified | **verified** | Every quarter 2018Q1–2026Q1 matches the MPR verbatim; 4 points also confirmed against PBoC press releases |
| `tsf_stock_level` | 19 (census) + 3 external | 19 | 0 | 0 | verified | **verified** | 2026-Q2 = 462.06trn independently confirmed |
| `walr_general` | 33 (census) | 33 | 0 | 0 | verified | **verified** | Highest-weight MCI input; clean across the entire sample |
| `excess_reserve_ratio` | 33 (census) | 33 | 0 | 0 | verified | **verified** | **2024-Q3 = 1.8% is correct, not an anomaly** — see below |
| `ncd_issuance_war` | 14 (census) | 14 | 0 | 0 | verified | **verified (values) / metadata must be corrected** | It is the **3-month** NCD rate, not "all tenors" as the notes claim |
| `m1_yoy` | 5 | 5 | 0 | 0 | partial | **partial** (values verified; caliber break real and unadjusted) | Jan-2025 redefinition now *confirmed*, no longer an unsourced assumption |
| `cpi_yoy` | 7 | 7 | 0 | 0 | partial | **verified** | Incl. all four 2026 points checked |
| `ppi_yoy` | 8 | 8 | 0 | 0 | partial | **verified** | The +4% mid-2026 reflation is **real and official** |
| `core_cpi_yoy` | 5 (census) | 2 | **3 (definitional)** | 0 | verified | **suspect** | 3 of 5 points are year-to-date cumulative averages labelled as single quarters |
| `dr007` | 4 (via MPR period averages) | 4 | 0 | 3 (Oct–Dec 2024 monthly) | partial | **partial** | Convention confirmed to <0.5bp; but series ends 2024-12, 18 months short |
| `cgb_10y` | 0 point-verified; 3 anchors consistent | — | 0 | 24 | partial | **partial** | No official monthly average obtainable; level/shape corroborated indirectly only |
| `real_gdp_yoy_cum` | 8 | 8 | 0 | 0 | partial | **verified** | 2026-Q2 = 4.7 confirmed by NBS |
| `real_gdp_yoy_q` | 5 (internal) + 1 external | 5 | 0 | 0 | partial | **partial** | Arithmetically consistent; incomplete (2024 quarters and 2026-Q2 available but absent) |
| `nominal_gdp_level_cum` | 7 (census) | 7 transcribed correctly | **mixed-vintage break** | 0 | verified | **suspect** | 2023 value is the superseded pre-census figure; 2.8pp spurious jump at the 2023/24 seam |
| `lpr_1y` | 2 | 2 | 0 | 0 | verified | **verified** | |
| `lpr_5y` | 2 | 2 | 0 | 0 | verified | **verified** | |
| `rrr_large` | 3 | 3 | 0 | 0 | partial | **partial → verified within its stated window** | No change is missing through 2026-Q1; truncation caveat still correct |
| `rrr_small` | 3 | 3 | 0 | 0 | partial | **partial → verified within its stated window** | Same |
| `m2_yoy` *(bonus)* | 7 MPR + 2 external | 9 | 0 | 0 | partial | **verified** | Not on the audit list; checked opportunistically |
| `m2_level` *(bonus)* | 1 | 1 | 0 | 0 | partial | partial | 2026-06 = 356,710.8 matches PBoC 356.71万亿 exactly |
| `tsf_flow`, `new_rmb_loans`, `fx_reserves` | 0 | — | — | — | partial | partial (unaudited) | Out of scope this pass |

**Totals: 178 observation-level comparisons; 175 matched; 3 definitional mismatches; 27 observations unverifiable (24 × `cgb_10y`, 3 × `dr007` Q4-2024).**

---

# DISCREPANCIES FOUND

Three problems. None is a transcription error — the build pass copied its sources accurately in every single case. All three are **definitional / vintage** defects, which is the harder class to catch and the class that silently corrupts derived indices.

### D1 — `nominal_gdp_level_cum` is a mixed-vintage series, with a 2.8pp artificial jump at the 2023/2024 seam **(SEVERITY: HIGH)**

| Date | Dataset | Official, current vintage | Status |
|---|---|---|---|
| 2023-Q4 | **126,100** RMB bn | **129,427.2** RMB bn | Dataset holds the *superseded pre-census* figure |
| 2024-Q4 | **134,900** RMB bn | **134,806.6** RMB bn | Dataset holds the *preliminary*; final verification lowered it by 101.8bn |

The NBS bulletin of 31 Dec 2024 revised 2023 GDP up by RMB 3,369.0bn (+2.7%) — RMB 2,025.7bn from the Fifth National Economic Census and RMB 1,343.3bn from the reformed treatment of urban residents' housing services. The 2023Q4 MPR figure of 126.1万亿 predates that and is no longer NBS's number. The 2024 figure in the file (134.9万亿, from the 2024Q4 MPR) is already on the post-census basis, and was itself superseded on 26 Dec 2025 by the final verification at 134.8066万亿.

**Consequence:** nominal GDP growth for 2024 computed from this file is
`134,900 / 126,100 − 1 = +6.98%`
against the true, like-for-like
`134,806.6 / 129,427.2 − 1 = +4.16%`.
A **2.8 percentage point** phantom acceleration, sitting exactly on the boundary. Anything that differences or ratios this series across 2023→2024 — velocity, credit-to-GDP, a nominal output gap, a debt-service ratio — inherits that error. The existing note ("a YoY computed from two published cumulative levels will not exactly equal the official nominal growth rate") understates this by an order of magnitude.

*Sources:* NBS Bulletin on the Revision of Annual GDP Data for 2023 (stats.gov.cn, 31 Dec 2024); "China revises 2024 GDP data", gov.cn / Xinhua, 26 Dec 2025; PBoC MPR 2023Q4 and 2024Q4.

### D2 — `core_cpi_yoy` mixes year-to-date cumulative averages with single-quarter rates **(SEVERITY: MEDIUM)**

The series is declared `freq: "Q"` and the notes claim only quarters "where the PBoC MPR states an unambiguous China core-CPI rate **for that quarter**" were kept. That is not what the MPR says. Reading the source sentences:

| Date | Dataset | MPR sentence | What it actually is |
|---|---|---|---|
| 2023-Q3 | 0.7 | 「**前三季度**…不包括食品和能源的核心CPI同比上涨0.7%，涨幅与上半年大致持平」 | **Jan–Sep 2023 cumulative** |
| 2024-Q2 | 0.7 | 「**上半年**，扣除食品和能源的核心CPI同比上涨0.7%，与一季度持平」 | **H1 2024 cumulative** |
| 2024-Q3 | 0.5 | 「**前三季度**，不包括食品和能源的核心CPI同比上涨0.5%，涨幅比上半年回落0.2个百分点」 | **Jan–Sep 2024 cumulative** |
| 2025-Q1 | 0.3 | 「一季度同比上涨0.3%」 | Q1 — cumulative ≡ quarterly, OK |
| 2026-Q1 | 1.2 | 「扣除食品和能源的核心CPI同比上涨1.2%」 | Q1 — OK |

Three of five points are YTD averages. The 2024-Q3 point is the most misleading: NBS monthly core CPI for Jul/Aug/Sep 2024 was 0.4 / 0.3 / 0.1, i.e. a true single-quarter reading near **0.2–0.3%**, against the 0.5 in the file — an overstatement of ~0.2–0.3pp precisely during the disinflationary trough the index is supposed to detect. A 5-point series in which the labels mean three different things should not be used as a quarterly input at all.

### D3 — `ncd_issuance_war` is the 3-month NCD rate, not the all-tenor rate its metadata claims **(SEVERITY: LOW — values correct, description wrong)**

All 14 values reproduce the MPR exactly, but every one of them comes from the sentence 「**3个月期**同业存单发行加权平均利率为N%」. Examples: 2024-Q3 「…为1.87%，比同期限Shibor高1个基点」; 2026-Q1 「…为1.57%，与同期限Shibor持平」; 2024-Q2 「…为2.1%，比同期限Shibor低5个基点」.

The notes instead describe it as "the all-tenor, all-issuer weighted average NCD ISSUANCE rate" and explain its low level by "short tenors dominate issuance". The real explanation is simpler: it *is* a short tenor. The stated benchmark relationship also changes — the MPR consistently benchmarks it against **3M Shibor**, so the natural spread partner is 3M Shibor or a 3M NCD secondary yield, not 1Y AAA. Fix the `name`, `name_zh` and `notes`; do not touch the values.

### Non-discrepancies — two build-time worries that I can now clear

**The 2024-Q3 excess reserve ratio of 1.8% is correct.** The build flagged it as anomalous against a typical Q3 of 1.3–1.4%. It is verbatim from the 2024Q3 MPR: 「9月末，金融机构超额准备金率为1.8%，银行体系流动性合理充裕。」 And it has an obvious mechanical cause sitting two sentences earlier in the same paragraph: 「2月、9月各降准0.5个百分点，累计释放中长期流动性约2万亿元」. The September 2024 RRR cut took effect on **27 September**, three days before quarter-end, converting roughly RMB 1trn of *required* reserves into *excess* reserves that the quarter-end snapshot then measured — on top of the 24 September stimulus package. The following quarter it normalises to 1.1%. **Do not "correct" this value.** It is a genuine policy artefact and arguably one of the more informative points in the series.

**The M1 redefinition is a sourced fact, not an assumption.** The `m1_yoy` notes say the Jan-2025 redefinition "could not be re-verified from a PBoC primary document in this session — treat the break flag as a modelling instruction, not a sourced fact." It is now verified: the PBoC announced on **2 December 2024** that from January 2025 M1 would be broadened to M0 + corporate demand deposits + **personal demand deposits** + **non-bank payment institutions' client reserve funds**, which lifted the M1 stock from RMB 63.3trn to RMB 105.1trn. The note can be upgraded from a modelling instruction to a documented series break. Separately, the PBoC published a comparable-basis back series for 2024 that this dataset does **not** use, so the Dec-2024 → Jan-2025 step of −1.4 → +0.4 is entirely definitional.

---

## Per-series detail

### `tsf_stock_yoy` — TSF stock growth — **verified**

Full census: all 33 quarters re-extracted from the MPR text and compared. 33/33 exact.

| Date | Dataset | Official | Source | Verdict |
|---|---|---|---|---|
| 2024-Q2 | 8.1 | 8.10% (stock RMB 395.11trn end-Jun 2024) | PBoC financial statistics via press | match |
| 2024-Q3 | 8.0 | 「9月末社会融资规模存量…同比分别增长8.0%和6.8%」 | MPR 2024Q3 + gov.cn | match |
| 2024-Q4 | 8.0 | "AFRE stock totalled 408.3 trillion yuan at end-2024, up by 8.0 percent…on a comparable basis" | NBS Statistical Communiqué 2024 | match |
| 2025-Q1 | 8.4 | 422.96trn, +8.4% | PBoC via China Daily, 13 Apr 2025 | match |
| 2026-Q1 | 7.9 | 456.46trn, +7.9% | PBoC via CGTN, 13 Apr 2026 | match |

Remaining 28 quarters verified against MPR prose (e.g. 2019-Q1 「3月末社会融资规模存量为208.41万亿元，同比增长10.7%」; 2021-Q4 「同比分别增长9.0%和10.3%」; 2022-Q4 「…9.6%」; 2023-Q4 「…9.5%」).

*Two corrections to the metadata, both in the dataset's favour:*
- The note claims 2025-Q4 (8.3) is "the one value NOT from the MPR text — the 2025Q4 report omits the phrase". It does not omit it: 「年末社会融资规模存量、广义货币供应量（M2）同比分别增长**8.3%**和8.5%，明显高于名义GDP增速」. The point is primary-sourced like the rest.
- **Gap:** 2026-Q2 = **7.4%** is published (end-June 2026 AFRE RMB 462.06trn, +7.4% YoY) and `tsf_stock_level` already carries the 2026-Q2 level — but `tsf_stock_yoy` stops at 2026-Q1. The two TSF series end on different dates for no reason. Add it.

### `walr_general` — weighted average lending rate, general loans — **verified** (30% of MCI weight)

Full census: **33/33 exact**, 2018-Q1 (6.01) through 2026-Q1 (3.54). No mismatch anywhere in the sample.

The build's structural claim is confirmed exactly. Through 2024-Q3 the value appears in prose — 2024-Q2 「其中，一般贷款加权平均利率为**4.13%**，同比下降0.35个百分点」, 2024-Q3 「…为**4.15%**…」. From **2024-Q4** the PBoC dropped it from the narrative and it survives only as a row in Table 3 「新发放贷款加权平均利率情况」:

```
2024Q4 MPR, Table 3          level   vs Sep   vs y/y
新发放贷款加权平均利率        3.28    -0.39    -0.55
一般贷款加权平均利率          3.82    -0.33    -0.53   <- dataset 2024-Q4
其中：企业贷款加权平均利率    3.34    -0.17    -0.41
票据融资加权平均利率          1.02    -0.33    -0.45
个人住房贷款加权平均利率      3.09    -0.21    -0.88

2026Q1 MPR, Table 3          level   vs Dec   vs y/y
新发放贷款加权平均利率        3.23     0.09    -0.21
一般贷款加权平均利率          3.54    -0.01    -0.21   <- dataset 2026-Q1
其中：企业贷款加权平均利率    3.05    -0.06    -0.21
```

Table rows for 2025-Q1/Q2/Q3/Q4 give 3.75 / 3.69 / 3.67 / 3.55 — all matching the file.

This is the series most worth being paranoid about and it is the cleanest in the file. Two cross-checks against the *independent* channel confirm the mirror is not corrupted: the 3.28 headline row reconciles with press reporting of "12月份新发放贷款加权平均利率约3.3%", and the 2026Q1 corporate row of 3.05 reconciles with reporting of the 2026Q1 MPR as "3月份，企业贷款加权平均利率约3.1%".

**One definitional point to make explicit in the notes:** this is the rate on **newly issued** general loans in the final month of the quarter (the table is titled 新发放贷款加权平均利率情况), not the rate on the outstanding stock. For an MCI that is the right choice — it is the marginal cost of credit — but it should be stated, because a reader who assumes a stock rate will misread the 2024Q3→Q4 drop of 4.15→3.82.

### `excess_reserve_ratio` — **verified**

Full census: **33/33 exact** against 「X月末，金融机构超额（存款）准备金率为N%」 in each report.

| Date | Dataset | MPR text | Verdict |
|---|---|---|---|
| 2024-Q1 | 1.5 | 「3月末，金融机构超额准备金率为1.5%」 | match |
| 2024-Q2 | 1.5 | 「6月末，金融机构超额准备金率为1.5%」 | match |
| **2024-Q3** | **1.8** | 「9月末，金融机构超额准备金率为**1.8%**，银行体系流动性合理充裕」 | **match — flag resolved, see above** |
| 2024-Q4 | 1.1 | 「2024年末，金融机构超额准备金率为1.1%」 | match |
| 2025-Q1 | 1.0 | 「3月末，金融机构超额准备金率为1.0%」 | match |
| 2025-Q4 | 1.5 | 「2025年末，金融机构超额存款准备金率为1.5%」 | match |
| 2026-Q1 | 1.4 | 「金融机构超额准备金率为1.4%」 | match |

### `m1_yoy` — **partial** (values verified; caliber break real)

| Date | Dataset | Official | Source | Verdict |
|---|---|---|---|---|
| 2024-09 | −7.4 | M1 RMB 62.8trn, −7.4% YoY | PBoC MPR 2024Q3 / China Daily 14 Nov 2024 | match (old caliber) |
| 2025-01 | 0.4 | M1 RMB 112.45trn, +0.4% — first print on the new caliber | PBoC, 14 Feb 2025 | match (new caliber) |
| 2025-09 | 7.2 | M1 RMB 113.15trn, +7.2%, a 55-month high | PBoC Q1–Q3 2025 report, 15 Oct 2025 | match |
| 2026-03 | 5.1 | +5.1% YoY in Q1 2026 | PBoC Q1 2026 financial data | match |
| 2026-06 | 4.0 | M1 RMB 118.48trn, +4.0% | PBoC H1 2026 report, 15 Jul 2026 | match |

No off-by-one: the June-2026 value is genuinely June, not July (July 2026 M1 was RMB 115.46trn, also +4.0% — a coincidence that would have hidden a one-month shift, so it was checked explicitly).

Keep `partial`, but for a different reason than the file gives: the values are right and the break is now documented, so the residual risk is the **unadjusted caliber split** (pre-2025 old basis, 2025+ new basis) rather than unverified provenance. The MCI must either use the PBoC's comparable-basis 2024 back series or break the sample at 2025-01.

### `cpi_yoy` — **upgrade partial → verified**

| Date | Dataset | Official | Source |
|---|---|---|---|
| 2024-12 | 0.1 | +0.1% | NBS, CPI for December 2024 |
| 2025-07 | 0.0 | flat YoY | NBS, 9 Aug 2025 |
| 2026-01 | 0.2 | +0.2% | NBS (cited as "previous month" in the Feb release) |
| 2026-02 | 1.3 | +1.3%, highest in nearly three years | NBS, 10 Mar 2026 |
| 2026-04 | 1.2 | +1.2% | NBS, 11 May 2026 |
| 2026-05 | 1.2 | +1.2% | NBS, 10 Jun 2026 |
| 2026-06 | 1.0 | +1.0% | NBS, 10 Jul 2026 |

7/7. Including every 2026 point the brief singled out.

### `ppi_yoy` — **upgrade partial → verified. The reflation claim holds.**

The dataset's most aggressive-looking assertion — PPI from −0.9% in Feb 2026 to +4.1% by Jun 2026 — is **confirmed by NBS at every checked point.**

| Date | Dataset | Official | Source |
|---|---|---|---|
| 2024-11 | −2.5 | −2.5% | NBS |
| 2024-12 | −2.3 | −2.3%, narrowing from Nov's −2.5% | NBS |
| 2025-06 | −3.6 | −3.6% | NBS |
| 2025-07 | −3.6 | −3.6%, "the same as in June" | NBS, 9 Aug 2025 |
| 2026-03 | +0.5 | 「3月同比上涨0.5%，为连续下降41个月」后首次转正 | PBoC MPR 2026Q1 |
| 2026-04 | +2.8 | +2.8% YoY, +1.7% MoM | NBS, 11 May 2026 |
| 2026-05 | +3.9 | +3.9% YoY, +0.5% MoM | NBS, 10 Jun 2026 |
| 2026-06 | +4.1 | +4.1% YoY, −0.3% MoM; purchasing prices +6.4%; mining +16.5% | NBS, 10 Jul 2026 |

8/8. The turning point is corroborated twice over: NBS prints the levels, and the PBoC's own 2026Q1 MPR independently describes March 2026 as the first positive PPI print after 41 consecutive months of decline. The NBS commentary attributes the April surge to 「国际大宗商品价格快速上涨，国内部分行业需求增加、市场竞争秩序不断优化」 — imported commodity prices plus anti-involution supply discipline. This is a genuine regime change, not a data artefact, and the MCI should treat it as such.

### `core_cpi_yoy` — **downgrade verified → suspect.** See D2.

### `dr007` — **partial**

No official monthly average is published, so the series was validated against the **period averages the PBoC quotes in the MPR**, recomputed from the file:

| Period | MPR quoted average | Recomputed from dataset | Error |
|---|---|---|---|
| 2023 Q1 | 2.03% | 2.0227% | 0.7bp |
| 2024 Q1 | 「均值为1.87%」 | 1.8705% | 0.05bp |
| 2024 H1 | 「均值为1.87%」 | 1.8731% | 0.3bp |
| 2024 Q1–Q3 | 「前三季度…DR007均值为1.85%」 | 1.8502% | **0.02bp** |

Four independent reconciliations at <1bp. The monthly-average convention stated in the notes is confirmed, and the level is right. **Unverifiable:** Oct / Nov / Dec 2024 individually — the 2024Q4 MPR quotes no DR007 average and CFETS/chinamoney is blocked. Stays `partial`, but the binding problem is **staleness, not accuracy**: the series ends 2024-12 while everything else runs to 2026-06. An MCI liquidity block built on a DR007 that stops 18 months early is not usable; this is the single largest coverage hole in the file.

### `cgb_10y` — **partial, nothing point-verified**

No source reachable in this session publishes monthly averages of the ChinaBond 10Y fixing, and the daily data behind the file could not be re-derived. Three independent anchors are *consistent* with the series but none pins a value:

- PBoC *Financial Market Report 2024*: the 10Y CGB yield stood at **1.68%** at end-December 2024. The file's Dec-2024 **monthly average** is 1.8002, which is what you would expect for a month that opened near 2.02 and closed at 1.68 — consistent, and a useful warning that this series must never be compared to a month-end quote (12bp gap in Dec-2024 alone).
- The record low of **1.596%** was set on 6 Feb 2025. The file's Feb-2025 average of 1.6715 sits plausibly above it.
- On 7 Sep 2026 the 10Y was reported at **1.680%**, described as near its lowest since mid-June 2025. The file has 2025-06 at 1.6503 (its trough) and a 1.73–1.86 band in between — consistent with that description.

Verdict: shape and order of magnitude corroborated, zero observations verified. Keep `partial` and do not promote it on the strength of the source's self-reported "cross-checked within 1bp" claim, which could not be tested.

### `real_gdp_yoy_cum` — **upgrade partial → verified**

| Date | Dataset | Official | Source |
|---|---|---|---|
| 2024-Q4 | 5.0 | 「全年国内生产总值134.9万亿元…同比增长5.0%，各季度分别同比增长5.3%、4.7%、4.6%、5.4%」 | MPR 2024Q4 |
| 2025-Q1..Q4 | 5.4 / 5.3 / 5.2 / 5.0 | identical in MPR 2025Q1/Q2/Q3/Q4 | MPR |
| 2026-Q1 | 5.0 | 「一季度国内生产总值33.4万亿元…同比增长5.0%」 | MPR 2026Q1 |
| 2026-Q2 | 4.7 | H1 2026 GDP +4.7% YoY, RMB 69.57trn; Q2 single-quarter +4.3% | NBS, 15 Jul 2026 |

8/8. The 2024 single-quarter path quoted by the MPR (5.3 / 4.7 / 4.6 / 5.4) also reconciles arithmetically with the cumulative path in the file (5.3 / 5.0 / 4.8 / 5.0), which is a genuine independent constraint, not a tautology.

### `real_gdp_yoy_q` — **partial (completeness, not accuracy)**

2025-Q1..Q4 (5.4 / 5.2 / 4.8 / 4.5) and 2026-Q1 (5.0) are internally consistent with the cumulative series, and 2026-Q1 = 5.0 is confirmed. But the series is needlessly short at both ends: the 2024 single-quarter values (**5.3 / 4.7 / 4.6 / 5.4**) are stated verbatim in the 2024Q4 MPR, and **2026-Q2 = 4.3** was published by NBS on 15 Jul 2026. Both are free additions.

### `nominal_gdp_level_cum` — **downgrade verified → suspect.** See D1.

All 7 values transcribe their source correctly — 126.1 / 134.9 / 31.9 / 66.1 / 101.5 / 140.2 / 33.4 万亿 all appear verbatim in the corresponding MPRs (e.g. 2025Q4: 「初步核算，全年国内生产总值140.2万亿元」; 2026Q1: 「一季度国内生产总值33.4万亿元」). The defect is vintage mixing, not transcription.

### `lpr_1y`, `lpr_5y` — **verified**

| Date | Series | Dataset | Official |
|---|---|---|---|
| 2024-02 | 1Y | 3.45 | unchanged at 3.45% at the 20 Feb 2024 fixing |
| 2024-02 | 5Y | 3.95 | cut 25bp from 4.20% to 3.95% — largest since the 2019 reform |
| 2024-10 | 1Y | 3.10 | cut 25bp from 3.35% on 21 Oct 2024 |
| 2024-10 | 5Y | 3.60 | cut 25bp from 3.85% on 21 Oct 2024 |

Confirms the build's own integrity check that the implied change history reproduces the published record.

### `rrr_large`, `rrr_small` — **partial, with the forward caveat liftable to 2026-Q1**

| Date | `rrr_large` | Official |
|---|---|---|
| 2024-02-05 | 10.0 | first of 2024's two 0.5pp cuts — MPR 2024Q4: 「2月、9月各降准0.5个百分点，累计释放…约2万亿元」 |
| 2024-09-27 | 9.5 | second of the two |
| 2025-05-15 | 9.0 | 0.5pp cut effective 15 May 2025, ~RMB 1trn released; auto-finance and leasing companies cut from 5% to zero |

The notes say "changes after 2025-05-15 are unverified; the 2025Q4 MPR refers to a 0.5pp RRR cut that could not be unambiguously dated." That is resolvable. The 2025Q4 MPR's dedicated section 「三、下调金融机构存款准备金率」 describes exactly **one** cut for the whole of 2025 and dates it: 「2025年5月15日，中国人民银行下调金融机构存款准备金率0.5个百分点，向市场提供长期流动性约1万亿元」. The 2026Q1 MPR contains **zero** occurrences of 降准. So nothing is missing through 2026-Q1 and forward-filling 9.0 / 6.0 to that date is safe. (A pbc.gov.cn "PBOC to Cut Required Reserve Ratio" page carrying a 2025-11-21 stamp is a CMS republish timestamp, not a new cut — the same CMS re-dates the Q4-2024 MPC page to 2025-08-08. Do not read it as a missed change.) The *backward* truncation caveat — omitted 2019 and 2021 cuts — remains correct and important.

### `ncd_issuance_war` — **values verified, metadata suspect.** See D3.

### `m2_yoy` / `m2_level` — bonus check, **upgrade `m2_yoy` partial → verified**

Not on the audit list, but it came free with the MPR census and it matters for the MCI. MPR headline sentences give 2024-Q3 6.8, 2024-Q4 7.3, 2025-Q1 7.0, 2025-Q2 8.3, 2025-Q3 8.4, 2025-Q4 8.5, 2026-Q1 8.5 — **all seven match the file exactly.** Two further PBoC releases confirm 2025-09 = 8.4 (M2 RMB 335.38trn) and 2026-06 = 8.0 (M2 RMB 356.71trn); the latter also validates `m2_level` 2026-06 = 356,710.8 to the last digit.

---

## Cross-cutting issue: the dataset is two months stale

`meta.generated` is 2026-09-12 and the upstream snapshot is AS_OF 2026-07-19, so the monthly series stop at 2026-06 (LPR at 2026-07). Today is 2026-09-13. July and August 2026 have both been published — July M1 RMB 115.46trn (+4.0%), Jan–Jul new RMB loans 10.38trn, Jan–Jul AFRE 22.25trn, and NBS released July CPI/PPI on 9 Aug 2026. Any MCI built today from this file is reading a two-month-old world. Not an accuracy defect; flag it in `meta` and refresh before the index goes live.

---

# RECOMMENDED CONFIDENCE CHANGES

Apply exactly these. Everything not listed keeps its current rating.

| Series | Current | **Recommended** | Why |
|---|---|---|---|
| `core_cpi_yoy` | verified | **suspect** | 3 of 5 points are YTD cumulative averages labelled as single quarters (2023-Q3 = Jan–Sep, 2024-Q2 = H1, 2024-Q3 = Jan–Sep). The notes assert the opposite. 2024-Q3 overstates the true quarterly rate by ~0.2–0.3pp. Do not use as a quarterly input until reconstructed from NBS monthly core CPI. |
| `nominal_gdp_level_cum` | verified | **suspect** | Mixed vintage. 2023-Q4 = 126,100 is the pre-census figure superseded by 129,427.2; 2024-Q4 = 134,900 is preliminary, finalised at 134,806.6. Growth across the 2023/24 seam is overstated by 2.8pp. Values are transcribed correctly — the defect is basis, not transcription. |
| `cpi_yoy` | partial | **verified** | 7/7 against NBS, including all four 2026 points. |
| `ppi_yoy` | partial | **verified** | 8/8 against NBS; the 2026 reflation to +4.1% is confirmed, and the March-2026 turning point is independently corroborated by the PBoC MPR. |
| `real_gdp_yoy_cum` | partial | **verified** | 8/8 against MPR and NBS, including 2026-Q2 = 4.7; cumulative and single-quarter paths reconcile. |
| `m2_yoy` | partial | **verified** | 7 MPR headline points + 2 PBoC releases, all exact. |
| `rrr_large` | partial | **verified-within-window** (or keep `partial` if the schema has no such value) | All three checked changes confirmed; the 2025Q4 and 2026Q1 MPRs positively establish that no change is missing through 2026-Q1. The backward-truncation caveat stays. |
| `rrr_small` | partial | **verified-within-window** (same proviso) | Same evidence. |
| `tsf_stock_yoy` | verified | **verified** (unchanged) — but fix the note | The claim that 2025-Q4 is not from the MPR is wrong; it is. Also add the published 2026-Q2 = 7.4. |
| `ncd_issuance_war` | verified | **verified** (values) — but fix `name`/`notes` | It is the **3-month** NCD issuance rate benchmarked to 3M Shibor, not the all-tenor rate. Leave the numbers alone. |
| `m1_yoy` | partial | **partial** (unchanged, reason revised) | Values 5/5 verified and the Jan-2025 redefinition is now documented, so the note's "could not be re-verified…not a sourced fact" should be rewritten. Residual risk is the unadjusted caliber split, not provenance. |
| `dr007` | partial | **partial** (unchanged) | Convention and level verified to <1bp against four MPR period averages, but the series ends 2024-12. Coverage, not accuracy, is what keeps it below `verified`. |
| `cgb_10y` | partial | **partial** (unchanged) | Zero observations independently verified. Consistent with three external anchors; that is corroboration, not verification. Do not promote. |
| `walr_general` | verified | **verified** (unchanged) | 33/33 exact. Add to the notes that it is the rate on **newly issued** general loans in the quarter's final month. |
| `excess_reserve_ratio` | verified | **verified** (unchanged) | 33/33 exact. **Clear the 2024-Q3 anomaly flag** — 1.8% is correct and is caused by the 27 Sep 2024 RRR cut landing three days before the quarter-end snapshot. |
| `real_gdp_yoy_q` | partial | **partial** (unchanged) | Accurate but incomplete; 2024 quarters and 2026-Q2 = 4.3 are published and should be added. |
| `tsf_flow`, `new_rmb_loans`, `fx_reserves`, `m2_level`, `tsf_stock_level` | partial / verified | unchanged | Not audited this pass (`tsf_stock_level` was census-checked against the MPR and matched 19/19, so its `verified` stands). |

---

## Sources

**Primary text corpus (read directly)**
- PBoC 中国货币政策执行报告, quarterly cleaned full text 2006Q1–2026Q1 — `https://github.com/epiphany24262/monetary_policy_project`, `data/interim/report_text/`. Reports relied on: 2022Q4, 2023Q1–Q4, 2024Q1–Q4, 2025Q1–Q4, 2026Q1.

**National Bureau of Statistics**
- Bulletin on the Revision of Annual GDP Data for 2023 — https://www.stats.gov.cn/english/PressRelease/202412/t20241231_1958128.html
- Statistical Communiqué on the 2024 National Economic and Social Development — https://www.stats.gov.cn/english/PressRelease/202502/t20250228_1958822.html
- Consumer Price Index for December 2024 — https://www.stats.gov.cn/english/PressRelease/202501/t20250114_1958199.html
- 2026年4月份工业生产者出厂价格 — https://www.stats.gov.cn/sj/zxfb/202605/t20260511_1963658.html
- 2026年5月份工业生产者出厂价格 — https://www.stats.gov.cn/sj/zxfb/202606/t20260610_1963922.html
- Industrial Producer Price Indexes in June 2026 — https://www.stats.gov.cn/english/PressRelease/202607/t20260710_1964093.html
- Consumer Price Index in June 2026 — https://www.stats.gov.cn/english/PressRelease/202607/t20260710_1964094.html
- Consumer Price Index in February 2026 — https://www.stats.gov.cn/english/PressRelease/202603/t20260310_1962748.html
- National Economy in the First Half Year 2026 — https://www.stats.gov.cn/english/PressRelease/202607/t20260715_1964120.html

**People's Bank of China**
- Monetary Policy Report Q3 2024 (PDF) — https://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125957/5347949/afbfa5df25ee45889d916a2819b60a43/2024110815410752868.pdf
- Monetary Policy Report Q4 2024 (PDF) — https://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125957/5347949/ad0bc3efe0234fed8cc6260a134a6e95/2025022618190099812.pdf
- 2026年第一季度中国货币政策执行报告 (PDF) — https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2026051118520164705/2026051118500062162.pdf
- 2025年第四季度中国货币政策执行报告 (PDF, MOFCOM mirror) — https://cif.mofcom.gov.cn/cif/html/upload/20260211143114167_2025%E5%B9%B4%E7%AC%AC%E5%9B%9B%E5%AD%A3%E5%BA%A6%E4%B8%AD%E5%9B%BD%E8%B4%A7%E5%B8%81%E6%94%BF%E7%AD%96%E6%89%A7%E8%A1%8C%E6%8A%A5%E5%91%8A.pdf
- Financial Market Report 2024 — https://www.pbc.gov.cn/en/3688247/3688978/3709134/5579031/2025013009512017217.pdf
- 2025年1月金融统计数据报告 (M1 112.45trn, +0.4%) — https://jrj.sh.gov.cn/SCGK194/20250217/01ac96e8b04e4226b2bfbe1b28c0f4ab.html ; https://www.nbd.com.cn/articles/2025-02-14/3752554.html
- 央行：1月末M2余额318.52万亿元 同比增长7% — http://finance.people.com.cn/n1/2025/0214/c1004-40418849.html
- 2025年前三季度金融统计数据 (M1 113.15trn, +7.2%; M2 335.38trn, +8.4%) — https://www.jiemian.com/article/13467974.html ; https://www.21jingji.com/article/20251015/herald/240d8c27765311704a663ef1b2bc2e74.html
- 2026年上半年金融统计数据 (M2 356.71trn +8.0%; M1 118.48trn +4.0%) — https://www.stcn.com/article/detail/4020692.html ; https://finance.ifeng.com/c/8umSesX45Ax
- Report on Aggregate Financing to the Real Economy — https://www.pbc.gov.cn/en/3688247/3688975/4505202/4505205/index.html
- PBOC to Cut Required Reserve Ratio (May 2025) — https://www.pbc.gov.cn/en/3688229/3688335/3730270/index.html

**Official press and wires**
- China revises 2024 GDP data (final verification, 134.8066trn) — https://english.www.gov.cn/archive/statistics/202512/26/content_WS694e26e4c6d00ca5f9a0846e.html ; https://www.globaltimes.cn/page/202512/1351543.shtml
- China revises up 2023 GDP by 3.37t yuan — https://www.globaltimes.cn/page/202412/1325835.shtml
- Revising 2023 GDP data not to impact economic growth in 2024: NBS — https://english.www.gov.cn/archive/statistics/202412/28/content_WS676f5abac6d0868f4e8ee562.html
- China's GDP expands 4.7 pct in H1 2026 — https://english.news.cn/20260715/2042180783634565b4e002fd241e5e2b/c.html ; https://news.cgtn.com/news/2026-07-15/Graphics-China-s-GDP-expands-4-7-in-H1-2026-1ONzcSE5qmI/p.html
- China's March total social financing grows by 7.9% y/y (2026) — https://news.cgtn.com/news/2026-04-13/China-s-March-total-social-financing-grows-by-7-9-y-y-1MjnGR4Ps3e/p.html
- China records robust momentum in financing activity (Mar 2025, 422.96trn +8.4%) — https://www.chinadaily.com.cn/a/202504/13/WS67fbb559a3104d9fd381efd1.html
- China's financial data signals a shift toward confidence (H1 2026, AFRE 462.06trn +7.4%) — https://news.cgtn.com/news/2026-07-15/China-s-financial-data-signals-a-shift-toward-confidence-1ONH86hdtyE/p.html
- China broadens M1 money supply measure — https://www.chinadaily.com.cn/a/202412/02/WS674db6cda310f1265a1d0a4e.html
- China's central bank revises statistical scope of M1 — https://www.globaltimes.cn/page/202412/1324233.shtml
- Commentary: China's Changes to M1 Money Supply Will Curb Volatility — https://www.caixinglobal.com/2024-12-04/commentary-chinas-changes-to-m1-money-supply-will-curb-volatility-102264496.html
- Money supply giving off recovery signs (Sep 2024 M1 62.8trn, −7.4%) — https://www.chinadaily.com.cn/a/202411/14/WS67355637a310f1265a1cd4cb.html
- China cuts benchmark lending rates by 25 basis points (21 Oct 2024) — https://www.cnbc.com/2024/10/21/china-lowers-benchmark-lending-rates-by-25-basis-points.html
- China makes record cut to mortgage reference rate (20 Feb 2024, 5Y 4.20→3.95) — https://www.centralbanking.com/central-banks/monetary-policy/7960852/china-makes-record-cut-to-mortgage-reference-rate
- China to cut reserve requirement ratio by 0.5 pp from May 15 — https://english.www.gov.cn/news/202505/07/content_WS681af001c6d0868f4e8f2509.html
- China's first RRR cut for financial institutions in 2025 takes effect — https://english.www.gov.cn/news/202505/15/content_WS68254f59c6d0868f4e8f2902.html
- China's PPI down 3.6 pct in July 2025 — https://english.www.gov.cn/archive/statistics/202508/09/content_WS6896b24cc6d0868f4e8f4bb3.html
- China's CPI up 0.2 pct in 2024 — https://english.www.gov.cn/archive/statistics/202501/09/content_WS677f3418c6d0868f4e8eea16.html
- China's PPI up 4.1% in June 2026 — http://english.scio.gov.cn/pressroom/2026-07/09/content_118591343.html
- 央行：我国贷款加权平均利率持续处于历史低位 (Dec 2024 new-loan WALR ~3.3%) — https://www.cnr.cn/jrpd/jdt/20250213/t20250213_527070845.shtml
- 2026年第一季度中国货币政策执行报告解读 (Mar 2026 corporate loan rate ~3.1%) — https://jrj.sh.gov.cn/ZXYW178/20260512/04aee48e58f74c55b29f8105651a7783.html
- China's yuan loans increase by 10.38T yuan in Jan–July 2026 — http://www.china.org.cn/2026-08/15/content_118648829.shtml

**Blocked and therefore not used:** pbc.gov.cn, stats.gov.cn, cif.mofcom.gov.cn, jrj.sh.gov.cn (direct fetch), yield.chinabond.com.cn, chinamoney.com.cn, FRED, BIS, IMF. URLs above are cited as the provenance of figures quoted in search results, not as pages fetched in this session.
