# ASSISTED SLATE -- 2026-10-17T11:28Z (`SL-20261017T112819Z-7cce66e5`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

121 open matches not seen started, 672 markets. Skipped: {"first_ball_already_observed": 4}. Sources: shadow board 2026-10-17T11:18:18.521689+00:00, Model 4 2026-10-17T11:18:36.458700+00:00, Gen-1 ledger 2026-10-17T11:18:15.083983+00:00, external 2026-10-17T11:01:48.627725+00:00, capture 20261017T105949Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-17 12:00Z**
* Recommended RUN TENNIS time: **2026-10-17 11:15Z**  (**OVERDUE -- run now**)
* Final price/status check time: **2026-10-17 11:50Z**
* Number of matches in window: 5 (Clement Chidekh vs Gilles Arnaud Bailly, Giovanni Mpetshi Perricard vs Remy Bertola, Aleksandr Shevchenko vs Daniil Glinka, Nishesh Basavareddy vs Edas Butvilas, Kimmer Coppejans vs Andrea Guerrieri)

* **22 main-tour match(es) have NO verified start status** (START_UNKNOWN, STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-10-17T11:28Z. Refresh due by: 2026-10-17 11:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 42, "HIGH_REVIEW": 67, "NORMAL": 283, "REVIEW": 98, "UNPRICED": 182}; match winners: {"EXTREME": 12, "HIGH_REVIEW": 31, "NORMAL": 96, "REVIEW": 29, "UNPRICED": 74}; quote freshness at build: {"AGING": 490}.

## Ivanova / Stankovic vs Elena Barbulescu / Simionescu -- W50 Stara Zagora SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-16 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-16T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT16IVASTAELESIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Barbulescu / Simionescu (`KXITFWDOUBLES-26OCT16IVASTAELESIM-ELESIM`) | 0.13 / 0.15 (9) | 14.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ivanova / Stankovic (`KXITFWDOUBLES-26OCT16IVASTAELESIM-IVASTA`) | 0.83 / 0.86 (20) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Luka Pavlovic vs Ilia Simakin -- ATP Almaty Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-17 11:20Z
* Current expected start: 2026-10-17 09:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-17 08:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-17T11:20:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:202146:209899:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luka Pavlovic (`KXATPMATCH-26OCT17PAVSIM-PAV`) | 0.40 / 0.44 (64) | 42.0% | 23.6% | 22.5% | 18.7% [15.4%-22.8%] | -- | 34.4% | 34.4% | MODEL_LONE_OUTLIER | PASS | -18.4 pp | HIGH_REVIEW | AGING | B / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Ilia Simakin (`KXATPMATCH-26OCT17PAVSIM-SIM`) | 0.55 / 0.59 (41) | 57.0% | 76.4% | 77.5% | 81.3% [77.2%-84.6%] | -- | 65.8% | 65.8% | MODEL_LONE_OUTLIER | WATCH | +19.4 pp | HIGH_REVIEW | AGING | B / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1148.0, B 3713.0; serve-point win A 64.5%, B 29.5%; Elo A 1437.6, B 1720.5; model uncertainty 0.0373
* Form inputs: days since last match A 12, B 9; matches on record A 212, B 239; data quality B

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT17PAVSIM-SIM  (YES = Ilia Simakin)
Model: 76%
Kalshi: 57%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: B (ADEQUATE)
Reasons: EXTERNAL_MARKET_CONFIRMATION, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.041, surface_pool_high -0.034, surface_dev_loose -0.002, surface_dev_tight +0.005
* Derivatives listed: 10 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPEXACTMATCH-26OCT17PAVSIM-SIM21` Will Ilia Simakin win the Luka Pavlovic vs Ilia Simakin match by a set score of 2-1?: 0.60/0.65 mid 62.5%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap -32.9 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17PAVSIM-PAV21` Will Luka Pavlovic win the Luka Pavlovic vs Ilia Simakin match by a set score of 2-1?: 0.34/0.40 mid 37.0%, model 13.6% (projection_v2.0 (prediction ledger)) -- gap -23.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; ONE_SIDED_OR_NO_QUOTE

