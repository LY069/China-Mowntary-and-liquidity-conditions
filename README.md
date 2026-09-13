# China Monetary & Liquidity Conditions

A research pack and interactive tracker separating two things that market commentary routinely
conflates: **monetary conditions** (the policy stance as transmitted to the real economy, over
quarters) and **liquidity conditions** (the availability and price of short-term funding inside the
financial system, over days). In China the two come apart more than almost anywhere else, and telling
them apart is the point of this repository.

**→ Start with the [lead economist's synthesis](research/00-synthesis.md).**

---

## The tracker

An interactive dashboard covering 59 indicators (38 populated), with a Monetary Conditions Index, a Liquidity
Conditions Index and the transmission gap between them.

```bash
python3 scripts/build_app_data.py     # merge data, compute derived series + composites
python3 scripts/make_standalone.py    # emit a single-file page
open docs/index.html
```

`docs/index.html` is self-contained and needs no server. Every indicator opens a panel with its time
series, its transmission mechanism, its implications for growth, inflation and policy, its sources and
confidence rating, and — most usefully — the ways it misleads.

Two design decisions worth knowing:

- **Positive always means looser.** Every series is signed by whether a rise loosens or tightens, then
  banded against its own history, so a row reads the same way regardless of the underlying convention.
- **The tool refuses readings it cannot justify.** Trending level series (M2 stock) and seasonal flows
  (monthly TSF) get no loose/tight label, because a z-score on a rising level always reads "loose" and
  says nothing. Composite months resting on stale quarterly inputs are flagged as such rather than
  presented as live.

## Research

| Note | What it covers |
|---|---|
| [00 · Synthesis](research/00-synthesis.md) | The answers, in brief, and the current call |
| [01 · Definitions & framework](research/01-definitions-framework.md) | What each concept means, the four senses of "liquidity", China's institutional specifics |
| [02 · Monetary indicators](research/02-monetary-indicators.md) | ~40 indicators: aggregates, credit, rates, RRR, FX, composites |
| [03 · Liquidity indicators](research/03-liquidity-indicators.md) | ~40 indicators: repo, bank funding, PBoC operations, autonomous factors, market liquidity |
| [04 · Recent research](research/04-recent-research.md) | The 2024–26 PBoC framework overhaul, new measurement methods, 23 new indicators to build |
| [05 · Data sources](research/05-data-sources.md) | Endpoint-level sourcing manual and production pull strategy |
| [06 · Implications](research/06-implications.md) | Transmission, lead/lags, thresholds, the PBoC reaction function, read-across matrix, scenario map |
| [07 · Data validation](research/07-data-validation.md) | Independent audit: 178 comparisons against PBoC/NBS, discrepancies, confidence ratings |

## Repository layout

```
research/           the six research notes plus the synthesis
data/
  registry_*.json   indicator definitions — the single source of truth for the app
  composites.json   how the two indices are constructed
  seed/series.json  fetched observations
  seed/analyst_supplied.json   values entered by hand, kept separate so provenance stays auditable
scripts/
  build_app_data.py    merge, derive, compose → app/data.js
  make_standalone.py   app/ fragment → docs/index.html
  refresh_data.py      re-pull from public sources via akshare
tests/                 unit tests for the refresh parsing helpers
app/                   the tracker source (Artifact-form fragment + generated data.js)
docs/                  generated single-file build
```

To add an indicator, give it an entry in a `data/registry_*.json` file and observations under the same
key, then rebuild. The build reports every series it could not construct and why — missing data fails
loudly rather than quietly producing a plausible-looking index.

## Data provenance — read before using any number

This dataset was assembled inside a sandbox whose egress policy blocked **every** macroeconomic data
host: the PBoC, NBS, ChinaBond, CFETS, FRED, the BIS, the IMF and the World Bank were all unreachable.
Fetched values therefore came from **third-party mirrors, not primary publishers**. That is the gap the
[refresh workflow](#refreshing) exists to close — it pulls from the publishers' own endpoints on a
runner that can actually reach them.

In the meantime the dataset has been **independently audited**: 178 observation-level comparisons
against PBoC and NBS sources, of which 175 matched. See
[`research/07-data-validation.md`](research/07-data-validation.md). Every series carries a confidence
rating, visible in the app:

| Rating | Meaning |
|---|---|
| `verified` | Checked against the official record and matched. The six Monetary Policy Report series were audited by full census, not spot check — `walr_general`, which carries 30% of the monetary index, matched 33/33. |
| `partial` | From a mirror whose upstream is an official series, not confirmed at the publisher. |
| `analyst-supplied` | Entered from domain knowledge because no machine-readable source was reachable. |
| `suspect` | **Failed the audit.** Shown in the app with the problem stated and no loose/tight reading, so a known data defect cannot masquerade as a signal. |

Two series are flagged `suspect`: `nominal_gdp_level_cum` mixes pre- and post-census GDP vintages
(computing growth across that seam produces a phantom 2.8pp jump), and `core_cpi_yoy` labels three
year-to-date averages as single quarters.

The 7-day reverse repo and 1-year MLF rates are `analyst-supplied` — entered by hand because no
machine-readable source was reachable, and kept in their own file so they stay auditable. They have
since been corroborated against an independent Wind export: **12/12 overlapping OMO change dates and
14/14 MLF dates agree exactly, with no disagreements.**

One audit finding is worth repeating because it looks like an error and is not: `excess_reserve_ratio`
at 2024-Q3 = 1.8% is **correct**. The 27 September 2024 RRR cut landed three days before the
quarter-end snapshot. Do not "fix" it.

38 of 59 defined indicators carry data. The rest — including R007, the 1-year AAA NCD rate, DR001 and
TSF excluding government bonds — are defined, documented, and named in the app along with what their
absence costs, rather than quietly averaged over.

### Refreshing

The dataset refreshes itself. `.github/workflows/refresh-data.yml` runs weekly on a
GitHub runner — which, unlike the sandbox this was built in, has unrestricted network — and pulls
from the publishers' own endpoints via akshare, rebuilds, validates, and commits only if the sanity
gate passes. That workflow is what closes the provenance gap: values it commits come from primary
sources, not mirrors. It can also be run on demand from the Actions tab, with a dry-run option.

To run it locally:

```bash
pip install "setuptools<60" wheel
pip install --no-build-isolation jsonpath     # see note below
pip install akshare

python3 scripts/refresh_data.py               # dry run — reports what it would change
python3 scripts/refresh_data.py --write
python3 scripts/build_app_data.py && python3 scripts/make_standalone.py
python3 scripts/validate_data.py              # never skip this
```

The `jsonpath` dance is not optional. akshare depends on it; it ships sdist-only and its legacy
`setup.py` calls `install` during `bdist_wheel`, which modern setuptools rejects, so a plain
`pip install akshare` fails. Building it against `setuptools<60` with build isolation off works.

The weighted average lending rate and the excess reserve ratio have no machine-readable source at
all: they appear only in the quarterly PBoC Monetary Policy Report PDF and must be entered by hand.

### Guardrails

`scripts/validate_data.py` is the gate between a refresh and a commit. A silent mis-parse is far more
dangerous than a loud failure — it produces a plausible-looking index built on wrong numbers — so the
gate checks structure (well-formed, sorted, no future dates), plausibility (a policy rate of 40% means
the units are wrong, not that the PBoC panicked), anchors (values that are matters of public record and
cannot legitimately change), and coherence. If it fails, the refresh workflow restores the previous
dataset and uploads the rejected one for inspection rather than committing it.

Tests:

```bash
python3 tests/test_refresh_helpers.py     # column resolution, date parsing, unit scaling
python3 tests/test_refresh_fetchers.py    # every fetcher, against akshare's real response shapes
```

The fetcher tests replay column names read out of akshare 1.18.94's own source rather than guessed,
so they verify everything between the API boundary and the output file without touching the network.
They caught a real bug during development: the CFETS repo endpoint caps a request at one calendar
month, and the script was asking for a multi-year range. What they cannot verify is that the live
endpoints still return those columns — only the scheduled workflow does that.

`.github/workflows/ci.yml` runs both test suites, the build, and the gate on every push, and fails if
the committed `app/data.js` or `docs/index.html` is stale relative to its inputs.
