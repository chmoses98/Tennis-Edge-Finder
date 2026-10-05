# Projection pipeline audit (2026-10-05)

Performed before any code was changed, on `main` @ `4bd491d` (the SHA RUN TENNIS #98 and #99 ran) and
`tennis-data` @ `5b4603e`. Findings were recorded as they were made; this file collects them. Each item is
marked with what was done about it in this branch.

## Reproduced baseline

| claim | reproduced |
|---|---|
| ATP all-level walk-forward (eval 2015+, n = 321,480): elo_levelprior Brier 0.2000, elo_plain 0.2001, production elo_surface_k_lo 0.2042 | **exactly** (`scripts/research/elo_study.py`, Sackmann rows) |
| WTA (n = 299,185): 0.1933 / 0.1936 / 0.2004 | **exactly** |
| RUN TENNIS #98: success on 4bd491d, 32 min (pull 8 min, build 5, project/settle 5, publish 13.5) | yes (job timings from the Actions API) |
| Health after #99: TENNIS-2,3,4,5,6,8,10 FAIL, TENNIS-9 UNKNOWN; TENNIS-4 344 projectable / 248 projected / 96 not | yes (`health_latest.json` on tennis-data) |
| Test suite | 661 passed, 1 skipped |
| Canonical build | 1,631,376 rows through 2026-10-04 (hash differs from #99's only because a newer source snapshot landed after it) |

## Correct (kept)

* Walk-forward replay discipline in the Elo/Gen-2 code: predictions are read before the update.
* Gen-2's opponent adjustment and point orientation (`pb = P(A wins a point on B's serve)`), its evidence
  shrinkage, level offsets and surface deviations.
* The exact DP scoring engine for every format in live use (verified against a vectorised re-implementation
  to 1e-9).
* Fail-closed identity (exact names, compound-surname rule, human-reviewed aliases only).
* Append-only, hash-chained ledger and evidence stores; frozen candidates and producers.
* Market-free import graph of the fundamental lanes.

## Objectively broken (fixed)

| # | defect | evidence | fix |
|---|---|---|---|
| 1 | **85,008 duplicate matches** in the canonical table: exact-key dedupe cannot see the same match dated differently by two id systems (TML Challenger = tournament end, Sackmann = start; ESPN = match day, "Round 2") | 80,481 TML Challenger rows duplicated Sackmann (99.6% identical scores); 16,165 duplicates inside the 2021-2025 ATP evaluation window alone; double-counted rating updates, and second copies "predicted" after their own result | `tennis_edge/data/dedupe.py` |
| 2 | **Production priced markets the exchange had already settled** | 2,695 of 17,296 settled ledger rows (15.6%) generated after Kalshi's settlement timestamp, still occurring daily; root cause: incremental capture never marks a market closed and run_tennis trusted the last record | full open snapshot before pricing, captured settlements excluded, stale records cannot vouch; TENNIS-6 now detects the class |
| 3 | **TENNIS-6 could not see post-start pricing below tour level** (no first-ball source) | the 2,631 post-settlement rows above passed it | exchange settlement time used as a hard upper bound on the first ball |
| 4 | **Every assisted slate row STALE** | 475/475 rows on the #99 slate; capture cadence slipped to 20-80 min because every pass fetched and checked out the whole 8 GB evidence branch | blobless sparse publish and pulls; fresh open snapshot before the slate; stale-slate refresh dispatch |
| 5 | Mirror ATP main-tour files never loaded | ATP main-tour serve stats stopped in May though the mirror has them to 09-29 | loaded |
| 6 | New players (not in Sackmann) never rated | 244 TML + 111 ESPN foreign-only players excluded from every rating | guarded minting |
| 7 | `KXATPT5RANK` unknown series (TENNIS-2/3) | new series 2026-10-01 | classified SEASON_RANKING (unpriced) |
| 8 | Frozen engine: advantage-set tail truncation uses `1 - P(break)` | up to ~0.04 on set probability with two strong servers | not fixed in place (frozen source); all affected formats ended 2021; documented and tested around |
| 9 | Settlement "sports truth" was Kalshi's own result | 13,364 rows `source: kalshi_result`; TENNIS-9 permanently UNKNOWN | independent lane from Sackmann / TML / ESPN; reconciliation |
| 10 | `match_key` not unique across source files | 166,044 colliding rows in v1 (WTA main vs qual/ITF, TML vs Sackmann) | replay uses a source-qualified uid; noted for joins |

## Questionable (changed with evidence)

* **Production Elo configuration** (k0 180 + surface + level K): worst of 15 variants on 2016-2020 on both tours,
  badly under-confident on WTA (calibration slope 1.37), slow on ITF. Replaced only through the preregistered
  promotion.
* **Gen-1 structural model** in the production ensemble: adds nothing once Gen-2 is weighted by evidence (dropped
  by the selection rule).
* **Surface lookup for live events** (`pricing/competition.py::lookup_surface`) falls back to "any token
  matches", which can borrow another event's surface. Left as is (it only nudges a 0.25-weight surface rating);
  listed as a limitation.
* **ESPN level labels** (WTA 125 events labelled 250/500, Rome / Montreal as 500): affects 2026 segment reporting
  and level priors for new players; listed as a limitation, not hand-patched.
* **TENNIS-10 denominator** counted rows priced after the first ball as "missing a pregame close"; those rows are
  now in the quarantine register and reported separately (threshold unchanged).

## Lacking evidence (not changed)

* Rankings as a feature (no current free rankings feed for live inference).
* Travel, time zones, altitude, weather, indoor/outdoor, round-of-event fatigue beyond what the context block
  measures: no reproducible historical source.
* Injury news: no source that can be reproduced historically without leakage; kept out of the fitted model.

## Should not be changed

* Frozen prospective candidates, producers and their sources (`tests/test_frozen_producers.py`).
* The append-only evidence on `tennis-data` (nothing deleted; legacy violations quarantined by id).
* The evidence branch prefix `tennis-edge-finder/`.
* Real-money authority (OFF).
