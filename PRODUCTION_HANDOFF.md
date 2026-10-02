# Production handoff (2026-09-28)

**Real-money authority: OFF.** No candidate is eligible for CEO review. No frozen model, threshold,
inclusion rule, minimum N, pass condition, freeze timestamp or candidate definition was changed (sha256 of
every frozen model source and all seven candidate JSONs pinned in `tests/test_frozen_producers.py`). No
historical Gen-2, fair_v1 or Model 4 probability was reconstructed.

## 2026-10-02 update: start-time reconciliation and RUN TENNIS timing

Six WTA Beijing matches had started before the handicapping run because (1) the first-ball watchlist came from
a daily discovery snapshot that predated their listing, (2) Kalshi's 06:00Z time was a day placeholder for all
27 matches, (3) a pregame-only first-ball truth was misread as a start bound, and (4) nothing planned the next
window. Now: every slate match carries a reconciled START STATUS (truth > live state > ESPN live schedule >
court progression > Kalshi nominal), main-tour BETs need a live pending reading <= 30 min old, and the
first-ball conductor writes `firstball/store/schedule/NEXT_WINDOW.md` every ~10 min and dispatches the
assisted slate 45 and 10 min before the earliest credible first ball (a full RUN TENNIS first only when the
producer rows are > 3 h old). Decision schema v3. TENNIS-18 `start_time_window_health`. Full description and
verification steps: `docs/START_TIME_RECONCILIATION.md`. No model, probability, candidate, staking or authority
change; AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF.

**Where to look before handicapping:** `tennis-data` ->
`tennis-edge-finder/data/firstball/store/schedule/NEXT_WINDOW.md` (recommended RUN TENNIS time, final check
time, matches in the window) and the START STATUS block of each match in `assisted_slates/latest.md`.

## What landed on `main`

| PR | merge | content |
|---|---|---|
| #1 | `6787a83` | the prospective-confirmation audit (d0b28d9): harvester, settlement health, order-book parsing, trade-tape continuation, Laver Cup taxonomy, post-start guard, evidence store |
| #2 | `ca241d0` | frozen producers live (shadow board, Model 4), write-once experiment starts, live harvesters, TENNIS-15, sibling strict-CLV view, weekly MATCH_WINNER baseline, EC-004 economics |
| #3 | `d6e9763` | fix for the Model 4 truth-join crash that TENNIS-15 caught in production; per-candidate harvest isolation |

No PR had CI checks (the repository has no test workflow); each was verified locally (461 tests) and then in
production.

## Production evidence (GitHub Actions + `tennis-data`)

* RUN TENNIS #65 (`ca241d0`, dispatched 03:20Z), #66 (`ca241d0`, scheduled 05:37Z), #67 (`d6e9763`, 12:40Z):
  all `success`; each ran projections, both producers, settlement, the harvest and health, and published.
* The scheduled 11:25Z RUN TENNIS did not start (GitHub cron skipped/delayed it); #67 was dispatched instead.
* Capture conductor #149 on `ca241d0` since 03:20Z (the 01:24Z run on the old code was cancelled to deploy).
* Heartbeats (`frozen_producers/heartbeats.jsonl`): shadow board 03:33Z (260 rows), 05:46Z (314), 12:52Z (429);
  Model 4 03:33Z (0 -- every match with a listed derivative had started), 05:46Z (52 exact-score),
  12:53Z (245: 116 exact-score, 54 game-spread, 75 total-games).

## Experiment starts (write-once, `data/research/experiment_starts/`, activating `main` = `ca241d0`)

