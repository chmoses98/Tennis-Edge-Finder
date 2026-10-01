# ChatGPT-assisted handicapping lane

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** The track starts with zero
evidence and makes no profitability claim.

## The question

> Does the data Tennis-Edge-Finder produces help ChatGPT identify and price individual tennis bets well
> enough to produce positive after-fee returns?

This is not "does Gen-2 beat Kalshi", "does selector_v1 make money" or "is every model disagreement an
edge". The real workflow is selective: **model/repo data + market prices + external market context →
ChatGPT handicapping → market selection → an actual betting decision by a person.** The repository is the
information engine; ChatGPT is the handicapper; a person decides and places (or does not place) the bet.

## Separation from the frozen research

The lane lives beside the autonomous experiments and cannot touch them:

* `tennis_edge/assisted/` imports no model-fitting code and never opens a producer store, a candidate
  definition or an experiment-start record for writing (`tests/test_assisted_track.py` checks the source).
* Gen-1, Gen-2, Model 4, fair_v1, selector_v1, external_v1, every frozen candidate, threshold, minimum N,
  pass condition and experiment start are unchanged (sha256 pins in `tests/test_frozen_producers.py`,
  re-asserted by the assisted tests).
* Postmortems and results never feed back into a weight, a threshold, a selector or a rule.
* No code path places, routes or sizes an order.

## Flow

```
RUN TENNIS (every 6 h)                                   a person / ChatGPT
  frozen producers -> build_assisted_slate.py  --->  assisted_slates/latest.{md,json}  (read the packet)
                                                                  |
                                                     handicap, choose the expression, decide
                                                                  |
                     TENNIS assisted record (workflow_dispatch) <-+  kind=decision  (BET / PASS / WATCH)
                                                                  +  kind=wager     (only if actually placed)
  run_assisted_pipeline.py: compile ledgers, settle, CLV, scorecard, PIPELINE_STATUS  <- later truth
  health gates: TENNIS-16 assisted_decision_pipeline_health (operations only)
```

## Paths (on the `tennis-data` branch, under the historical `tennis-edge-finder/` prefix)

| path | written by | what |
|---|---|---|
| `data/research/assisted_slates/latest.json`, `latest.md` | RUN TENNIS, `TENNIS assisted slate` | the handicapping packet |
| `data/research/assisted_slates/slate_runs.jsonl` | same | one line per slate build |
| `data/research/assisted_decisions/TRACK_START.json` | RUN TENNIS, once | effective start of the track, authority state |
| `data/research/assisted_decisions/records/{decisions,wagers,postmortems,evidence}/<day>/<id>.json` | `TENNIS assisted record` | write-once records, one file per id |
| `data/research/assisted_decisions/assisted_decisions.jsonl` (+ `_wagers`, `_postmortems`, `_evidence`) | RUN TENNIS | canonical append-only, hash-chained ledgers compiled from the records |
| `data/research/assisted_decisions/assisted_settlements.jsonl` | RUN TENNIS | derived settlement + CLV rows |
| `data/research/assisted_decisions/PIPELINE_STATUS.json` | RUN TENNIS | last run, integrity, settle counts (read by TENNIS-16) |
| `data/research/assisted_handicapping/SCORECARD.{json,md}` | RUN TENNIS | live scorecard + CEO scoreboard |
| `research/assisted_handicapping/SCORECARD.{json,md}` (main) | `run_assisted_pipeline.py` | scorecard snapshot committed with the code (empty at launch) |

Raw URLs for ChatGPT: `https://raw.githubusercontent.com/chmoses98/Tennis-Edge-Finder/tennis-data/tennis-edge-finder/data/research/assisted_slates/latest.md`
(and `latest.json`, and `.../assisted_handicapping/SCORECARD.md`).

**Why one file per record.** Evidence reaches `tennis-data` through `scripts/ci/publish_branch.py`, which
copies a local tree over the branch tip. Two jobs appending to one shared JSONL would overwrite each
other's rows. A record file's path is its id, so a publish can never lose or replace one;
`publish_branch.py --no-overwrite` fails loudly (exit 4) if an existing record would change. The canonical
JSONL ledgers are compiled from the records by a single writer (RUN TENNIS), append-only.

## "RUN TENNIS" procedure

1. Read `assisted_slates/latest.md` (for fresher quotes, dispatch `TENNIS assisted slate` first).
2. For each match considered, decide BET / PASS / WATCH. Re-check the live Kalshi book; pass the live
   `kalshi_bid`/`kalshi_ask` in the decision when you have them.
