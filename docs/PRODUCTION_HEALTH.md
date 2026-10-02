# Production health gates (tennis_edge/health/gates.py)

| gate | name | PASS condition | evidence |
|---|---|---|---|
| TENNIS-1 | complete Kalshi tennis discovery | latest discovery complete, catalogue fully paginated, no failures, < 36 h old | data/kalshi/discovery/<run>/summary.json |
| TENNIS-2 | taxonomy normalization | no tennis series outside the family registry; >= 99.5 % of live markets PARSED or explicitly UNSUPPORTED | series_tennis.json + parser |
| TENNIS-3 | active-market mapping | zero UNPARSED among OPEN markets | markets/*.json (open) |
| TENNIS-4 | active-market projection | every open projectable market present in the latest projection run | data/research/projections/latest.json |
| TENNIS-5 | capture freshness | latest capture manifest <= 30 min old, no incomplete stage | data/kalshi/capture/<day>/<run>.manifest.json |
| TENNIS-6 | no post-start leakage | every ledger row generated before actual first ball (or scheduled - 5 min when unknown, counted) | ledger + starts |
| TENNIS-7 | player identity integrity | no AMBIGUOUS mapping used in production | link/mapping summaries |
| TENNIS-8 | sports truth health | >= 98 % of settled predictions have gradeable sports truth | settlement table |
| TENNIS-9 | exchange settlement health | zero unexplained sports/exchange conflicts; no unreviewed important_info id change | settlements + config/kalshi_settlement_rules.json |
| TENNIS-10 | CLV close coverage | canonical close for >= 95 % of settled pregame predictions (basis breakdown reported) | close table |
| TENNIS-11 | probability consistency | no invariant violation across a match's priced markets | payoffs.check_consistency |
| TENNIS-12 | append-only ledger | hash chain intact | data/research/ledger/*.jsonl |
| TENNIS-13 | reproducible artifacts | build manifest hash matches matches.parquet; source run ids recorded | data/processed/build_manifest.json |
| TENNIS-14 | data-source freshness | newest match-data snapshot <= 8 days old and covers the current season | data/sources/*/manifest.json |

UNKNOWN (evidence absent) is treated as not-PASS. Gates are never relaxed to go green; fix the pipeline.
`python -c "from tennis_edge.health.gates import run_all; [print(g.to_dict()) for g in run_all()]"`.

## First-ball submetrics (added 2026-09-11)

`tennis_edge.health.gates.first_ball_metrics()` derives these from evidence on disk and feeds gates
TENNIS-6, TENNIS-8 and TENNIS-10:

| metric | meaning |
|---|---|
| `truths`, `strict_truths`, `no_play` | matches with any first-ball truth, with A/B truth, and confirmed walkovers |
| `by_confidence` | A / B / C / UNKNOWN distribution |
| `bracket_seconds_median`, `bracket_seconds_p90` | the timestamp error bound actually being achieved |
| `contradictions`, `contradiction_rate` | material source disagreements, and their share |
| `chain_violations` | append-only integrity of the first-ball store |
| `observations`, `matches_observed` | raw polling volume and reach |
| `watchlist.levels_with_a_wired_source` / `levels_without_any_source` | the structural coverage gap, reported as counts |
| `watchlist.pct_covered_with_source_mapping` | share of watched matches at covered levels actually bound to a source |
| `pct_classifiable`, `pct_strict_pregame` | share of prospective observations with a class other than START_UNKNOWN, and the strict share |
| `executable_close_rows`, `strict_clv_rows` | closes and CLV rows that are first-ball anchored |
| `horizons_populated` / `horizons_total` | how many canonical decision horizons had a real quote |

### What changed in the gates

* **TENNIS-6** now prefers actual first-ball truth over the scheduled fallback for every match where
  truth exists.
* **TENNIS-8** is no longer only about settled-prediction sports truth. It also requires an intact
  first-ball hash chain and that at least 90% of watched matches *at levels with a wired source* are
  actually bound to that source. Levels with no source at all are reported as counts, never averaged in.
