# Edge Finder app export (TENNIS)

`scripts/app_export.py` (thin CLI) over `tennis_edge/app_export.py` (pure adapter) maps what this repository
already produces onto the vendored app contract `contract/edge_finder_contract` (`edge_finder.app.v1`) and
publishes it atomically. It is an infrastructure pass: no model, threshold, selector, staking rule, authority or
promotion status is touched, and the exporter reads no credential of any kind.

```
python scripts/app_export.py --out data/app/latest [--data-root data] [--accounting-dir <accounting-data checkout>]
                             [--now <iso with zone>] [--commit-sha X] [--workflow-run-id Y]
```

## Where the app reads it
`contract/edge_finder_contract/registry.json`: repo `chmoses98/Tennis-Edge-Finder`, branch **`tennis-data`**, app root
**`tennis-edge-finder/data/app/latest`**. The exporter writes `data/app/latest` in the workflow's working tree and
`scripts/ci/publish_branch.py --src data/app` carries it under the branch's historical `tennis-edge-finder/` prefix,
exactly like `data/research`. `data/app/` is gitignored on `main`.

Files: `manifest.json`, `events.json`, `markets.json`, `model_prices.json`, `recommendations.json`, `theses.json`
(always empty), `wagers.json`, `settlements.json`, `runs.json`, `board.json`, `performance.json`, `health.json`,
`event_detail/<event_id>.json` (one per event on the board).

## Sources (data-root relative) and mapping
| object | source | notes |
|---|---|---|
| run | `research/assisted_slates/latest.json` | `native_run_id` = `slate_id`; `completed_at` = slate `built_at`; `model_version` = `assisted_slate_v2`; `commit_sha` = `--commit-sha`, else the newest `frozen_producers/heartbeats.jsonl` `code_sha`, else `PIPELINE_STATUS.json` `code_sha` |
| events | slate `matches[]` | one per match packet (see identity) |
| markets | slate `matches[].markets[]` | every listed contract, prices in dollars straight from `kalshi.{bid,ask,no_ask}`, `captured_at` = `quote_captured_at`, `market_status` OPEN (the slate only lists open, not-started contracts) |
| model prices | slate rows with `model_probability_yes` | PRIMARY = the slate's own `model_probability_yes` / `model_probability_source` (fair_v1 shadow board, else Model 4 market_conditioned_v1, else Gen-1); `lower/upper` only from `fair_v1_envelope`; `uncertainty` null (never fabricated); secondary numbers (`gen1`, `gen2`, `model4_*`, `model_side_edges`, discrepancy fields) in `extensions`; `generated_at` = slate `built_at`, `inputs_as_of` = quote capture time; `data_quality_status` maps the slate's own data label (ADEQUATE -> OK, LIMITED/POOR -> DEGRADED, else UNKNOWN); `support_status` = `discrepancy_sanity_status`. Doubles / unmapped rows have no model price (no frozen producer speaks for them). |
| recommendations (a) | `research/assisted_decisions/records/decisions/**` (`AD-...`) | the human/ChatGPT decisions: BET -> `RECOMMENDED` (`research_only=false`), PASS -> `PASS`, WATCH -> `WATCH`; `authority=ASSISTED`; `native_id` = `decision_id`; `fair_probability`/`current_price` for the SELECTION (`chatgpt_fair_probability` is P(YES), converted when the side is NO); a decision on a match that has left the slate gets a market stub and, if needed, an event built from the record. None exist yet. |
| recommendations (b) | slate rows | **research-only candidates, not picks**: `discrepancy_band` in REVIEW / HIGH_REVIEW / EXTREME (the bands `config/discrepancy_sanity.json` already defines; NORMAL and UNPRICED are not disagreements) AND `model_preferred_side` in YES/NO AND `start.bet_allowed`. `status=RESEARCH_CANDIDATE`, `authority=RESEARCH_ONLY`, `research_only=true`, selection = `model_preferred_side`, edge = the slate's fee-adjusted `model_side_edges[selection]`, `native_id` = `slate_id|ticker|side`. A row whose own sanity status is `DATA_WARNING` ("PASS UNTIL RECHECKED": EXTREME band or a hard identity/orientation fault) is `NOT_PLAYABLE` with the slate's display status as `reason_not_playable`. |
| theses | none | the repository produces no thesis prose for the slate; `summary` is never invented |
| wagers (routed) | `<accounting-dir>/data/accounting/wagers.jsonl` | `source=KALSHI_ROUTER`, identity from `source_bet_key`; settlements from `settlements.jsonl` (`result` None with established money -> `SCALAR`); a market no longer listed gets `market_stub` |
| wagers (assisted) | `research/assisted_decisions/records/wagers/**` (`AW-...`) | `source=MANUAL`, `native_id` = `wager_id`, `external_order_id` / `decision_id` in `source_ids`; settlements from `assisted_settlements.jsonl` (`row_kind=WAGER`, highest revision), CLV only where the settler established a strict pregame close |
| health | `research/health_latest.json` (TENNIS-1..18), slate `built_at` / `refresh_due_by`, newest heartbeat, `PIPELINE_STATUS.json` | see below |

