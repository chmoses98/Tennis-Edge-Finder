# ASSISTED SLATE -- 2026-10-17T15:15Z (`SL-20261017T151534Z-63507a30`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

146 open matches not seen started, 721 markets. Skipped: {"first_ball_already_observed": 1}. Sources: shadow board 2026-10-17T12:27:40.206104+00:00, Model 4 2026-10-17T12:27:55.599924+00:00, Gen-1 ledger 2026-10-17T12:27:36.916356+00:00, external 2026-10-17T15:02:03.868675+00:00, capture 20261017T150022Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-18 02:30Z**
* Recommended RUN TENNIS time: **2026-10-18 01:45Z**
* Final price/status check time: **2026-10-18 02:20Z**
* Number of matches in window: 8 (Maya Joint vs Kayla Day, Taylah Preston vs Emerson Jones, Mary Stoiana vs Sayaka Ishii, Daria Snigur vs Katarzyna Kawa, Anastasia Zakharova vs Polina Kudermetova, Harriet Dart vs Aoi Ito ...)

* **22 main-tour match(es) have NO verified start status** (START_UNKNOWN, STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-10-17T15:15Z. Refresh due by: 2026-10-18 01:45Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 34, "HIGH_REVIEW": 60, "NORMAL": 256, "REVIEW": 95, "UNPRICED": 276}; match winners: {"EXTREME": 17, "HIGH_REVIEW": 17, "NORMAL": 64, "REVIEW": 26, "UNPRICED": 168}; quote freshness at build: {"FRESH": 445}.