* **TENNIS-10** measures close coverage against **strict** first-ball-anchored closes. A close cut off at
  `scheduled_start - margin` no longer counts toward it. With no A/B truth yet the gate reports UNKNOWN,
  which is a failure for production purposes, by design.

Thresholds were not moved to accommodate any of this. The gates that fail, fail because the underlying
coverage does not exist yet, and that is the information they are meant to carry.


## Wave 3 additions

* **TENNIS-14 (fundamental staleness)** is red for the WOMEN only. ATP serve statistics reach 2026-09-01
  through the TML Challenger mirror; WTA stops at 2026-04-27 and a bounded search found no free, permitted
  replacement (`docs/DATA_SOURCES.md`). Results for both tours are current to 2026-09-11 via ESPN, so the
  Elo family is fresh on both sides and only the structural model is starved.
* **Identity confidence is now graded.** An exact full-name match carries 1.0 (0.9 if the player has not
  appeared in two years); a compound-surname alias carries 0.9. Qualification requires >= 0.95, so an
  aliased identity can restore board coverage but can never drive a SHADOW_BET.
* **The opportunity store** (`data/research/opportunities/`) is append-only and hash-chained, and
  `OpportunityStore.verify_chain()` checks both the chain and each row's own fingerprint. It belongs in the
  same daily integrity sweep as the prediction ledger and the first-ball store.


## Wave 4 additions

* **The external dislocation ledger** (`data/research/external/dislocations/`) is append-only and
  hash-chained; `DislocationLedger.verify_chain()` belongs in the same daily integrity sweep as the
  prediction ledger, the first-ball store and the opportunity store.
* **Single-witness reference.** Every reference value this system can currently build comes from ONE
  independent group (Bovada). `Reference.n_independent_groups` is recorded on every row, and a second
  venue is the single largest improvement available to this layer.
* **The external witness is a recreational book.** Bovada is not a sharp reference. Health reporting
  should never describe a Bovada/Kalshi gap as a mispricing.
* **Staleness is bounded in both directions**: the venue's own timestamp against our fetch (15 min) and
  our fetch against now (15 min). A venue that publishes no timestamp reads as unknown, never as zero.
* **Model freeze.** `fair_v1`, `gen2_dyn_hier_sr_v1` and `selector_v1` are frozen for Wave 4 and a test
  asserts their version strings. A bug fix that changes historical probabilities needs a new version;
  frozen predictions are never retroactively replaced.


## Wave 5 additions

* **Two external witness groups now exist** (`bovada`, `smarkets`). `Reference.n_independent_groups` is
  still the number to watch: a reference built from one group is one venue's opinion.
* **The exchange spread bound is load-bearing.** Smarkets quotes tennis at a median 10c spread, so most
  of its rows are excluded from the reference by design and counted in `excluded_wide_book`. A sudden
  fall in that count means either the books tightened or the bound was changed; only the first is good
  news.
* **Smarkets publishes no order-book timestamp.** Its rows carry `source_timestamp: None` and are
  therefore bounded only by capture age. If a future Smarkets change starts supplying one, the
  `require_source_timestamp` path already exists to use it.
* **The Smarkets traversal is undocumented upstream** and recorded only in
  `tennis_edge/external_market/smarkets.py:TRAVERSAL`, asserted by a test. If that query ever stops
  accepting `type=tennis_match`, capture silently returns an empty board -- the scan's
  `smarkets_fetch.events_seen` is the canary.


## Prospective-evidence audit (2026-09-27)

What the gates were reading, and what changed. No threshold moved; see `research/PROSPECTIVE_EVIDENCE_AUDIT.md`.

* **TENNIS-8/9/10 said "no settled predictions yet" for sixteen days while the settlement table held
  12,330 settled rows.** Settlement ingestion was healthy; the health step called `run_all()` with no
  settlement inputs, so `sports_total` and `n_settled` were always `None`. `settlement_stats()` now reads
  `data/research/settlements/*.jsonl` and the latest `data/research/clv/<run>.jsonl` directly.