Every wager goes through `linkage.apply_links` (only model prices / recommendations that predate `placed_at`;
null otherwise, never the nearest).

## Identity
- `event_id` = `ids.event_id("TENNIS", "kalshi_event_ticker", <slate event_id>)`; `source_ids` carries `match_key`,
  `physical_match_id` (when the shadow board resolved one) and `match_code`.
- participants: `PLAYER`, namespace `kalshi_player_name`, source id = the whitespace-normalised, lower-cased player
  name the contract text names (the slate carries no Sackmann id at match level; `sackmann_id` will take over when
  it does). Each participant's match-winner ticker travels in its `source_ids`. `home/away` are null.
- `market_id` = `mkt_kalshi_<TICKER>`; `side=PARTICIPANT` with the player's `participant_id` when `subject_is_a` is
  a boolean, else null (totals, spreads, exact set scores).
- `start_time_utc` = `start.current_expected_start`, else the Kalshi nominal. `start_time_confidence`: a live
  schedule reading is `VERIFIED` (HIGH) / `ESTIMATED` (MEDIUM, LOW); a plain Kalshi nominal is `SCHEDULED`; a Kalshi
  day placeholder with nothing better is `PLACEHOLDER`. `status`: STARTED -> LIVE, NO_PLAY -> CANCELLED, else SCHEDULED.
- run id: deterministic from (sport, repo, `slate_id`, slate `built_at`); re-exporting the same slate (after a decision
  is recorded) keeps its run id. Two runs with the same inputs and `--now` are byte-identical.