3. Record every decision **before the first ball**, within 3 h of making it: dispatch
   `TENNIS assisted record` with `kind=decision` and the JSON payload, or run the CLI.
4. If a person actually places a bet, record it separately with `kind=wager`. A recommendation is never
   assumed to have become a wager.
5. After settlement, optionally record a `postmortem`; new facts learned after the decision go in as
   `evidence`. Neither changes the decision.

## Decision-recording command

```
python scripts/research/record_assisted_decision.py --input decision.json            # or stdin / --json '{...}'
python scripts/research/record_assisted_decision.py --kind wager --input wager.json
python scripts/research/record_assisted_decision.py --template decision               # input template
python scripts/research/record_assisted_decision.py --dry-run --input decision.json   # validate only
```
Workflow: **Actions → TENNIS assisted record → Run workflow**, `kind` + `payload` (the same JSON).
Exit 0 recorded, 2 refused (with a stable code), 1 unexpected error.

### Minimal decision payload

```json
{"ticker": "KXATPMATCH-26OCT01FARFER-FER", "side": "YES", "decision": "BET",
 "kalshi_bid": 0.49, "kalshi_ask": 0.50,
 "chatgpt_fair_probability": 0.55, "chatgpt_confidence": "MEDIUM",
 "chatgpt_thesis": "...", "key_supporting_factors": ["..."], "key_opposing_factors": ["..."],
 "factor_tags": ["SERVE_EDGE", "PRICE_VALUE"],
 "primary_match_thesis": "...", "why_chosen_expression_best_matches_thesis": "...",
 "bet_up_to_price": 0.52, "stake_units_if_bet": 1}
```
A PASS needs `ticker`, `decision` and `pass_reason_if_pass` (a probability and a side are welcome). A
WATCH needs `side`, `chatgpt_fair_probability` and `chatgpt_thesis`. Everything else (model, market and
external context, identity, first-ball status, agreement classification) is filled and stamped by the
recorder from the slate and the capture; values the handicapper supplies for model/external fields are
kept as supplied and listed in `model_context_source.fields_from_input`.

### What the recorder enforces

| rule | refusal code |
|---|---|
| the track has a valid TRACK_START | `TRACK_NOT_STARTED` |
| only schema fields; JSON object | `UNKNOWN_FIELD`, `INVALID_PAYLOAD` |
| Kalshi ticker, match-scope family (futures/novelties refused) | `INVALID_TICKER`, `UNSUPPORTED_MARKET_FAMILY` |
| market exists on the capture or the current slate and is open | `MARKET_NOT_FOUND`, `MARKET_NOT_OPEN` |
| event / physical match ids consistent with the ticker and the slate | `IDENTIFIER_MISMATCH` |
| `created_at` has a UTC offset, is not in the future, is recorded within 3 h, is after the track start | `INVALID_TIMESTAMP`, `DECISION_IN_FUTURE`, `RECORDED_TOO_LATE`, `BEFORE_TRACK_START` |
| made before any first ball the store has observed (any confidence) | `POST_START_DECISION` |
| made before but recorded after the first ball | admitted, `RECORDED_AFTER_FIRST_BALL`, excluded from the headline scorecard |
| a BET has a two-sided price, confidence, thesis, bet-up-to, stake in (0, 10] units | `MARKET_PRICE_UNAVAILABLE`, `MISSING_FIELD`, `INVALID_FIELD` |
| factor tags from the fixed vocabulary, no repeats (none is fine) | `INVALID_FACTOR_TAG` |
| `chosen_expression` is the ticker's own family | `EXPRESSION_MISMATCH` |
| decision id unique; the same decision resubmitted within 6 h | `DUPLICATE_ID`, `DUPLICATE_SUBMISSION` |
| a wager links to a recorded decision on the same ticker/side, after it, stake = price x contracts | `UNKNOWN_DECISION`, `WAGER_MARKET_MISMATCH`, `INVALID_TIMESTAMP`, `STAKE_MISMATCH` |

## Exact decision schema (schema_version 2, `tennis_edge/assisted/schema.py::DECISION_SCHEMA`; v1 = v2 without the discrepancy group)

Probability convention: every probability is **P(ticker resolves YES)**; `side_entry_price`,
`bet_up_to_price` and `bet_up_to_probability` are for the named contract side (NO ask = 1 - YES bid).