* **TENNIS-8 counts only sports truth INDEPENDENT of the exchange.** Every settled row's "sports truth" is
  copied from Kalshi's own result (`source: kalshi_result`). That cannot be reconciled against Kalshi, so
  it is reported (`settlement.sports_truth_kalshi_derived`) but not counted as ok. Result: FAIL, 0 of
  12,066 -- the honest state, and the gap to close is an independent results feed in the settle job.
* **TENNIS-9** reports UNKNOWN with the reason "no sports truth independent of the exchange" instead of
  the stale "no settled predictions yet".
* **TENNIS-10** now uses one population for numerator and denominator: settled predictions whose match has
  A/B first-ball truth (2,688), of which 2,312 have a strict CLV record (86%). FAIL at the unchanged 95%.
  The shortfall is the 330 rows priced after the first ball (below) plus rows with no quote before it.
* **TENNIS-6** still FAILS on every violation. Its detail now separates `post_start_confirmed` (297),
  `inside_first_ball_bracket` (33), `schedule_fallback` (0) and `no_start_information` (0), reports
  `n_violations` (330; the list is still truncated to 20), and counts the conservative START_UNKNOWN rows
  that passed the schedule check (9,718) as what they are: not violations. It also checks the thing that
  would be a true leak -- a post-start row used as strict evidence -- directly: `post_start_rows_in_strict_research` = 0.
  The 330 rows are real: Challenger/WTA-125 matches whose nominal start was hours after the actual first
  ball were priced in play. `run_tennis.py` now refuses any match the first-ball store has already seen
  start (`matches_already_started`), across every series of the same physical match.
* **TENNIS-5** no longer fails merely because a trade-tape window was truncated and its remainder QUEUED
  (`tennis_edge/kalshi/trade_tape.py`); it fails on fetch errors, on an ABANDONED gap, and when the oldest
  queued gap is more than two hours old. Before the fix every one of 1,689 passes truncated and the cursor
  silently skipped ~2.75 hours of tape.
* **TENNIS-2/3** pass: the two Laver Cup series are now explicit (`TEAM_EVENT_MATCH_WINNER`, unpriced).

## TENNIS-15 prospective_confirmation_health (2026-09-28)

Per frozen candidate: producer required / active (last heartbeat, scan or capture manifest), effective
scorable start, eligible / settled / strict-CLV N, last evidence and its age, candidate status, last
harvest success and failure. Health labels, deliberately distinct:

| label | meaning | gate |
|---|---|---|
| HEALTHY_NO_QUALIFYING_MARKETS | producer alive, harvest fine, nothing qualified | PASS |
| INSUFFICIENT_N / PENDING_SETTLEMENT / PENDING_STRICT_CLV | scoring, not yet decidable | PASS |
| SCORING_ACTIVE | enough to evaluate the frozen conditions | PASS |
| PRODUCER_NOT_RUNNING | no heartbeat inside 13 h (shadow board, Model 4) or 2 h (external scan, capture books), or no experiment-start record | FAIL |
| HARVEST_FAILED | the last harvest failure is newer than the last success (`candidate_confirmation/HARVEST_STATUS.json`) | FAIL |

A harvest failure is an `::error::` annotation in RUN TENNIS, is recorded by `--record-failure`, and
FAILS TENNIS-15; settlement and capture outputs still publish, and the next run retries from the immutable
inputs. Zero evidence because Kalshi listed nothing qualifying is healthy; a silent producer is not.

## TENNIS-16 assisted_decision_pipeline_health (2026-09-30)

The ChatGPT-assisted lane's OPERATIONS gate (`tennis_edge/assisted/health.py`), separate from TENNIS-15 and
from any authority: it says whether the lane is recording, settling and scoring correctly, never whether it
makes money. Reported: latest slate build and age, latest assisted decision, settlement freshness,
unsettled decisions (and those stalled over 7 days), strict CLV coverage, schema validity, duplicate
decisions (ids and content), post-start decision violations, integrity violations (record fingerprints,
canonical hash chains, compile checks), TRACK_START fingerprint.