## Freshness thresholds and authority
`bet_authority = ASSISTED` (a human decides from the slate; no automated placement exists). Thresholds travel in
`health.json`: market data FRESH <= 10 min, STALE > 30 min (the slate's own FRESH/AGING edges); model FRESH <= 6 h
(RUN TENNIS cadence), STALE > 13 h (TENNIS-16 fails at 13 h of slate age). `last_model_generated` = slate `built_at`,
`last_market_capture` = newest quote capture on the slate, `next_scheduled_run` = slate `refresh_due_by`. Failing
production gates are `warnings`; a failing TENNIS-16 (the assisted pipeline) is an `error` (overall DEGRADED).
Extra components: `assisted_pipeline` (PIPELINE_STATUS `last_run_at`), `frozen_producers` (newest heartbeat),
`assisted_pipeline_gate` (TENNIS-16).

## Failure path and workflow placement
Both `tennis-run.yml` (after "Project, settle, health") and `tennis-assisted-slate.yml` (after "Build the slate")
run the export BEFORE their publish step, and the publish step carries `data/app` to `tennis-data` right after
`data/research` / the slate. On any exception the exporter writes **`health.json` only** (export component DEGRADED,
`payload_run_id` = the last-known-good manifest's run), leaves every payload file byte-for-byte, and exits 1. The
workflow step records that (`APP_EXPORT_FAILED=1`, an `::error::` annotation) and a final step fails the job
**after** the publish, so a broken export can neither block the research/slate publication nor go unnoticed.
`|| true` is not used anywhere on this path. When the branch has no payload yet, health is UNAVAILABLE.

## Tests
`tests/test_app_contract_v1.py` (fixtures carved from real tennis-data records): vendored contract intact, end-to-end
export + `verify_published`, determinism, failure safety, stale health, naive timestamps refused, no secret-shaped
strings, routed + assisted wagers with settlements and ledger P&L totals, and a real-data smoke test that skips on
`main` (the slate lives on `tennis-data`; set `TENNIS_DATA_ROOT` to run it).

Real-data proof (tennis-data as of 2026-10-02T13:37Z, `--now 2026-10-02T13:45:00Z`): slate `SL-20261002T133719Z-11e40dc4`,
116 events, 471 markets, 264 model prices (138 fair_v1, 126 Model 4), 41 recommendations (33 RESEARCH_CANDIDATE,
8 NOT_PLAYABLE, all research-only), 0 wagers, health HEALTHY (kalshi AGING, model FRESH), `verify_published` = [],
`python -m edge_finder_contract validate <out>` OK, 3.1 MB.

## Known gaps
- No Sackmann player id reaches the slate's match packet, so participant identity is name-based (`kalshi_player_name`);
  namesakes are flagged by the slate's identity checks (carried in event extensions) but not disambiguated here.
- `publish_branch.py` copies files and never deletes, so `event_detail/` files of events that left the board remain on
  `tennis-data` beside the new manifest (they are not named by it and the app never reads them). A later pass could
  prune `tennis-edge-finder/data/app/latest/event_detail` on the branch before copying.
- The slate carries no thesis prose and no automated recommendation; `theses.json` stays empty by design.
- Health gates TENNIS-2/3/4/6/8/10 fail today for reasons documented in docs/PRODUCTION_HEALTH.md (taxonomy, coverage,
  leakage audit, truth reconciliation); they surface as warnings, not as export problems.
- `data_quality_status` on a model price maps the slate's player-sample label, not a producer-level input audit.

## Contract feedback
- `health.json` exposes a failed export only through `components.export` (status DEGRADED + detail); a top-level
  boolean would let a reader avoid string-matching the detail.
- The manifest `freshness` map is free-form per key; the exporter uses `kalshi` and `model`, which other sports should
  mirror for the registry UI.

## Explorer (research graph, contract 1.1.0)
`scripts/research_export.py` (thin CLI) over `tennis_edge/research_export.py` (pure adapter: `load_inputs` ->
`build_explorer` -> `export_explorer` = `research.publish_explorer`) publishes `app/latest/explorer/` beside the v1
files. It runs AFTER the v1 export with the same `--data-root/--out`; `run_id` is the v1 manifest's, `generated_at`
defaults to the v1 manifest's `generated_at` (the same `now`), `as_of` is the newest data timestamp read. It refuses
(exit 1, previous `explorer/` untouched) when the v1 export of the run failed or when the slate on disk is not the one
the v1 payload was built from. Stdlib only (the slate workflow installs nothing); no network; no model fitting.

```
python scripts/research_export.py --out data/app/latest [--data-root data] [--now <iso>] [--top-n 200] [--capture-days 3]
```

Workflows: in both `tennis-run.yml` and `tennis-assisted-slate.yml` the "App export + research export" step runs it as
its own command right after the v1 export (skipped when the v1 export failed), logs to the step summary, records a
failure as `RESEARCH_EXPORT_FAILED=1` with an `::error::research_export ...` annotation, and a final step fails the job
AFTER the publish (which carries `data/app`, explorer included). The slate workflow additionally pulls
`research/settlements/SCORECARD.md`, `research/candidate_confirmation` and yesterday's external dislocations; it
only has yesterday's and today's ledger/capture, so its per-ticker history is two days deep (RUN TENNIS has everything).

### What it publishes
| file | content | source |
|---|---|---|
| `players/<prt_>.json` | overall + per-surface Elo with match counts (ranked), structural serve/return abilities, serve-point evidence, last match date, ratings_as_of, authority RESEARCH_ONLY; for slate players also the current game, opponent, markets, v1 model prices and per-matchup serve-point probabilities | `processed/ratings_{ATP,WTA}.json`; ledger inputs; Model 4 |
| `rankings/<rnk_>.json` | Elo overall + Hard/Clay/Grass/Carpet, per tour (10 rankings) | rating state, arithmetic only |
| `events/<evt_>.json` | v1 event, matchup rows (player A in the `home` slot, B in `away`), v1 markets, v1 model prices (fair_v1 / Model 4 = RESEARCH), the ledger's six model numbers per ticker per run (projections + `extensions.ledger` with mid, quality grade, start basis, settlement outcome and strict CLV where present), Model 4 set-score / games distributions and fair_v1 envelopes (RESEARCH), surface, first-ball / start status + truth row, Bovada/Smarkets de-vigged vs Kalshi vs model | v1 payload, slate, `research/ledger`, `research/settlements`, `frozen_producers/model4`, `firstball/store/truths`, `research/external/dislocations` |
| `market_history/<evt_>.json` | every v1 ticker's Kalshi quote points (bid/ask/last/volume/OI, ~10-15 min) | `kalshi/capture/<day>/*.quotes.jsonl.gz`, now-3d..now |
| `series/<ser_>.json` | per-ticker ledger model fair (ELO_DP_FAIR), x = RUN; one series per match-winner pair (side B is the exact complement) | `research/ledger` |
| `metrics.json` | 18 metrics incl. settled Brier/log-loss/slope, strict CLV by family, Pinnacle benchmark + elo_study (RESEARCH) in `extensions` | `SCORECARD.md`, `CLV_SCORECARD.json`, `research/market_benchmark`, `research/elo_study` |

Identity: v1 participants keep their `kalshi_player_name` `prt_` ids (same `build.participant` call); the rating id is
attached as `source_ids.tennis_rating_id` (`ATP:104925`) only when the normalised full name identifies exactly one rated
player of the tour (the `identity/crosswalk.py` rule) and agrees with the slate's own player ids; otherwise the profile
keeps its v1 identity and carries no rating. Top-N players not on the slate use the `tennis_rating_id` namespace.
Universe (stated in every ranking's `filter`): slate players with a rating + the top 200 by overall Elo among players
whose last rated match is within 365 days of the ratings `as_of_date`. If `explorer/index.json` would exceed 300 KB the
top-N tail (never a slate player) is shrunk and a warning says so.

### Capabilities (audit 2026-10-03)
VERIFIED: raw_projections, market_prices, market_price_history (window-limited), game_markets, search.
PARTIAL: player_profiles, player_metrics, opponent_adjustment, situational_splits (surface), matchup_metrics,
event_research, rankings, comparisons, time_series, calibration, historical_accuracy, clv (limitations verbatim from
the audit: end-state ratings, sports truth 0%, TENNIS-10, first-ball coverage). RESEARCH: projection_distributions.
UNAVAILABLE (with reasons): team_profiles/metrics/game_logs, team_props (no teams); player_game_logs,
historical_results, opponents/H2H, usage, advanced_stats (the canonical `matches.parquet` is rebuilt per run and on no
branch; it is not rebuilt here); schedule_strength, recent_form_windows, lineups/draws, injuries, player_props,
play_by_play, weather, venue_effects beyond surface, wager_history (ledgers empty). A missing input in a run downgrades
its capability to UNAVAILABLE instead of claiming it.

### Sizes (tennis-data @ 23add39d9, slate SL-20261003T055612Z-8b35f7e8, `--now 2026-10-03T06:20:00Z`)
135 events, 607 player profiles (270 slate: 170 rated, 90 doubles pairs, 9 NO_CANONICAL_MATCH, 1 AMBIGUOUS_NAME),
10 rankings, 49 series, 135 market histories (17,895 quote points), 18 metrics; `research.tree_bytes`:
players 5,824,150 · market_history 3,271,669 · events 2,492,223 · rankings 551,026 · index.json 295,301 ·
search_index.json 269,249 · series 82,171 · metrics.json 46,865 · capabilities.json 17,878 (12.9 MB total). Largest
files: profile 19.0 KB, event 36.1 KB, market history 204.5 KB, ranking 64.0 KB. Build 4.6 s; `verify_explorer` = [],
every GAME packet validates with `quality.missing == []`.

### Deliberately not published
The canonical match table and anything derived from it (match logs, H2H, W-L, minutes, box serve stats); as-of rating
checkpoints and the elo_study per-match parquet files (no rating trajectories); the raw trade tape, books and candles;
official rankings (acquired, unused); doubles ratings (none exist; doubles ledger rows are RESEARCH). `publish_branch.py`
never deletes, so explorer files that left the index stay on `tennis-data` unreferenced (clients follow `index.json`).
