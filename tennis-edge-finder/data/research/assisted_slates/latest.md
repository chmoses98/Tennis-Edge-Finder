# ASSISTED SLATE -- 2026-10-24T13:28Z (`SL-20261024T132848Z-72f5077a`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

135 open matches not seen started, 629 markets. Skipped: {"no_play_confirmed": 1, "no_match_winner_listed": 2, "first_ball_already_observed": 3, "scheduled_start_over_24h_past": 1}. Sources: shadow board 2026-10-24T11:50:37.641573+00:00, Model 4 2026-10-24T11:50:49.832882+00:00, Gen-1 ledger 2026-10-24T11:50:32.683364+00:00, external 2026-10-24T13:11:58.439129+00:00, capture 20261024T130901Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-24 13:30Z**
* Recommended RUN TENNIS time: **2026-10-24 12:45Z**  (**OVERDUE -- run now**)
* Final price/status check time: **2026-10-24 13:20Z**
* Number of matches in window: 5 (Aleksandar Kovacevic vs James Duckworth, Francisco Cerundolo vs Tallon Griekspoor, Flavio Cobolli vs Lorenzo Musetti, Remy Bertola vs Jakub Paul, Corentin Moutet vs Tomas Machac)

* **35 main-tour match(es) have NO verified start status** (START_UNKNOWN, STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-10-24T13:28Z. Refresh due by: 2026-10-24 12:45Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 30, "HIGH_REVIEW": 41, "NORMAL": 210, "REVIEW": 50, "UNPRICED": 298}; match winners: {"EXTREME": 17, "HIGH_REVIEW": 24, "NORMAL": 68, "REVIEW": 27, "UNPRICED": 134}; quote freshness at build: {"FRESH": 331}.

## Mahin Qureshi vs Meshkatolzahra Safi -- Billie Jean King Cup Qualifiers UNK

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 10:00Z
* Current expected start: 2026-10-24 10:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-10-24 09:15Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

OTHER (TEAM) · Hard · scheduled 2026-10-24T10:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221823:264229:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mahin Qureshi (`KXWTAMATCH-26OCT24QURSAF-QUR`) | 0.15 / 0.24 (6) | 19.5% | -- | 33.4% | 28.7% [27.0%-31.5%] | -- | -- | -- | -- | PASS | +9.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Meshkatolzahra Safi (`KXWTAMATCH-26OCT24QURSAF-SAF`) | 0.77 / 0.84 (38) | 80.5% | -- | 66.6% | 71.3% [68.5%-73.0%] | -- | -- | -- | -- | PASS | -9.2 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 80.0, B 598.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0226
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.028, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jaime Faria vs Mika Brunold -- ATP Basel Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 10:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-24 09:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:209983:210262:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mika Brunold (`KXATPMATCH-26OCT24FARBRU-BRU`) | 0.78 / 0.79 (47144) | 78.5% | 29.0% | 44.5% | 29.8% [17.4%-34.8%] | -- | 47.7% | 47.7% | MODEL_LONE_OUTLIER | PASS | -49.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Jaime Faria (`KXATPMATCH-26OCT24FARBRU-FAR`) | 0.21 / 0.22 (55819) | 21.5% | 71.0% | 55.5% | 70.2% [65.2%-82.6%] | -- | 52.4% | 52.4% | MODEL_LONE_OUTLIER | PASS | +49.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 4786.0, B 1536.0; serve-point win A 65.1%, B 39.2%; Elo A 1778.3, B 1510.5; model uncertainty 0.0871
* Form inputs: days since last match A 5, B 684; matches on record A 313, B 128; data quality F

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT24FARBRU-FAR  (YES = Jaime Faria)
Model: 71%
Kalshi: 22%
Gap: +49 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, SCHEDULED_START_PASSED, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose -0.018, surface_dev_tight +0.018
* Derivatives listed: 6 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 6 carry a model probability
  * `KXATPEXACTMATCH-26OCT24FARBRU-BRU20` Will Mika Brunold win the Jaime Faria vs Mika Brunold match by a set score of 2-0?: 0.50/0.54 mid 52.0%, model 12.7% (projection_v2.0 (prediction ledger)) -- gap -39.3 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data POOR
  * `KXATPSETWINNER-26OCT24FARBRU-2-BRU` Will Mika Brunold win set 2 in the Jaime Faria vs Mika Brunold match: 0.52/0.53 mid 52.5%, model 35.6% (projection_v2.0 (prediction ledger)) -- gap -16.9 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPSETWINNER-26OCT24FARBRU-2-FAR` Will Jaime Faria win set 2 in the Jaime Faria vs Mika Brunold match: 0.47/0.48 mid 47.5%, model 64.4% (projection_v2.0 (prediction ledger)) -- gap +16.9 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXATPEXACTMATCH-26OCT24FARBRU-BRU21` Will Mika Brunold win the Jaime Faria vs Mika Brunold match by a set score of 2-1?: 0.24/0.26 mid 25.0%, model 16.4% (projection_v2.0 (prediction ledger)) -- gap -8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
  * `KXATPEXACTMATCH-26OCT24FARBRU-FAR21` Will Jaime Faria win the Jaime Faria vs Mika Brunold match by a set score of 2-1?: 0.21/0.23 mid 22.0%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data POOR
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS; ONE_SIDED_OR_NO_QUOTE