## Joel Schwaerzler vs Federico Cina -- ATP Brussels Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-17 13:30Z
* Current expected start: 2026-10-17 10:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-17 09:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-17T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:210748:212082:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Cina (`KXATPMATCH-26OCT17SCHCIN-CIN`) | 0.81 / 0.83 (11) | 82.0% | 59.5% | 61.1% | 60.1% [59.7%-61.1%] | -- | 54.8% | 54.8% | MODEL_LONE_OUTLIER | PASS | -22.5 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Joel Schwaerzler (`KXATPMATCH-26OCT17SCHCIN-SCH`) | 0.17 / 0.19 (5389) | 18.0% | 40.5% | 38.9% | 39.9% [38.9%-40.3%] | -- | 44.7% | 44.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +22.5 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 3799.0, B 3338.0; serve-point win A 65.1%, B 32.9%; Elo A 1607.6, B 1670.7; model uncertainty 0.007
* Form inputs: days since last match A 12, B 10; matches on record A 147, B 152; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT17SCHCIN-SCH  (YES = Joel Schwaerzler)
Model: 41%
Kalshi: 18%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_MODEL
Data quality: A (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, EXTERNAL_MARKET_CONFIRMATION
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.009, surface_dev_tight +0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT17SCHCIN-CIN5` Will Federico Cina win at least 4.5 more games than Joel Schwaerzler?: 0.57/0.60 mid 58.5%, model 18.7% (projection_v2.0 (prediction ledger)) -- gap -39.8 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17SCHCIN-CIN20` Will Federico Cina win the Joel Schwaerzler vs Federico Cina match by a set score of 2-0?: 0.63/0.64 mid 63.5%, model 31.8% (projection_v2.0 (prediction ledger)) -- gap -31.8 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17SCHCIN-CIN2` Will Federico Cina win at least 1.5 more games than Joel Schwaerzler?: 0.69/0.81 mid 75.0%, model 51.5% (projection_v2.0 (prediction ledger)) -- gap -23.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17SCHCIN-23` Over 22.5 games: 0.37/0.56 mid 46.5%, model 63.3% (projection_v2.0 (prediction ledger)) -- gap +16.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17SCHCIN-18` Over 17.5 games: 0.66/0.96 mid 81.0%, model 95.2% (projection_v2.0 (prediction ledger)) -- gap +14.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17SCHCIN-CIN21` Will Federico Cina win the Joel Schwaerzler vs Federico Cina match by a set score of 2-1?: 0.14/0.20 mid 17.0%, model 27.7% (projection_v2.0 (prediction ledger)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17SCHCIN-2-SCH` Will Joel Schwaerzler win set 2 in the Joel Schwaerzler vs Federico Cina match: 0.33/0.34 mid 33.5%, model 43.6% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17SCHCIN-2-CIN` Will Federico Cina win set 2 in the Joel Schwaerzler vs Federico Cina match: 0.65/0.66 mid 65.5%, model 56.4% (projection_v2.0 (prediction ledger)) -- gap -9.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT17SCHCIN-28` Over 27.5 games: 0.22/0.49 mid 35.5%, model 42.6% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17SCHCIN-SCH21` Will Joel Schwaerzler win the Joel Schwaerzler vs Federico Cina match by a set score of 2-1?: 0.12/0.18 mid 15.0%, model 21.5% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17SCHCIN-SCH2` Will Joel Schwaerzler win at least 1.5 more games than Federico Cina?: 0.26/0.30 mid 28.0%, model 32.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Harry Wendelken vs Gauthier Onclin -- ATP Brussels Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-17 13:30Z
* Current expected start: 2026-10-17 10:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-17 09:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-17T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206904:207784:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gauthier Onclin (`KXATPMATCH-26OCT17WENONC-ONC`) | 0.81 / 0.82 (15453) | 81.5% | 49.2% | 44.8% | 48.4% [45.3%-54.1%] | -- | 52.2% | 52.2% | MODEL_LONE_OUTLIER | PASS | -32.3 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Harry Wendelken (`KXATPMATCH-26OCT17WENONC-WEN`) | 0.18 / 0.19 (36526) | 18.5% | 50.8% | 55.2% | 51.6% [45.9%-54.7%] | -- | 47.2% | 47.2% | MODEL_LONE_OUTLIER | WATCH | +32.3 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 2654.0, B 3092.0; serve-point win A 58.5%, B 41.7%; Elo A 1578.0, B 1608.1; model uncertainty 0.0442
* Form inputs: days since last match A 19, B 12; matches on record A 249, B 406; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT17WENONC-WEN  (YES = Harry Wendelken)
Model: 51%
Kalshi: 18%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_MODEL
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose +0.010, surface_dev_tight -0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26OCT17WENONC-1-WEN` Will Harry Wendelken win set 1 in the Harry Wendelken vs Gauthier Onclin match: 0.02/0.04 mid 3.0%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap +47.5 pp, EXTREME, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17WENONC-1-ONC` Will Gauthier Onclin win set 1 in the Harry Wendelken vs Gauthier Onclin match: 0.95/0.98 mid 96.5%, model 49.5% (projection_v2.0 (prediction ledger)) -- gap -47.0 pp, EXTREME, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17WENONC-ONC20` Will Gauthier Onclin win the Harry Wendelken vs Gauthier Onclin match by a set score of 2-0?: 0.57/0.63 mid 60.0%, model 24.5% (projection_v2.0 (prediction ledger)) -- gap -35.5 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17WENONC-ONC5` Will Gauthier Onclin win at least 4.5 more games than Harry Wendelken?: 0.52/0.55 mid 53.5%, model 20.2% (projection_v2.0 (prediction ledger)) -- gap -33.3 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17WENONC-ONC2` Will Gauthier Onclin win at least 1.5 more games than Harry Wendelken?: 0.58/0.79 mid 68.5%, model 42.4% (projection_v2.0 (prediction ledger)) -- gap -26.1 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17WENONC-WEN20` Will Harry Wendelken win the Harry Wendelken vs Gauthier Onclin match by a set score of 2-0?: 0.01/0.04 mid 2.5%, model 25.5% (projection_v2.0 (prediction ledger)) -- gap +23.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17WENONC-20` Over 19.5 games: 0.53/0.55 mid 54.0%, model 75.9% (projection_v2.0 (prediction ledger)) -- gap +21.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17WENONC-2-WEN` Will Harry Wendelken win set 2 in the Harry Wendelken vs Gauthier Onclin match: 0.36/0.39 mid 37.5%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17WENONC-2-ONC` Will Gauthier Onclin win set 2 in the Harry Wendelken vs Gauthier Onclin match: 0.60/0.64 mid 62.0%, model 49.5% (projection_v2.0 (prediction ledger)) -- gap -12.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT17WENONC-WEN2` Will Harry Wendelken win at least 1.5 more games than Gauthier Onclin?: 0.26/0.37 mid 31.5%, model 44.0% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17WENONC-25` Over 24.5 games: 0.30/0.51 mid 40.5%, model 50.3% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17WENONC-WEN21` Will Harry Wendelken win the Harry Wendelken vs Gauthier Onclin match by a set score of 2-1?: 0.16/0.21 mid 18.5%, model 25.3% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17WENONC-ONC21` Will Gauthier Onclin win the Harry Wendelken vs Gauthier Onclin match by a set score of 2-1?: 0.16/0.21 mid 18.5%, model 24.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17WENONC-30` Over 29.5 games: 0.06/0.38 mid 22.0%, model 25.1% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; WIDE_SPREAD

## Iga Swiatek vs Maja Chwalinska -- WTA Wuhan SF

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-17 13:30Z
* Current expected start: 2026-10-17 10:40Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-17 09:55Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-170_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (MASTERS_1000) · Hard · scheduled 2026-10-17T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:216081:216347:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maja Chwalinska (`KXWTAMATCH-26OCT17SWICHW-CHW`) | 0.18 / 0.19 (5000) | 18.5% | 19.4% | 20.8% | 17.6% [14.4%-19.7%] | 17.3% | 17.3% | 17.3% | MODEL_LONE_OUTLIER | PASS | +0.8 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Iga Swiatek (`KXWTAMATCH-26OCT17SWICHW-SWI`) | 0.81 / 0.82 (68695) | 81.5% | 80.7% | 79.2% | 82.4% [80.3%-85.6%] | 82.7% | 82.7% | 82.7% | MODEL_LONE_OUTLIER | PASS | -0.8 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4863.0, B 3543.0; serve-point win A 57.9%, B 48.6%; Elo A 2182.4, B 1835.8; model uncertainty 0.0266
* Form inputs: days since last match A 1, B 1; matches on record A 547, B 395; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.021, surface_dev_tight +0.016
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17SWICHW-20` Over 19.5 games: 0.45/0.46 mid 45.5%, model 63.3% (projection_v2.0 (prediction ledger)) -- gap +17.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17SWICHW-25` Over 24.5 games: 0.19/0.27 mid 23.0%, model 38.8% (projection_v2.0 (prediction ledger)) -- gap +15.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17SWICHW-15` Over 14.5 games: 0.86/0.97 mid 91.5%, model 97.5% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17SWICHW-2-CHW` Will Maja Chwalinska win set 2 in the Iga Swiatek vs Maja Chwalinska match: 0.21/0.24 mid 22.5%, model 28.2% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17SWICHW-2-SWI` Will Iga Swiatek win set 2 in the Iga Swiatek vs Maja Chwalinska match: 0.75/0.79 mid 77.0%, model 71.8% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17SWICHW-1-CHW` Will Maja Chwalinska win set 1 in the Iga Swiatek vs Maja Chwalinska match: 0.22/0.25 mid 23.5%, model 28.2% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17SWICHW-1-SWI` Will Iga Swiatek win set 1 in the Iga Swiatek vs Maja Chwalinska match: 0.75/0.77 mid 76.0%, model 71.8% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rafael Jodar vs Daniil Medvedev -- ATP Shanghai SF

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-17 05:00Z
* Current expected start: 2026-10-17 10:54Z
* Source: COURT_PROGRESSION: preceding match on Stadium Court in progress (set 3 of best-of-5); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-17 10:09Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+354_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-17T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106421:212588:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael Jodar (`KXATPMATCH-26OCT16JODMED-JOD`) | 0.35 / 0.36 (25596) | 35.5% | 42.5% | 38.3% | 36.9% [36.4%-37.8%] | 38.4% | 36.2% | 37.3% | MARKETS_AGREE | PASS | +7.0 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Daniil Medvedev (`KXATPMATCH-26OCT16JODMED-MED`) | 0.64 / 0.65 (34284) | 64.5% | 57.5% | 61.7% | 63.1% [62.2%-63.6%] | 61.6% | 63.9% | 62.8% | MARKETS_AGREE | PASS | -7.0 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4261.0, B 5727.0; serve-point win A 59.6%, B 38.9%; Elo A 1993.3, B 2103.4; model uncertainty 0.0072
* Form inputs: days since last match A 1, B 3; matches on record A 116, B 856; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT16JODMED-MED20` Will Daniil Medvedev win the Rafael Jodar vs Daniil Medvedev match by a set score of 2-0?: 0.36/0.49 mid 42.5%, model 30.3% (projection_v2.0 (prediction ledger)) -- gap -12.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT16JODMED-23` Over 22.5 games: 0.49/0.50 mid 49.5%, model 57.9% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT16JODMED-MED3` Will Daniil Medvedev win at least 2.5 more games than Rafael Jodar?: 0.50/0.51 mid 50.5%, model 44.5% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT16JODMED-JOD21` Will Rafael Jodar win the Rafael Jodar vs Daniil Medvedev match by a set score of 2-1?: 0.14/0.19 mid 16.5%, model 22.2% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT16JODMED-MED6` Will Daniil Medvedev win at least 5.5 more games than Rafael Jodar?: 0.16/0.25 mid 20.5%, model 15.0% (projection_v2.0 (prediction ledger)) -- gap -5.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT16JODMED-28` Over 27.5 games: 0.27/0.37 mid 32.0%, model 37.1% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT16JODMED-2-JOD` Will Rafael Jodar win set 2 in the Rafael Jodar vs Daniil Medvedev match: 0.39/0.41 mid 40.0%, model 45.0% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT16JODMED-MED21` Will Daniil Medvedev win the Rafael Jodar vs Daniil Medvedev match by a set score of 2-1?: 0.19/0.26 mid 22.5%, model 27.2% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT16JODMED-2-MED` Will Daniil Medvedev win set 2 in the Rafael Jodar vs Daniil Medvedev match: 0.58/0.61 mid 59.5%, model 55.0% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT16JODMED-JOD20` Will Rafael Jodar win the Rafael Jodar vs Daniil Medvedev match by a set score of 2-0?: 0.12/0.20 mid 16.0%, model 20.2% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT16JODMED-1-JOD` Will Rafael Jodar win set 1 in the Rafael Jodar vs Daniil Medvedev match: 0.40/0.43 mid 41.5%, model 45.0% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT16JODMED-JOD2` Will Rafael Jodar win at least 1.5 more games than Daniil Medvedev?: 0.29/0.36 mid 32.5%, model 35.3% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT16JODMED-1-MED` Will Daniil Medvedev win set 1 in the Rafael Jodar vs Daniil Medvedev match: 0.55/0.60 mid 57.5%, model 55.0% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT16JODMED-18` Over 17.5 games: 0.91/0.94 mid 92.5%, model 90.5% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Petr Bar Biryukov vs Stefanos Sakellaridis -- ATP Almaty Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-17 14:00Z
* Current expected start: 2026-10-17 11:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-17 10:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-17T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208852:209951:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Petr Bar Biryukov (`KXATPMATCH-26OCT17BARSAK-BAR`) | 0.35 / 0.36 (11932) | 35.5% | 28.8% | 22.3% | 27.8% [24.8%-30.1%] | 31.8% | 35.1% | 33.5% | KALSHI_LONE_OUTLIER | PASS | -6.7 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Stefanos Sakellaridis (`KXATPMATCH-26OCT17BARSAK-SAK`) | 0.64 / 0.65 (12085) | 64.5% | 71.2% | 77.7% | 72.2% [69.9%-75.2%] | 68.2% | 64.8% | 66.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.7 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2591.0, B 3408.0; serve-point win A 68.3%, B 26.8%; Elo A 1512.2, B 1606.8; model uncertainty 0.0269
* Form inputs: days since last match A 18, B 12; matches on record A 179, B 321; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.024, surface_dev_loose -0.014, surface_dev_tight +0.007
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT17BARSAK-SAK21` Will Stefanos Sakellaridis win the Petr Bar Biryukov vs Stefanos Sakellaridis match by a set score of 2-1?: 0.19/0.24 mid 21.5%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17BARSAK-BAR20` Will Petr Bar Biryukov win the Petr Bar Biryukov vs Stefanos Sakellaridis match by a set score of 2-0?: 0.18/0.20 mid 19.0%, model 12.6% (projection_v2.0 (prediction ledger)) -- gap -6.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17BARSAK-1-BAR` Will Petr Bar Biryukov win set 1 in the Petr Bar Biryukov vs Stefanos Sakellaridis match: 0.36/0.41 mid 38.5%, model 35.4% (projection_v2.0 (prediction ledger)) -- gap -3.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17BARSAK-1-SAK` Will Stefanos Sakellaridis win set 1 in the Petr Bar Biryukov vs Stefanos Sakellaridis match: 0.59/0.64 mid 61.5%, model 64.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17BARSAK-2-BAR` Will Petr Bar Biryukov win set 2 in the Petr Bar Biryukov vs Stefanos Sakellaridis match: 0.36/0.41 mid 38.5%, model 35.4% (projection_v2.0 (prediction ledger)) -- gap -3.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17BARSAK-2-SAK` Will Stefanos Sakellaridis win set 2 in the Petr Bar Biryukov vs Stefanos Sakellaridis match: 0.59/0.64 mid 61.5%, model 64.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17BARSAK-BAR21` Will Petr Bar Biryukov win the Petr Bar Biryukov vs Stefanos Sakellaridis match by a set score of 2-1?: 0.13/0.16 mid 14.5%, model 16.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17BARSAK-SAK20` Will Stefanos Sakellaridis win the Petr Bar Biryukov vs Stefanos Sakellaridis match by a set score of 2-0?: 0.40/0.44 mid 42.0%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE

## Martyna Kubka vs Dominika Salkova -- WTA 125K Rovereto SF

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-17 14:00Z
* Current expected start: 2026-10-17 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-17 10:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · Hard · scheduled 2026-10-17T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221243:222966:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martyna Kubka (`KXWTACHALLENGERMATCH-26OCT17KUBSAL-KUB`) | 0.75 / 0.76 (21518) | 75.5% | 52.1% | 69.0% | 61.5% [47.4%-66.7%] | -- | 52.5% | 52.5% | MODEL_LONE_OUTLIER | WATCH | -23.4 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Dominika Salkova (`KXWTACHALLENGERMATCH-26OCT17KUBSAL-SAL`) | 0.24 / 0.25 (20) | 24.5% | 47.9% | 31.0% | 38.5% [33.3%-52.6%] | -- | 47.4% | 47.4% | MODEL_LONE_OUTLIER | PASS | +23.4 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 2983.0, B 3665.0; serve-point win A 62.0%, B 38.4%; Elo A 1689.5, B 1727.9; model uncertainty 0.0964
* Form inputs: days since last match A 2, B 1; matches on record A 333, B 297; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT17KUBSAL-SAL  (YES = Dominika Salkova)
Model: 48%
Kalshi: 24%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_MODEL
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.019, surface_dev_loose -0.000, surface_dev_tight -0.009
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS

## Jessica Bouzas Maneiro vs Clara Burel -- WTA 125K Lisbon SF

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-17 14:10Z
* Current expected start: 2026-10-17 11:19Z
* Source: COURT_PROGRESSION: preceding match on Estadio CIF in progress (set 1 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-17 10:34Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · Clay · scheduled 2026-10-17T14:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216262:222601:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jessica Bouzas Maneiro (`KXWTACHALLENGERMATCH-26OCT17BOUBUR-BOU`) | 0.45 / 0.46 (4874) | 45.5% | 58.9% | 66.2% | 61.6% [59.6%-63.7%] | 45.9% | 45.9% | 45.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +13.4 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Clara Burel (`KXWTACHALLENGERMATCH-26OCT17BOUBUR-BUR`) | 0.53 / 0.54 (328) | 53.5% | 41.1% | 33.8% | 38.4% [36.3%-40.5%] | 54.1% | 54.2% | 54.2% | MODEL_LONE_OUTLIER | PASS | -12.4 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3457.0, B 1472.0; serve-point win A 51.3%, B 50.3%; Elo A 1831.1, B 1784.0; model uncertainty 0.0206
* Form inputs: days since last match A 1, B 1; matches on record A 441, B 306; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS

## Martin Landaluce vs Liam Draxl -- ATP Challenger Jinan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 11:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-17T11:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208119:212021:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liam Draxl (`KXATPCHALLENGERMATCH-26OCT17LANDRA-DRA`) | 0.30 / 0.31 (68) | 30.5% | 39.0% | 41.9% | 43.9% [42.4%-50.5%] | -- | 37.2% | 37.2% | MODEL_LONE_OUTLIER | PASS | +8.5 pp | NORMAL | AGING | F / POOR | AGREES_WITH_MODEL | VERIFIED |
| Martin Landaluce (`KXATPCHALLENGERMATCH-26OCT17LANDRA-LAN`) | 0.68 / 0.69 (11352) | 68.5% | 61.0% | 58.1% | 56.1% [49.5%-57.6%] | -- | 62.3% | 62.3% | MODEL_LONE_OUTLIER | PASS | -7.5 pp | NORMAL | AGING | F / POOR | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 3597.0, B 3235.0; serve-point win A 62.9%, B 39.3%; Elo A 1706.0, B 1693.1; model uncertainty 0.0404
* Form inputs: days since last match A 698, B 11; matches on record A 115, B 329; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.015, surface_dev_loose +0.015, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Clement Chidekh vs Gilles Arnaud Bailly -- ATP Brussels Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-17 14:40Z
* Current expected start: 2026-10-17 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-17 11:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-17T14:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206889:211451:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gilles Arnaud Bailly (`KXATPMATCH-26OCT17CHIARN-ARN`) | 0.15 / 0.16 (5000) | 15.5% | 20.1% | 13.4% | 17.3% [14.7%-22.4%] | 18.2% | 15.2% | 16.7% | MODEL_LONE_OUTLIER | PASS | +4.5 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Clement Chidekh (`KXATPMATCH-26OCT17CHIARN-CHI`) | 0.84 / 0.85 (34379) | 84.5% | 80.0% | 86.6% | 82.7% [77.6%-85.3%] | 81.8% | 85.2% | 83.5% | MODEL_LONE_OUTLIER | PASS | -4.5 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3878.0, B 1899.0; serve-point win A 63.2%, B 43.3%; Elo A 1687.3, B 1482.8; model uncertainty 0.0382
* Form inputs: days since last match A 19, B 40; matches on record A 279, B 130; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.016, surface_dev_tight -0.017
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT17CHIARN-22` Over 21.5 games: 0.41/0.42 mid 41.5%, model 55.0% (projection_v2.0 (prediction ledger)) -- gap +13.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17CHIARN-CHI5` Will Clement Chidekh win at least 4.5 more games than Gilles Arnaud Bailly?: 0.58/0.59 mid 58.5%, model 45.1% (projection_v2.0 (prediction ledger)) -- gap -13.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17CHIARN-17` Over 16.5 games: 0.64/0.93 mid 78.5%, model 91.5% (projection_v2.0 (prediction ledger)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17CHIARN-CHI20` Will Clement Chidekh win the Clement Chidekh vs Gilles Arnaud Bailly match by a set score of 2-0?: 0.61/0.62 mid 61.5%, model 50.8% (projection_v2.0 (prediction ledger)) -- gap -10.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17CHIARN-CHI21` Will Clement Chidekh win the Clement Chidekh vs Gilles Arnaud Bailly match by a set score of 2-1?: 0.19/0.22 mid 20.5%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17CHIARN-CHI8` Will Clement Chidekh win at least 7.5 more games than Gilles Arnaud Bailly?: 0.13/0.22 mid 17.5%, model 9.1% (projection_v2.0 (prediction ledger)) -- gap -8.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17CHIARN-2-ARN` Will Gilles Arnaud Bailly win set 2 in the Clement Chidekh vs Gilles Arnaud Bailly match: 0.20/0.23 mid 21.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17CHIARN-1-ARN` Will Gilles Arnaud Bailly win set 1 in the Clement Chidekh vs Gilles Arnaud Bailly match: 0.20/0.24 mid 22.0%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17CHIARN-1-CHI` Will Clement Chidekh win set 1 in the Clement Chidekh vs Gilles Arnaud Bailly match: 0.76/0.79 mid 77.5%, model 71.2% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17CHIARN-2-CHI` Will Clement Chidekh win set 2 in the Clement Chidekh vs Gilles Arnaud Bailly match: 0.77/0.78 mid 77.5%, model 71.2% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT17CHIARN-CHI2` Will Clement Chidekh win at least 1.5 more games than Gilles Arnaud Bailly?: 0.74/0.87 mid 80.5%, model 74.9% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17CHIARN-27` Over 26.5 games: 0.20/0.36 mid 28.0%, model 33.2% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17CHIARN-ARN21` Will Gilles Arnaud Bailly win the Clement Chidekh vs Gilles Arnaud Bailly match by a set score of 2-1?: 0.07/0.10 mid 8.5%, model 11.8% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17CHIARN-ARN20` Will Gilles Arnaud Bailly win the Clement Chidekh vs Gilles Arnaud Bailly match by a set score of 2-0?: 0.07/0.09 mid 8.0%, model 8.3% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; WIDE_SPREAD

## Giovanni Mpetshi Perricard vs Remy Bertola -- ATP Brussels Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-17 14:40Z
* Current expected start: 2026-10-17 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-17 11:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-17T14:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200329:208659:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Remy Bertola (`KXATPMATCH-26OCT17MPEBER-BER`) | 0.41 / 0.42 (6880) | 41.5% | 36.8% | 51.8% | 45.0% [39.1%-48.6%] | 43.4% | 43.0% | 43.2% | MODEL_LONE_OUTLIER | WATCH | -4.7 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Giovanni Mpetshi Perricard (`KXATPMATCH-26OCT17MPEBER-MPE`) | 0.57 / 0.58 (15411) | 57.5% | 63.2% | 48.2% | 55.0% [51.4%-60.9%] | 56.6% | 57.2% | 56.9% | MODEL_LONE_OUTLIER | PASS | +5.7 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4159.0, B 3382.0; serve-point win A 73.3%, B 29.7%; Elo A 1720.5, B 1574.7; model uncertainty 0.0477
* Form inputs: days since last match A 47, B 19; matches on record A 307, B 405; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.018, surface_dev_loose -0.009, surface_dev_tight +0.014
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT17MPEBER-26` Over 25.5 games: 0.47/0.48 mid 47.5%, model 57.9% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17MPEBER-MPE5` Will Giovanni Mpetshi Perricard win at least 4.5 more games than Remy Bertola?: 0.15/0.28 mid 21.5%, model 11.4% (projection_v2.0 (prediction ledger)) -- gap -10.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17MPEBER-21` Over 20.5 games: 0.58/0.95 mid 76.5%, model 86.4% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17MPEBER-31` Over 30.5 games: 0.13/0.50 mid 31.5%, model 40.1% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17MPEBER-BER20` Will Remy Bertola win the Giovanni Mpetshi Perricard vs Remy Bertola match by a set score of 2-0?: 0.22/0.25 mid 23.5%, model 16.9% (projection_v2.0 (prediction ledger)) -- gap -6.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17MPEBER-MPE21` Will Giovanni Mpetshi Perricard win the Giovanni Mpetshi Perricard vs Remy Bertola match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 28.5% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17MPEBER-BER2` Will Remy Bertola win at least 1.5 more games than Giovanni Mpetshi Perricard?: 0.29/0.37 mid 33.0%, model 27.6% (projection_v2.0 (prediction ledger)) -- gap -5.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17MPEBER-2-MPE` Will Giovanni Mpetshi Perricard win set 2 in the Giovanni Mpetshi Perricard vs Remy Bertola match: 0.53/0.55 mid 54.0%, model 58.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17MPEBER-2-BER` Will Remy Bertola win set 2 in the Giovanni Mpetshi Perricard vs Remy Bertola match: 0.42/0.47 mid 44.5%, model 41.1% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT17MPEBER-MPE2` Will Giovanni Mpetshi Perricard win at least 1.5 more games than Remy Bertola?: 0.49/0.51 mid 50.0%, model 53.1% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17MPEBER-1-BER` Will Remy Bertola win set 1 in the Giovanni Mpetshi Perricard vs Remy Bertola match: 0.42/0.45 mid 43.5%, model 41.1% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17MPEBER-1-MPE` Will Giovanni Mpetshi Perricard win set 1 in the Giovanni Mpetshi Perricard vs Remy Bertola match: 0.55/0.58 mid 56.5%, model 58.9% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17MPEBER-BER21` Will Remy Bertola win the Giovanni Mpetshi Perricard vs Remy Bertola match by a set score of 2-1?: 0.17/0.20 mid 18.5%, model 19.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17MPEBER-MPE20` Will Giovanni Mpetshi Perricard win the Giovanni Mpetshi Perricard vs Remy Bertola match by a set score of 2-0?: 0.33/0.35 mid 34.0%, model 34.7% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aleksandr Shevchenko vs Daniil Glinka -- ATP Almaty Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-17 15:00Z
* Current expected start: 2026-10-17 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-17 11:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-17T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206750:207686:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniil Glinka (`KXATPMATCH-26OCT17SHEGLI-GLI`) | 0.44 / 0.45 (47410) | 44.5% | 45.2% | 60.8% | 54.0% [47.0%-57.9%] | 43.4% | 42.2% | 42.8% | MARKETS_AGREE | PASS | +0.7 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | AMBIGUOUS |
| Aleksandr Shevchenko (`KXATPMATCH-26OCT17SHEGLI-SHE`) | 0.55 / 0.56 (7268) | 55.5% | 54.8% | 39.2% | 46.0% [42.1%-53.0%] | 56.6% | 58.2% | 57.4% | MARKETS_AGREE | PASS | -0.7 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | AMBIGUOUS |

* Serve evidence (points): A 4772.0, B 3880.0; serve-point win A 65.0%, B 36.0%; Elo A 1712.4, B 1617.0; model uncertainty 0.0542
* Form inputs: days since last match A 23, B 12; matches on record A 477, B 329; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.020, surface_dev_loose -0.015, surface_dev_tight +0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT17SHEGLI-SHE5` Will Alexander Shevchenko win at least 4.5 more games than Daniil Glinka?: 0.22/0.29 mid 25.5%, model 18.1% (projection_v2.0 (prediction ledger)) -- gap -7.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT17SHEGLI-26` Over 25.5 games: 0.44/0.45 mid 44.5%, model 50.3% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17SHEGLI-SHE21` Will Alexander Shevchenko win the Alexander Shevchenko vs Daniil Glinka match by a set score of 2-1?: 0.20/0.23 mid 21.5%, model 26.5% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17SHEGLI-GLI21` Will Daniil Glinka win the Alexander Shevchenko vs Daniil Glinka match by a set score of 2-1?: 0.17/0.20 mid 18.5%, model 23.3% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17SHEGLI-GLI20` Will Daniil Glinka win the Alexander Shevchenko vs Daniil Glinka match by a set score of 2-0?: 0.25/0.26 mid 25.5%, model 21.9% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17SHEGLI-SHE20` Will Alexander Shevchenko win the Alexander Shevchenko vs Daniil Glinka match by a set score of 2-0?: 0.31/0.32 mid 31.5%, model 28.3% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT17SHEGLI-SHE2` Will Alexander Shevchenko win at least 1.5 more games than Daniil Glinka?: 0.49/0.50 mid 49.5%, model 47.1% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17SHEGLI-2-GLI` Will Daniil Glinka win set 2 in the Alexander Shevchenko vs Daniil Glinka match: 0.43/0.46 mid 44.5%, model 46.8% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT17SHEGLI-GLI2` Will Daniil Glinka win at least 1.5 more games than Alexander Shevchenko?: 0.36/0.44 mid 40.0%, model 37.7% (projection_v2.0 (prediction ledger)) -- gap -2.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT17SHEGLI-31` Over 30.5 games: 0.20/0.30 mid 25.0%, model 27.2% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17SHEGLI-1-GLI` Will Daniil Glinka win set 1 in the Alexander Shevchenko vs Daniil Glinka match: 0.43/0.47 mid 45.0%, model 46.8% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17SHEGLI-1-SHE` Will Alexander Shevchenko win set 1 in the Alexander Shevchenko vs Daniil Glinka match: 0.53/0.55 mid 54.0%, model 53.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17SHEGLI-2-SHE` Will Alexander Shevchenko win set 2 in the Alexander Shevchenko vs Daniil Glinka match: 0.53/0.55 mid 54.0%, model 53.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT17SHEGLI-21` Over 20.5 games: 0.62/0.87 mid 74.5%, model 75.1% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Storm Hunter / Katerina Siniakova vs Sara Errani / Jasmine Paolini -- WTA Wuhan SF

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-10-17 14:40Z
* Current expected start: 2026-10-17 12:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-17 11:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-17T14:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17HUNSINERRPAO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Errani / Jasmine Paolini (`KXWTADOUBLES-26OCT17HUNSINERRPAO-ERRPAO`) | 0.38 / 0.42 (610) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Storm Hunter / Katerina Siniakova (`KXWTADOUBLES-26OCT17HUNSINERRPAO-HUNSIN`) | 0.57 / 0.60 (120) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Daniel de Jonge / Jannik Opitz vs David Stevenson / Marcus Willis -- ATP Challenger Roanne SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-17T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17DEOPISTEWIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel de Jonge / Jannik Opitz (`KXATPCHALLENGERDOUBLES-26OCT17DEOPISTEWIL-DEOPI`) | 0.04 / 0.08 (662) | 6.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| David Stevenson / Marcus Willis (`KXATPCHALLENGERDOUBLES-26OCT17DEOPISTEWIL-STEWIL`) | 0.93 / 0.96 (1322) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Bianca Andreescu vs Lucie Havlickova -- WTA 125K Rovereto SF

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-17 16:00Z
* Current expected start: 2026-10-17 13:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-17 12:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Hard · scheduled 2026-10-17T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215370:222980:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bianca Andreescu (`KXWTACHALLENGERMATCH-26OCT17ANDHAV-AND`) | 0.58 / 0.59 (1577) | 58.5% | 59.2% | 42.8% | 52.6% [49.0%-58.8%] | 58.4% | 58.2% | 58.3% | MODEL_LONE_OUTLIER | PASS | +0.7 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Lucie Havlickova (`KXWTACHALLENGERMATCH-26OCT17ANDHAV-HAV`) | 0.41 / 0.42 (16) | 41.5% | 40.8% | 57.2% | 47.4% [41.2%-51.0%] | 41.6% | 41.5% | 41.6% | MODEL_LONE_OUTLIER | WATCH | -0.7 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2877.0, B 2440.0; serve-point win A 60.9%, B 40.9%; Elo A 1892.5, B 1766.4; model uncertainty 0.0491
* Form inputs: days since last match A 1, B 1; matches on record A 369, B 202; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE

## Zsombor Piros vs Alejo Sanchez Quilez -- ATP Challenger Maia SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-17T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200436:211639:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zsombor Piros (`KXATPCHALLENGERMATCH-26OCT17PIRSAN-PIR`) | 0.84 / 0.87 (149) | 85.5% | 85.8% | 87.2% | 87.7% [86.4%-88.6%] | -- | 69.7% | -- | INSUFFICIENT_INPUTS | PASS | +0.3 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejo Sanchez Quilez (`KXATPCHALLENGERMATCH-26OCT17PIRSAN-SAN`) | 0.13 / 0.15 (216) | 14.0% | 14.2% | 12.8% | 12.3% [11.4%-13.6%] | -- | 30.1% | -- | INSUFFICIENT_INPUTS | PASS | +0.2 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4115.0, B 1220.0; serve-point win A 63.9%, B 44.3%; Elo A 1778.6, B 1435.5; model uncertainty 0.011
* Form inputs: days since last match A 12, B 12; matches on record A 526, B 113; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose +0.008, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Nishesh Basavareddy vs Edas Butvilas -- ATP Brussels Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-17 15:50Z
* Current expected start: 2026-10-17 13:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-17 12:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-17T15:50:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:210220:210460:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nishesh Basavareddy (`KXATPMATCH-26OCT17BASBUT-BAS`) | 0.62 / 0.63 (2) | 62.5% | 52.3% | 42.0% | 50.0% [47.0%-54.0%] | 62.3% | 62.7% | 62.5% | MODEL_LONE_OUTLIER | PASS | -10.2 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Edas Butvilas (`KXATPMATCH-26OCT17BASBUT-BUT`) | 0.36 / 0.38 (28075) | 37.0% | 47.6% | 58.0% | 50.0% [46.0%-53.0%] | 37.7% | 36.8% | 37.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.7 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2705.0, B 3824.0; serve-point win A 63.5%, B 36.9%; Elo A 1737.5, B 1636.2; model uncertainty 0.035
* Form inputs: days since last match A 12, B 12; matches on record A 142, B 231; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.025, surface_dev_loose -0.015, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT17BASBUT-23` Over 22.5 games: 0.45/0.46 mid 45.5%, model 60.9% (projection_v2.0 (prediction ledger)) -- gap +15.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17BASBUT-BAS3` Will Nishesh Basavareddy win at least 2.5 more games than Edas Butvilas?: 0.51/0.53 mid 52.0%, model 37.9% (projection_v2.0 (prediction ledger)) -- gap -14.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17BASBUT-BAS6` Will Nishesh Basavareddy win at least 5.5 more games than Edas Butvilas?: 0.17/0.30 mid 23.5%, model 9.8% (projection_v2.0 (prediction ledger)) -- gap -13.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17BASBUT-BAS20` Will Nishesh Basavareddy win the Nishesh Basavareddy vs Edas Butvilas match by a set score of 2-0?: 0.39/0.40 mid 39.5%, model 26.6% (projection_v2.0 (prediction ledger)) -- gap -12.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17BASBUT-28` Over 27.5 games: 0.13/0.47 mid 30.0%, model 40.5% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17BASBUT-18` Over 17.5 games: 0.73/0.94 mid 83.5%, model 93.3% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17BASBUT-2-BUT` Will Edas Butvilas win set 2 in the Nishesh Basavareddy vs Edas Butvilas match: 0.37/0.41 mid 39.0%, model 48.4% (projection_v2.0 (prediction ledger)) -- gap +9.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT17BASBUT-BUT2` Will Edas Butvilas win at least 1.5 more games than Nishesh Basavareddy?: 0.29/0.34 mid 31.5%, model 40.2% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17BASBUT-1-BAS` Will Nishesh Basavareddy win set 1 in the Nishesh Basavareddy vs Edas Butvilas match: 0.58/0.62 mid 60.0%, model 51.6% (projection_v2.0 (prediction ledger)) -- gap -8.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17BASBUT-1-BUT` Will Edas Butvilas win set 1 in the Nishesh Basavareddy vs Edas Butvilas match: 0.38/0.42 mid 40.0%, model 48.4% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17BASBUT-BUT21` Will Edas Butvilas win the Nishesh Basavareddy vs Edas Butvilas match by a set score of 2-1?: 0.14/0.19 mid 16.5%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17BASBUT-2-BAS` Will Nishesh Basavareddy win set 2 in the Nishesh Basavareddy vs Edas Butvilas match: 0.58/0.60 mid 59.0%, model 51.6% (projection_v2.0 (prediction ledger)) -- gap -7.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17BASBUT-BAS21` Will Nishesh Basavareddy win the Nishesh Basavareddy vs Edas Butvilas match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 25.8% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17BASBUT-BUT20` Will Edas Butvilas win the Nishesh Basavareddy vs Edas Butvilas match by a set score of 2-0?: 0.19/0.21 mid 20.0%, model 23.4% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kimmer Coppejans vs Andrea Guerrieri -- ATP Brussels Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-17 15:50Z
* Current expected start: 2026-10-17 13:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-17 12:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-17T15:50:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106293:200462:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kimmer Coppejans (`KXATPMATCH-26OCT17COPGUE-COP`) | 0.40 / 0.41 (5575) | 40.5% | 48.9% | 51.0% | 53.7% [50.5%-59.3%] | 40.6% | 41.0% | 40.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Andrea Guerrieri (`KXATPMATCH-26OCT17COPGUE-GUE`) | 0.59 / 0.60 (616) | 59.5% | 51.1% | 48.9% | 46.3% [40.7%-49.5%] | 59.4% | 58.5% | 59.0% | MODEL_LONE_OUTLIER | PASS | -8.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3531.0, B 2272.0; serve-point win A 57.5%, B 42.3%; Elo A 1610.3, B 1563.8; model uncertainty 0.0439
* Form inputs: days since last match A 9, B 19; matches on record A 840, B 345; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.031, surface_dev_loose -0.026, surface_dev_tight +0.021
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT17COPGUE-GUE4` Will Andrea Guerrieri win at least 3.5 more games than Kimmer Coppejans?: 0.43/0.45 mid 44.0%, model 31.1% (projection_v2.0 (prediction ledger)) -- gap -12.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17COPGUE-22` Over 21.5 games: 0.50/0.52 mid 51.0%, model 63.7% (projection_v2.0 (prediction ledger)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17COPGUE-GUE20` Will Andrea Guerrieri win the Kimmer Coppejans vs Andrea Guerrieri match by a set score of 2-0?: 0.35/0.39 mid 37.0%, model 25.8% (projection_v2.0 (prediction ledger)) -- gap -11.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17COPGUE-GUE7` Will Andrea Guerrieri win at least 6.5 more games than Kimmer Coppejans?: 0.01/0.35 mid 18.0%, model 7.6% (projection_v2.0 (prediction ledger)) -- gap -10.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17COPGUE-17` Over 16.5 games: 0.71/0.98 mid 84.5%, model 94.4% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17COPGUE-COP2` Will Kimmer Coppejans win at least 1.5 more games than Andrea Guerrieri?: 0.28/0.38 mid 33.0%, model 42.1% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17COPGUE-27` Over 26.5 games: 0.28/0.36 mid 32.0%, model 40.3% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17COPGUE-COP21` Will Kimmer Coppejans win the Kimmer Coppejans vs Andrea Guerrieri match by a set score of 2-1?: 0.15/0.18 mid 16.5%, model 24.6% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17COPGUE-1-COP` Will Kimmer Coppejans win set 1 in the Kimmer Coppejans vs Andrea Guerrieri match: 0.40/0.44 mid 42.0%, model 49.2% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17COPGUE-2-COP` Will Kimmer Coppejans win set 2 in the Kimmer Coppejans vs Andrea Guerrieri match: 0.40/0.44 mid 42.0%, model 49.2% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17COPGUE-2-GUE` Will Andrea Guerrieri win set 2 in the Kimmer Coppejans vs Andrea Guerrieri match: 0.56/0.58 mid 57.0%, model 50.8% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17COPGUE-1-GUE` Will Andrea Guerrieri win set 1 in the Kimmer Coppejans vs Andrea Guerrieri match: 0.55/0.58 mid 56.5%, model 50.8% (projection_v2.0 (prediction ledger)) -- gap -5.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17COPGUE-GUE21` Will Andrea Guerrieri win the Kimmer Coppejans vs Andrea Guerrieri match by a set score of 2-1?: 0.20/0.23 mid 21.5%, model 25.4% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17COPGUE-COP20` Will Kimmer Coppejans win the Kimmer Coppejans vs Andrea Guerrieri match by a set score of 2-0?: 0.21/0.23 mid 22.0%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nikita Belozertsev vs Luka Talan Lopatic -- M15 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-17T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212589:tml:B0V0:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikita Belozertsev (`KXITFMATCH-26OCT17BELTAL-BEL`) | 0.63 / 0.66 (1) | 64.5% | 60.4% | 56.1% | 58.2% [58.1%-58.2%] | -- | -- | -- | -- | PASS | -4.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Luka Talan Lopatic (`KXITFMATCH-26OCT17BELTAL-TAL`) | 0.34 / 0.37 (547) | 35.5% | 39.6% | 43.9% | 41.8% [41.8%-41.9%] | -- | -- | -- | -- | PASS | +4.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 199.0, B 0.0; serve-point win A 61.7%, B 40.3%; Elo A 1345.7, B 1286.5; model uncertainty 0.0005
* Form inputs: days since last match A 173, B 1055; matches on record A 3, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Finn Murgett vs Peter Makk -- M15 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-17T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207407:208818:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Peter Makk (`KXITFMATCH-26OCT17MURMAK-MAK`) | 0.63 / 0.66 (42) | 64.5% | 54.4% | 51.5% | 51.0% [51.0%-52.0%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.1 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Finn Murgett (`KXITFMATCH-26OCT17MURMAK-MUR`) | 0.34 / 0.36 (245) | 35.0% | 45.6% | 48.5% | 49.0% [48.0%-49.0%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.6 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 278.0; serve-point win A 62.6%, B 36.5%; Elo A 1222.1, B 1231.4; model uncertainty 0.0051
* Form inputs: days since last match A 1069, B 28; matches on record A 15, B 32; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amit Vales vs Giulio Perego -- M15 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-17T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211707:212280:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giulio Perego (`KXITFMATCH-26OCT17VALPER-PER`) | 0.32 / 0.36 (730) | 34.0% | 43.3% | 53.1% | 50.0% [47.9%-51.0%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.3 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amit Vales (`KXITFMATCH-26OCT17VALPER-VAL`) | 0.63 / 0.67 (41) | 65.0% | 56.7% | 46.9% | 50.0% [49.0%-52.0%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.3 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 397.0, B 0.0; serve-point win A 61.7%, B 39.6%; Elo A 1315.0, B 1314.2; model uncertainty 0.0154
* Form inputs: days since last match A 29, B 698; matches on record A 61, B 22; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ioannis Xilas vs Jip Van Assendelft -- M15 Heraklion QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-17T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209354:210206:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jip Van Assendelft (`KXITFMATCH-26OCT17XILVAN-VAN`) | 0.08 / 0.10 (6718) | 9.0% | 19.8% | 62.8% | 35.7% [31.9%-38.7%] | 10.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.8 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ioannis Xilas (`KXITFMATCH-26OCT17XILVAN-XIL`) | 0.90 / 0.93 (7200) | 91.5% | 80.2% | 37.2% | 64.3% [61.3%-68.1%] | 89.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.3 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 992.0, B 0.0; serve-point win A 62.0%, B 44.5%; Elo A 1344.3, B 1240.0; model uncertainty 0.0339
* Form inputs: days since last match A 96, B 838; matches on record A 90, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.038, surface_pool_high -0.030, surface_dev_loose -0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniel Cukierman / Fernando Romboli vs Jarno Jans / Joran Vliegen -- ATP Challenger Olbia F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-17T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17CUKROMJANVLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Cukierman / Fernando Romboli (`KXATPCHALLENGERDOUBLES-26OCT17CUKROMJANVLI-CUKROM`) | 0.49 / 0.51 (97) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jarno Jans / Joran Vliegen (`KXATPCHALLENGERDOUBLES-26OCT17CUKROMJANVLI-JANVLI`) | 0.48 / 0.50 (37) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Felix Gill vs Radu Mihai Papoe -- ATP Challenger Catania SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-17T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208269:208457:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Gill (`KXATPCHALLENGERMATCH-26OCT17GILPAP-GIL`) | 0.40 / 0.41 (21269) | 40.5% | 49.5% | 50.0% | 50.0% [49.5%-50.0%] | 55.4% | 54.8% | 54.8% | MODEL_LONE_OUTLIER | PASS | +9.0 pp | NORMAL | AGING | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Radu Mihai Papoe (`KXATPCHALLENGERMATCH-26OCT17GILPAP-PAP`) | 0.59 / 0.60 (17193) | 59.5% | 50.5% | 50.0% | 50.0% [50.0%-50.5%] | 44.6% | 45.1% | 45.1% | MODEL_LONE_OUTLIER | SHADOW_BET | -9.0 pp | NORMAL | AGING | B / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2694.0, B 833.0; serve-point win A 59.8%, B 40.1%; Elo A 1649.8, B 1652.1; model uncertainty 0.0026
* Form inputs: days since last match A 26, B 29; matches on record A 281, B 124; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Kristijan Juhas vs Nikita Mashtakov -- M15 Bol SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-17T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209099:tml:MW62:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristijan Juhas (`KXITFMATCH-26OCT17JUHMAS-JUH`) | 0.77 / 0.82 (87) | 79.5% | 39.9% | 61.7% | 34.0% [33.8%-34.1%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -39.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Nikita Mashtakov (`KXITFMATCH-26OCT17JUHMAS-MAS`) | 0.18 / 0.22 (80) | 20.0% | 60.1% | 38.3% | 66.0% [65.9%-66.2%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +40.1 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 306.0; serve-point win A 59.0%, B 39.1%; Elo A 1298.8, B 1408.9; model uncertainty 0.0012
* Form inputs: days since last match A 852, B 26; matches on record A 56, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT17JUHMAS-MAS  (YES = Nikita Mashtakov)
Model: 60%
Kalshi: 20%
Gap: +40 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alice Tubello vs Alisa Oktiabreva -- W35 Heraklion SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-17T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220554:260765:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alisa Oktiabreva (`KXITFWMATCH-26OCT17TUBOKT-OKT`) | 0.79 / 0.82 (6) | 80.5% | 61.1% | 46.8% | 52.1% [50.5%-54.8%] | 72.4% | -- | 72.4% | MODEL_LONE_OUTLIER | PASS | -19.4 pp | HIGH_REVIEW | AGING | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Alice Tubello (`KXITFWMATCH-26OCT17TUBOKT-TUB`) | 0.17 / 0.19 (5) | 18.0% | 38.9% | 53.2% | 47.9% [45.2%-49.5%] | 27.6% | -- | 27.6% | MODEL_LONE_OUTLIER | WATCH | +20.9 pp | HIGH_REVIEW | AGING | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 2580.0, B 1999.0; serve-point win A 48.5%, B 49.4%; Elo A 1707.4, B 1777.6; model uncertainty 0.0214
* Form inputs: days since last match A 23, B 89; matches on record A 332, B 67; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17TUBOKT-TUB  (YES = Alice Tubello)
Model: 39%
Kalshi: 18%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.027, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francesco Passaro vs Matej Dodig -- ATP Challenger Maia SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 14:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-17T14:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208859:212063:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matej Dodig (`KXATPCHALLENGERMATCH-26OCT17PASDOD-DOD`) | 0.59 / 0.60 (17032) | 59.5% | 58.3% | 59.7% | 57.3% [53.9%-58.7%] | 59.2% | 60.3% | 60.3% | MODEL_LONE_OUTLIER | PASS | -1.2 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Francesco Passaro (`KXATPCHALLENGERMATCH-26OCT17PASDOD-PAS`) | 0.39 / 0.40 (26372) | 39.5% | 41.7% | 40.3% | 42.7% [41.3%-46.1%] | 40.8% | 39.6% | 39.6% | MODEL_LONE_OUTLIER | WATCH | +2.2 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3936.0, B 3779.0; serve-point win A 64.8%, B 33.5%; Elo A 1730.9, B 1738.9; model uncertainty 0.024
* Form inputs: days since last match A 12, B 12; matches on record A 355, B 215; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.009, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Lucie Petruzelova vs Luisina Giovannini -- W50 Stara Zagora QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 14:34Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T14:34:40Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221219:236972:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luisina Giovannini (`KXITFWMATCH-26OCT17PETGIO-GIO`) | 0.94 / 0.96 (155) | 95.0% | 96.1% | 94.1% | 93.3% [91.0%-94.7%] | -- | -- | -- | -- | WATCH | +1.1 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lucie Petruzelova (`KXITFWMATCH-26OCT17PETGIO-PET`) | 0.04 / 0.05 (77) | 4.5% | 3.9% | 5.9% | 6.7% [5.3%-9.0%] | -- | -- | -- | -- | PASS | -0.6 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1518.0, B 3057.0; serve-point win A 48.2%, B 38.5%; Elo A 1321.0, B 1751.6; model uncertainty 0.0184
* Form inputs: days since last match A 187, B 54; matches on record A 141, B 199; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martin Damm Jr vs Buvaysar Gadamauri -- ATP Brussels Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-17 17:00Z
* Current expected start: 2026-10-17 15:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-17 14:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-120_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-17T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:102093:207527:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Damm Jr (`KXATPMATCH-26OCT17DAMGAD-DAM`) | 0.84 / 0.85 (11237) | 84.5% | 56.3% | 46.6% | 56.2% [51.4%-66.0%] | 81.8% | 84.4% | 83.1% | MODEL_LONE_OUTLIER | PASS | -28.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Buvaysar Gadamauri (`KXATPMATCH-26OCT17DAMGAD-GAD`) | 0.14 / 0.15 (31515) | 14.5% | 43.7% | 53.4% | 43.8% [34.0%-48.6%] | 18.2% | 15.7% | 16.9% | KALSHI_LONE_OUTLIER | PASS | +29.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3075.0, B 2063.0; serve-point win A 67.9%, B 33.4%; Elo A 1594.2, B 1460.3; model uncertainty 0.073
* Form inputs: days since last match A 726, B 12; matches on record A 252, B 234; data quality F

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT17DAMGAD-GAD  (YES = Buvaysar Gadamauri)
Model: 44%
Kalshi: 14%
Gap: +29 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.048, surface_pool_high +0.047, surface_dev_loose -0.005, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26OCT17DAMGAD-DAM20` Will Martin Damm Jr win the Martin Damm Jr vs Buvaysar Gadamauri match by a set score of 2-0?: 0.60/0.64 mid 62.0%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap -32.6 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data POOR
  * `KXATPGSPREAD-26OCT17DAMGAD-DAM3` Will Martin Damm Jr win at least 2.5 more games than Buvaysar Gadamauri?: 0.53/0.90 mid 71.5%, model 39.0% (projection_v2.0 (prediction ledger)) -- gap -32.5 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data POOR
  * `KXATPGSPREAD-26OCT17DAMGAD-DAM6` Will Martin Damm Jr win at least 5.5 more games than Buvaysar Gadamauri?: 0.29/0.33 mid 31.0%, model 7.1% (projection_v2.0 (prediction ledger)) -- gap -23.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data POOR
  * `KXATPSETWINNER-26OCT17DAMGAD-1-DAM` Will Martin Damm Jr win set 1 in the Martin Damm Jr vs Buvaysar Gadamauri match: 0.76/0.79 mid 77.5%, model 54.2% (projection_v2.0 (prediction ledger)) -- gap -23.3 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT17DAMGAD-1-GAD` Will Buvaysar Gadamauri win set 1 in the Martin Damm Jr vs Buvaysar Gadamauri match: 0.21/0.24 mid 22.5%, model 45.8% (projection_v2.0 (prediction ledger)) -- gap +23.3 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT17DAMGAD-2-DAM` Will Martin Damm Jr win set 2 in the Martin Damm Jr vs Buvaysar Gadamauri match: 0.76/0.79 mid 77.5%, model 54.2% (projection_v2.0 (prediction ledger)) -- gap -23.3 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT17DAMGAD-2-GAD` Will Buvaysar Gadamauri win set 2 in the Martin Damm Jr vs Buvaysar Gadamauri match: 0.21/0.24 mid 22.5%, model 45.8% (projection_v2.0 (prediction ledger)) -- gap +23.3 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data POOR
  * `KXATPGTOTAL-26OCT17DAMGAD-21` Over 20.5 games: 0.58/0.60 mid 59.0%, model 79.1% (projection_v2.0 (prediction ledger)) -- gap +20.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data POOR
  * `KXATPGTOTAL-26OCT17DAMGAD-26` Over 25.5 games: 0.28/0.41 mid 34.5%, model 52.9% (projection_v2.0 (prediction ledger)) -- gap +18.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data POOR
  * `KXATPGTOTAL-26OCT17DAMGAD-16` Over 15.5 games: 0.76/0.95 mid 85.5%, model 99.6% (projection_v2.0 (prediction ledger)) -- gap +14.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT17DAMGAD-GAD20` Will Buvaysar Gadamauri win the Martin Damm Jr vs Buvaysar Gadamauri match by a set score of 2-0?: 0.05/0.09 mid 7.0%, model 20.9% (projection_v2.0 (prediction ledger)) -- gap +13.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT17DAMGAD-GAD21` Will Buvaysar Gadamauri win the Martin Damm Jr vs Buvaysar Gadamauri match by a set score of 2-1?: 0.07/0.11 mid 9.0%, model 22.7% (projection_v2.0 (prediction ledger)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data POOR
  * `KXATPGSPREAD-26OCT17DAMGAD-DAM9` Will Martin Damm Jr win at least 8.5 more games than Buvaysar Gadamauri?: 0.01/0.23 mid 12.0%, model 0.3% (projection_v2.0 (prediction ledger)) -- gap -11.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT17DAMGAD-DAM21` Will Martin Damm Jr win the Martin Damm Jr vs Buvaysar Gadamauri match by a set score of 2-1?: 0.18/0.20 mid 19.0%, model 26.9% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data POOR
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aziz Dougaz vs Tom Gentzsch -- ATP Brussels Q1

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-17 17:00Z
* Current expected start: 2026-10-17 15:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-17 14:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-120_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-17T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144826:210167:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aziz Dougaz (`KXATPMATCH-26OCT17DOUGEN-DOU`) | 0.46 / 0.47 (2501) | 46.5% | 54.1% | 52.9% | 55.3% [52.4%-57.7%] | 44.4% | 47.4% | 45.9% | MARKETS_AGREE | SHADOW_BET | +7.6 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Tom Gentzsch (`KXATPMATCH-26OCT17DOUGEN-GEN`) | 0.54 / 0.55 (55371) | 54.5% | 45.9% | 47.1% | 44.7% [42.3%-47.6%] | 55.6% | 52.5% | 54.1% | MARKETS_AGREE | PASS | -8.6 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2266.0, B 3256.0; serve-point win A 67.2%, B 33.6%; Elo A 1590.1, B 1527.2; model uncertainty 0.0262
* Form inputs: days since last match A 11, B 26; matches on record A 623, B 260; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.024, surface_dev_loose +0.019, surface_dev_tight -0.014
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT17DOUGEN-GEN4` Will Tom Gentzsch win at least 3.5 more games than Aziz Dougaz?: 0.31/0.36 mid 33.5%, model 20.6% (projection_v2.0 (prediction ledger)) -- gap -12.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17DOUGEN-23` Over 22.5 games: 0.52/0.53 mid 52.5%, model 65.0% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT17DOUGEN-GEN7` Will Tom Gentzsch win at least 6.5 more games than Aziz Dougaz?: 0.01/0.27 mid 14.0%, model 2.1% (projection_v2.0 (prediction ledger)) -- gap -11.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17DOUGEN-18` Over 17.5 games: 0.72/0.98 mid 85.0%, model 96.0% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17DOUGEN-GEN20` Will Tom Gentzsch win the Aziz Dougaz vs Tom Gentzsch match by a set score of 2-0?: 0.30/0.35 mid 32.5%, model 22.4% (projection_v2.0 (prediction ledger)) -- gap -10.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT17DOUGEN-28` Over 27.5 games: 0.31/0.39 mid 35.0%, model 44.0% (projection_v2.0 (prediction ledger)) -- gap +9.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17DOUGEN-DOU21` Will Aziz Dougaz win the Aziz Dougaz vs Tom Gentzsch match by a set score of 2-1?: 0.17/0.21 mid 19.0%, model 26.3% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17DOUGEN-2-DOU` Will Aziz Dougaz win set 2 in the Aziz Dougaz vs Tom Gentzsch match: 0.45/0.47 mid 46.0%, model 52.7% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT17DOUGEN-DOU2` Will Aziz Dougaz win at least 1.5 more games than Tom Gentzsch?: 0.40/0.41 mid 40.5%, model 45.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17DOUGEN-1-DOU` Will Aziz Dougaz win set 1 in the Aziz Dougaz vs Tom Gentzsch match: 0.45/0.50 mid 47.5%, model 52.7% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT17DOUGEN-2-GEN` Will Tom Gentzsch win set 2 in the Aziz Dougaz vs Tom Gentzsch match: 0.50/0.55 mid 52.5%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17DOUGEN-DOU20` Will Aziz Dougaz win the Aziz Dougaz vs Tom Gentzsch match by a set score of 2-0?: 0.20/0.26 mid 23.0%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT17DOUGEN-1-GEN` Will Tom Gentzsch win set 1 in the Aziz Dougaz vs Tom Gentzsch match: 0.50/0.52 mid 51.0%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT17DOUGEN-GEN21` Will Tom Gentzsch win the Aziz Dougaz vs Tom Gentzsch match by a set score of 2-1?: 0.19/0.23 mid 21.0%, model 23.6% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Robin Bertrand vs Sergio Callejon Hernando -- M15 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-17T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209850:212090:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robin Bertrand (`KXITFMATCH-26OCT17BERCAL-BER`) | 0.70 / 0.74 (6) | 72.0% | 67.8% | 47.4% | 64.8% [58.9%-74.9%] | 50.9% | -- | 50.9% | MODEL_LONE_OUTLIER | WATCH | -4.2 pp | NORMAL | AGING | C / LIMITED | EXTERNAL_OUTLIER | VERIFIED |
| Sergio Callejon Hernando (`KXITFMATCH-26OCT17BERCAL-CAL`) | 0.25 / 0.29 (2) | 27.0% | 32.2% | 52.6% | 35.2% [25.1%-41.1%] | 49.0% | -- | 49.0% | MODEL_LONE_OUTLIER | PASS | +5.2 pp | NORMAL | AGING | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 2130.0, B 632.0; serve-point win A 59.8%, B 43.7%; Elo A 1543.6, B 1382.9; model uncertainty 0.0803
* Form inputs: days since last match A 152, B 33; matches on record A 313, B 64; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.033, surface_pool_high -0.030, surface_dev_loose -0.014, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Calvin Mueller vs Mika Petkovic -- M15 Offenbach F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209166:213001:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Calvin Mueller (`KXITFMATCH-26OCT17MUEPET-MUE`) | 0.02 / 0.03 (435) | 2.5% | 24.8% | 60.1% | 40.9% [40.9%-40.9%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +22.3 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mika Petkovic (`KXITFMATCH-26OCT17MUEPET-PET`) | 0.97 / 0.98 (1468) | 97.5% | 75.2% | 39.9% | 59.1% [59.1%-59.1%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -22.3 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 972.0; serve-point win A 58.3%, B 36.3%; Elo A 1277.6, B 1338.0; model uncertainty 0.0002
* Form inputs: days since last match A 2630, B 19; matches on record A 1, B 25; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT17MUEPET-MUE  (YES = Calvin Mueller)
Model: 25%
Kalshi: 2%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Massimo Giunta vs Gianluca Cadenasso -- ATP Challenger Catania SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-17T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210668:211533:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gianluca Cadenasso (`KXATPCHALLENGERMATCH-26OCT17GIUCAD-CAD`) | 0.55 / 0.56 (3085) | 55.5% | 75.2% | 68.8% | 74.3% [72.6%-75.9%] | 55.4% | 55.0% | 55.0% | MODEL_LONE_OUTLIER | WATCH | +19.7 pp | HIGH_REVIEW | AGING | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Massimo Giunta (`KXATPCHALLENGERMATCH-26OCT17GIUCAD-GIU`) | 0.44 / 0.45 (223) | 44.5% | 24.8% | 31.2% | 25.7% [24.1%-27.4%] | 44.6% | 44.9% | 44.9% | MODEL_LONE_OUTLIER | PASS | -19.7 pp | HIGH_REVIEW | AGING | B / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 1067.0, B 1540.0; serve-point win A 60.7%, B 33.8%; Elo A 1350.5, B 1572.1; model uncertainty 0.0161
* Form inputs: days since last match A 12, B 12; matches on record A 99, B 118; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT17GIUCAD-CAD  (YES = Gianluca Cadenasso)
Model: 75%
Kalshi: 56%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: EXTERNAL_STALE
Data quality: B (LIMITED)
Reasons: LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Jerome Kym vs Mika Brunold -- ATP Challenger Roanne SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-17T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208843:209983:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mika Brunold (`KXATPCHALLENGERMATCH-26OCT17KYMBRU-BRU`) | 0.31 / 0.32 (2225) | 31.5% | 30.4% | 27.4% | 27.4% [26.2%-28.6%] | 32.3% | 33.6% | 32.3% | MODEL_LONE_OUTLIER | PASS | -1.1 pp | NORMAL | AGING | F / POOR | ALL_AGREE | VERIFIED |
| Jerome Kym (`KXATPCHALLENGERMATCH-26OCT17KYMBRU-KYM`) | 0.68 / 0.69 (595) | 68.5% | 69.6% | 72.6% | 72.6% [71.4%-73.8%] | 67.7% | 66.3% | 67.7% | MODEL_LONE_OUTLIER | PASS | +1.1 pp | NORMAL | AGING | F / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2885.0, B 1536.0; serve-point win A 65.8%, B 38.3%; Elo A 1683.6, B 1510.5; model uncertainty 0.0122
* Form inputs: days since last match A 19, B 677; matches on record A 249, B 128; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.009, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Korokozidi / Marie Voracek vs Andronicou / Eleni Poulka -- W35 Heraklion SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17KORMARANDELE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andronicou / Eleni Poulka (`KXITFWDOUBLES-26OCT17KORMARANDELE-ANDELE`) | 0.07 / 0.75 (55) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Korokozidi / Marie Voracek (`KXITFWDOUBLES-26OCT17KORMARANDELE-KORMAR`) | 0.07 / 0.97 (15) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Eliska Tichackova vs Tara Wuerth -- W15 Bol SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17TICWUE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eliska Tichackova (`KXITFWMATCH-26OCT17TICWUE-TIC`) | -- / 0.01 (6501) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tara Wuerth (`KXITFWMATCH-26OCT17TICWUE-WUE`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Florent Bax vs Jack Loge -- M25 Luanda SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202147:211504:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florent Bax (`KXITFMATCH-26OCT17BAXLOG-BAX`) | 0.55 / 0.58 (15) | 56.5% | 67.6% | 49.5% | 66.7% [63.0%-69.4%] | 57.0% | -- | 57.0% | MODEL_LONE_OUTLIER | WATCH | +11.1 pp | REVIEW | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Jack Loge (`KXITFMATCH-26OCT17BAXLOG-LOG`) | 0.41 / 0.43 (53) | 42.0% | 32.4% | 50.5% | 33.3% [30.6%-37.0%] | 43.0% | -- | 43.0% | MODEL_LONE_OUTLIER | PASS | -9.6 pp | NORMAL | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2193.0, B 467.0; serve-point win A 63.9%, B 39.7%; Elo A 1538.2, B 1378.5; model uncertainty 0.0318
* Form inputs: days since last match A 33, B 75; matches on record A 261, B 89; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maks Kasnikowski vs Damir Dzumhur -- ATP Challenger Olbia SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-17T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106000:209874:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Damir Dzumhur (`KXATPCHALLENGERMATCH-26OCT17KASDZU-DZU`) | 0.50 / 0.51 (13430) | 50.5% | 57.9% | 51.0% | 57.2% [54.1%-63.2%] | 50.0% | 50.8% | 50.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.4 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Maks Kasnikowski (`KXATPCHALLENGERMATCH-26OCT17KASDZU-KAS`) | 0.48 / 0.49 (5406) | 48.5% | 42.1% | 49.0% | 42.8% [36.8%-45.9%] | 50.0% | 49.6% | 49.6% | MODEL_LONE_OUTLIER | PASS | -6.4 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3242.0, B 4752.0; serve-point win A 58.7%, B 39.7%; Elo A 1592.6, B 1744.2; model uncertainty 0.0453
* Form inputs: days since last match A 12, B 12; matches on record A 273, B 1058; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Kypriotis / Nouchakis (`KXITFDOUBLES-26OCT17KYPNOUNOLPER-KYPNOU`) | 0.06 / 0.27 (101) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nolan / Perego (`KXITFDOUBLES-26OCT17KYPNOUNOLPER-NOLPER`) | 0.17 / 0.82 (100) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Muller / Van Sambeek (`KXITFDOUBLES-26OCT17MULVANWALWRI-MULVAN`) | 0.02 / 0.95 (2) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Walters / Wright (`KXITFDOUBLES-26OCT17MULVANWALWRI-WALWRI`) | 0.06 / 0.90 (100) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nirundorn / van Wyk vs Freire Da Silva / Rivet -- M15 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT17NIRVANFRERIV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Freire Da Silva / Rivet (`KXITFDOUBLES-26OCT17NIRVANFRERIV-FRERIV`) | 0.34 / 0.40 (8) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nirundorn / van Wyk (`KXITFDOUBLES-26OCT17NIRVANFRERIV-NIRVAN`) | 0.51 / 0.63 (76) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kuzmova / Milovanovic vs Barrera Aguirre / Zhu -- W35 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17KUZMILBARZHU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barrera Aguirre / Zhu (`KXITFWDOUBLES-26OCT17KUZMILBARZHU-BARZHU`) | 0.23 / 0.73 (15) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kuzmova / Milovanovic (`KXITFWDOUBLES-26OCT17KUZMILBARZHU-KUZMIL`) | 0.26 / 0.76 (13) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Reguer / Zelnickova vs Sacco / Vaissaud -- W15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17REGZELSACVAI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reguer / Zelnickova (`KXITFWDOUBLES-26OCT17REGZELSACVAI-REGZEL`) | 0.56 / 0.68 (38) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sacco / Vaissaud (`KXITFWDOUBLES-26OCT17REGZELSACVAI-SACVAI`) | 0.32 / 0.43 (49) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Valeriia Artemeva vs Carolina Alves -- W50 Stara Zagora QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-17T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206430:267841:2026-10-17`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carolina Alves (`KXITFWMATCH-26OCT17ARTALV-ALV`) | 0.86 / 0.87 (1661) | 86.5% | 84.2% | 80.8% | 79.0% [76.1%-80.8%] | 73.6% | -- | 73.6% | MODEL_LONE_OUTLIER | WATCH | -2.3 pp | NORMAL | AGING | C / LIMITED | EXTERNAL_OUTLIER | VERIFIED |
| Valeriia Artemeva (`KXITFWMATCH-26OCT17ARTALV-ART`) | 0.13 / 0.14 (1671) | 13.5% | 15.8% | 19.2% | 21.1% [19.2%-23.9%] | 26.4% | -- | 26.4% | ALL_THREE_DISAGREE | PASS | +2.3 pp | NORMAL | AGING | C / LIMITED | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 1430.0, B 3024.0; serve-point win A 48.4%, B 44.1%; Elo A 1338.9, B 1548.8; model uncertainty 0.0236
* Form inputs: days since last match A 187, B 31; matches on record A 41, B 699; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lew Yan Foon / Tubello vs Herazo / Ogescu -- W35 Heraklion SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17LEWTUBHEROGE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Herazo / Ogescu (`KXITFWDOUBLES-26OCT17LEWTUBHEROGE-HEROGE`) | 0.38 / 0.48 (49) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lew Yan Foon / Tubello (`KXITFWDOUBLES-26OCT17LEWTUBHEROGE-LEWTUB`) | 0.02 / 0.62 (65) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Taraba Wallberg / Zeltina vs Bohrer Martins / Ezzat -- W35 Santa Margherita di Pula F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-17 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-17T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT17TARZELBOHEZZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bohrer Martins / Ezzat (`KXITFWDOUBLES-26OCT17TARZELBOHEZZ-BOHEZZ`) | 0.16 / 0.18 (105) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Taraba Wallberg / Zeltina (`KXITFWDOUBLES-26OCT17TARZELBOHEZZ-TARZEL`) | 0.80 / 0.85 (21) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Milos Karol / Andrew Paulson (`KXATPCHALLENGERDOUBLES-26OCT17PERWINKARPAU-KARPAU`) | 0.68 / 0.73 (74) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tiago Pereira / Benjamin Winter Lopez (`KXATPCHALLENGERDOUBLES-26OCT17PERWINKARPAU-PERWIN`) | 0.21 / 0.35 (57) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Jacob Fearnley (`KXATPCHALLENGERMATCH-26OCT17FEANAR-FEA`) | 0.67 / 0.68 (827) | 67.5% | 69.4% | 56.2% | 63.7% [60.8%-67.6%] | 66.4% | 68.4% | -- | INSUFFICIENT_INPUTS | PASS | +1.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luca Nardi (`KXATPCHALLENGERMATCH-26OCT17FEANAR-NAR`) | 0.31 / 0.32 (15444) | 31.5% | 30.6% | 43.8% | 36.2% [32.4%-39.2%] | 33.6% | 32.7% | -- | INSUFFICIENT_INPUTS | WATCH | -0.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4058.0, B 3056.0; serve-point win A 60.9%, B 43.0%; Elo A 1871.8, B 1659.3; model uncertainty 0.034
* Form inputs: days since last match A 19, B 12; matches on record A 178, B 346; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.019, surface_dev_loose -0.019, surface_dev_tight +0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Nicolai Budkov Kjaer (`KXATPCHALLENGERMATCH-26OCT17BUDMAR-BUD`) | 0.70 / 0.71 (3724) | 70.5% | 66.2% | 66.6% | 65.2% [63.0%-67.0%] | 68.8% | 71.1% | -- | INSUFFICIENT_INPUTS | PASS | -4.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matteo Martineau (`KXATPCHALLENGERMATCH-26OCT17BUDMAR-MAR`) | 0.29 / 0.30 (11167) | 29.5% | 33.8% | 33.4% | 34.8% [33.0%-37.0%] | 31.2% | 28.9% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +4.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3085.0, B 4114.0; serve-point win A 67.6%, B 35.9%; Elo A 1656.0, B 1566.6; model uncertainty 0.02
* Form inputs: days since last match A 19, B 19; matches on record A 143, B 540; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.009, surface_dev_loose +0.004, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Biletic / Kajin (`KXITFDOUBLES-26OCT17BILKAJJUHPOP-BILKAJ`) | 0.33 / 0.36 (39) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juhas / Popovic (`KXITFDOUBLES-26OCT17BILKAJJUHPOP-JUHPOP`) | 0.14 / 0.67 (530) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Iannis Miletich (`KXITFMATCH-26OCT17WAZMIL-MIL`) | 0.36 / 0.38 (6325) | 37.0% | 76.9% | 43.9% | 66.9% [65.0%-68.8%] | 38.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +39.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alan Wazny (`KXITFMATCH-26OCT17WAZMIL-WAZ`) | 0.59 / 0.60 (62) | 59.5% | 23.1% | 56.1% | 33.1% [31.2%-35.0%] | 61.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -36.4 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 252.0, B 110.0; serve-point win A 58.3%, B 35.9%; Elo A 1217.0, B 1351.2; model uncertainty 0.0189
* Form inputs: days since last match A 33, B 684; matches on record A 7, B 37; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT17WAZMIL-MIL  (YES = Iannis Miletich)
Model: 77%
Kalshi: 37%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
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
| Added / Faurel (`KXITFDOUBLES-26OCT17BERDOMADDFAU-ADDFAU`) | 0.15 / 0.95 (2) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bernardo / Domingos (`KXITFDOUBLES-26OCT17BERDOMADDFAU-BERDOM`) | 0.04 / 0.91 (400) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Joao Eduardo Schiessl (`KXITFMATCH-26OCT17TOSSCH-SCH`) | 0.77 / 0.78 (1) | 77.5% | 78.8% | 52.0% | 72.2% [69.6%-73.8%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.4 pp | NORMAL | AGING | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rafael Tosetto (`KXITFMATCH-26OCT17TOSSCH-TOS`) | 0.21 / 0.23 (54) | 22.0% | 21.1% | 47.9% | 27.8% [26.2%-30.4%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -0.8 pp | NORMAL | AGING | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 251.0, B 1048.0; serve-point win A 57.9%, B 35.9%; Elo A 1206.5, B 1397.9; model uncertainty 0.0212
* Form inputs: days since last match A 166, B 12; matches on record A 66, B 131; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
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
| Luna Maria Cinalli (`KXITFWMATCH-26OCT17SANCIN-CIN`) | 0.28 / 0.29 (35) | 28.5% | 19.1% | 35.8% | 25.1% [21.8%-27.7%] | 30.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.4 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ana Sofia Sanchez (`KXITFWMATCH-26OCT17SANCIN-SAN`) | 0.69 / 0.71 (1) | 70.0% | 80.9% | 64.2% | 74.9% [72.3%-78.2%] | 69.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +10.9 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3191.0, B 795.0; serve-point win A 53.7%, B 52.8%; Elo A 1620.5, B 1377.8; model uncertainty 0.0295
* Form inputs: days since last match A 35, B 173; matches on record A 854, B 34; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
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
| Hernando Jose Escurra Isnardi (`KXITFMATCH-26OCT17SAKESC-ESC`) | 0.17 / 0.18 (56) | 17.5% | 17.0% | 38.6% | 15.1% [13.4%-17.9%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.5 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pedro Sakamoto (`KXITFMATCH-26OCT17SAKESC-SAK`) | 0.82 / 0.83 (41) | 82.5% | 83.0% | 61.4% | 84.9% [82.1%-86.6%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +0.5 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

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
| Josefina Estevez (`KXITFWMATCH-26OCT17ESTGAT-EST`) | 0.31 / 0.32 (981) | 31.5% | 8.3% | 32.9% | 15.7% [10.9%-19.1%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -23.2 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Barbara Gatica (`KXITFWMATCH-26OCT17ESTGAT-GAT`) | 0.66 / 0.68 (26) | 67.0% | 91.7% | 67.1% | 84.3% [80.9%-89.1%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +24.7 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 732.0, B 633.0; serve-point win A 45.2%, B 44.5%; Elo A 1285.0, B 1649.7; model uncertainty 0.0412
* Form inputs: days since last match A 278, B 1608; matches on record A 55, B 388; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17ESTGAT-GAT  (YES = Barbara Gatica)
Model: 92%
Kalshi: 67%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
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
| Dana Guzman (`KXITFWMATCH-26OCT17GUZSTE-GUZ`) | 0.33 / 0.36 (91) | 34.5% | 19.4% | 63.1% | 31.6% [15.8%-45.7%] | -- | -- | -- | -- | PASS | -15.1 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sloane Stephens (`KXITFWMATCH-26OCT17GUZSTE-STE`) | 0.62 / 0.65 (7) | 63.5% | 80.6% | 36.9% | 68.5% [54.3%-84.2%] | -- | -- | -- | -- | PASS | +17.1 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 812.0, B 2061.0; serve-point win A 51.0%, B 42.5%; Elo A 1552.1, B 1813.0; model uncertainty 0.1495
* Form inputs: days since last match A 243, B 29; matches on record A 42, B 685; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17GUZSTE-STE  (YES = Sloane Stephens)
Model: 81%
Kalshi: 64%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
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
| El Jardi / Frodin (`KXITFWDOUBLES-26OCT17JOHRAPELJFRO-ELJFRO`) | 0.42 / 0.66 (63) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Johnson / Rapolu (`KXITFWDOUBLES-26OCT17JOHRAPELJFRO-JOHRAP`) | 0.05 / 0.58 (0) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Jack Anthrop (`KXITFMATCH-26OCT17ANTSTE-ANT`) | 0.80 / 0.81 (185) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eli Stephenson (`KXITFMATCH-26OCT17ANTSTE-STE`) | 0.18 / 0.19 (6690) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Hugo Dellien (`KXATPCHALLENGERMATCH-26OCT17LADEL-DEL`) | 0.78 / 0.79 (65) | 78.5% | 73.3% | 68.7% | 73.6% [71.9%-75.7%] | 76.9% | 75.5% | -- | INSUFFICIENT_INPUTS | PASS | -5.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juan Manuel La Serna (`KXATPCHALLENGERMATCH-26OCT17LADEL-LA`) | 0.21 / 0.22 (2772) | 21.5% | 26.7% | 31.3% | 26.4% [24.3%-28.1%] | 23.1% | 22.8% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +5.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2310.0, B 4561.0; serve-point win A 55.1%, B 40.2%; Elo A 1525.0, B 1770.7; model uncertainty 0.0193
* Form inputs: days since last match A 40, B 26; matches on record A 138, B 885; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Lucas Andrade Da Silva (`KXITFMATCH-26OCT17MBIAND-AND`) | 0.81 / 0.82 (6797) | 81.5% | 68.7% | 59.0% | 66.6% [64.7%-68.4%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.8 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mwendwa Mbithi (`KXITFMATCH-26OCT17MBIAND-MBI`) | 0.18 / 0.19 (1188) | 18.5% | 31.3% | 41.0% | 33.4% [31.6%-35.3%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.8 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

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
| Theo Papamalamis (`KXITFMATCH-26OCT17SLAPAP-PAP`) | 0.77 / 0.80 (96) | 78.5% | 66.6% | 46.5% | 64.7% [63.7%-65.8%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.9 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nikola Slavic (`KXITFMATCH-26OCT17SLAPAP-SLA`) | 0.20 / 0.22 (6645) | 21.0% | 33.4% | 53.5% | 35.3% [34.2%-36.3%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.4 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

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
| Reese Brantmeier (`KXITFWMATCH-26OCT17BRARIN-BRA`) | 0.72 / 0.76 (1414) | 74.0% | 62.1% | 15.7% | 46.9% [39.7%-53.1%] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.9 pp | REVIEW | AGING | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kajsa Rinaldo Persson (`KXITFWMATCH-26OCT17BRARIN-RIN`) | 0.24 / 0.27 (27) | 25.5% | 37.9% | 84.3% | 53.1% [46.9%-60.3%] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +12.4 pp | REVIEW | AGING | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

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
| Ayala / Romero (`KXITFWDOUBLES-26OCT17GATPERAYAROM-AYAROM`) | 0.30 / 0.49 (107) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gatica / Pereira (`KXITFWDOUBLES-26OCT17GATPERAYAROM-GATPER`) | 0.27 / 0.70 (0) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Ariana Arseneault (`KXITFWMATCH-26OCT17XUXARS-ARS`) | 0.50 / 0.51 (8) | 50.5% | 35.4% | 55.8% | 46.8% [39.0%-50.0%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.2 pp | HIGH_REVIEW (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mimi Xu (`KXITFWMATCH-26OCT17XUXARS-XUX`) | 0.48 / 0.49 (490) | 48.5% | 64.6% | 44.2% | 53.2% [50.0%-61.0%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +16.1 pp | HIGH_REVIEW (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1841.0, B 2049.0; serve-point win A 57.6%, B 45.3%; Elo A 1592.8, B 1496.9; model uncertainty 0.0551
* Form inputs: days since last match A 257, B 26; matches on record A 98, B 129; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17XUXARS-XUX  (YES = Mimi Xu)
Model: 65%
Kalshi: 48%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
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
| Julieta Pareja (`KXITFWMATCH-26OCT17PENPAR-PAR`) | 0.79 / 0.81 (67) | 80.0% | 79.0% | 54.2% | 66.9% [62.5%-75.1%] | 78.6% | -- | 78.6% | MODEL_LONE_OUTLIER | PASS | -1.0 pp | NORMAL | AGING | B / ADEQUATE | ALL_AGREE | VERIFIED |
| Kristina Penickova (`KXITFWMATCH-26OCT17PENPAR-PEN`) | 0.18 / 0.21 (6528) | 19.5% | 21.0% | 45.8% | 33.1% [24.9%-37.5%] | 21.4% | -- | 21.4% | MODEL_LONE_OUTLIER | WATCH | +1.5 pp | NORMAL | AGING | B / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1178.0, B 1273.0; serve-point win A 53.3%, B 40.6%; Elo A 1497.9, B 1696.0; model uncertainty 0.0634
* Form inputs: days since last match A 52, B 38; matches on record A 39, B 63; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.010, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
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
| Debru / Marionneau (`KXITFDOUBLES-26OCT17RODTOKDEBMAR-DEBMAR`) | 0.08 / 0.63 (2) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Roddick / Tokac (`KXITFDOUBLES-26OCT17RODTOKDEBMAR-RODTOK`) | 0.36 / 0.48 (64) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Arseneault / Lacasse (`KXITFWDOUBLES-26OCT17ARSLACBRAXUX-ARSLAC`) | 0.05 / 0.59 (52) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Brantmeier / Xu (`KXITFWDOUBLES-26OCT17ARSLACBRAXUX-BRAXUX`) | 0.41 / 0.46 (9) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Francisco Comesana (`KXATPCHALLENGERMATCH-26OCT17COMSEY-COM`) | 0.41 / 0.42 (1278) | 41.5% | 45.6% | 31.0% | 37.3% [34.1%-41.6%] | -- | 41.9% | -- | INSUFFICIENT_INPUTS | PASS | +4.1 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thiago Seyboth Wild (`KXATPCHALLENGERMATCH-26OCT17COMSEY-SEY`) | 0.57 / 0.59 (10600) | 58.0% | 54.4% | 69.0% | 62.7% [58.4%-65.9%] | -- | 58.3% | -- | INSUFFICIENT_INPUTS | WATCH | -3.6 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4413.0, B 3996.0; serve-point win A 64.0%, B 35.1%; Elo A 1777.7, B 1742.2; model uncertainty 0.0375
* Form inputs: days since last match A 12, B 12; matches on record A 441, B 485; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.014, surface_dev_tight +0.024
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

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
| Alex Hernandez (`KXITFMATCH-26OCT17HEROSO-HER`) | 0.57 / 0.62 (171) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juan Sebastian Osorio (`KXITFMATCH-26OCT17HEROSO-OSO`) | 0.36 / 0.42 (79) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Brostrom Poulsen / Slavic (`KXITFDOUBLES-26OCT17BROSLAKAPSHE-BROSLA`) | 0.08 / 0.84 (156) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kapasi / Sheldon (`KXITFDOUBLES-26OCT17BROSLAKAPSHE-KAPSHE`) | 0.04 / 0.29 (39) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Henrique Chabalgoity / Fontes Damorim (`KXITFDOUBLES-26OCT17VICPAGHENFON-HENFON`) | 0.04 / 0.23 (36) | 13.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victor Couto Loureiro / Pagotto (`KXITFDOUBLES-26OCT17VICPAGHENFON-VICPAG`) | 0.08 / 0.96 (27) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Kristina Liutova (`KXITFWMATCH-26OCT17LIUZAR-LIU`) | 0.63 / 0.69 (53) | 66.0% | 46.3% | 52.1% | 44.1% [37.4%-51.1%] | -- | -- | -- | -- | PASS | -19.7 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Renata Zarazua (`KXITFWMATCH-26OCT17LIUZAR-ZAR`) | 0.31 / 0.34 (30) | 32.5% | 53.7% | 47.9% | 55.9% [48.9%-62.6%] | -- | -- | -- | -- | WATCH | +21.2 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 754.0, B 4923.0; serve-point win A 53.6%, B 45.8%; Elo A 1701.6, B 1765.5; model uncertainty 0.0682
* Form inputs: days since last match A 47, B 7; matches on record A 37, B 698; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17LIUZAR-ZAR  (YES = Renata Zarazua)
Model: 54%
Kalshi: 32%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
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
| Lui Maxted (`KXITFMATCH-26OCT17MAXROL-MAX`) | 0.59 / 0.61 (7960) | 60.0% | 37.2% | 47.5% | 35.2% [34.2%-35.2%] | -- | -- | -- | -- | PASS | -22.8 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cosme Rolland de Ravel (`KXITFMATCH-26OCT17MAXROL-ROL`) | 0.40 / 0.41 (2) | 40.5% | 62.8% | 52.5% | 64.8% [64.8%-65.8%] | -- | -- | -- | -- | PASS | +22.3 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 473.0; serve-point win A 61.1%, B 36.3%; Elo A 1353.4, B 1459.5; model uncertainty 0.005
* Form inputs: days since last match A 726, B 110; matches on record A 16, B 7; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT17MAXROL-ROL  (YES = Cosme Rolland de Ravel)
Model: 63%
Kalshi: 40%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Diego Hidalgo / Mariano Kestelboim (`KXATPCHALLENGERDOUBLES-26OCT17HIDKESMIGRIB-HIDKES`) | 0.06 / 0.94 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luis Guto Miguel / Eduardo Ribeiro (`KXATPCHALLENGERDOUBLES-26OCT17HIDKESMIGRIB-MIGRIB`) | 0.06 / 0.94 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Alvarado / Mbithi (`KXITFDOUBLES-26OCT17SEBURRALVMBI-ALVMBI`) | 0.05 / 0.32 (36) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sebastian Gomez / Urrea (`KXITFDOUBLES-26OCT17SEBURRALVMBI-SEBURR`) | 0.07 / 0.84 (156) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Alastair Gray (`KXITFMATCH-26OCT17GRAMOS-GRA`) | 0.59 / 0.62 (29) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dominick Mosejczuk (`KXITFMATCH-26OCT17GRAMOS-MOS`) | 0.36 / 0.37 (4) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maya Joint vs Kayla Day -- WTA Osaka Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-18 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-18 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215037:233741:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kayla Day (`KXWTAMATCH-26OCT17JOIDAY-DAY`) | 0.43 / 0.44 (150) | 43.5% | 47.9% | 74.1% | 64.4% [50.0%-69.2%] | 44.4% | 43.8% | -- | INSUFFICIENT_INPUTS | WATCH | +4.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maya Joint (`KXWTAMATCH-26OCT17JOIDAY-JOI`) | 0.56 / 0.57 (6375) | 56.5% | 52.0% | 25.9% | 35.6% [30.8%-50.0%] | 55.6% | 56.4% | -- | INSUFFICIENT_INPUTS | PASS | -4.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3855.0, B 3639.0; serve-point win A 57.0%, B 43.4%; Elo A 1824.8, B 1748.9; model uncertainty 0.096
* Form inputs: days since last match A 0, B 0; matches on record A 237, B 478; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.024, surface_dev_tight +0.025
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17JOIDAY-16` Over 15.5 games: 0.02/0.98 mid 50.0%, model 97.4% (projection_v2.0 (prediction ledger)) -- gap +47.4 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17JOIDAY-26` Over 25.5 games: 0.27/0.39 mid 33.0%, model 45.0% (projection_v2.0 (prediction ledger)) -- gap +12.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17JOIDAY-21` Over 20.5 games: 0.55/0.58 mid 56.5%, model 68.2% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17JOIDAY-2-JOI` Will Maya Joint win set 2 in the Maya Joint vs Kayla Day match: 0.48/0.63 mid 55.5%, model 51.4% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17JOIDAY-1-DAY` Will Kayla Day win set 1 in the Maya Joint vs Kayla Day match: 0.43/0.48 mid 45.5%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17JOIDAY-1-JOI` Will Maya Joint win set 1 in the Maya Joint vs Kayla Day match: 0.51/0.57 mid 54.0%, model 51.4% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17JOIDAY-2-DAY` Will Kayla Day win set 2 in the Maya Joint vs Kayla Day match: 0.37/0.61 mid 49.0%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Taylah Preston vs Emerson Jones -- WTA Osaka Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-18 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-18 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:223194:263644:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emerson Jones (`KXWTAMATCH-26OCT17PREJON-JON`) | 0.50 / 0.52 (160) | 51.0% | 44.3% | 35.0% | 38.0% [37.0%-42.1%] | -- | 52.6% | -- | INSUFFICIENT_INPUTS | PASS | -6.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Taylah Preston (`KXWTAMATCH-26OCT17PREJON-PRE`) | 0.47 / 0.51 (8862) | 49.0% | 55.7% | 65.0% | 62.0% [57.9%-63.0%] | -- | 47.4% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +6.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5098.0, B 3547.0; serve-point win A 56.5%, B 44.6%; Elo A 1818.4, B 1792.5; model uncertainty 0.0255
* Form inputs: days since last match A 0, B 0; matches on record A 265, B 149; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.015
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17PREJON-17` Over 16.5 games: 0.03/0.99 mid 51.0%, model 93.5% (projection_v2.0 (prediction ledger)) -- gap +42.5 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17PREJON-22` Over 21.5 games: 0.49/0.51 mid 50.0%, model 62.5% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17PREJON-27` Over 26.5 games: 0.03/0.99 mid 51.0%, model 39.2% (projection_v2.0 (prediction ledger)) -- gap -11.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PREJON-2-JON` Will Emerson Jones win set 2 in the Taylah Preston vs Emerson Jones match: 0.44/0.70 mid 57.0%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap -10.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PREJON-2-PRE` Will Taylah Preston win set 2 in the Taylah Preston vs Emerson Jones match: 0.30/0.61 mid 45.5%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PREJON-1-PRE` Will Taylah Preston win set 1 in the Taylah Preston vs Emerson Jones match: 0.46/0.51 mid 48.5%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PREJON-1-JON` Will Emerson Jones win set 1 in the Taylah Preston vs Emerson Jones match: 0.48/0.53 mid 50.5%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mary Stoiana vs Sayaka Ishii -- WTA Osaka Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-18 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 02:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-18 01:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:223168:259967:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sayaka Ishii (`KXWTAMATCH-26OCT17STOISH-ISH`) | 0.11 / 0.13 (6514) | 12.0% | 21.9% | 19.9% | 23.2% [21.7%-26.5%] | 14.1% | 14.6% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +9.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mary Stoiana (`KXWTAMATCH-26OCT17STOISH-STO`) | 0.87 / 0.88 (531) | 87.5% | 78.1% | 80.2% | 76.8% [73.5%-78.3%] | 85.9% | 87.1% | -- | INSUFFICIENT_INPUTS | PASS | -9.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2840.0, B 1713.0; serve-point win A 61.7%, B 44.2%; Elo A 1802.0, B 1641.6; model uncertainty 0.0239
* Form inputs: days since last match A 0, B 0; matches on record A 141, B 190; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.016, surface_dev_loose +0.011, surface_dev_tight -0.016
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXWTAGTOTAL-26OCT17STOISH-19` Over 18.5 games: 0.50/0.51 mid 50.5%, model 76.0% (projection_v2.0 (prediction ledger)) -- gap +25.5 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17STOISH-1-ISH` Will Sayaka Ishii win set 1 in the Mary Stoiana vs Sayaka Ishii match: 0.07/0.21 mid 14.0%, model 30.2% (projection_v2.0 (prediction ledger)) -- gap +16.2 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17STOISH-24` Over 23.5 games: 0.23/0.34 mid 28.5%, model 44.3% (projection_v2.0 (prediction ledger)) -- gap +15.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17STOISH-2-STO` Will Mary Stoiana win set 2 in the Mary Stoiana vs Sayaka Ishii match: 0.82/0.85 mid 83.5%, model 69.8% (projection_v2.0 (prediction ledger)) -- gap -13.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17STOISH-2-ISH` Will Sayaka Ishii win set 2 in the Mary Stoiana vs Sayaka Ishii match: 0.15/0.19 mid 17.0%, model 30.2% (projection_v2.0 (prediction ledger)) -- gap +13.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17STOISH-1-STO` Will Mary Stoiana win set 1 in the Mary Stoiana vs Sayaka Ishii match: 0.82/0.83 mid 82.5%, model 69.8% (projection_v2.0 (prediction ledger)) -- gap -12.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Daria Snigur vs Katarzyna Kawa -- WTA Ningbo Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-18 05:00Z
* Current expected start: 2026-10-18 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-18 02:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-120_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:203514:220750:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katarzyna Kawa (`KXWTAMATCH-26OCT17SNIKAW-KAW`) | 0.17 / 0.18 (1541) | 17.5% | 12.4% | 3.6% | 5.5% [3.9%-15.8%] | -- | 18.3% | -- | INSUFFICIENT_INPUTS | PASS | -5.1 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daria Snigur (`KXWTAMATCH-26OCT17SNIKAW-SNI`) | 0.82 / 0.83 (336) | 82.5% | 87.6% | 96.4% | 94.5% [84.2%-96.1%] | -- | 81.5% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +5.1 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4190.0, B 4311.0; serve-point win A 57.7%, B 50.9%; Elo A 1893.2, B 1606.2; model uncertainty 0.0596
* Form inputs: days since last match A 0, B 0; matches on record A 442, B 702; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.006, surface_pool_high +0.006, surface_dev_loose +0.014, surface_dev_tight -0.022
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17SNIKAW-26` Over 25.5 games: 0.03/0.98 mid 50.5%, model 28.2% (projection_v2.0 (prediction ledger)) -- gap -22.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17SNIKAW-16` Over 15.5 games: 0.54/0.95 mid 74.5%, model 90.5% (projection_v2.0 (prediction ledger)) -- gap +16.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17SNIKAW-21` Over 20.5 games: 0.42/0.43 mid 42.5%, model 48.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17SNIKAW-1-KAW` Will Katarzyna Kawa win set 1 in the Daria Snigur vs Katarzyna Kawa match: 0.13/0.25 mid 19.0%, model 22.0% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17SNIKAW-1-SNI` Will Daria Snigur win set 1 in the Daria Snigur vs Katarzyna Kawa match: 0.73/0.78 mid 75.5%, model 78.0% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17SNIKAW-2-KAW` Will Katarzyna Kawa win set 2 in the Daria Snigur vs Katarzyna Kawa match: 0.13/0.28 mid 20.5%, model 22.0% (projection_v2.0 (prediction ledger)) -- gap +1.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17SNIKAW-2-SNI` Will Daria Snigur win set 2 in the Daria Snigur vs Katarzyna Kawa match: 0.73/0.84 mid 78.5%, model 78.0% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anastasia Zakharova vs Polina Kudermetova -- WTA Ningbo Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-18 05:00Z
* Current expected start: 2026-10-18 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-18 02:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-120_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220435:221236:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Kudermetova (`KXWTAMATCH-26OCT17ZAKKUD-KUD`) | 0.43 / 0.46 (162) | 44.5% | 52.8% | 47.4% | 47.9% [46.8%-49.5%] | -- | 44.8% | -- | INSUFFICIENT_INPUTS | PASS | +8.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Zakharova (`KXWTAMATCH-26OCT17ZAKKUD-ZAK`) | 0.55 / 0.57 (6572) | 56.0% | 47.2% | 52.6% | 52.1% [50.5%-53.2%] | -- | 55.2% | -- | INSUFFICIENT_INPUTS | PASS | -8.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4628.0, B 4285.0; serve-point win A 55.9%, B 43.6%; Elo A 1819.2, B 1806.1; model uncertainty 0.0132
* Form inputs: days since last match A 0, B 0; matches on record A 479, B 388; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.011, surface_dev_loose +0.005, surface_dev_tight +0.000
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT17ZAKKUD-1-KUD` Will Polina Kudermetova win set 1 in the Anastasia Zakharova vs Polina Kudermetova match: 0.39/0.48 mid 43.5%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17ZAKKUD-2-KUD` Will Polina Kudermetova win set 2 in the Anastasia Zakharova vs Polina Kudermetova match: 0.39/0.49 mid 44.0%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17ZAKKUD-2-ZAK` Will Anastasia Zakharova win set 2 in the Anastasia Zakharova vs Polina Kudermetova match: 0.47/0.65 mid 56.0%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap -7.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17ZAKKUD-1-ZAK` Will Anastasia Zakharova win set 1 in the Anastasia Zakharova vs Polina Kudermetova match: 0.47/0.57 mid 52.0%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Harriet Dart vs Aoi Ito -- WTA Osaka Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-18 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-18 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211279:256684:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harriet Dart (`KXWTAMATCH-26OCT17DARITO-DAR`) | 0.58 / 0.59 (650) | 58.5% | 62.4% | 79.2% | 71.3% [65.6%-74.8%] | 57.5% | 59.6% | 59.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.9 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Aoi Ito (`KXWTAMATCH-26OCT17DARITO-ITO`) | 0.40 / 0.42 (1780) | 41.0% | 37.6% | 20.8% | 28.7% [25.2%-34.4%] | 42.5% | 40.5% | 40.5% | MODEL_LONE_OUTLIER | PASS | -3.4 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4244.0, B 2722.0; serve-point win A 55.0%, B 47.3%; Elo A 1789.0, B 1765.2; model uncertainty 0.0461
* Form inputs: days since last match A 0, B 0; matches on record A 674, B 302; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.027, surface_pool_high -0.028, surface_dev_loose +0.013, surface_dev_tight -0.014
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17DARITO-18` Over 17.5 games: 0.03/0.98 mid 50.5%, model 86.0% (projection_v2.0 (prediction ledger)) -- gap +35.5 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17DARITO-28` Over 27.5 games: 0.03/0.98 mid 50.5%, model 32.3% (projection_v2.0 (prediction ledger)) -- gap -18.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17DARITO-23` Over 22.5 games: 0.44/0.45 mid 44.5%, model 54.1% (projection_v2.0 (prediction ledger)) -- gap +9.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17DARITO-1-DAR` Will Harriet Dart win set 1 in the Harriet Dart vs Aoi Ito match: 0.50/0.57 mid 53.5%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17DARITO-2-DAR` Will Harriet Dart win set 2 in the Harriet Dart vs Aoi Ito match: 0.50/0.63 mid 56.5%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17DARITO-1-ITO` Will Aoi Ito win set 1 in the Harriet Dart vs Aoi Ito match: 0.38/0.46 mid 42.0%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17DARITO-2-ITO` Will Aoi Ito win set 2 in the Harriet Dart vs Aoi Ito match: 0.37/0.46 mid 41.5%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sinja Kraus vs Sofia Kenin -- WTA Osaka Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-18 04:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-18 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213550:221257:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Kenin (`KXWTAMATCH-26OCT17KRAKEN-KEN`) | 0.54 / 0.56 (115) | 55.0% | 50.5% | 29.6% | 38.2% [34.8%-47.4%] | -- | 51.3% | -- | INSUFFICIENT_INPUTS | PASS | -4.5 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sinja Kraus (`KXWTAMATCH-26OCT17KRAKEN-KRA`) | 0.44 / 0.45 (6845) | 44.5% | 49.5% | 70.4% | 61.8% [52.6%-65.2%] | -- | 48.7% | -- | INSUFFICIENT_INPUTS | WATCH | +5.0 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5054.0, B 3897.0; serve-point win A 58.4%, B 41.5%; Elo A 1722.8, B 1812.1; model uncertainty 0.0631
* Form inputs: days since last match A 0, B 0; matches on record A 493, B 525; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.020, surface_dev_loose +0.015, surface_dev_tight -0.020
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17KRAKEN-16` Over 15.5 games: 0.03/0.99 mid 51.0%, model 97.8% (projection_v2.0 (prediction ledger)) -- gap +46.8 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT17KRAKEN-21` Over 20.5 games: 0.53/0.56 mid 54.5%, model 69.3% (projection_v2.0 (prediction ledger)) -- gap +14.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT17KRAKEN-2-KEN` Will Sofia Kenin win set 2 in the Sinja Kraus vs Sofia Kenin match: 0.47/0.70 mid 58.5%, model 50.3% (projection_v2.0 (prediction ledger)) -- gap -8.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT17KRAKEN-1-KRA` Will Sinja Kraus win set 1 in the Sinja Kraus vs Sofia Kenin match: 0.39/0.49 mid 44.0%, model 49.6% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT17KRAKEN-26` Over 25.5 games: 0.03/0.98 mid 50.5%, model 45.9% (projection_v2.0 (prediction ledger)) -- gap -4.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT17KRAKEN-2-KRA` Will Sinja Kraus win set 2 in the Sinja Kraus vs Sofia Kenin match: 0.39/0.55 mid 47.0%, model 49.6% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT17KRAKEN-1-KEN` Will Sofia Kenin win set 1 in the Sinja Kraus vs Sofia Kenin match: 0.47/0.56 mid 51.5%, model 50.3% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Claire Liu vs Maddison Inglis -- WTA Osaka Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-18 06:40Z
* Current expected start: 2026-10-18 04:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-18 03:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T06:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213666:214906:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maddison Inglis (`KXWTAMATCH-26OCT17LIUING-ING`) | 0.34 / 0.36 (7350) | 35.0% | 45.7% | 46.4% | 47.9% [41.2%-51.0%] | -- | 39.4% | -- | INSUFFICIENT_INPUTS | WATCH | +10.7 pp | REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Claire Liu (`KXWTAMATCH-26OCT17LIUING-LIU`) | 0.65 / 0.66 (258) | 65.5% | 54.3% | 53.6% | 52.1% [49.0%-58.8%] | -- | 60.7% | -- | INSUFFICIENT_INPUTS | PASS | -11.2 pp | REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3837.0, B 3027.0; serve-point win A 58.9%, B 41.9%; Elo A 1770.0, B 1770.9; model uncertainty 0.0494
* Form inputs: days since last match A 0, B 0; matches on record A 455, B 482; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.042, surface_pool_high -0.031, surface_dev_loose +0.005, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17LIUING-18` Over 17.5 games: 0.15/0.97 mid 56.0%, model 89.4% (projection_v2.0 (prediction ledger)) -- gap +33.4 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT17LIUING-28` Over 27.5 games: 0.02/0.99 mid 50.5%, model 36.0% (projection_v2.0 (prediction ledger)) -- gap -14.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT17LIUING-2-LIU` Will Claire Liu win set 2 in the Claire Liu vs Maddison Inglis match: 0.57/0.75 mid 66.0%, model 52.9% (projection_v2.0 (prediction ledger)) -- gap -13.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26OCT17LIUING-23` Over 22.5 games: 0.43/0.48 mid 45.5%, model 57.2% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26OCT17LIUING-1-ING` Will Maddison Inglis win set 1 in the Claire Liu vs Maddison Inglis match: 0.33/0.40 mid 36.5%, model 47.1% (projection_v2.0 (prediction ledger)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT17LIUING-1-LIU` Will Claire Liu win set 1 in the Claire Liu vs Maddison Inglis match: 0.57/0.63 mid 60.0%, model 52.9% (projection_v2.0 (prediction ledger)) -- gap -7.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT17LIUING-2-ING` Will Maddison Inglis win set 2 in the Claire Liu vs Maddison Inglis match: 0.30/0.50 mid 40.0%, model 47.1% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Connie Ma (`KXITFWMATCH-26OCT17MAXMAX2-MAX`) | 0.64 / 0.66 (3) | 65.0% | 29.5% | 26.1% | 31.0% [29.0%-32.9%] | -- | -- | -- | -- | PASS | -35.5 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Lea Ma (`KXITFWMATCH-26OCT17MAXMAX2-MAX2`) | 0.33 / 0.35 (9) | 34.0% | 70.5% | 73.9% | 69.0% [67.1%-71.0%] | -- | -- | -- | -- | PASS | +36.5 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 2727.0; serve-point win A 56.5%, B 39.4%; Elo A 1475.0, B 1614.7; model uncertainty 0.0195
* Form inputs: days since last match A 1839, B 34; matches on record A 21, B 168; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT17MAXMAX2-MAX2  (YES = Lea Ma)
Model: 71%
Kalshi: 34%
Gap: +37 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.019, surface_dev_loose +0.001, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alycia Parks vs Yulia Putintseva -- WTA Ningbo Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-18 05:00Z
* Current expected start: 2026-10-18 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-18 03:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-30_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201709:219917:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alycia Parks (`KXWTAMATCH-26OCT17PARPUT-PAR`) | 0.25 / 0.26 (958) | 25.5% | 38.4% | 41.2% | 39.1% [37.1%-40.7%] | -- | 25.1% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +12.9 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yulia Putintseva (`KXWTAMATCH-26OCT17PARPUT-PUT`) | 0.73 / 0.74 (4) | 73.5% | 61.6% | 58.8% | 60.9% [59.3%-62.9%] | -- | 75.1% | -- | INSUFFICIENT_INPUTS | PASS | -11.9 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5263.0, B 4366.0; serve-point win A 56.9%, B 40.8%; Elo A 1775.0, B 1893.3; model uncertainty 0.0177
* Form inputs: days since last match A 0, B 0; matches on record A 437, B 857; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT17PARPUT-17` Over 16.5 games: 0.03/0.98 mid 50.5%, model 94.0% (projection_v2.0 (prediction ledger)) -- gap +43.5 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PARPUT-2-PAR` Will Alycia Parks win set 2 in the Alycia Parks vs Yulia Putintseva match: 0.20/0.31 mid 25.5%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap +16.7 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PARPUT-2-PUT` Will Yulia Putintseva win set 2 in the Alycia Parks vs Yulia Putintseva match: 0.66/0.80 mid 73.0%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap -15.2 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17PARPUT-22` Over 21.5 games: 0.46/0.49 mid 47.5%, model 62.6% (projection_v2.0 (prediction ledger)) -- gap +15.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PARPUT-1-PAR` Will Alycia Parks win set 1 in the Alycia Parks vs Yulia Putintseva match: 0.24/0.31 mid 27.5%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap +14.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT17PARPUT-27` Over 26.5 games: 0.03/0.98 mid 50.5%, model 39.4% (projection_v2.0 (prediction ledger)) -- gap -11.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT17PARPUT-1-PUT` Will Yulia Putintseva win set 1 in the Alycia Parks vs Yulia Putintseva match: 0.62/0.69 mid 65.5%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap -7.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anhelina Kalinina vs Aliaksandra Sasnovich -- WTA Ningbo Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-18 07:10Z
* Current expected start: 2026-10-18 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-18 03:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T07:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:205925:211843:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anhelina Kalinina (`KXWTAMATCH-26OCT18KALSAS-KAL`) | 0.08 / 0.93 (200) | 50.5% | 51.5% | 56.8% | 54.8% [52.1%-55.3%] | -- | -- | -- | -- | PASS | +1.0 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aliaksandra Sasnovich (`KXWTAMATCH-26OCT18KALSAS-SAS`) | 0.08 / 0.93 (200) | 50.5% | 48.5% | 43.2% | 45.2% [44.7%-47.9%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4204.0, B 4822.0; serve-point win A 56.1%, B 44.2%; Elo A 1824.8, B 1839.7; model uncertainty 0.0158
* Form inputs: days since last match A 5, B 0; matches on record A 611, B 789; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.000
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Gabriel Diallo vs Rei Sakamoto -- ATP Almaty Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 06:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-18 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:209113:210536:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriel Diallo (`KXATPMATCH-26OCT18DIASAK-DIA`) | 0.38 / 0.43 (7364) | 40.5% | 55.4% | 52.8% | 55.7% [54.2%-57.1%] | -- | 41.1% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +14.9 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rei Sakamoto (`KXATPMATCH-26OCT18DIASAK-SAK`) | 0.58 / 0.62 (6390) | 60.0% | 44.6% | 47.2% | 44.3% [42.9%-45.8%] | -- | 59.1% | -- | INSUFFICIENT_INPUTS | PASS | -15.4 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4598.0, B 3076.0; serve-point win A 69.0%, B 32.2%; Elo A 1825.8, B 1744.4; model uncertainty 0.0141
* Form inputs: days since last match A 0, B 0; matches on record A 277, B 145; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.014, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18DIASAK-19` Over 18.5 games: 0.02/0.99 mid 50.5%, model 94.0% (projection_v2.0 (prediction ledger)) -- gap +43.5 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18DIASAK-1-DIA` Will Gabriel Diallo win set 1 in the Gabriel Diallo vs Rei Sakamoto match: 0.33/0.44 mid 38.5%, model 53.6% (projection_v2.0 (prediction ledger)) -- gap +15.1 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18DIASAK-SAK20` Will Rei Sakamoto win the Gabriel Diallo vs Rei Sakamoto match by a set score of 2-0?: 0.15/0.54 mid 34.5%, model 21.5% (projection_v2.0 (prediction ledger)) -- gap -13.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18DIASAK-1-SAK` Will Rei Sakamoto win set 1 in the Gabriel Diallo vs Rei Sakamoto match: 0.55/0.60 mid 57.5%, model 46.4% (projection_v2.0 (prediction ledger)) -- gap -11.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18DIASAK-2-DIA` Will Gabriel Diallo win set 2 in the Gabriel Diallo vs Rei Sakamoto match: 0.40/0.45 mid 42.5%, model 53.6% (projection_v2.0 (prediction ledger)) -- gap +11.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18DIASAK-29` Over 28.5 games: 0.02/0.99 mid 50.5%, model 42.1% (projection_v2.0 (prediction ledger)) -- gap -8.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18DIASAK-2-SAK` Will Rei Sakamoto win set 2 in the Gabriel Diallo vs Rei Sakamoto match: 0.48/0.60 mid 54.0%, model 46.4% (projection_v2.0 (prediction ledger)) -- gap -7.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18DIASAK-24` Over 23.5 games: 0.12/0.98 mid 55.0%, model 58.4% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18DIASAK-SAK21` Will Rei Sakamoto win the Gabriel Diallo vs Rei Sakamoto match by a set score of 2-1?: 0.05/0.43 mid 24.0%, model 23.1% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Adam Walton vs Nikoloz Basilashvili -- ATP Almaty Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-18 06:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-18 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105932:200443:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikoloz Basilashvili (`KXATPMATCH-26OCT18WALBAS-BAS`) | 0.51 / 0.55 (499) | 53.0% | 35.8% | 39.3% | 39.8% [36.9%-45.1%] | -- | 53.2% | -- | INSUFFICIENT_INPUTS | PASS | -17.2 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Adam Walton (`KXATPMATCH-26OCT18WALBAS-WAL`) | 0.45 / 0.50 (6995) | 47.5% | 64.2% | 60.7% | 60.2% [54.9%-63.1%] | -- | 46.8% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +16.7 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5302.0, B 3285.0; serve-point win A 66.3%, B 36.6%; Elo A 1742.6, B 1683.6; model uncertainty 0.0407
* Form inputs: days since last match A 0, B 0; matches on record A 348, B 911; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18WALBAS-WAL  (YES = Adam Walton)
Model: 64%
Kalshi: 48%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.028, surface_dev_loose -0.010, surface_dev_tight +0.015
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT18WALBAS-BAS20` Will Nikoloz Basilashvili win the Adam Walton vs Nikoloz Basilashvili match by a set score of 2-0?: 0.11/0.50 mid 30.5%, model 16.3% (projection_v2.0 (prediction ledger)) -- gap -14.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18WALBAS-2-WAL` Will Adam Walton win set 2 in the Adam Walton vs Nikoloz Basilashvili match: 0.37/0.58 mid 47.5%, model 59.6% (projection_v2.0 (prediction ledger)) -- gap +12.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18WALBAS-1-WAL` Will Adam Walton win set 1 in the Adam Walton vs Nikoloz Basilashvili match: 0.35/0.61 mid 48.0%, model 59.6% (projection_v2.0 (prediction ledger)) -- gap +11.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18WALBAS-WAL20` Will Adam Walton win the Adam Walton vs Nikoloz Basilashvili match by a set score of 2-0?: 0.05/0.44 mid 24.5%, model 35.5% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18WALBAS-2-BAS` Will Nikoloz Basilashvili win set 2 in the Adam Walton vs Nikoloz Basilashvili match: 0.42/0.58 mid 50.0%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap -9.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18WALBAS-WAL21` Will Adam Walton win the Adam Walton vs Nikoloz Basilashvili match by a set score of 2-1?: 0.02/0.41 mid 21.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT18WALBAS-BAS21` Will Nikoloz Basilashvili win the Adam Walton vs Nikoloz Basilashvili match by a set score of 2-1?: 0.04/0.43 mid 23.5%, model 19.4% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18WALBAS-1-BAS` Will Nikoloz Basilashvili win set 1 in the Adam Walton vs Nikoloz Basilashvili match: 0.29/0.59 mid 44.0%, model 40.4% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Han Shi vs Alina Korneeva -- WTA Ningbo Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-18 08:20Z
* Current expected start: 2026-10-18 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: 2026-10-18 05:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-18T08:20:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:222559:252499:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Korneeva (`KXWTAMATCH-26OCT18SHIKOR-KOR`) | 0.74 / 0.78 (2210) | 76.0% | 85.2% | 76.0% | 79.6% [78.0%-82.8%] | -- | 76.3% | -- | INSUFFICIENT_INPUTS | PASS | +9.2 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Han Shi (`KXWTAMATCH-26OCT18SHIKOR-SHI`) | 0.23 / 0.26 (7045) | 24.5% | 14.8% | 24.0% | 20.4% [17.2%-22.0%] | -- | 23.9% | -- | INSUFFICIENT_INPUTS | PASS | -9.7 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3226.0, B 3297.0; serve-point win A 50.3%, B 41.8%; Elo A 1600.6, B 1915.0; model uncertainty 0.0237
* Form inputs: days since last match A 173, B 21; matches on record A 228, B 191; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose +0.004, surface_dev_tight -0.004
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT18SHIKOR-1-KOR` Will Alina Korneeva win set 1 in the Han Shi vs Alina Korneeva match: 0.67/0.74 mid 70.5%, model 75.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18SHIKOR-2-KOR` Will Alina Korneeva win set 2 in the Han Shi vs Alina Korneeva match: 0.67/0.88 mid 77.5%, model 75.8% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18SHIKOR-1-SHI` Will Han Shi win set 1 in the Han Shi vs Alina Korneeva match: 0.20/0.31 mid 25.5%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap -1.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT18SHIKOR-2-SHI` Will Han Shi win set 2 in the Han Shi vs Alina Korneeva match: 0.12/0.35 mid 23.5%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Nao Nishino (`KXITFWMATCH-26OCT17NISPEN-NIS`) | 0.26 / 0.30 (27) | 28.0% | 26.4% | 23.2% | 32.6% [28.8%-36.4%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Annika Penickova (`KXITFWMATCH-26OCT17NISPEN-PEN`) | 0.68 / 0.74 (146) | 71.0% | 73.6% | 76.8% | 67.4% [63.6%-71.2%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 295.0, B 702.0; serve-point win A 52.9%, B 42.4%; Elo A 1367.9, B 1478.8; model uncertainty 0.0378
* Form inputs: days since last match A 446, B 53; matches on record A 12, B 38; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.005, surface_dev_loose -0.009, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

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
| Martin Borisiouk (`KXITFMATCH-26OCT17BORDEL-BOR`) | 0.36 / 0.37 (4) | 36.5% | 42.1% | 65.5% | 39.2% [33.5%-45.6%] | 38.5% | -- | 38.5% | MARKETS_AGREE | WATCH | +5.7 pp | NORMAL | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Matthew Dellavedova (`KXITFMATCH-26OCT17BORDEL-DEL`) | 0.60 / 0.65 (15) | 62.5% | 57.9% | 34.5% | 60.8% [54.4%-66.5%] | 61.5% | -- | 61.5% | MODEL_LONE_OUTLIER | PASS | -4.7 pp | NORMAL | AGING | C / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 345.0, B 1203.0; serve-point win A 63.4%, B 35.0%; Elo A 1337.8, B 1461.1; model uncertainty 0.0604
* Form inputs: days since last match A 33, B 25; matches on record A 80, B 356; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.015, surface_dev_loose +0.001, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria KHOMUTSIANSKAYA vs Sijia Wei -- W15 Shenzhen F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-18T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221096:222944:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria KHOMUTSIANSKAYA (`KXITFWMATCH-26OCT17KHOWEI-KHO`) | 0.43 / 0.51 (26) | 47.0% | 52.3% | 92.9% | 78.6% [60.0%-85.5%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.3 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sijia Wei (`KXITFWMATCH-26OCT17KHOWEI-WEI`) | 0.49 / 0.53 (47) | 51.0% | 47.7% | 7.1% | 21.3% [14.5%-40.0%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.3 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3178.0, B 2150.0; serve-point win A 56.4%, B 44.1%; Elo A 1665.8, B 1716.7; model uncertainty 0.1275
* Form inputs: days since last match A 271, B 12; matches on record A 171, B 308; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.022, surface_pool_high -0.020, surface_dev_loose +0.007, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; WIDE_SPREAD
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
| Ma / Passola (`KXITFWDOUBLES-26OCT17MAXPASRENSHO-MAXPAS`) | 0.08 / 0.54 (54) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rencheli / Sholokhova (`KXITFWDOUBLES-26OCT17MAXPASRENSHO-RENSHO`) | 0.08 / 0.70 (83) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Terence Atmane vs Rinky Hijikata -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208014:209279:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Terence Atmane (`KXATPMATCH-26OCT18ATMHIJ-ATM`) | 0.06 / 0.94 (222) | 50.0% | 47.1% | 54.9% | 52.9% [48.5%-54.4%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rinky Hijikata (`KXATPMATCH-26OCT18ATMHIJ-HIJ`) | 0.06 / 0.94 (200) | 50.0% | 52.8% | 45.1% | 47.1% [45.6%-51.5%] | -- | -- | -- | -- | PASS | +2.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4446.0, B 5282.0; serve-point win A 65.7%, B 33.7%; Elo A 1764.1, B 1794.6; model uncertainty 0.0292
* Form inputs: days since last match A 12, B 10; matches on record A 397, B 434; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.010
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18ATMHIJ-1-HIJ` Will Rinky Hijikata win set 1 in the Terence Atmane vs Rinky Hijikata match: 0.01/0.96 mid 48.5%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ATMHIJ-2-HIJ` Will Rinky Hijikata win set 2 in the Terence Atmane vs Rinky Hijikata match: 0.05/0.96 mid 50.5%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ATMHIJ-2-ATM` Will Terence Atmane win set 2 in the Terence Atmane vs Rinky Hijikata match: 0.01/0.93 mid 47.0%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18ATMHIJ-1-ATM` Will Terence Atmane win set 1 in the Terence Atmane vs Rinky Hijikata match: 0.01/0.96 mid 48.5%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## N. Sriram Balaji / Evan King vs Anirudh Chandrasekar / Ray Ho -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18BALKINCHARAY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N. Sriram Balaji / Evan King (`KXATPDOUBLES-26OCT18BALKINCHARAY-BALKIN`) | 0.05 / 0.95 (137) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anirudh Chandrasekar / Ray Ho (`KXATPDOUBLES-26OCT18BALKINCHARAY-CHARAY`) | 0.05 / 0.95 (137) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144869:208233:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mattia Bellucci (`KXATPMATCH-26OCT18BELETC-BEL`) | 0.06 / 0.94 (222) | 50.0% | 57.8% | 48.5% | 50.0% [49.5%-51.5%] | -- | -- | -- | -- | PASS | +7.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tomas Martin Etcheverry (`KXATPMATCH-26OCT18BELETC-ETC`) | 0.06 / 0.94 (200) | 50.0% | 42.2% | 51.4% | 50.0% [48.5%-50.5%] | -- | -- | -- | -- | PASS | -7.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4439.0, B 5437.0; serve-point win A 67.4%, B 34.3%; Elo A 1795.9, B 1757.3; model uncertainty 0.0097
* Form inputs: days since last match A 10, B 7; matches on record A 394, B 635; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18BELETC-1-BEL` Will Mattia Bellucci win set 1 in the Mattia Bellucci vs Tomas Martin Etcheverry match: 0.01/0.93 mid 47.0%, model 55.2% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BELETC-2-BEL` Will Mattia Bellucci win set 2 in the Mattia Bellucci vs Tomas Martin Etcheverry match: 0.01/0.96 mid 48.5%, model 55.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BELETC-1-ETC` Will Tomas Martin Etcheverry win set 1 in the Mattia Bellucci vs Tomas Martin Etcheverry match: 0.05/0.96 mid 50.5%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap -5.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18BELETC-2-ETC` Will Tomas Martin Etcheverry win set 2 in the Mattia Bellucci vs Tomas Martin Etcheverry match: 0.01/0.96 mid 48.5%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Luciano Darderi / Tomas Martin Etcheverry vs Jason Kubler / John Peers -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18DARETCKUBPEE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciano Darderi / Tomas Martin Etcheverry (`KXATPDOUBLES-26OCT18DARETCKUBPEE-DARETC`) | 0.05 / 0.95 (137) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jason Kubler / John Peers (`KXATPDOUBLES-26OCT18DARETCKUBPEE-KUBPEE`) | 0.05 / 0.95 (137) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18DONPIEREYSAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Donski / Filip Pieczonka (`KXATPDOUBLES-26OCT18DONPIEREYSAN-DONPIE`) | 0.05 / 0.95 (137) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arthur Reymond / Luca Sanchez (`KXATPDOUBLES-26OCT18DONPIEREYSAN-REYSAN`) | 0.05 / 0.95 (137) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18GILVERBHASEG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuki Bhambri / Ryan Seggerman (`KXATPDOUBLES-26OCT18GILVERBHASEG-BHASEG`) | 0.05 / 0.95 (137) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sander Gille / Sem Verbeek (`KXATPDOUBLES-26OCT18GILVERBHASEG-GILVER`) | 0.05 / 0.95 (137) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18HIJWALBUBNUR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Bublik / Zangar Nurlanuly (`KXATPDOUBLES-26OCT18HIJWALBUBNUR-BUBNUR`) | 0.05 / 0.95 (137) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rinky Hijikata / Adam Walton (`KXATPDOUBLES-26OCT18HIJWALBUBNUR-HIJWAL`) | 0.05 / 0.95 (137) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105902:200175:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Duckworth (`KXATPMATCH-26OCT18KECDUC-DUC`) | 0.06 / 0.94 (222) | 50.0% | 37.7% | 45.6% | 45.1% [45.1%-45.6%] | -- | -- | -- | -- | PASS | -12.3 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Miomir Kecmanovic (`KXATPMATCH-26OCT18KECDUC-KEC`) | 0.08 / 0.94 (200) | 51.0% | 62.3% | 54.4% | 54.9% [54.4%-54.9%] | -- | -- | -- | -- | PASS | +11.3 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5396.0, B 5242.0; serve-point win A 67.4%, B 35.1%; Elo A 1788.4, B 1745.5; model uncertainty 0.0025
* Form inputs: days since last match A 10, B 9; matches on record A 606, B 896; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.000
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18KECDUC-2-KEC` Will Miomir Kecmanovic win set 2 in the Miomir Kecmanovic vs James Duckworth match: 0.01/0.96 mid 48.5%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18KECDUC-1-KEC` Will Miomir Kecmanovic win set 1 in the Miomir Kecmanovic vs James Duckworth match: 0.05/0.93 mid 49.0%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18KECDUC-1-DUC` Will James Duckworth win set 1 in the Miomir Kecmanovic vs James Duckworth match: 0.05/0.93 mid 49.0%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap -7.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18KECDUC-2-DUC` Will James Duckworth win set 2 in the Miomir Kecmanovic vs James Duckworth match: 0.01/0.96 mid 48.5%, model 41.7% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nathaniel Lammons / Jackson Withrow vs Jakob Schnaitter / Mark Wallner -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18LAMWITSCHWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nathaniel Lammons / Jackson Withrow (`KXATPDOUBLES-26OCT18LAMWITSCHWAL-LAMWIT`) | 0.05 / 0.95 (137) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jakob Schnaitter / Mark Wallner (`KXATPDOUBLES-26OCT18LAMWITSCHWAL-SCHWAL`) | 0.05 / 0.95 (137) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105173:126846:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Mannarino (`KXATPMATCH-26OCT18MANVUK-MAN`) | 0.06 / 0.94 (222) | 50.0% | 48.8% | 57.3% | 56.3% [55.9%-57.3%] | -- | -- | -- | -- | PASS | -1.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aleksandar Vukic (`KXATPMATCH-26OCT18MANVUK-VUK`) | 0.06 / 0.94 (200) | 50.0% | 51.2% | 42.7% | 43.7% [42.7%-44.1%] | -- | -- | -- | -- | PASS | +1.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4276.0, B 4441.0; serve-point win A 65.8%, B 33.9%; Elo A 1772.8, B 1736.9; model uncertainty 0.0071
* Form inputs: days since last match A 6, B 11; matches on record A 1273, B 591; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18MANVUK-1-VUK` Will Aleksandar Vukic win set 1 in the Adrian Mannarino vs Aleksandar Vukic match: 0.01/0.96 mid 48.5%, model 50.8% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MANVUK-2-VUK` Will Aleksandar Vukic win set 2 in the Adrian Mannarino vs Aleksandar Vukic match: 0.01/0.96 mid 48.5%, model 50.8% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MANVUK-1-MAN` Will Adrian Mannarino win set 1 in the Adrian Mannarino vs Aleksandar Vukic match: 0.01/0.96 mid 48.5%, model 49.2% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MANVUK-2-MAN` Will Adrian Mannarino win set 2 in the Adrian Mannarino vs Aleksandar Vukic match: 0.01/0.96 mid 48.5%, model 49.2% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fabian Marozsan vs Timofey Skatov -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206681:207608:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fabian Marozsan (`KXATPMATCH-26OCT18MARSKA-MAR`) | 0.06 / 0.94 (222) | 50.0% | 73.8% | 70.9% | 72.6% [71.7%-73.8%] | -- | -- | -- | -- | PASS | +23.8 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Timofey Skatov (`KXATPMATCH-26OCT18MARSKA-SKA`) | 0.06 / 0.94 (200) | 50.0% | 26.2% | 29.1% | 27.4% [26.2%-28.3%] | -- | -- | -- | -- | PASS | -23.8 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4574.0, B 4414.0; serve-point win A 66.3%, B 38.8%; Elo A 1778.2, B 1562.5; model uncertainty 0.0103
* Form inputs: days since last match A 9, B 11; matches on record A 439, B 455; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18MARSKA-MAR  (YES = Fabian Marozsan)
Model: 74%
Kalshi: 50%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: WIDE_SPREAD, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.004, surface_dev_loose +0.012, surface_dev_tight -0.008
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18MARSKA-1-MAR` Will Fabian Marozsan win set 1 in the Fabian Marozsan vs Timofey Skatov match: 0.01/0.96 mid 48.5%, model 66.5% (projection_v2.0 (prediction ledger)) -- gap +18.0 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MARSKA-2-MAR` Will Fabian Marozsan win set 2 in the Fabian Marozsan vs Timofey Skatov match: 0.01/0.96 mid 48.5%, model 66.5% (projection_v2.0 (prediction ledger)) -- gap +18.0 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MARSKA-1-SKA` Will Timofey Skatov win set 1 in the Fabian Marozsan vs Timofey Skatov match: 0.01/0.96 mid 48.5%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap -15.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18MARSKA-2-SKA` Will Timofey Skatov win set 2 in the Fabian Marozsan vs Timofey Skatov match: 0.01/0.96 mid 48.5%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap -15.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
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
| Francisco Cabral / James Tracy (`KXATPDOUBLES-26OCT18MIEOBECABTRA-CABTRA`) | 0.45 / 0.48 (188) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26OCT18MIEOBECABTRA-MIEOBE`) | 0.50 / 0.55 (3975) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18MIEOBEOMAZHU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26OCT18MIEOBEOMAZHU-MIEOBE`) | 0.05 / 0.95 (137) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Amir Omarkhanov / Beibit Zhukayev (`KXATPDOUBLES-26OCT18MIEOBEOMAZHU-OMAZHU`) | 0.05 / 0.95 (137) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207830:tml:N0GN:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Machac (`KXATPMATCH-26OCT18NURMAC-MAC`) | 0.06 / 0.94 (222) | 50.0% | 98.2% | 88.3% | 96.2% [94.8%-97.6%] | -- | -- | -- | -- | PASS | +48.1 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zangar Nurlanuly (`KXATPMATCH-26OCT18NURMAC-NUR`) | 0.06 / 0.94 (200) | 50.0% | 1.8% | 11.7% | 3.8% [2.4%-5.2%] | -- | -- | -- | -- | PASS | -48.1 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 195.0, B 3439.0; serve-point win A 54.0%, B 29.4%; Elo A 1329.8, B 1926.2; model uncertainty 0.014
* Form inputs: days since last match A 68, B 8; matches on record A 4, B 440; data quality D

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18NURMAC-MAC  (YES = Tomas Machac)
Model: 98%
Kalshi: 50%
Gap: +48 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.014, surface_dev_loose +0.000, surface_dev_tight -0.001
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18NURMAC-1-MAC` Will Tomas Machac win set 1 in the Zangar Nurlanuly vs Tomas Machac match: 0.01/0.96 mid 48.5%, model 91.9% (projection_v2.0 (prediction ledger)) -- gap +43.4 pp, EXTREME, DATA_WARNING, quote AGING, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18NURMAC-2-MAC` Will Tomas Machac win set 2 in the Zangar Nurlanuly vs Tomas Machac match: 0.01/0.96 mid 48.5%, model 91.9% (projection_v2.0 (prediction ledger)) -- gap +43.4 pp, EXTREME, DATA_WARNING, quote AGING, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18NURMAC-1-NUR` Will Zangar Nurlanuly win set 1 in the Zangar Nurlanuly vs Tomas Machac match: 0.01/0.96 mid 48.5%, model 8.1% (projection_v2.0 (prediction ledger)) -- gap -40.4 pp, EXTREME, DATA_WARNING, quote AGING, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT18NURMAC-2-NUR` Will Zangar Nurlanuly win set 2 in the Zangar Nurlanuly vs Tomas Machac match: 0.01/0.96 mid 48.5%, model 8.1% (projection_v2.0 (prediction ledger)) -- gap -40.4 pp, EXTREME, DATA_WARNING, quote AGING, identity AMBIGUOUS, data POOR
* Warnings: BET_BLOCKED_START_STATUS; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jean-Julien Rojer / Theodore Winegar vs Facundo Diaz Acosta / Thiago Agustin Tirante -- ATP Almaty R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-18T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT18ROJWINDIATIR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Facundo Diaz Acosta / Thiago Agustin Tirante (`KXATPDOUBLES-26OCT18ROJWINDIATIR-DIATIR`) | 0.05 / 0.95 (137) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jean-Julien Rojer / Theodore Winegar (`KXATPDOUBLES-26OCT18ROJWINDIATIR-ROJWIN`) | 0.05 / 0.95 (137) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:202058:207680:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Facundo Diaz Acosta (`KXATPMATCH-26OCT18TIRDIA-DIA`) | 0.06 / 0.94 (222) | 50.0% | 39.5% | 46.5% | 43.6% [39.2%-45.5%] | -- | -- | -- | -- | PASS | -10.5 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thiago Agustin Tirante (`KXATPMATCH-26OCT18TIRDIA-TIR`) | 0.06 / 0.94 (200) | 50.0% | 60.5% | 53.5% | 56.4% [54.5%-60.8%] | -- | -- | -- | -- | PASS | +10.5 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4745.0, B 5003.0; serve-point win A 65.1%, B 37.0%; Elo A 1741.7, B 1628.9; model uncertainty 0.0317
* Form inputs: days since last match A 7, B 9; matches on record A 449, B 449; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose +0.029, surface_dev_tight -0.020
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18TIRDIA-1-TIR` Will Thiago Agustin Tirante win set 1 in the Thiago Agustin Tirante vs Facundo Diaz Acosta match: 0.01/0.96 mid 48.5%, model 57.1% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TIRDIA-2-TIR` Will Thiago Agustin Tirante win set 2 in the Thiago Agustin Tirante vs Facundo Diaz Acosta match: 0.01/0.96 mid 48.5%, model 57.1% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TIRDIA-1-DIA` Will Facundo Diaz Acosta win set 1 in the Thiago Agustin Tirante vs Facundo Diaz Acosta match: 0.01/0.96 mid 48.5%, model 42.9% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TIRDIA-2-DIA` Will Facundo Diaz Acosta win set 2 in the Thiago Agustin Tirante vs Facundo Diaz Acosta match: 0.01/0.96 mid 48.5%, model 42.9% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Stefanos Tsitsipas vs Aleksandar Kovacevic -- ATP Almaty R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-17 10:39Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-19T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126774:206499:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksandar Kovacevic (`KXATPMATCH-26OCT18TSIKOV-KOV`) | 0.08 / 0.94 (200) | 51.0% | 27.0% | 32.6% | 30.5% [23.5%-35.1%] | -- | -- | -- | -- | PASS | -24.0 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefanos Tsitsipas (`KXATPMATCH-26OCT18TSIKOV-TSI`) | 0.06 / 0.94 (200) | 50.0% | 73.0% | 67.4% | 69.5% [64.9%-76.5%] | -- | -- | -- | -- | PASS | +23.0 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5084.0, B 4809.0; serve-point win A 73.1%, B 32.2%; Elo A 1952.1, B 1756.9; model uncertainty 0.0581
* Form inputs: days since last match A 3, B 10; matches on record A 801, B 399; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18TSIKOV-TSI  (YES = Stefanos Tsitsipas)
Model: 73%
Kalshi: 50%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: WIDE_SPREAD, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.039, surface_pool_high -0.046, surface_dev_loose -0.008, surface_dev_tight +0.013
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT18TSIKOV-1-TSI` Will Stefanos Tsitsipas win set 1 in the Stefanos Tsitsipas vs Aleksandar Kovacevic match: 0.01/0.96 mid 48.5%, model 65.9% (projection_v2.0 (prediction ledger)) -- gap +17.4 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TSIKOV-2-TSI` Will Stefanos Tsitsipas win set 2 in the Stefanos Tsitsipas vs Aleksandar Kovacevic match: 0.01/0.96 mid 48.5%, model 65.9% (projection_v2.0 (prediction ledger)) -- gap +17.4 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TSIKOV-1-KOV` Will Aleksandar Kovacevic win set 1 in the Stefanos Tsitsipas vs Aleksandar Kovacevic match: 0.01/0.96 mid 48.5%, model 34.1% (projection_v2.0 (prediction ledger)) -- gap -14.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18TSIKOV-2-KOV` Will Aleksandar Kovacevic win set 2 in the Stefanos Tsitsipas vs Aleksandar Kovacevic match: 0.01/0.96 mid 48.5%, model 34.1% (projection_v2.0 (prediction ledger)) -- gap -14.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jacob Fearnley vs Hugo Gaston -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200384:207985:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacob Fearnley (`KXATPMATCH-26OCT18FEAGAS-FEA`) | 0.67 / 0.71 (38) | 69.0% | 58.6% | 55.6% | 55.6% [53.6%-57.2%] | 69.1% | 69.9% | 69.1% | MODEL_LONE_OUTLIER | PASS | -10.4 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Hugo Gaston (`KXATPMATCH-26OCT18FEAGAS-GAS`) | 0.28 / 0.33 (6967) | 30.5% | 41.4% | 44.4% | 44.4% [42.8%-46.4%] | 30.9% | 30.4% | 30.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.9 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4058.0, B 4582.0; serve-point win A 61.0%, B 40.6%; Elo A 1773.0, B 1728.8; model uncertainty 0.0179
* Form inputs: days since last match A 19, B 12; matches on record A 178, B 502; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18FEAGAS-18` Over 17.5 games: 0.12/0.99 mid 55.5%, model 90.3% (projection_v2.0 (prediction ledger)) -- gap +34.9 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18FEAGAS-28` Over 27.5 games: 0.01/0.99 mid 50.0%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap -13.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FEAGAS-2-FEA` Will Jacob Fearnley win set 2 in the Jacob Fearnley vs Hugo Gaston match: 0.58/0.79 mid 68.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap -12.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FEAGAS-1-GAS` Will Hugo Gaston win set 1 in the Jacob Fearnley vs Hugo Gaston match: 0.16/0.48 mid 32.0%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FEAGAS-2-GAS` Will Hugo Gaston win set 2 in the Jacob Fearnley vs Hugo Gaston match: 0.19/0.46 mid 32.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18FEAGAS-23` Over 22.5 games: 0.02/0.98 mid 50.0%, model 57.7% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18FEAGAS-1-FEA` Will Jacob Fearnley win set 1 in the Jacob Fearnley vs Hugo Gaston match: 0.33/0.80 mid 56.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tallon Griekspoor vs Max Schoenhaus -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:134868:212268:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tallon Griekspoor (`KXATPMATCH-26OCT18GRISCH-GRI`) | 0.75 / 0.78 (3) | 76.5% | 80.0% | 72.1% | 83.3% [77.7%-89.4%] | 77.5% | 78.8% | -- | INSUFFICIENT_INPUTS | WATCH | +3.5 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Schoenhaus (`KXATPMATCH-26OCT18GRISCH-SCH`) | 0.20 / 0.27 (93) | 23.5% | 20.0% | 27.9% | 16.7% [10.6%-22.3%] | 22.5% | 21.0% | -- | INSUFFICIENT_INPUTS | PASS | -3.5 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4445.0, B 1578.0; serve-point win A 71.4%, B 35.6%; Elo A 1871.5, B 1465.9; model uncertainty 0.0584
* Form inputs: days since last match A 9, B 33; matches on record A 677, B 52; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.028, surface_dev_loose +0.002, surface_dev_tight -0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18GRISCH-18` Over 17.5 games: 0.01/0.99 mid 50.0%, model 93.6% (projection_v2.0 (prediction ledger)) -- gap +43.6 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18GRISCH-2-GRI` Will Tallon Griekspoor win set 2 in the Tallon Griekspoor vs Max Schoenhaus match: 0.23/0.73 mid 48.0%, model 71.3% (projection_v2.0 (prediction ledger)) -- gap +23.3 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18GRISCH-1-GRI` Will Tallon Griekspoor win set 1 in the Tallon Griekspoor vs Max Schoenhaus match: 0.25/0.73 mid 49.0%, model 71.3% (projection_v2.0 (prediction ledger)) -- gap +22.3 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18GRISCH-28` Over 27.5 games: 0.01/0.99 mid 50.0%, model 36.2% (projection_v2.0 (prediction ledger)) -- gap -13.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18GRISCH-23` Over 22.5 games: 0.02/0.98 mid 50.0%, model 56.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18GRISCH-2-SCH` Will Max Schoenhaus win set 2 in the Tallon Griekspoor vs Max Schoenhaus match: 0.09/0.59 mid 34.0%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18GRISCH-1-SCH` Will Max Schoenhaus win set 1 in the Tallon Griekspoor vs Max Schoenhaus match: 0.08/0.45 mid 26.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mariano Navone vs Juan Manuel Cerundolo -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207678:208363:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel Cerundolo (`KXATPMATCH-26OCT18NAVCER-CER`) | 0.39 / 0.44 (18) | 41.5% | 46.6% | 36.5% | 40.4% [38.9%-42.9%] | 40.6% | 39.1% | 40.6% | MODEL_LONE_OUTLIER | PASS | +5.1 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Mariano Navone (`KXATPMATCH-26OCT18NAVCER-NAV`) | 0.56 / 0.61 (10) | 58.5% | 53.4% | 63.5% | 59.6% [57.1%-61.1%] | 59.4% | 60.9% | 59.4% | MODEL_LONE_OUTLIER | PASS | -5.1 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5176.0, B 5332.0; serve-point win A 61.9%, B 38.8%; Elo A 1725.4, B 1754.7; model uncertainty 0.0199
* Form inputs: days since last match A 9, B 7; matches on record A 410, B 506; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose -0.001, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18NAVCER-18` Over 17.5 games: 0.01/0.99 mid 50.0%, model 91.8% (projection_v2.0 (prediction ledger)) -- gap +41.8 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18NAVCER-28` Over 27.5 games: 0.01/0.99 mid 50.0%, model 38.7% (projection_v2.0 (prediction ledger)) -- gap -11.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18NAVCER-2-CER` Will Juan Manuel Cerundolo win set 2 in the Mariano Navone vs Juan Manuel Cerundolo match: 0.08/0.65 mid 36.5%, model 47.7% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18NAVCER-1-CER` Will Juan Manuel Cerundolo win set 1 in the Mariano Navone vs Juan Manuel Cerundolo match: 0.16/0.65 mid 40.5%, model 47.7% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18NAVCER-23` Over 22.5 games: 0.12/0.98 mid 55.0%, model 59.3% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18NAVCER-1-NAV` Will Mariano Navone win set 1 in the Mariano Navone vs Juan Manuel Cerundolo match: 0.35/0.78 mid 56.5%, model 52.3% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18NAVCER-2-NAV` Will Mariano Navone win set 2 in the Mariano Navone vs Juan Manuel Cerundolo match: 0.31/0.82 mid 56.5%, model 52.3% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dino Prizmic vs Damir Dzumhur -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106000:209976:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Damir Dzumhur (`KXATPMATCH-26OCT18PRIDZU-DZU`) | 0.27 / 0.34 (7) | 30.5% | 23.2% | 30.3% | 29.4% [28.5%-31.2%] | 30.9% | 30.3% | 30.9% | MARKETS_AGREE | PASS | -7.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Dino Prizmic (`KXATPMATCH-26OCT18PRIDZU-PRI`) | 0.67 / 0.68 (2) | 67.5% | 76.8% | 69.7% | 70.6% [68.8%-71.5%] | 69.1% | 69.9% | 69.1% | MARKETS_AGREE | PASS | +9.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3904.0, B 4752.0; serve-point win A 63.0%, B 42.6%; Elo A 1827.6, B 1664.3; model uncertainty 0.0138
* Form inputs: days since last match A 26, B 12; matches on record A 223, B 1058; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18PRIDZU-18` Over 17.5 games: 0.01/0.99 mid 50.0%, model 86.0% (projection_v2.0 (prediction ledger)) -- gap +36.0 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18PRIDZU-28` Over 27.5 games: 0.01/0.99 mid 50.0%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap -18.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18PRIDZU-1-PRI` Will Dino Prizmic win set 1 in the Dino Prizmic vs Damir Dzumhur match: 0.30/0.78 mid 54.0%, model 68.8% (projection_v2.0 (prediction ledger)) -- gap +14.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18PRIDZU-1-DZU` Will Damir Dzumhur win set 1 in the Dino Prizmic vs Damir Dzumhur match: 0.26/0.62 mid 44.0%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap -12.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18PRIDZU-2-PRI` Will Dino Prizmic win set 2 in the Dino Prizmic vs Damir Dzumhur match: 0.39/0.87 mid 63.0%, model 68.8% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18PRIDZU-2-DZU` Will Damir Dzumhur win set 2 in the Dino Prizmic vs Damir Dzumhur match: 0.14/0.59 mid 36.5%, model 31.2% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18PRIDZU-23` Over 22.5 games: 0.02/0.98 mid 50.0%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Holger Rune vs Raphael Collignon -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208029:209920:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raphael Collignon (`KXATPMATCH-26OCT18RUNCOL-COL`) | 0.45 / 0.50 (6429) | 47.5% | 38.0% | 42.7% | 38.0% [35.6%-39.8%] | 47.8% | 47.6% | 47.8% | MODEL_LONE_OUTLIER | PASS | -9.5 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Holger Rune (`KXATPMATCH-26OCT18RUNCOL-RUN`) | 0.50 / 0.55 (6809) | 52.5% | 62.0% | 57.3% | 62.0% [60.2%-64.4%] | 52.2% | 53.9% | 52.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +9.5 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2551.0, B 5214.0; serve-point win A 67.0%, B 35.5%; Elo A 1972.9, B 1825.6; model uncertainty 0.021
* Form inputs: days since last match A 10, B 47; matches on record A 430, B 351; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.009, surface_dev_loose +0.004, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18RUNCOL-20` Over 19.5 games: 0.12/0.98 mid 55.0%, model 82.9% (projection_v2.0 (prediction ledger)) -- gap +27.9 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18RUNCOL-30` Over 29.5 games: 0.01/0.98 mid 49.5%, model 33.2% (projection_v2.0 (prediction ledger)) -- gap -16.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18RUNCOL-1-RUN` Will Holger Rune win set 1 in the Holger Rune vs Raphael Collignon match: 0.13/0.77 mid 45.0%, model 58.1% (projection_v2.0 (prediction ledger)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18RUNCOL-1-COL` Will Raphael Collignon win set 1 in the Holger Rune vs Raphael Collignon match: 0.20/0.72 mid 46.0%, model 41.9% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18RUNCOL-25` Over 24.5 games: 0.02/0.98 mid 50.0%, model 53.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18RUNCOL-2-COL` Will Raphael Collignon win set 2 in the Holger Rune vs Raphael Collignon match: 0.13/0.72 mid 42.5%, model 41.9% (projection_v2.0 (prediction ledger)) -- gap -0.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18RUNCOL-2-RUN` Will Holger Rune win set 2 in the Holger Rune vs Raphael Collignon match: 0.26/0.91 mid 58.5%, model 58.1% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Toby Samuel vs Zizou Bergs -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200267:210389:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zizou Bergs (`KXATPMATCH-26OCT18SAMBER-BER`) | 0.65 / 0.67 (6) | 66.0% | 46.0% | 28.0% | 36.1% [30.6%-44.0%] | 62.3% | 68.3% | 68.3% | ALL_THREE_DISAGREE | PASS | -20.0 pp | HIGH_REVIEW | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Toby Samuel (`KXATPMATCH-26OCT18SAMBER-SAM`) | 0.34 / 0.38 (10) | 36.0% | 54.0% | 72.0% | 63.8% [56.0%-69.4%] | 37.7% | 62.5% | -- | INSUFFICIENT_INPUTS | PASS | +18.0 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2684.0, B 5362.0; serve-point win A 62.9%, B 37.9%; Elo A 1804.6, B 1810.8; model uncertainty 0.0666
* Form inputs: days since last match A 19, B 3; matches on record A 136, B 552; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT18SAMBER-SAM  (YES = Toby Samuel)
Model: 54%
Kalshi: 36%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.019, surface_dev_loose +0.042, surface_dev_tight -0.029
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18SAMBER-31` Over 30.5 games: 0.01/0.98 mid 49.5%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap -25.3 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18SAMBER-21` Over 20.5 games: 0.01/0.98 mid 49.5%, model 72.8% (projection_v2.0 (prediction ledger)) -- gap +23.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAMBER-2-SAM` Will Toby Samuel win set 2 in the Toby Samuel vs Zizou Bergs match: 0.10/0.63 mid 36.5%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +16.1 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAMBER-1-SAM` Will Toby Samuel win set 1 in the Toby Samuel vs Zizou Bergs match: 0.16/0.59 mid 37.5%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +15.2 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAMBER-2-BER` Will Zizou Bergs win set 2 in the Toby Samuel vs Zizou Bergs match: 0.28/0.75 mid 51.5%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18SAMBER-1-BER` Will Zizou Bergs win set 1 in the Toby Samuel vs Zizou Bergs match: 0.25/0.73 mid 49.0%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18SAMBER-26` Over 25.5 games: 0.02/0.98 mid 50.0%, model 48.7% (projection_v2.0 (prediction ledger)) -- gap -1.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jan-Lennard Struff vs Marcos Giron -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105526:106218:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcos Giron (`KXATPMATCH-26OCT18STRGIR-GIR`) | 0.36 / 0.42 (16) | 39.0% | 52.3% | 49.0% | 49.5% [44.2%-53.4%] | 37.7% | 38.2% | 37.7% | EXTERNAL_LONE_OUTLIER | PASS | +13.3 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26OCT18STRGIR-STR`) | 0.56 / 0.65 (9) | 60.5% | 47.7% | 51.0% | 50.5% [46.6%-55.8%] | 62.3% | 61.8% | 62.3% | MARKETS_AGREE | PASS | -12.8 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4788.0, B 4538.0; serve-point win A 66.0%, B 33.6%; Elo A 1780.4, B 1807.1; model uncertainty 0.0462
* Form inputs: days since last match A 7, B 9; matches on record A 1054, B 707; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.039, surface_dev_loose -0.010, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18STRGIR-19` Over 18.5 games: 0.01/0.99 mid 50.0%, model 91.5% (projection_v2.0 (prediction ledger)) -- gap +41.5 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18STRGIR-2-GIR` Will Marcos Giron win set 2 in the Jan-Lennard Struff vs Marcos Giron match: 0.12/0.68 mid 40.0%, model 51.5% (projection_v2.0 (prediction ledger)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18STRGIR-29` Over 28.5 games: 0.01/0.99 mid 50.0%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap -10.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18STRGIR-2-STR` Will Jan-Lennard Struff win set 2 in the Jan-Lennard Struff vs Marcos Giron match: 0.30/0.84 mid 57.0%, model 48.5% (projection_v2.0 (prediction ledger)) -- gap -8.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18STRGIR-24` Over 23.5 games: 0.02/0.98 mid 50.0%, model 56.5% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18STRGIR-1-GIR` Will Marcos Giron win set 1 in the Jan-Lennard Struff vs Marcos Giron match: 0.14/0.78 mid 46.0%, model 51.5% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18STRGIR-1-STR` Will Jan-Lennard Struff win set 1 in the Jan-Lennard Struff vs Marcos Giron match: 0.20/0.75 mid 47.5%, model 48.5% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Botic Van de Zandschulp vs Kamil Majchrzak -- ATP Brussels R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-18 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Hard · scheduled 2026-10-18T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111794:122298:2026-10-18`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kamil Majchrzak (`KXATPMATCH-26OCT18VANMAJ-MAJ`) | 0.37 / 0.42 (252) | 39.5% | 38.0% | 41.0% | 40.0% [39.0%-41.5%] | 40.6% | 40.3% | 40.6% | MODEL_LONE_OUTLIER | PASS | -1.4 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Botic Van de Zandschulp (`KXATPMATCH-26OCT18VANMAJ-VAN`) | 0.58 / 0.63 (6373) | 60.5% | 62.0% | 59.0% | 60.0% [58.5%-61.0%] | 59.4% | 59.8% | 59.4% | MODEL_LONE_OUTLIER | PASS | +1.4 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5172.0, B 4319.0; serve-point win A 63.7%, B 38.7%; Elo A 1902.6, B 1803.8; model uncertainty 0.0123
* Form inputs: days since last match A 3, B 10; matches on record A 618, B 674; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT18VANMAJ-31` Over 30.5 games: 0.01/0.98 mid 49.5%, model 23.4% (projection_v2.0 (prediction ledger)) -- gap -26.1 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT18VANMAJ-21` Over 20.5 games: 0.01/0.98 mid 49.5%, model 71.6% (projection_v2.0 (prediction ledger)) -- gap +22.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18VANMAJ-2-VAN` Will Botic Van de Zandschulp win set 2 in the Botic Van de Zandschulp vs Kamil Majchrzak match: 0.23/0.72 mid 47.5%, model 58.0% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18VANMAJ-1-VAN` Will Botic Van de Zandschulp win set 1 in the Botic Van de Zandschulp vs Kamil Majchrzak match: 0.28/0.80 mid 54.0%, model 58.0% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT18VANMAJ-1-MAJ` Will Kamil Majchrzak win set 1 in the Botic Van de Zandschulp vs Kamil Majchrzak match: 0.10/0.66 mid 38.0%, model 42.0% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT18VANMAJ-26` Over 25.5 games: 0.02/0.98 mid 50.0%, model 47.5% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT18VANMAJ-2-MAJ` Will Kamil Majchrzak win set 2 in the Botic Van de Zandschulp vs Kamil Majchrzak match: 0.14/0.70 mid 42.0%, model 42.0% (projection_v2.0 (prediction ledger)) -- gap -0.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