| candidate | original confirmation_start | effective scorable start | permanently UNSCORABLE |
|---|---|---|---|
| EC-2026-001-MKTCOND-EXACT-SCORE | 2026-09-12 06:30Z | 2026-09-28 03:33:38Z | 09-12 06:30Z -> 09-28 03:33:38Z |
| EC-2026-002-MKTCOND-GAME-SPREAD | 2026-09-12 06:30Z | 2026-09-28 03:33:38Z | 09-12 06:30Z -> 09-28 03:33:38Z |
| EC-2026-003-GEN2-MODERATE-EVIDENCE | 2026-09-12 06:30Z | 2026-09-28 03:33:22Z | 09-12 06:30Z -> 09-28 03:33:22Z |
| W3-2026-001-ABSTAIN-ITF | 2026-09-12 17:24:05Z | 2026-09-28 03:33:22Z | 09-12 17:24Z -> 09-28 03:33:22Z |
| W3-2026-002-NONITF-POSITIVE-EDGE | 2026-09-12 17:24:05Z | 2026-09-28 03:33:22Z | 09-12 17:24Z -> 09-28 03:33:22Z |

## Candidate status (harvest 20260928T125456Z)

| candidate | status | eligible / min N | settled | strict CLV | note |
|---|---|---|---|---|---|
| EC-001 exact score | INSUFFICIENT_N | 29 / 400 matches | 0 scored | n/a | listed contracts only |
| EC-002 game spread / totals | INSUFFICIENT_N | 25 / 400 matches | 0 scored | n/a | |
| EC-003 Gen-2 moderate evidence | INSUFFICIENT_N | 128 / 1000 | 20 | 0 | |
| EC-004 coherence (DISCOVERY_ONLY) | INSUFFICIENT_N | 3 / 10 | n/a | n/a | never a strategy |
| W3-001 abstain ITF | INSUFFICIENT_N | 66 ITF / 400 | 31 | n/a | abstention only |
| W3-002 non-ITF positive edge | INSUFFICIENT_N | 73 / 600 | 10 | 0 | accuracy condition binding |
| W4 Kalshi lone outlier | INSUFFICIENT_N | 1 / 200 | 1 | 1 | first observation per contract |

Nothing here is a finding: every candidate is far below its frozen minimum. The early settled numbers are
recorded in the reports and must not be read.

## Health

TENNIS-15 PASS; every candidate's producer active. The 05:46Z harvest failure (a `datetime.date` vs
`Timestamp` comparison in the EC-001/002 truth join, first reached when Model 4 had rows) was surfaced by
TENNIS-15 as HARVEST_FAILED, fixed in #3, and cleared by the 12:56Z success. TENNIS-5 PASS (trade backlog
0). TENNIS-6 FAIL on the 330 historical post-start rows only: 570 ledger rows since deployment, 0 new
violations, 0 post-start rows in strict research. TENNIS-4 FAIL: 38 newly listed ITF/Challenger contracts
whose players have no exact identity mapping (pre-existing identity coverage, not this work). TENNIS-8
FAIL / TENNIS-9 UNKNOWN: no exchange-independent sports truth in the settle job. TENNIS-10 FAIL: 86%
strict close coverage on the exact join.

## Evidence pipeline

* Sibling strict-CLV view (`clv_physical_join/`, join version 1, canonical physical match id): strict rows
  2,312 -> 2,914; 671 rows given a sibling truth, 602 recovered strict (TOTAL_GAMES 528, SET_WINNER 46,
  GAME_SPREAD 18, TOTAL_SETS 4, EXACT_SET_SCORE 4, MATCH_WINNER 2); 217 set/game-leg truth sources refused.
  The exact-join history is untouched.
* Trade tape: first new pass 03:24:37Z; 33 passes on the new code, 0 incomplete, 0 abandoned gaps, the
  queued 19 minutes drained by 03:59Z, contiguous new windows, <= 250 pages and <= 240 s per pass. The 54
  historical windows (~2.75 h) stay missing and were not reconstructed.
* MATCH_WINNER strict CLV, one decision per physical match: N 270, -1.62c, 95% CI [-2.78c, -0.52c]
  (W37 -5.69c n=35; W38 -1.12c n=113; W39 -0.92c n=122). Descriptive only.
* Laver Cup: parsed, never priced (no authoritative scoring format).