| group | fields |
|---|---|
| identity | decision_id (`AD-YYYYMMDD-<12 hex>`), schema_version, track, created_at, recorded_at, recorder_version, code_sha, slate_id, slate_built_at, input_payload_sha256 |
| match | physical_match_id, event_id, match_code, ticker, series, tour, level, level_bucket, competition, surface, surface_bucket, players, market_family, market_description, side, strike, scheduled_start, first_ball_status_at_decision, first_ball_source_coverage, scheduled_start_passed_at_decision |
| model context | gen1_probability, gen2_probability, model4_probability_if_applicable, fair_v1_probability, model_probability_yes, model_probability_source, selector_state, model_uncertainty, serve_evidence_player_a, serve_evidence_player_b, rating_state, surface_adjustment, recent_form_inputs, additional_model_inputs, model_context_source |
| market context | kalshi_bid, kalshi_ask, kalshi_mid, kalshi_spread, displayed_size, fee, market_implied_probability, side_entry_price, side_fee, market_quote_source, market_quote_observed_at, market_quote_age_seconds, repo_market_at_decision |
| external context | bovada_probability_if_available, smarkets_probability_if_available, external_consensus, triangulation_state, external_freshness, external_context_source |
| handicapping | chatgpt_fair_probability, chatgpt_confidence (LOW/MEDIUM/HIGH), chatgpt_thesis, key_supporting_factors, key_opposing_factors, factor_tags, model_agreement_state, model_preferred_side, chatgpt_preferred_side, model_side_edges, material_disagreement_with_kalshi, market_disagreement_reason, why_market_may_be_wrong, why_model_may_be_wrong, pass_reason_if_pass |
| discrepancy sanity (v2) | model_market_gap_pp, discrepancy_band, discrepancy_sanity_status, discrepancy_reason_tags, identity_check_status, ticker_orientation_status, market_freshness_status, external_confirmation_status, data_quality_status, discrepancy_conditions, discrepancy_explanation, sample_asymmetry_justification, external_unavailable_reason, discrepancy_context_source |
| expression | primary_match_thesis, available_expressions, chosen_expression, why_chosen_expression_best_matches_thesis |
| decision | decision (BET/PASS/WATCH), recommended_price, bet_up_to_probability, bet_up_to_price, stake_units_if_bet, actual_wagered |
| authority | authority (`ASSISTED_HUMAN_DECISION_NO_AUTOMATED_EXECUTION`), autonomous_real_money_authority (`OFF`), automated_execution (`false`), warnings |

`model_probability_yes` is the repository's number for THIS contract: fair_v1 (match winner), else Model 4
conditioned (listed derivatives), else Gen-1 ELO_DP_FAIR, else Gen-2.

Immutable once written (Part 11; the whole record is fingerprinted, and these are the fields an integrity
violation names): decision_id, created_at, ticker, side, decision, chatgpt_fair_probability,
chatgpt_confidence, chatgpt_thesis, key_supporting/opposing_factors, factor_tags, primary_match_thesis,
chosen_expression, why_chosen_expression…, bet_up_to_probability/price, recommended_price,
stake_units_if_bet, kalshi_bid/ask/mid, side_entry_price, market_implied_probability, and the agreement
fields. Later information is appended only as settlement, CLV, postmortem or evidence rows.

## Exact wager schema

wager_id (`AW-…`), decision_id, schema_version, recorded_at, placed_at, ticker, side, entry_price,
contracts, stake_dollars, fees (default: Kalshi taker fee), source (`MANUAL_KALSHI_UI`,
`MANUAL_KALSHI_API`, `KALSHI_ROUTER`, `OTHER`), status (`FILLED`, `PARTIAL_FILL`, `CANCELLED`,
`VOIDED_BY_EXCHANGE`), external_order_id (the hook for a future Kalshi router: unique, never reused),
decision_was_bet, placed_after_first_ball, first_ball_status_at_placement, input_payload_sha256,
authority, warnings.

## Settlement rows (derived, `assisted_settlements.jsonl`)

settlement_id, row_kind (`DECISION` | `WAGER`), decision_id, wager_id, revision, supersedes, settled_at,
settlement_result (YES/NO/VOID_SCALAR), settlement_value_yes, side, side_won, entry_price, contracts,
gross_pnl, fees, net_pnl, roi, strict_close, strict_executable_clv, midpoint_clv, clv_timing_class,
clv_exclusion_reason, first_ball_confidence, first_ball_lower_utc, post_start_violation, and for decisions
the model-side hypothetical (`model_side_unit`, `model_side_strict_executable_clv`) and `outcome_yes`.