## Nishesh Basavareddy vs Edas Butvilas -- ATP Brussels Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-17 15:50Z
* Current expected start: 2026-10-17 13:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-17 12:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-17T15:50:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:210220:210460:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nishesh Basavareddy (`KXATPMATCH-26OCT17BASBUT-BAS`) | 0.56 / 0.57 (18992) | 56.5% | 52.3% | 42.0% | 50.0% [47.0%-54.0%] | 62.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Edas Butvilas (`KXATPMATCH-26OCT17BASBUT-BUT`) | 0.43 / 0.44 (36355) | 43.5% | 47.6% | 58.0% | 50.0% [46.0%-53.0%] | 37.7% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +4.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2705.0, B 3824.0; serve-point win A 63.5%, B 36.9%; Elo A 1737.5, B 1636.2; model uncertainty 0.035
* Form inputs: days since last match A 12, B 12; matches on record A 142, B 231; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.025, surface_dev_loose -0.015, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT17BASBUT-BAS6` Will Nishesh Basavareddy win at least 5.5 more games than Edas Butvilas?: 0.11/0.32 mid 21.5%, model 9.8% (projection_v2.0 (prediction ledger)) -- gap -11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17BASBUT-18` Over 17.5 games: 0.69/0.96 mid 82.5%, model 93.3% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17BASBUT-23` Over 22.5 games: 0.51/0.53 mid 52.0%, model 60.9% (projection_v2.0 (prediction ledger)) -- gap +8.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17BASBUT-BAS20` Will Nishesh Basavareddy win the Nishesh Basavareddy vs Edas Butvilas match by a set score of 2-0?: 0.32/0.35 mid 33.5%, model 26.6% (projection_v2.0 (prediction ledger)) -- gap -6.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17BASBUT-BUT21` Will Edas Butvilas win the Nishesh Basavareddy vs Edas Butvilas match by a set score of 2-1?: 0.16/0.19 mid 17.5%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17BASBUT-BAS3` Will Nishesh Basavareddy win at least 2.5 more games than Edas Butvilas?: 0.43/0.45 mid 44.0%, model 37.9% (projection_v2.0 (prediction ledger)) -- gap -6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17BASBUT-BUT2` Will Edas Butvilas win at least 1.5 more games than Nishesh Basavareddy?: 0.34/0.37 mid 35.5%, model 40.2% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17BASBUT-2-BAS` Will Nishesh Basavareddy win set 2 in the Nishesh Basavareddy vs Edas Butvilas match: 0.54/0.56 mid 55.0%, model 51.6% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17BASBUT-2-BUT` Will Edas Butvilas win set 2 in the Nishesh Basavareddy vs Edas Butvilas match: 0.44/0.46 mid 45.0%, model 48.4% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT17BASBUT-28` Over 27.5 games: 0.28/0.48 mid 38.0%, model 40.5% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17BASBUT-1-BUT` Will Edas Butvilas win set 1 in the Nishesh Basavareddy vs Edas Butvilas match: 0.45/0.47 mid 46.0%, model 48.4% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17BASBUT-BAS21` Will Nishesh Basavareddy win the Nishesh Basavareddy vs Edas Butvilas match by a set score of 2-1?: 0.22/0.25 mid 23.5%, model 25.8% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17BASBUT-1-BAS` Will Nishesh Basavareddy win set 1 in the Nishesh Basavareddy vs Edas Butvilas match: 0.53/0.54 mid 53.5%, model 51.6% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17BASBUT-BUT20` Will Edas Butvilas win the Nishesh Basavareddy vs Edas Butvilas match by a set score of 2-0?: 0.20/0.25 mid 22.5%, model 23.4% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kimmer Coppejans vs Andrea Guerrieri -- ATP Brussels Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-17 15:50Z
* Current expected start: 2026-10-17 13:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-17 12:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-17T15:50:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106293:200462:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kimmer Coppejans (`KXATPMATCH-26OCT17COPGUE-COP`) | 0.26 / 0.27 (56250) | 26.5% | 48.9% | 51.0% | 53.7% [50.5%-59.3%] | 41.7% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +22.4 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andrea Guerrieri (`KXATPMATCH-26OCT17COPGUE-GUE`) | 0.73 / 0.74 (26405) | 73.5% | 51.1% | 48.9% | 46.3% [40.7%-49.5%] | 58.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -22.4 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3531.0, B 2272.0; serve-point win A 57.5%, B 42.3%; Elo A 1610.3, B 1563.8; model uncertainty 0.0439
* Form inputs: days since last match A 9, B 19; matches on record A 840, B 345; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT17COPGUE-COP  (YES = Kimmer Coppejans)
Model: 49%
Kalshi: 26%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.031, surface_dev_loose -0.026, surface_dev_tight +0.021
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT17COPGUE-GUE4` Will Andrea Guerrieri win at least 3.5 more games than Kimmer Coppejans?: 0.51/0.54 mid 52.5%, model 31.1% (projection_v2.0 (prediction ledger)) -- gap -21.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17COPGUE-1-COP` Will Kimmer Coppejans win set 1 in the Kimmer Coppejans vs Andrea Guerrieri match: 0.26/0.31 mid 28.5%, model 49.2% (projection_v2.0 (prediction ledger)) -- gap +20.7 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT17COPGUE-GUE7` Will Andrea Guerrieri win at least 6.5 more games than Kimmer Coppejans?: 0.11/0.42 mid 26.5%, model 7.6% (projection_v2.0 (prediction ledger)) -- gap -18.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17COPGUE-1-GUE` Will Andrea Guerrieri win set 1 in the Kimmer Coppejans vs Andrea Guerrieri match: 0.67/0.71 mid 69.0%, model 50.8% (projection_v2.0 (prediction ledger)) -- gap -18.2 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17COPGUE-GUE20` Will Andrea Guerrieri win the Kimmer Coppejans vs Andrea Guerrieri match by a set score of 2-0?: 0.41/0.45 mid 43.0%, model 25.8% (projection_v2.0 (prediction ledger)) -- gap -17.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17COPGUE-COP2` Will Kimmer Coppejans win at least 1.5 more games than Andrea Guerrieri?: 0.23/0.34 mid 28.5%, model 42.1% (projection_v2.0 (prediction ledger)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17COPGUE-2-COP` Will Kimmer Coppejans win set 2 in the Kimmer Coppejans vs Andrea Guerrieri match: 0.35/0.40 mid 37.5%, model 49.2% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17COPGUE-2-GUE` Will Andrea Guerrieri win set 2 in the Kimmer Coppejans vs Andrea Guerrieri match: 0.61/0.64 mid 62.5%, model 50.8% (projection_v2.0 (prediction ledger)) -- gap -11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT17COPGUE-22` Over 21.5 games: 0.52/0.57 mid 54.5%, model 63.7% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17COPGUE-COP21` Will Kimmer Coppejans win the Kimmer Coppejans vs Andrea Guerrieri match by a set score of 2-1?: 0.14/0.17 mid 15.5%, model 24.6% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17COPGUE-COP20` Will Kimmer Coppejans win the Kimmer Coppejans vs Andrea Guerrieri match by a set score of 2-0?: 0.14/0.17 mid 15.5%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17COPGUE-17` Over 16.5 games: 0.73/0.99 mid 86.0%, model 94.4% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17COPGUE-27` Over 26.5 games: 0.30/0.40 mid 35.0%, model 40.3% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17COPGUE-GUE21` Will Andrea Guerrieri win the Kimmer Coppejans vs Andrea Guerrieri match by a set score of 2-1?: 0.25/0.26 mid 25.5%, model 25.4% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Amit Vales vs Giulio Perego -- M15 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-17T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211707:212280:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giulio Perego (`KXITFMATCH-26OCT17VALPER-PER`) | 0.50 / 0.51 (23810) | 50.5% | 43.3% | 53.1% | 50.0% [47.9%-51.0%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amit Vales (`KXITFMATCH-26OCT17VALPER-VAL`) | 0.49 / 0.50 (8615) | 49.5% | 56.7% | 46.9% | 50.0% [49.0%-52.0%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 397.0, B 0.0; serve-point win A 61.7%, B 39.6%; Elo A 1315.0, B 1314.2; model uncertainty 0.0154
* Form inputs: days since last match A 29, B 698; matches on record A 61, B 22; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martin Damm Jr vs Buvaysar Gadamauri -- ATP Brussels Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-17 17:00Z
* Current expected start: 2026-10-17 15:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-17 14:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-120_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-17T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:102093:207527:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Damm Jr (`KXATPMATCH-26OCT17DAMGAD-DAM`) | 0.85 / 0.86 (21435) | 85.5% | 56.3% | 46.6% | 56.2% [51.4%-66.0%] | 81.8% | 84.8% | 83.3% | KALSHI_LONE_OUTLIER | PASS | -29.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Buvaysar Gadamauri (`KXATPMATCH-26OCT17DAMGAD-GAD`) | 0.13 / 0.14 (13960) | 13.5% | 43.7% | 53.4% | 43.8% [34.0%-48.6%] | 18.2% | 15.2% | 16.7% | KALSHI_LONE_OUTLIER | PASS | +30.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3075.0, B 2063.0; serve-point win A 67.9%, B 33.4%; Elo A 1594.2, B 1460.3; model uncertainty 0.073
* Form inputs: days since last match A 726, B 12; matches on record A 252, B 234; data quality F

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT17DAMGAD-GAD  (YES = Buvaysar Gadamauri)
Model: 44%
Kalshi: 14%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.048, surface_pool_high +0.047, surface_dev_loose -0.005, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT17DAMGAD-DAM3` Will Martin Damm Jr win at least 2.5 more games than Buvaysar Gadamauri?: 0.72/0.82 mid 77.0%, model 39.0% (projection_v2.0 (prediction ledger)) -- gap -38.0 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT17DAMGAD-DAM20` Will Martin Damm Jr win the Martin Damm Jr vs Buvaysar Gadamauri match by a set score of 2-0?: 0.61/0.64 mid 62.5%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap -33.1 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGSPREAD-26OCT17DAMGAD-DAM6` Will Martin Damm Jr win at least 5.5 more games than Buvaysar Gadamauri?: 0.33/0.42 mid 37.5%, model 7.1% (projection_v2.0 (prediction ledger)) -- gap -30.4 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data POOR
  * `KXATPSETWINNER-26OCT17DAMGAD-2-GAD` Will Buvaysar Gadamauri win set 2 in the Martin Damm Jr vs Buvaysar Gadamauri match: 0.21/0.23 mid 22.0%, model 45.8% (projection_v2.0 (prediction ledger)) -- gap +23.8 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT17DAMGAD-1-GAD` Will Buvaysar Gadamauri win set 1 in the Martin Damm Jr vs Buvaysar Gadamauri match: 0.21/0.24 mid 22.5%, model 45.8% (projection_v2.0 (prediction ledger)) -- gap +23.3 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT17DAMGAD-2-DAM` Will Martin Damm Jr win set 2 in the Martin Damm Jr vs Buvaysar Gadamauri match: 0.76/0.79 mid 77.5%, model 54.2% (projection_v2.0 (prediction ledger)) -- gap -23.3 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT17DAMGAD-1-DAM` Will Martin Damm Jr win set 1 in the Martin Damm Jr vs Buvaysar Gadamauri match: 0.76/0.78 mid 77.0%, model 54.2% (projection_v2.0 (prediction ledger)) -- gap -22.8 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPGTOTAL-26OCT17DAMGAD-26` Over 25.5 games: 0.22/0.40 mid 31.0%, model 52.9% (projection_v2.0 (prediction ledger)) -- gap +21.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGTOTAL-26OCT17DAMGAD-21` Over 20.5 games: 0.57/0.60 mid 58.5%, model 79.1% (projection_v2.0 (prediction ledger)) -- gap +20.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT17DAMGAD-GAD21` Will Buvaysar Gadamauri win the Martin Damm Jr vs Buvaysar Gadamauri match by a set score of 2-1?: 0.05/0.10 mid 7.5%, model 22.7% (projection_v2.0 (prediction ledger)) -- gap +15.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGTOTAL-26OCT17DAMGAD-16` Over 15.5 games: 0.78/0.94 mid 86.0%, model 99.6% (projection_v2.0 (prediction ledger)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT17DAMGAD-GAD20` Will Buvaysar Gadamauri win the Martin Damm Jr vs Buvaysar Gadamauri match by a set score of 2-0?: 0.08/0.09 mid 8.5%, model 20.9% (projection_v2.0 (prediction ledger)) -- gap +12.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data POOR
  * `KXATPGSPREAD-26OCT17DAMGAD-DAM9` Will Martin Damm Jr win at least 8.5 more games than Buvaysar Gadamauri?: 0.01/0.24 mid 12.5%, model 0.3% (projection_v2.0 (prediction ledger)) -- gap -12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT17DAMGAD-DAM21` Will Martin Damm Jr win the Martin Damm Jr vs Buvaysar Gadamauri match by a set score of 2-1?: 0.18/0.24 mid 21.0%, model 26.9% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aziz Dougaz vs Tom Gentzsch -- ATP Brussels Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-17 17:00Z
* Current expected start: 2026-10-17 15:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-17 14:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-120_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-17T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144826:210167:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aziz Dougaz (`KXATPMATCH-26OCT17DOUGEN-DOU`) | 0.47 / 0.48 (42546) | 47.5% | 54.1% | 52.9% | 55.3% [52.4%-57.7%] | 46.8% | 48.6% | 47.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.6 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Tom Gentzsch (`KXATPMATCH-26OCT17DOUGEN-GEN`) | 0.52 / 0.54 (20072) | 53.0% | 45.9% | 47.1% | 44.7% [42.3%-47.6%] | 53.2% | 51.3% | 52.3% | MODEL_LONE_OUTLIER | PASS | -7.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2266.0, B 3256.0; serve-point win A 67.2%, B 33.6%; Elo A 1590.1, B 1527.2; model uncertainty 0.0262
* Form inputs: days since last match A 11, B 26; matches on record A 623, B 260; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.024, surface_dev_loose +0.019, surface_dev_tight -0.014
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT17DOUGEN-GEN4` Will Tom Gentzsch win at least 3.5 more games than Aziz Dougaz?: 0.32/0.35 mid 33.5%, model 20.6% (projection_v2.0 (prediction ledger)) -- gap -12.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17DOUGEN-GEN7` Will Tom Gentzsch win at least 6.5 more games than Aziz Dougaz?: 0.03/0.27 mid 15.0%, model 2.1% (projection_v2.0 (prediction ledger)) -- gap -12.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17DOUGEN-GEN20` Will Tom Gentzsch win the Aziz Dougaz vs Tom Gentzsch match by a set score of 2-0?: 0.33/0.35 mid 34.0%, model 22.4% (projection_v2.0 (prediction ledger)) -- gap -11.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17DOUGEN-23` Over 22.5 games: 0.53/0.54 mid 53.5%, model 65.0% (projection_v2.0 (prediction ledger)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17DOUGEN-18` Over 17.5 games: 0.74/0.98 mid 86.0%, model 96.0% (projection_v2.0 (prediction ledger)) -- gap +10.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17DOUGEN-28` Over 27.5 games: 0.33/0.36 mid 34.5%, model 44.0% (projection_v2.0 (prediction ledger)) -- gap +9.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17DOUGEN-DOU21` Will Aziz Dougaz win the Aziz Dougaz vs Tom Gentzsch match by a set score of 2-1?: 0.16/0.21 mid 18.5%, model 26.3% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17DOUGEN-DOU2` Will Aziz Dougaz win at least 1.5 more games than Tom Gentzsch?: 0.38/0.42 mid 40.0%, model 45.8% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17DOUGEN-2-DOU` Will Aziz Dougaz win set 2 in the Aziz Dougaz vs Tom Gentzsch match: 0.45/0.49 mid 47.0%, model 52.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17DOUGEN-2-GEN` Will Tom Gentzsch win set 2 in the Aziz Dougaz vs Tom Gentzsch match: 0.51/0.54 mid 52.5%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17DOUGEN-1-DOU` Will Aziz Dougaz win set 1 in the Aziz Dougaz vs Tom Gentzsch match: 0.46/0.50 mid 48.0%, model 52.7% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17DOUGEN-1-GEN` Will Tom Gentzsch win set 1 in the Aziz Dougaz vs Tom Gentzsch match: 0.50/0.54 mid 52.0%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17DOUGEN-GEN21` Will Tom Gentzsch win the Aziz Dougaz vs Tom Gentzsch match by a set score of 2-1?: 0.18/0.23 mid 20.5%, model 23.6% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17DOUGEN-DOU20` Will Aziz Dougaz win the Aziz Dougaz vs Tom Gentzsch match by a set score of 2-0?: 0.25/0.29 mid 27.0%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap +0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kypriotis / Nouchakis vs Nolan / Perego -- M15 Heraklion SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17KYPNOUNOLPER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kypriotis / Nouchakis (`KXITFDOUBLES-26OCT17KYPNOUNOLPER-KYPNOU`) | 0.20 / 0.63 (35) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nolan / Perego (`KXITFDOUBLES-26OCT17KYPNOUNOLPER-NOLPER`) | 0.29 / 0.73 (7) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Muller / Van Sambeek vs Walters / Wright -- M15 Heraklion SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17MULVANWALWRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Muller / Van Sambeek (`KXITFDOUBLES-26OCT17MULVANWALWRI-MULVAN`) | 0.34 / 0.37 (111) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Walters / Wright (`KXITFDOUBLES-26OCT17MULVANWALWRI-WALWRI`) | 0.63 / 0.64 (10) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Tiago Pereira / Benjamin Winter Lopez vs Milos Karol / Andrew Paulson -- ATP Challenger Maia F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-17T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17PERWINKARPAU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Milos Karol / Andrew Paulson (`KXATPCHALLENGERDOUBLES-26OCT17PERWINKARPAU-KARPAU`) | 0.52 / 0.55 (167) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tiago Pereira / Benjamin Winter Lopez (`KXATPCHALLENGERDOUBLES-26OCT17PERWINKARPAU-PERWIN`) | 0.44 / 0.48 (516) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Jacob Fearnley vs Luca Nardi -- ATP Challenger Olbia SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-17T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207985:208134:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacob Fearnley (`KXATPCHALLENGERMATCH-26OCT17FEANAR-FEA`) | 0.84 / 0.85 (33939) | 84.5% | 69.4% | 56.2% | 63.7% [60.8%-67.6%] | 66.4% | -- | 66.4% | KALSHI_LONE_OUTLIER | PASS | -15.1 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Luca Nardi (`KXATPCHALLENGERMATCH-26OCT17FEANAR-NAR`) | 0.15 / 0.16 (20643) | 15.5% | 30.6% | 43.8% | 36.2% [32.4%-39.2%] | 33.6% | -- | 33.6% | KALSHI_LONE_OUTLIER | WATCH | +15.1 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 4058.0, B 3056.0; serve-point win A 60.9%, B 43.0%; Elo A 1871.8, B 1659.3; model uncertainty 0.034
* Form inputs: days since last match A 19, B 12; matches on record A 178, B 346; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT17FEANAR-NAR  (YES = Luca Nardi)
Model: 31%
Kalshi: 16%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_MODEL
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.019, surface_dev_loose -0.019, surface_dev_tight +0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Nicolai Budkov Kjaer vs Matteo Martineau -- ATP Challenger Roanne SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-17T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149282:200188:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolai Budkov Kjaer (`KXATPCHALLENGERMATCH-26OCT17BUDMAR-BUD`) | 0.56 / 0.57 (31990) | 56.5% | 66.2% | 66.6% | 65.2% [63.0%-67.0%] | 68.8% | -- | 68.8% | KALSHI_LONE_OUTLIER | PASS | +9.7 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Matteo Martineau (`KXATPCHALLENGERMATCH-26OCT17BUDMAR-MAR`) | 0.43 / 0.44 (23468) | 43.5% | 33.8% | 33.4% | 34.8% [33.0%-37.0%] | 31.2% | -- | 31.2% | KALSHI_LONE_OUTLIER | SHADOW_BET | -9.7 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 3085.0, B 4114.0; serve-point win A 67.6%, B 35.9%; Elo A 1656.0, B 1566.6; model uncertainty 0.02
* Form inputs: days since last match A 19, B 19; matches on record A 143, B 540; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.009, surface_dev_loose +0.004, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Biletic / Kajin vs Juhas / Popovic -- M15 Bol F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17BILKAJJUHPOP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Biletic / Kajin (`KXITFDOUBLES-26OCT17BILKAJJUHPOP-BILKAJ`) | 0.44 / 0.47 (20) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juhas / Popovic (`KXITFDOUBLES-26OCT17BILKAJJUHPOP-JUHPOP`) | 0.49 / 0.56 (33) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alan Wazny vs Iannis Miletich -- M15 Bol SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-17T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211391:213048:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iannis Miletich (`KXITFMATCH-26OCT17WAZMIL-MIL`) | 0.13 / 0.14 (21469) | 13.5% | 76.9% | 43.9% | 66.9% [65.0%-68.8%] | 38.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +63.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alan Wazny (`KXITFMATCH-26OCT17WAZMIL-WAZ`) | 0.87 / 0.88 (12) | 87.5% | 23.1% | 56.1% | 33.1% [31.2%-35.0%] | 61.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -64.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 252.0, B 110.0; serve-point win A 58.3%, B 35.9%; Elo A 1217.0, B 1351.2; model uncertainty 0.0189
* Form inputs: days since last match A 33, B 684; matches on record A 7, B 37; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT17WAZMIL-MIL  (YES = Iannis Miletich)
Model: 77%
Kalshi: 14%
Gap: +63 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bernardo / Domingos vs Added / Faurel -- M25 Luanda F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17BERDOMADDFAU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Added / Faurel (`KXITFDOUBLES-26OCT17BERDOMADDFAU-ADDFAU`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bernardo / Domingos (`KXITFDOUBLES-26OCT17BERDOMADDFAU-BERDOM`) | -- / 0.01 (33017) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Korokozidi / Marie Voracek vs Herazo / Ogescu -- W35 Heraklion F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T19:00:40Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17KORMARHEROGE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Herazo / Ogescu (`KXITFWDOUBLES-26OCT17KORMARHEROGE-HEROGE`) | 0.26 / 0.32 (65) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Korokozidi / Marie Voracek (`KXITFWDOUBLES-26OCT17KORMARHEROGE-KORMAR`) | 0.65 / 0.71 (1) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Rafael Tosetto vs Joao Eduardo Schiessl -- M15 Maringa SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208006:210214:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Eduardo Schiessl (`KXITFMATCH-26OCT17TOSSCH-SCH`) | 0.91 / 0.92 (17208) | 91.5% | 78.8% | 52.0% | 72.2% [69.6%-73.8%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.7 pp | REVIEW | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rafael Tosetto (`KXITFMATCH-26OCT17TOSSCH-TOS`) | 0.08 / 0.09 (8695) | 8.5% | 21.1% | 47.9% | 27.8% [26.2%-30.4%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +12.7 pp | REVIEW | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 251.0, B 1048.0; serve-point win A 57.9%, B 35.9%; Elo A 1206.5, B 1397.9; model uncertainty 0.0212
* Form inputs: days since last match A 166, B 12; matches on record A 66, B 131; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ana Sofia Sanchez vs Luna Maria Cinalli -- W15 Maceio SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204419:260711:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luna Maria Cinalli (`KXITFWMATCH-26OCT17SANCIN-CIN`) | 0.50 / 0.51 (10143) | 50.5% | 19.1% | 35.8% | 25.1% [21.8%-27.7%] | 30.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -31.4 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ana Sofia Sanchez (`KXITFWMATCH-26OCT17SANCIN-SAN`) | 0.49 / 0.50 (11597) | 49.5% | 80.9% | 64.2% | 74.9% [72.3%-78.2%] | 69.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +31.4 pp | EXTREME (DATA_WARNING) | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3191.0, B 795.0; serve-point win A 53.7%, B 52.8%; Elo A 1620.5, B 1377.8; model uncertainty 0.0295
* Form inputs: days since last match A 35, B 173; matches on record A 854, B 34; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17SANCIN-SAN  (YES = Ana Sofia Sanchez)
Model: 81%
Kalshi: 50%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ioannis Xilas vs Luka Talan Lopatic -- M15 Heraklion SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 20:34Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T20:34:40Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17XILTAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luka Talan Lopatic (`KXITFMATCH-26OCT17XILTAL-TAL`) | 0.14 / 0.96 (55) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ioannis Xilas (`KXITFMATCH-26OCT17XILTAL-XIL`) | 0.04 / 0.96 (55) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pedro Sakamoto vs Hernando Jose Escurra Isnardi -- M15 Maringa SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106203:200622:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hernando Jose Escurra Isnardi (`KXITFMATCH-26OCT17SAKESC-ESC`) | 0.12 / 0.18 (10) | 15.0% | 17.0% | 38.6% | 15.1% [13.4%-17.9%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pedro Sakamoto (`KXITFMATCH-26OCT17SAKESC-SAK`) | 0.82 / 0.84 (10) | 83.0% | 83.0% | 61.4% | 84.9% [82.1%-86.6%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.0 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1912.0, B 342.0; serve-point win A 66.6%, B 40.9%; Elo A 1566.3, B 1211.6; model uncertainty 0.0224
* Form inputs: days since last match A 19, B 28; matches on record A 670, B 54; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Josefina Estevez vs Barbara Gatica -- W15 Maceio SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211903:260717:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Josefina Estevez (`KXITFWMATCH-26OCT17ESTGAT-EST`) | 0.32 / 0.34 (53) | 33.0% | 8.3% | 32.9% | 15.7% [10.9%-19.1%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -24.7 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Barbara Gatica (`KXITFWMATCH-26OCT17ESTGAT-GAT`) | 0.65 / 0.69 (41) | 67.0% | 91.7% | 67.1% | 84.3% [80.9%-89.1%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +24.7 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 732.0, B 633.0; serve-point win A 45.2%, B 44.5%; Elo A 1285.0, B 1649.7; model uncertainty 0.0412
* Form inputs: days since last match A 278, B 1608; matches on record A 55, B 388; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17ESTGAT-GAT  (YES = Barbara Gatica)
Model: 92%
Kalshi: 67%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dana Guzman vs Sloane Stephens -- W100 Edmond OK QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-17T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201585:221834:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dana Guzman (`KXITFWMATCH-26OCT17GUZSTE-GUZ`) | 0.36 / 0.39 (36) | 37.5% | 19.4% | 63.1% | 31.6% [15.8%-45.7%] | -- | -- | -- | -- | PASS | -18.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sloane Stephens (`KXITFWMATCH-26OCT17GUZSTE-STE`) | 0.62 / 0.64 (1) | 63.0% | 80.6% | 36.9% | 68.5% [54.3%-84.2%] | -- | -- | -- | -- | PASS | +17.6 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 812.0, B 2061.0; serve-point win A 51.0%, B 42.5%; Elo A 1552.1, B 1813.0; model uncertainty 0.1495
* Form inputs: days since last match A 243, B 29; matches on record A 42, B 685; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17GUZSTE-STE  (YES = Sloane Stephens)
Model: 81%
Kalshi: 63%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.046, surface_pool_high +0.054, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Johnson / Rapolu vs El Jardi / Frodin -- W100 Edmond OK SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17JOHRAPELJFRO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| El Jardi / Frodin (`KXITFWDOUBLES-26OCT17JOHRAPELJFRO-ELJFRO`) | 0.56 / 0.67 (52) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Johnson / Rapolu (`KXITFWDOUBLES-26OCT17JOHRAPELJFRO-JOHRAP`) | 0.28 / 0.41 (19) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jack Anthrop vs Eli Stephenson -- M15 Lexington KY SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17ANTSTE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Anthrop (`KXITFMATCH-26OCT17ANTSTE-ANT`) | 0.80 / 0.81 (195) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eli Stephenson (`KXITFMATCH-26OCT17ANTSTE-STE`) | 0.19 / 0.20 (10590) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Manuel La Serna vs Hugo Dellien -- ATP Challenger Santa Cruz 2 SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-17T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106198:210412:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Dellien (`KXATPCHALLENGERMATCH-26OCT17LADEL-DEL`) | 0.78 / 0.79 (327) | 78.5% | 73.3% | 68.7% | 73.6% [71.9%-75.7%] | 76.6% | 78.2% | 76.6% | KALSHI_LONE_OUTLIER | PASS | -5.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Juan Manuel La Serna (`KXATPCHALLENGERMATCH-26OCT17LADEL-LA`) | 0.21 / 0.22 (1308) | 21.5% | 26.7% | 31.3% | 26.4% [24.3%-28.1%] | 23.4% | 21.7% | 23.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +5.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2310.0, B 4561.0; serve-point win A 55.1%, B 40.2%; Elo A 1525.0, B 1770.7; model uncertainty 0.0193
* Form inputs: days since last match A 40, B 26; matches on record A 138, B 885; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Mwendwa Mbithi vs Lucas Andrade Da Silva -- M15 Quito SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-17T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132017:212455:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Andrade Da Silva (`KXITFMATCH-26OCT17MBIAND-AND`) | 0.81 / 0.83 (2858) | 82.0% | 68.7% | 59.0% | 66.6% [64.7%-68.4%] | 81.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.3 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mwendwa Mbithi (`KXITFMATCH-26OCT17MBIAND-MBI`) | 0.17 / 0.18 (1457) | 17.5% | 31.3% | 41.0% | 33.4% [31.6%-35.3%] | 18.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 387.0; serve-point win A 60.9%, B 35.2%; Elo A 1277.7, B 1401.0; model uncertainty 0.0183
* Form inputs: days since last match A 677, B 19; matches on record A 130, B 10; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.018, surface_dev_loose +0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikola Slavic vs Theo Papamalamis -- M15 Lexington KY SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-17T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208302:210494:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Papamalamis (`KXITFMATCH-26OCT17SLAPAP-PAP`) | 0.79 / 0.80 (48) | 79.5% | 66.6% | 46.5% | 64.7% [63.7%-65.8%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nikola Slavic (`KXITFMATCH-26OCT17SLAPAP-SLA`) | 0.21 / 0.22 (10038) | 21.5% | 33.4% | 53.5% | 35.3% [34.2%-36.3%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 99.0, B 354.0; serve-point win A 61.8%, B 34.8%; Elo A 1251.3, B 1365.1; model uncertainty 0.0104
* Form inputs: days since last match A 97, B 432; matches on record A 17, B 55; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.009, surface_dev_loose +0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Reese Brantmeier vs Kajsa Rinaldo Persson -- W50 Quebec City SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-17T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211643:222034:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reese Brantmeier (`KXITFWMATCH-26OCT17BRARIN-BRA`) | 0.73 / 0.76 (1893) | 74.5% | 62.1% | 15.7% | 46.9% [39.7%-53.1%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.4 pp | REVIEW | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kajsa Rinaldo Persson (`KXITFWMATCH-26OCT17BRARIN-RIN`) | 0.25 / 0.26 (6395) | 25.5% | 37.9% | 84.3% | 53.1% [46.9%-60.3%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +12.4 pp | REVIEW | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 133.0, B 3104.0; serve-point win A 59.1%, B 43.2%; Elo A 1565.6, B 1566.1; model uncertainty 0.0674
* Form inputs: days since last match A 20, B 24; matches on record A 89, B 430; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.072, surface_pool_high +0.063, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gatica / Pereira vs Ayala / Romero -- W15 Maceio F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17GATPERAYAROM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayala / Romero (`KXITFWDOUBLES-26OCT17GATPERAYAROM-AYAROM`) | 0.31 / 0.48 (73) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gatica / Pereira (`KXITFWDOUBLES-26OCT17GATPERAYAROM-GATPER`) | 0.45 / 0.69 (0) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mimi Xu vs Ariana Arseneault -- W50 Quebec City SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-17T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220502:259685:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ariana Arseneault (`KXITFWMATCH-26OCT17XUXARS-ARS`) | 0.48 / 0.49 (52) | 48.5% | 35.4% | 55.8% | 46.8% [39.0%-50.0%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.2 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mimi Xu (`KXITFWMATCH-26OCT17XUXARS-XUX`) | 0.51 / 0.52 (129) | 51.5% | 64.6% | 44.2% | 53.2% [50.0%-61.0%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +13.2 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1841.0, B 2049.0; serve-point win A 57.6%, B 45.3%; Elo A 1592.8, B 1496.9; model uncertainty 0.0551
* Form inputs: days since last match A 257, B 26; matches on record A 98, B 129; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kristina Penickova vs Julieta Pareja -- W100 Edmond OK QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 22:45Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-17T22:45:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264075:266381:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julieta Pareja (`KXITFWMATCH-26OCT17PENPAR-PAR`) | 0.79 / 0.81 (409) | 80.0% | 79.0% | 54.2% | 66.9% [62.5%-75.1%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.0 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kristina Penickova (`KXITFWMATCH-26OCT17PENPAR-PEN`) | 0.20 / 0.21 (6139) | 20.5% | 21.0% | 45.8% | 33.1% [24.9%-37.5%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +0.5 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1178.0, B 1273.0; serve-point win A 53.3%, B 40.6%; Elo A 1497.9, B 1696.0; model uncertainty 0.0634
* Form inputs: days since last match A 52, B 38; matches on record A 39, B 63; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.010, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Roddick / Tokac vs Debru / Marionneau -- M25 Austin TX F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17RODTOKDEBMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Debru / Marionneau (`KXITFDOUBLES-26OCT17RODTOKDEBMAR-DEBMAR`) | 0.41 / 0.61 (8) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Roddick / Tokac (`KXITFDOUBLES-26OCT17RODTOKDEBMAR-RODTOK`) | 0.38 / 0.54 (27) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arseneault / Lacasse vs Brantmeier / Xu -- W50 Quebec City F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17ARSLACBRAXUX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arseneault / Lacasse (`KXITFWDOUBLES-26OCT17ARSLACBRAXUX-ARSLAC`) | 0.06 / 0.52 (1) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Brantmeier / Xu (`KXITFWDOUBLES-26OCT17ARSLACBRAXUX-BRAXUX`) | 0.52 / 0.75 (2) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Francisco Comesana vs Thiago Seyboth Wild -- ATP Challenger Santa Cruz 2 SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 23:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-17T23:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:205734:207681:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Comesana (`KXATPCHALLENGERMATCH-26OCT17COMSEY-COM`) | 0.41 / 0.42 (1096) | 41.5% | 45.6% | 31.0% | 37.3% [34.1%-41.6%] | 41.6% | 41.7% | -- | INSUFFICIENT_INPUTS | PASS | +4.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thiago Seyboth Wild (`KXATPCHALLENGERMATCH-26OCT17COMSEY-SEY`) | 0.57 / 0.59 (10302) | 58.0% | 54.4% | 69.0% | 62.7% [58.4%-65.9%] | 58.4% | 58.2% | -- | INSUFFICIENT_INPUTS | WATCH | -3.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4413.0, B 3996.0; serve-point win A 64.0%, B 35.1%; Elo A 1777.7, B 1742.2; model uncertainty 0.0375
* Form inputs: days since last match A 12, B 12; matches on record A 441, B 485; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.014, surface_dev_tight +0.024
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Alex Hernandez vs Juan Sebastian Osorio -- M15 Quito SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17HEROSO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Hernandez (`KXITFMATCH-26OCT17HEROSO-HER`) | 0.58 / 0.62 (8306) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juan Sebastian Osorio (`KXITFMATCH-26OCT17HEROSO-OSO`) | 0.41 / 0.42 (7667) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Brostrom Poulsen / Slavic vs Kapasi / Sheldon -- M15 Lexington KY SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-18T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17BROSLAKAPSHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brostrom Poulsen / Slavic (`KXITFDOUBLES-26OCT17BROSLAKAPSHE-BROSLA`) | 0.72 / 0.80 (0) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kapasi / Sheldon (`KXITFDOUBLES-26OCT17BROSLAKAPSHE-KAPSHE`) | 0.20 / 0.27 (34) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Victor Couto Loureiro / Pagotto vs Henrique Chabalgoity / Fontes Damorim -- M15 Maringa F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-18T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17VICPAGHENFON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Henrique Chabalgoity / Fontes Damorim (`KXITFDOUBLES-26OCT17VICPAGHENFON-HENFON`) | 0.20 / 0.52 (1) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victor Couto Loureiro / Pagotto (`KXITFDOUBLES-26OCT17VICPAGHENFON-VICPAG`) | 0.34 / 0.81 (74) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kristina Liutova vs Renata Zarazua -- W100 Edmond OK SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213887:269714:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristina Liutova (`KXITFWMATCH-26OCT17LIUZAR-LIU`) | 0.63 / 0.66 (74) | 64.5% | 46.3% | 52.1% | 44.1% [37.4%-51.1%] | -- | -- | -- | -- | PASS | -18.2 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Renata Zarazua (`KXITFWMATCH-26OCT17LIUZAR-ZAR`) | 0.34 / 0.35 (38) | 34.5% | 53.7% | 47.9% | 55.9% [48.9%-62.6%] | -- | -- | -- | -- | WATCH | +19.2 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 754.0, B 4923.0; serve-point win A 53.6%, B 45.8%; Elo A 1701.6, B 1765.5; model uncertainty 0.0682
* Form inputs: days since last match A 47, B 7; matches on record A 37, B 698; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17LIUZAR-ZAR  (YES = Renata Zarazua)
Model: 54%
Kalshi: 34%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.037, surface_dev_loose +0.021, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lui Maxted vs Cosme Rolland de Ravel -- M25 Austin TX SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210747:tml:R0KE:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lui Maxted (`KXITFMATCH-26OCT17MAXROL-MAX`) | 0.58 / 0.60 (7706) | 59.0% | 37.2% | 47.5% | 35.2% [34.2%-35.2%] | -- | -- | -- | -- | PASS | -21.8 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cosme Rolland de Ravel (`KXITFMATCH-26OCT17MAXROL-ROL`) | 0.41 / 0.42 (51) | 41.5% | 62.8% | 52.5% | 64.8% [64.8%-65.8%] | -- | -- | -- | -- | PASS | +21.3 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 473.0; serve-point win A 61.1%, B 36.3%; Elo A 1353.4, B 1459.5; model uncertainty 0.005
* Form inputs: days since last match A 726, B 110; matches on record A 16, B 7; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT17MAXROL-ROL  (YES = Cosme Rolland de Ravel)
Model: 63%
Kalshi: 42%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diego Hidalgo / Mariano Kestelboim vs Luis Guto Miguel / Eduardo Ribeiro -- ATP Challenger Santa Cruz 2 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-18T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17HIDKESMIGRIB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diego Hidalgo / Mariano Kestelboim (`KXATPCHALLENGERDOUBLES-26OCT17HIDKESMIGRIB-HIDKES`) | 0.11 / 0.94 (100) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luis Guto Miguel / Eduardo Ribeiro (`KXATPCHALLENGERDOUBLES-26OCT17HIDKESMIGRIB-MIGRIB`) | 0.06 / 0.54 (43) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sebastian Gomez / Urrea vs Alvarado / Mbithi -- M15 Quito F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-18T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17SEBURRALVMBI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alvarado / Mbithi (`KXITFDOUBLES-26OCT17SEBURRALVMBI-ALVMBI`) | 0.20 / 0.30 (35) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sebastian Gomez / Urrea (`KXITFDOUBLES-26OCT17SEBURRALVMBI-SEBURR`) | 0.66 / 0.80 (0) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alastair Gray vs Dominick Mosejczuk -- M25 Austin TX SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17GRAMOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alastair Gray (`KXITFMATCH-26OCT17GRAMOS-GRA`) | 0.62 / 0.63 (9088) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dominick Mosejczuk (`KXITFMATCH-26OCT17GRAMOS-MOS`) | 0.37 / 0.40 (56) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maya Joint vs Kayla Day -- WTA Osaka Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215037:233741:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kayla Day (`KXWTAMATCH-26OCT17JOIDAY-DAY`) | 0.44 / 0.45 (81) | 44.5% | 47.9% | 74.1% | 64.4% [50.0%-68.7%] | 44.4% | 44.5% | 44.5% | MODEL_LONE_OUTLIER | WATCH | +3.5 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Maya Joint (`KXWTAMATCH-26OCT17JOIDAY-JOI`) | 0.55 / 0.57 (9391) | 56.0% | 52.0% | 25.9% | 35.6% [31.3%-50.0%] | 55.6% | 56.1% | 56.1% | MODEL_LONE_OUTLIER | PASS | -4.0 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3855.0, B 3639.0; serve-point win A 57.0%, B 43.4%; Elo A 1824.8, B 1748.9; model uncertainty 0.0937
* Form inputs: days since last match A 0, B 0; matches on record A 237, B 478; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.024, surface_dev_tight +0.025
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17JOIDAY-26` Over 25.5 games: 0.18/0.33 mid 25.5%, model 45.0% (projection_v2.0 (prediction ledger)) -- gap +19.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17JOIDAY-16` Over 15.5 games: 0.57/0.99 mid 78.0%, model 97.4% (projection_v2.0 (prediction ledger)) -- gap +19.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17JOIDAY-21` Over 20.5 games: 0.55/0.57 mid 56.0%, model 68.2% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17JOIDAY-2-DAY` Will Kayla Day win set 2 in the Maya Joint vs Kayla Day match: 0.40/0.47 mid 43.5%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17JOIDAY-1-DAY` Will Kayla Day win set 1 in the Maya Joint vs Kayla Day match: 0.43/0.47 mid 45.0%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17JOIDAY-1-JOI` Will Maya Joint win set 1 in the Maya Joint vs Kayla Day match: 0.52/0.55 mid 53.5%, model 51.4% (projection_v2.0 (prediction ledger)) -- gap -2.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17JOIDAY-2-JOI` Will Maya Joint win set 2 in the Maya Joint vs Kayla Day match: 0.49/0.57 mid 53.0%, model 51.4% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Taylah Preston vs Emerson Jones -- WTA Osaka Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:223194:263644:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emerson Jones (`KXWTAMATCH-26OCT17PREJON-JON`) | 0.50 / 0.52 (186) | 51.0% | 44.3% | 35.0% | 38.5% [37.0%-43.2%] | 51.1% | 50.3% | -- | INSUFFICIENT_INPUTS | PASS | -6.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Taylah Preston (`KXWTAMATCH-26OCT17PREJON-PRE`) | 0.47 / 0.50 (56) | 48.5% | 55.7% | 65.0% | 61.5% [56.8%-63.0%] | 48.9% | 47.5% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +7.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5098.0, B 3547.0; serve-point win A 56.5%, B 44.6%; Elo A 1818.4, B 1792.5; model uncertainty 0.0307
* Form inputs: days since last match A 0, B 0; matches on record A 265, B 149; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.010, surface_dev_tight -0.015
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17PREJON-17` Over 16.5 games: 0.29/0.99 mid 64.0%, model 93.5% (projection_v2.0 (prediction ledger)) -- gap +29.5 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17PREJON-22` Over 21.5 games: 0.49/0.51 mid 50.0%, model 62.5% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17PREJON-27` Over 26.5 games: 0.03/0.56 mid 29.5%, model 39.2% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PREJON-2-PRE` Will Taylah Preston win set 2 in the Taylah Preston vs Emerson Jones match: 0.43/0.50 mid 46.5%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PREJON-1-PRE` Will Taylah Preston win set 1 in the Taylah Preston vs Emerson Jones match: 0.47/0.50 mid 48.5%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PREJON-1-JON` Will Emerson Jones win set 1 in the Taylah Preston vs Emerson Jones match: 0.48/0.52 mid 50.0%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PREJON-2-JON` Will Emerson Jones win set 2 in the Taylah Preston vs Emerson Jones match: 0.45/0.52 mid 48.5%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap -2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mary Stoiana vs Sayaka Ishii -- WTA Osaka Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:223168:259967:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sayaka Ishii (`KXWTAMATCH-26OCT17STOISH-ISH`) | 0.12 / 0.14 (13981) | 13.0% | 21.9% | 19.9% | 23.6% [22.1%-27.3%] | 14.7% | 13.2% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +8.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mary Stoiana (`KXWTAMATCH-26OCT17STOISH-STO`) | 0.86 / 0.88 (1006) | 87.0% | 78.1% | 80.2% | 76.3% [72.7%-77.9%] | 85.3% | 87.4% | 87.4% | MODEL_LONE_OUTLIER | PASS | -8.9 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2840.0, B 1713.0; serve-point win A 61.7%, B 44.2%; Elo A 1802.0, B 1641.6; model uncertainty 0.0263
* Form inputs: days since last match A 0, B 0; matches on record A 141, B 190; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.012, surface_pool_high -0.012, surface_dev_loose +0.007, surface_dev_tight -0.012
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXWTAGTOTAL-26OCT17STOISH-19` Over 18.5 games: 0.50/0.51 mid 50.5%, model 76.0% (projection_v2.0 (prediction ledger)) -- gap +25.5 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17STOISH-24` Over 23.5 games: 0.21/0.31 mid 26.0%, model 44.3% (projection_v2.0 (prediction ledger)) -- gap +18.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17STOISH-1-ISH` Will Sayaka Ishii win set 1 in the Mary Stoiana vs Sayaka Ishii match: 0.09/0.21 mid 15.0%, model 30.2% (projection_v2.0 (prediction ledger)) -- gap +15.2 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17STOISH-2-STO` Will Mary Stoiana win set 2 in the Mary Stoiana vs Sayaka Ishii match: 0.80/0.85 mid 82.5%, model 69.8% (projection_v2.0 (prediction ledger)) -- gap -12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17STOISH-1-STO` Will Mary Stoiana win set 1 in the Mary Stoiana vs Sayaka Ishii match: 0.80/0.83 mid 81.5%, model 69.8% (projection_v2.0 (prediction ledger)) -- gap -11.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17STOISH-2-ISH` Will Sayaka Ishii win set 2 in the Mary Stoiana vs Sayaka Ishii match: 0.16/0.31 mid 23.5%, model 30.2% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Daria Snigur vs Katarzyna Kawa -- WTA Ningbo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 05:00Z
* Current expected start: 2026-10-18 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 02:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-120_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:203514:220750:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katarzyna Kawa (`KXWTAMATCH-26OCT17SNIKAW-KAW`) | 0.16 / 0.17 (590) | 16.5% | 12.4% | 3.6% | 5.6% [3.9%-15.8%] | 19.1% | 17.5% | 17.5% | MODEL_LONE_OUTLIER | PASS | -4.1 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Daria Snigur (`KXWTAMATCH-26OCT17SNIKAW-SNI`) | 0.83 / 0.84 (7153) | 83.5% | 87.6% | 96.4% | 94.4% [84.2%-96.1%] | 80.9% | 82.7% | 82.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +4.1 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4190.0, B 4311.0; serve-point win A 57.7%, B 50.9%; Elo A 1893.2, B 1606.2; model uncertainty 0.0596
* Form inputs: days since last match A 0, B 0; matches on record A 442, B 702; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.007, surface_dev_loose +0.015, surface_dev_tight -0.020
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17SNIKAW-16` Over 15.5 games: 0.40/0.95 mid 67.5%, model 90.5% (projection_v2.0 (prediction ledger)) -- gap +23.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17SNIKAW-26` Over 25.5 games: 0.03/0.39 mid 21.0%, model 28.2% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17SNIKAW-21` Over 20.5 games: 0.41/0.42 mid 41.5%, model 48.7% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17SNIKAW-1-KAW` Will Katarzyna Kawa win set 1 in the Daria Snigur vs Katarzyna Kawa match: 0.14/0.24 mid 19.0%, model 22.0% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17SNIKAW-2-KAW` Will Katarzyna Kawa win set 2 in the Daria Snigur vs Katarzyna Kawa match: 0.15/0.24 mid 19.5%, model 22.0% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17SNIKAW-1-SNI` Will Daria Snigur win set 1 in the Daria Snigur vs Katarzyna Kawa match: 0.75/0.78 mid 76.5%, model 78.0% (projection_v2.0 (prediction ledger)) -- gap +1.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17SNIKAW-2-SNI` Will Daria Snigur win set 2 in the Daria Snigur vs Katarzyna Kawa match: 0.75/0.79 mid 77.0%, model 78.0% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anastasia Zakharova vs Polina Kudermetova -- WTA Ningbo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 05:00Z
* Current expected start: 2026-10-18 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 02:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-120_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220435:221236:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Kudermetova (`KXWTAMATCH-26OCT17ZAKKUD-KUD`) | 0.44 / 0.46 (2222) | 45.0% | 52.8% | 47.4% | 47.9% [46.8%-48.4%] | 44.4% | 44.8% | -- | INSUFFICIENT_INPUTS | PASS | +7.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Zakharova (`KXWTAMATCH-26OCT17ZAKKUD-ZAK`) | 0.55 / 0.56 (6315) | 55.5% | 47.2% | 52.6% | 52.1% [51.6%-53.2%] | 55.6% | 55.2% | -- | INSUFFICIENT_INPUTS | PASS | -8.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4628.0, B 4285.0; serve-point win A 55.9%, B 43.6%; Elo A 1819.2, B 1806.1; model uncertainty 0.0079
* Form inputs: days since last match A 0, B 0; matches on record A 479, B 388; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.011, surface_dev_loose +0.005, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17ZAKKUD-17` Over 16.5 games: 0.40/0.98 mid 69.0%, model 93.7% (projection_v2.0 (prediction ledger)) -- gap +24.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17ZAKKUD-22` Over 21.5 games: 0.47/0.49 mid 48.0%, model 62.8% (projection_v2.0 (prediction ledger)) -- gap +14.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17ZAKKUD-27` Over 26.5 games: 0.03/0.54 mid 28.5%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17ZAKKUD-1-KUD` Will Polina Kudermetova win set 1 in the Anastasia Zakharova vs Polina Kudermetova match: 0.40/0.47 mid 43.5%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17ZAKKUD-2-KUD` Will Polina Kudermetova win set 2 in the Anastasia Zakharova vs Polina Kudermetova match: 0.40/0.49 mid 44.5%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +7.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17ZAKKUD-1-ZAK` Will Anastasia Zakharova win set 1 in the Anastasia Zakharova vs Polina Kudermetova match: 0.53/0.57 mid 55.0%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap -6.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17ZAKKUD-2-ZAK` Will Anastasia Zakharova win set 2 in the Anastasia Zakharova vs Polina Kudermetova match: 0.49/0.58 mid 53.5%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap -5.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Harriet Dart vs Aoi Ito -- WTA Osaka Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211279:256684:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harriet Dart (`KXWTAMATCH-26OCT17DARITO-DAR`) | 0.58 / 0.60 (1480) | 59.0% | 62.4% | 79.2% | 71.3% [64.6%-74.4%] | 57.5% | 59.7% | 59.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.4 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Aoi Ito (`KXWTAMATCH-26OCT17DARITO-ITO`) | 0.39 / 0.42 (6442) | 40.5% | 37.6% | 20.8% | 28.7% [25.6%-35.4%] | 42.5% | 40.5% | 40.5% | MODEL_LONE_OUTLIER | PASS | -2.9 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4244.0, B 2722.0; serve-point win A 55.0%, B 47.3%; Elo A 1789.0, B 1765.2; model uncertainty 0.0489
* Form inputs: days since last match A 0, B 0; matches on record A 674, B 302; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.027, surface_pool_high -0.028, surface_dev_loose +0.009, surface_dev_tight -0.018
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17DARITO-28` Over 27.5 games: 0.03/0.27 mid 15.0%, model 32.3% (projection_v2.0 (prediction ledger)) -- gap +17.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17DARITO-18` Over 17.5 games: 0.40/0.98 mid 69.0%, model 86.0% (projection_v2.0 (prediction ledger)) -- gap +17.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17DARITO-23` Over 22.5 games: 0.44/0.45 mid 44.5%, model 54.1% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17DARITO-2-DAR` Will Harriet Dart win set 2 in the Harriet Dart vs Aoi Ito match: 0.51/0.60 mid 55.5%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17DARITO-1-DAR` Will Harriet Dart win set 1 in the Harriet Dart vs Aoi Ito match: 0.54/0.58 mid 56.0%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17DARITO-1-ITO` Will Aoi Ito win set 1 in the Harriet Dart vs Aoi Ito match: 0.37/0.46 mid 41.5%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17DARITO-2-ITO` Will Aoi Ito win set 2 in the Harriet Dart vs Aoi Ito match: 0.37/0.46 mid 41.5%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sinja Kraus vs Sofia Kenin -- WTA Osaka Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213550:221257:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Kenin (`KXWTAMATCH-26OCT17KRAKEN-KEN`) | 0.54 / 0.56 (4415) | 55.0% | 50.5% | 29.6% | 38.2% [34.8%-47.4%] | 54.3% | 54.5% | 54.5% | MODEL_LONE_OUTLIER | PASS | -4.5 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Sinja Kraus (`KXWTAMATCH-26OCT17KRAKEN-KRA`) | 0.45 / 0.46 (6146) | 45.5% | 49.5% | 70.4% | 61.8% [52.6%-65.2%] | 45.7% | 45.7% | 45.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +4.0 pp | NORMAL | FRESH | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5054.0, B 3897.0; serve-point win A 58.4%, B 41.5%; Elo A 1722.8, B 1812.1; model uncertainty 0.0631
* Form inputs: days since last match A 0, B 0; matches on record A 493, B 525; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.020, surface_dev_loose +0.015, surface_dev_tight -0.020
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17KRAKEN-16` Over 15.5 games: 0.03/0.99 mid 51.0%, model 97.8% (projection_v2.0 (prediction ledger)) -- gap +46.8 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT17KRAKEN-21` Over 20.5 games: 0.54/0.56 mid 55.0%, model 69.3% (projection_v2.0 (prediction ledger)) -- gap +14.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT17KRAKEN-26` Over 25.5 games: 0.03/0.61 mid 32.0%, model 45.9% (projection_v2.0 (prediction ledger)) -- gap +13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT17KRAKEN-2-KRA` Will Sinja Kraus win set 2 in the Sinja Kraus vs Sofia Kenin match: 0.41/0.49 mid 45.0%, model 49.6% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT17KRAKEN-1-KRA` Will Sinja Kraus win set 1 in the Sinja Kraus vs Sofia Kenin match: 0.44/0.48 mid 46.0%, model 49.6% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT17KRAKEN-1-KEN` Will Sofia Kenin win set 1 in the Sinja Kraus vs Sofia Kenin match: 0.51/0.56 mid 53.5%, model 50.3% (projection_v2.0 (prediction ledger)) -- gap -3.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT17KRAKEN-2-KEN` Will Sofia Kenin win set 2 in the Sinja Kraus vs Sofia Kenin match: 0.48/0.56 mid 52.0%, model 50.3% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Claire Liu vs Maddison Inglis -- WTA Osaka Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 06:40Z
* Current expected start: 2026-10-18 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 03:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T06:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213666:214906:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maddison Inglis (`KXWTAMATCH-26OCT17LIUING-ING`) | 0.34 / 0.36 (6890) | 35.0% | 45.7% | 46.4% | 47.9% [42.2%-51.0%] | 36.1% | 35.2% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +10.7 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Claire Liu (`KXWTAMATCH-26OCT17LIUING-LIU`) | 0.65 / 0.66 (86) | 65.5% | 54.3% | 53.6% | 52.1% [49.0%-57.8%] | 63.9% | 63.9% | -- | INSUFFICIENT_INPUTS | PASS | -11.2 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3837.0, B 3027.0; serve-point win A 58.9%, B 41.9%; Elo A 1770.0, B 1770.9; model uncertainty 0.0443
* Form inputs: days since last match A 0, B 0; matches on record A 455, B 482; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.042, surface_pool_high -0.031, surface_dev_loose +0.005, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17LIUING-18` Over 17.5 games: 0.38/0.97 mid 67.5%, model 89.4% (projection_v2.0 (prediction ledger)) -- gap +21.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT17LIUING-23` Over 22.5 games: 0.42/0.44 mid 43.0%, model 57.2% (projection_v2.0 (prediction ledger)) -- gap +14.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT17LIUING-2-ING` Will Maddison Inglis win set 2 in the Claire Liu vs Maddison Inglis match: 0.31/0.40 mid 35.5%, model 47.1% (projection_v2.0 (prediction ledger)) -- gap +11.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT17LIUING-1-ING` Will Maddison Inglis win set 1 in the Claire Liu vs Maddison Inglis match: 0.36/0.40 mid 38.0%, model 47.1% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT17LIUING-1-LIU` Will Claire Liu win set 1 in the Claire Liu vs Maddison Inglis match: 0.60/0.63 mid 61.5%, model 52.9% (projection_v2.0 (prediction ledger)) -- gap -8.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT17LIUING-2-LIU` Will Claire Liu win set 2 in the Claire Liu vs Maddison Inglis match: 0.58/0.65 mid 61.5%, model 52.9% (projection_v2.0 (prediction ledger)) -- gap -8.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT17LIUING-28` Over 27.5 games: 0.03/0.57 mid 30.0%, model 36.0% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Connie Ma vs Lea Ma -- W35 Redding CA SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221143:221220:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Connie Ma (`KXITFWMATCH-26OCT17MAXMAX2-MAX`) | 0.64 / 0.67 (279) | 65.5% | 29.5% | 26.1% | 31.0% [29.0%-32.9%] | -- | -- | -- | -- | PASS | -36.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Lea Ma (`KXITFWMATCH-26OCT17MAXMAX2-MAX2`) | 0.33 / 0.35 (9) | 34.0% | 70.5% | 73.9% | 69.0% [67.1%-71.0%] | -- | -- | -- | -- | PASS | +36.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 2727.0; serve-point win A 56.5%, B 39.4%; Elo A 1475.0, B 1614.7; model uncertainty 0.0195
* Form inputs: days since last match A 1839, B 34; matches on record A 21, B 168; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17MAXMAX2-MAX2  (YES = Lea Ma)
Model: 71%
Kalshi: 34%
Gap: +37 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.019, surface_dev_loose +0.001, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alycia Parks vs Yulia Putintseva -- WTA Ningbo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 05:00Z
* Current expected start: 2026-10-18 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 03:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-30_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201709:219917:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alycia Parks (`KXWTAMATCH-26OCT17PARPUT-PAR`) | 0.24 / 0.26 (11308) | 25.0% | 38.4% | 41.2% | 39.1% [37.1%-40.7%] | 25.5% | 24.3% | 24.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +13.4 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Yulia Putintseva (`KXWTAMATCH-26OCT17PARPUT-PUT`) | 0.75 / 0.76 (308) | 75.5% | 61.6% | 58.8% | 60.9% [59.3%-62.9%] | 74.5% | 75.8% | 75.8% | MODEL_LONE_OUTLIER | PASS | -13.9 pp | REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5263.0, B 4366.0; serve-point win A 56.9%, B 40.8%; Elo A 1775.0, B 1893.3; model uncertainty 0.0177
* Form inputs: days since last match A 0, B 0; matches on record A 437, B 857; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17PARPUT-17` Over 16.5 games: 0.40/0.98 mid 69.0%, model 94.0% (projection_v2.0 (prediction ledger)) -- gap +25.0 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17PARPUT-27` Over 26.5 games: 0.03/0.28 mid 15.5%, model 39.4% (projection_v2.0 (prediction ledger)) -- gap +23.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17PARPUT-22` Over 21.5 games: 0.45/0.47 mid 46.0%, model 62.6% (projection_v2.0 (prediction ledger)) -- gap +16.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PARPUT-1-PAR` Will Alycia Parks win set 1 in the Alycia Parks vs Yulia Putintseva match: 0.28/0.31 mid 29.5%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PARPUT-1-PUT` Will Yulia Putintseva win set 1 in the Alycia Parks vs Yulia Putintseva match: 0.69/0.70 mid 69.5%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap -11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PARPUT-2-PUT` Will Yulia Putintseva win set 2 in the Alycia Parks vs Yulia Putintseva match: 0.52/0.81 mid 66.5%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap -8.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PARPUT-2-PAR` Will Alycia Parks win set 2 in the Alycia Parks vs Yulia Putintseva match: 0.21/0.48 mid 34.5%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anhelina Kalinina vs Aliaksandra Sasnovich -- WTA Ningbo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 07:10Z
* Current expected start: 2026-10-18 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 03:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T07:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:205925:211843:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anhelina Kalinina (`KXWTAMATCH-26OCT18KALSAS-KAL`) | 0.40 / 0.41 (6738) | 40.5% | 51.5% | 56.8% | 54.8% [51.6%-55.3%] | -- | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.0 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aliaksandra Sasnovich (`KXWTAMATCH-26OCT18KALSAS-SAS`) | 0.59 / 0.61 (387) | 60.0% | 48.5% | 43.2% | 45.2% [44.7%-48.4%] | -- | 57.2% | -- | INSUFFICIENT_INPUTS | PASS | -11.5 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4204.0, B 4822.0; serve-point win A 56.1%, B 44.2%; Elo A 1824.8, B 1839.7; model uncertainty 0.0184
* Form inputs: days since last match A 5, B 0; matches on record A 611, B 789; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT18KALSAS-17` Over 16.5 games: 0.03/0.99 mid 51.0%, model 93.6% (projection_v2.0 (prediction ledger)) -- gap +42.6 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT18KALSAS-22` Over 21.5 games: 0.40/0.55 mid 47.5%, model 62.8% (projection_v2.0 (prediction ledger)) -- gap +15.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT18KALSAS-27` Over 26.5 games: 0.03/0.84 mid 43.5%, model 39.4% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT18KALSAS-2-KAL` Will Anhelina Kalinina win set 2 in the Anhelina Kalinina vs Aliaksandra Sasnovich match: 0.36/0.58 mid 47.0%, model 51.0% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18KALSAS-1-SAS` Will Aliaksandra Sasnovich win set 1 in the Anhelina Kalinina vs Aliaksandra Sasnovich match: 0.43/0.61 mid 52.0%, model 49.0% (projection_v2.0 (prediction ledger)) -- gap -3.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18KALSAS-2-SAS` Will Aliaksandra Sasnovich win set 2 in the Anhelina Kalinina vs Aliaksandra Sasnovich match: 0.43/0.61 mid 52.0%, model 49.0% (projection_v2.0 (prediction ledger)) -- gap -3.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18KALSAS-1-KAL` Will Anhelina Kalinina win set 1 in the Anhelina Kalinina vs Aliaksandra Sasnovich match: 0.36/0.61 mid 48.5%, model 51.0% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gabriel Diallo vs Rei Sakamoto -- ATP Almaty Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 06:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:209113:210536:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriel Diallo (`KXATPMATCH-26OCT18DIASAK-DIA`) | 0.46 / 0.47 (562) | 46.5% | 55.4% | 52.8% | 55.7% [54.7%-57.1%] | 45.7% | 47.0% | 46.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Rei Sakamoto (`KXATPMATCH-26OCT18DIASAK-SAK`) | 0.52 / 0.53 (6129) | 52.5% | 44.6% | 47.2% | 44.3% [42.9%-45.3%] | 54.3% | 49.4% | 54.3% | MODEL_LONE_OUTLIER | PASS | -7.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4598.0, B 3076.0; serve-point win A 69.0%, B 32.2%; Elo A 1825.8, B 1744.4; model uncertainty 0.0119
* Form inputs: days since last match A 0, B 0; matches on record A 277, B 145; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.009, surface_dev_tight +0.014
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT18DIASAK-DIA21` Will Gabriel Diallo win the Gabriel Diallo vs Rei Sakamoto match by a set score of 2-1?: 0.04/0.24 mid 14.0%, model 26.7% (projection_v2.0 (prediction ledger)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18DIASAK-24` Over 23.5 games: 0.46/0.49 mid 47.5%, model 58.4% (projection_v2.0 (prediction ledger)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18DIASAK-SAK2` Will Rei Sakamoto win at least 1.5 more games than Gabriel Diallo?: 0.45/0.48 mid 46.5%, model 36.1% (projection_v2.0 (prediction ledger)) -- gap -10.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18DIASAK-19` Over 18.5 games: 0.69/0.99 mid 84.0%, model 94.0% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18DIASAK-SAK21` Will Rei Sakamoto win the Gabriel Diallo vs Rei Sakamoto match by a set score of 2-1?: 0.04/0.24 mid 14.0%, model 23.1% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18DIASAK-SAK5` Will Rei Sakamoto win at least 4.5 more games than Gabriel Diallo?: 0.13/0.23 mid 18.0%, model 9.1% (projection_v2.0 (prediction ledger)) -- gap -8.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18DIASAK-29` Over 28.5 games: 0.33/0.37 mid 35.0%, model 42.1% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18DIASAK-DIA2` Will Gabriel Diallo win at least 1.5 more games than Rei Sakamoto?: 0.39/0.41 mid 40.0%, model 46.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18DIASAK-1-DIA` Will Gabriel Diallo win set 1 in the Gabriel Diallo vs Rei Sakamoto match: 0.45/0.50 mid 47.5%, model 53.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18DIASAK-2-DIA` Will Gabriel Diallo win set 2 in the Gabriel Diallo vs Rei Sakamoto match: 0.45/0.50 mid 47.5%, model 53.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18DIASAK-2-SAK` Will Rei Sakamoto win set 2 in the Gabriel Diallo vs Rei Sakamoto match: 0.50/0.55 mid 52.5%, model 46.4% (projection_v2.0 (prediction ledger)) -- gap -6.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18DIASAK-1-SAK` Will Rei Sakamoto win set 1 in the Gabriel Diallo vs Rei Sakamoto match: 0.50/0.54 mid 52.0%, model 46.4% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18DIASAK-DIA20` Will Gabriel Diallo win the Gabriel Diallo vs Rei Sakamoto match by a set score of 2-0?: 0.25/0.28 mid 26.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18DIASAK-SAK20` Will Rei Sakamoto win the Gabriel Diallo vs Rei Sakamoto match by a set score of 2-0?: 0.12/0.34 mid 23.0%, model 21.5% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Adam Walton vs Nikoloz Basilashvili -- ATP Almaty Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 06:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105932:200443:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikoloz Basilashvili (`KXATPMATCH-26OCT18WALBAS-BAS`) | 0.54 / 0.55 (6100) | 54.5% | 35.8% | 39.3% | 40.2% [36.9%-45.1%] | 54.3% | 54.2% | 54.3% | MODEL_LONE_OUTLIER | PASS | -18.7 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Adam Walton (`KXATPMATCH-26OCT18WALBAS-WAL`) | 0.45 / 0.46 (2214) | 45.5% | 64.2% | 60.7% | 59.8% [54.9%-63.1%] | 45.7% | 45.9% | 45.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +18.7 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5302.0, B 3285.0; serve-point win A 66.3%, B 36.6%; Elo A 1742.6, B 1683.6; model uncertainty 0.0407
* Form inputs: days since last match A 0, B 0; matches on record A 348, B 911; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18WALBAS-WAL  (YES = Adam Walton)
Model: 64%
Kalshi: 46%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.033, surface_dev_loose -0.015, surface_dev_tight +0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT18WALBAS-BAS2` Will Nikoloz Basilashvili win at least 1.5 more games than Adam Walton?: 0.47/0.50 mid 48.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap -19.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18WALBAS-WAL20` Will Adam Walton win the Adam Walton vs Nikoloz Basilashvili match by a set score of 2-0?: 0.07/0.28 mid 17.5%, model 35.5% (projection_v2.0 (prediction ledger)) -- gap +18.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18WALBAS-WAL2` Will Adam Walton win at least 1.5 more games than Nikoloz Basilashvili?: 0.33/0.46 mid 39.5%, model 56.8% (projection_v2.0 (prediction ledger)) -- gap +17.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18WALBAS-WAL21` Will Adam Walton win the Adam Walton vs Nikoloz Basilashvili match by a set score of 2-1?: 0.05/0.22 mid 13.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +15.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18WALBAS-1-WAL` Will Adam Walton win set 1 in the Adam Walton vs Nikoloz Basilashvili match: 0.44/0.49 mid 46.5%, model 59.6% (projection_v2.0 (prediction ledger)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18WALBAS-2-BAS` Will Nikoloz Basilashvili win set 2 in the Adam Walton vs Nikoloz Basilashvili match: 0.51/0.56 mid 53.5%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap -13.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18WALBAS-2-WAL` Will Adam Walton win set 2 in the Adam Walton vs Nikoloz Basilashvili match: 0.44/0.49 mid 46.5%, model 59.6% (projection_v2.0 (prediction ledger)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18WALBAS-1-BAS` Will Nikoloz Basilashvili win set 1 in the Adam Walton vs Nikoloz Basilashvili match: 0.51/0.54 mid 52.5%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap -12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18WALBAS-BAS5` Will Nikoloz Basilashvili win at least 4.5 more games than Adam Walton?: 0.10/0.22 mid 16.0%, model 9.0% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18WALBAS-BAS20` Will Nikoloz Basilashvili win the Adam Walton vs Nikoloz Basilashvili match by a set score of 2-0?: 0.12/0.33 mid 22.5%, model 16.3% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18WALBAS-21` Over 20.5 games: 0.48/0.88 mid 68.0%, model 73.9% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18WALBAS-26` Over 25.5 games: 0.40/0.48 mid 44.0%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18WALBAS-BAS21` Will Nikoloz Basilashvili win the Adam Walton vs Nikoloz Basilashvili match by a set score of 2-1?: 0.05/0.25 mid 15.0%, model 19.4% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18WALBAS-31` Over 30.5 games: 0.03/0.43 mid 23.0%, model 26.6% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tatiana Prozorova vs Kamilla Rakhimova -- WTA Ningbo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 08:20Z
* Current expected start: 2026-10-18 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 05:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T08:20:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215872:236955:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tatiana Prozorova (`KXWTAMATCH-26OCT18PRORAK-PRO`) | 0.41 / 0.45 (192) | 43.0% | 49.3% | 72.2% | 64.8% [49.5%-69.0%] | -- | 43.3% | -- | INSUFFICIENT_INPUTS | PASS | +6.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kamilla Rakhimova (`KXWTAMATCH-26OCT18PRORAK-RAK`) | 0.54 / 0.58 (6222) | 56.0% | 50.7% | 27.8% | 35.2% [31.0%-50.5%] | -- | 56.7% | -- | INSUFFICIENT_INPUTS | PASS | -5.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3551.0, B 5718.0; serve-point win A 58.5%, B 41.4%; Elo A 1799.1, B 1839.4; model uncertainty 0.0977
* Form inputs: days since last match A 10, B 7; matches on record A 290, B 475; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose +0.009, surface_dev_tight -0.019
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 4 carry a model probability
  * `KXWTASETWINNER-26OCT18PRORAK-2-RAK` Will Kamilla Rakhimova win set 2 in the Tatiana Prozorova vs Kamilla Rakhimova match: 0.51/0.73 mid 62.0%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap -11.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18PRORAK-2-PRO` Will Tatiana Prozorova win set 2 in the Tatiana Prozorova vs Kamilla Rakhimova match: 0.27/0.57 mid 42.0%, model 49.5% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18PRORAK-1-PRO` Will Tatiana Prozorova win set 1 in the Tatiana Prozorova vs Kamilla Rakhimova match: 0.42/0.47 mid 44.5%, model 49.5% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT18PRORAK-1-RAK` Will Kamilla Rakhimova win set 1 in the Tatiana Prozorova vs Kamilla Rakhimova match: 0.50/0.58 mid 54.0%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap -3.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Han Shi vs Alina Korneeva -- WTA Ningbo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 08:20Z
* Current expected start: 2026-10-18 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 05:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T08:20:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:222559:252499:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Korneeva (`KXWTAMATCH-26OCT18SHIKOR-KOR`) | 0.75 / 0.77 (2752) | 76.0% | 85.2% | 76.0% | 79.6% [78.0%-82.8%] | 74.5% | 76.3% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +9.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Han Shi (`KXWTAMATCH-26OCT18SHIKOR-SHI`) | 0.23 / 0.25 (5670) | 24.0% | 14.8% | 24.0% | 20.4% [17.2%-22.0%] | 25.5% | 23.9% | -- | INSUFFICIENT_INPUTS | PASS | -9.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3226.0, B 3297.0; serve-point win A 50.3%, B 41.8%; Elo A 1600.6, B 1915.0; model uncertainty 0.0237
* Form inputs: days since last match A 173, B 21; matches on record A 228, B 191; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose +0.004, surface_dev_tight -0.004
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT18SHIKOR-15` Over 14.5 games: 0.03/0.99 mid 51.0%, model 96.6% (projection_v2.0 (prediction ledger)) -- gap +45.6 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT18SHIKOR-1-KOR` Will Alina Korneeva win set 1 in the Han Shi vs Alina Korneeva match: 0.68/0.71 mid 69.5%, model 75.8% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT18SHIKOR-20` Over 19.5 games: 0.51/0.54 mid 52.5%, model 58.8% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT18SHIKOR-2-KOR` Will Alina Korneeva win set 2 in the Han Shi vs Alina Korneeva match: 0.68/0.74 mid 71.0%, model 75.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18SHIKOR-1-SHI` Will Han Shi win set 1 in the Han Shi vs Alina Korneeva match: 0.26/0.31 mid 28.5%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT18SHIKOR-25` Over 24.5 games: 0.03/0.61 mid 32.0%, model 34.8% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT18SHIKOR-2-SHI` Will Han Shi win set 2 in the Han Shi vs Alina Korneeva match: 0.21/0.31 mid 26.0%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap -1.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Xi Cheng Huang vs Semen Pankin -- ATP Challenger Guangzhou Nansha Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-18T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17HUAPAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xi Cheng Huang (`KXATPCHALLENGERMATCH-26OCT17HUAPAN-HUA`) | 0.05 / 0.86 (5893) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Semen Pankin (`KXATPCHALLENGERMATCH-26OCT17HUAPAN-PAN`) | 0.05 / 0.93 (40) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Arthur Weber vs Dominik Palan -- ATP Challenger Guangzhou Nansha Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-18T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17WEBPAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dominik Palan (`KXATPCHALLENGERMATCH-26OCT17WEBPAL-PAL`) | 0.07 / 0.35 (229) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arthur Weber (`KXATPCHALLENGERMATCH-26OCT17WEBPAL-WEB`) | 0.21 / 0.81 (17) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Xiaoyin Yang vs Khumoyun Sultanov -- ATP Challenger Guangzhou Nansha Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-18T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17YANSUL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Khumoyun Sultanov (`KXATPCHALLENGERMATCH-26OCT17YANSUL-SUL`) | 0.05 / 0.93 (49) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xiaoyin Yang (`KXATPCHALLENGERMATCH-26OCT17YANSUL-YAN`) | 0.05 / 0.94 (416) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nao Nishino vs Annika Penickova -- W35 Redding CA SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 07:15Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T07:15:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:265628:266379:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nao Nishino (`KXITFWMATCH-26OCT17NISPEN-NIS`) | 0.25 / 0.30 (24) | 27.5% | 26.4% | 23.2% | 32.6% [28.8%-36.4%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Annika Penickova (`KXITFWMATCH-26OCT17NISPEN-PEN`) | 0.68 / 0.72 (3072) | 70.0% | 73.6% | 76.8% | 67.4% [63.6%-71.2%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 295.0, B 702.0; serve-point win A 52.9%, B 42.4%; Elo A 1367.9, B 1478.8; model uncertainty 0.0378
* Form inputs: days since last match A 446, B 53; matches on record A 12, B 38; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.005, surface_dev_loose -0.009, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Roman Safiullin vs Ilia Simakin -- ATP Almaty Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 08:00Z
* Current expected start: 2026-10-18 07:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 06:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-30_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126128:209899:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Roman Safiullin (`KXATPMATCH-26OCT18SAFSIM-SAF`) | 0.79 / 0.80 (130) | 79.5% | 67.3% | 52.4% | 57.8% [54.9%-65.4%] | 77.5% | 79.9% | -- | INSUFFICIENT_INPUTS | PASS | -12.2 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ilia Simakin (`KXATPMATCH-26OCT18SAFSIM-SIM`) | 0.20 / 0.21 (2142) | 20.5% | 32.7% | 47.5% | 42.2% [34.6%-45.1%] | 22.5% | 20.3% | -- | INSUFFICIENT_INPUTS | PASS | +12.2 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4418.0, B 3713.0; serve-point win A 67.2%, B 36.5%; Elo A 1876.8, B 1720.5; model uncertainty 0.0524
* Form inputs: days since last match A 8, B 9; matches on record A 675, B 239; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.024, surface_pool_high -0.019, surface_dev_loose -0.005, surface_dev_tight +0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT18SAFSIM-SAF21` Will Roman Safiullin win the Roman Safiullin vs Ilia Simakin match by a set score of 2-1?: 0.07/0.26 mid 16.5%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAFSIM-1-SAF` Will Roman Safiullin win set 1 in the Roman Safiullin vs Ilia Simakin match: 0.72/0.76 mid 74.0%, model 61.8% (projection_v2.0 (prediction ledger)) -- gap -12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAFSIM-1-SIM` Will Ilia Simakin win set 1 in the Roman Safiullin vs Ilia Simakin match: 0.24/0.28 mid 26.0%, model 38.2% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAFSIM-2-SAF` Will Roman Safiullin win set 2 in the Roman Safiullin vs Ilia Simakin match: 0.71/0.76 mid 73.5%, model 61.8% (projection_v2.0 (prediction ledger)) -- gap -11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAFSIM-2-SIM` Will Ilia Simakin win set 2 in the Roman Safiullin vs Ilia Simakin match: 0.24/0.29 mid 26.5%, model 38.2% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SAFSIM-SIM21` Will Ilia Simakin win the Roman Safiullin vs Ilia Simakin match by a set score of 2-1?: 0.02/0.13 mid 7.5%, model 18.1% (projection_v2.0 (prediction ledger)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SAFSIM-SAF20` Will Roman Safiullin win the Roman Safiullin vs Ilia Simakin match by a set score of 2-0?: 0.36/0.59 mid 47.5%, model 38.2% (projection_v2.0 (prediction ledger)) -- gap -9.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SAFSIM-SIM20` Will Ilia Simakin win the Roman Safiullin vs Ilia Simakin match by a set score of 2-0?: 0.02/0.11 mid 6.5%, model 14.6% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Martin Borisiouk vs Matthew Dellavedova -- M25 Qian Daohu F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200456:202354:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Borisiouk (`KXITFMATCH-26OCT17BORDEL-BOR`) | 0.36 / 0.38 (74) | 37.0% | 42.1% | 65.5% | 39.2% [33.5%-45.6%] | 38.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +5.2 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matthew Dellavedova (`KXITFMATCH-26OCT17BORDEL-DEL`) | 0.59 / 0.64 (2) | 61.5% | 57.9% | 34.5% | 60.8% [54.4%-66.5%] | 61.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 345.0, B 1203.0; serve-point win A 63.4%, B 35.0%; Elo A 1337.8, B 1461.1; model uncertainty 0.0604
* Form inputs: days since last match A 33, B 25; matches on record A 80, B 356; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.015, surface_dev_loose +0.001, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ekaterina Khodzhaeva vs Natalie CHEN -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17KHOCHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Natalie CHEN (`KXITFWMATCH-26OCT17KHOCHE-CHE`) | 0.03 / 0.95 (27) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ekaterina Khodzhaeva (`KXITFWMATCH-26OCT17KHOCHE-KHO`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuka Matsumoto vs Faith Perera -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17MATPER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuka Matsumoto (`KXITFWMATCH-26OCT17MATPER-MAT`) | 0.03 / 0.95 (27) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Faith Perera (`KXITFWMATCH-26OCT17MATPER-PER`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofya Nabokova vs Jannat Chiripal -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17NABCHI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jannat Chiripal (`KXITFWMATCH-26OCT17NABCHI-CHI`) | 0.03 / 0.97 (285) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofya Nabokova (`KXITFWMATCH-26OCT17NABCHI-NAB`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sarah Pang vs Xiaochuan Nie -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17PANNIE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xiaochuan Nie (`KXITFWMATCH-26OCT17PANNIE-NIE`) | 0.03 / 0.97 (285) | 50.0% | 76.2% | -- | -- [-----] | -- | -- | -- | -- | -- | +26.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Sarah Pang (`KXITFWMATCH-26OCT17PANNIE-PAN`) | 0.03 / 0.95 (27) | 49.0% | 23.8% | -- | -- [-----] | -- | -- | -- | -- | -- | -25.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 50.3%, B 44.4%; Elo A 962.5, B 1099.8; model uncertainty None
* Form inputs: days since last match A 957, B 334; matches on record A 73, B 9; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17PANNIE-NIE  (YES = Xiaochuan Nie)
Model: 76%
Kalshi: 50%
Gap: +26 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lidia Podgorichani vs Harini Parthiban -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17PODPAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harini Parthiban (`KXITFWMATCH-26OCT17PODPAR-PAR`) | 0.03 / 0.97 (285) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lidia Podgorichani (`KXITFWMATCH-26OCT17PODPAR-POD`) | 0.03 / 0.95 (27) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria KHOMUTSIANSKAYA vs Sijia Wei -- W15 Shenzhen F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221096:222944:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria KHOMUTSIANSKAYA (`KXITFWMATCH-26OCT17KHOWEI-KHO`) | 0.47 / 0.52 (7977) | 49.5% | 52.3% | 92.9% | 78.6% [60.0%-85.5%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sijia Wei (`KXITFWMATCH-26OCT17KHOWEI-WEI`) | 0.48 / 0.52 (6102) | 50.0% | 47.7% | 7.1% | 21.3% [14.5%-40.0%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.3 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3178.0, B 2150.0; serve-point win A 56.4%, B 44.1%; Elo A 1665.8, B 1716.7; model uncertainty 0.1275
* Form inputs: days since last match A 271, B 12; matches on record A 171, B 308; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.022, surface_pool_high -0.020, surface_dev_loose +0.007, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yu Shan vs Anna Yang -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17SHAYAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yu Shan (`KXITFWMATCH-26OCT17SHAYAN-SHA`) | 0.04 / 0.97 (285) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anna Yang (`KXITFWMATCH-26OCT17SHAYAN-YAN`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Junjie Sun vs Chihiro Muramatsu -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17SUNMUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chihiro Muramatsu (`KXITFWMATCH-26OCT17SUNMUR-MUR`) | 0.04 / 0.97 (285) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Junjie Sun (`KXITFWMATCH-26OCT17SUNMUR-SUN`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jiayu Xu vs Kanna Soeda -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17XUXSOE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanna Soeda (`KXITFWMATCH-26OCT17XUXSOE-SOE`) | 0.04 / 0.97 (285) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jiayu Xu (`KXITFWMATCH-26OCT17XUXSOE-XUX`) | 0.04 / 0.97 (263) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ma / Passola vs Rencheli / Sholokhova -- W35 Redding CA F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:15Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-18T08:15:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17MAXPASRENSHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ma / Passola (`KXITFWDOUBLES-26OCT17MAXPASRENSHO-MAXPAS`) | 0.08 / 0.52 (52) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rencheli / Sholokhova (`KXITFWDOUBLES-26OCT17MAXPASRENSHO-RENSHO`) | 0.41 / 0.69 (80) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alejandro Davidovich Fokina vs Rafael Jodar -- ATP Shanghai F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 11:30Z
* Current expected start: 2026-10-18 08:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 07:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-18T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT18DAVJOD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alejandro Davidovich Fokina (`KXATPMATCH-26OCT18DAVJOD-DAV`) | 0.43 / 0.45 (64329) | 44.0% | -- | -- | -- [-----] | -- | 42.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rafael Jodar (`KXATPMATCH-26OCT18DAVJOD-JOD`) | 0.55 / 0.57 (71890) | 56.0% | -- | -- | -- [-----] | -- | 57.2% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nancy Lee vs Saily Prashantkumar Thakkar -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17LEETHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nancy Lee (`KXITFWMATCH-26OCT17LEETHA-LEE`) | 0.03 / 0.97 (285) | 50.0% | 77.6% | -- | -- [-----] | -- | -- | -- | -- | -- | +27.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Saily Prashantkumar Thakkar (`KXITFWMATCH-26OCT17LEETHA-THA`) | 0.03 / 0.97 (263) | 50.0% | 22.4% | -- | -- [-----] | -- | -- | -- | -- | -- | -27.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 55.2%, B 50.4%; Elo A 1286.3, B 1183.5; model uncertainty None
* Form inputs: days since last match A 341, B 173; matches on record A 1, B 11; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17LEETHA-LEE  (YES = Nancy Lee)
Model: 78%
Kalshi: 50%
Gap: +28 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Moeka Miyata vs Niyati Hiranandani Bhandari -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17MIYBHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Niyati Hiranandani Bhandari (`KXITFWMATCH-26OCT17MIYBHA-BHA`) | 0.03 / 0.97 (285) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Moeka Miyata (`KXITFWMATCH-26OCT17MIYBHA-MIY`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Saina Jayesh Vaidya vs Saumrita Jagatdeo Verma -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17VAIVER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Saina Jayesh Vaidya (`KXITFWMATCH-26OCT17VAIVER-VAI`) | 0.03 / 0.97 (285) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Saumrita Jagatdeo Verma (`KXITFWMATCH-26OCT17VAIVER-VER`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Caitlin Diane Woo vs Violet Apisah -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17WOOAPI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Violet Apisah (`KXITFWMATCH-26OCT17WOOAPI-API`) | 0.03 / 0.97 (285) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Caitlin Diane Woo (`KXITFWMATCH-26OCT17WOOAPI-WOO`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zi Xuan Yang vs Amodini Naik -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17YANNAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amodini Naik (`KXITFWMATCH-26OCT17YANNAI-NAI`) | 0.03 / 0.97 (285) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zi Xuan Yang (`KXITFWMATCH-26OCT17YANNAI-YAN`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Terence Atmane vs Rinky Hijikata -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208014:209279:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Terence Atmane (`KXATPMATCH-26OCT18ATMHIJ-ATM`) | 0.59 / 0.62 (248) | 60.5% | 47.1% | 54.9% | 52.9% [48.5%-54.4%] | -- | -- | -- | -- | PASS | -13.3 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rinky Hijikata (`KXATPMATCH-26OCT18ATMHIJ-HIJ`) | 0.40 / 0.41 (57) | 40.5% | 52.8% | 45.1% | 47.1% [45.6%-51.5%] | -- | -- | -- | -- | SHADOW_BET | +12.3 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4446.0, B 5282.0; serve-point win A 65.7%, B 33.7%; Elo A 1764.1, B 1794.6; model uncertainty 0.0292
* Form inputs: days since last match A 12, B 10; matches on record A 397, B 434; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18ATMHIJ-1-HIJ` Will Rinky Hijikata win set 1 in the Terence Atmane vs Rinky Hijikata match: 0.03/0.95 mid 49.0%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ATMHIJ-2-HIJ` Will Rinky Hijikata win set 2 in the Terence Atmane vs Rinky Hijikata match: 0.06/0.95 mid 50.5%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ATMHIJ-1-ATM` Will Terence Atmane win set 1 in the Terence Atmane vs Rinky Hijikata match: 0.03/0.95 mid 49.0%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ATMHIJ-2-ATM` Will Terence Atmane win set 2 in the Terence Atmane vs Rinky Hijikata match: 0.03/0.92 mid 47.5%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## N. Sriram Balaji / Evan King vs Anirudh Chandrasekar / Ray Ho -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18BALKINCHARAY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N. Sriram Balaji / Evan King (`KXATPDOUBLES-26OCT18BALKINCHARAY-BALKIN`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anirudh Chandrasekar / Ray Ho (`KXATPDOUBLES-26OCT18BALKINCHARAY-CHARAY`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mattia Bellucci vs Tomas Martin Etcheverry -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144869:208233:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mattia Bellucci (`KXATPMATCH-26OCT18BELETC-BEL`) | 0.48 / 0.52 (6100) | 50.0% | 57.8% | 48.5% | 50.0% [49.5%-51.5%] | -- | -- | -- | -- | PASS | +7.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tomas Martin Etcheverry (`KXATPMATCH-26OCT18BELETC-ETC`) | 0.47 / 0.51 (6180) | 49.0% | 42.2% | 51.4% | 50.0% [48.5%-50.5%] | -- | -- | -- | -- | PASS | -6.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4439.0, B 5437.0; serve-point win A 67.4%, B 34.3%; Elo A 1795.9, B 1757.3; model uncertainty 0.0097
* Form inputs: days since last match A 10, B 7; matches on record A 394, B 635; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT18BELETC-ETC20` Will Tomas Martin Etcheverry win the Mattia Bellucci vs Tomas Martin Etcheverry match by a set score of 2-0?: 0.01/0.93 mid 47.0%, model 20.1% (projection_v2.0 (prediction ledger)) -- gap -26.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BELETC-ETC21` Will Tomas Martin Etcheverry win the Mattia Bellucci vs Tomas Martin Etcheverry match by a set score of 2-1?: 0.01/0.95 mid 48.0%, model 22.1% (projection_v2.0 (prediction ledger)) -- gap -25.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BELETC-BEL21` Will Mattia Bellucci win the Mattia Bellucci vs Tomas Martin Etcheverry match by a set score of 2-1?: 0.01/0.93 mid 47.0%, model 27.3% (projection_v2.0 (prediction ledger)) -- gap -19.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18BELETC-BEL20` Will Mattia Bellucci win the Mattia Bellucci vs Tomas Martin Etcheverry match by a set score of 2-0?: 0.01/0.93 mid 47.0%, model 30.5% (projection_v2.0 (prediction ledger)) -- gap -16.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BELETC-1-BEL` Will Mattia Bellucci win set 1 in the Mattia Bellucci vs Tomas Martin Etcheverry match: 0.02/0.93 mid 47.5%, model 55.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BELETC-2-BEL` Will Mattia Bellucci win set 2 in the Mattia Bellucci vs Tomas Martin Etcheverry match: 0.03/0.95 mid 49.0%, model 55.2% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BELETC-1-ETC` Will Tomas Martin Etcheverry win set 1 in the Mattia Bellucci vs Tomas Martin Etcheverry match: 0.05/0.96 mid 50.5%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap -5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BELETC-2-ETC` Will Tomas Martin Etcheverry win set 2 in the Mattia Bellucci vs Tomas Martin Etcheverry match: 0.03/0.95 mid 49.0%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Luciano Darderi / Tomas Martin Etcheverry vs Jason Kubler / John Peers -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18DARETCKUBPEE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciano Darderi / Tomas Martin Etcheverry (`KXATPDOUBLES-26OCT18DARETCKUBPEE-DARETC`) | 0.09 / 0.89 (132) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jason Kubler / John Peers (`KXATPDOUBLES-26OCT18DARETCKUBPEE-KUBPEE`) | 0.05 / 0.90 (130) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alexander Donski / Filip Pieczonka vs Arthur Reymond / Luca Sanchez -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18DONPIEREYSAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Donski / Filip Pieczonka (`KXATPDOUBLES-26OCT18DONPIEREYSAN-DONPIE`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arthur Reymond / Luca Sanchez (`KXATPDOUBLES-26OCT18DONPIEREYSAN-REYSAN`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sander Gille / Sem Verbeek vs Yuki Bhambri / Ryan Seggerman -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18GILVERBHASEG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuki Bhambri / Ryan Seggerman (`KXATPDOUBLES-26OCT18GILVERBHASEG-BHASEG`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sander Gille / Sem Verbeek (`KXATPDOUBLES-26OCT18GILVERBHASEG-GILVER`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Rinky Hijikata / Adam Walton vs Alexander Bublik / Zangar Nurlanuly -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18HIJWALBUBNUR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Bublik / Zangar Nurlanuly (`KXATPDOUBLES-26OCT18HIJWALBUBNUR-BUBNUR`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rinky Hijikata / Adam Walton (`KXATPDOUBLES-26OCT18HIJWALBUBNUR-HIJWAL`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Miomir Kecmanovic vs James Duckworth -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105902:200175:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Duckworth (`KXATPMATCH-26OCT18KECDUC-DUC`) | 0.37 / 0.41 (78) | 39.0% | 37.7% | 45.6% | 45.1% [45.1%-45.6%] | -- | -- | -- | -- | SHADOW_BET | -1.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Miomir Kecmanovic (`KXATPMATCH-26OCT18KECDUC-KEC`) | 0.58 / 0.63 (7493) | 60.5% | 62.3% | 54.4% | 54.9% [54.4%-54.9%] | -- | -- | -- | -- | PASS | +1.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5396.0, B 5242.0; serve-point win A 67.4%, B 35.1%; Elo A 1788.4, B 1745.5; model uncertainty 0.0025
* Form inputs: days since last match A 10, B 9; matches on record A 606, B 896; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18KECDUC-1-KEC` Will Miomir Kecmanovic win set 1 in the Miomir Kecmanovic vs James Duckworth match: 0.06/0.92 mid 49.0%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18KECDUC-2-KEC` Will Miomir Kecmanovic win set 2 in the Miomir Kecmanovic vs James Duckworth match: 0.03/0.95 mid 49.0%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18KECDUC-1-DUC` Will James Duckworth win set 1 in the Miomir Kecmanovic vs James Duckworth match: 0.06/0.92 mid 49.0%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap -7.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18KECDUC-2-DUC` Will James Duckworth win set 2 in the Miomir Kecmanovic vs James Duckworth match: 0.03/0.95 mid 49.0%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap -7.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nathaniel Lammons / Jackson Withrow vs Jakob Schnaitter / Mark Wallner -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18LAMWITSCHWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nathaniel Lammons / Jackson Withrow (`KXATPDOUBLES-26OCT18LAMWITSCHWAL-LAMWIT`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jakob Schnaitter / Mark Wallner (`KXATPDOUBLES-26OCT18LAMWITSCHWAL-SCHWAL`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Adrian Mannarino vs Aleksandar Vukic -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105173:126846:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Mannarino (`KXATPMATCH-26OCT18MANVUK-MAN`) | 0.58 / 0.60 (603) | 59.0% | 48.8% | 57.3% | 56.3% [55.9%-57.3%] | -- | -- | -- | -- | PASS | -10.2 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aleksandar Vukic (`KXATPMATCH-26OCT18MANVUK-VUK`) | 0.38 / 0.42 (6113) | 40.0% | 51.2% | 42.7% | 43.7% [42.7%-44.1%] | -- | -- | -- | -- | PASS | +11.2 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4276.0, B 4441.0; serve-point win A 65.8%, B 33.9%; Elo A 1772.8, B 1736.9; model uncertainty 0.0071
* Form inputs: days since last match A 6, B 11; matches on record A 1273, B 591; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT18MANVUK-VUK21` Will Aleksandar Vukic win the Adrian Mannarino vs Aleksandar Vukic match by a set score of 2-1?: 0.02/0.97 mid 49.5%, model 25.4% (projection_v2.0 (prediction ledger)) -- gap -24.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MANVUK-VUK20` Will Aleksandar Vukic win the Adrian Mannarino vs Aleksandar Vukic match by a set score of 2-0?: 0.02/0.97 mid 49.5%, model 25.8% (projection_v2.0 (prediction ledger)) -- gap -23.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MANVUK-1-VUK` Will Aleksandar Vukic win set 1 in the Adrian Mannarino vs Aleksandar Vukic match: 0.02/0.95 mid 48.5%, model 50.8% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MANVUK-2-VUK` Will Aleksandar Vukic win set 2 in the Adrian Mannarino vs Aleksandar Vukic match: 0.02/0.95 mid 48.5%, model 50.8% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MANVUK-MAN21` Will Adrian Mannarino win the Adrian Mannarino vs Aleksandar Vukic match by a set score of 2-1?: 0.02/0.50 mid 26.0%, model 24.6% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18MANVUK-MAN20` Will Adrian Mannarino win the Adrian Mannarino vs Aleksandar Vukic match by a set score of 2-0?: 0.02/0.48 mid 25.0%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MANVUK-1-MAN` Will Adrian Mannarino win set 1 in the Adrian Mannarino vs Aleksandar Vukic match: 0.03/0.95 mid 49.0%, model 49.2% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MANVUK-2-MAN` Will Adrian Mannarino win set 2 in the Adrian Mannarino vs Aleksandar Vukic match: 0.03/0.95 mid 49.0%, model 49.2% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fabian Marozsan vs Timofey Skatov -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206681:207608:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fabian Marozsan (`KXATPMATCH-26OCT18MARSKA-MAR`) | 0.76 / 0.81 (74) | 78.5% | 73.8% | 70.9% | 72.6% [71.7%-73.8%] | -- | -- | -- | -- | PASS | -4.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Timofey Skatov (`KXATPMATCH-26OCT18MARSKA-SKA`) | 0.17 / 0.24 (7052) | 20.5% | 26.2% | 29.1% | 27.4% [26.2%-28.3%] | -- | -- | -- | -- | PASS | +5.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4574.0, B 4414.0; serve-point win A 66.3%, B 38.8%; Elo A 1778.2, B 1562.5; model uncertainty 0.0103
* Form inputs: days since last match A 9, B 11; matches on record A 439, B 455; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.004, surface_dev_loose +0.012, surface_dev_tight -0.008
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18MARSKA-1-MAR` Will Fabian Marozsan win set 1 in the Fabian Marozsan vs Timofey Skatov match: 0.03/0.94 mid 48.5%, model 66.5% (projection_v2.0 (prediction ledger)) -- gap +18.0 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MARSKA-2-MAR` Will Fabian Marozsan win set 2 in the Fabian Marozsan vs Timofey Skatov match: 0.03/0.95 mid 49.0%, model 66.5% (projection_v2.0 (prediction ledger)) -- gap +17.5 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MARSKA-1-SKA` Will Timofey Skatov win set 1 in the Fabian Marozsan vs Timofey Skatov match: 0.04/0.95 mid 49.5%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap -16.0 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MARSKA-2-SKA` Will Timofey Skatov win set 2 in the Fabian Marozsan vs Timofey Skatov match: 0.03/0.95 mid 49.0%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap -15.5 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lucas Miedler / Neil Oberleitner vs Francisco Cabral / James Tracy -- ATP Shanghai F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18MIEOBECABTRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cabral / James Tracy (`KXATPDOUBLES-26OCT18MIEOBECABTRA-CABTRA`) | 0.45 / 0.48 (188) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26OCT18MIEOBECABTRA-MIEOBE`) | 0.51 / 0.55 (4549) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Lucas Miedler / Neil Oberleitner vs Amir Omarkhanov / Beibit Zhukayev -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18MIEOBEOMAZHU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26OCT18MIEOBEOMAZHU-MIEOBE`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Amir Omarkhanov / Beibit Zhukayev (`KXATPDOUBLES-26OCT18MIEOBEOMAZHU-OMAZHU`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Zangar Nurlanuly vs Tomas Machac -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207830:tml:N0GN:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Machac (`KXATPMATCH-26OCT18NURMAC-MAC`) | 0.92 / 0.93 (37) | 92.5% | 98.2% | 88.3% | 96.2% [94.8%-97.6%] | -- | -- | -- | -- | PASS | +5.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zangar Nurlanuly (`KXATPMATCH-26OCT18NURMAC-NUR`) | 0.05 / 0.07 (6207) | 6.0% | 1.8% | 11.7% | 3.8% [2.4%-5.2%] | -- | -- | -- | -- | PASS | -4.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 195.0, B 3439.0; serve-point win A 54.0%, B 29.4%; Elo A 1329.8, B 1926.2; model uncertainty 0.014
* Form inputs: days since last match A 68, B 8; matches on record A 4, B 440; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.014, surface_dev_loose +0.000, surface_dev_tight -0.001
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18NURMAC-1-MAC` Will Tomas Machac win set 1 in the Zangar Nurlanuly vs Tomas Machac match: 0.03/0.95 mid 49.0%, model 91.9% (projection_v2.0 (prediction ledger)) -- gap +42.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18NURMAC-2-MAC` Will Tomas Machac win set 2 in the Zangar Nurlanuly vs Tomas Machac match: 0.03/0.95 mid 49.0%, model 91.9% (projection_v2.0 (prediction ledger)) -- gap +42.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18NURMAC-1-NUR` Will Zangar Nurlanuly win set 1 in the Zangar Nurlanuly vs Tomas Machac match: 0.03/0.95 mid 49.0%, model 8.1% (projection_v2.0 (prediction ledger)) -- gap -40.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18NURMAC-2-NUR` Will Zangar Nurlanuly win set 2 in the Zangar Nurlanuly vs Tomas Machac match: 0.03/0.95 mid 49.0%, model 8.1% (projection_v2.0 (prediction ledger)) -- gap -40.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPEXACTMATCH-26OCT18NURMAC-MAC20` Will Tomas Machac win the Zangar Nurlanuly vs Tomas Machac match by a set score of 2-0?: 0.02/0.96 mid 49.0%, model 84.5% (projection_v2.0 (prediction ledger)) -- gap +35.5 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT18NURMAC-MAC21` Will Tomas Machac win the Zangar Nurlanuly vs Tomas Machac match by a set score of 2-1?: 0.02/0.96 mid 49.0%, model 13.6% (projection_v2.0 (prediction ledger)) -- gap -35.4 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data POOR
* Warnings: BET_BLOCKED_START_STATUS; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jean-Julien Rojer / Theodore Winegar vs Facundo Diaz Acosta / Thiago Agustin Tirante -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18ROJWINDIATIR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Facundo Diaz Acosta / Thiago Agustin Tirante (`KXATPDOUBLES-26OCT18ROJWINDIATIR-DIATIR`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jean-Julien Rojer / Theodore Winegar (`KXATPDOUBLES-26OCT18ROJWINDIATIR-ROJWIN`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Thiago Agustin Tirante vs Facundo Diaz Acosta -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:202058:207680:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Facundo Diaz Acosta (`KXATPMATCH-26OCT18TIRDIA-DIA`) | 0.26 / 0.27 (9) | 26.5% | 39.5% | 46.5% | 43.6% [39.2%-45.5%] | -- | -- | -- | -- | PASS | +13.0 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thiago Agustin Tirante (`KXATPMATCH-26OCT18TIRDIA-TIR`) | 0.69 / 0.74 (112) | 71.5% | 60.5% | 53.5% | 56.4% [54.5%-60.8%] | -- | -- | -- | -- | PASS | -11.0 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4745.0, B 5003.0; serve-point win A 65.1%, B 37.0%; Elo A 1741.7, B 1628.9; model uncertainty 0.0317
* Form inputs: days since last match A 7, B 9; matches on record A 449, B 449; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose +0.029, surface_dev_tight -0.020
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT18TIRDIA-DIA20` Will Facundo Diaz Acosta win the Thiago Agustin Tirante vs Facundo Diaz Acosta match by a set score of 2-0?: 0.02/0.76 mid 39.0%, model 18.4% (projection_v2.0 (prediction ledger)) -- gap -20.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18TIRDIA-DIA21` Will Facundo Diaz Acosta win the Thiago Agustin Tirante vs Facundo Diaz Acosta match by a set score of 2-1?: 0.02/0.76 mid 39.0%, model 21.0% (projection_v2.0 (prediction ledger)) -- gap -18.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18TIRDIA-TIR21` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Facundo Diaz Acosta match by a set score of 2-1?: 0.02/0.72 mid 37.0%, model 28.0% (projection_v2.0 (prediction ledger)) -- gap -9.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TIRDIA-1-TIR` Will Thiago Agustin Tirante win set 1 in the Thiago Agustin Tirante vs Facundo Diaz Acosta match: 0.03/0.95 mid 49.0%, model 57.1% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TIRDIA-2-TIR` Will Thiago Agustin Tirante win set 2 in the Thiago Agustin Tirante vs Facundo Diaz Acosta match: 0.03/0.95 mid 49.0%, model 57.1% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TIRDIA-1-DIA` Will Facundo Diaz Acosta win set 1 in the Thiago Agustin Tirante vs Facundo Diaz Acosta match: 0.03/0.95 mid 49.0%, model 42.9% (projection_v2.0 (prediction ledger)) -- gap -6.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TIRDIA-2-DIA` Will Facundo Diaz Acosta win set 2 in the Thiago Agustin Tirante vs Facundo Diaz Acosta match: 0.03/0.95 mid 49.0%, model 42.9% (projection_v2.0 (prediction ledger)) -- gap -6.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18TIRDIA-TIR20` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Facundo Diaz Acosta match by a set score of 2-0?: 0.01/0.75 mid 38.0%, model 32.6% (projection_v2.0 (prediction ledger)) -- gap -5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Stefanos Tsitsipas vs Aleksandar Kovacevic -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126774:206499:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksandar Kovacevic (`KXATPMATCH-26OCT18TSIKOV-KOV`) | 0.21 / 0.26 (53) | 23.5% | 27.0% | 32.6% | 30.5% [23.5%-35.1%] | -- | -- | -- | -- | PASS | +3.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefanos Tsitsipas (`KXATPMATCH-26OCT18TSIKOV-TSI`) | 0.72 / 0.78 (150) | 75.0% | 73.0% | 67.4% | 69.5% [64.9%-76.5%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5084.0, B 4809.0; serve-point win A 73.1%, B 32.2%; Elo A 1952.1, B 1756.9; model uncertainty 0.0581
* Form inputs: days since last match A 3, B 10; matches on record A 801, B 399; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.039, surface_pool_high -0.046, surface_dev_loose -0.008, surface_dev_tight +0.013
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18TSIKOV-1-TSI` Will Stefanos Tsitsipas win set 1 in the Stefanos Tsitsipas vs Aleksandar Kovacevic match: 0.03/0.95 mid 49.0%, model 65.9% (projection_v2.0 (prediction ledger)) -- gap +16.9 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TSIKOV-2-TSI` Will Stefanos Tsitsipas win set 2 in the Stefanos Tsitsipas vs Aleksandar Kovacevic match: 0.03/0.95 mid 49.0%, model 65.9% (projection_v2.0 (prediction ledger)) -- gap +16.9 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TSIKOV-1-KOV` Will Aleksandar Kovacevic win set 1 in the Stefanos Tsitsipas vs Aleksandar Kovacevic match: 0.03/0.95 mid 49.0%, model 34.1% (projection_v2.0 (prediction ledger)) -- gap -14.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TSIKOV-2-KOV` Will Aleksandar Kovacevic win set 2 in the Stefanos Tsitsipas vs Aleksandar Kovacevic match: 0.03/0.95 mid 49.0%, model 34.1% (projection_v2.0 (prediction ledger)) -- gap -14.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yanan Hou vs chengwei Han -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17HOUHAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| chengwei Han (`KXITFWMATCH-26OCT17HOUHAN-HAN`) | 0.04 / 0.95 (27) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yanan Hou (`KXITFWMATCH-26OCT17HOUHAN-HOU`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zijun Jiang vs Zihan Yang -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17JIAYAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zijun Jiang (`KXITFWMATCH-26OCT17JIAYAN-JIA`) | 0.04 / 0.97 (285) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zihan Yang (`KXITFWMATCH-26OCT17JIAYAN-YAN`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xichen Zhao vs WENFEI YU -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17ZHAYUX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WENFEI YU (`KXITFWMATCH-26OCT17ZHAYUX-YUX`) | 0.04 / 0.97 (285) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xichen Zhao (`KXITFWMATCH-26OCT17ZHAYUX-ZHA`) | 0.03 / 0.92 (20) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Samir Banerjee vs Karan Singh -- M25 Solapur F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209079:210000:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samir Banerjee (`KXITFMATCH-26OCT17BANSIN-BAN`) | 0.23 / 0.67 (75) | 45.0% | 72.2% | 78.4% | 68.5% [66.5%-70.0%] | -- | -- | -- | -- | PASS | +27.2 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Karan Singh (`KXITFMATCH-26OCT17BANSIN-SIN`) | 0.16 / 0.55 (55) | 35.5% | 27.8% | 21.6% | 31.4% [30.0%-33.5%] | -- | -- | -- | -- | PASS | -7.7 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 167.0, B 1139.0; serve-point win A 64.4%, B 40.2%; Elo A 1460.8, B 1336.3; model uncertainty 0.0173
* Form inputs: days since last match A 705, B 82; matches on record A 74, B 178; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT17BANSIN-BAN  (YES = Samir Banerjee)
Model: 72%
Kalshi: 45%
Gap: +27 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aleksandr Shevchenko vs Stefanos Sakellaridis -- ATP Almaty Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 13:00Z
* Current expected start: 2026-10-18 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 09:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT18SHESAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefanos Sakellaridis (`KXATPMATCH-26OCT18SHESAK-SAK`) | 0.06 / 0.94 (222) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aleksandr Shevchenko (`KXATPMATCH-26OCT18SHESAK-SHE`) | 0.06 / 0.94 (200) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Na Hyun Kang vs Mirudhula Palanivel -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18KANPAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Na Hyun Kang (`KXITFWMATCH-26OCT18KANPAL-KAN`) | 0.03 / 0.95 (27) | 49.0% | 84.1% | -- | -- [-----] | -- | -- | -- | -- | -- | +35.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mirudhula Palanivel (`KXITFWMATCH-26OCT18KANPAL-PAL`) | 0.03 / 0.97 (263) | 50.0% | 15.9% | -- | -- [-----] | -- | -- | -- | -- | -- | -34.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 56.3%, B 51.2%; Elo A 1286.1, B 1176.6; model uncertainty None
* Form inputs: days since last match A 173, B 397; matches on record A 31, B 12; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18KANPAL-KAN  (YES = Na Hyun Kang)
Model: 84%
Kalshi: 49%
Gap: +35 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aditi Rawat vs Kelly Yi Xian CHEN -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18RAWCHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kelly Yi Xian CHEN (`KXITFWMATCH-26OCT18RAWCHE-CHE`) | 0.03 / 0.97 (285) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aditi Rawat (`KXITFWMATCH-26OCT18RAWCHE-RAW`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jiho Shin vs Lulwa Naswardhani -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18SHINAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lulwa Naswardhani (`KXITFWMATCH-26OCT18SHINAS-NAS`) | 0.03 / 0.97 (285) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jiho Shin (`KXITFWMATCH-26OCT18SHINAS-SHI`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nirelle Yasin vs Bela Tamhankar -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18YASTAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bela Tamhankar (`KXITFWMATCH-26OCT18YASTAM-TAM`) | 0.03 / 0.95 (27) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nirelle Yasin (`KXITFWMATCH-26OCT18YASTAM-YAS`) | 0.03 / 0.95 (27) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Minxu Zhou vs Nalu Himeno -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18ZHOHIM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nalu Himeno (`KXITFWMATCH-26OCT18ZHOHIM-HIM`) | 0.03 / 0.97 (285) | 50.0% | 22.1% | -- | -- [-----] | -- | -- | -- | -- | -- | -27.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Minxu Zhou (`KXITFWMATCH-26OCT18ZHOHIM-ZHO`) | 0.03 / 0.97 (263) | 50.0% | 77.9% | -- | -- [-----] | -- | -- | -- | -- | -- | +27.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 56.4%, B 49.4%; Elo A 1278.5, B 1094.5; model uncertainty None
* Form inputs: days since last match A 698, B 222; matches on record A 3, B 20; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT18ZHOHIM-ZHO  (YES = Minxu Zhou)
Model: 78%
Kalshi: 50%
Gap: +28 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maja Chwalinska vs Sonay Kartal -- WTA Wuhan F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-18 13:30Z
* Current expected start: 2026-10-18 10:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: 2026-10-18 09:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT18CHWKAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maja Chwalinska (`KXWTAMATCH-26OCT18CHWKAR-CHW`) | 0.41 / 0.46 (785) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sonay Kartal (`KXWTAMATCH-26OCT18CHWKAR-KAR`) | 0.50 / 0.57 (40) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Yeongseok Jeong vs Henry De Keulenaer -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18JEODEK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Henry De Keulenaer (`KXITFMATCH-26OCT18JEODEK-DEK`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yeongseok Jeong (`KXITFMATCH-26OCT18JEODEK-JEO`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ren Nakamura vs Julien Tremolieres -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18NAKTRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ren Nakamura (`KXITFMATCH-26OCT18NAKTRE-NAK`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Julien Tremolieres (`KXITFMATCH-26OCT18NAKTRE-TRE`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Guillermo Olaso vs Charles Josshua Kinaadman -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18OLAKIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charles Josshua Kinaadman (`KXITFMATCH-26OCT18OLAKIN-KIN`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Guillermo Olaso (`KXITFMATCH-26OCT18OLAKIN-OLA`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marko Retelj vs Roy Hobbs -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18RETHOB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Roy Hobbs (`KXITFMATCH-26OCT18RETHOB-HOB`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marko Retelj (`KXITFMATCH-26OCT18RETHOB-RET`) | 0.03 / 0.97 (363) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Meng Yi Chen vs Junlu Sun -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18CHESUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Meng Yi Chen (`KXITFWMATCH-26OCT18CHESUN-CHE`) | 0.04 / 0.97 (285) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Junlu Sun (`KXITFWMATCH-26OCT18CHESUN-SUN`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yui Chikaraishi vs Jasmin Jebawy -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18CHIJEB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yui Chikaraishi (`KXITFWMATCH-26OCT18CHIJEB-CHI`) | 0.04 / 0.97 (285) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jasmin Jebawy (`KXITFWMATCH-26OCT18CHIJEB-JEB`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jasmine Lin vs Liuyan An -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18LINANX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liuyan An (`KXITFWMATCH-26OCT18LINANX-ANX`) | 0.04 / 0.97 (285) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jasmine Lin (`KXITFWMATCH-26OCT18LINANX-LIN`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jiumeng Liu vs Xiaowei Li -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18LIULIX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiumeng Liu (`KXITFWMATCH-26OCT18LIULIX-LIU`) | 0.04 / 0.97 (285) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xiaowei Li (`KXITFWMATCH-26OCT18LIULIX-LIX`) | 0.03 / 0.97 (263) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Darja Suvirdjonkova vs Guyu Xu -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18SUVXUX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Darja Suvirdjonkova (`KXITFWMATCH-26OCT18SUVXUX-SUV`) | 0.04 / 0.97 (285) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Guyu Xu (`KXITFWMATCH-26OCT18SUVXUX-XUX`) | 0.03 / 0.94 (33) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jialan Cai vs Ke Ren -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18CAIREN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jialan Cai (`KXITFWMATCH-26OCT18CAIREN-CAI`) | 0.04 / 0.97 (235) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ke Ren (`KXITFWMATCH-26OCT18CAIREN-REN`) | 0.03 / 0.97 (213) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marika Jones vs Yiru Chen -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18JONCHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yiru Chen (`KXITFWMATCH-26OCT18JONCHE-CHE`) | 0.04 / 0.97 (235) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marika Jones (`KXITFWMATCH-26OCT18JONCHE-JON`) | 0.03 / 0.97 (213) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xi Luo vs Sitong Chen -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18LUOCHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sitong Chen (`KXITFWMATCH-26OCT18LUOCHE-CHE`) | 0.04 / 0.97 (235) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xi Luo (`KXITFWMATCH-26OCT18LUOCHE-LUO`) | 0.03 / 0.97 (213) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zi Ye Zhang vs Ekaterina Kuznetsova -- W35 Qian Daohu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18ZHAKUZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Kuznetsova (`KXITFWMATCH-26OCT18ZHAKUZ-KUZ`) | 0.04 / 0.97 (235) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zi Ye Zhang (`KXITFWMATCH-26OCT18ZHAKUZ-ZHA`) | 0.03 / 0.97 (213) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eric Ahren Moonga vs Tobias Albig -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18AHRALB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eric Ahren Moonga (`KXITFMATCH-26OCT18AHRALB-AHR`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tobias Albig (`KXITFMATCH-26OCT18AHRALB-ALB`) | 0.03 / 0.97 (313) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hong-Lin Fu vs Taentawan Taddeo Majoli Maggioli -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18FUXMAJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hong-Lin Fu (`KXITFMATCH-26OCT18FUXMAJ-FUX`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Taentawan Taddeo Majoli Maggioli (`KXITFMATCH-26OCT18FUXMAJ-MAJ`) | 0.03 / 0.97 (313) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luke Jie Xi Ho vs Yoan Naydenov -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18HOXNAY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luke Jie Xi Ho (`KXITFMATCH-26OCT18HOXNAY-HOX`) | 0.05 / 0.95 (30) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yoan Naydenov (`KXITFMATCH-26OCT18HOXNAY-NAY`) | 0.03 / 0.97 (313) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luke Koh vs Aditya Kothari -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18KOHKOT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luke Koh (`KXITFMATCH-26OCT18KOHKOT-KOH`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aditya Kothari (`KXITFMATCH-26OCT18KOHKOT-KOT`) | 0.05 / 0.95 (30) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michael Ng vs Hendrik Thada Grohbruegge -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18NGXGRO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hendrik Thada Grohbruegge (`KXITFMATCH-26OCT18NGXGRO-GRO`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Michael Ng (`KXITFMATCH-26OCT18NGXGRO-NGX`) | 0.03 / 0.97 (313) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oskari Paldanius vs Romain Faucon -- M15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18PALFAU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romain Faucon (`KXITFMATCH-26OCT18PALFAU-FAU`) | 0.04 / 0.96 (19) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oskari Paldanius (`KXITFMATCH-26OCT18PALFAU-PAL`) | 0.04 / 0.96 (19) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carolina Alves vs Alena Kovackova -- W50 Stara Zagora SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18ALVKOV:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carolina Alves (`KXITFWMATCH-26OCT18ALVKOV-ALV`) | 0.04 / 0.96 (15) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alena Kovackova (`KXITFWMATCH-26OCT18ALVKOV-KOV`) | 0.04 / 0.96 (15) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Felitsata Dorofeeva-Rybas vs Giulia Safina Popa -- W15 Chisinau F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18DORPOP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felitsata Dorofeeva-Rybas (`KXITFWMATCH-26OCT18DORPOP-DOR`) | 0.04 / 0.96 (17) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Giulia Safina Popa (`KXITFWMATCH-26OCT18DORPOP-POP`) | 0.04 / 0.96 (17) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ipek Oz vs Lucie Petruzelova -- W50 Stara Zagora SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18OZXPET:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ipek Oz (`KXITFWMATCH-26OCT18OZXPET-OZX`) | 0.03 / 0.97 (212) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucie Petruzelova (`KXITFWMATCH-26OCT18OZXPET-PET`) | 0.03 / 0.97 (212) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuliya Perapekhina vs Lamis Alhussein Abdel Aziz -- W15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-18T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT18PERALH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lamis Alhussein Abdel Aziz (`KXITFWMATCH-26OCT18PERALH-ALH`) | 0.03 / 0.97 (212) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yuliya Perapekhina (`KXITFWMATCH-26OCT18PERALH-PER`) | 0.03 / 0.97 (212) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Guido Andreozzi / Manuel Guinard vs Michael Geerts / Joran Vliegen -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18ANDGUIGEEVLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guido Andreozzi / Manuel Guinard (`KXATPDOUBLES-26OCT18ANDGUIGEEVLI-ANDGUI`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Michael Geerts / Joran Vliegen (`KXATPDOUBLES-26OCT18ANDGUIGEEVLI-GEEVLI`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sander Arends / Luke Johnson vs Orlando Luz / Rafael Matos -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18AREJOHLUZMAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sander Arends / Luke Johnson (`KXATPDOUBLES-26OCT18AREJOHLUZMAT-AREJOH`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Orlando Luz / Rafael Matos (`KXATPDOUBLES-26OCT18AREJOHLUZMAT-LUZMAT`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nicolas Barrientos / David Pel vs Marcelo Melo / John-Patrick Smith -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18BARPELMELSMI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Barrientos / David Pel (`KXATPDOUBLES-26OCT18BARPELMELSMI-BARPEL`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marcelo Melo / John-Patrick Smith (`KXATPDOUBLES-26OCT18BARPELMELSMI-MELSMI`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Remy Bertola vs Federico Cina -- ATP Brussels Q3

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT18BERCIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Remy Bertola (`KXATPMATCH-26OCT18BERCIN-BER`) | 0.08 / 0.94 (222) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Federico Cina (`KXATPMATCH-26OCT18BERCIN-CIN`) | 0.06 / 0.94 (200) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Francisco Cerundolo / Alex Michelsen vs Zizou Bergs / Alexander Blockx -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18CERMICBERBLO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zizou Bergs / Alexander Blockx (`KXATPDOUBLES-26OCT18CERMICBERBLO-BERBLO`) | 0.18 / 0.90 (10) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Francisco Cerundolo / Alex Michelsen (`KXATPDOUBLES-26OCT18CERMICBERBLO-CERMIC`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Clement Chidekh vs Gauthier Onclin -- ATP Brussels Q3

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT18CHIONC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clement Chidekh (`KXATPMATCH-26OCT18CHIONC-CHI`) | 0.06 / 0.94 (222) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gauthier Onclin (`KXATPMATCH-26OCT18CHIONC-ONC`) | 0.06 / 0.94 (200) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Raphael Collignon / David Goffin vs Marc Polmans / Jan Zielinski -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18COLGOFPOLZIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raphael Collignon / David Goffin (`KXATPDOUBLES-26OCT18COLGOFPOLZIE-COLGOF`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marc Polmans / Jan Zielinski (`KXATPDOUBLES-26OCT18COLGOFPOLZIE-POLZIE`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sadio Doumbia / Bart Stevens vs Maximo Gonzalez / Andres Molteni -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18DOUSTEGONMOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sadio Doumbia / Bart Stevens (`KXATPDOUBLES-26OCT18DOUSTEGONMOL-DOUSTE`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maximo Gonzalez / Andres Molteni (`KXATPDOUBLES-26OCT18DOUSTEGONMOL-GONMOL`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jacob Fearnley vs Hugo Gaston -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200384:207985:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacob Fearnley (`KXATPMATCH-26OCT18FEAGAS-FEA`) | 0.67 / 0.69 (808) | 68.0% | 58.6% | 55.6% | 55.6% [53.6%-57.2%] | -- | 69.9% | -- | INSUFFICIENT_INPUTS | PASS | -9.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hugo Gaston (`KXATPMATCH-26OCT18FEAGAS-GAS`) | 0.31 / 0.33 (6216) | 32.0% | 41.4% | 44.4% | 44.4% [42.8%-46.4%] | -- | 30.4% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +9.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4058.0, B 4582.0; serve-point win A 61.0%, B 40.6%; Elo A 1773.0, B 1728.8; model uncertainty 0.0179
* Form inputs: days since last match A 19, B 12; matches on record A 178, B 502; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT18FEAGAS-GAS21` Will Hugo Gaston win the Jacob Fearnley vs Hugo Gaston match by a set score of 2-1?: 0.02/0.17 mid 9.5%, model 21.8% (projection_v2.0 (prediction ledger)) -- gap +12.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18FEAGAS-FEA4` Will Jacob Fearnley win at least 3.5 more games than Hugo Gaston?: 0.46/0.49 mid 47.5%, model 36.2% (projection_v2.0 (prediction ledger)) -- gap -11.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18FEAGAS-GAS2` Will Hugo Gaston win at least 1.5 more games than Jacob Fearnley?: 0.21/0.26 mid 23.5%, model 34.7% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18FEAGAS-FEA21` Will Jacob Fearnley win the Jacob Fearnley vs Hugo Gaston match by a set score of 2-1?: 0.07/0.26 mid 16.5%, model 27.5% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18FEAGAS-GAS20` Will Hugo Gaston win the Jacob Fearnley vs Hugo Gaston match by a set score of 2-0?: 0.02/0.16 mid 9.0%, model 19.6% (projection_v2.0 (prediction ledger)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FEAGAS-1-GAS` Will Hugo Gaston win set 1 in the Jacob Fearnley vs Hugo Gaston match: 0.33/0.37 mid 35.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18FEAGAS-23` Over 22.5 games: 0.45/0.52 mid 48.5%, model 57.7% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FEAGAS-1-FEA` Will Jacob Fearnley win set 1 in the Jacob Fearnley vs Hugo Gaston match: 0.62/0.67 mid 64.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap -8.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18FEAGAS-18` Over 17.5 games: 0.65/0.99 mid 82.0%, model 90.3% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FEAGAS-2-GAS` Will Hugo Gaston win set 2 in the Jacob Fearnley vs Hugo Gaston match: 0.34/0.38 mid 36.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18FEAGAS-28` Over 27.5 games: 0.11/0.52 mid 31.5%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18FEAGAS-FEA20` Will Jacob Fearnley win the Jacob Fearnley vs Hugo Gaston match by a set score of 2-0?: 0.26/0.46 mid 36.0%, model 31.1% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FEAGAS-2-FEA` Will Jacob Fearnley win set 2 in the Jacob Fearnley vs Hugo Gaston match: 0.55/0.66 mid 60.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tallon Griekspoor vs Max Schoenhaus -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:134868:212268:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tallon Griekspoor (`KXATPMATCH-26OCT18GRISCH-GRI`) | 0.78 / 0.79 (100) | 78.5% | 80.0% | 72.1% | 83.3% [77.7%-89.4%] | -- | 78.8% | -- | INSUFFICIENT_INPUTS | WATCH | +1.5 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Schoenhaus (`KXATPMATCH-26OCT18GRISCH-SCH`) | 0.20 / 0.21 (58) | 20.5% | 20.0% | 27.9% | 16.7% [10.6%-22.3%] | -- | 21.0% | -- | INSUFFICIENT_INPUTS | PASS | -0.5 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4445.0, B 1578.0; serve-point win A 71.4%, B 35.6%; Elo A 1871.5, B 1465.9; model uncertainty 0.0584
* Form inputs: days since last match A 9, B 33; matches on record A 677, B 52; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.028, surface_dev_loose +0.002, surface_dev_tight -0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT18GRISCH-GRI21` Will Tallon Griekspoor win the Tallon Griekspoor vs Max Schoenhaus match by a set score of 2-1?: 0.07/0.27 mid 17.0%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18GRISCH-18` Over 17.5 games: 0.68/0.99 mid 83.5%, model 93.6% (projection_v2.0 (prediction ledger)) -- gap +10.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18GRISCH-23` Over 22.5 games: 0.47/0.52 mid 49.5%, model 56.6% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18GRISCH-GRI7` Will Tallon Griekspoor win at least 6.5 more games than Max Schoenhaus?: 0.12/0.15 mid 13.5%, model 7.6% (projection_v2.0 (prediction ledger)) -- gap -5.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18GRISCH-GRI4` Will Tallon Griekspoor win at least 3.5 more games than Max Schoenhaus?: 0.53/0.55 mid 54.0%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap -5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18GRISCH-GRI20` Will Tallon Griekspoor win the Tallon Griekspoor vs Max Schoenhaus match by a set score of 2-0?: 0.35/0.57 mid 46.0%, model 50.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18GRISCH-28` Over 27.5 games: 0.11/0.52 mid 31.5%, model 36.2% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18GRISCH-SCH21` Will Max Schoenhaus win the Tallon Griekspoor vs Max Schoenhaus match by a set score of 2-1?: 0.02/0.13 mid 7.5%, model 11.8% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18GRISCH-1-GRI` Will Tallon Griekspoor win set 1 in the Tallon Griekspoor vs Max Schoenhaus match: 0.72/0.75 mid 73.5%, model 71.3% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18GRISCH-1-SCH` Will Max Schoenhaus win set 1 in the Tallon Griekspoor vs Max Schoenhaus match: 0.25/0.28 mid 26.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18GRISCH-2-SCH` Will Max Schoenhaus win set 2 in the Tallon Griekspoor vs Max Schoenhaus match: 0.25/0.29 mid 27.0%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18GRISCH-SCH20` Will Max Schoenhaus win the Tallon Griekspoor vs Max Schoenhaus match by a set score of 2-0?: 0.02/0.12 mid 7.0%, model 8.2% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18GRISCH-2-GRI` Will Tallon Griekspoor win set 2 in the Tallon Griekspoor vs Max Schoenhaus match: 0.70/0.75 mid 72.5%, model 71.3% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18GRISCH-SCH2` Will Max Schoenhaus win at least 1.5 more games than Tallon Griekspoor?: 0.14/0.17 mid 15.5%, model 14.5% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tallon Griekspoor / Botic Van de Zandschulp vs Juan Manuel Cerundolo / Benjamin Kittay -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18GRIVANCERKIT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel Cerundolo / Benjamin Kittay (`KXATPDOUBLES-26OCT18GRIVANCERKIT-CERKIT`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tallon Griekspoor / Botic Van de Zandschulp (`KXATPDOUBLES-26OCT18GRIVANCERKIT-GRIVAN`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mariano Navone vs Juan Manuel Cerundolo -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207678:208363:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel Cerundolo (`KXATPMATCH-26OCT18NAVCER-CER`) | 0.39 / 0.41 (363) | 40.0% | 46.6% | 36.5% | 40.4% [38.9%-42.9%] | -- | 40.9% | -- | INSUFFICIENT_INPUTS | PASS | +6.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mariano Navone (`KXATPMATCH-26OCT18NAVCER-NAV`) | 0.56 / 0.59 (7) | 57.5% | 53.4% | 63.5% | 59.6% [57.1%-61.1%] | -- | 59.1% | -- | INSUFFICIENT_INPUTS | PASS | -4.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5176.0, B 5332.0; serve-point win A 61.9%, B 38.8%; Elo A 1725.4, B 1754.7; model uncertainty 0.0199
* Form inputs: days since last match A 9, B 7; matches on record A 410, B 506; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose -0.001, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT18NAVCER-CER21` Will Juan Manuel Cerundolo win the Mariano Navone vs Juan Manuel Cerundolo match by a set score of 2-1?: 0.02/0.21 mid 11.5%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap +12.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18NAVCER-NAV21` Will Mariano Navone win the Mariano Navone vs Juan Manuel Cerundolo match by a set score of 2-1?: 0.05/0.25 mid 15.0%, model 26.1% (projection_v2.0 (prediction ledger)) -- gap +11.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18NAVCER-18` Over 17.5 games: 0.64/0.99 mid 81.5%, model 91.8% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18NAVCER-23` Over 22.5 games: 0.47/0.52 mid 49.5%, model 59.3% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18NAVCER-NAV3` Will Mariano Navone win at least 2.5 more games than Juan Manuel Cerundolo?: 0.47/0.49 mid 48.0%, model 39.7% (projection_v2.0 (prediction ledger)) -- gap -8.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18NAVCER-CER20` Will Juan Manuel Cerundolo win the Mariano Navone vs Juan Manuel Cerundolo match by a set score of 2-0?: 0.04/0.25 mid 14.5%, model 22.8% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18NAVCER-28` Over 27.5 games: 0.11/0.52 mid 31.5%, model 38.7% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18NAVCER-1-CER` Will Juan Manuel Cerundolo win set 1 in the Mariano Navone vs Juan Manuel Cerundolo match: 0.41/0.45 mid 43.0%, model 47.7% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18NAVCER-1-NAV` Will Mariano Navone win set 1 in the Mariano Navone vs Juan Manuel Cerundolo match: 0.55/0.59 mid 57.0%, model 52.3% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18NAVCER-2-CER` Will Juan Manuel Cerundolo win set 2 in the Mariano Navone vs Juan Manuel Cerundolo match: 0.40/0.46 mid 43.0%, model 47.7% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18NAVCER-2-NAV` Will Mariano Navone win set 2 in the Mariano Navone vs Juan Manuel Cerundolo match: 0.54/0.59 mid 56.5%, model 52.3% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18NAVCER-CER2` Will Juan Manuel Cerundolo win at least 1.5 more games than Mariano Navone?: 0.35/0.38 mid 36.5%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18NAVCER-NAV20` Will Mariano Navone win the Mariano Navone vs Juan Manuel Cerundolo match by a set score of 2-0?: 0.16/0.38 mid 27.0%, model 27.3% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Petr Nouza / Michael Venus vs Constantin Frantzen / Robert Galloway -- ATP Brussels R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18NOUVENFRAGAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Constantin Frantzen / Robert Galloway (`KXATPDOUBLES-26OCT18NOUVENFRAGAL-FRAGAL`) | 0.18 / 0.90 (10) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Petr Nouza / Michael Venus (`KXATPDOUBLES-26OCT18NOUVENFRAGAL-NOUVEN`) | 0.05 / 0.90 (10) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Dino Prizmic vs Damir Dzumhur -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106000:209976:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Damir Dzumhur (`KXATPMATCH-26OCT18PRIDZU-DZU`) | 0.29 / 0.36 (6101) | 32.5% | 23.2% | 30.3% | 29.4% [28.5%-31.2%] | -- | 30.3% | -- | INSUFFICIENT_INPUTS | PASS | -9.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dino Prizmic (`KXATPMATCH-26OCT18PRIDZU-PRI`) | 0.64 / 0.68 (112) | 66.0% | 76.8% | 69.7% | 70.6% [68.8%-71.5%] | -- | 69.9% | -- | INSUFFICIENT_INPUTS | WATCH | +10.8 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3904.0, B 4752.0; serve-point win A 63.0%, B 42.6%; Elo A 1827.6, B 1664.3; model uncertainty 0.0138
* Form inputs: days since last match A 26, B 12; matches on record A 223, B 1058; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT18PRIDZU-PRI21` Will Dino Prizmic win the Dino Prizmic vs Damir Dzumhur match by a set score of 2-1?: 0.07/0.26 mid 16.5%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18PRIDZU-PRI20` Will Dino Prizmic win the Dino Prizmic vs Damir Dzumhur match by a set score of 2-0?: 0.26/0.47 mid 36.5%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18PRIDZU-PRI4` Will Dino Prizmic win at least 3.5 more games than Damir Dzumhur?: 0.44/0.53 mid 48.5%, model 55.0% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18PRIDZU-18` Over 17.5 games: 0.61/0.99 mid 80.0%, model 86.0% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18PRIDZU-DZU2` Will Damir Dzumhur win at least 1.5 more games than Dino Prizmic?: 0.19/0.27 mid 23.0%, model 18.1% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18PRIDZU-DZU21` Will Damir Dzumhur win the Dino Prizmic vs Damir Dzumhur match by a set score of 2-1?: 0.02/0.17 mid 9.5%, model 13.4% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18PRIDZU-23` Over 22.5 games: 0.44/0.50 mid 47.0%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18PRIDZU-1-PRI` Will Dino Prizmic win set 1 in the Dino Prizmic vs Damir Dzumhur match: 0.64/0.67 mid 65.5%, model 68.8% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18PRIDZU-2-PRI` Will Dino Prizmic win set 2 in the Dino Prizmic vs Damir Dzumhur match: 0.64/0.67 mid 65.5%, model 68.8% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18PRIDZU-1-DZU` Will Damir Dzumhur win set 1 in the Dino Prizmic vs Damir Dzumhur match: 0.32/0.36 mid 34.0%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18PRIDZU-2-DZU` Will Damir Dzumhur win set 2 in the Dino Prizmic vs Damir Dzumhur match: 0.32/0.36 mid 34.0%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18PRIDZU-28` Over 27.5 games: 0.09/0.50 mid 29.5%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18PRIDZU-DZU20` Will Damir Dzumhur win the Dino Prizmic vs Damir Dzumhur match by a set score of 2-0?: 0.02/0.17 mid 9.5%, model 9.8% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Holger Rune vs Raphael Collignon -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208029:209920:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raphael Collignon (`KXATPMATCH-26OCT18RUNCOL-COL`) | 0.43 / 0.46 (179) | 44.5% | 38.0% | 42.7% | 38.0% [35.6%-39.8%] | -- | 45.3% | -- | INSUFFICIENT_INPUTS | PASS | -6.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Holger Rune (`KXATPMATCH-26OCT18RUNCOL-RUN`) | 0.54 / 0.55 (100) | 54.5% | 62.0% | 57.3% | 62.0% [60.2%-64.4%] | -- | 54.3% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +7.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2551.0, B 5214.0; serve-point win A 67.0%, B 35.5%; Elo A 1972.9, B 1825.6; model uncertainty 0.021
* Form inputs: days since last match A 10, B 47; matches on record A 430, B 351; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.009, surface_dev_loose +0.004, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT18RUNCOL-RUN21` Will Holger Rune win the Holger Rune vs Raphael Collignon match by a set score of 2-1?: 0.05/0.24 mid 14.5%, model 28.3% (projection_v2.0 (prediction ledger)) -- gap +13.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18RUNCOL-COL2` Will Raphael Collignon win at least 1.5 more games than Holger Rune?: 0.38/0.47 mid 42.5%, model 30.6% (projection_v2.0 (prediction ledger)) -- gap -11.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18RUNCOL-RUN20` Will Holger Rune win the Holger Rune vs Raphael Collignon match by a set score of 2-0?: 0.13/0.34 mid 23.5%, model 33.7% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18RUNCOL-RUN2` Will Holger Rune win at least 1.5 more games than Raphael Collignon?: 0.38/0.50 mid 44.0%, model 54.2% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18RUNCOL-30` Over 29.5 games: 0.22/0.29 mid 25.5%, model 33.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18RUNCOL-COL21` Will Raphael Collignon win the Holger Rune vs Raphael Collignon match by a set score of 2-1?: 0.03/0.23 mid 13.0%, model 20.4% (projection_v2.0 (prediction ledger)) -- gap +7.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18RUNCOL-25` Over 24.5 games: 0.42/0.53 mid 47.5%, model 53.9% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18RUNCOL-1-RUN` Will Holger Rune win set 1 in the Holger Rune vs Raphael Collignon match: 0.51/0.55 mid 53.0%, model 58.1% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18RUNCOL-2-COL` Will Raphael Collignon win set 2 in the Holger Rune vs Raphael Collignon match: 0.45/0.49 mid 47.0%, model 41.9% (projection_v2.0 (prediction ledger)) -- gap -5.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18RUNCOL-2-RUN` Will Holger Rune win set 2 in the Holger Rune vs Raphael Collignon match: 0.51/0.55 mid 53.0%, model 58.1% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18RUNCOL-20` Over 19.5 games: 0.73/0.83 mid 78.0%, model 82.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18RUNCOL-1-COL` Will Raphael Collignon win set 1 in the Holger Rune vs Raphael Collignon match: 0.44/0.49 mid 46.5%, model 41.9% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT18RUNCOL-RUN5` Will Holger Rune win at least 4.5 more games than Raphael Collignon?: 0.12/0.24 mid 18.0%, model 20.7% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18RUNCOL-COL20` Will Raphael Collignon win the Holger Rune vs Raphael Collignon match by a set score of 2-0?: 0.05/0.32 mid 18.5%, model 17.6% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Toby Samuel vs Zizou Bergs -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200267:210389:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zizou Bergs (`KXATPMATCH-26OCT18SAMBER-BER`) | 0.65 / 0.66 (42) | 65.5% | 46.0% | 28.0% | 36.1% [30.6%-44.0%] | -- | 68.8% | 68.8% | ALL_THREE_DISAGREE | PASS | -19.5 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Toby Samuel (`KXATPMATCH-26OCT18SAMBER-SAM`) | 0.34 / 0.36 (418) | 35.0% | 54.0% | 72.0% | 63.8% [56.0%-69.4%] | -- | -- | -- | INSUFFICIENT_INPUTS | WATCH | +19.0 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2684.0, B 5362.0; serve-point win A 62.9%, B 37.9%; Elo A 1804.6, B 1810.8; model uncertainty 0.0666
* Form inputs: days since last match A 19, B 3; matches on record A 136, B 552; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18SAMBER-SAM  (YES = Toby Samuel)
Model: 54%
Kalshi: 35%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.019, surface_dev_loose +0.042, surface_dev_tight -0.029
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT18SAMBER-SAM2` Will Toby Samuel win at least 1.5 more games than Zizou Bergs?: 0.10/0.35 mid 22.5%, model 46.7% (projection_v2.0 (prediction ledger)) -- gap +24.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18SAMBER-BER2` Will Zizou Bergs win at least 1.5 more games than Toby Samuel?: 0.37/0.73 mid 55.0%, model 38.8% (projection_v2.0 (prediction ledger)) -- gap -16.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAMBER-1-SAM` Will Toby Samuel win set 1 in the Toby Samuel vs Zizou Bergs match: 0.37/0.41 mid 39.0%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAMBER-2-BER` Will Zizou Bergs win set 2 in the Toby Samuel vs Zizou Bergs match: 0.59/0.63 mid 61.0%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap -13.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAMBER-2-SAM` Will Toby Samuel win set 2 in the Toby Samuel vs Zizou Bergs match: 0.37/0.41 mid 39.0%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAMBER-1-BER` Will Zizou Bergs win set 1 in the Toby Samuel vs Zizou Bergs match: 0.59/0.62 mid 60.5%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap -13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18SAMBER-31` Over 30.5 games: 0.18/0.50 mid 34.0%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SAMBER-BER20` Will Zizou Bergs win the Toby Samuel vs Zizou Bergs match by a set score of 2-0?: 0.18/0.46 mid 32.0%, model 22.4% (projection_v2.0 (prediction ledger)) -- gap -9.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18SAMBER-BER21` Will Zizou Bergs win the Toby Samuel vs Zizou Bergs match by a set score of 2-1?: 0.06/0.30 mid 18.0%, model 23.6% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18SAMBER-21` Over 20.5 games: 0.61/0.95 mid 78.0%, model 72.8% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18SAMBER-26` Over 25.5 games: 0.29/0.68 mid 48.5%, model 48.7% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jan-Lennard Struff vs Marcos Giron -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105526:106218:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcos Giron (`KXATPMATCH-26OCT18STRGIR-GIR`) | 0.35 / 0.39 (6100) | 37.0% | 52.3% | 49.0% | 49.5% [44.2%-53.4%] | -- | 38.0% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +15.3 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26OCT18STRGIR-STR`) | 0.60 / 0.62 (39) | 61.0% | 47.7% | 51.0% | 50.5% [46.6%-55.8%] | -- | 61.8% | -- | INSUFFICIENT_INPUTS | PASS | -13.3 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4788.0, B 4538.0; serve-point win A 66.0%, B 33.6%; Elo A 1780.4, B 1807.1; model uncertainty 0.0462
* Form inputs: days since last match A 7, B 9; matches on record A 1054, B 707; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18STRGIR-GIR  (YES = Marcos Giron)
Model: 52%
Kalshi: 37%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.039, surface_dev_loose -0.010, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT18STRGIR-STR3` Will Jan-Lennard Struff win at least 2.5 more games than Marcos Giron?: 0.47/0.49 mid 48.0%, model 32.0% (projection_v2.0 (prediction ledger)) -- gap -16.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18STRGIR-GIR21` Will Marcos Giron win the Jan-Lennard Struff vs Marcos Giron match by a set score of 2-1?: 0.02/0.20 mid 11.0%, model 25.7% (projection_v2.0 (prediction ledger)) -- gap +14.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18STRGIR-GIR20` Will Marcos Giron win the Jan-Lennard Struff vs Marcos Giron match by a set score of 2-0?: 0.02/0.22 mid 12.0%, model 26.6% (projection_v2.0 (prediction ledger)) -- gap +14.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18STRGIR-GIR2` Will Marcos Giron win at least 1.5 more games than Jan-Lennard Struff?: 0.30/0.32 mid 31.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18STRGIR-1-GIR` Will Marcos Giron win set 1 in the Jan-Lennard Struff vs Marcos Giron match: 0.38/0.43 mid 40.5%, model 51.5% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18STRGIR-1-STR` Will Jan-Lennard Struff win set 1 in the Jan-Lennard Struff vs Marcos Giron match: 0.57/0.62 mid 59.5%, model 48.5% (projection_v2.0 (prediction ledger)) -- gap -11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18STRGIR-2-GIR` Will Marcos Giron win set 2 in the Jan-Lennard Struff vs Marcos Giron match: 0.38/0.43 mid 40.5%, model 51.5% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18STRGIR-2-STR` Will Jan-Lennard Struff win set 2 in the Jan-Lennard Struff vs Marcos Giron match: 0.57/0.62 mid 59.5%, model 48.5% (projection_v2.0 (prediction ledger)) -- gap -11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18STRGIR-19` Over 18.5 games: 0.65/0.99 mid 82.0%, model 91.5% (projection_v2.0 (prediction ledger)) -- gap +9.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18STRGIR-STR21` Will Jan-Lennard Struff win the Jan-Lennard Struff vs Marcos Giron match by a set score of 2-1?: 0.07/0.27 mid 17.0%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18STRGIR-24` Over 23.5 games: 0.47/0.52 mid 49.5%, model 56.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18STRGIR-STR20` Will Jan-Lennard Struff win the Jan-Lennard Struff vs Marcos Giron match by a set score of 2-0?: 0.19/0.40 mid 29.5%, model 23.5% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18STRGIR-29` Over 28.5 games: 0.13/0.54 mid 33.5%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Botic Van de Zandschulp vs Kamil Majchrzak -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 14:52Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111794:122298:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kamil Majchrzak (`KXATPMATCH-26OCT18VANMAJ-MAJ`) | 0.38 / 0.42 (440) | 40.0% | 38.0% | 41.0% | 40.0% [39.0%-41.5%] | -- | 40.3% | -- | INSUFFICIENT_INPUTS | PASS | -1.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Botic Van de Zandschulp (`KXATPMATCH-26OCT18VANMAJ-VAN`) | 0.58 / 0.60 (6463) | 59.0% | 62.0% | 59.0% | 60.0% [58.5%-61.0%] | -- | 59.8% | -- | INSUFFICIENT_INPUTS | PASS | +3.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5172.0, B 4319.0; serve-point win A 63.7%, B 38.7%; Elo A 1902.6, B 1803.8; model uncertainty 0.0123
* Form inputs: days since last match A 3, B 10; matches on record A 618, B 674; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT18VANMAJ-VAN21` Will Botic Van de Zandschulp win the Botic Van de Zandschulp vs Kamil Majchrzak match by a set score of 2-1?: 0.05/0.29 mid 17.0%, model 28.3% (projection_v2.0 (prediction ledger)) -- gap +11.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18VANMAJ-VAN2` Will Botic Van de Zandschulp win at least 1.5 more games than Kamil Majchrzak?: 0.31/0.59 mid 45.0%, model 54.8% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18VANMAJ-31` Over 30.5 games: 0.10/0.51 mid 30.5%, model 23.4% (projection_v2.0 (prediction ledger)) -- gap -7.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18VANMAJ-VAN20` Will Botic Van de Zandschulp win the Botic Van de Zandschulp vs Kamil Majchrzak match by a set score of 2-0?: 0.14/0.42 mid 28.0%, model 33.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18VANMAJ-21` Over 20.5 games: 0.55/0.96 mid 75.5%, model 71.6% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18VANMAJ-MAJ20` Will Kamil Majchrzak win the Botic Van de Zandschulp vs Kamil Majchrzak match by a set score of 2-0?: 0.02/0.26 mid 14.0%, model 17.6% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT18VANMAJ-MAJ2` Will Kamil Majchrzak win at least 1.5 more games than Botic Van de Zandschulp?: 0.15/0.44 mid 29.5%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18VANMAJ-1-VAN` Will Botic Van de Zandschulp win set 1 in the Botic Van de Zandschulp vs Kamil Majchrzak match: 0.55/0.58 mid 56.5%, model 58.0% (projection_v2.0 (prediction ledger)) -- gap +1.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18VANMAJ-2-VAN` Will Botic Van de Zandschulp win set 2 in the Botic Van de Zandschulp vs Kamil Majchrzak match: 0.55/0.59 mid 57.0%, model 58.0% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18VANMAJ-26` Over 25.5 games: 0.46/0.51 mid 48.5%, model 47.5% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18VANMAJ-1-MAJ` Will Kamil Majchrzak win set 1 in the Botic Van de Zandschulp vs Kamil Majchrzak match: 0.40/0.45 mid 42.5%, model 42.0% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18VANMAJ-2-MAJ` Will Kamil Majchrzak win set 2 in the Botic Van de Zandschulp vs Kamil Majchrzak match: 0.40/0.45 mid 42.5%, model 42.0% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
