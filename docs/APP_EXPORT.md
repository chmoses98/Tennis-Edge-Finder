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