* DECISION rows: one contract of the decision's side at the decision's own executable price, taker fee
  included (`pnl_unit = ONE_CONTRACT_AT_DECISION_PRICE`); units P&L = ROI x stake_units.
* WAGER rows: the person's actual contracts, price and fees (`pnl_unit = ACTUAL_WAGER_DOLLARS`);
  ROI = net / (stake + fees). Cancelled wagers are not scored.
* Strict CLV: close = last executable quote strictly before the earliest possible first ball of A/B
  first-ball truth; entry must be STRICT_PREGAME. Executable CLV = side close bid - side entry ask;
  midpoint CLV secondary. Challenger/ITF/WTA125 have no first-ball source, so no strict CLV there.
* If first-ball truth arrives after a row was written, ONE revision row is appended; nothing is rewritten.

## Agreement classification (Part 4)

A side is **preferred** when its fee-adjusted executable edge (probability - side ask - taker fee) is
strictly positive, computed on the decision's own quote; otherwise NEUTRAL (or NONE without a number).

| decision | model preferred side | state |
|---|---|---|
| BET on side S | S | AGREED_WITH_MODEL |
| BET on side S | the other side | OVERRULED_MODEL |
| BET | NEUTRAL / NONE | MODEL_NEUTRAL |
| PASS / WATCH | YES or NO | OVERRULED_MODEL (a declined model edge: the pass-quality sample) |
| PASS / WATCH | NEUTRAL / NONE | MODEL_AND_CHATGPT_BOTH_PASS |

"Followed model" = an agreed bet whose ChatGPT probability is within 2pp of the model's.
Material disagreement with Kalshi = |ChatGPT - Kalshi mid| >= 5pp.

## Factor tags and expressions

Tags: SERVE_EDGE, RETURN_EDGE, SURFACE_FIT, PLAYER_FORM, FATIGUE, TRAVEL, SCHEDULING, INJURY,
MATCHUP_STYLE, LEFTY_RIGHTY, TIEBREAK_PROFILE, BREAK_POINT_PROFILE, OPPONENT_QUALITY, TOURNAMENT_CONTEXT,
MOTIVATION_CONTEXT, EXTERNAL_MARKET_CONFIRMATION, MARKET_OVERREACTION, MARKET_UNDERREACTION,
MODEL_DISAGREEMENT, PRICE_VALUE, DERIVATIVE_VALUE, LIQUIDITY, OTHER. Multiple allowed; none is fine.

Expressions: MATCH_WINNER, SET_WINNER, GAME_SPREAD, TOTAL_GAMES, TOTAL_SETS, EXACT_SET_SCORE,
PLAYER_SET_HANDICAP (Kalshi SET_SPREAD), OTHER_SUPPORTED_KALSHI_MARKET (any-set winner, tiebreak).

## The slate

For every open match the first-ball store has not seen start: players, level, surface, scheduled time,
first-ball status and source coverage, every listed Kalshi market (bid/ask/size/spread/fee/age), Gen-1
(prediction ledger), Gen-2 and fair_v1 with its perturbation envelope (shadow board), Model 4 on listed
derivatives, serve evidence, serve-point/Elo rating state (hold/break follow from serve-point
probabilities through the DP engine; there is no separate hold/break model), recency/experience inputs
(the repo has no win-loss form model), surface-prior sensitivity, Bovada/Smarkets/consensus/triangulation
(external_v1 scan), model-minus-mid, model uncertainty, selector_v1 / external_v1 flags, frozen research
context (e.g. W3-001's ITF abstention), and data-quality warnings. Every model number is the frozen
producer's own output at its own prediction time. The slate ranks nothing as a bet.

## Discrepancy sanity layer (2026-10-01, decision schema v2)

**The model should usually sit close to an efficient market.** The value is a strong independent estimate so
that RARE, TRUSTWORTHY disagreements can be investigated. Small disagreement is normal, moderate may be
interesting, large needs an explanation, extreme is a diagnostic alarm until proven otherwise: "model 80%,
Kalshi 20%" first asks *why are we so different?* (`tennis_edge/assisted/discrepancy.py`, thresholds in
`config/discrepancy_sanity.json`). The layer never changes a model probability; it only labels how a gap may
be presented and what a BET on it must clear.

