# tennis-edge-finder

Free-data tennis projection and Kalshi tennis-market research platform. **Status: research / market capture.
Real-money authority OFF. No model has shown edge against bookmaker prices, and Wave 3 found no subset of
Kalshi tennis markets where our probability is more accurate than the price -- including the subsets that
returned a profit. See WAVE3_SELECTIVE_EDGE_REPORT.md and MORNING_REPORT.md.**

### ChatGPT-assisted handicapping lane (new, 2026-09-30)

A separate prospective lane measures the workflow that is actually used: repo data + Kalshi prices +
external prices -> ChatGPT handicapping -> market selection -> a person's betting decision.
`scripts/research/build_assisted_slate.py` writes the handicapping packet (`assisted_slates/latest.{md,json}`),
`scripts/research/record_assisted_decision.py` (or the `TENNIS assisted record` workflow) records each
BET / PASS / WATCH before the first ball and, separately, any wager a person actually placed;
`scripts/research/run_assisted_pipeline.py` settles, measures strict CLV and builds the scorecard and CEO
scoreboard; TENNIS-16 watches the pipeline. **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF;
CHATGPT_ASSISTED_TRACK = ACTIVE;** no frozen model or candidate is touched and no profitability is implied.
See `docs/ASSISTED_HANDICAPPING.md`.

### Discrepancy sanity layer (new, 2026-10-01)

A big model-vs-Kalshi gap is a question, not an edge. Every priced contract on the assisted slate carries
its gap, a band (NORMAL <10 / REVIEW 10-15 / HIGH_REVIEW 15-25 / EXTREME >=25 pp) and identity, ticker
orientation, quote freshness, external and data-quality checks; EXTREME gaps are DATA_WARNING by default and
a BET on one is refused unless nine conditions hold (then only eligible for human review). TENNIS-17 guards
it. The audit behind it (`research/model_market_discrepancy/AUDIT.md`) found most extreme gaps were
ITF/Challenger markets priced after Kalshi had settled, in-play prints or stale quotes, not model insight.
No model probability changed.

### Start-time reconciliation (new, 2026-10-02)

Kalshi's scheduled time is not a start time (on 2026-10-02 it was a 06:00Z placeholder for 27 WTA matches,
six of which had started by 03:05-05:50Z). Every slate match now carries a reconciled START STATUS (first-ball
truth > live state > ESPN live schedule > court progression > Kalshi nominal), BETs fail closed unless a live
source recently saw the match pending, and the first-ball conductor plans the next main-tour window from the
EARLIEST credible first ball, dispatching the slate refresh 45 and 10 minutes before it
(`firstball/store/schedule/NEXT_WINDOW.md`). TENNIS-18 guards it. See `docs/START_TIME_RECONCILIATION.md`.

### External reference markets

`scripts/external/capture_and_scan.py` runs inside the capture conductor: it fetches Bovada's public
tennis coupon and Smarkets' exchange order books, de-vigs the book, maps every venue through the same
player registry, and records where Kalshi and an independent venue disagree. Two separate witness groups,
neither of them Kalshi and neither of them our model. See `docs/EXTERNAL_MARKET_SOURCES.md` for what was probed and rejected
(Pinnacle answers 451; Polymarket lists tennis and does not trade it; Smarkets is a genuine exchange
whose tennis books are five times wider than Kalshi's) and `docs/EXTERNAL_MARKET_PROTOCOL.md` for how a
disagreement is allowed to become an opinion.

### Selective mispricing detector

`scripts/ops/shadow_board.py` prices the live board, applies `selector_v1`, and returns PASS on most of it.
The three decisions are PASS, WATCH and SHADOW_BET; there is no fourth, and no code path in this repository
expresses a real wager. A SHADOW_BET means an opportunity survived every check we know how to run, which is
a statement about our checks rather than about the market -- every row says so in its own text. See
`docs/SELECTIVE_EDGE_PROTOCOL.md`, `docs/OPPORTUNITY_SCHEMA.md` and `research/SELECTOR_FAILURE_MODES.md`.

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
* Scores settled Kalshi markets walk-forward (`data/processed/asof/`: every player's state after each match,
  read strictly before the match date) and studies WHEN a disagreement with the price is worth anything.
  The answer so far is "at ITF level, less than nothing".

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
KNOWN_LIMITATIONS.md, DECISION_LOG.md, FIRST_BALL_SOURCES.md, FIRST_BALL_TRUTH.md, START_TIME_RECONCILIATION.md.
Reports: MORNING_REPORT.md, FIRST_BALL_WAVE_REPORT.md. Migration record: MIGRATION_AUDIT.md.
Prospective confirmation of the frozen candidates: PROSPECTIVE_CONFIRMATION_REPORT.md,
research/PROSPECTIVE_EVIDENCE_AUDIT.md, `scripts/research/harvest_candidate_evidence.py` (derived,
append-only evidence layer in `data/research/candidate_evidence/`; candidate definitions are never written).
Frozen producers run live since 2026-09-28 (shadow board, Model 4): docs/FROZEN_PRODUCERS.md; health gate TENNIS-15.
