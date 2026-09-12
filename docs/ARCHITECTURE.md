# Architecture

Repository: `chmoses98/tennis-edge-finder` (standalone since the 2026-09-11 migration; it was built inside
`chmoses98/nfl-edge-finder` overnight — see MIGRATION_AUDIT.md). Code lives at the repository root; the orphan
`tennis-data` branch keeps its original `tennis-edge-finder/data/...` prefix so every pre-migration evidence
commit kept its ORIGINAL SHA.

```
GitHub Actions runner (open internet)                      dev sandbox / owner machine (egress-restricted)
┌──────────────────────────────────────────┐              ┌──────────────────────────────────────────────┐
│ tennis-bootstrap.yml  (daily + dispatch) │              │ tennis_edge/data/build.py  -> matches.parquet │
│   scripts/data/bootstrap_sources.py      │  git fetch   │ tennis_edge/models/state.py -> ratings_*.json │
│   scripts/kalshi/discover_tennis.py      │ ───────────► │ scripts/run_tennis.py -> projections + ledger │
│ tennis-capture.yml (self-chaining loop)  │  tennis-data │ scripts/research/*  -> RESULTS_*.md           │
│   scripts/kalshi/capture_tennis.py       │   branch     │ tennis_edge/health/gates.py -> TENNIS-1..14   │
│ tennis-firstball.yml (self-chaining)     │              │ scripts/ops/settle_ledger.py -> timing, CLV,  │
│   scripts/firstball/poll_first_ball.py   │              │   horizons, segmented coverage                │
└──────────────────────────────────────────┘              └──────────────────────────────────────────────┘
```

Immutable evidence lives on the orphan `tennis-data` branch (`tennis-edge-finder/data/sources/<run>/`,
`data/kalshi/discovery/<run>/`, `data/kalshi/capture/<day>/<run>.*.jsonl.gz`); code lives on the code branch;
nothing under `data/` is committed to `main` except the small research artifacts that were committed before the
migration (ledger, projections, settlements, health snapshot) and are preserved as-is.

## Layers (tennis_edge/)
| package | role |
|---|---|
| `kalshi/` | read-only API client; series taxonomy classifier; family registry; market parser (rules text -> payoff) |
| `data/` | gz/xlsx readers; Sackmann/TML normaliser + validation/quarantine; tennis-data odds loader + vig removal; multi-source builder with provenance |
| `identity/` | name normalisation; player registry + alias table; tennis-data ↔ canonical linking with confidence; Kalshi competitor mapper (fail closed) |
| `rules/` | score parser; match formats + data-driven registry (config/formats.json) |
| `sim/` | exact DP engine (game/tiebreak/set/match distributions, inversion); Monte Carlo validator |
| `models/` | Elo family; structural serve/return; production state fitter; data-quality score |
| `pricing/` | payoff pricing from one distribution; consistency invariants; fees; competition/level/surface inference |
| `futures/` | exact bracket DP for tournament winner / round advancement |
| `doubles/` | team identity + baseline interface (explicitly unvalidated) |
| `ledger/` | append-only hash-chained prediction ledger; SportsTruth / ExchangeTruth; executable quote timelines; first-ball-anchored canonical close; CLV v2 |
| `firstball/` | ACTUAL first-ball truth: source catalogue and prober, live-score adapters, fail-closed match mapping, multi-source reconciliation, immutable hash-chained store, timing classification, canonical decision horizons, adaptive watchlist |
| `eval/` | proper scores, calibration, paired bootstrap |
| `health/` | gates TENNIS-1..14 |

## One universe, many payoffs
`run_tennis` builds, per match, ONE `MatchDistribution` from point-win probabilities (inverted from the
ensemble match probability with the tour/surface serve baseline) and prices every family on that event as a
functional of it; `check_consistency` enforces winner = sum of exact-score paths, monotone ladders, set-mass
constraints. Tournament markets reuse the same matchup function through the bracket DP.

## Automated settlement flow (designed; parts pending external feeds)
DISCOVER MATCH (discovery/capture) → CAPTURE MARKETS (10-min quotes/books, global trade tape) → GENERATE
PREGAME PROJECTIONS (run_tennis, ledger) → DETECT ACTUAL START (**needs live-score feed; interface in
ledger/close.py**) → FREEZE PREGAME CORPUS → DETECT FINAL RESULT (Sackmann/TML refresh, Kalshi
expiration_value as secondary) → INGEST SPORTS TRUTH → INGEST KALSHI TERMINAL SETTLEMENT (capture
settlements stream) → SELECT CANONICAL CLOSE (candles/quotes before cutoff) → SCORE MODEL → CLV → REPORTS.


## Wave 3: the selective layer

```
capture / discovery ──► fair.py ──────────────► Opportunity ──► qualify_v1 ──► selector_v1 ──► PASS
   (prices, depth)      (13 configs, no          (immutable,      (12 hard        (7 gates)     WATCH
                         prices as inputs)        fingerprinted)   filters)                     SHADOW_BET
        ▲                    ▲                         │
        │                    │                         ▼
   asof_<tour>.json.gz   ratings + Gen-2        data/research/opportunities/
   (walk-forward, read   state per checkpoint    (append-only, hash-chained)
    strictly before D)
```

`tennis_edge/models/fair.py` is the single place a fair probability is computed, so the research pipeline
and the live board cannot drift apart. It imports nothing that touches prices; `tests/test_gen2.py` walks
the import graph and fails if Model 3 can reach a price-bearing module.

`tennis_edge/models/asof.py` exists because the production rating artifact is an END state, and scoring a
July market with it would let July inform July. A market on day D reads the last checkpoint strictly before
D -- before the DATE, not the timestamp, so a player who plays twice in a day contributes neither match.

`tennis_edge/selector/model.py` enforces the chronology in code: fitting outside the declared window
raises, and fitting a frozen selector raises. There is no flag to turn either off.
