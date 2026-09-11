# tennis-edge-finder

Free-data tennis projection and Kalshi tennis-market research platform. **Status: research / market capture.
Real-money authority OFF. No model has shown edge against bookmaker prices; see MORNING_REPORT.md.**

### First-ball truth

`tennis-firstball.yml` polls live-score feeds adaptively and brackets the ACTUAL first ball of every
mapped match, so "this observation existed before the first ball" is a checkable claim rather than an
assumption about a scheduled time. Solved for ATP and WTA main tour and the Grand Slams; Challenger,
ITF and qualifying have no reachable source and fail closed as START_UNKNOWN. Real-money authority OFF.

## What it does
* Discovers the entire Kalshi tennis universe dynamically (143 series, 165k markets parsed), normalises every
  market into a payoff definition, and captures quotes/books/trades/settlements/candles prospectively.
* Builds a canonical match table from Sackmann (ATP/WTA all levels) + TML (ATP) snapshots with validation,
  quarantine and provenance (1.6M matches, 1990-2026).
* Rates players walk-forward (Elo family, structural serve/return), prices every match-scope market family
  from ONE exact match distribution (DP engine validated against Monte Carlo), checks probability invariants,
  and writes an append-only, hash-chained prediction ledger with the market quote beside every projection.
* Benchmarks against Pinnacle closing-style prices, fits walk-forward hybrids, reports disagreement buckets.

## Run (automated)
`.github/workflows/tennis-run.yml` (cron, push to `.run-trigger`, or dispatch) rebuilds, refits, prices, settles
and publishes to the `tennis-data` branch; `tennis-capture.yml` captures markets every 10 minutes (cron +
self-dispatching conductor); `tennis-bootstrap.yml` refreshes source snapshots and the Kalshi discovery daily.

## Run (local)
```
pip install -e . && python -m pytest -q tests
git fetch origin tennis-data && git archive origin/tennis-data tennis-edge-finder/data | tar -x --strip-components=1   # snapshots -> ./data
python tennis_edge/data/build.py                 # canonical matches.parquet
python -m tennis_edge.models.state --tour ATP && python -m tennis_edge.models.state --tour WTA
python scripts/run_tennis.py                      # projections + ledger + REPORT_<run>.md
python scripts/research/elo_study.py --tour ATP; python scripts/research/market_benchmark.py --tour ATP
```
Evidence (source snapshots, Kalshi captures, ledger, projections, settlements) lives on the orphan `tennis-data`
branch under the historical `tennis-edge-finder/data/...` prefix; see MIGRATION_AUDIT.md for why that prefix stays.

Docs: docs/ARCHITECTURE.md, DATA_SOURCES.md, KALSHI_MARKET_TAXONOMY.md, IDENTITY.md, MODELING.md,
VALIDATION.md, CLV_AND_SETTLEMENT.md, PROSPECTIVE_RESEARCH_PROTOCOL.md, PRODUCTION_HEALTH.md,
KNOWN_LIMITATIONS.md, DECISION_LOG.md, FIRST_BALL_SOURCES.md, FIRST_BALL_TRUTH.md.
Reports: MORNING_REPORT.md, FIRST_BALL_WAVE_REPORT.md. Migration record: MIGRATION_AUDIT.md.