## Joel Schwaerzler vs Titouan Droguet -- ATP Vienna Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 13:40Z
* Current expected start: 2026-10-24 11:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-24 10:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Clay · scheduled 2026-10-24T13:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208169:212082:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Titouan Droguet (`KXATPMATCH-26OCT24SCHDRO-DRO`) | 0.58 / 0.59 (41636) | 58.5% | 76.1% | 77.3% | 76.9% [75.8%-78.4%] | -- | 72.8% | 72.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +17.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Joel Schwaerzler (`KXATPMATCH-26OCT24SCHDRO-SCH`) | 0.41 / 0.42 (17999) | 41.5% | 23.9% | 22.7% | 23.1% [21.6%-24.2%] | -- | 26.7% | 26.7% | MODEL_LONE_OUTLIER | PASS | -17.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 3799.0, B 5236.0; serve-point win A 62.7%, B 31.5%; Elo A 1667.4, B 1871.4; model uncertainty 0.013
* Form inputs: days since last match A 19, B 4; matches on record A 178, B 429; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT24SCHDRO-DRO  (YES = Titouan Droguet)
Model: 76%
Kalshi: 58%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_MODEL
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_CONFIRMATION, UNKNOWN
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.011, surface_dev_loose -0.015, surface_dev_tight +0.011
* Derivatives listed: 4 (EXACT_SET_SCORE, MATCH_WINNER); 4 carry a model probability
  * `KXATPEXACTMATCH-26OCT24SCHDRO-SCH21` Will Joel Schwaerzler win the Joel Schwaerzler vs Titouan Droguet match by a set score of 2-1?: 0.41/0.61 mid 51.0%, model 13.8% (projection_v2.0 (prediction ledger)) -- gap -37.2 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24SCHDRO-DRO21` Will Titouan Droguet win the Joel Schwaerzler vs Titouan Droguet match by a set score of 2-1?: 0.34/0.53 mid 43.5%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap -13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Sebastian Baez vs Giovanni Mpetshi Perricard -- ATP Basel Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-24 11:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:202104:208659:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Baez (`KXATPMATCH-26OCT24BAEMPE-BAE`) | 0.04 / 0.05 (6) | 4.5% | 52.0% | 59.3% | 57.5% [56.1%-58.4%] | 41.7% | -- | 41.7% | MODEL_LONE_OUTLIER | WATCH | +47.5 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Giovanni Mpetshi Perricard (`KXATPMATCH-26OCT24BAEMPE-MPE`) | 0.95 / 0.96 (88) | 95.5% | 48.0% | 40.7% | 42.5% [41.6%-43.9%] | 58.3% | -- | 58.3% | MODEL_LONE_OUTLIER | PASS | -47.5 pp | EXTREME (DATA_WARNING) | FRESH | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 4992.0, B 3847.0; serve-point win A 69.2%, B 31.2%; Elo A 1715.5, B 1698.8; model uncertainty 0.0116
* Form inputs: days since last match A 4, B 7; matches on record A 494, B 309; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT24BAEMPE-BAE  (YES = Sebastian Baez)
Model: 52%
Kalshi: 4%
Gap: +48 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, EXTERNAL_MARKET_CONFIRMATION, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.005, surface_dev_tight +0.000
* Derivatives listed: 6 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 6 carry a model probability
  * `KXATPEXACTMATCH-26OCT24BAEMPE-MPE20` Will Giovanni Mpetshi Perricard win the Sebastian Baez vs Giovanni Mpetshi Perricard match by a set score of 2-0?: 0.90/0.92 mid 91.0%, model 23.7% (projection_v2.0 (prediction ledger)) -- gap -67.3 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BAEMPE-2-BAE` Will Sebastian Baez win set 2 in the Sebastian Baez vs Giovanni Mpetshi Perricard match: 0.08/0.10 mid 9.0%, model 51.3% (projection_v2.0 (prediction ledger)) -- gap +42.4 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BAEMPE-2-MPE` Will Giovanni Mpetshi Perricard win set 2 in the Sebastian Baez vs Giovanni Mpetshi Perricard match: 0.88/0.92 mid 90.0%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap -41.4 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BAEMPE-BAE21` Will Sebastian Baez win the Sebastian Baez vs Giovanni Mpetshi Perricard match by a set score of 2-1?: 0.04/0.05 mid 4.5%, model 25.7% (projection_v2.0 (prediction ledger)) -- gap +21.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BAEMPE-MPE21` Will Giovanni Mpetshi Perricard win the Sebastian Baez vs Giovanni Mpetshi Perricard match by a set score of 2-1?: 0.04/0.06 mid 5.0%, model 24.3% (projection_v2.0 (prediction ledger)) -- gap +19.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE

## Alex Molcan vs Hamad Medjedovic -- ATP Vienna Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 14:20Z
* Current expected start: 2026-10-24 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-24 11:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Clay · scheduled 2026-10-24T14:20:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144684:209098:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hamad Medjedovic (`KXATPMATCH-26OCT24MOLMED-MED`) | 0.59 / 0.60 (5149) | 59.5% | 54.8% | 44.4% | 51.0% [48.5%-54.0%] | -- | 58.0% | 58.0% | MODEL_LONE_OUTLIER | PASS | -4.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Alex Molcan (`KXATPMATCH-26OCT24MOLMED-MOL`) | 0.40 / 0.41 (575) | 40.5% | 45.2% | 55.6% | 49.0% [46.0%-51.5%] | -- | 41.9% | 41.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +4.7 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3131.0, B 3309.0; serve-point win A 61.8%, B 37.2%; Elo A 1844.7, B 1931.5; model uncertainty 0.0278
* Form inputs: days since last match A 17, B 4; matches on record A 552, B 310; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose +0.005, surface_dev_tight +0.000
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24MOLMED-MED20` Will Hamad Medjedovic win the Alex Molcan vs Hamad Medjedovic match by a set score of 2-0?: 0.35/0.40 mid 37.5%, model 28.3% (projection_v2.0 (prediction ledger)) -- gap -9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOLMED-MOL21` Will Alex Molcan win the Alex Molcan vs Hamad Medjedovic match by a set score of 2-1?: 0.15/0.20 mid 17.5%, model 23.3% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOLMED-MED21` Will Hamad Medjedovic win the Alex Molcan vs Hamad Medjedovic match by a set score of 2-1?: 0.19/0.24 mid 21.5%, model 26.5% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOLMED-1-MOL` Will Alex Molcan win set 1 in the Alex Molcan vs Hamad Medjedovic match: 0.41/0.45 mid 43.0%, model 46.8% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOLMED-2-MED` Will Hamad Medjedovic win set 2 in the Alex Molcan vs Hamad Medjedovic match: 0.54/0.60 mid 57.0%, model 53.2% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOLMED-2-MOL` Will Alex Molcan win set 2 in the Alex Molcan vs Hamad Medjedovic match: 0.40/0.46 mid 43.0%, model 46.8% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOLMED-1-MED` Will Hamad Medjedovic win set 1 in the Alex Molcan vs Hamad Medjedovic match: 0.54/0.59 mid 56.5%, model 53.2% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOLMED-MOL20` Will Alex Molcan win the Alex Molcan vs Hamad Medjedovic match by a set score of 2-0?: 0.21/0.25 mid 23.0%, model 21.9% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE

## Henry Bernet vs Daniel Altmaier -- ATP Basel Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-24 11:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:127157:148679:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Altmaier (`KXATPMATCH-26OCT24BERALT-ALT`) | 0.55 / 0.56 (5003) | 55.5% | 62.9% | 48.5% | 63.8% [53.9%-76.5%] | -- | 54.5% | 54.5% | MODEL_LONE_OUTLIER | WATCH | +7.4 pp | NORMAL | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Henry Bernet (`KXATPMATCH-26OCT24BERALT-BER`) | 0.44 / 0.46 (10038) | 45.0% | 37.1% | 51.5% | 36.2% [23.5%-46.1%] | -- | 45.5% | 45.5% | MODEL_LONE_OUTLIER | PASS | -7.9 pp | NORMAL | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1360.0, B 5258.0; serve-point win A 64.9%, B 32.4%; Elo A 1515.4, B 1714.1; model uncertainty 0.1134
* Form inputs: days since last match A 12, B 2; matches on record A 34, B 707; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.066, surface_pool_high +0.080, surface_dev_loose +0.019, surface_dev_tight -0.023
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24BERALT-BER20` Will Henry Bernet win the Henry Bernet vs Daniel Altmaier match by a set score of 2-0?: 0.24/0.28 mid 26.0%, model 17.1% (projection_v2.0 (prediction ledger)) -- gap -8.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BERALT-ALT21` Will Daniel Altmaier win the Henry Bernet vs Daniel Altmaier match by a set score of 2-1?: 0.18/0.23 mid 20.5%, model 28.5% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BERALT-1-ALT` Will Daniel Altmaier win set 1 in the Henry Bernet vs Daniel Altmaier match: 0.51/0.56 mid 53.5%, model 58.7% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BERALT-2-ALT` Will Daniel Altmaier win set 2 in the Henry Bernet vs Daniel Altmaier match: 0.51/0.57 mid 54.0%, model 58.7% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BERALT-1-BER` Will Henry Bernet win set 1 in the Henry Bernet vs Daniel Altmaier match: 0.43/0.48 mid 45.5%, model 41.3% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BERALT-2-BER` Will Henry Bernet win set 2 in the Henry Bernet vs Daniel Altmaier match: 0.43/0.48 mid 45.5%, model 41.3% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BERALT-BER21` Will Henry Bernet win the Henry Bernet vs Daniel Altmaier match by a set score of 2-1?: 0.16/0.21 mid 18.5%, model 20.0% (projection_v2.0 (prediction ledger)) -- gap +1.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BERALT-ALT20` Will Daniel Altmaier win the Henry Bernet vs Daniel Altmaier match by a set score of 2-0?: 0.31/0.36 mid 33.5%, model 34.4% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE

## Fabian Marozsan vs Sebastian Sorger -- ATP Vienna Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 14:50Z
* Current expected start: 2026-10-24 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-24 11:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Clay · scheduled 2026-10-24T14:50:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206681:210285:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fabian Marozsan (`KXATPMATCH-26OCT24MARSOR-MAR`) | 0.81 / 0.83 (10565) | 82.0% | 80.8% | 73.1% | 87.1% [82.4%-91.4%] | 80.9% | 82.3% | 81.6% | MODEL_LONE_OUTLIER | WATCH | -1.2 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |
| Sebastian Sorger (`KXATPMATCH-26OCT24MARSOR-SOR`) | 0.17 / 0.19 (5482) | 18.0% | 19.2% | 26.9% | 12.9% [8.6%-17.6%] | 19.1% | 18.1% | 18.6% | MODEL_LONE_OUTLIER | PASS | +1.2 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4525.0, B 572.0; serve-point win A 65.6%, B 41.3%; Elo A 1829.4, B 1488.6; model uncertainty 0.045
* Form inputs: days since last match A 4, B 47; matches on record A 453, B 228; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.028, surface_dev_loose -0.000, surface_dev_tight +0.003
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24MARSOR-MAR20` Will Fabian Marozsan win the Fabian Marozsan vs Sebastian Sorger match by a set score of 2-0?: 0.59/0.64 mid 61.5%, model 51.7% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT24MARSOR-MAR21` Will Fabian Marozsan win the Fabian Marozsan vs Sebastian Sorger match by a set score of 2-1?: 0.19/0.23 mid 21.0%, model 29.0% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPSETWINNER-26OCT24MARSOR-2-MAR` Will Fabian Marozsan win set 2 in the Fabian Marozsan vs Sebastian Sorger match: 0.74/0.80 mid 77.0%, model 71.9% (projection_v2.0 (prediction ledger)) -- gap -5.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT24MARSOR-2-SOR` Will Sebastian Sorger win set 2 in the Fabian Marozsan vs Sebastian Sorger match: 0.20/0.26 mid 23.0%, model 28.1% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT24MARSOR-1-SOR` Will Sebastian Sorger win set 1 in the Fabian Marozsan vs Sebastian Sorger match: 0.22/0.25 mid 23.5%, model 28.1% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT24MARSOR-1-MAR` Will Fabian Marozsan win set 1 in the Fabian Marozsan vs Sebastian Sorger match: 0.73/0.77 mid 75.0%, model 71.9% (projection_v2.0 (prediction ledger)) -- gap -3.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPEXACTMATCH-26OCT24MARSOR-SOR21` Will Sebastian Sorger win the Fabian Marozsan vs Sebastian Sorger match by a set score of 2-1?: 0.07/0.11 mid 9.0%, model 11.3% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26OCT24MARSOR-SOR20` Will Sebastian Sorger win the Fabian Marozsan vs Sebastian Sorger match by a set score of 2-0?: 0.08/0.10 mid 9.0%, model 7.9% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; WIDE_SPREAD

## Sandro Kopp vs Filippo Romano -- ATP Challenger Florence SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-24T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207491:211542:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sandro Kopp (`KXATPCHALLENGERMATCH-26OCT24KOPROM-KOP`) | -- / 0.01 (138359) | -- | 46.4% | 45.0% | 47.0% [45.1%-50.0%] | 53.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | FRESH | A / ADEQUATE | INSUFFICIENT_INPUTS | VERIFIED |
| Filippo Romano (`KXATPCHALLENGERMATCH-26OCT24KOPROM-ROM`) | 0.99 / -- (0) | -- | 53.6% | 55.0% | 53.0% [50.0%-54.9%] | 46.9% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | -- | UNPRICED | FRESH | A / ADEQUATE | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 2600.0, B 1962.0; serve-point win A 65.2%, B 34.0%; Elo A 1462.2, B 1466.6; model uncertainty 0.0247
* Form inputs: days since last match A 12, B 12; matches on record A 412, B 163; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.019, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE

## Daniil Medvedev vs Alexander Bublik -- ATP Almaty SF

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 16:00Z
* Current expected start: 2026-10-24 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-24 12:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106421:122330:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Bublik (`KXATPMATCH-26OCT24MEDBUB-BUB`) | 0.32 / 0.33 (76118) | 32.5% | 34.9% | 30.5% | 30.5% [29.6%-32.1%] | -- | 34.7% | 34.7% | MODEL_LONE_OUTLIER | PASS | +2.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Daniil Medvedev (`KXATPMATCH-26OCT24MEDBUB-MED`) | 0.67 / 0.68 (32045) | 67.5% | 65.1% | 69.5% | 69.5% [67.8%-70.4%] | -- | 65.2% | 65.2% | MODEL_LONE_OUTLIER | WATCH | -2.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5908.0, B 5279.0; serve-point win A 68.2%, B 35.0%; Elo A 2098.4, B 1965.1; model uncertainty 0.0126
* Form inputs: days since last match A 1, B 1; matches on record A 873, B 723; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.000, surface_dev_tight +0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT24MEDBUB-MED6` Will Daniil Medvedev win at least 5.5 more games than Alexander Bublik?: 0.13/0.41 mid 27.0%, model 10.8% (projection_v2.0 (prediction ledger)) -- gap -16.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MEDBUB-MED20` Will Daniil Medvedev win the Daniil Medvedev vs Alexander Bublik match by a set score of 2-0?: 0.41/0.42 mid 41.5%, model 36.3% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24MEDBUB-MED3` Will Daniil Medvedev win at least 2.5 more games than Alexander Bublik?: 0.50/0.56 mid 53.0%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MEDBUB-1-MED` Will Daniil Medvedev win set 1 in the Daniil Medvedev vs Alexander Bublik match: 0.64/0.66 mid 65.0%, model 60.2% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT24MEDBUB-29` Over 28.5 games: 0.30/0.37 mid 33.5%, model 38.1% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MEDBUB-1-BUB` Will Alexander Bublik win set 1 in the Daniil Medvedev vs Alexander Bublik match: 0.35/0.36 mid 35.5%, model 39.8% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT24MEDBUB-24` Over 23.5 games: 0.50/0.52 mid 51.0%, model 54.6% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MEDBUB-MED21` Will Daniil Medvedev win the Daniil Medvedev vs Alexander Bublik match by a set score of 2-1?: 0.25/0.27 mid 26.0%, model 28.8% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MEDBUB-2-BUB` Will Alexander Bublik win set 2 in the Daniil Medvedev vs Alexander Bublik match: 0.36/0.38 mid 37.0%, model 39.8% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MEDBUB-BUB21` Will Alexander Bublik win the Daniil Medvedev vs Alexander Bublik match by a set score of 2-1?: 0.16/0.18 mid 17.0%, model 19.1% (projection_v2.0 (prediction ledger)) -- gap +2.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MEDBUB-2-MED` Will Daniil Medvedev win set 2 in the Daniil Medvedev vs Alexander Bublik match: 0.61/0.63 mid 62.0%, model 60.2% (projection_v2.0 (prediction ledger)) -- gap -1.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT24MEDBUB-19` Over 18.5 games: 0.90/0.93 mid 91.5%, model 90.7% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MEDBUB-BUB20` Will Alexander Bublik win the Daniil Medvedev vs Alexander Bublik match by a set score of 2-0?: 0.15/0.16 mid 15.5%, model 15.8% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24MEDBUB-BUB2` Will Alexander Bublik win at least 1.5 more games than Daniil Medvedev?: 0.20/0.35 mid 27.5%, model 27.6% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yihan Qu vs Teodora Kostovic -- WTA Guangzhou Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 06:00Z
* Current expected start: 2026-10-24 13:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-24 12:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+420_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:264086:267439:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Teodora Kostovic (`KXWTAMATCH-26OCT23YIHKOS-KOS`) | 0.81 / 0.82 (11342) | 81.5% | 97.0% | 92.0% | 94.6% [93.9%-95.4%] | -- | 83.0% | 83.0% | MODEL_LONE_OUTLIER | PASS | +15.5 pp | HIGH_REVIEW | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Yihan Qu (`KXWTAMATCH-26OCT23YIHKOS-YIH`) | 0.18 / 0.19 (31426) | 18.5% | 3.0% | 8.0% | 5.4% [4.6%-6.1%] | -- | 17.4% | 17.4% | MODEL_LONE_OUTLIER | PASS | -15.5 pp | HIGH_REVIEW | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 377.0, B 3286.0; serve-point win A 50.3%, B 35.3%; Elo A 1192.8, B 1710.9; model uncertainty 0.0075
* Form inputs: days since last match A 6, B 8; matches on record A 16, B 114; data quality D

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT23YIHKOS-KOS  (YES = Teodora Kostovic)
Model: 97%
Kalshi: 82%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, EXTERNAL_MARKET_REJECTION, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.007, surface_dev_loose -0.003, surface_dev_tight +0.001
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23YIHKOS-2-KOS` Will Teodora Kostovic win set 2 in the Yihan Qu vs Teodora Kostovic match: 0.73/0.76 mid 74.5%, model 89.6% (projection_v2.0 (prediction ledger)) -- gap +15.1 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT23YIHKOS-2-YIH` Will Yihan Qu win set 2 in the Yihan Qu vs Teodora Kostovic match: 0.24/0.26 mid 25.0%, model 10.4% (projection_v2.0 (prediction ledger)) -- gap -14.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT23YIHKOS-1-KOS` Will Teodora Kostovic win set 1 in the Yihan Qu vs Teodora Kostovic match: 0.87/0.92 mid 89.5%, model 89.6% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26OCT23YIHKOS-1-YIH` Will Yihan Qu win set 1 in the Yihan Qu vs Teodora Kostovic match: 0.07/0.14 mid 10.5%, model 10.4% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## En-Shuo Liang vs Tereza Valentova -- WTA Tokyo Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 08:00Z
* Current expected start: 2026-10-24 13:04Z
* Source: COURT_PROGRESSION: preceding match on Center finished; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-24 12:19Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+304_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215314:238184:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| En-Shuo Liang (`KXWTAMATCH-26OCT24LIAVAL-LIA`) | 0.12 / 0.15 (7) | 13.5% | -- | 18.0% | 19.0% [16.3%-21.6%] | 15.2% | 13.6% | 15.2% | MARKETS_AGREE | SHADOW_BET | +5.5 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Tereza Valentova (`KXWTAMATCH-26OCT24LIAVAL-VAL`) | 0.86 / 0.88 (109) | 87.0% | -- | 82.0% | 81.0% [78.4%-83.7%] | 84.8% | 86.1% | 84.8% | MARKETS_AGREE | PASS | -6.0 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2476.0, B 3231.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0268
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.026, surface_dev_loose -0.004, surface_dev_tight -0.000
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anastasia Zakharova vs Ruien Zhang -- WTA Guangzhou Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-24 06:00Z
* Current expected start: 2026-10-24 13:09Z
* Source: COURT_PROGRESSION: preceding match on Center Court in progress (set 3 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-24 12:24Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+429_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-24T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220435:263869:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Zakharova (`KXWTAMATCH-26OCT23ZAKZHA-ZAK`) | 0.89 / 0.90 (15044) | 89.5% | 87.7% | 89.9% | 89.4% [87.7%-90.1%] | 89.9% | 92.2% | 91.0% | MODEL_LONE_OUTLIER | PASS | -1.8 pp | NORMAL | FRESH | B / ADEQUATE | ALL_AGREE | VERIFIED |
| Ruien Zhang (`KXWTAMATCH-26OCT23ZAKZHA-ZHA`) | 0.10 / 0.11 (8902) | 10.5% | 12.3% | 10.1% | 10.6% [9.9%-12.3%] | 10.1% | 9.5% | 9.8% | MODEL_LONE_OUTLIER | PASS | +1.8 pp | NORMAL | FRESH | B / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4628.0, B 1375.0; serve-point win A 61.5%, B 47.4%; Elo A 1813.0, B 1448.5; model uncertainty 0.012
* Form inputs: days since last match A 2, B 18; matches on record A 481, B 107; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.007, surface_dev_loose +0.007, surface_dev_tight -0.010
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT23ZAKZHA-2-ZAK` Will Anastasia Zakharova win set 2 in the Anastasia Zakharova vs Ruien Zhang match: 0.84/0.86 mid 85.0%, model 78.1% (projection_v2.0 (prediction ledger)) -- gap -6.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23ZAKZHA-2-ZHA` Will Ruien Zhang win set 2 in the Anastasia Zakharova vs Ruien Zhang match: 0.14/0.16 mid 15.0%, model 21.9% (projection_v2.0 (prediction ledger)) -- gap +6.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23ZAKZHA-1-ZAK` Will Anastasia Zakharova win set 1 in the Anastasia Zakharova vs Ruien Zhang match: 0.81/0.83 mid 82.0%, model 78.1% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT23ZAKZHA-1-ZHA` Will Ruien Zhang win set 1 in the Anastasia Zakharova vs Ruien Zhang match: 0.17/0.19 mid 18.0%, model 21.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS

## Aleksandar Kovacevic vs James Duckworth -- ATP Basel Q1

**START STATUS: START_IMMINENT**
* Nominal schedule: 2026-10-24 11:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-24 13:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-24 12:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105902:206499:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Duckworth (`KXATPMATCH-26OCT24KOVDUC-DUC`) | 0.39 / 0.40 (1976) | 39.5% | 44.0% | 56.5% | 54.6% [51.9%-57.9%] | 40.6% | 39.4% | 40.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +4.5 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Aleksandar Kovacevic (`KXATPMATCH-26OCT24KOVDUC-KOV`) | 0.60 / 0.61 (9869) | 60.5% | 56.0% | 43.5% | 45.4% [42.1%-48.1%] | 59.4% | 60.3% | 59.8% | MODEL_LONE_OUTLIER | PASS | -4.5 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4778.0, B 5151.0; serve-point win A 70.6%, B 30.7%; Elo A 1756.5, B 1745.6; model uncertainty 0.0303
* Form inputs: days since last match A 4, B 1; matches on record A 400, B 900; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.032, surface_pool_high +0.028, surface_dev_loose +0.005, surface_dev_tight -0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24KOVDUC-KOV20` Will Aleksandar Kovacevic win the Aleksandar Kovacevic vs James Duckworth match by a set score of 2-0?: 0.36/0.38 mid 37.0%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap -7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24KOVDUC-DUC21` Will James Duckworth win the Aleksandar Kovacevic vs James Duckworth match by a set score of 2-1?: 0.16/0.20 mid 18.0%, model 22.9% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KOVDUC-1-DUC` Will James Duckworth win set 1 in the Aleksandar Kovacevic vs James Duckworth match: 0.40/0.43 mid 41.5%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24KOVDUC-KOV21` Will Aleksandar Kovacevic win the Aleksandar Kovacevic vs James Duckworth match by a set score of 2-1?: 0.20/0.25 mid 22.5%, model 26.8% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KOVDUC-1-KOV` Will Aleksandar Kovacevic win set 1 in the Aleksandar Kovacevic vs James Duckworth match: 0.57/0.59 mid 58.0%, model 54.0% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KOVDUC-2-DUC` Will James Duckworth win set 2 in the Aleksandar Kovacevic vs James Duckworth match: 0.40/0.44 mid 42.0%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap +4.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24KOVDUC-2-KOV` Will Aleksandar Kovacevic win set 2 in the Aleksandar Kovacevic vs James Duckworth match: 0.55/0.60 mid 57.5%, model 54.0% (projection_v2.0 (prediction ledger)) -- gap -3.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24KOVDUC-DUC20` Will James Duckworth win the Aleksandar Kovacevic vs James Duckworth match by a set score of 2-0?: 0.20/0.24 mid 22.0%, model 21.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Francisco Cerundolo vs Tallon Griekspoor -- ATP Brussels SF

**START STATUS: START_IMMINENT**
* Nominal schedule: 2026-10-24 17:00Z
* Current expected start: 2026-10-24 13:39Z
* Source: COURT_PROGRESSION: preceding match on Centre Court in progress (set 2 of best-of-5); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-24 12:54Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-201_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:134868:202103:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cerundolo (`KXATPMATCH-26OCT24CERGRI-CER`) | 0.59 / 0.60 (71031) | 59.5% | 61.0% | 64.7% | 61.5% [58.7%-62.9%] | 58.3% | 59.2% | 58.8% | MODEL_LONE_OUTLIER | PASS | +1.5 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Tallon Griekspoor (`KXATPMATCH-26OCT24CERGRI-GRI`) | 0.40 / 0.41 (32201) | 40.5% | 39.0% | 35.3% | 38.5% [37.1%-41.3%] | 41.7% | 40.7% | 41.2% | MODEL_LONE_OUTLIER | PASS | -1.5 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5642.0, B 4445.0; serve-point win A 67.3%, B 35.0%; Elo A 1877.7, B 1864.6; model uncertainty 0.021
* Form inputs: days since last match A 1, B 1; matches on record A 562, B 689; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.019, surface_dev_loose -0.005, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT24CERGRI-25` Over 24.5 games: 0.46/0.47 mid 46.5%, model 54.5% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24CERGRI-30` Over 29.5 games: 0.26/0.27 mid 26.5%, model 34.0% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24CERGRI-CER21` Will Francisco Cerundolo win the Francisco Cerundolo vs Tallon Griekspoor match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 28.1% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24CERGRI-GRI20` Will Tallon Griekspoor win the Francisco Cerundolo vs Tallon Griekspoor match by a set score of 2-0?: 0.22/0.24 mid 23.0%, model 18.1% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24CERGRI-CER5` Will Francisco Cerundolo win at least 4.5 more games than Tallon Griekspoor?: 0.22/0.26 mid 24.0%, model 19.6% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24CERGRI-20` Over 19.5 games: 0.78/0.81 mid 79.5%, model 83.7% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24CERGRI-CER20` Will Francisco Cerundolo win the Francisco Cerundolo vs Tallon Griekspoor match by a set score of 2-0?: 0.35/0.39 mid 37.0%, model 33.0% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24CERGRI-GRI21` Will Tallon Griekspoor win the Francisco Cerundolo vs Tallon Griekspoor match by a set score of 2-1?: 0.16/0.18 mid 17.0%, model 20.8% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERGRI-1-GRI` Will Tallon Griekspoor win set 1 in the Francisco Cerundolo vs Tallon Griekspoor match: 0.41/0.42 mid 41.5%, model 42.6% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT24CERGRI-GRI2` Will Tallon Griekspoor win at least 1.5 more games than Francisco Cerundolo?: 0.29/0.33 mid 31.0%, model 31.4% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERGRI-2-CER` Will Francisco Cerundolo win set 2 in the Francisco Cerundolo vs Tallon Griekspoor match: 0.55/0.59 mid 57.0%, model 57.4% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERGRI-2-GRI` Will Tallon Griekspoor win set 2 in the Francisco Cerundolo vs Tallon Griekspoor match: 0.41/0.45 mid 43.0%, model 42.6% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26OCT24CERGRI-CER2` Will Francisco Cerundolo win at least 1.5 more games than Tallon Griekspoor?: 0.53/0.54 mid 53.5%, model 53.1% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24CERGRI-1-CER` Will Francisco Cerundolo win set 1 in the Francisco Cerundolo vs Tallon Griekspoor match: 0.57/0.58 mid 57.5%, model 57.4% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE

## Flavio Cobolli vs Lorenzo Musetti -- ATP Lyon SF

**START STATUS: START_IMMINENT**
* Nominal schedule: 2026-10-24 16:10Z
* Current expected start: 2026-10-24 13:39Z
* Source: COURT_PROGRESSION: preceding match on Court Central Auvergne-Rhone-Alpes in progress (set 2 of best-of-5); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-24 12:54Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-151_MIN

ATP (TOUR_500_250) · Clay · scheduled 2026-10-24T16:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207518:207925:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Flavio Cobolli (`KXATPMATCH-26OCT24COBMUS-COB`) | 0.54 / 0.56 (115702) | 55.0% | 35.2% | 39.4% | 37.0% [35.6%-38.5%] | 54.3% | 54.8% | 54.5% | MODEL_LONE_OUTLIER | PASS | -19.8 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Lorenzo Musetti (`KXATPMATCH-26OCT24COBMUS-MUS`) | 0.45 / 0.46 (101512) | 45.5% | 64.8% | 60.6% | 63.0% [61.6%-64.4%] | 45.7% | 44.9% | 45.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +19.2 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 6397.0, B 4401.0; serve-point win A 60.2%, B 36.8%; Elo A 1972.1, B 2117.5; model uncertainty 0.0145
* Form inputs: days since last match A 1, B 1; matches on record A 453, B 486; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT24COBMUS-MUS  (YES = Lorenzo Musetti)
Model: 65%
Kalshi: 46%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_REJECTION, UNKNOWN
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.009, surface_dev_tight -0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT24COBMUS-COB2` Will Flavio Cobolli win at least 1.5 more games than Lorenzo Musetti?: 0.48/0.49 mid 48.5%, model 28.7% (projection_v2.0 (prediction ledger)) -- gap -19.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24COBMUS-MUS2` Will Lorenzo Musetti win at least 1.5 more games than Flavio Cobolli?: 0.40/0.41 mid 40.5%, model 57.9% (projection_v2.0 (prediction ledger)) -- gap +17.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24COBMUS-COB20` Will Flavio Cobolli win the Flavio Cobolli vs Lorenzo Musetti match by a set score of 2-0?: 0.32/0.33 mid 32.5%, model 16.0% (projection_v2.0 (prediction ledger)) -- gap -16.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24COBMUS-1-MUS` Will Lorenzo Musetti win set 1 in the Flavio Cobolli vs Lorenzo Musetti match: 0.45/0.48 mid 46.5%, model 60.0% (projection_v2.0 (prediction ledger)) -- gap +13.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24COBMUS-2-COB` Will Flavio Cobolli win set 2 in the Flavio Cobolli vs Lorenzo Musetti match: 0.51/0.56 mid 53.5%, model 40.0% (projection_v2.0 (prediction ledger)) -- gap -13.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24COBMUS-2-MUS` Will Lorenzo Musetti win set 2 in the Flavio Cobolli vs Lorenzo Musetti match: 0.44/0.49 mid 46.5%, model 60.0% (projection_v2.0 (prediction ledger)) -- gap +13.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24COBMUS-1-COB` Will Flavio Cobolli win set 1 in the Flavio Cobolli vs Lorenzo Musetti match: 0.52/0.54 mid 53.0%, model 40.0% (projection_v2.0 (prediction ledger)) -- gap -13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24COBMUS-MUS20` Will Lorenzo Musetti win the Flavio Cobolli vs Lorenzo Musetti match by a set score of 2-0?: 0.25/0.28 mid 26.5%, model 35.9% (projection_v2.0 (prediction ledger)) -- gap +9.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24COBMUS-MUS21` Will Lorenzo Musetti win the Flavio Cobolli vs Lorenzo Musetti match by a set score of 2-1?: 0.18/0.21 mid 19.5%, model 28.8% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24COBMUS-MUS5` Will Lorenzo Musetti win at least 4.5 more games than Flavio Cobolli?: 0.17/0.26 mid 21.5%, model 28.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24COBMUS-23` Over 22.5 games: 0.52/0.53 mid 52.5%, model 57.3% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24COBMUS-28` Over 27.5 games: 0.31/0.34 mid 32.5%, model 37.0% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24COBMUS-COB21` Will Flavio Cobolli win the Flavio Cobolli vs Lorenzo Musetti match by a set score of 2-1?: 0.19/0.23 mid 21.0%, model 19.2% (projection_v2.0 (prediction ledger)) -- gap -1.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24COBMUS-18` Over 17.5 games: 0.89/0.90 mid 89.5%, model 90.8% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Remy Bertola vs Jakub Paul -- ATP Basel Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 16:40Z
* Current expected start: 2026-10-24 14:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-24 13:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T16:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200329:207605:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Remy Bertola (`KXATPMATCH-26OCT24BERPAU-BER`) | 0.69 / 0.71 (23206) | 70.0% | 55.9% | 57.0% | 56.0% [53.0%-59.4%] | 69.1% | 70.3% | 69.1% | MODEL_LONE_OUTLIER | PASS | -14.1 pp | REVIEW | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jakub Paul (`KXATPMATCH-26OCT24BERPAU-PAU`) | 0.29 / 0.31 (421) | 30.0% | 44.1% | 43.0% | 44.0% [40.6%-47.0%] | 30.9% | 29.3% | 30.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +14.1 pp | REVIEW | FRESH | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3337.0, B 1141.0; serve-point win A 63.4%, B 37.7%; Elo A 1601.8, B 1574.1; model uncertainty 0.0321
* Form inputs: days since last match A 3, B 12; matches on record A 469, B 398; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.030, surface_dev_loose +0.005, surface_dev_tight -0.010
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24BERPAU-BER20` Will Remy Bertola win the Remy Bertola vs Jakub Paul match by a set score of 2-0?: 0.41/0.49 mid 45.0%, model 29.1% (projection_v2.0 (prediction ledger)) -- gap -15.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BERPAU-1-PAU` Will Jakub Paul win set 1 in the Remy Bertola vs Jakub Paul match: 0.32/0.35 mid 33.5%, model 46.1% (projection_v2.0 (prediction ledger)) -- gap +12.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BERPAU-1-BER` Will Remy Bertola win set 1 in the Remy Bertola vs Jakub Paul match: 0.64/0.68 mid 66.0%, model 53.9% (projection_v2.0 (prediction ledger)) -- gap -12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BERPAU-PAU20` Will Jakub Paul win the Remy Bertola vs Jakub Paul match by a set score of 2-0?: 0.02/0.17 mid 9.5%, model 21.2% (projection_v2.0 (prediction ledger)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BERPAU-PAU21` Will Jakub Paul win the Remy Bertola vs Jakub Paul match by a set score of 2-1?: 0.12/0.16 mid 14.0%, model 22.9% (projection_v2.0 (prediction ledger)) -- gap +8.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BERPAU-2-BER` Will Remy Bertola win set 2 in the Remy Bertola vs Jakub Paul match: 0.09/0.91 mid 50.0%, model 53.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24BERPAU-BER21` Will Remy Bertola win the Remy Bertola vs Jakub Paul match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 26.8% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24BERPAU-2-PAU` Will Jakub Paul win set 2 in the Remy Bertola vs Jakub Paul match: 0.08/0.91 mid 49.5%, model 46.1% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Corentin Moutet vs Tomas Machac -- ATP Vienna Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 17:00Z
* Current expected start: 2026-10-24 14:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-24 13:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Clay · scheduled 2026-10-24T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144895:207830:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Machac (`KXATPMATCH-26OCT24MOUMAC-MAC`) | 0.58 / 0.59 (5201) | 58.5% | 44.3% | 44.9% | 46.4% [43.8%-51.5%] | 59.4% | 59.2% | 59.3% | MODEL_LONE_OUTLIER | PASS | -14.2 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Corentin Moutet (`KXATPMATCH-26OCT24MOUMAC-MOU`) | 0.42 / 0.43 (22798) | 42.5% | 55.7% | 55.1% | 53.6% [48.5%-56.2%] | 40.6% | 40.8% | 40.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +13.2 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4376.0, B 3720.0; serve-point win A 60.8%, B 40.3%; Elo A 1842.6, B 1835.3; model uncertainty 0.0385
* Form inputs: days since last match A 1, B 2; matches on record A 603, B 456; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.026, surface_dev_loose +0.010, surface_dev_tight -0.010
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26OCT24MOUMAC-MAC20` Will Tomas Machac win the Corentin Moutet vs Tomas Machac match by a set score of 2-0?: 0.35/0.39 mid 37.0%, model 21.3% (projection_v2.0 (prediction ledger)) -- gap -15.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOUMAC-2-MOU` Will Corentin Moutet win set 2 in the Corentin Moutet vs Tomas Machac match: 0.41/0.45 mid 43.0%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOUMAC-MOU21` Will Corentin Moutet win the Corentin Moutet vs Tomas Machac match by a set score of 2-1?: 0.14/0.19 mid 16.5%, model 26.8% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOUMAC-2-MAC` Will Tomas Machac win set 2 in the Corentin Moutet vs Tomas Machac match: 0.54/0.58 mid 56.0%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOUMAC-1-MOU` Will Corentin Moutet win set 1 in the Corentin Moutet vs Tomas Machac match: 0.44/0.45 mid 44.5%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap +9.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24MOUMAC-1-MAC` Will Tomas Machac win set 1 in the Corentin Moutet vs Tomas Machac match: 0.54/0.56 mid 55.0%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap -8.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOUMAC-MOU20` Will Corentin Moutet win the Corentin Moutet vs Tomas Machac match by a set score of 2-0?: 0.22/0.24 mid 23.0%, model 29.0% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24MOUMAC-MAC21` Will Tomas Machac win the Corentin Moutet vs Tomas Machac match by a set score of 2-1?: 0.19/0.23 mid 21.0%, model 23.0% (projection_v2.0 (prediction ledger)) -- gap +2.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE

## Popovic / Shinikova vs Alhussein Abdel Aziz / Samir -- W15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24POPSHIALHSAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alhussein Abdel Aziz / Samir (`KXITFWDOUBLES-26OCT24POPSHIALHSAM-ALHSAM`) | 0.88 / 0.89 (120) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Popovic / Shinikova (`KXITFWDOUBLES-26OCT24POPSHIALHSAM-POPSHI`) | 0.08 / 0.13 (224) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Svyatoslav Gulin vs Elmer Moller -- ATP Challenger Lisbon SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-24T14:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209284:210425:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Svyatoslav Gulin (`KXATPCHALLENGERMATCH-26OCT24GULMOL-GUL`) | 0.13 / 0.14 (21392) | 13.5% | 32.8% | 36.0% | 29.8% [25.4%-32.6%] | 32.9% | -- | 32.9% | MODEL_LONE_OUTLIER | PASS | +19.2 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Elmer Moller (`KXATPCHALLENGERMATCH-26OCT24GULMOL-MOL`) | 0.86 / 0.87 (36677) | 86.5% | 67.2% | 64.0% | 70.2% [67.5%-74.6%] | 67.1% | -- | 67.1% | MODEL_LONE_OUTLIER | PASS | -19.2 pp | HIGH_REVIEW | FRESH | B / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 1071.0, B 3763.0; serve-point win A 54.3%, B 42.4%; Elo A 1551.2, B 1722.1; model uncertainty 0.0356
* Form inputs: days since last match A 12, B 12; matches on record A 261, B 310; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT24GULMOL-GUL  (YES = Svyatoslav Gulin)
Model: 33%
Kalshi: 14%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_MODEL
Data quality: B (ADEQUATE)
Reasons: EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.022, surface_pool_high +0.019, surface_dev_loose -0.000, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Dorji / Tsheyang Wangmo vs Al-Mudahka / Khalifa -- Billie Jean King Cup Qualifiers UNK

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TEAM) · surface ? · scheduled 2026-10-24T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24DORTSHALMKHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Al-Mudahka / Khalifa (`KXITFWDOUBLES-26OCT24DORTSHALMKHA-ALMKHA`) | 0.55 / 0.70 (300) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dorji / Tsheyang Wangmo (`KXITFWDOUBLES-26OCT24DORTSHALMKHA-DORTSH`) | 0.30 / 0.98 (330) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Karin Saizan / Usama Ali vs Abualhaj / Sayej -- Billie Jean King Cup Qualifiers UNK

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TEAM) · surface ? · scheduled 2026-10-24T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24KARUSAABUSAY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abualhaj / Sayej (`KXITFWDOUBLES-26OCT24KARUSAABUSAY-ABUSAY`) | 0.01 / 0.99 (637) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karin Saizan / Usama Ali (`KXITFWDOUBLES-26OCT24KARUSAABUSAY-KARUSA`) | 0.01 / 0.99 (1287) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Qureshi / Suhail vs sagheb tehrani / Soltani -- Billie Jean King Cup Qualifiers UNK

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 14:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TEAM) · surface ? · scheduled 2026-10-24T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24QURSUHSAGSOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Qureshi / Suhail (`KXITFWDOUBLES-26OCT24QURSUHSAGSOL-QURSUH`) | 0.01 / 0.99 (1387) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| sagheb tehrani / Soltani (`KXITFWDOUBLES-26OCT24QURSUHSAGSOL-SAGSOL`) | 0.01 / 0.99 (537) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Michele Ribecai / Gabriele Volpi vs Dominik Recek / Daniel Siniakov -- ATP Challenger Florence QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 15:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-24T15:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24RIBVOLRECSIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dominik Recek / Daniel Siniakov (`KXATPCHALLENGERDOUBLES-26OCT24RIBVOLRECSIN-RECSIN`) | 0.54 / 0.85 (233) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Michele Ribecai / Gabriele Volpi (`KXATPCHALLENGERDOUBLES-26OCT24RIBVOLRECSIN-RIBVOL`) | 0.10 / 0.29 (28) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Oriol Roca Batalla vs Michele Ribecai -- ATP Challenger Florence SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 15:15Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-24T15:15:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24ROCRIB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michele Ribecai (`KXATPCHALLENGERMATCH-26OCT24ROCRIB-RIB`) | 0.53 / 0.55 (6383) | 54.0% | -- | -- | -- [-----] | -- | 55.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oriol Roca Batalla (`KXATPCHALLENGERMATCH-26OCT24ROCRIB-ROC`) | 0.45 / 0.47 (20459) | 46.0% | -- | -- | -- [-----] | -- | 43.7% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Francesco Forti / Filippo Romano vs Mats Hermans / Max Houkes -- ATP Challenger Florence SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 15:55Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-24T15:55:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24FORROMHERHOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesco Forti / Filippo Romano (`KXATPCHALLENGERDOUBLES-26OCT24FORROMHERHOU-FORROM`) | 0.05 / 0.95 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mats Hermans / Max Houkes (`KXATPCHALLENGERDOUBLES-26OCT24FORROMHERHOU-HERHOU`) | 0.05 / 0.95 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Thiago Agustin Tirante vs Adrian Mannarino -- ATP Vienna Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 19:00Z
* Current expected start: 2026-10-24 16:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-24 15:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Clay · scheduled 2026-10-24T19:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105173:202058:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Mannarino (`KXATPMATCH-26OCT24TIRMAN-MAN`) | 0.40 / 0.41 (26364) | 40.5% | 19.7% | 19.2% | 19.9% [15.7%-26.8%] | 40.6% | 39.1% | 39.1% | MARKETS_AGREE | PASS | -20.8 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Thiago Agustin Tirante (`KXATPMATCH-26OCT24TIRMAN-TIR`) | 0.61 / 0.62 (6199) | 61.5% | 80.3% | 80.8% | 80.1% [73.2%-84.3%] | 59.4% | 61.0% | 61.0% | MARKETS_AGREE | WATCH | +18.8 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4804.0, B 4318.0; serve-point win A 67.7%, B 39.2%; Elo A 1828.7, B 1598.5; model uncertainty 0.0555
* Form inputs: days since last match A 5, B 1; matches on record A 489, B 1320; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT24TIRMAN-TIR  (YES = Thiago Agustin Tirante)
Model: 80%
Kalshi: 62%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.017, surface_dev_loose +0.043, surface_dev_tight -0.044
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT24TIRMAN-2-TIR` Will Thiago Agustin Tirante win set 2 in the Thiago Agustin Tirante vs Adrian Mannarino match: 0.08/0.91 mid 49.5%, model 71.5% (projection_v2.0 (prediction ledger)) -- gap +22.1 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24TIRMAN-2-MAN` Will Adrian Mannarino win set 2 in the Thiago Agustin Tirante vs Adrian Mannarino match: 0.08/0.91 mid 49.5%, model 28.4% (projection_v2.0 (prediction ledger)) -- gap -21.1 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24TIRMAN-1-TIR` Will Thiago Agustin Tirante win set 1 in the Thiago Agustin Tirante vs Adrian Mannarino match: 0.56/0.59 mid 57.5%, model 71.5% (projection_v2.0 (prediction ledger)) -- gap +14.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24TIRMAN-MAN20` Will Adrian Mannarino win the Thiago Agustin Tirante vs Adrian Mannarino match by a set score of 2-0?: 0.20/0.24 mid 22.0%, model 8.1% (projection_v2.0 (prediction ledger)) -- gap -13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24TIRMAN-1-MAN` Will Adrian Mannarino win set 1 in the Thiago Agustin Tirante vs Adrian Mannarino match: 0.40/0.43 mid 41.5%, model 28.4% (projection_v2.0 (prediction ledger)) -- gap -13.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24TIRMAN-TIR20` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Adrian Mannarino match by a set score of 2-0?: 0.37/0.40 mid 38.5%, model 51.2% (projection_v2.0 (prediction ledger)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24TIRMAN-TIR21` Will Thiago Agustin Tirante win the Thiago Agustin Tirante vs Adrian Mannarino match by a set score of 2-1?: 0.18/0.24 mid 21.0%, model 29.1% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24TIRMAN-MAN21` Will Adrian Mannarino win the Thiago Agustin Tirante vs Adrian Mannarino match by a set score of 2-1?: 0.13/0.19 mid 16.0%, model 11.6% (projection_v2.0 (prediction ledger)) -- gap -4.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kumru / Paszun vs Vogt / Yashina -- W35 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24KUMPASVOGYAS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kumru / Paszun (`KXITFWDOUBLES-26OCT24KUMPASVOGYAS-KUMPAS`) | 0.02 / 0.06 (44) | 4.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vogt / Yashina (`KXITFWDOUBLES-26OCT24KUMPASVOGYAS-VOGYAS`) | 0.93 / 0.99 (616) | 96.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Arthur Fils vs Jan-Lennard Struff -- ATP Brussels SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-24 19:30Z
* Current expected start: 2026-10-24 16:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-24 15:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-24T19:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105526:209950:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fils (`KXATPMATCH-26OCT24FILSTR-FIL`) | 0.81 / 0.82 (85913) | 81.5% | 85.7% | 81.7% | 81.7% [78.5%-83.0%] | 79.8% | 81.0% | 80.4% | MODEL_LONE_OUTLIER | PASS | +4.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26OCT24FILSTR-STR`) | 0.19 / 0.20 (43472) | 19.5% | 14.3% | 18.3% | 18.3% [17.0%-21.5%] | 20.2% | 19.1% | 19.6% | MODEL_LONE_OUTLIER | PASS | -5.2 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4268.0, B 4793.0; serve-point win A 71.2%, B 37.6%; Elo A 2048.2, B 1805.2; model uncertainty 0.0224
* Form inputs: days since last match A 1, B 1; matches on record A 334, B 1070; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.006, surface_dev_loose +0.012, surface_dev_tight -0.019
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26OCT24FILSTR-FIL8` Will Arthur Fils win at least 7.5 more games than Jan-Lennard Struff?: 0.04/0.19 mid 11.5%, model 4.6% (projection_v2.0 (prediction ledger)) -- gap -6.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24FILSTR-FIL2` Will Arthur Fils win at least 1.5 more games than Jan-Lennard Struff?: 0.72/0.76 mid 74.0%, model 80.5% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24FILSTR-FIL21` Will Arthur Fils win the Arthur Fils vs Jan-Lennard Struff match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 27.7% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT24FILSTR-FIL5` Will Arthur Fils win at least 4.5 more games than Jan-Lennard Struff?: 0.43/0.44 mid 43.5%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24FILSTR-18` Over 17.5 games: 0.84/0.89 mid 86.5%, model 90.0% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT24FILSTR-28` Over 27.5 games: 0.26/0.29 mid 27.5%, model 30.8% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24FILSTR-STR20` Will Jan-Lennard Struff win the Arthur Fils vs Jan-Lennard Struff match by a set score of 2-0?: 0.07/0.10 mid 8.5%, model 5.7% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24FILSTR-1-STR` Will Jan-Lennard Struff win set 1 in the Arthur Fils vs Jan-Lennard Struff match: 0.25/0.27 mid 26.0%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26OCT24FILSTR-23` Over 22.5 games: 0.47/0.49 mid 48.0%, model 49.4% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24FILSTR-2-FIL` Will Arthur Fils win set 2 in the Arthur Fils vs Jan-Lennard Struff match: 0.73/0.77 mid 75.0%, model 76.2% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24FILSTR-STR21` Will Jan-Lennard Struff win the Arthur Fils vs Jan-Lennard Struff match by a set score of 2-1?: 0.08/0.11 mid 9.5%, model 8.7% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT24FILSTR-1-FIL` Will Arthur Fils win set 1 in the Arthur Fils vs Jan-Lennard Struff match: 0.76/0.77 mid 76.5%, model 76.2% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT24FILSTR-2-STR` Will Jan-Lennard Struff win set 2 in the Arthur Fils vs Jan-Lennard Struff match: 0.22/0.25 mid 23.5%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT24FILSTR-FIL20` Will Arthur Fils win the Arthur Fils vs Jan-Lennard Struff match by a set score of 2-0?: 0.57/0.59 mid 58.0%, model 58.0% (projection_v2.0 (prediction ledger)) -- gap +0.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sonja Zhenikhova vs Andrea Obradovic -- W15 Bol SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:239474:264961:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Obradovic (`KXITFWMATCH-26OCT24ZHEOBR-OBR`) | 0.56 / 0.57 (35) | 56.5% | 49.6% | 61.1% | 55.3% [51.1%-58.5%] | -- | -- | -- | -- | PASS | -6.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sonja Zhenikhova (`KXITFWMATCH-26OCT24ZHEOBR-ZHE`) | 0.40 / 0.42 (307) | 41.0% | 50.4% | 38.9% | 44.7% [41.5%-48.9%] | -- | -- | -- | -- | PASS | +9.4 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1212.0, B 929.0; serve-point win A 53.0%, B 47.1%; Elo A 1388.4, B 1405.6; model uncertainty 0.0372
* Form inputs: days since last match A 243, B 411; matches on record A 38, B 108; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.016, surface_dev_loose -0.021, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karol Drzewiecki / Piotr Matuszewski vs Tiago Pereira / Benjamin Winter Lopez -- ATP Challenger Lisbon F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-24T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24DRZMATPERWIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karol Drzewiecki / Piotr Matuszewski (`KXATPCHALLENGERDOUBLES-26OCT24DRZMATPERWIN-DRZMAT`) | 0.47 / 0.54 (63) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tiago Pereira / Benjamin Winter Lopez (`KXATPCHALLENGERDOUBLES-26OCT24DRZMATPERWIN-PERWIN`) | 0.43 / 0.49 (59) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mia Horvit vs Tara Wuerth -- W15 Bol SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24HORWUE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mia Horvit (`KXITFWMATCH-26OCT24HORWUE-HOR`) | 0.54 / 0.57 (107) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tara Wuerth (`KXITFWMATCH-26OCT24HORWUE-WUE`) | 0.40 / 0.46 (73) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Geoffrey Blancaneaux vs Imanol Lopez Morillo -- M15 Bol SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 17:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T17:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144972:202209:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Geoffrey Blancaneaux (`KXITFMATCH-26OCT24BLALOP-BLA`) | 0.35 / 0.41 (39) | 38.0% | 69.8% | 51.5% | 66.0% [62.6%-69.2%] | 67.5% | -- | 67.5% | MODEL_LONE_OUTLIER | PASS | +31.8 pp | EXTREME (DATA_WARNING) | FRESH | C / POOR | AGREES_WITH_MODEL | VERIFIED |
| Imanol Lopez Morillo (`KXITFMATCH-26OCT24BLALOP-LOP`) | 0.52 / 0.57 (15) | 54.5% | 30.2% | 48.5% | 34.0% [30.8%-37.4%] | 32.5% | -- | 32.5% | MODEL_LONE_OUTLIER | PASS | -24.3 pp | HIGH_REVIEW | FRESH | C / POOR | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 3141.0, B 173.0; serve-point win A 62.6%, B 41.4%; Elo A 1526.1, B 1365.3; model uncertainty 0.033
* Form inputs: days since last match A 26, B 26; matches on record A 668, B 357; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT24BLALOP-BLA  (YES = Geoffrey Blancaneaux)
Model: 70%
Kalshi: 38%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_MODEL
Data quality: C (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.034, surface_pool_high +0.032, surface_dev_loose -0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bertimon / Blancaneaux vs Bielinskyi / Simundza -- M15 Bol SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24BERBLABIESIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bertimon / Blancaneaux (`KXITFDOUBLES-26OCT24BERBLABIESIM-BERBLA`) | 0.01 / 0.98 (3) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bielinskyi / Simundza (`KXITFDOUBLES-26OCT24BERBLABIESIM-BIESIM`) | -- / 0.98 (4) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Weronika Falkowska vs Federica Urgesi -- W35 Loule SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216579:223415:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weronika Falkowska (`KXITFWMATCH-26OCT24FALURG-FAL`) | 0.44 / 0.45 (6761) | 44.5% | 43.4% | 58.4% | 54.2% [47.3%-57.4%] | 49.0% | -- | 49.0% | MARKETS_AGREE | WATCH | -1.1 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |
| Federica Urgesi (`KXITFWMATCH-26OCT24FALURG-URG`) | 0.55 / 0.56 (3438) | 55.5% | 56.6% | 41.6% | 45.8% [42.6%-52.7%] | 50.9% | -- | 50.9% | MARKETS_AGREE | PASS | +1.1 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 2031.0, B 2635.0; serve-point win A 55.0%, B 43.7%; Elo A 1576.2, B 1586.9; model uncertainty 0.0501
* Form inputs: days since last match A 19, B 33; matches on record A 372, B 169; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.011, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Suzan Lamens vs Elsa Jacquemot -- W100 Wrexham SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215480:221039:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elsa Jacquemot (`KXITFWMATCH-26OCT24LAMJAC-JAC`) | 0.74 / 0.75 (109) | 74.5% | 37.8% | 48.9% | 46.8% [44.1%-47.9%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -36.7 pp | EXTREME (DATA_WARNING) | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Suzan Lamens (`KXITFWMATCH-26OCT24LAMJAC-LAM`) | 0.25 / 0.26 (232) | 25.5% | 62.2% | 51.1% | 53.2% [52.1%-55.9%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +36.7 pp | EXTREME (DATA_WARNING) | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3938.0, B 4592.0; serve-point win A 54.4%, B 47.9%; Elo A 1843.2, B 1779.0; model uncertainty 0.0186
* Form inputs: days since last match A 19, B 11; matches on record A 545, B 402; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT24LAMJAC-LAM  (YES = Suzan Lamens)
Model: 62%
Kalshi: 26%
Gap: +37 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Philip Henning vs Adrien Gobat -- M25 Sarreguemines SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-10-24T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202475:210254:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrien Gobat (`KXITFMATCH-26OCT24HENGOB-GOB`) | 0.29 / 0.30 (10428) | 29.5% | 23.2% | 40.4% | 34.1% [33.2%-35.6%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Philip Henning (`KXITFMATCH-26OCT24HENGOB-HEN`) | 0.70 / 0.71 (284) | 70.5% | 76.8% | 59.6% | 65.9% [64.4%-66.8%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1821.0, B 307.0; serve-point win A 64.2%, B 41.5%; Elo A 1580.2, B 1362.9; model uncertainty 0.0118
* Form inputs: days since last match A 12, B 243; matches on record A 215, B 161; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.009, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mariam Bolkvadze vs Harmony Tan -- W50 Cherbourg-en-Cotentin SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211552:213734:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariam Bolkvadze (`KXITFWMATCH-26OCT24BOLTAN-BOL`) | 0.21 / 0.23 (43) | 22.0% | 49.4% | 27.8% | 38.4% [34.4%-45.2%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +27.4 pp | EXTREME (DATA_WARNING) | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Harmony Tan (`KXITFWMATCH-26OCT24BOLTAN-TAN`) | 0.75 / 0.79 (52) | 77.0% | 50.6% | 72.2% | 61.6% [54.8%-65.6%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -26.4 pp | EXTREME (DATA_WARNING) | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1814.0, B 3731.0; serve-point win A 53.6%, B 46.3%; Elo A 1733.1, B 1710.5; model uncertainty 0.054
* Form inputs: days since last match A 16, B 10; matches on record A 553, B 652; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT24BOLTAN-BOL  (YES = Mariam Bolkvadze)
Model: 49%
Kalshi: 22%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.021, surface_dev_loose -0.000, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Felipe Meligeni Alves vs Valerio Aboian -- ATP Challenger Cali SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-24T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200335:209254:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valerio Aboian (`KXATPCHALLENGERMATCH-26OCT24MELABO-ABO`) | 0.24 / 0.25 (2811) | 24.5% | 32.7% | 35.9% | 33.0% [31.2%-34.0%] | -- | 24.7% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +8.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Felipe Meligeni Alves (`KXATPCHALLENGERMATCH-26OCT24MELABO-MEL`) | 0.75 / 0.77 (17993) | 76.0% | 67.3% | 64.1% | 67.0% [66.0%-68.8%] | -- | 75.3% | -- | INSUFFICIENT_INPUTS | PASS | -8.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2750.0, B 2578.0; serve-point win A 62.1%, B 41.4%; Elo A 1672.6, B 1509.5; model uncertainty 0.0139
* Form inputs: days since last match A 12, B 12; matches on record A 528, B 364; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Christie / Silva vs Britton / Klugman -- W100 Wrexham SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24CHRSILBRIKLU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Britton / Klugman (`KXITFWDOUBLES-26OCT24CHRSILBRIKLU-BRIKLU`) | 0.30 / 0.60 (6) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Christie / Silva (`KXITFWDOUBLES-26OCT24CHRSILBRIKLU-CHRSIL`) | 0.37 / 0.64 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ana Sofia Sanchez vs Barbara Gatica -- W15 Campina Grande SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-24T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204419:211903:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barbara Gatica (`KXITFWMATCH-26OCT24SANGAT-GAT`) | 0.41 / 0.42 (7071) | 41.5% | 70.1% | 43.6% | 56.4% [53.2%-61.6%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +28.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ana Sofia Sanchez (`KXITFWMATCH-26OCT24SANGAT-SAN`) | 0.58 / 0.59 (5898) | 58.5% | 29.9% | 56.4% | 43.6% [38.4%-46.8%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -28.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 3191.0, B 633.0; serve-point win A 47.2%, B 48.8%; Elo A 1543.7, B 1628.4; model uncertainty 0.0421
* Form inputs: days since last match A 42, B 1615; matches on record A 854, B 388; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT24SANGAT-GAT  (YES = Barbara Gatica)
Model: 70%
Kalshi: 42%
Gap: +29 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.027, surface_pool_high -0.026, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katarina Zavatska vs Manon Leonard -- W50 Cherbourg-en-Cotentin SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215290:215807:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manon Leonard (`KXITFWMATCH-26OCT24ZAVLEO-LEO`) | 0.54 / 0.57 (67) | 55.5% | 43.9% | 50.5% | 50.5% [41.5%-55.9%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.6 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katarina Zavatska (`KXITFWMATCH-26OCT24ZAVLEO-ZAV`) | 0.41 / 0.45 (94) | 43.0% | 56.1% | 49.5% | 49.5% [44.1%-58.5%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +13.1 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4227.0, B 3201.0; serve-point win A 54.1%, B 47.0%; Elo A 1610.5, B 1624.9; model uncertainty 0.0717
* Form inputs: days since last match A 15, B 131; matches on record A 498, B 348; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.043, surface_pool_high -0.053, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Florencia Urrutia vs Justina Maria Gonzalez Daniele -- W15 Campina Grande SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-24T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220447:260708:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justina Maria Gonzalez Daniele (`KXITFWMATCH-26OCT24URRGON-GON`) | 0.46 / 0.50 (347) | 48.0% | 48.0% | 50.0% | 47.3% [43.1%-48.9%] | -- | -- | -- | -- | PASS | -0.0 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Florencia Urrutia (`KXITFWMATCH-26OCT24URRGON-URR`) | 0.50 / 0.51 (20) | 50.5% | 52.0% | 50.0% | 52.7% [51.1%-56.9%] | -- | -- | -- | -- | PASS | +1.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2454.0, B 2911.0; serve-point win A 51.1%, B 49.3%; Elo A 1496.2, B 1445.0; model uncertainty 0.0293
* Form inputs: days since last match A 180, B 180; matches on record A 106, B 154; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gustavo Heide vs Matheus Pucinelli de Almeida -- ATP Challenger Cali SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-24T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207799:208361:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gustavo Heide (`KXATPCHALLENGERMATCH-26OCT24HEIPDA-HEI`) | 0.58 / 0.60 (5853) | 59.0% | 61.9% | 58.7% | 62.2% [60.2%-64.6%] | 58.4% | 60.1% | 60.1% | MODEL_LONE_OUTLIER | WATCH | +2.9 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Matheus Pucinelli de Almeida (`KXATPCHALLENGERMATCH-26OCT24HEIPDA-PDA`) | 0.40 / 0.41 (64) | 40.5% | 38.1% | 41.3% | 37.8% [35.4%-39.8%] | 41.6% | 40.2% | 40.2% | MODEL_LONE_OUTLIER | PASS | -2.4 pp | NORMAL | FRESH | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3721.0, B 3547.0; serve-point win A 61.1%, B 41.2%; Elo A 1767.8, B 1639.8; model uncertainty 0.0219
* Form inputs: days since last match A 19, B 19; matches on record A 314, B 409; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Oliver Ojakaar vs Rodrigo Fernandes -- M15 Ithaca SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210312:212075:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigo Fernandes (`KXITFMATCH-26OCT24OJAFER-FER`) | 0.35 / 0.36 (9) | 35.5% | 30.9% | 20.9% | 27.7% [25.8%-29.6%] | 35.6% | -- | 35.6% | MODEL_LONE_OUTLIER | PASS | -4.6 pp | NORMAL | FRESH | F / POOR | ALL_AGREE | VERIFIED |
| Oliver Ojakaar (`KXITFMATCH-26OCT24OJAFER-OJA`) | 0.64 / 0.65 (502) | 64.5% | 69.1% | 79.1% | 72.3% [70.4%-74.2%] | 64.4% | -- | 64.4% | MODEL_LONE_OUTLIER | PASS | +4.6 pp | NORMAL | FRESH | F / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 188.0, B 311.0; serve-point win A 63.2%, B 40.7%; Elo A 1370.4, B 1228.2; model uncertainty 0.0188
* Form inputs: days since last match A 418, B 432; matches on record A 48, B 37; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.001, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jack Anthrop vs Rafael Ymer -- M15 Ithaca SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210294:212165:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Anthrop (`KXITFMATCH-26OCT24ANTYME-ANT`) | 0.85 / 0.88 (77) | 86.5% | 91.9% | 83.6% | 78.6% [78.0%-80.1%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Rafael Ymer (`KXITFMATCH-26OCT24ANTYME-YME`) | 0.12 / 0.14 (4) | 13.0% | 8.1% | 16.4% | 21.4% [19.9%-22.0%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 204.0, B 75.0; serve-point win A 67.1%, B 43.9%; Elo A 1442.4, B 1184.7; model uncertainty 0.0105
* Form inputs: days since last match A 348, B 740; matches on record A 77, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.000, surface_dev_loose -0.001, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alan Magadan / Rodrigo Pacheco Mendez vs Federico Zeballos / Marcelo Zormann -- ATP Challenger Cali F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-24T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24MAGPACZEBZOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alan Magadan / Rodrigo Pacheco Mendez (`KXATPCHALLENGERDOUBLES-26OCT24MAGPACZEBZOR-MAGPAC`) | 0.48 / 0.63 (108) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Federico Zeballos / Marcelo Zormann (`KXATPCHALLENGERDOUBLES-26OCT24MAGPACZEBZOR-ZEBZOR`) | 0.36 / 0.52 (119) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Reese Brantmeier vs Hiromi Abe -- W75 Saguenay SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221362:222034:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hiromi Abe (`KXITFWMATCH-26OCT24BRAABE-ABE`) | 0.30 / 0.31 (263) | 30.5% | 42.5% | 79.8% | 58.4% [56.4%-61.4%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.0 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Reese Brantmeier (`KXITFWMATCH-26OCT24BRAABE-BRA`) | 0.69 / 0.70 (84) | 69.5% | 57.5% | 20.2% | 41.6% [38.6%-43.6%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.0 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 133.0, B 2555.0; serve-point win A 56.4%, B 45.0%; Elo A 1649.0, B 1691.9; model uncertainty 0.0253
* Form inputs: days since last match A 27, B 222; matches on record A 89, B 200; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Madison Brengle vs Ella McDonald -- W50 Austin F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-24T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201483:259591:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madison Brengle (`KXITFWMATCH-26OCT24BREMCD-BRE`) | 0.50 / 0.51 (55) | 50.5% | 69.9% | 51.6% | 63.1% [59.6%-71.3%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +19.4 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ella McDonald (`KXITFWMATCH-26OCT24BREMCD-MCD`) | 0.49 / 0.50 (289) | 49.5% | 30.1% | 48.4% | 36.9% [28.7%-40.4%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.4 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2464.0, B 1341.0; serve-point win A 53.5%, B 50.4%; Elo A 1752.5, B 1577.6; model uncertainty 0.0589
* Form inputs: days since last match A 59, B 123; matches on record A 1012, B 146; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT24BREMCD-BRE  (YES = Madison Brengle)
Model: 70%
Kalshi: 50%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.005, surface_dev_loose -0.020, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dahlberg / Velcz vs Cox / Ojakaar -- M15 Ithaca F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24DAHVELCOXOJA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cox / Ojakaar (`KXITFDOUBLES-26OCT24DAHVELCOXOJA-COXOJA`) | 0.05 / 0.51 (51) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dahlberg / Velcz (`KXITFDOUBLES-26OCT24DAHVELCOXOJA-DAHVEL`) | 0.05 / 0.63 (67) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sander Jong vs Darwin Blanch -- ATP Challenger Fort Worth SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-24T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210093:210464:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Darwin Blanch (`KXATPCHALLENGERMATCH-26OCT24JONBLA-BLA`) | 0.73 / 0.74 (5600) | 73.5% | 74.0% | 61.2% | 73.1% [71.9%-73.6%] | 73.1% | 73.9% | 73.5% | MARKETS_AGREE | PASS | +0.5 pp | NORMAL | FRESH | C / POOR | ALL_AGREE | VERIFIED |
| Sander Jong (`KXATPCHALLENGERMATCH-26OCT24JONBLA-JON`) | 0.27 / 0.28 (2975) | 27.5% | 26.0% | 38.8% | 26.9% [26.4%-28.1%] | 26.9% | 27.1% | 27.0% | MARKETS_AGREE | PASS | -1.5 pp | NORMAL | FRESH | C / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 155.0, B 3314.0; serve-point win A 63.5%, B 31.2%; Elo A 1504.4, B 1711.7; model uncertainty 0.0082
* Form inputs: days since last match A 139, B 26; matches on record A 126, B 173; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Ariana Arseneault vs Yuki Naito -- W75 Saguenay SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-24T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216044:220502:2026-10-24`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ariana Arseneault (`KXITFWMATCH-26OCT24ARSNAI-ARS`) | 0.51 / 0.52 (277) | 51.5% | 36.6% | 48.4% | 42.6% [38.4%-45.2%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.9 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuki Naito (`KXITFWMATCH-26OCT24ARSNAI-NAI`) | 0.46 / 0.49 (23) | 47.5% | 63.4% | 51.6% | 57.4% [54.8%-61.6%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +15.9 pp | HIGH_REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2049.0, B 2186.0; serve-point win A 52.8%, B 44.7%; Elo A 1491.0, B 1603.6; model uncertainty 0.0339
* Form inputs: days since last match A 33, B 33; matches on record A 129, B 359; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT24ARSNAI-NAI  (YES = Yuki Naito)
Model: 63%
Kalshi: 48%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Henrique Chabalgoity / Fontes Damorim vs Farjat / Martinez -- M15 Maceio F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-24 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-24T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24HENFONFARMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Farjat / Martinez (`KXITFDOUBLES-26OCT24HENFONFARMAR-FARMAR`) | 0.35 / 0.37 (174) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Henrique Chabalgoity / Fontes Damorim (`KXITFDOUBLES-26OCT24HENFONFARMAR-HENFON`) | 0.63 / 0.67 (89) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Bayerlova / Gimbrere vs Brantmeier / Tanguilig -- W75 Saguenay F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-25T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24BAYGIMBRATAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bayerlova / Gimbrere (`KXITFWDOUBLES-26OCT24BAYGIMBRATAN-BAYGIM`) | 0.05 / 0.41 (42) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Brantmeier / Tanguilig (`KXITFWDOUBLES-26OCT24BAYGIMBRATAN-BRATAN`) | 0.19 / 0.72 (89) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Fairclough / Christine Lutkemeyer vs Fouad / Justine Hejtmanek -- W35 Bakersfield CA SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-25T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24FAICHRFOUJUS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fairclough / Christine Lutkemeyer (`KXITFWDOUBLES-26OCT24FAICHRFOUJUS-FAICHR`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fouad / Justine Hejtmanek (`KXITFWDOUBLES-26OCT24FAICHRFOUJUS-FOUJUS`) | 0.05 / 0.95 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mediorreal Arias / Sofia Sanchez vs Garcia Vidal / Konishi Camargo Silva -- W15 Campina Grande F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-25T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24MEDSOFGARKON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Garcia Vidal / Konishi Camargo Silva (`KXITFWDOUBLES-26OCT24MEDSOFGARKON-GARKON`) | 0.05 / 0.38 (40) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mediorreal Arias / Sofia Sanchez (`KXITFWDOUBLES-26OCT24MEDSOFGARKON-MEDSOF`) | 0.05 / 0.74 (96) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jenson Brooksby vs Gabriel Debru -- ATP Challenger Fort Worth SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 00:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-25T00:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202385:210120:2026-10-25`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jenson Brooksby (`KXATPCHALLENGERMATCH-26OCT24BRODEB-BRO`) | 0.80 / 0.83 (5097) | 81.5% | 62.8% | 61.2% | 64.1% [63.1%-66.5%] | -- | -- | -- | -- | PASS | -18.7 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gabriel Debru (`KXATPCHALLENGERMATCH-26OCT24BRODEB-DEB`) | 0.17 / 0.19 (90) | 18.0% | 37.2% | 38.8% | 35.9% [33.6%-36.9%] | -- | -- | -- | -- | SHADOW_BET | +19.2 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2946.0, B 1388.0; serve-point win A 61.2%, B 41.3%; Elo A 1828.9, B 1692.9; model uncertainty 0.0165
* Form inputs: days since last match A 15, B 89; matches on record A 289, B 184; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT24BRODEB-DEB  (YES = Gabriel Debru)
Model: 37%
Kalshi: 18%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Joao Victor Couto Loureiro vs Kaua Lorenzo Santos Gava -- M15 Maceio SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208533:211732:2026-10-25`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Victor Couto Loureiro (`KXITFMATCH-26OCT24COUSAN-COU`) | 0.55 / 0.59 (337) | 57.0% | 71.9% | 38.0% | 40.9% [40.9%-40.9%] | -- | -- | -- | -- | PASS | +14.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kaua Lorenzo Santos Gava (`KXITFMATCH-26OCT24COUSAN-SAN`) | 0.40 / 0.43 (122) | 41.5% | 28.1% | 62.0% | 59.1% [59.1%-59.1%] | -- | -- | -- | -- | PASS | -13.4 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 509.0, B 49.0; serve-point win A 62.6%, B 41.9%; Elo A 1202.1, B 1180.4; model uncertainty 0.0002
* Form inputs: days since last match A 201, B 453; matches on record A 139, B 6; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aliaksandra Sasnovich vs Kamilla Rakhimova -- WTA Tokyo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-25 04:00Z
* Current expected start: 2026-10-25 01:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-25 00:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-150_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-25T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:205925:215872:2026-10-25`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kamilla Rakhimova (`KXWTAMATCH-26OCT24SASRAK-RAK`) | 0.43 / 0.46 (1222) | 44.5% | 52.9% | 43.7% | 44.7% [44.2%-47.9%] | 45.7% | 44.4% | 45.7% | MODEL_LONE_OUTLIER | PASS | +8.4 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Aliaksandra Sasnovich (`KXWTAMATCH-26OCT24SASRAK-SAS`) | 0.54 / 0.57 (1300) | 55.5% | 47.1% | 56.3% | 55.3% [52.1%-55.8%] | 54.3% | 54.8% | 54.3% | MODEL_LONE_OUTLIER | PASS | -8.4 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4822.0, B 5718.0; serve-point win A 55.2%, B 44.2%; Elo A 1844.7, B 1844.8; model uncertainty 0.0185
* Form inputs: days since last match A 0, B 0; matches on record A 793, B 479; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.000
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT24SASRAK-1-SAS` Will Aliaksandra Sasnovich win set 1 in the Aliaksandra Sasnovich vs Kamilla Rakhimova match: 0.52/0.56 mid 54.0%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap -5.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT24SASRAK-1-RAK` Will Kamilla Rakhimova win set 1 in the Aliaksandra Sasnovich vs Kamilla Rakhimova match: 0.45/0.48 mid 46.5%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT24SASRAK-2-SAS` Will Aliaksandra Sasnovich win set 2 in the Aliaksandra Sasnovich vs Kamilla Rakhimova match: 0.08/0.91 mid 49.5%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26OCT24SASRAK-2-RAK` Will Kamilla Rakhimova win set 2 in the Aliaksandra Sasnovich vs Kamilla Rakhimova match: 0.08/0.94 mid 51.0%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Heather Watson vs Alycia Parks -- WTA Tokyo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-25 04:00Z
* Current expected start: 2026-10-25 01:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-25 00:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-150_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-25T04:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201586:219917:2026-10-25`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alycia Parks (`KXWTAMATCH-26OCT24WATPAR-PAR`) | 0.53 / 0.55 (380) | 54.0% | 60.9% | 69.8% | 64.1% [56.2%-67.0%] | 53.2% | 52.6% | 53.2% | MARKETS_AGREE | WATCH | +6.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Heather Watson (`KXWTAMATCH-26OCT24WATPAR-WAT`) | 0.45 / 0.47 (1673) | 46.0% | 39.1% | 30.2% | 35.9% [33.0%-43.8%] | 46.8% | 47.2% | 46.8% | MARKETS_AGREE | PASS | -6.9 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2194.0, B 5263.0; serve-point win A 58.8%, B 39.0%; Elo A 1739.3, B 1772.6; model uncertainty 0.0538
* Form inputs: days since last match A 0, B 0; matches on record A 822, B 440; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.014, surface_dev_loose -0.009, surface_dev_tight +0.010

## Lorenzo Gagliardo vs Pedro Sakamoto -- M15 Maceio SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106203:207682:2026-10-25`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Gagliardo (`KXITFMATCH-26OCT24GAGSAK-GAG`) | 0.34 / 0.37 (40) | 35.5% | 34.6% | 54.6% | 18.9% [15.4%-22.5%] | -- | -- | -- | -- | PASS | -0.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pedro Sakamoto (`KXITFMATCH-26OCT24GAGSAK-SAK`) | 0.61 / 0.64 (185) | 62.5% | 65.4% | 45.4% | 81.2% [77.5%-84.6%] | -- | -- | -- | -- | PASS | +2.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 202.0, B 1912.0; serve-point win A 57.6%, B 39.3%; Elo A 1321.4, B 1575.2; model uncertainty 0.0354
* Form inputs: days since last match A 229, B 26; matches on record A 97, B 717; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mai Hontama vs Maya Joint -- WTA Tokyo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-25 05:00Z
* Current expected start: 2026-10-25 02:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-25 01:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-25T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT24HONJOI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mai Hontama (`KXWTAMATCH-26OCT24HONJOI-HON`) | 0.08 / 0.29 (5) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maya Joint (`KXWTAMATCH-26OCT24HONJOI-JOI`) | 0.68 / 0.92 (10) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hanna Chang vs Connie Ma -- W35 Bakersfield CA SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-25T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213949:221143:2026-10-25`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanna Chang (`KXITFWMATCH-26OCT24CHAMAX-CHA`) | 0.17 / 0.22 (32) | 19.5% | 68.7% | 75.6% | 68.5% [68.5%-68.5%] | -- | -- | -- | -- | PASS | +49.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Connie Ma (`KXITFWMATCH-26OCT24CHAMAX-MAX`) | 0.76 / 0.83 (240) | 79.5% | 31.4% | 24.4% | 31.6% [31.6%-31.6%] | -- | -- | -- | -- | PASS | -48.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 3084.0, B 0.0; serve-point win A 56.4%, B 47.2%; Elo A 1608.7, B 1475.0; model uncertainty 0.0
* Form inputs: days since last match A 187, B 1846; matches on record A 519, B 21; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT24CHAMAX-CHA  (YES = Hanna Chang)
Model: 69%
Kalshi: 20%
Gap: +49 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lan Mi vs Jenna DeFalco -- W35 Bakersfield CA SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-25T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221914:260141:2026-10-25`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jenna DeFalco (`KXITFWMATCH-26OCT24MIXDEF-DEF`) | 0.52 / 0.54 (44) | 53.0% | 42.2% | 29.5% | 38.9% [33.8%-48.4%] | -- | -- | -- | -- | PASS | -10.8 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lan Mi (`KXITFWMATCH-26OCT24MIXDEF-MIX`) | 0.44 / 0.48 (78) | 46.0% | 57.8% | 70.5% | 61.1% [51.6%-66.2%] | -- | -- | -- | -- | WATCH | +11.8 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2699.0, B 1687.0; serve-point win A 50.4%, B 51.1%; Elo A 1444.9, B 1442.5; model uncertainty 0.0728
* Form inputs: days since last match A 180, B 180; matches on record A 89, B 247; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.015, surface_dev_loose +0.015, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kimberly Birrell vs Daria Kasatkina -- WTA Tokyo Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-25 06:00Z
* Current expected start: 2026-10-25 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-25 02:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

WTA (TOUR_500_250) · surface ? · scheduled 2026-10-25T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT24BIRKAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kimberly Birrell (`KXWTAMATCH-26OCT24BIRKAS-BIR`) | 0.27 / 0.74 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daria Kasatkina (`KXWTAMATCH-26OCT24BIRKAS-KAS`) | 0.24 / 0.78 (4) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alevtina Ibragimova vs Polina Iatcenko -- WTA Guangzhou Q3

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-25 05:00Z
* Current expected start: 2026-10-25 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-25 02:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-120_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-25T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:223325:260581:2026-10-25`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Iatcenko (`KXWTAMATCH-26OCT24IBRIAT-IAT`) | 0.64 / 0.66 (6286) | 65.0% | 57.9% | 63.4% | 62.4% [56.3%-64.8%] | 63.2% | 62.9% | 63.2% | MODEL_LONE_OUTLIER | PASS | -7.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Alevtina Ibragimova (`KXWTAMATCH-26OCT24IBRIAT-IBR`) | 0.33 / 0.36 (498) | 34.5% | 42.1% | 36.6% | 37.6% [35.1%-43.7%] | 36.8% | 37.4% | 36.8% | KALSHI_LONE_OUTLIER | PASS | +7.6 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2867.0, B 2951.0; serve-point win A 56.8%, B 41.7%; Elo A 1692.0, B 1767.7; model uncertainty 0.0428
* Form inputs: days since last match A 0, B 0; matches on record A 202, B 300; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.025, surface_dev_loose +0.005, surface_dev_tight -0.005
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26OCT24IBRIAT-1-IAT` Will Polina Iatcenko win set 1 in the Alevtina Ibragimova vs Polina Iatcenko match: 0.60/0.64 mid 62.0%, model 55.3% (projection_v2.0 (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT24IBRIAT-2-IBR` Will Alevtina Ibragimova win set 2 in the Alevtina Ibragimova vs Polina Iatcenko match: 0.08/0.94 mid 51.0%, model 44.7% (projection_v2.0 (prediction ledger)) -- gap -6.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT24IBRIAT-1-IBR` Will Alevtina Ibragimova win set 1 in the Alevtina Ibragimova vs Polina Iatcenko match: 0.37/0.41 mid 39.0%, model 44.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT24IBRIAT-2-IAT` Will Polina Iatcenko win set 2 in the Alevtina Ibragimova vs Polina Iatcenko match: 0.08/0.94 mid 51.0%, model 55.3% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ashlyn Krueger vs Katerina Siniakova -- WTA Osaka F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-25 07:30Z
* Current expected start: 2026-10-25 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-25 03:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

WTA (TOUR_500_250) · Hard · scheduled 2026-10-25T07:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211701:221909:2026-10-25`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashlyn Krueger (`KXWTAMATCH-26OCT25KRUSIN-KRU`) | 0.45 / 0.47 (14730) | 46.0% | 45.6% | 30.9% | 35.2% [33.2%-39.6%] | 45.7% | 46.0% | 45.9% | MODEL_LONE_OUTLIER | PASS | -0.4 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Katerina Siniakova (`KXWTAMATCH-26OCT25KRUSIN-SIN`) | 0.54 / 0.55 (13494) | 54.5% | 54.4% | 69.1% | 64.8% [60.4%-66.8%] | 54.3% | 53.3% | 54.3% | MODEL_LONE_OUTLIER | SHADOW_BET | -0.1 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4211.0, B 4278.0; serve-point win A 57.3%, B 41.9%; Elo A 1906.0, B 1924.5; model uncertainty 0.0319
* Form inputs: days since last match A 0, B 0; matches on record A 345, B 724; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.004, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26OCT25KRUSIN-27` Over 26.5 games: 0.03/0.97 mid 50.0%, model 40.2% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT25KRUSIN-22` Over 21.5 games: 0.54/0.57 mid 55.5%, model 63.6% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT25KRUSIN-2-SIN` Will Katerina Siniakova win set 2 in the Ashlyn Krueger vs Katerina Siniakova match: 0.01/0.92 mid 46.5%, model 52.9% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26OCT25KRUSIN-17` Over 16.5 games: 0.85/0.95 mid 90.0%, model 94.3% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26OCT25KRUSIN-2-KRU` Will Ashlyn Krueger win set 2 in the Ashlyn Krueger vs Katerina Siniakova match: 0.01/0.98 mid 49.5%, model 47.1% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT25KRUSIN-1-KRU` Will Ashlyn Krueger win set 1 in the Ashlyn Krueger vs Katerina Siniakova match: 0.47/0.49 mid 48.0%, model 47.1% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26OCT25KRUSIN-1-SIN` Will Katerina Siniakova win set 1 in the Ashlyn Krueger vs Katerina Siniakova match: 0.50/0.54 mid 52.0%, model 52.9% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Blake Ellis vs Isaac Becroft -- M25 Tamworth F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-25T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:134329:208653:2026-10-25`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isaac Becroft (`KXITFMATCH-26OCT24ELLBEC-BEC`) | 0.45 / 0.56 (17) | 50.5% | 19.9% | 51.0% | 25.1% [24.2%-26.4%] | -- | -- | -- | -- | PASS | -30.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Blake Ellis (`KXITFMATCH-26OCT24ELLBEC-ELL`) | 0.43 / 0.45 (18) | 44.0% | 80.1% | 49.0% | 74.9% [73.6%-75.8%] | -- | -- | -- | -- | PASS | +36.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1850.0, B 69.0; serve-point win A 66.0%, B 40.6%; Elo A 1570.8, B 1311.2; model uncertainty 0.0109
* Form inputs: days since last match A 40, B 180; matches on record A 391, B 106; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT24ELLBEC-ELL  (YES = Blake Ellis)
Model: 80%
Kalshi: 44%
Gap: +36 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.008, surface_dev_loose -0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hikaru Sato vs I Wen Wan -- W35 Sydney F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-25T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221141:267449:2026-10-25`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hikaru Sato (`KXITFWMATCH-26OCT24SATWAN-SAT`) | 0.61 / 0.64 (4) | 62.5% | 78.9% | 55.3% | 69.7% [66.9%-73.8%] | -- | -- | -- | -- | PASS | +16.4 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| I Wen Wan (`KXITFWMATCH-26OCT24SATWAN-WAN`) | 0.34 / 0.38 (17) | 36.0% | 21.1% | 44.7% | 30.3% [26.2%-33.1%] | -- | -- | -- | -- | PASS | -14.9 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1807.0, B 553.0; serve-point win A 59.1%, B 47.0%; Elo A 1465.8, B 1276.4; model uncertainty 0.0345
* Form inputs: days since last match A 187, B 236; matches on record A 175, B 26; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT24SATWAN-SAT  (YES = Hikaru Sato)
Model: 79%
Kalshi: 62%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.000, surface_dev_loose +0.009, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cristina Bucsa / Nicole Melichar-Martinez vs Desirae Krawczyk / Fanny Stollar -- WTA Ningbo F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-25 09:30Z
* Current expected start: 2026-10-25 06:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-25 05:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT25BUCMELKRASTO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Bucsa / Nicole Melichar-Martinez (`KXWTADOUBLES-26OCT25BUCMELKRASTO-BUCMEL`) | 0.05 / 0.95 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Desirae Krawczyk / Fanny Stollar (`KXWTADOUBLES-26OCT25BUCMELKRASTO-KRASTO`) | 0.05 / 0.95 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Lucas Miedler / Neil Oberleitner vs Yuki Bhambri / Ryan Seggerman -- ATP Almaty F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-25 10:00Z
* Current expected start: 2026-10-25 07:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: 2026-10-25 06:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25MIEOBEBHASEG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuki Bhambri / Ryan Seggerman (`KXATPDOUBLES-26OCT25MIEOBEBHASEG-BHASEG`) | 0.05 / 0.94 (84) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26OCT25MIEOBEBHASEG-MIEOBE`) | 0.06 / 0.95 (257) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Becroft / Shepp vs Talic / Vickery -- M25 Tamworth SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-25T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24BECSHETALVIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Becroft / Shepp (`KXITFDOUBLES-26OCT24BECSHETALVIC-BECSHE`) | 0.05 / 0.92 (30) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Talic / Vickery (`KXITFDOUBLES-26OCT24BECSHETALVIC-TALVIC`) | 0.05 / 0.88 (56) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Hugo Hashimoto vs Yuto Oki -- M15 Tanagura F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212639:213074:2026-10-25`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Hashimoto (`KXITFMATCH-26OCT24HASOKI-HAS`) | 0.49 / 0.54 (153) | 51.5% | 38.4% | 47.4% | 48.0% [47.9%-48.0%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuto Oki (`KXITFMATCH-26OCT24HASOKI-OKI`) | 0.45 / 0.49 (36) | 47.0% | 61.6% | 52.5% | 52.0% [52.0%-52.0%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 113.0; serve-point win A 57.8%, B 39.9%; Elo A 1248.3, B 1310.2; model uncertainty 0.0001
* Form inputs: days since last match A 208, B 208; matches on record A 5, B 42; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eric Jr Olivarez vs Vivek Kolluru -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-25T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT24OLIKOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vivek Kolluru (`KXITFMATCH-26OCT24OLIKOL-KOL`) | 0.04 / 0.96 (22) | 50.0% | 55.9% | -- | -- [-----] | -- | -- | -- | -- | -- | +5.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Eric Jr Olivarez (`KXITFMATCH-26OCT24OLIKOL-OLI`) | 0.03 / 0.97 (280) | 50.0% | 44.1% | -- | -- [-----] | -- | -- | -- | -- | -- | -5.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 59.0%, B 39.9%; Elo A 1225.8, B 1256.8; model uncertainty None
* Form inputs: days since last match A 194, B 348; matches on record A 4, B 2; data quality F
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jesy Chea vs Amodini Naik -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-25T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24CHENAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jesy Chea (`KXITFWMATCH-26OCT24CHENAI-CHE`) | 0.04 / 0.66 (22) | 35.0% | 44.1% | -- | -- [-----] | -- | -- | -- | -- | -- | +9.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Amodini Naik (`KXITFWMATCH-26OCT24CHENAI-NAI`) | 0.35 / 0.97 (206) | 66.0% | 55.9% | -- | -- [-----] | -- | -- | -- | -- | -- | -10.1 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 52.1%, B 46.8%; Elo A 1228.5, B 1182.8; model uncertainty None
* Form inputs: days since last match A 341, B 208; matches on record A 2, B 9; data quality F
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yi Jie Janelle Chen vs Saumrita Jagatdeo Verma -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24CHEVER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yi Jie Janelle Chen (`KXITFWMATCH-26OCT24CHEVER-CHE`) | 0.04 / 0.95 (30) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Saumrita Jagatdeo Verma (`KXITFWMATCH-26OCT24CHEVER-VER`) | 0.03 / 0.97 (206) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mirudhula Palanivel vs Minxu Zhou -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-25T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24PALZHO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mirudhula Palanivel (`KXITFWMATCH-26OCT24PALZHO-PAL`) | 0.04 / 0.56 (33) | 30.0% | 25.2% | -- | -- [-----] | -- | -- | -- | -- | -- | -4.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Minxu Zhou (`KXITFWMATCH-26OCT24PALZHO-ZHO`) | 0.45 / 0.97 (206) | 71.0% | 74.8% | -- | -- [-----] | -- | -- | -- | -- | -- | +3.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 50.8%, B 44.2%; Elo A 1176.6, B 1278.5; model uncertainty None
* Form inputs: days since last match A 404, B 705; matches on record A 12, B 3; data quality F
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luca Staeheli vs Mikalai Haliak -- M15 Shenzhen F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-25T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144915:207664:2026-10-25`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mikalai Haliak (`KXITFMATCH-26OCT24STAHAL-HAL`) | 0.28 / 0.34 (42) | 31.0% | 47.4% | 38.3% | 55.7% [52.1%-64.1%] | 33.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +16.4 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luca Staeheli (`KXITFMATCH-26OCT24STAHAL-STA`) | 0.64 / 0.70 (75) | 67.0% | 52.6% | 61.7% | 44.3% [35.9%-47.9%] | 67.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.4 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 545.0, B 2107.0; serve-point win A 55.3%, B 45.2%; Elo A 1379.1, B 1367.0; model uncertainty 0.0601
* Form inputs: days since last match A 26, B 215; matches on record A 123, B 344; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT24STAHAL-HAL  (YES = Mikalai Haliak)
Model: 47%
Kalshi: 31%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.015, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Violet Apisah vs Alexandra Malova -- W15 Singapore F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24APIMAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Violet Apisah (`KXITFWMATCH-26OCT24APIMAL-API`) | 0.60 / 0.73 (96) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexandra Malova (`KXITFWMATCH-26OCT24APIMAL-MAL`) | 0.20 / 0.30 (1) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria KHOMUTSIANSKAYA vs Xinxin Yao -- W35 Qian Daohu F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-25T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222944:252587:2026-10-25`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria KHOMUTSIANSKAYA (`KXITFWMATCH-26OCT24KHOYAO-KHO`) | 0.52 / 0.56 (125) | 54.0% | 68.2% | 96.2% | 90.1% [73.4%-93.9%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +14.2 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xinxin Yao (`KXITFWMATCH-26OCT24KHOYAO-YAO`) | 0.44 / 0.47 (14) | 45.5% | 31.8% | 3.8% | 9.9% [6.1%-26.6%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.7 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3178.0, B 2972.0; serve-point win A 57.2%, B 46.4%; Elo A 1665.8, B 1573.7; model uncertainty 0.1025
* Form inputs: days since last match A 278, B 19; matches on record A 171, B 320; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.005, surface_dev_loose +0.007, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yilin Chen vs Jannat Chiripal -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-25T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24CHECHI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yilin Chen (`KXITFWMATCH-26OCT24CHECHI-CHE`) | 0.04 / 0.96 (22) | 50.0% | 91.9% | -- | -- [-----] | -- | -- | -- | -- | -- | +41.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Jannat Chiripal (`KXITFWMATCH-26OCT24CHECHI-CHI`) | 0.03 / 0.97 (206) | 50.0% | 8.1% | -- | -- [-----] | -- | -- | -- | -- | -- | -41.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 57.7%, B 52.7%; Elo A 1304.9, B 1107.9; model uncertainty None
* Form inputs: days since last match A 502, B 180; matches on record A 9, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT24CHECHI-CHE  (YES = Yilin Chen)
Model: 92%
Kalshi: 50%
Gap: +42 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tejaswi Manneni vs Xiaochuan Nie -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24MANNIE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tejaswi Manneni (`KXITFWMATCH-26OCT24MANNIE-MAN`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xiaochuan Nie (`KXITFWMATCH-26OCT24MANNIE-NIE`) | 0.03 / 0.97 (206) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Harini Parthiban vs Bela Tamhankar -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24PARTAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harini Parthiban (`KXITFWMATCH-26OCT24PARTAM-PAR`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bela Tamhankar (`KXITFWMATCH-26OCT24PARTAM-TAM`) | 0.03 / 0.97 (1918) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zi Xuan Yang vs Nalu Himeno -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT24YANHIM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nalu Himeno (`KXITFWMATCH-26OCT24YANHIM-HIM`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zi Xuan Yang (`KXITFWMATCH-26OCT24YANHIM-YAN`) | 0.03 / 0.97 (1918) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elena Rybakina vs Leylah Fernandez -- WTA Ningbo F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z
* Current expected start: 2026-10-25 09:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:00Z
* Recommended handicap-by time: 2026-10-25 08:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT25RYBFER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leylah Fernandez (`KXWTAMATCH-26OCT25RYBFER-FER`) | 0.24 / 0.26 (1) | 25.0% | 21.6% | -- | -- [-----] | -- | 26.3% | -- | INSUFFICIENT_INPUTS | -- | -3.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Elena Rybakina (`KXWTAMATCH-26OCT25RYBFER-RYB`) | 0.73 / 0.76 (5845) | 74.5% | 78.4% | -- | -- [-----] | -- | 73.1% | -- | INSUFFICIENT_INPUTS | -- | +3.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 66.0%, B 40.3%; Elo A 2248.9, B 1977.8; model uncertainty None
* Form inputs: days since last match A 1, B 0; matches on record A 591, B 404; data quality A
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maxime Janvier vs Ergi Kirkin -- M15 Singapore F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-25T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126125:144985:2026-10-25`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxime Janvier (`KXITFMATCH-26OCT24JANKIR-JAN`) | 0.53 / 0.58 (10) | 55.5% | 50.0% | 62.4% | 60.4% [54.5%-63.3%] | -- | -- | -- | -- | PASS | -5.5 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ergi Kirkin (`KXITFMATCH-26OCT24JANKIR-KIR`) | 0.28 / 0.46 (46) | 37.0% | 50.0% | 37.6% | 39.6% [36.7%-45.5%] | -- | -- | -- | -- | PASS | +12.9 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2255.0, B 1449.0; serve-point win A 60.9%, B 39.1%; Elo A 1467.8, B 1451.9; model uncertainty 0.044
* Form inputs: days since last match A 40, B 75; matches on record A 773, B 492; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.019, surface_dev_loose +0.010, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luke Koh vs Sam Kydd Baumgartner -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25KOHBAU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sam Kydd Baumgartner (`KXITFMATCH-26OCT25KOHBAU-BAU`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luke Koh (`KXITFMATCH-26OCT25KOHBAU-KOH`) | 0.03 / 0.97 (280) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tomohiro Masabayashi vs Julien Tremolieres -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25MASTRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomohiro Masabayashi (`KXITFMATCH-26OCT25MASTRE-MAS`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Julien Tremolieres (`KXITFMATCH-26OCT25MASTRE-TRE`) | 0.03 / 0.97 (280) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sarah Pang vs Saily Prashantkumar Thakkar -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT25PANTHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sarah Pang (`KXITFWMATCH-26OCT25PANTHA-PAN`) | 0.04 / 0.95 (30) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Saily Prashantkumar Thakkar (`KXITFWMATCH-26OCT25PANTHA-THA`) | 0.03 / 0.97 (1918) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jiho Shin vs Janie Ho -- W15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT25SHIHOX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Janie Ho (`KXITFWMATCH-26OCT25SHIHOX-HOX`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jiho Shin (`KXITFWMATCH-26OCT25SHIHOX-SHI`) | 0.03 / 0.97 (206) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karan Singh vs Digvijay Pratap Singh -- M25 Mumbai F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25SINSIN2:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karan Singh (`KXITFMATCH-26OCT25SINSIN2-SIN`) | 0.58 / 0.63 (58) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Digvijay Pratap Singh (`KXITFMATCH-26OCT25SINSIN2-SIN2`) | 0.20 / 0.42 (43) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adithya SURESH vs Loic Namigandet Tenguere -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25SURNAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Loic Namigandet Tenguere (`KXITFMATCH-26OCT25SURNAM-NAM`) | 0.04 / 0.96 (22) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Adithya SURESH (`KXITFMATCH-26OCT25SURNAM-SUR`) | 0.03 / 0.97 (280) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eric Ahren Moonga vs Congsup Congcar -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25AHRCON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eric Ahren Moonga (`KXITFMATCH-26OCT25AHRCON-AHR`) | 0.04 / 0.97 (302) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Congsup Congcar (`KXITFMATCH-26OCT25AHRCON-CON`) | 0.03 / 0.97 (280) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tanakorn Srirat vs Alexander Watanabe Eriksson -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25SRIWAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tanakorn Srirat (`KXITFMATCH-26OCT25SRIWAT-SRI`) | 0.04 / 0.66 (22) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Watanabe Eriksson (`KXITFMATCH-26OCT25SRIWAT-WAT`) | 0.35 / 0.95 (30) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daisuke Sumizawa vs Yao Hui Dylan Chan -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25SUMCHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yao Hui Dylan Chan (`KXITFMATCH-26OCT25SUMCHA-CHA`) | 0.04 / 0.97 (302) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daisuke Sumizawa (`KXITFMATCH-26OCT25SUMCHA-SUM`) | 0.03 / 0.97 (280) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ha Minh Duc Vu vs Roy Hobbs -- M15 Singapore R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 11:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-25T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25VUXHOB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Roy Hobbs (`KXITFMATCH-26OCT25VUXHOB-HOB`) | 0.04 / 0.97 (302) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ha Minh Duc Vu (`KXITFMATCH-26OCT25VUXHOB-VUX`) | 0.03 / 0.97 (280) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matteo Berrettini vs Tomas Martin Etcheverry -- ATP Vienna R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25BERETC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Berrettini (`KXATPMATCH-26OCT25BERETC-BER`) | 0.56 / 0.80 (8) | 68.0% | 57.1% | -- | -- [-----] | -- | -- | -- | -- | -- | -10.8 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Tomas Martin Etcheverry (`KXATPMATCH-26OCT25BERETC-ETC`) | 0.20 / 0.61 (30) | 40.5% | 42.9% | -- | -- [-----] | -- | -- | -- | -- | -- | +2.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 68.8%, B 32.7%; Elo A 1968.7, B 1883.7; model uncertainty None
* Form inputs: days since last match A 4, B 3; matches on record A 562, B 648; data quality A
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT25BERETC-1-BER` Will Matteo Berrettini win set 1 in the Matteo Berrettini vs Tomas Martin Etcheverry match: 0.01/0.98 mid 49.5%, model 54.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25BERETC-2-BER` Will Matteo Berrettini win set 2 in the Matteo Berrettini vs Tomas Martin Etcheverry match: 0.01/0.98 mid 49.5%, model 54.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25BERETC-1-ETC` Will Tomas Martin Etcheverry win set 1 in the Matteo Berrettini vs Tomas Martin Etcheverry match: 0.01/0.98 mid 49.5%, model 45.2% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25BERETC-2-ETC` Will Tomas Martin Etcheverry win set 2 in the Matteo Berrettini vs Tomas Martin Etcheverry match: 0.01/0.98 mid 49.5%, model 45.2% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Henry Bernet / Dominic Stricker vs Sadio Doumbia / David Pel -- ATP Basel R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25BERSTRDOUPEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Henry Bernet / Dominic Stricker (`KXATPDOUBLES-26OCT25BERSTRDOUPEL-BERSTR`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sadio Doumbia / David Pel (`KXATPDOUBLES-26OCT25BERSTRDOUPEL-DOUPEL`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Simone Bolelli / Andrea Vavassori vs Marcelo Melo / Alexander Zverev -- ATP Vienna R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25BOLVAVMELZVE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Simone Bolelli / Andrea Vavassori (`KXATPDOUBLES-26OCT25BOLVAVMELZVE-BOLVAV`) | 0.05 / 0.95 (6) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marcelo Melo / Alexander Zverev (`KXATPDOUBLES-26OCT25BOLVAVMELZVE-MELZVE`) | 0.05 / 0.95 (6) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Robert Cash / Alexander Erler vs Guido Andreozzi / Manuel Guinard -- ATP Vienna R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25CASERLANDGUI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guido Andreozzi / Manuel Guinard (`KXATPDOUBLES-26OCT25CASERLANDGUI-ANDGUI`) | 0.05 / 0.95 (6) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Robert Cash / Alexander Erler (`KXATPDOUBLES-26OCT25CASERLANDGUI-CASERL`) | 0.05 / 0.95 (6) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Francisco Cerundolo / Tomas Martin Etcheverry vs Marcelo Arevalo / Mate Pavic -- ATP Vienna R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25CERETCAREPAV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcelo Arevalo / Mate Pavic (`KXATPDOUBLES-26OCT25CERETCAREPAV-AREPAV`) | 0.05 / 0.95 (6) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Francisco Cerundolo / Tomas Martin Etcheverry (`KXATPDOUBLES-26OCT25CERETCAREPAV-CERETC`) | 0.05 / 0.95 (6) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Flavio Cobolli vs Grigor Dimitrov -- ATP Vienna R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25COBDIM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Flavio Cobolli (`KXATPMATCH-26OCT25COBDIM-COB`) | 0.32 / 0.83 (5) | 57.5% | 67.0% | -- | -- [-----] | -- | -- | -- | -- | -- | +9.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Grigor Dimitrov (`KXATPMATCH-26OCT25COBDIM-DIM`) | 0.06 / 0.87 (30) | 46.5% | 33.0% | -- | -- [-----] | -- | -- | -- | -- | -- | -13.5 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 65.7%, B 37.9%; Elo A 1972.1, B 1916.5; model uncertainty None
* Form inputs: days since last match A 1, B 33; matches on record A 453, B 992; data quality A
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT25COBDIM-1-COB` Will Flavio Cobolli win set 1 in the Flavio Cobolli vs Grigor Dimitrov match: 0.01/0.98 mid 49.5%, model 61.6% (projection_v2.0 (prediction ledger)) -- gap +12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25COBDIM-2-COB` Will Flavio Cobolli win set 2 in the Flavio Cobolli vs Grigor Dimitrov match: 0.01/0.98 mid 49.5%, model 61.6% (projection_v2.0 (prediction ledger)) -- gap +12.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25COBDIM-1-DIM` Will Grigor Dimitrov win set 1 in the Flavio Cobolli vs Grigor Dimitrov match: 0.01/0.98 mid 49.5%, model 38.5% (projection_v2.0 (prediction ledger)) -- gap -11.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25COBDIM-2-DIM` Will Grigor Dimitrov win set 2 in the Flavio Cobolli vs Grigor Dimitrov match: 0.01/0.98 mid 49.5%, model 38.5% (projection_v2.0 (prediction ledger)) -- gap -11.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Luciano Darderi vs Matteo Arnaldi -- ATP Vienna R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25DARARN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Arnaldi (`KXATPMATCH-26OCT25DARARN-ARN`) | 0.25 / 0.76 (5) | 50.5% | 40.9% | -- | -- [-----] | -- | -- | -- | -- | -- | -9.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Luciano Darderi (`KXATPMATCH-26OCT25DARARN-DAR`) | 0.20 / 0.80 (8) | 50.0% | 59.1% | -- | -- [-----] | -- | -- | -- | -- | -- | +9.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 62.3%, B 39.5%; Elo A 1989.1, B 1909.9; model uncertainty None
* Form inputs: days since last match A 3, B 5; matches on record A 437, B 399; data quality A
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT25DARARN-1-DAR` Will Luciano Darderi win set 1 in the Luciano Darderi vs Matteo Arnaldi match: 0.01/0.98 mid 49.5%, model 56.1% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25DARARN-2-DAR` Will Luciano Darderi win set 2 in the Luciano Darderi vs Matteo Arnaldi match: 0.01/0.98 mid 49.5%, model 56.1% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25DARARN-1-ARN` Will Matteo Arnaldi win set 1 in the Luciano Darderi vs Matteo Arnaldi match: 0.01/0.98 mid 49.5%, model 43.9% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25DARARN-2-ARN` Will Matteo Arnaldi win set 2 in the Luciano Darderi vs Matteo Arnaldi match: 0.01/0.98 mid 49.5%, model 43.9% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alejandro Davidovich Fokina vs Zizou Bergs -- ATP Basel R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25DAVBER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zizou Bergs (`KXATPMATCH-26OCT25DAVBER-BER`) | 0.18 / 0.69 (5) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alejandro Davidovich Fokina (`KXATPMATCH-26OCT25DAVBER-DAV`) | 0.14 / 0.93 (45) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Novak Djokovic vs Ugo Humbert -- ATP Basel R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25DJOHUM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Novak Djokovic (`KXATPMATCH-26OCT25DJOHUM-DJO`) | 0.59 / 0.93 (45) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ugo Humbert (`KXATPMATCH-26OCT25DJOHUM-HUM`) | 0.06 / 0.63 (13) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Taylor Fritz vs Stefanos Tsitsipas -- ATP Basel R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25FRITSI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taylor Fritz (`KXATPMATCH-26OCT25FRITSI-FRI`) | 0.32 / 0.83 (5) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stefanos Tsitsipas (`KXATPMATCH-26OCT25FRITSI-TSI`) | 0.06 / 0.87 (30) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Robert Galloway / Andre Goransson vs Marc Polmans / Jan Zielinski -- ATP Basel R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25GALGORPOLZIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robert Galloway / Andre Goransson (`KXATPDOUBLES-26OCT25GALGORPOLZIE-GALGOR`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marc Polmans / Jan Zielinski (`KXATPDOUBLES-26OCT25GALGORPOLZIE-POLZIE`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Tallon Griekspoor vs Brandon Nakashima -- ATP Vienna R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25GRINAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tallon Griekspoor (`KXATPMATCH-26OCT25GRINAK-GRI`) | 0.08 / 0.45 (5) | 26.5% | 40.7% | -- | -- [-----] | -- | -- | -- | -- | -- | +14.2 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Brandon Nakashima (`KXATPMATCH-26OCT25GRINAK-NAK`) | 0.45 / 0.93 (45) | 69.0% | 59.3% | -- | -- [-----] | -- | -- | -- | -- | -- | -9.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 66.5%, B 31.6%; Elo A 1863.9, B 1858.4; model uncertainty None
* Form inputs: days since last match A 1, B 1; matches on record A 689, B 471; data quality A
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT25GRINAK-1-NAK` Will Brandon Nakashima win set 1 in the Tallon Griekspoor vs Brandon Nakashima match: 0.01/0.98 mid 49.5%, model 56.2% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25GRINAK-2-NAK` Will Brandon Nakashima win set 2 in the Tallon Griekspoor vs Brandon Nakashima match: 0.01/0.98 mid 49.5%, model 56.2% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25GRINAK-1-GRI` Will Tallon Griekspoor win set 1 in the Tallon Griekspoor vs Brandon Nakashima match: 0.01/0.98 mid 49.5%, model 43.8% (projection_v2.0 (prediction ledger)) -- gap -5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25GRINAK-2-GRI` Will Tallon Griekspoor win set 2 in the Tallon Griekspoor vs Brandon Nakashima match: 0.01/0.98 mid 49.5%, model 43.8% (projection_v2.0 (prediction ledger)) -- gap -5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Harri Heliovaara / Henry Patten vs Austin Krajicek / Nikola Mektic -- ATP Vienna R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25HELPATKRAMEK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harri Heliovaara / Henry Patten (`KXATPDOUBLES-26OCT25HELPATKRAMEK-HELPAT`) | 0.05 / 0.95 (6) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Austin Krajicek / Nikola Mektic (`KXATPDOUBLES-26OCT25HELPATKRAMEK-KRAMEK`) | 0.05 / 0.95 (6) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rinky Hijikata vs Yannick Hanfmann -- ATP Basel Q3

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-25T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25HIJHAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yannick Hanfmann (`KXATPMATCH-26OCT25HIJHAN-HAN`) | 0.24 / 0.75 (5) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rinky Hijikata (`KXATPMATCH-26OCT25HIJHAN-HIJ`) | 0.07 / 0.91 (30) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hubert Hurkacz vs Arthur Fils -- ATP Basel R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25HURFIL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fils (`KXATPMATCH-26OCT25HURFIL-FIL`) | 0.52 / 0.93 (45) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hubert Hurkacz (`KXATPMATCH-26OCT25HURFIL-HUR`) | 0.06 / 0.77 (30) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Karen Khachanov vs Carlos Alcaraz -- ATP Vienna R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25KHAALC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlos Alcaraz (`KXATPMATCH-26OCT25KHAALC-ALC`) | 0.70 / 0.89 (39) | 79.5% | 85.0% | -- | -- [-----] | -- | -- | -- | -- | -- | +5.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Karen Khachanov (`KXATPMATCH-26OCT25KHAALC-KHA`) | 0.10 / 0.49 (30) | 29.5% | 15.0% | -- | -- [-----] | -- | -- | -- | -- | -- | -14.5 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 58.1%, B 33.7%; Elo A 1929.2, B 2344.6; model uncertainty None
* Form inputs: days since last match A 1, B 12; matches on record A 764, B 476; data quality A
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT25KHAALC-1-ALC` Will Carlos Alcaraz win set 1 in the Karen Khachanov vs Carlos Alcaraz match: 0.01/0.98 mid 49.5%, model 75.6% (projection_v2.0 (prediction ledger)) -- gap +26.1 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25KHAALC-2-ALC` Will Carlos Alcaraz win set 2 in the Karen Khachanov vs Carlos Alcaraz match: 0.01/0.98 mid 49.5%, model 75.6% (projection_v2.0 (prediction ledger)) -- gap +26.1 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25KHAALC-1-KHA` Will Karen Khachanov win set 1 in the Karen Khachanov vs Carlos Alcaraz match: 0.01/0.98 mid 49.5%, model 24.4% (projection_v2.0 (prediction ledger)) -- gap -25.1 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25KHAALC-2-KHA` Will Karen Khachanov win set 2 in the Karen Khachanov vs Carlos Alcaraz match: 0.01/0.98 mid 49.5%, model 24.4% (projection_v2.0 (prediction ledger)) -- gap -25.1 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Kevin Krawietz / Tim Putz vs Jakob Schnaitter / Mark Wallner -- ATP Basel R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25KRAPUTSCHWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kevin Krawietz / Tim Putz (`KXATPDOUBLES-26OCT25KRAPUTSCHWAL-KRAPUT`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jakob Schnaitter / Mark Wallner (`KXATPDOUBLES-26OCT25KRAPUTSCHWAL-SCHWAL`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jerome Kym vs Arthur Rinderknech -- ATP Basel R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25KYMRIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jerome Kym (`KXATPMATCH-26OCT25KYMRIN-KYM`) | 0.22 / 0.42 (1) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arthur Rinderknech (`KXATPMATCH-26OCT25KYMRIN-RIN`) | 0.43 / 0.86 (3) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Orlando Luz / Rafael Matos vs Christian Harrison / Neal Skupski -- ATP Vienna R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25LUZMATHARSKU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Christian Harrison / Neal Skupski (`KXATPDOUBLES-26OCT25LUZMATHARSKU-HARSKU`) | 0.05 / 0.95 (146) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Orlando Luz / Rafael Matos (`KXATPDOUBLES-26OCT25LUZMATHARSKU-LUZMAT`) | 0.05 / 0.95 (146) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Daniel Merida vs Daniil Medvedev -- ATP Vienna R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25MERMED:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniil Medvedev (`KXATPMATCH-26OCT25MERMED-MED`) | 0.74 / 0.83 (37) | 78.5% | 64.5% | -- | -- [-----] | -- | -- | -- | -- | -- | -14.0 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Daniel Merida (`KXATPMATCH-26OCT25MERMED-MER`) | 0.15 / 0.56 (30) | 35.5% | 35.5% | -- | -- [-----] | -- | -- | -- | -- | -- | +0.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 57.8%, B 39.4%; Elo A 1827.4, B 1931.0; model uncertainty None
* Form inputs: days since last match A 16, B 1; matches on record A 355, B 873; data quality A
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT25MERMED-1-MED` Will Daniil Medvedev win set 1 in the Daniel Merida vs Daniil Medvedev match: 0.01/0.98 mid 49.5%, model 59.8% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25MERMED-2-MED` Will Daniil Medvedev win set 2 in the Daniel Merida vs Daniil Medvedev match: 0.01/0.98 mid 49.5%, model 59.8% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25MERMED-1-MER` Will Daniel Merida win set 1 in the Daniel Merida vs Daniil Medvedev match: 0.01/0.98 mid 49.5%, model 40.2% (projection_v2.0 (prediction ledger)) -- gap -9.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25MERMED-2-MER` Will Daniel Merida win set 2 in the Daniel Merida vs Daniil Medvedev match: 0.01/0.98 mid 49.5%, model 40.2% (projection_v2.0 (prediction ledger)) -- gap -9.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Alex Michelsen vs Botic Van de Zandschulp -- ATP Basel R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25MICVAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Michelsen (`KXATPMATCH-26OCT25MICVAN-MIC`) | 0.52 / 0.94 (222) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Botic Van de Zandschulp (`KXATPMATCH-26OCT25MICVAN-VAN`) | 0.06 / 0.77 (30) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Lucas Miedler / Neil Oberleitner vs Petr Nouza / Michael Venus -- ATP Vienna R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25MIEOBENOUVEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26OCT25MIEOBENOUVEN-MIEOBE`) | 0.05 / 0.95 (6) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Petr Nouza / Michael Venus (`KXATPDOUBLES-26OCT25MIEOBENOUVEN-NOUVEN`) | 0.05 / 0.95 (6) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lorenzo Musetti vs Frances Tiafoe -- ATP Vienna R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25MUSTIA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Musetti (`KXATPMATCH-26OCT25MUSTIA-MUS`) | 0.26 / 0.56 (1) | 41.0% | 65.0% | -- | -- [-----] | -- | -- | -- | -- | -- | +24.0 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Frances Tiafoe (`KXATPMATCH-26OCT25MUSTIA-TIA`) | 0.27 / 0.78 (56) | 52.5% | 35.0% | -- | -- [-----] | -- | -- | -- | -- | -- | -17.5 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 64.8%, B 38.3%; Elo A 2117.5, B 1923.5; model uncertainty None
* Form inputs: days since last match A 1, B 13; matches on record A 486, B 715; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT25MUSTIA-MUS  (YES = Lorenzo Musetti)
Model: 65%
Kalshi: 41%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, EVENT_MAPPING_RISK, NO_EXTERNAL_REFERENCE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT25MUSTIA-1-MUS` Will Lorenzo Musetti win set 1 in the Lorenzo Musetti vs Frances Tiafoe match: 0.01/0.98 mid 49.5%, model 60.2% (projection_v2.0 (prediction ledger)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25MUSTIA-2-MUS` Will Lorenzo Musetti win set 2 in the Lorenzo Musetti vs Frances Tiafoe match: 0.01/0.98 mid 49.5%, model 60.2% (projection_v2.0 (prediction ledger)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25MUSTIA-1-TIA` Will Frances Tiafoe win set 1 in the Lorenzo Musetti vs Frances Tiafoe match: 0.01/0.98 mid 49.5%, model 39.8% (projection_v2.0 (prediction ledger)) -- gap -9.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25MUSTIA-2-TIA` Will Frances Tiafoe win set 2 in the Lorenzo Musetti vs Frances Tiafoe match: 0.01/0.98 mid 49.5%, model 39.8% (projection_v2.0 (prediction ledger)) -- gap -9.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mariano Navone / Alejandro Tabilo vs Constantin Frantzen / Robin Haase -- ATP Basel R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25NAVTABFRAHAA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Constantin Frantzen / Robin Haase (`KXATPDOUBLES-26OCT25NAVTABFRAHAA-FRAHAA`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mariano Navone / Alejandro Tabilo (`KXATPDOUBLES-26OCT25NAVTABFRAHAA-NAVTAB`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Cameron Norrie vs Francisco Cerundolo -- ATP Vienna R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25NORCER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cerundolo (`KXATPMATCH-26OCT25NORCER-CER`) | 0.57 / 0.81 (7) | 69.0% | 74.8% | -- | -- [-----] | -- | -- | -- | -- | -- | +5.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Cameron Norrie (`KXATPMATCH-26OCT25NORCER-NOR`) | 0.19 / 0.77 (37) | 48.0% | 25.2% | -- | -- [-----] | -- | -- | -- | -- | -- | -22.8 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 57.9%, B 37.0%; Elo A 1882.6, B 2026.1; model uncertainty None
* Form inputs: days since last match A 4, B 1; matches on record A 677, B 562; data quality A
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT25NORCER-1-CER` Will Francisco Cerundolo win set 1 in the Cameron Norrie vs Francisco Cerundolo match: 0.01/0.98 mid 49.5%, model 67.2% (projection_v2.0 (prediction ledger)) -- gap +17.7 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25NORCER-2-CER` Will Francisco Cerundolo win set 2 in the Cameron Norrie vs Francisco Cerundolo match: 0.01/0.98 mid 49.5%, model 67.2% (projection_v2.0 (prediction ledger)) -- gap +17.7 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25NORCER-1-NOR` Will Cameron Norrie win set 1 in the Cameron Norrie vs Francisco Cerundolo match: 0.01/0.98 mid 49.5%, model 32.8% (projection_v2.0 (prediction ledger)) -- gap -16.7 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25NORCER-2-NOR` Will Cameron Norrie win set 2 in the Cameron Norrie vs Francisco Cerundolo match: 0.01/0.98 mid 49.5%, model 32.8% (projection_v2.0 (prediction ledger)) -- gap -16.7 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hugo Nys / Edouard Roger-Vasselin vs Theo Arribage / Albano Olivetti -- ATP Basel R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25NYSROGARROLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26OCT25NYSROGARROLI-ARROLI`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hugo Nys / Edouard Roger-Vasselin (`KXATPDOUBLES-26OCT25NYSROGARROLI-NYSROG`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Tommy Paul vs Andrey Rublev -- ATP Vienna R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25PAURUB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tommy Paul (`KXATPMATCH-26OCT25PAURUB-PAU`) | 0.29 / 0.80 (13) | 54.5% | 59.3% | -- | -- [-----] | -- | -- | -- | -- | -- | +4.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Andrey Rublev (`KXATPMATCH-26OCT25PAURUB-RUB`) | 0.20 / 0.73 (6) | 46.5% | 40.7% | -- | -- [-----] | -- | -- | -- | -- | -- | -5.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 64.5%, B 37.4%; Elo A 2000.6, B 1948.9; model uncertainty None
* Form inputs: days since last match A 1, B 3; matches on record A 728, B 835; data quality A
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT25PAURUB-1-PAU` Will Tommy Paul win set 1 in the Tommy Paul vs Andrey Rublev match: 0.01/0.98 mid 49.5%, model 56.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25PAURUB-2-PAU` Will Tommy Paul win set 2 in the Tommy Paul vs Andrey Rublev match: 0.01/0.98 mid 49.5%, model 56.2% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25PAURUB-1-RUB` Will Andrey Rublev win set 1 in the Tommy Paul vs Andrey Rublev match: 0.01/0.98 mid 49.5%, model 43.8% (projection_v2.0 (prediction ledger)) -- gap -5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25PAURUB-2-RUB` Will Andrey Rublev win set 2 in the Tommy Paul vs Andrey Rublev match: 0.01/0.98 mid 49.5%, model 43.8% (projection_v2.0 (prediction ledger)) -- gap -5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jakub Paul / Matej Vocel vs Alex Michelsen / Botic Van de Zandschulp -- ATP Basel R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25PAUVOCMICVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Michelsen / Botic Van de Zandschulp (`KXATPDOUBLES-26OCT25PAUVOCMICVAN-MICVAN`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jakub Paul / Matej Vocel (`KXATPDOUBLES-26OCT25PAUVOCMICVAN-PAUVOC`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Adam Pavlasek / Patrik Rikl vs Julian Cash / Lloyd Glasspool -- ATP Basel R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25PAVRIKCASGLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julian Cash / Lloyd Glasspool (`KXATPDOUBLES-26OCT25PAVRIKCASGLA-CASGLA`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Adam Pavlasek / Patrik Rikl (`KXATPDOUBLES-26OCT25PAVRIKCASGLA-PAVRIK`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jurij Rodionov vs Nikoloz Basilashvili -- ATP Vienna R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25RODBAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikoloz Basilashvili (`KXATPMATCH-26OCT25RODBAS-BAS`) | 0.50 / 0.80 (5) | 65.0% | 47.0% | -- | -- [-----] | -- | -- | -- | -- | -- | -18.0 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Jurij Rodionov (`KXATPMATCH-26OCT25RODBAS-ROD`) | 0.20 / 0.77 (30) | 48.5% | 53.0% | -- | -- [-----] | -- | -- | -- | -- | -- | +4.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 62.7%, B 37.9%; Elo A 1688.6, B 1757.7; model uncertainty None
* Form inputs: days since last match A 6, B 1; matches on record A 612, B 965; data quality A
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT25RODBAS-1-ROD` Will Jurij Rodionov win set 1 in the Jurij Rodionov vs Nikoloz Basilashvili match: 0.01/0.98 mid 49.5%, model 52.0% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25RODBAS-2-ROD` Will Jurij Rodionov win set 2 in the Jurij Rodionov vs Nikoloz Basilashvili match: 0.01/0.98 mid 49.5%, model 52.0% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25RODBAS-1-BAS` Will Nikoloz Basilashvili win set 1 in the Jurij Rodionov vs Nikoloz Basilashvili match: 0.01/0.98 mid 49.5%, model 48.0% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25RODBAS-2-BAS` Will Nikoloz Basilashvili win set 2 in the Jurij Rodionov vs Nikoloz Basilashvili match: 0.01/0.98 mid 49.5%, model 48.0% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Holger Rune vs Quentin Halys -- ATP Basel R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25RUNHAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Quentin Halys (`KXATPMATCH-26OCT25RUNHAL-HAL`) | 0.25 / 0.76 (5) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Holger Rune (`KXATPMATCH-26OCT25RUNHAL-RUN`) | 0.10 / 0.94 (200) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ryan Seggerman / Learner Tien vs Lukas Neumayer / Jurij Rodionov -- ATP Vienna R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25SEGTIENEUROD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lukas Neumayer / Jurij Rodionov (`KXATPDOUBLES-26OCT25SEGTIENEUROD-NEUROD`) | 0.05 / 0.95 (6) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ryan Seggerman / Learner Tien (`KXATPDOUBLES-26OCT25SEGTIENEUROD-SEGTIE`) | 0.05 / 0.95 (6) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ben Shelton vs Casper Ruud -- ATP Basel R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25SHERUU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Casper Ruud (`KXATPMATCH-26OCT25SHERUU-RUU`) | 0.12 / 0.41 (1) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ben Shelton (`KXATPMATCH-26OCT25SHERUU-SHE`) | 0.23 / 0.93 (57) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dominic Stricker vs Alexander Bublik -- ATP Basel R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25STRBUB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Bublik (`KXATPMATCH-26OCT25STRBUB-BUB`) | 0.66 / 0.93 (45) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dominic Stricker (`KXATPMATCH-26OCT25STRBUB-STR`) | 0.06 / 0.77 (30) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Alejandro Tabilo vs Rafael Jodar -- ATP Basel R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25TABJOD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael Jodar (`KXATPMATCH-26OCT25TABJOD-JOD`) | 0.70 / 0.94 (222) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alejandro Tabilo (`KXATPMATCH-26OCT25TABJOD-TAB`) | 0.06 / 0.67 (30) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Valentin Vacherot vs Mariano Navone -- ATP Basel R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25VACNAV:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariano Navone (`KXATPMATCH-26OCT25VACNAV-NAV`) | 0.20 / 0.49 (200) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Valentin Vacherot (`KXATPMATCH-26OCT25VACNAV-VAC`) | 0.51 / 0.93 (2) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Luca Van Assche vs Learner Tien -- ATP Vienna R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25VANTIE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Learner Tien (`KXATPMATCH-26OCT25VANTIE-TIE`) | 0.65 / 0.94 (222) | 79.5% | 58.6% | -- | -- [-----] | -- | -- | -- | -- | -- | -20.9 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Luca Van Assche (`KXATPMATCH-26OCT25VANTIE-VAN`) | 0.06 / 0.54 (30) | 30.0% | 41.4% | -- | -- [-----] | -- | -- | -- | -- | -- | +11.4 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 57.1%, B 41.3%; Elo A 1816.2, B 1796.2; model uncertainty None
* Form inputs: days since last match A 1, B 12; matches on record A 393, B 249; data quality A
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT25VANTIE-1-TIE` Will Learner Tien win set 1 in the Luca Van Assche vs Learner Tien match: 0.01/0.98 mid 49.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25VANTIE-2-TIE` Will Learner Tien win set 2 in the Luca Van Assche vs Learner Tien match: 0.01/0.98 mid 49.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25VANTIE-1-VAN` Will Luca Van Assche win set 1 in the Luca Van Assche vs Learner Tien match: 0.01/0.98 mid 49.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT25VANTIE-2-VAN` Will Luca Van Assche win set 2 in the Luca Van Assche vs Learner Tien match: 0.01/0.98 mid 49.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Stan Wawrinka vs Jiri Lehecka -- ATP Basel R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25WAWLEH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiri Lehecka (`KXATPMATCH-26OCT25WAWLEH-LEH`) | 0.78 / 0.93 (44) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stan Wawrinka (`KXATPMATCH-26OCT25WAWLEH-WAW`) | 0.06 / 0.52 (30) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Alexander Zverev vs Martin Landaluce -- ATP Vienna R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-25 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-26T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (TOUR_500_250) · Clay · scheduled 2026-10-25T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT25ZVELAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Landaluce (`KXATPMATCH-26OCT25ZVELAN-LAN`) | 0.06 / 0.20 (4) | 13.0% | 7.6% | -- | -- [-----] | -- | -- | -- | -- | -- | -5.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Alexander Zverev (`KXATPMATCH-26OCT25ZVELAN-ZVE`) | 0.51 / 0.94 (200) | 72.5% | 92.3% | -- | -- [-----] | -- | -- | -- | -- | -- | +19.9 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 69.5%, B 42.0%; Elo A 2162.9, B 1721.8; model uncertainty None
* Form inputs: days since last match A 7, B 179; matches on record A 937, B 210; data quality B

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT25ZVELAN-ZVE  (YES = Alexander Zverev)
Model: 92%
Kalshi: 72%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26OCT25ZVELAN-1-ZVE` Will Alexander Zverev win set 1 in the Alexander Zverev vs Martin Landaluce match: 0.01/0.98 mid 49.5%, model 83.0% (projection_v2.0 (prediction ledger)) -- gap +33.5 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT25ZVELAN-2-ZVE` Will Alexander Zverev win set 2 in the Alexander Zverev vs Martin Landaluce match: 0.01/0.98 mid 49.5%, model 83.0% (projection_v2.0 (prediction ledger)) -- gap +33.5 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT25ZVELAN-1-LAN` Will Martin Landaluce win set 1 in the Alexander Zverev vs Martin Landaluce match: 0.01/0.98 mid 49.5%, model 17.0% (projection_v2.0 (prediction ledger)) -- gap -32.5 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26OCT25ZVELAN-2-LAN` Will Martin Landaluce win set 2 in the Alexander Zverev vs Martin Landaluce match: 0.01/0.98 mid 49.5%, model 17.0% (projection_v2.0 (prediction ledger)) -- gap -32.5 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Julian Cash / Lloyd Glasspool vs Theo Arribage / Albano Olivetti -- ATP Lyon F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-25 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-24 12:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-25T04:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-25T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT25CASGLAARROLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26OCT25CASGLAARROLI-ARROLI`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Julian Cash / Lloyd Glasspool (`KXATPDOUBLES-26OCT25CASGLAARROLI-CASGLA`) | 0.05 / 0.95 (156) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