| label | meaning | gate |
|---|---|---|
| HEALTHY_NO_DECISIONS_YET | slate and pipeline fresh, nothing recorded yet | PASS |
| HEALTHY | fresh, every record valid, nothing overdue | PASS |
| UNHEALTHY | any of SLATE_STALE, PIPELINE_STALE, PIPELINE_ERROR, INTEGRITY_VIOLATION, SCHEMA_INVALID, DUPLICATE_DECISIONS, POST_START_DECISIONS (last 7 d), SETTLEMENT_STALLED, TRACK_START_MODIFIED | FAIL |
| (no TRACK_START or no slate yet) | the lane has not run in production | UNKNOWN |


## TENNIS-17 model_market_discrepancy_integrity (2026-10-01)

An INTEGRITY gate over the assisted discrepancy sanity layer (`tennis_edge/assisted/health.py::gate_17`), not
a profitability gate: a model-market disagreement on its own never fails it. It reads the latest assisted
slate and every schema-v2 assisted decision, recomputes each priced contract's band from its own model number
and Kalshi mid, and checks that no large disagreement escapes the layer.

| failure | meaning |
|---|---|
| SLATE_LACKS_DISCREPANCY_CLASSIFICATION | the slate predates the layer, or a priced row / v2 decision carries no classification |
| BAND_MISMATCH | a row's band is not the band of its own gap (the layer was bypassed or edited) |
| MALFORMED_PROBABILITY | a model or market probability outside [0, 1], NaN, or not a number |
| TICKER_ORIENTATION_MISMATCH | a contract whose YES side contradicts our player A/B orientation (or a BET recorded on one) |
| EXTREME_UNRESOLVED_IDENTITY | an EXTREME gap with ambiguous/failed identity surfaced as anything but DATA_WARNING |
| EXTREME_STALE_PRICE_ACTIONABLE | an EXTREME gap on a STALE quote surfaced as anything but DATA_WARNING |
| EXTREME_BYPASS | an EXTREME gap not at DATA_WARNING on the slate, or a recorded BET on one that is not ELIGIBLE_FOR_HUMAN_REVIEW with all nine Part J conditions met and an explanation |
| HIGH_REVIEW_BYPASS | a HIGH_REVIEW gap surfaced without the explanation requirement, or a recorded BET on one with no `discrepancy_explanation` |

UNKNOWN when no slate exists yet. EXTREME rows held at DATA_WARNING with ambiguous identity or stale quotes
are the layer working, and PASS. The detail reports counts by band, status, freshness, identity and
orientation and a sample of the EXTREME rows.


## TENNIS-18 start_time_window_health (2026-10-02)

Guards the start-time reconciliation and the RUN TENNIS window planner (`tennis_edge/assisted/health.py::gate_18`,
`docs/START_TIME_RECONCILIATION.md`). It reads `firstball/store/schedule/plan_latest.json`, the latest assisted
slate, the slate run log and every schema-v3 assisted decision.

| failure | meaning |
|---|---|
| PLAN_STALE | no window plan in the last 45 min: the conductor's planner is not watching the clock |
| SLATE_LACKS_START_STATUS | the latest slate carries no reconciled start status |
| BET_ALLOWED_ON_BLOCKING_STATUS | a slate match STARTED / STATUS_AMBIGUOUS / NO_PLAY is marked bet-allowed |
| BET_ON_UNVERIFIED_START | a recorded (v3) BET whose start status at decision blocked a BET |
| WINDOW_MISSED | a planned ATP/WTA window whose first ball passed in the last 24 h without a slate built 60-5 min before it |

UNKNOWN until the planner has run in production (no `plan_latest.json`). The detail reports the next
window, counts by status and the missed windows. Replayed on 2026-10-02's data it fails with
SLATE_LACKS_START_STATUS and WINDOW_MISSED 06:00Z -- the miss that motivated it.
