# Prospective research protocol

1. Every projection run appends one row per priced market to `data/research/ledger/<day>.jsonl`
   (`ledger/predictions.py`): prediction_id, generated_at_utc, match_id (event ticker), ticker, family,
   feature_snapshot_id (ratings hash), data_source_versions (discovery run, ratings build time), model_version,
   git_sha, market quote at prediction time (bid/ask both sides, source, timestamp, volume, OI, liquidity),
   all model probabilities (ELO, STRUCTURAL, ENSEMBLE, ELO_DP_FAIR, MARKET_MID, HYBRID placeholder),
   quality pillars, scheduled_start, seconds_to_scheduled_start, fee-adjusted EV fields, prev_hash, row_hash.
2. Rows are never rewritten. Actual start, sports truth, exchange truth and canonical close are recorded in
   SEPARATE settlement tables keyed by prediction_id. Gate TENNIS-12 verifies the hash chain.
3. Pregame validity: a row counts as a pregame prediction only if generated_at < actual_first_ball (or, while
   first-ball truth is unavailable, < scheduled_start - 5 min, flagged SCHEDULED_MINUS_MARGIN). Post-start rows
   are excluded from every evaluation (TENNIS-6).
4. Scoring: Brier/log-loss/calibration of each model column vs the market mid at prediction time AND vs the
   canonical close; executable CLV against the close; disagreement buckets. Reported per family, tour, level.
5. Promotion: a model column may become the decision model only after a pre-registered prospective window
   (>= 1,000 gradeable match-winner predictions, >= 8 weeks, all tours) in which it beats the market mid on
   log-loss with a bootstrap CI excluding zero AND shows non-negative executable CLV. Real-money authority
   is a separate, human decision after that.
6. Multiple testing: subgroup claims require n >= 300 per subgroup, holdout confirmation, and the
   hypothesis must have been registered in `research/hypothesis_registry.md` before the evaluation window.

## Automation
`scripts/ops/settle_ledger.py` joins ledger rows with the captured settlement stream and candle histories,
records ExchangeTruth / provisional SportsTruth (exchange result until a results feed exists), the canonical
close (candle bid/ask before min(scheduled, close − 7 h)) and CLV, appends to data/research/settlements/ and
rewrites SCORECARD.md (scores shown only from 30 gradeable rows). `.github/workflows/tennis-run.yml` runs
build → states → run_tennis → settle → health on the runner and publishes data/research to `tennis-data`.

## Timing classification (added by the first-ball wave, 2026-09-11)

Every prospective observation now carries an explicit timing class, derived from first-ball truth and
written to `data/research/timing/<run>.jsonl` on the `tennis-data` branch:

| class | meaning |
|---|---|
| `STRICT_PREGAME` | captured strictly before the EARLIEST possible first ball |
| `POST_START` | captured at or after the LATEST possible first ball |
| `AMBIGUOUS` | inside the first-ball bracket, or credible sources contradict each other |
| `START_UNKNOWN` | no trustworthy first-ball evidence for this match |

Rules this protocol now binds itself to:

* **Strict pregame research uses `STRICT_PREGAME` rows only.** Nothing else is eligible, at any
  confidence, for any claim about information held before the first ball.
* **Nothing is dropped.** `POST_START`, `AMBIGUOUS` and `START_UNKNOWN` rows are retained and labelled.
  A research record that deletes its inconvenient rows is a highlight reel.
* **The classification is DERIVED, the observation is IMMUTABLE.** A ledger row's `generated_at_utc` is
  never rewritten. When better first-ball truth arrives, the truth store gains a new derivation version
  and every affected row is reclassified from it, with the classifier version and derivation version
  recorded on the derived row. Recovering sports truth after the fact is allowed and expected.
  Rewriting a prediction or quote timestamp is forbidden.
* **Confidence C is never silently promoted.** An indirect bound classifies as `START_UNKNOWN` unless a
  caller explicitly opts into exploratory mode, which strict research does not.
* **A scheduled time is not a start.** The close function takes a truth object, so a nominal time, a
  Kalshi `occurrence_datetime` or a market `close_time` cannot be substituted for the first ball by
  accident. `tests/test_firstball.py` pins each of those substitutions as a failure.

## Segmented coverage schema

`data/research/segments/coverage.json` records, per run, the counts needed by the next research wave,
segmented by tour, level, family, surface, discipline, timing class, truth confidence, close basis,
data-quality grade, spread bucket, liquidity bucket, time-to-first-ball bucket, implied-probability
bucket, favourite/underdog and model-market disagreement bucket.

It deliberately records **counts and coverage only** -- n, strict n, rows with a close, rows with CLV. No
performance is reported by bucket, and no bucket is promoted. The purpose of this schema is to guarantee
that when edge research does begin, it begins on rows whose pregame status can survive an audit.

## Prospective invariant: no evidence from a contract that was already terminal (2026-10-01)

**A producer observation timestamped at or after a known Kalshi terminal settlement timestamp of its contract
cannot count as prospective evidence.** Only the exchange's own recorded `settlement_ts` (via
`confirmation.sources.settlement_payout`) decides it: never a schedule, a price, a result, file order or the
current time. A missing or unparsable `settlement_ts` never declares a row post-settlement by itself (the other
timing rules still apply), and `settlement_ts == predicted_at` fails closed.

Why it was needed: where no first-ball source exists (Challenger / WTA125 / ITF, and some main-tour matches) the
timing class is START_UNKNOWN, so the first-ball checks alone let through shadow-board rows priced after Kalshi
had already settled the market (at ~0.01 / 0.99).

How it is applied (`confirmation/started_candidates.py::_settled_before_observation`):

* W3-2026-001 / W3-2026-002: the FIRST observation of each contract, as before. If it was post-settlement the
  contract is EXCLUDED with `MARKET_SETTLED_BEFORE_OBSERVATION` and `settled_at` attached. The second
  observation is never substituted, because that would change the pre-registered decision unit.
* EC-2026-003: the first prediction run per physical match; contaminated if ANY of its match-winner contracts
  was already terminal at that run's timestamp. No later run is substituted.
* EC-2026-001 / 002 (Model 4): the same generic invariant on the derivative and both conditioning match-winner
  contracts of the first run (none affected at introduction).
* W4 and EC-004: checked, not changed. W4 already requires STRICT_PREGAME first-ball truth, and no EC-004 or W4
  observation showed the impossible chronology.

The reason is distinct from `TIMING_POST_START` (play known to have begun). The repair is an
**evidence-accounting correction, not a frozen-rule change**. The evidence store is append-only and versioned,
so a previously INCLUDED observation gets a NEWER EXCLUDED version (same observation_id, same decision-time
fields, `settled_at` populated). The old line stays forever, readers take the latest version, and the hash chain
is verified on every harvest. Each candidate report carries `evidence_accounting_correction` (counts by level and
by prior state), and `harvest_runs.jsonl` logs the per-candidate counts.
