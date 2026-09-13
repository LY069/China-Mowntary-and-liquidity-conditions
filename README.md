# China Monetary & Liquidity Conditions

A research pack and interactive tracker separating two things that market commentary routinely
conflates: **monetary conditions** (the policy stance as transmitted to the real economy, over
quarters) and **liquidity conditions** (the availability and price of short-term funding inside the
financial system, over days). In China the two come apart more than almost anywhere else, and telling
them apart is the point of this repository.

**→ Start with the [lead economist's synthesis](research/00-synthesis.md).**

---

## The tracker

An interactive dashboard covering 59 indicators, with a Monetary Conditions Index, a Liquidity
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
Every fetched value therefore came from **third-party mirrors on GitHub, not from a primary
publisher**. Values were spot-checked against the official record and match where checked — LPR, RRR,
M1, M2, CPI, PPI, TSF and nominal GDP levels all verify exactly — but **re-pulling from primary sources
is task one** for anyone using this seriously.

Each series carries a confidence rating, visible in the app:

| Rating | Meaning |
|---|---|
| `verified` | Traced to a named official publication, typically the PBoC Monetary Policy Report |
| `partial` | From a mirror whose upstream is an official series, not confirmed at the publisher |
| `analyst-supplied` | Entered from domain knowledge because no machine-readable source was reachable |

Two series are `analyst-supplied`: the 7-day reverse repo rate and the 1-year MLF rate. They were added
deliberately — without a policy rate there is no DR007 spread, no real policy rate and no liquidity
index at all — and they are cross-checked against Monetary Policy Report anchors and against the RRR
series, which independently corroborates the May 2025 easing package.

About 25 defined indicators carry no data, including R007, the 1-year AAA NCD rate, DR001, the REER and
TSF excluding government bonds. The app names each one and what its absence costs.

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