| band | gap | slate status | a BET needs |
|---|---|---|---|
| NORMAL | < 10 pp | OK | nothing extra |
| REVIEW | 10-15 pp | REVIEW_CONTEXT (context surfaced) | nothing extra |
| HIGH_REVIEW | 15-25 pp | EXPLANATION_REQUIRED_BEFORE_BET (DATA_WARNING if identity is not verified) | `discrepancy_explanation` |
| EXTREME | >= 25 pp | DATA_WARNING / PASS UNTIL RECHECKED | `discrepancy_explanation` and all nine conditions below; the record is then only ELIGIBLE_FOR_HUMAN_REVIEW |

EXTREME conditions (Part J): (1) identity verified, (2) ticker orientation verified, (3) FRESH (<= 10 min)
two-sided Kalshi price -- pass the live `kalshi_bid`/`kalshi_ask`, (4) ADEQUATE data quality, (5) no severe
sample asymmetry or `sample_asymmetry_justification`, (6) the external market supports the model's direction,
or it is unavailable/stale and `external_unavailable_reason` says why, (7) `why_market_may_be_wrong`,
(8) `why_model_may_be_wrong`, (9) ChatGPT's own side probability clears the side's ask plus the taker fee
and the ask is within `bet_up_to_price`. A BET whose identity or ticker orientation FAILED is refused at
any gap. Refusal codes: `DISCREPANCY_EXPLANATION_REQUIRED`, `DISCREPANCY_DATA_WARNING`. PASS and WATCH are
always admitted and carry the classification. The recorder measures the gap with the repository's own
model number for the contract, so a typed model probability cannot move it.

Every slate row carries `model_market_gap_pp`, `discrepancy_band`, `discrepancy_sanity_status`,
`discrepancy_reason_tags`, `identity_check_status`, `ticker_orientation_status`, `market_freshness_status`,
`external_confirmation_status`, `data_quality_status` and the full `discrepancy` block (evidence, identity
checks, EXTREME preconditions); `latest.md` shows a MODEL-MARKET GAP / BAND / FRESHNESS / DATA QUALITY /
EXTERNAL / IDENTITY column set and a `DISCREPANCY SANITY CHECK` block under every gap of 15 pp or more.

Reason tags (each backed by a measured value): STALE_KALSHI_QUOTE, ONE_SIDED_BOOK, WIDE_SPREAD,
LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, TICKER_SIDE_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY,
THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, SURFACE_DATA_THIN,
MODEL_HIGH_UNCERTAINTY, MODEL_CALIBRATION_OUTLIER, EXTERNAL_MARKET_CONFIRMATION, EXTERNAL_MARKET_REJECTION,
NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE (no first-ball source at HIGH_REVIEW+), SCHEDULED_START_PASSED,
MODEL_INTERNAL_DISAGREEMENT, UNKNOWN. Health: TENNIS-17 (`docs/PRODUCTION_HEALTH.md`). Evidence behind it:
`research/model_market_discrepancy/AUDIT.md` (rebuilt by RUN TENNIS into
`data/research/model_market_discrepancy/` on `tennis-data`).

## Scorecard and CEO scoreboard

`build_scorecard()` (primary unit = the decision; money = reported wagers) reports total decisions, actual
wagers (number, stake, wins, losses, pushes/voids, net P&L, ROI), pricing (strict executable CLV mean /
median / 95% CI, midpoint CLV), Brier of ChatGPT / model / Kalshi mid / external / each model input on the
same settled decisions, selective disagreement, agreement, overrides, model-follow, passes (hypothetical
model-side result of declined model edges), and breakdowns by expression, factor tag, level, surface and
confidence. The CEO scoreboard answers the ten questions; every answer is `INSUFFICIENT_EVIDENCE` below
N = 30 and none says "profitable" unless the 95% interval excludes zero. The bootstrap uses the
confirmation layer's fixed seed, so rebuilding on the same inputs reproduces every number.

## TENNIS-16 `assisted_decision_pipeline_health`

Operations, not profitability. Reports latest slate build, latest assisted decision, settlement freshness,
unsettled decisions, strict CLV coverage, schema validity, duplicates, post-start decision violations,
integrity violations. FAIL on: slate or pipeline older than 13 h, a pipeline error newer than its last
success, a broken fingerprint/chain, an invalid or duplicated decision, a post-start decision in the last
7 days, a decision unsettled after 7 days, a modified TRACK_START. UNKNOWN until the first production run.
Zero decisions is `HEALTHY_NO_DECISIONS_YET` (PASS).
