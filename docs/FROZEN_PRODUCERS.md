# Frozen producers (live since the 2026-09-28 deployment)

Five frozen candidates were UNSCORABLE because the probability each one decides on was never produced
after its freeze. This document describes the two producers that now write those probabilities live.
Neither producer contains, fits or modifies a model: `tests/test_frozen_producers.py` pins the sha256 of
every frozen model source (fair_v1, Gen-2, Elo, as-of states, Model 4, selector_v1, qualification,
external_v1, the DP engine, the contract pricer and the fee schedule) to the Wave 5 baseline `625bc55`.

Both run inside RUN TENNIS (`.github/workflows/tennis-run.yml`, cron `25 */6 * * *`), after
`run_tennis.py` and before settlement, the candidate harvest and the health gates. Real-money authority
is OFF; neither producer can express a wager.

## 1. Shadow board -- `shadow_board_v1`

| | |
|---|---|
| entrypoint | `scripts/ops/shadow_board.py` (the exact Wave 3 script; one run on 2026-09-12 17:13Z, then never scheduled) |
| serves | EC-2026-003-GEN2-MODERATE-EVIDENCE, W3-2026-001-ABSTAIN-ITF, W3-2026-002-NONITF-POSITIVE-EDGE |
| inputs | latest capture day's carry-forward quotes (`data/kalshi/capture`), walk-forward as-of states (`data/processed/asof`), rating registry for identity, canonical match table for surface, first-ball store |
| model | `compute_fair` (fair_v1, base config + the 13 frozen PERTURBATIONS), `qualify` (12 checks), `decide` (selector_v1) -- unchanged calls |
| runtime | ~15 s for ~240 contracts |
| outputs | `data/research/opportunities/<day>.jsonl` (the frozen Opportunity rows, unchanged schema); `data/research/frozen_producers/shadow_board/<day>.jsonl` (companion records, below); `data/research/frozen_producers/heartbeats.jsonl`; `data/research/shadow_board/SHADOW_BOARD.md` |
| versions | `fair_v1`, `gen2_dyn_hier_sr_v1`, `selector_v1`; Gen-1 = fair_v1 MODEL_1 Elo (walk-forward, base config) |

Companion record (one per contract side, append-only, hash-chained, fingerprinted), written AT
PREDICTION TIME: `predicted_at`, `physical_match_id`, `event`, `ticker`, family/side/strike, `subject`,
`tour`, `level`, competition, surface, format, match date, both player ids, `gen1_elo_probability`,
`gen1_sr_probability`, `gen2_probability`, `gen2_blend_probability` (= `fair_v1_probability`),
`blend_weight`, serve evidence of each player and `thinner_serve_points`, the full perturbation envelope,
`model_uncertainty`, the 12-check `qualification` and `qualification_ok`, `selector_decision`,
fee-adjusted/robust/raw edge, Kalshi bid/ask/mid/spread, fee, displayed size, quote timestamp and age,
identity confidence (each side), data quality, model versions, as-of base date, `code_sha`, opportunity id
and fingerprint.

## 2. Model 4 board -- `model4_board_v1`

| | |
|---|---|
| entrypoint | `scripts/ops/model4_board.py` (new wrapper; the model is `tennis_edge/models/market_conditioned.py`, unchanged) |
| serves | EC-2026-001-MKTCOND-EXACT-SCORE, EC-2026-002-MKTCOND-GAME-SPREAD |
| universe | ONLY contracts Kalshi lists: active EXACT_SET_SCORE, GAME_SPREAD and TOTAL_GAMES contracts on singles matches with a mapped match-winner pair. A match with no listed derivative writes nothing. |
| fundamental lane | Gen-2 point probabilities from the as-of artifact (its frozen Gen-2 config, = fair_v1 base), `match_distribution` |
| conditioned lane | `conditioned_distribution(p_market, gen2_pa, gen2_pb, fmt)`; p_market = proportional de-vig of the two match-winner YES asks (the Kalshi analogue of the study's de-vigged bookmaker offer prices), fixed before any prospective outcome; bids and mids stored beside it |
| contract prices | `tennis_edge.pricing.payoffs.price_market` on each distribution |
| orientation | derivative rules text (full names) must match the match-winner text (surnames) side for side; otherwise refused, never flipped |
| runtime | seconds |
| outputs | `data/research/frozen_producers/model4/<day>.jsonl`; heartbeat |

Record fields: `predicted_at`, `physical_match_id`, `match_code`, ticker, family, line / exact score,
`model_version` (`market_conditioned_v1`), `fundamental_version` (`gen2_dyn_hier_sr_v1`), both contract
probabilities, both distributions' set-score maps, expected game differential and total games, Gen-2
point probabilities and evidence, the conditioning quote (asks, bids, two-sidedness, de-vig method,
p_market, its capture timestamp, service level), Kalshi bid/ask/spread/fee/displayed sizes and quote
timestamp, first-ball status at prediction, `code_sha`.

## Chronology protections (both producers)

* Ratings: `AsOfStates.state(pid, on)` / `gen2_state(pids, on)` return what was known the morning of the
  match date; no later result can reach a prediction.
* Market: quotes are the capture's own records, each with its capture timestamp; the conditioning quote's
  timestamp is stored.
* Started matches: `tennis_edge/firstball/started.py` refuses every series of a physical match the
  first-ball store has already seen start (any confidence; refusing is the conservative direction).
* Timing is re-derived at harvest time from first-ball truth; confirmed POST_START / AMBIGUOUS rows are
  never evidence, and strict CLV uses A/B truth only.

## Experiment-start records

`data/research/experiment_starts/<candidate>.json`, written ONCE by the producer's first production run
(`tennis_edge/producers/records.py::ensure_experiment_starts`), never rewritten, fingerprinted. Fields:
candidate_id, original_frozen_at, original_confirmation_start, producer_missing_period_start/end,
effective_scorable_start, model_version, producer, producer_version, activating_main_sha, timing
admission, reason the prior period is UNSCORABLE. The original candidate JSON is not touched. The
interval [original confirmation_start, effective_scorable_start) is permanently UNSCORABLE.

Decision units, fixed at experiment start and before any outcome: W3 = the FIRST observation of each
contract (the discovery set priced each contract once at a fixed cutoff); EC-003 = the first observation
of each physical match (side A for Brier; the positive-edge side, if any, for CLV/EV); EC-001/002 = the
first prediction run of each physical match. Sports truth for EC-001/002 = the one completed match between
the two players in the canonical table (retirements and ambiguous pairings excluded).
