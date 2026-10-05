# ASSISTED SLATE -- 2026-10-05T12:38Z (`SL-20261005T123800Z-532f9be3`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

209 open matches not seen started, 716 markets. Skipped: {"first_ball_already_observed": 9, "scheduled_start_over_24h_past": 5, "no_match_winner_listed": 2}. Sources: shadow board 2026-10-05T06:13:41.544143+00:00, Model 4 2026-10-04T21:57:13.668537+00:00, Gen-1 ledger 2026-10-05T06:13:38.064252+00:00, external 2026-10-05T12:18:43.557977+00:00, capture 20261005T121426Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-06 03:00Z**
* Recommended RUN TENNIS time: **2026-10-06 02:15Z**
* Final price/status check time: **2026-10-06 02:50Z**
* Number of matches in window: 6 (Daria Snigur vs Mirra Andreeva, Aziz Dougaz vs Federico Cina, Liam Draxl vs Nikoloz Basilashvili, Roman Safiullin vs Shintaro Mochizuki, Bernard Tomic vs Timofey Skatov, Linda Noskova vs Ekaterina Alexandrova)

* **24 main-tour match(es) have NO verified start status** (START_UNKNOWN, STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-10-05T12:38Z. Refresh due by: 2026-10-06 02:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 50, "HIGH_REVIEW": 42, "NORMAL": 80, "REVIEW": 31, "UNPRICED": 513}; match winners: {"EXTREME": 50, "HIGH_REVIEW": 41, "NORMAL": 74, "REVIEW": 28, "UNPRICED": 225}; quote freshness at build: {"AGING": 137, "STALE": 66}.

## Alexandra Shubladze vs Tyra Caterina Grant -- WTA 125K Suzhou R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-05 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

WTA125 (WTA_125) · Hard · scheduled 2026-10-05T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:260168:261972:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tyra Caterina Grant (`KXWTACHALLENGERMATCH-26OCT04SHUGRA-GRA`) | 0.41 / 0.45 (501) | 43.0% | -- | 19.4% | 31.6% [25.4%-44.7%] | -- | -- | -- | -- | PASS | -11.3 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexandra Shubladze (`KXWTACHALLENGERMATCH-26OCT04SHUGRA-SHU`) | 0.55 / 0.57 (23) | 56.0% | -- | 80.5% | 68.3% [55.3%-74.6%] | -- | -- | -- | -- | WATCH | +12.3 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3247.0, B 2460.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0967
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose +0.004, surface_dev_tight +0.000
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE

## Hugo Grenier vs Georgii Kravchenko -- ATP Challenger Villena Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-05T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126409:206662:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Grenier (`KXATPCHALLENGERMATCH-26OCT05GREKRA-GRE`) | 0.03 / 0.04 (100) | 3.5% | 60.7% | 41.4% | 53.0% [48.0%-59.5%] | -- | -- | -- | -- | PASS | +49.5 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Georgii Kravchenko (`KXATPCHALLENGERMATCH-26OCT05GREKRA-KRA`) | 0.96 / 0.98 (4775) | 97.0% | 39.3% | 58.6% | 47.0% [40.5%-52.0%] | -- | -- | -- | -- | SHADOW_BET | -50.0 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4799.0, B 3617.0; serve-point win A 63.7%, B 38.5%; Elo A 1658.2, B 1447.0; model uncertainty 0.0578
* Form inputs: days since last match A 14, B 28; matches on record A 946, B 408; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT05GREKRA-GRE  (YES = Hugo Grenier)
Model: 53%
Kalshi: 4%
Gap: +50 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE

## Daniel Siniakov vs Yanaki Milev -- ATP Challenger Palermo Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209338:210200:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yanaki Milev (`KXATPCHALLENGERMATCH-26OCT05SINMIL-MIL`) | 0.86 / 0.90 (26) | 88.0% | 33.3% | 20.4% | 29.5% [23.9%-38.2%] | -- | -- | -- | -- | PASS | -58.5 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniel Siniakov (`KXATPCHALLENGERMATCH-26OCT05SINMIL-SIN`) | 0.09 / 0.13 (275) | 11.0% | 66.7% | 79.6% | 70.5% [61.8%-76.1%] | -- | -- | -- | -- | WATCH | +59.5 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2055.0, B 3208.0; serve-point win A 61.6%, B 41.8%; Elo A 1422.2, B 1382.6; model uncertainty 0.0714
* Form inputs: days since last match A 28, B 35; matches on record A 135, B 230; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT05SINMIL-SIN  (YES = Daniel Siniakov)
Model: 70%
Kalshi: 11%
Gap: +59 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.009, surface_dev_loose +0.009, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Coco Gauff vs Xinran Sun -- WTA Beijing R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-05 06:00Z
* Current expected start: 2026-10-05 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-05 11:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+390_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-05T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT04GAUSUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coco Gauff (`KXWTAMATCH-26OCT04GAUSUN-GAU`) | 0.92 / 0.93 (27574) | 92.5% | -- | -- | -- [-----] | 92.0% | 93.1% | 92.5% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xinran Sun (`KXWTAMATCH-26OCT04GAUSUN-SUN`) | 0.07 / 0.08 (13066) | 7.5% | -- | -- | -- [-----] | 8.0% | 7.4% | 7.7% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE

## Dominika Salkova vs Himeno Sakatsume -- WTA 125K Samsun R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-05 13:20Z
* Current expected start: 2026-10-05 12:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-05 11:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · surface ? · scheduled 2026-10-05T13:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT05SALSAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Himeno Sakatsume (`KXWTACHALLENGERMATCH-26OCT05SALSAK-SAK`) | 0.52 / 0.53 (3692) | 52.5% | -- | -- | -- [-----] | 53.1% | 52.8% | 52.9% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dominika Salkova (`KXWTACHALLENGERMATCH-26OCT05SALSAK-SAL`) | 0.47 / 0.48 (415) | 47.5% | -- | -- | -- [-----] | 46.9% | 47.4% | 47.2% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS

## Coleman Wong vs Cruz Hewitt -- ATP Shanghai Q1

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-05 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-05 12:32Z
* Source: COURT_PROGRESSION: preceding match on Stadium Court in progress (set 3 of best-of-5); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-05 11:47Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-05T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:209409:213178:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cruz Hewitt (`KXATPMATCH-26OCT05WONHEW-HEW`) | 0.19 / 0.20 (6220) | 19.5% | -- | 25.2% | 22.6% [21.1%-23.3%] | -- | 18.9% | 18.9% | MODEL_LONE_OUTLIER | PASS | +3.1 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Coleman Wong (`KXATPMATCH-26OCT05WONHEW-WON`) | 0.80 / 0.81 (10410) | 80.5% | -- | 74.8% | 77.4% [76.7%-78.9%] | -- | 81.0% | 81.0% | MODEL_LONE_OUTLIER | PASS | -3.1 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 6632.0, B 2741.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.011
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGSPREAD-26OCT05WONHEW-WON8` Will Coleman Wong win at least 7.5 more games than Cruz Hewitt?: 0.03/0.37 mid 20.0%, model 4.3% (market_conditioned_v1 (model4_board_v1)) -- gap -15.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT05WONHEW-17` Over 16.5 games: 0.65/0.98 mid 81.5%, model 96.0% (market_conditioned_v1 (model4_board_v1)) -- gap +14.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT05WONHEW-22` Over 21.5 games: 0.47/0.49 mid 48.0%, model 62.3% (market_conditioned_v1 (model4_board_v1)) -- gap +14.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT05WONHEW-27` Over 26.5 games: 0.06/0.44 mid 25.0%, model 37.7% (market_conditioned_v1 (model4_board_v1)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT05WONHEW-WON5` Will Coleman Wong win at least 4.5 more games than Cruz Hewitt?: 0.43/0.46 mid 44.5%, model 35.2% (market_conditioned_v1 (model4_board_v1)) -- gap -9.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT05WONHEW-WON21` Will Coleman Wong win the Coleman Wong vs Cruz Hewitt match by a set score of 2-1?: 0.21/0.22 mid 21.5%, model 29.4% (market_conditioned_v1 (model4_board_v1)) -- gap +7.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT05WONHEW-WON20` Will Coleman Wong win the Coleman Wong vs Cruz Hewitt match by a set score of 2-0?: 0.55/0.57 mid 56.0%, model 48.8% (market_conditioned_v1 (model4_board_v1)) -- gap -7.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT05WONHEW-WON2` Will Coleman Wong win at least 1.5 more games than Cruz Hewitt?: 0.53/0.82 mid 67.5%, model 72.1% (market_conditioned_v1 (model4_board_v1)) -- gap +4.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT05WONHEW-HEW21` Will Cruz Hewitt win the Coleman Wong vs Cruz Hewitt match by a set score of 2-1?: 0.08/0.11 mid 9.5%, model 12.7% (market_conditioned_v1 (model4_board_v1)) -- gap +3.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT05WONHEW-HEW20` Will Cruz Hewitt win the Coleman Wong vs Cruz Hewitt match by a set score of 2-0?: 0.09/0.11 mid 10.0%, model 9.1% (market_conditioned_v1 (model4_board_v1)) -- gap -0.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; MODEL_ROW_STALE; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nicolas Barrientos vs Javier Barranco Cosano -- ATP Challenger Braga Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:104905:200266:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Barrientos (`KXATPCHALLENGERMATCH-26OCT05BARBAR2-BAR`) | 0.08 / 0.09 (60) | 8.5% | 41.4% | 51.0% | 39.2% [36.7%-42.7%] | 22.3% | -- | 22.3% | MODEL_LONE_OUTLIER | WATCH | +30.7 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Javier Barranco Cosano (`KXATPCHALLENGERMATCH-26OCT05BARBAR2-BAR2`) | 0.89 / 0.91 (148) | 90.0% | 58.6% | 49.0% | 60.8% [57.3%-63.3%] | 77.7% | -- | 77.7% | MODEL_LONE_OUTLIER | PASS | -29.2 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 637.0, B 3597.0; serve-point win A 59.1%, B 39.3%; Elo A 1514.0, B 1619.1; model uncertainty 0.0301
* Form inputs: days since last match A 160, B 49; matches on record A 555, B 666; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT05BARBAR2-BAR  (YES = Nicolas Barrientos)
Model: 39%
Kalshi: 8%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Hynek Barton vs Pyotr Nesterov -- ATP Challenger Villena Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-05T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05BARNES:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hynek Barton (`KXATPCHALLENGERMATCH-26OCT05BARNES-BAR`) | 0.58 / 0.59 (28075) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pyotr Nesterov (`KXATPCHALLENGERMATCH-26OCT05BARNES-NES`) | 0.41 / 0.42 (19038) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Matyas Cerny vs Dimitris Sakellaridis -- ATP Challenger Palermo Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210063:212029:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matyas Cerny (`KXATPCHALLENGERMATCH-26OCT05CERSAK-CER`) | 0.85 / 0.86 (29570) | 85.5% | 67.3% | 74.2% | 72.0% [66.8%-75.0%] | 62.5% | -- | 62.5% | MARKETS_AGREE | SHADOW_BET | -13.5 pp | REVIEW | AGING | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Dimitris Sakellaridis (`KXATPCHALLENGERMATCH-26OCT05CERSAK-SAK`) | 0.14 / 0.15 (30810) | 14.5% | 32.7% | 25.8% | 28.0% [25.0%-33.2%] | 37.5% | -- | 37.5% | MARKETS_AGREE | PASS | +13.5 pp | REVIEW | AGING | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 2034.0, B 4537.0; serve-point win A 61.6%, B 41.8%; Elo A 1427.2, B 1281.1; model uncertainty 0.0413
* Form inputs: days since last match A 70, B 70; matches on record A 106, B 154; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.022, surface_dev_loose +0.018, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Oleksii Krutykh vs Filip Pieczonka -- ATP Challenger Braga Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208071:210091:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oleksii Krutykh (`KXATPCHALLENGERMATCH-26OCT05KRUPIE-KRU`) | 0.62 / 0.64 (425) | 63.0% | 61.9% | 67.3% | 62.6% [61.6%-64.5%] | 51.0% | 51.2% | 51.1% | MODEL_LONE_OUTLIER | SHADOW_BET | -0.4 pp | NORMAL | AGING | B / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |
| Filip Pieczonka (`KXATPCHALLENGERMATCH-26OCT05KRUPIE-PIE`) | 0.36 / 0.37 (20) | 36.5% | 38.1% | 32.7% | 37.4% [35.5%-38.4%] | 49.0% | 49.1% | 49.0% | MODEL_LONE_OUTLIER | PASS | +0.9 pp | NORMAL | AGING | B / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 3866.0, B 1044.0; serve-point win A 61.1%, B 41.3%; Elo A 1489.1, B 1422.6; model uncertainty 0.0145
* Form inputs: days since last match A 42, B 21; matches on record A 531, B 79; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.010, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Christian Langmo vs Oleksandr Ovcharenko -- ATP Challenger Palermo Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132052:209191:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Christian Langmo (`KXATPCHALLENGERMATCH-26OCT05LANOVC-LAN`) | 0.06 / 0.07 (21338) | 6.5% | 35.4% | 32.8% | 33.2% [31.1%-37.3%] | -- | -- | -- | -- | PASS | +26.7 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oleksandr Ovcharenko (`KXATPCHALLENGERMATCH-26OCT05LANOVC-OVC`) | 0.93 / 0.94 (30927) | 93.5% | 64.6% | 67.2% | 66.8% [62.7%-69.0%] | -- | -- | -- | -- | PASS | -26.7 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4895.0, B 2396.0; serve-point win A 58.5%, B 38.7%; Elo A 1413.6, B 1532.0; model uncertainty 0.0315
* Form inputs: days since last match A 28, B 35; matches on record A 481, B 328; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT05LANOVC-LAN  (YES = Christian Langmo)
Model: 33%
Kalshi: 6%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.018, surface_dev_loose -0.005, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Filippo Moroni vs Ignacio Parisca Romera -- ATP Challenger Palermo Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208092:212306:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filippo Moroni (`KXATPCHALLENGERMATCH-26OCT05MORPAR-MOR`) | 0.46 / 0.51 (625) | 48.5% | 69.0% | 66.5% | 66.5% [64.5%-67.9%] | -- | 48.6% | 48.6% | MODEL_LONE_OUTLIER | PASS | +18.0 pp | HIGH_REVIEW (DATA_WARNING) | AGING | B / LIMITED | AGREES_WITH_KALSHI | AMBIGUOUS |
| Ignacio Parisca Romera (`KXATPCHALLENGERMATCH-26OCT05MORPAR-PAR`) | 0.49 / 0.53 (29) | 51.0% | 31.0% | 33.5% | 33.5% [32.1%-35.5%] | -- | 51.7% | 51.7% | MODEL_LONE_OUTLIER | PASS | -17.5 pp | HIGH_REVIEW (DATA_WARNING) | AGING | B / LIMITED | AGREES_WITH_KALSHI | AMBIGUOUS |

* Serve evidence (points): A 2040.0, B 2357.0; serve-point win A 61.8%, B 42.0%; Elo A 1499.3, B 1375.8; model uncertainty 0.0174
* Form inputs: days since last match A 161, B 140; matches on record A 112, B 97; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT05MORPAR-MOR  (YES = Filippo Moroni)
Model: 66%
Kalshi: 48%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: B (LIMITED)
Reasons: PLAYER_IDENTITY_RISK, STALE_PLAYER_DATA, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.005, surface_dev_loose -0.009, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Ryan Nijboer vs Benjamin Hassan -- ATP Challenger Braga Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 13:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133975:207764:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Hassan (`KXATPCHALLENGERMATCH-26OCT05NIJHAS-HAS`) | 0.15 / 0.16 (14330) | 15.5% | 62.3% | 51.0% | 57.1% [53.6%-63.6%] | 57.2% | 57.5% | 57.2% | MODEL_LONE_OUTLIER | PASS | +41.6 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Ryan Nijboer (`KXATPCHALLENGERMATCH-26OCT05NIJHAS-NIJ`) | 0.84 / 0.85 (4954) | 84.5% | 37.7% | 49.0% | 42.9% [36.4%-46.4%] | 42.8% | 42.3% | 42.8% | MODEL_LONE_OUTLIER | PASS | -41.6 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 4005.0, B 5302.0; serve-point win A 58.7%, B 38.9%; Elo A 1482.5, B 1645.2; model uncertainty 0.05
* Form inputs: days since last match A 14, B 14; matches on record A 484, B 672; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT05NIJHAS-HAS  (YES = Benjamin Hassan)
Model: 57%
Kalshi: 16%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_MODEL
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.020, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Philip Henning vs Ivan Marrero Curbelo -- ATP Challenger Villena Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-05T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202326:202475:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Philip Henning (`KXATPCHALLENGERMATCH-26OCT05HENMAR-HEN`) | 0.94 / 0.96 (19612) | 95.0% | 69.8% | 81.2% | 77.9% [75.1%-79.8%] | -- | 76.7% | 76.7% | MODEL_LONE_OUTLIER | PASS | -17.1 pp | HIGH_REVIEW | AGING | A / LIMITED | AGREES_WITH_MODEL | VERIFIED |
| Ivan Marrero Curbelo (`KXATPCHALLENGERMATCH-26OCT05HENMAR-MAR`) | 0.04 / 0.06 (10288) | 5.0% | 30.2% | 18.8% | 22.1% [20.2%-24.9%] | -- | 23.6% | 23.6% | MODEL_LONE_OUTLIER | PASS | +17.1 pp | HIGH_REVIEW | AGING | A / LIMITED | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 4250.0, B 3304.0; serve-point win A 64.6%, B 39.5%; Elo A 1622.3, B 1477.2; model uncertainty 0.0238
* Form inputs: days since last match A 63, B 28; matches on record A 212, B 224; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT05HENMAR-MAR  (YES = Ivan Marrero Curbelo)
Model: 22%
Kalshi: 5%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_MODEL
Data quality: A (LIMITED)
Reasons: STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.004, surface_dev_loose +0.015, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Max Hans Rehberg vs Mili Poljicak -- ATP Challenger Villena Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208819:209890:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mili Poljicak (`KXATPCHALLENGERMATCH-26OCT05REHPOL-POL`) | 0.70 / 0.71 (28475) | 70.5% | 43.8% | 37.0% | 38.4% [37.0%-40.2%] | 38.4% | 36.2% | 37.3% | MODEL_LONE_OUTLIER | PASS | -32.1 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Max Hans Rehberg (`KXATPCHALLENGERMATCH-26OCT05REHPOL-REH`) | 0.29 / 0.30 (33680) | 29.5% | 56.2% | 63.0% | 61.7% [59.8%-63.0%] | 61.6% | 64.4% | 63.0% | MODEL_LONE_OUTLIER | PASS | +32.1 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 4369.0, B 3989.0; serve-point win A 63.2%, B 38.0%; Elo A 1612.4, B 1548.4; model uncertainty 0.0162
* Form inputs: days since last match A 28, B 28; matches on record A 305, B 306; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT05REHPOL-REH  (YES = Max Hans Rehberg)
Model: 62%
Kalshi: 30%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_MODEL
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.014, surface_dev_loose +0.013, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Galena Krastenova vs Andzhelina Kostova -- W50 Burgas R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:265603:269682:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andzhelina Kostova (`KXITFWMATCH-26OCT05KRAKOS-KOS`) | 0.03 / 0.04 (8941) | 3.5% | 39.0% | 32.9% | 38.4% [36.3%-38.9%] | -- | -- | -- | -- | PASS | +34.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Galena Krastenova (`KXITFWMATCH-26OCT05KRAKOS-KRA`) | 0.96 / 0.97 (471) | 96.5% | 61.0% | 67.1% | 61.6% [61.1%-63.7%] | -- | -- | -- | -- | PASS | -34.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 135.0, B 121.0; serve-point win A 58.1%, B 44.0%; Elo A 1281.1, B 1203.6; model uncertainty 0.0129
* Form inputs: days since last match A 392, B 385; matches on record A 24, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05KRAKOS-KOS  (YES = Andzhelina Kostova)
Model: 38%
Kalshi: 4%
Gap: +35 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sophia Ksandinov vs Thea Marcu -- W15 Chisinau R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05KSAMAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sophia Ksandinov (`KXITFWMATCH-26OCT05KSAMAR-KSA`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thea Marcu (`KXITFWMATCH-26OCT05KSAMAR-MAR`) | -- / 0.01 (182462) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Noemi La Cagnina vs Maria Rentoumi -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222935:270259:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noemi La Cagnina (`KXITFWMATCH-26OCT05LACREN-LAC`) | 0.98 / 0.99 (316) | 98.5% | 50.3% | 34.4% | 48.9% [47.3%-50.0%] | -- | -- | -- | -- | PASS | -49.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Rentoumi (`KXITFWMATCH-26OCT05LACREN-REN`) | 0.01 / 0.02 (186) | 1.5% | 49.7% | 65.6% | 51.1% [50.0%-52.7%] | -- | -- | -- | -- | PASS | +49.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 289.0, B 149.0; serve-point win A 55.7%, B 44.3%; Elo A 1257.3, B 1255.5; model uncertainty 0.0134
* Form inputs: days since last match A 161, B 86; matches on record A 69, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05LACREN-REN  (YES = Maria Rentoumi)
Model: 51%
Kalshi: 2%
Gap: +50 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.011, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emma Mazzoni vs Cristina PESCUCCI -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220790:223094:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emma Mazzoni (`KXITFWMATCH-26OCT05MAZPES-MAZ`) | 0.42 / 0.48 (397) | 45.0% | 37.9% | 33.0% | 37.4% [36.4%-39.0%] | -- | -- | -- | -- | PASS | -7.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cristina PESCUCCI (`KXITFWMATCH-26OCT05MAZPES-PES`) | 0.54 / 0.58 (53) | 56.0% | 62.1% | 67.0% | 62.6% [61.1%-63.6%] | -- | -- | -- | -- | PASS | +6.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 168.0, B 112.0; serve-point win A 54.5%, B 43.1%; Elo A 1070.3, B 1156.4; model uncertainty 0.0128
* Form inputs: days since last match A 161, B 175; matches on record A 135, B 10; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.015, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diana-Ioana Simionescu vs Nicole Gadient -- W50 Burgas R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215712:264978:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicole Gadient (`KXITFWMATCH-26OCT05SIMGAD-GAD`) | -- / 0.01 (7516) | -- | 26.9% | 22.8% | 25.3% [22.0%-28.3%] | -- | -- | -- | -- | WATCH | -- | UNPRICED | STALE | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |
| Diana-Ioana Simionescu (`KXITFWMATCH-26OCT05SIMGAD-SIM`) | 0.99 / -- (0) | -- | 73.2% | 77.2% | 74.7% [71.7%-78.0%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 1418.0, B 918.0; serve-point win A 59.3%, B 45.3%; Elo A 1437.7, B 1270.3; model uncertainty 0.0314
* Form inputs: days since last match A 231, B 168; matches on record A 46, B 292; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Duje Ajdukovic vs Filip Cristian Jianu -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 14:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202262:207213:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Duje Ajdukovic (`KXATPCHALLENGERMATCH-26OCT05AJDJIA-AJD`) | 0.59 / 0.61 (10943) | 60.0% | 48.1% | 35.4% | 39.3% [36.8%-43.8%] | 57.2% | 59.4% | 58.3% | MODEL_LONE_OUTLIER | PASS | -20.7 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Filip Cristian Jianu (`KXATPCHALLENGERMATCH-26OCT05AJDJIA-JIA`) | 0.40 / 0.41 (3349) | 40.5% | 51.9% | 64.6% | 60.7% [56.2%-63.2%] | 42.8% | 41.0% | 41.9% | MODEL_LONE_OUTLIER | WATCH | +20.2 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5839.0, B 5523.0; serve-point win A 59.7%, B 39.9%; Elo A 1629.6, B 1599.3; model uncertainty 0.035
* Form inputs: days since last match A 28, B 14; matches on record A 594, B 710; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT05AJDJIA-JIA  (YES = Filip Cristian Jianu)
Model: 61%
Kalshi: 40%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Goncalo Marques vs Nikolas Sanchez Izquierdo -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 14:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149128:207663:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Goncalo Marques (`KXATPCHALLENGERMATCH-26OCT05MARSAI-MAR`) | 0.13 / 0.14 (4069) | 13.5% | 12.8% | 12.1% | 8.8% [8.1%-9.7%] | -- | 13.3% | 13.3% | MARKETS_AGREE | PASS | -4.7 pp | NORMAL | AGING | C / LIMITED | ALL_AGREE | VERIFIED |
| Nikolas Sanchez Izquierdo (`KXATPCHALLENGERMATCH-26OCT05MARSAI-SAI`) | 0.86 / 0.87 (2301) | 86.5% | 87.2% | 87.9% | 91.2% [90.3%-92.0%] | -- | 87.1% | -- | INSUFFICIENT_INPUTS | WATCH | +4.7 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 897.0, B 5721.0; serve-point win A 55.5%, B 35.7%; Elo A 1222.9, B 1668.1; model uncertainty 0.0083
* Form inputs: days since last match A 35, B 21; matches on record A 35, B 662; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.006, surface_dev_loose -0.006, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Zsombor Piros vs Tristan Boyer -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 14:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200436:207729:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tristan Boyer (`KXATPCHALLENGERMATCH-26OCT05PIRBOY-BOY`) | 0.19 / 0.22 (7189) | 20.5% | 37.4% | 31.8% | 33.2% [31.8%-35.5%] | 35.4% | -- | 35.4% | MODEL_LONE_OUTLIER | PASS | +12.7 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Zsombor Piros (`KXATPCHALLENGERMATCH-26OCT05PIRBOY-PIR`) | 0.77 / 0.81 (13363) | 79.0% | 62.6% | 68.2% | 66.8% [64.5%-68.2%] | 64.6% | -- | 64.6% | MODEL_LONE_OUTLIER | SHADOW_BET | -12.2 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 5933.0, B 4875.0; serve-point win A 61.1%, B 41.3%; Elo A 1797.0, B 1692.5; model uncertainty 0.0187
* Form inputs: days since last match A 34, B 21; matches on record A 675, B 326; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.009, surface_dev_loose +0.014, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Richard Antoni vs Cian Maguire -- M15 Burgas R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212825:213898:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Richard Antoni (`KXITFMATCH-26OCT05ANTMAG-ANT`) | 0.66 / 0.67 (236) | 66.5% | 58.6% | 51.0% | 57.2% [56.7%-58.3%] | -- | -- | -- | -- | PASS | -9.3 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cian Maguire (`KXITFMATCH-26OCT05ANTMAG-MAG`) | 0.32 / 0.33 (1) | 32.5% | 41.4% | 49.0% | 42.8% [41.7%-43.3%] | -- | -- | -- | -- | PASS | +10.3 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 717.0, B 311.0; serve-point win A 64.9%, B 36.9%; Elo A 1237.1, B 1176.7; model uncertainty 0.0078
* Form inputs: days since last match A 126, B 308; matches on record A 17, B 12; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maximilian Todorov vs Mihail Ivanov -- M15 Burgas R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208329:211605:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mihail Ivanov (`KXITFMATCH-26OCT05TODIVA-IVA`) | 0.99 / -- (0) | -- | 36.9% | 35.2% | 37.2% [35.6%-37.8%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Maximilian Todorov (`KXITFMATCH-26OCT05TODIVA-TOD`) | -- / 0.01 (173909) | -- | 63.1% | 64.8% | 62.8% [62.2%-64.4%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 115.0, B 222.0; serve-point win A 65.3%, B 37.3%; Elo A 1267.2, B 1173.7; model uncertainty 0.0111
* Form inputs: days since last match A 322, B 385; matches on record A 3, B 11; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Laura Boehner vs Angelica Sara -- W35 Seville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-05T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221258:267408:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laura Boehner (`KXITFWMATCH-26OCT05BOESAR-BOE`) | 0.99 / -- (0) | -- | 44.4% | 38.5% | 43.6% [41.0%-47.3%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Angelica Sara (`KXITFWMATCH-26OCT05BOESAR-SAR`) | -- / 0.01 (178140) | -- | 55.6% | 61.5% | 56.4% [52.7%-59.0%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 824.0, B 641.0; serve-point win A 53.5%, B 45.5%; Elo A 1298.6, B 1326.8; model uncertainty 0.0315
* Form inputs: days since last match A 175, B 329; matches on record A 221, B 26; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.016, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lilian Chidekh vs Romain Andres -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05CHIAND:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romain Andres (`KXITFMATCH-26OCT05CHIAND-AND`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lilian Chidekh (`KXITFMATCH-26OCT05CHIAND-CHI`) | 0.01 / 0.03 (11) | 2.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alex Kobelt vs Noah Malige -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05KOBMAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Kobelt (`KXITFMATCH-26OCT05KOBMAL-KOB`) | 0.86 / 0.87 (3838) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Noah Malige (`KXITFMATCH-26OCT05KOBMAL-MAL`) | 0.13 / 0.14 (6141) | 13.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dino Prizmic vs Jack Pinnington Jones -- ATP Challenger Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209957:209976:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Pinnington Jones (`KXATPCHALLENGERMATCH-26OCT05PRIPIN-PIN`) | 0.22 / 0.23 (32) | 22.5% | 24.1% | 26.9% | 25.2% [24.4%-26.5%] | 25.0% | 22.3% | 25.0% | KALSHI_LONE_OUTLIER | WATCH | +2.7 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Dino Prizmic (`KXATPCHALLENGERMATCH-26OCT05PRIPIN-PRI`) | 0.76 / 0.78 (5830) | 77.0% | 75.9% | 73.1% | 74.8% [73.5%-75.6%] | 75.0% | 77.0% | 76.0% | MARKETS_AGREE | PASS | -2.2 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4155.0, B 3466.0; serve-point win A 65.4%, B 40.2%; Elo A 1871.2, B 1650.3; model uncertainty 0.0103
* Form inputs: days since last match A 14, B 34; matches on record A 307, B 223; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Daniel Rincon vs Alejo Sanchez Quilez -- ATP Challenger Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209405:211639:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Rincon (`KXATPCHALLENGERMATCH-26OCT05RINSAN-RIN`) | 0.66 / 0.67 (3616) | 66.5% | 54.3% | 45.3% | 48.4% [45.9%-54.1%] | 64.6% | 65.8% | 65.2% | MODEL_LONE_OUTLIER | PASS | -18.1 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Alejo Sanchez Quilez (`KXATPCHALLENGERMATCH-26OCT05RINSAN-SAN`) | 0.33 / 0.34 (145) | 33.5% | 45.7% | 54.7% | 51.6% [45.9%-54.1%] | 35.4% | 34.5% | 35.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +18.1 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5943.0, B 3639.0; serve-point win A 63.0%, B 37.8%; Elo A 1617.2, B 1573.5; model uncertainty 0.0414
* Form inputs: days since last match A 14, B 21; matches on record A 422, B 187; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT05RINSAN-SAN  (YES = Alejo Sanchez Quilez)
Model: 52%
Kalshi: 34%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose -0.021, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Darrshan Suresh vs Mayank Sharma -- M25 Kigali R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05SURSHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mayank Sharma (`KXITFMATCH-26OCT05SURSHA-SHA`) | 0.47 / 0.48 (48) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Darrshan Suresh (`KXITFMATCH-26OCT05SURSHA-SUR`) | 0.51 / 0.52 (556) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ethan Terblanche vs Yash Chaurasia -- M25 Kigali R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208729:213562:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yash Chaurasia (`KXITFMATCH-26OCT05TERCHA-CHA`) | 0.97 / 0.98 (2761) | 97.5% | 38.0% | 50.5% | 38.7% [37.7%-38.8%] | -- | -- | -- | -- | PASS | -58.8 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ethan Terblanche (`KXITFMATCH-26OCT05TERCHA-TER`) | 0.02 / 0.03 (2866) | 2.5% | 62.0% | 49.5% | 61.3% [61.2%-62.3%] | -- | -- | -- | -- | PASS | +58.8 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 91.0, B 64.0; serve-point win A 61.1%, B 41.3%; Elo A 1187.4, B 1102.4; model uncertainty 0.0052
* Form inputs: days since last match A 154, B 140; matches on record A 3, B 23; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT05TERCHA-TER  (YES = Ethan Terblanche)
Model: 61%
Kalshi: 2%
Gap: +59 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giulia Safina Popa vs Anna Ozerova -- W50 Burgas R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216030:267428:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Ozerova (`KXITFWMATCH-26OCT05POPOZE-OZE`) | 0.05 / 0.17 (13) | 11.0% | 21.0% | 33.4% | 21.8% [21.0%-22.6%] | -- | -- | -- | -- | PASS | +10.8 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Giulia Safina Popa (`KXITFWMATCH-26OCT05POPOZE-POP`) | 0.59 / 0.94 (30) | 76.5% | 79.0% | 66.6% | 78.2% [77.4%-79.0%] | -- | -- | -- | -- | PASS | +1.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1013.0, B 140.0; serve-point win A 60.1%, B 46.1%; Elo A 1530.0, B 1300.1; model uncertainty 0.008
* Form inputs: days since last match A 371, B 392; matches on record A 38, B 165; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oana Georgeta Simion vs Sonja Zhenikhova -- W50 Burgas R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211646:264961:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oana Georgeta Simion (`KXITFWMATCH-26OCT05SIMZHE-SIM`) | 0.01 / 0.06 (119) | 3.5% | 59.7% | 55.9% | 60.0% [59.0%-62.1%] | -- | -- | -- | -- | PASS | +56.5 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sonja Zhenikhova (`KXITFWMATCH-26OCT05SIMZHE-ZHE`) | 0.99 / -- (0) | -- | 40.4% | 44.1% | 40.0% [37.9%-41.0%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 1762.0, B 1212.0; serve-point win A 57.9%, B 43.9%; Elo A 1501.4, B 1402.5; model uncertainty 0.0154
* Form inputs: days since last match A 182, B 224; matches on record A 543, B 38; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05SIMZHE-SIM  (YES = Oana Georgeta Simion)
Model: 60%
Kalshi: 4%
Gap: +57 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matei Florin Breazu vs Benedikt Szerencsits -- M15 Burgas R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149134:213902:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matei Florin Breazu (`KXITFMATCH-26OCT05BRESZE-BRE`) | 0.83 / 0.85 (595) | 84.0% | 52.4% | 61.3% | 53.1% [52.1%-56.2%] | -- | -- | -- | -- | PASS | -30.9 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Benedikt Szerencsits (`KXITFMATCH-26OCT05BRESZE-SZE`) | 0.14 / 0.15 (1) | 14.5% | 47.6% | 38.8% | 46.9% [43.8%-47.9%] | -- | -- | -- | -- | PASS | +32.4 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 571.0, B 184.0; serve-point win A 64.2%, B 36.2%; Elo A 1221.2, B 1204.7; model uncertainty 0.0206
* Form inputs: days since last match A 126, B 140; matches on record A 21, B 5; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT05BRESZE-SZE  (YES = Benedikt Szerencsits)
Model: 47%
Kalshi: 14%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vilius Gaubas vs Joao Domingues -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106249:209147:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Domingues (`KXATPCHALLENGERMATCH-26OCT05GAUDOM-DOM`) | 0.17 / 0.18 (4080) | 17.5% | 30.4% | 36.2% | 31.0% [28.8%-33.4%] | 18.8% | 18.8% | 18.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +13.5 pp | REVIEW | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Vilius Gaubas (`KXATPCHALLENGERMATCH-26OCT05GAUDOM-GAU`) | 0.82 / 0.83 (4099) | 82.5% | 69.6% | 63.8% | 69.0% [66.6%-71.2%] | 81.2% | 83.0% | 82.1% | MODEL_LONE_OUTLIER | PASS | -13.5 pp | REVIEW | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5548.0, B 3071.0; serve-point win A 61.9%, B 42.1%; Elo A 1745.8, B 1522.6; model uncertainty 0.0229
* Form inputs: days since last match A 28, B 79; matches on record A 367, B 842; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.009, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Maxim Khorozov vs Cezar Stefan Bentzel -- M15 Burgas R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05KHOBEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cezar Stefan Bentzel (`KXITFMATCH-26OCT05KHOBEN-BEN`) | 0.64 / 0.65 (448) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maxim Khorozov (`KXITFMATCH-26OCT05KHOBEN-KHO`) | 0.33 / 0.34 (1) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thiago Monteiro vs Elmer Moller -- ATP Challenger Braga R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106329:209284:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elmer Moller (`KXATPCHALLENGERMATCH-26OCT05MONMOL-MOL`) | 0.47 / 0.48 (288) | 47.5% | 46.2% | 45.4% | 45.9% [45.4%-46.9%] | 48.0% | 47.2% | 47.6% | MODEL_LONE_OUTLIER | PASS | -1.6 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Thiago Monteiro (`KXATPCHALLENGERMATCH-26OCT05MONMOL-MON`) | 0.52 / 0.53 (521) | 52.5% | 53.8% | 54.6% | 54.1% [53.1%-54.6%] | 52.0% | 53.5% | 52.8% | MODEL_LONE_OUTLIER | PASS | +1.6 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5678.0, B 4813.0; serve-point win A 60.3%, B 40.5%; Elo A 1743.6, B 1735.9; model uncertainty 0.0077
* Form inputs: days since last match A 14, B 34; matches on record A 1183, B 351; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Eleni Chatziavraam vs Lola Giza -- W50 Heraklion R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260503:269800:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eleni Chatziavraam (`KXITFWMATCH-26OCT05CHAGIZ-CHA`) | 0.01 / 0.02 (41028) | 1.5% | 38.5% | 13.6% | 34.9% [28.2%-38.4%] | -- | -- | -- | -- | PASS | +33.4 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lola Giza (`KXITFWMATCH-26OCT05CHAGIZ-GIZ`) | 0.98 / 0.99 (1212) | 98.5% | 61.5% | 86.4% | 65.1% [61.6%-71.8%] | -- | -- | -- | -- | PASS | -33.4 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 203.0, B 432.0; serve-point win A 54.6%, B 43.2%; Elo A 1168.6, B 1249.9; model uncertainty 0.051
* Form inputs: days since last match A 210, B 427; matches on record A 10, B 14; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05CHAGIZ-CHA  (YES = Eleni Chatziavraam)
Model: 35%
Kalshi: 2%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maayan Laron vs Maddalena Giordano -- W50 Heraklion R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220642:260224:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maddalena Giordano (`KXITFWMATCH-26OCT05LARGIO-GIO`) | 0.03 / 0.11 (6) | 7.0% | 20.5% | 9.3% | 17.7% [14.2%-23.2%] | -- | -- | -- | -- | WATCH | +10.7 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maayan Laron (`KXITFWMATCH-26OCT05LARGIO-LAR`) | 0.93 / 0.94 (6697) | 93.5% | 79.5% | 90.7% | 82.3% [76.8%-85.8%] | -- | -- | -- | -- | PASS | -11.2 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1019.0, B 1760.0; serve-point win A 58.8%, B 47.4%; Elo A 1357.6, B 1179.5; model uncertainty 0.0451
* Form inputs: days since last match A 161, B 161; matches on record A 28, B 144; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.021, surface_dev_loose +0.010, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Helena Muzinic vs Maria Eleni Poulka -- W50 Heraklion R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263887:266767:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Helena Muzinic (`KXITFWMATCH-26OCT05MUZPOU-MUZ`) | 0.35 / 0.36 (6335) | 35.5% | 44.6% | 50.0% | 44.7% [44.7%-44.7%] | -- | -- | -- | -- | PASS | +9.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maria Eleni Poulka (`KXITFWMATCH-26OCT05MUZPOU-POU`) | 0.64 / 0.65 (3258) | 64.5% | 55.4% | 50.0% | 55.3% [55.3%-55.3%] | -- | -- | -- | -- | PASS | -9.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 55.2%, B 43.8%; Elo A 1027.7, B 1065.0; model uncertainty 0.0
* Form inputs: days since last match A 763, B 693; matches on record A 19, B 18; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Nikolaidou vs Tilwith Di Girolami -- W50 Heraklion R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05NIKDIG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tilwith Di Girolami (`KXITFWMATCH-26OCT05NIKDIG-DIG`) | 0.95 / 0.98 (500) | 96.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofia Nikolaidou (`KXITFWMATCH-26OCT05NIKDIG-NIK`) | 0.02 / 0.04 (9731) | 3.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lilian Poling vs Kaat Coppez -- W35 Villeneuve d'Ascq R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221585:266467:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kaat Coppez (`KXITFWMATCH-26OCT05POLCOP-COP`) | 0.93 / 0.94 (2) | 93.5% | 62.4% | 80.5% | 63.2% [55.9%-69.5%] | -- | -- | -- | -- | WATCH | -30.3 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lilian Poling (`KXITFWMATCH-26OCT05POLCOP-POL`) | 0.05 / 0.07 (43816) | 6.0% | 37.6% | 19.5% | 36.8% [30.5%-44.1%] | -- | -- | -- | -- | PASS | +30.8 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1063.0, B 759.0; serve-point win A 54.5%, B 43.1%; Elo A 1276.4, B 1298.8; model uncertainty 0.0683
* Form inputs: days since last match A 161, B 161; matches on record A 93, B 70; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05POLCOP-POL  (YES = Lilian Poling)
Model: 37%
Kalshi: 6%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose -0.020, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marie Villet vs Charlotte CORA--BRUNETON -- W35 Villeneuve d'Ascq R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05VILCOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charlotte CORA--BRUNETON (`KXITFWMATCH-26OCT05VILCOR-COR`) | 0.30 / 0.31 (80) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marie Villet (`KXITFWMATCH-26OCT05VILCOR-VIL`) | 0.69 / 0.70 (91) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joaquin Aguilar Cardozo vs Lorenzo Joaquin Rodriguez -- ATP Challenger Antofagasta Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202271:212051:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joaquin Aguilar Cardozo (`KXATPCHALLENGERMATCH-26OCT05AGUROD-AGU`) | 0.86 / 0.87 (18239) | 86.5% | 50.8% | 54.2% | 53.1% [48.4%-54.7%] | 82.1% | 84.8% | 83.5% | KALSHI_LONE_OUTLIER | PASS | -33.4 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Lorenzo Joaquin Rodriguez (`KXATPCHALLENGERMATCH-26OCT05AGUROD-ROD`) | 0.13 / 0.14 (8291) | 13.5% | 49.2% | 45.8% | 46.9% [45.3%-51.6%] | 17.9% | 14.7% | 16.3% | KALSHI_LONE_OUTLIER | WATCH | +33.4 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2869.0, B 3486.0; serve-point win A 60.0%, B 40.2%; Elo A 1478.8, B 1465.3; model uncertainty 0.0314
* Form inputs: days since last match A 189, B 14; matches on record A 113, B 272; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT05AGUROD-ROD  (YES = Lorenzo Joaquin Rodriguez)
Model: 47%
Kalshi: 14%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.010, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Hernan Casanova vs Bernardo Munk Mesa -- ATP Challenger Antofagasta Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106292:212827:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hernan Casanova (`KXATPCHALLENGERMATCH-26OCT05CASMUN-CAS`) | 0.63 / 0.64 (5661) | 63.5% | 80.1% | 82.3% | 83.6% [82.9%-84.3%] | 63.8% | 63.7% | 63.7% | MODEL_LONE_OUTLIER | PASS | +20.1 pp | HIGH_REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Bernardo Munk Mesa (`KXATPCHALLENGERMATCH-26OCT05CASMUN-MUN`) | 0.36 / 0.37 (577) | 36.5% | 19.9% | 17.7% | 16.4% [15.7%-17.1%] | 36.2% | 36.5% | 36.4% | MODEL_LONE_OUTLIER | PASS | -20.1 pp | HIGH_REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4044.0, B 814.0; serve-point win A 63.2%, B 43.4%; Elo A 1596.9, B 1302.6; model uncertainty 0.0069
* Form inputs: days since last match A 91, B 273; matches on record A 911, B 18; data quality D

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT05CASMUN-CAS  (YES = Hernan Casanova)
Model: 84%
Kalshi: 64%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.003, surface_dev_loose +0.003, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Joao Eduardo Schiessl vs Alan Magadan -- ATP Challenger Antofagasta Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209246:210214:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alan Magadan (`KXATPCHALLENGERMATCH-26OCT05SCHMAG-MAG`) | 0.51 / 0.52 (1219) | 51.5% | 43.5% | 46.9% | 44.3% [42.3%-45.4%] | 52.0% | 50.6% | 52.0% | MODEL_LONE_OUTLIER | PASS | -7.2 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Joao Eduardo Schiessl (`KXATPCHALLENGERMATCH-26OCT05SCHMAG-SCH`) | 0.48 / 0.49 (234) | 48.5% | 56.5% | 53.1% | 55.7% [54.6%-57.7%] | 48.0% | 49.4% | 48.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.2 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3018.0, B 2744.0; serve-point win A 60.5%, B 40.7%; Elo A 1469.6, B 1392.8; model uncertainty 0.0153
* Form inputs: days since last match A 154, B 49; matches on record A 179, B 93; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Yasmine Kabbaj vs Neus Torner Sensano -- W35 Seville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:236956:269717:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yasmine Kabbaj (`KXITFWMATCH-26OCT05KABTOR-KAB`) | 0.78 / 0.79 (663) | 78.5% | 47.2% | 20.6% | 42.5% [31.9%-60.1%] | 72.4% | -- | 72.4% | MODEL_LONE_OUTLIER | PASS | -36.0 pp | EXTREME (DATA_WARNING) | AGING | B / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Neus Torner Sensano (`KXITFWMATCH-26OCT05KABTOR-TOR`) | 0.21 / 0.22 (1) | 21.5% | 52.8% | 79.4% | 57.5% [39.9%-68.1%] | 27.6% | -- | 27.6% | KALSHI_LONE_OUTLIER | WATCH | +36.0 pp | EXTREME (DATA_WARNING) | AGING | B / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 2651.0, B 1512.0; serve-point win A 53.7%, B 45.8%; Elo A 1617.8, B 1493.6; model uncertainty 0.1409
* Form inputs: days since last match A 16, B 22; matches on record A 185, B 40; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05KABTOR-TOR  (YES = Neus Torner Sensano)
Model: 57%
Kalshi: 22%
Gap: +36 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: B (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose -0.011, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katarina Kujovic vs Sana Garakani -- W35 Lagos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222309:268778:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sana Garakani (`KXITFWMATCH-26OCT05KUJGAR-GAR`) | 0.18 / 0.19 (120) | 18.5% | 33.1% | 54.3% | 36.4% [33.4%-38.9%] | -- | -- | -- | -- | PASS | +17.9 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katarina Kujovic (`KXITFWMATCH-26OCT05KUJGAR-KUJ`) | 0.81 / 0.82 (352) | 81.5% | 66.9% | 45.7% | 63.6% [61.1%-66.6%] | -- | -- | -- | -- | PASS | -17.9 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 711.0, B 335.0; serve-point win A 58.7%, B 44.7%; Elo A 1298.1, B 1175.8; model uncertainty 0.0275
* Form inputs: days since last match A 273, B 21; matches on record A 15, B 74; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05KUJGAR-GAR  (YES = Sana Garakani)
Model: 36%
Kalshi: 18%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefaniya Pushkar vs Elizabeth Jurna -- W35 Lagos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223374:265040:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elizabeth Jurna (`KXITFWMATCH-26OCT05PUSJUR-JUR`) | 0.81 / 0.85 (22) | 83.0% | 25.8% | 53.2% | 27.2% [26.2%-28.9%] | -- | -- | -- | -- | PASS | -55.8 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefaniya Pushkar (`KXITFWMATCH-26OCT05PUSJUR-PUS`) | 0.15 / 0.16 (1) | 15.5% | 74.2% | 46.8% | 72.8% [71.1%-73.9%] | -- | -- | -- | -- | PASS | +57.3 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 897.0, B 129.0; serve-point win A 59.5%, B 45.5%; Elo A 1302.1, B 1118.9; model uncertainty 0.0139
* Form inputs: days since last match A 161, B 161; matches on record A 23, B 89; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05PUSJUR-PUS  (YES = Stefaniya Pushkar)
Model: 73%
Kalshi: 16%
Gap: +57 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Moez Echargui vs Raul Brancaccio -- ATP Challenger Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 16:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-05T16:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:121411:134840:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raul Brancaccio (`KXATPCHALLENGERMATCH-26OCT05ECHBRA-BRA`) | 0.28 / 0.29 (68) | 28.5% | 47.7% | 54.6% | 51.5% [48.5%-52.6%] | -- | 27.8% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +23.0 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Moez Echargui (`KXATPCHALLENGERMATCH-26OCT05ECHBRA-ECH`) | 0.71 / 0.72 (6928) | 71.5% | 52.3% | 45.4% | 48.5% [47.4%-51.5%] | -- | 72.0% | -- | INSUFFICIENT_INPUTS | PASS | -23.0 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5190.0, B 6219.0; serve-point win A 62.8%, B 37.6%; Elo A 1598.1, B 1537.3; model uncertainty 0.0205
* Form inputs: days since last match A 14, B 14; matches on record A 704, B 773; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT05ECHBRA-BRA  (YES = Raul Brancaccio)
Model: 52%
Kalshi: 28%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Mateo Luis Alvarez Sarmiento vs Fermin Barcala Lopez -- M15 Pontevedra R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05ALVBAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateo Luis Alvarez Sarmiento (`KXITFMATCH-26OCT05ALVBAR-ALV`) | 0.93 / 0.97 (4824) | 95.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fermin Barcala Lopez (`KXITFMATCH-26OCT05ALVBAR-BAR`) | 0.04 / 0.05 (43) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luis Garcia Paez vs Ian Lucca Cervantes Tomas -- M15 Pontevedra R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212486:213037:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ian Lucca Cervantes Tomas (`KXITFMATCH-26OCT05GARCER-CER`) | 0.69 / 0.71 (2507) | 70.0% | 50.3% | 59.9% | 52.6% [51.0%-54.2%] | -- | -- | -- | -- | PASS | -17.4 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luis Garcia Paez (`KXITFMATCH-26OCT05GARCER-GAR`) | 0.29 / 0.31 (1688) | 30.0% | 49.7% | 40.1% | 47.4% [45.8%-48.9%] | -- | -- | -- | -- | PASS | +17.4 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1118.0, B 529.0; serve-point win A 62.6%, B 37.4%; Elo A 1159.3, B 1161.5; model uncertainty 0.0157
* Form inputs: days since last match A 140, B 378; matches on record A 32, B 24; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT05GARCER-GAR  (YES = Luis Garcia Paez)
Model: 47%
Kalshi: 30%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.011, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vasco Leote Prata vs Yannick Castelnuovo -- M15 Pontevedra R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211330:213314:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yannick Castelnuovo (`KXITFMATCH-26OCT05LEOCAS-CAS`) | 0.01 / 0.02 (2719) | 1.5% | 27.5% | 33.0% | 27.6% [26.4%-28.5%] | -- | -- | -- | -- | PASS | +26.1 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vasco Leote Prata (`KXITFMATCH-26OCT05LEOCAS-LEO`) | 0.98 / 0.99 (1154) | 98.5% | 72.5% | 67.0% | 72.4% [71.5%-73.6%] | -- | -- | -- | -- | PASS | -26.1 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 516.0, B 116.0; serve-point win A 65.0%, B 39.8%; Elo A 1348.6, B 1179.8; model uncertainty 0.0103
* Form inputs: days since last match A 434, B 378; matches on record A 17, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT05LEOCAS-CAS  (YES = Yannick Castelnuovo)
Model: 28%
Kalshi: 2%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aniketh Venkataraman vs Anup Bangargi -- M25 Kigali R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05VENBAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anup Bangargi (`KXITFMATCH-26OCT05VENBAN-BAN`) | 0.60 / 0.61 (2) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aniketh Venkataraman (`KXITFMATCH-26OCT05VENBAN-VEN`) | 0.35 / 0.37 (2) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adrover Gallego / Ros Parres vs Lovric / Mettraux -- W35 Seville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-05T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05ADRROSLOVMET:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrover Gallego / Ros Parres (`KXITFWDOUBLES-26OCT05ADRROSLOVMET-ADRROS`) | 0.08 / 0.10 (7) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lovric / Mettraux (`KXITFWDOUBLES-26OCT05ADRROSLOVMET-LOVMET`) | 0.88 / 0.92 (49) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Chiesa / Wilda Hennemann vs Gomez O'Hayon / Oliver sanchez -- W35 Seville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-05T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05CHIWILGOMOLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chiesa / Wilda Hennemann (`KXITFWDOUBLES-26OCT05CHIWILGOMOLI-CHIWIL`) | 0.95 / 0.97 (520) | 96.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gomez O'Hayon / Oliver sanchez (`KXITFWDOUBLES-26OCT05CHIWILGOMOLI-GOMOLI`) | 0.02 / 0.05 (770) | 3.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Maxi Carrascosa Diaz vs Borna Gojo -- ATP Challenger Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:127339:213759:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxi Carrascosa Diaz (`KXATPCHALLENGERMATCH-26OCT05CARGOJ-CAR`) | 0.04 / 0.05 (2337) | 4.5% | 3.3% | 9.5% | 4.3% [3.2%-5.0%] | -- | 2.4% | 2.4% | KALSHI_LONE_OUTLIER | PASS | -0.2 pp | NORMAL | AGING | D / POOR | ALL_AGREE | VERIFIED |
| Borna Gojo (`KXATPCHALLENGERMATCH-26OCT05CARGOJ-GOJ`) | 0.95 / 0.96 (627) | 95.5% | 96.7% | 90.5% | 95.7% [95.0%-96.8%] | -- | 95.8% | -- | INSUFFICIENT_INPUTS | PASS | +0.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 431.0, B 3870.0; serve-point win A 55.3%, B 30.1%; Elo A 1183.0, B 1771.4; model uncertainty 0.0091
* Form inputs: days since last match A 224, B 14; matches on record A 7, B 587; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Hugo Cardinaud vs VALENTIN LATRUBESSE -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05CARLAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Cardinaud (`KXITFMATCH-26OCT05CARLAT-CAR`) | 0.98 / 0.99 (1866) | 98.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| VALENTIN LATRUBESSE (`KXITFMATCH-26OCT05CARLAT-LAT`) | 0.01 / 0.02 (530) | 1.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Axel Garcian vs Sacha Grandvincent -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05GARGRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Axel Garcian (`KXITFMATCH-26OCT05GARGRA-GAR`) | 0.76 / 0.77 (2519) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sacha Grandvincent (`KXITFMATCH-26OCT05GARGRA-GRA`) | 0.23 / 0.25 (1881) | 24.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## LUCAS GONCALVES FRANCA vs King Onyx Umuhoza -- M25 Kigali R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05GONUMU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LUCAS GONCALVES FRANCA (`KXITFMATCH-26OCT05GONUMU-GON`) | 0.98 / 0.99 (775) | 98.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| King Onyx Umuhoza (`KXITFMATCH-26OCT05GONUMU-UMU`) | 0.01 / 0.02 (8358) | 1.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Justin Lenders vs Ruslan Serazhetdinov -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213135:214082:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justin Lenders (`KXITFMATCH-26OCT05LENSER-LEN`) | 0.72 / 0.82 (36) | 77.0% | 56.5% | 53.6% | 56.2% [56.2%-56.8%] | -- | -- | -- | -- | PASS | -20.8 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ruslan Serazhetdinov (`KXITFMATCH-26OCT05LENSER-SER`) | 0.16 / 0.24 (114) | 20.0% | 43.5% | 46.4% | 43.8% [43.2%-43.8%] | -- | -- | -- | -- | PASS | +23.8 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 370.0, B 311.0; serve-point win A 64.7%, B 36.7%; Elo A 1250.2, B 1204.8; model uncertainty 0.0029
* Form inputs: days since last match A 217, B 196; matches on record A 8, B 10; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT05LENSER-SER  (YES = Ruslan Serazhetdinov)
Model: 44%
Kalshi: 20%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mika Buchnik vs Maria Herazo -- W50 Heraklion R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05BUCHER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mika Buchnik (`KXITFWMATCH-26OCT05BUCHER-BUC`) | 0.35 / 0.48 (54) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Herazo (`KXITFWMATCH-26OCT05BUCHER-HER`) | 0.48 / 0.56 (4) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kim Chiarello vs Heerae Im -- W35 Villeneuve d'Ascq R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260091:269710:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kim Chiarello (`KXITFWMATCH-26OCT05CHIIMX-CHI`) | 0.58 / 0.68 (5) | 63.0% | 54.5% | 41.5% | 51.6% [47.9%-55.3%] | -- | -- | -- | -- | PASS | -11.4 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Heerae Im (`KXITFWMATCH-26OCT05CHIIMX-IMX`) | 0.22 / 0.30 (36) | 26.0% | 45.5% | 58.5% | 48.4% [44.7%-52.1%] | -- | -- | -- | -- | PASS | +22.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 458.0, B 568.0; serve-point win A 56.1%, B 44.7%; Elo A 1367.9, B 1336.6; model uncertainty 0.0373
* Form inputs: days since last match A 357, B 161; matches on record A 7, B 61; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05CHIIMX-IMX  (YES = Heerae Im)
Model: 48%
Kalshi: 26%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.011, surface_dev_loose -0.016, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Analu Freitas vs Kennedy Gibbs -- W35 Lagos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:249680:256710:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Analu Freitas (`KXITFWMATCH-26OCT05FREGIB-FRE`) | 0.17 / 0.18 (14) | 17.5% | 15.2% | 5.6% | 15.5% [15.4%-15.5%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kennedy Gibbs (`KXITFWMATCH-26OCT05FREGIB-GIB`) | 0.82 / 0.83 (2668) | 82.5% | 84.8% | 94.4% | 84.5% [84.5%-84.6%] | -- | -- | -- | -- | PASS | +2.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 363.0, B 0.0; serve-point win A 53.1%, B 39.1%; Elo A 1094.5, B 1393.3; model uncertainty 0.0003
* Form inputs: days since last match A 175, B 805; matches on record A 28, B 10; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Polina Isakova vs Georgina Hays -- W35 Lagos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:246516:267435:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Georgina Hays (`KXITFWMATCH-26OCT05ISAHAY-HAY`) | 0.53 / 0.59 (118) | 56.0% | 53.3% | 27.8% | 52.1% [51.6%-53.2%] | -- | -- | -- | -- | PASS | -3.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Polina Isakova (`KXITFWMATCH-26OCT05ISAHAY-ISA`) | 0.41 / 0.45 (17) | 43.0% | 46.7% | 72.2% | 47.9% [46.8%-48.4%] | -- | -- | -- | -- | PASS | +4.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 42.0, B 333.0; serve-point win A 56.7%, B 42.7%; Elo A 1175.6, B 1198.8; model uncertainty 0.008
* Form inputs: days since last match A 113, B 441; matches on record A 7, B 89; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Kryvoruchko vs Simona Ogescu -- W50 Heraklion R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221542:269993:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Kryvoruchko (`KXITFWMATCH-26OCT05KRYOGE-KRY`) | 0.18 / 0.19 (476) | 18.5% | 49.5% | 55.3% | 51.1% [48.9%-51.6%] | 20.6% | -- | 20.6% | KALSHI_LONE_OUTLIER | PASS | +32.6 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Simona Ogescu (`KXITFWMATCH-26OCT05KRYOGE-OGE`) | 0.81 / 0.83 (128) | 82.0% | 50.5% | 44.7% | 48.9% [48.4%-51.1%] | 79.4% | -- | 79.4% | KALSHI_LONE_OUTLIER | PASS | -33.1 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 335.0, B 1359.0; serve-point win A 55.6%, B 44.3%; Elo A 1341.9, B 1345.4; model uncertainty 0.0134
* Form inputs: days since last match A 399, B 315; matches on record A 7, B 231; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05KRYOGE-KRY  (YES = Sofia Kryvoruchko)
Model: 51%
Kalshi: 18%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maaya Rajeshwaran Revathi vs Daisy Mewett -- W35 Lagos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05RAJMEW:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daisy Mewett (`KXITFWMATCH-26OCT05RAJMEW-MEW`) | 0.03 / 0.05 (3747) | 4.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maaya Rajeshwaran Revathi (`KXITFWMATCH-26OCT05RAJMEW-RAJ`) | 0.95 / 0.96 (501) | 95.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lara Schmidt vs Viktoria Veleva -- W50 Heraklion R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215647:225861:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lara Schmidt (`KXITFWMATCH-26OCT05SCHVEL-SCH`) | 0.54 / 0.55 (8) | 54.5% | 84.7% | 48.4% | 78.2% [70.4%-85.8%] | 53.8% | -- | 53.8% | MODEL_LONE_OUTLIER | PASS | +23.7 pp | HIGH_REVIEW | STALE | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Viktoria Veleva (`KXITFWMATCH-26OCT05SCHVEL-VEL`) | 0.41 / 0.46 (178) | 43.5% | 15.3% | 51.6% | 21.8% [14.2%-29.6%] | 46.2% | -- | 46.2% | ALL_THREE_DISAGREE | PASS | -21.7 pp | HIGH_REVIEW | STALE | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 471.0, B 1099.0; serve-point win A 59.5%, B 48.2%; Elo A 1545.7, B 1249.0; model uncertainty 0.077
* Form inputs: days since last match A 448, B 161; matches on record A 210, B 85; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05SCHVEL-SCH  (YES = Lara Schmidt)
Model: 78%
Kalshi: 55%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.012, surface_pool_high -0.016, surface_dev_loose +0.011, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mariella Thamm vs eunchae Kim -- W35 Villeneuve d'Ascq R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260093:265701:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| eunchae Kim (`KXITFWMATCH-26OCT05THAKIM-KIM`) | 0.14 / 0.23 (20) | 18.5% | 19.7% | 32.9% | 21.0% [16.8%-24.3%] | -- | -- | -- | -- | PASS | +2.5 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mariella Thamm (`KXITFWMATCH-26OCT05THAKIM-THA`) | 0.65 / 0.80 (54) | 72.5% | 80.3% | 67.1% | 79.0% [75.7%-83.2%] | -- | -- | -- | -- | PASS | +6.5 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1262.0, B 197.0; serve-point win A 58.9%, B 47.5%; Elo A 1562.0, B 1317.7; model uncertainty 0.0375
* Form inputs: days since last match A 107, B 161; matches on record A 54, B 46; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.032, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katja Wiersholm vs Elena Korokozidi -- W50 Heraklion R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221202:222481:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Korokozidi (`KXITFWMATCH-26OCT05WIEKOR-KOR`) | 0.88 / 0.90 (835) | 89.0% | 47.9% | 61.6% | 48.4% [46.8%-50.5%] | -- | -- | -- | -- | PASS | -40.6 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katja Wiersholm (`KXITFWMATCH-26OCT05WIEKOR-WIE`) | 0.11 / 0.12 (329) | 11.5% | 52.1% | 38.4% | 51.6% [49.5%-53.2%] | -- | -- | -- | -- | PASS | +40.1 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 67.0, B 2005.0; serve-point win A 55.9%, B 44.5%; Elo A 1433.3, B 1418.7; model uncertainty 0.0188
* Form inputs: days since last match A 203, B 161; matches on record A 57, B 149; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05WIEKOR-WIE  (YES = Katja Wiersholm)
Model: 52%
Kalshi: 12%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.016, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mateus Alves vs Jose Pereira -- ATP Challenger Antofagasta Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105700:127123:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateus Alves (`KXATPCHALLENGERMATCH-26OCT05ALVPER-ALV`) | 0.83 / 0.84 (109) | 83.5% | 66.6% | 71.4% | 70.9% [69.3%-71.8%] | 80.3% | -- | 80.3% | KALSHI_LONE_OUTLIER | PASS | -12.6 pp | REVIEW | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Jose Pereira (`KXATPCHALLENGERMATCH-26OCT05ALVPER-PER`) | 0.16 / 0.17 (1591) | 16.5% | 33.4% | 28.6% | 29.1% [28.2%-30.7%] | 19.7% | -- | 19.7% | KALSHI_LONE_OUTLIER | SHADOW_BET | +12.6 pp | REVIEW | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4869.0, B 3145.0; serve-point win A 61.6%, B 41.8%; Elo A 1532.2, B 1387.5; model uncertainty 0.0126
* Form inputs: days since last match A 126, B 140; matches on record A 428, B 889; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.009, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Nicolas Kicker vs Thiago Cigarran -- ATP Challenger Antofagasta Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106044:208532:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thiago Cigarran (`KXATPCHALLENGERMATCH-26OCT05KICCIG-CIG`) | 0.12 / 0.13 (597) | 12.5% | 14.5% | 12.3% | 12.0% [10.9%-13.7%] | -- | -- | -- | -- | PASS | -0.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicolas Kicker (`KXATPCHALLENGERMATCH-26OCT05KICCIG-KIC`) | 0.86 / 0.87 (154) | 86.5% | 85.5% | 87.7% | 88.0% [86.3%-89.1%] | -- | -- | -- | -- | PASS | +1.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4358.0, B 2479.0; serve-point win A 64.0%, B 44.2%; Elo A 1631.0, B 1285.9; model uncertainty 0.0139
* Form inputs: days since last match A 14, B 49; matches on record A 885, B 167; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Lucio Ratti vs Maximo Zeitune -- ATP Challenger Antofagasta Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211636:212784:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucio Ratti (`KXATPCHALLENGERMATCH-26OCT05RATZEI-RAT`) | 0.53 / 0.54 (1409) | 53.5% | 65.0% | 74.5% | 69.8% [65.3%-72.4%] | 54.1% | -- | 54.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +16.3 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Maximo Zeitune (`KXATPCHALLENGERMATCH-26OCT05RATZEI-ZEI`) | 0.46 / 0.47 (4293) | 46.5% | 35.0% | 25.5% | 30.2% [27.6%-34.7%] | 45.9% | -- | 45.9% | MODEL_LONE_OUTLIER | PASS | -16.3 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3072.0, B 2380.0; serve-point win A 61.4%, B 41.6%; Elo A 1469.7, B 1392.8; model uncertainty 0.0355
* Form inputs: days since last match A 14, B 28; matches on record A 121, B 72; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT05RATZEI-RAT  (YES = Lucio Ratti)
Model: 70%
Kalshi: 54%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Boehner / Yesypchuk vs Candiotto / Vitoria Leme Da Silva -- W35 Seville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-05T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05BOEYESCANVIT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boehner / Yesypchuk (`KXITFWDOUBLES-26OCT05BOEYESCANVIT-BOEYES`) | 0.05 / 0.52 (2) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Candiotto / Vitoria Leme Da Silva (`KXITFWDOUBLES-26OCT05BOEYESCANVIT-CANVIT`) | 0.06 / 0.74 (54) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cabassers Morros / Cabassers Morros vs Cassani / Sara -- W35 Seville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-05T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05CABCABCASSAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cabassers Morros / Cabassers Morros (`KXITFWDOUBLES-26OCT05CABCABCASSAR-CABCAB`) | 0.08 / 0.49 (151) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cassani / Sara (`KXITFWDOUBLES-26OCT05CABCABCASSAR-CASSAR`) | 0.67 / 0.76 (1) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Corte / Teixido Garcia vs Fernandez Sanchez / Gudelj -- W35 Seville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-05T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05CORTEIFERGUD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Corte / Teixido Garcia (`KXITFWDOUBLES-26OCT05CORTEIFERGUD-CORTEI`) | 0.68 / 0.81 (1) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fernandez Sanchez / Gudelj (`KXITFWDOUBLES-26OCT05CORTEIFERGUD-FERGUD`) | 0.12 / 0.32 (100) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yannick Baluska vs Yannis Batsabaken -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05BALBAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yannick Baluska (`KXITFMATCH-26OCT05BALBAT-BAL`) | 0.15 / 0.19 (6) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yannis Batsabaken (`KXITFMATCH-26OCT05BALBAT-BAT`) | 0.78 / 0.79 (119) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bienvenue Bolangi vs Albin Colette -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05BOLCOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bienvenue Bolangi (`KXITFMATCH-26OCT05BOLCOL-BOL`) | 0.33 / 0.35 (104) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Albin Colette (`KXITFMATCH-26OCT05BOLCOL-COL`) | 0.64 / 0.69 (916) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Octave Caillat vs Jaume Casas Blasi -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:214410:214460:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Octave Caillat (`KXITFMATCH-26OCT05CAICAS-CAI`) | 0.34 / 0.44 (22) | 39.0% | 46.0% | 41.2% | 45.8% [44.8%-45.9%] | -- | -- | -- | -- | PASS | +6.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jaume Casas Blasi (`KXITFMATCH-26OCT05CAICAS-CAS`) | 0.51 / 0.61 (91) | 56.0% | 54.0% | 58.8% | 54.2% [54.1%-55.2%] | -- | -- | -- | -- | PASS | -1.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 101.0, B 81.0; serve-point win A 63.6%, B 35.6%; Elo A 1213.3, B 1241.4; model uncertainty 0.0056
* Form inputs: days since last match A 238, B 147; matches on record A 2, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carlos Giraldi vs Nicolas Rafael Goldberg Alviani -- M15 Pontevedra R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210400:211600:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlos Giraldi (`KXITFMATCH-26OCT05GIRGOL-GIR`) | 0.82 / 0.91 (628) | 86.5% | 50.8% | 36.8% | 48.4% [46.4%-50.0%] | -- | -- | -- | -- | PASS | -38.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicolas Rafael Goldberg Alviani (`KXITFMATCH-26OCT05GIRGOL-GOL`) | 0.07 / 0.14 (23) | 10.5% | 49.2% | 63.2% | 51.5% [50.0%-53.6%] | -- | -- | -- | -- | PASS | +41.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 601.0, B 319.0; serve-point win A 62.7%, B 37.5%; Elo A 1083.6, B 1078.3; model uncertainty 0.018
* Form inputs: days since last match A 126, B 392; matches on record A 27, B 28; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT05GIRGOL-GOL  (YES = Nicolas Rafael Goldberg Alviani)
Model: 52%
Kalshi: 10%
Gap: +41 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Noah Thurner vs Rodrigo Duarte -- M15 Pontevedra R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05THUDUA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigo Duarte (`KXITFMATCH-26OCT05THUDUA-DUA`) | 0.09 / 0.20 (310) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Noah Thurner (`KXITFMATCH-26OCT05THUDUA-THU`) | 0.76 / 0.90 (5) | 83.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carlotta Moccia vs Beatriz Castro -- W35 Lagos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223411:270381:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beatriz Castro (`KXITFWMATCH-26OCT05MOCCAS-CAS`) | 0.03 / 0.05 (204) | 4.0% | 41.9% | 31.1% | 41.0% [39.5%-41.5%] | -- | -- | -- | -- | PASS | +37.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carlotta Moccia (`KXITFWMATCH-26OCT05MOCCAS-MOC`) | 0.92 / 0.95 (50) | 93.5% | 58.1% | 68.9% | 59.0% [58.5%-60.5%] | -- | -- | -- | -- | PASS | -34.5 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 644.0, B 76.0; serve-point win A 57.8%, B 43.8%; Elo A 1325.0, B 1267.9; model uncertainty 0.0102
* Form inputs: days since last match A 217, B 168; matches on record A 120, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05MOCCAS-CAS  (YES = Beatriz Castro)
Model: 41%
Kalshi: 4%
Gap: +37 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marine Szostak vs Margaux Komano -- W35 Villeneuve d'Ascq R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221524:222347:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Margaux Komano (`KXITFWMATCH-26OCT05SZOKOM-KOM`) | 0.15 / 0.18 (826) | 16.5% | 27.9% | 25.6% | 25.1% [22.6%-28.7%] | -- | -- | -- | -- | PASS | +8.6 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marine Szostak (`KXITFWMATCH-26OCT05SZOKOM-SZO`) | 0.81 / 0.85 (2495) | 83.0% | 72.1% | 74.5% | 74.9% [71.3%-77.4%] | -- | -- | -- | -- | PASS | -8.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1767.0, B 941.0; serve-point win A 57.9%, B 46.5%; Elo A 1449.7, B 1256.1; model uncertainty 0.0303
* Form inputs: days since last match A 161, B 175; matches on record A 238, B 203; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.013, surface_dev_loose +0.009, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Klara Veldman vs Elise Renard -- W35 Villeneuve d'Ascq R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223418:260377:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elise Renard (`KXITFWMATCH-26OCT05VELREN-REN`) | 0.22 / 0.28 (6) | 25.0% | 49.3% | 38.9% | 46.8% [43.6%-50.0%] | -- | -- | -- | -- | PASS | +21.8 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Klara Veldman (`KXITFWMATCH-26OCT05VELREN-VEL`) | 0.73 / 0.74 (1) | 73.5% | 50.7% | 61.1% | 53.2% [50.0%-56.4%] | -- | -- | -- | -- | PASS | -20.3 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1299.0, B 389.0; serve-point win A 55.8%, B 44.4%; Elo A 1331.3, B 1326.2; model uncertainty 0.0319
* Form inputs: days since last match A 161, B 371; matches on record A 141, B 39; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05VELREN-REN  (YES = Elise Renard)
Model: 47%
Kalshi: 25%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pablo Llamas Ruiz vs Luca Nardi -- ATP Challenger Villena R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 18:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-05T18:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208010:208134:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pablo Llamas Ruiz (`KXATPCHALLENGERMATCH-26OCT05LLANAR-LLA`) | 0.60 / 0.61 (4124) | 60.5% | 50.3% | 51.5% | 48.5% [46.4%-52.0%] | 61.6% | 61.6% | 61.6% | MARKETS_AGREE | PASS | -12.0 pp | REVIEW | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Luca Nardi (`KXATPCHALLENGERMATCH-26OCT05LLANAR-NAR`) | 0.38 / 0.39 (907) | 38.5% | 49.7% | 48.5% | 51.5% [47.9%-53.6%] | 38.4% | 38.2% | 38.3% | MARKETS_AGREE | SHADOW_BET | +13.0 pp | REVIEW | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4479.0, B 5888.0; serve-point win A 62.6%, B 37.4%; Elo A 1653.0, B 1721.6; model uncertainty 0.0282
* Form inputs: days since last match A 28, B 86; matches on record A 377, B 467; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.021, surface_dev_loose -0.015, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Jules Alias vs Philippe Renard -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05ALIREN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jules Alias (`KXITFMATCH-26OCT05ALIREN-ALI`) | 0.20 / 0.28 (35) | 24.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Philippe Renard (`KXITFMATCH-26OCT05ALIREN-REN`) | 0.69 / 0.76 (17) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Julien Dando vs Robin Eldin -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05DANELD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julien Dando (`KXITFMATCH-26OCT05DANELD-DAN`) | 0.74 / 0.82 (64) | 78.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Robin Eldin (`KXITFMATCH-26OCT05DANELD-ELD`) | 0.22 / 0.23 (25) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maxence Rivet vs Paul Theate -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212134:214399:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxence Rivet (`KXITFMATCH-26OCT05RIVTHE-RIV`) | 0.74 / 0.76 (10) | 75.0% | 52.3% | 43.3% | 51.0% [50.0%-51.5%] | -- | -- | -- | -- | PASS | -24.0 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Paul Theate (`KXITFMATCH-26OCT05RIVTHE-THE`) | 0.25 / 0.26 (43) | 25.5% | 47.7% | 56.7% | 49.0% [48.4%-50.0%] | -- | -- | -- | -- | PASS | +23.5 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1121.0, B 240.0; serve-point win A 64.2%, B 36.2%; Elo A 1231.7, B 1215.7; model uncertainty 0.0077
* Form inputs: days since last match A 154, B 140; matches on record A 115, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT05RIVTHE-THE  (YES = Paul Theate)
Model: 49%
Kalshi: 26%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Louis Wessels vs Andrej Martin -- ATP Challenger Palermo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105413:144923:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrej Martin (`KXATPCHALLENGERMATCH-26OCT05WESMAR-MAR`) | 0.54 / 0.55 (86) | 54.5% | 64.7% | 54.6% | 61.1% [58.6%-64.0%] | -- | 55.0% | 55.0% | MODEL_LONE_OUTLIER | PASS | +6.6 pp | NORMAL | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Louis Wessels (`KXATPCHALLENGERMATCH-26OCT05WESMAR-WES`) | 0.45 / 0.46 (2558) | 45.5% | 35.3% | 45.4% | 38.9% [36.0%-41.4%] | -- | 45.1% | 45.1% | MODEL_LONE_OUTLIER | PASS | -6.6 pp | NORMAL | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3369.0, B 2756.0; serve-point win A 58.4%, B 38.6%; Elo A 1436.4, B 1598.3; model uncertainty 0.0269
* Form inputs: days since last match A 77, B 49; matches on record A 581, B 1378; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Kabbaj / Tsygourova vs Carreras Medina / Coltorti lopez -- W35 Seville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05KABTSYCARCOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carreras Medina / Coltorti lopez (`KXITFWDOUBLES-26OCT05KABTSYCARCOL-CARCOL`) | 0.06 / 0.15 (2) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kabbaj / Tsygourova (`KXITFWDOUBLES-26OCT05KABTSYCARCOL-KABTSY`) | 0.85 / 0.90 (0) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Melina Maria Maruca vs Fernanda Rain -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05MARRAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melina Maria Maruca (`KXITFWMATCH-26OCT05MARRAI-MAR`) | 0.46 / 0.52 (50) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fernanda Rain (`KXITFWMATCH-26OCT05MARRAI-RAI`) | 0.47 / 0.48 (5) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rodriguez Carretero / Trujillo Garnica vs Roura Llaverias / Torner Sensano -- W35 Seville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05RODTRUROUTOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodriguez Carretero / Trujillo Garnica (`KXITFWDOUBLES-26OCT05RODTRUROUTOR-RODTRU`) | 0.07 / 0.08 (27) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Roura Llaverias / Torner Sensano (`KXITFWDOUBLES-26OCT05RODTRUROUTOR-ROUTOR`) | 0.81 / 0.91 (1) | 86.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Solar Donoso / Teixido Garcia vs Mattel / Nguyen Tan -- W35 Seville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05SOLTEIMATNGU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mattel / Nguyen Tan (`KXITFWDOUBLES-26OCT05SOLTEIMATNGU-MATNGU`) | 0.08 / 0.79 (22) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Solar Donoso / Teixido Garcia (`KXITFWDOUBLES-26OCT05SOLTEIMATNGU-SOLTEI`) | 0.08 / 0.51 (2) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Agustina Soto Neira vs Gabriela Kawano Cho -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259599:266772:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela Kawano Cho (`KXITFWMATCH-26OCT05SOTKAW-KAW`) | 0.44 / 0.45 (65) | 44.5% | 46.3% | 25.6% | 44.1% [39.5%-45.7%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Agustina Soto Neira (`KXITFWMATCH-26OCT05SOTKAW-SOT`) | 0.55 / 0.56 (3139) | 55.5% | 53.7% | 74.4% | 55.9% [54.3%-60.5%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.3 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 349.0, B 126.0; serve-point win A 57.4%, B 43.4%; Elo A 1263.3, B 1237.5; model uncertainty 0.0314
* Form inputs: days since last match A 196, B 364; matches on record A 18, B 17; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aiken Tejada vs Agustina Daniela Duarte -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:265618:266453:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agustina Daniela Duarte (`KXITFWMATCH-26OCT05TEJDUA-DUA`) | 0.91 / 0.94 (45) | 92.5% | 60.8% | 30.1% | 59.5% [57.4%-60.6%] | 90.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -33.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aiken Tejada (`KXITFWMATCH-26OCT05TEJDUA-TEJ`) | 0.06 / 0.09 (417) | 7.5% | 39.2% | 69.9% | 40.5% [39.5%-42.6%] | 9.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +33.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 55.0, B 61.0; serve-point win A 56.0%, B 42.0%; Elo A 1061.1, B 1137.4; model uncertainty 0.0156
* Form inputs: days since last match A 336, B 196; matches on record A 19, B 10; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05TEJDUA-TEJ  (YES = Aiken Tejada)
Model: 40%
Kalshi: 8%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Murkel Dellien vs Juan Estevez -- ATP Challenger Antofagasta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05DEVEST:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Murkel Dellien (`KXATPCHALLENGERMATCH-26OCT05DEVEST-DEV`) | 0.44 / 0.45 (873) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juan Estevez (`KXATPCHALLENGERMATCH-26OCT05DEVEST-EST`) | 0.55 / 0.56 (4013) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Gonzalo Villanueva vs Nick Hardt -- ATP Challenger Antofagasta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106380:200572:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nick Hardt (`KXATPCHALLENGERMATCH-26OCT05VILHAR-HAR`) | 0.44 / 0.45 (1301) | 44.5% | -- | 59.9% | 58.9% [57.9%-60.9%] | 45.9% | 44.9% | 45.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +14.4 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Gonzalo Villanueva (`KXATPCHALLENGERMATCH-26OCT05VILHAR-VIL`) | 0.54 / 0.56 (927) | 55.0% | -- | 40.1% | 41.1% [39.1%-42.1%] | 54.1% | 55.1% | 54.6% | MODEL_LONE_OUTLIER | PASS | -13.9 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5724.0, B 4723.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0154
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Ema Burgic vs Serafima Elizarova -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202619:270346:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ema Burgic (`KXITFWMATCH-26OCT05BURELI-BUR`) | 0.86 / 0.88 (30) | 87.0% | 76.1% | 79.3% | 76.6% [75.7%-78.2%] | -- | -- | -- | -- | PASS | -10.4 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Serafima Elizarova (`KXITFWMATCH-26OCT05BURELI-ELI`) | 0.09 / 0.11 (28) | 10.0% | 23.9% | 20.6% | 23.4% [21.8%-24.3%] | -- | -- | -- | -- | PASS | +13.4 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1373.0, B 93.0; serve-point win A 58.4%, B 47.0%; Elo A 1468.1, B 1267.0; model uncertainty 0.0125
* Form inputs: days since last match A 224, B 329; matches on record A 225, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amparo Corvalan Mitilli vs Camila Markus -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05CORMAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amparo Corvalan Mitilli (`KXITFWMATCH-26OCT05CORMAR-COR`) | 0.05 / 0.11 (107) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Camila Markus (`KXITFWMATCH-26OCT05CORMAR-MAR`) | 0.91 / 0.95 (3145) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Kononova vs Eva Maria Ionescu -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215236:260490:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eva Maria Ionescu (`KXITFWMATCH-26OCT05KONION-ION`) | 0.62 / 0.69 (19) | 65.5% | 68.4% | 78.0% | 70.8% [68.0%-72.6%] | -- | -- | -- | -- | PASS | +5.3 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Kononova (`KXITFWMATCH-26OCT05KONION-KON`) | 0.27 / 0.34 (1) | 30.5% | 31.6% | 22.0% | 29.2% [27.4%-32.0%] | -- | -- | -- | -- | PASS | -1.3 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 370.0, B 1868.0; serve-point win A 53.9%, B 42.5%; Elo A 1343.3, B 1477.3; model uncertainty 0.023
* Form inputs: days since last match A 231, B 85; matches on record A 139, B 92; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.028, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isabella Mai vs Diva Bhatia -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05MAIBHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diva Bhatia (`KXITFWMATCH-26OCT05MAIBHA-BHA`) | 0.88 / 0.89 (1) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Isabella Mai (`KXITFWMATCH-26OCT05MAIBHA-MAI`) | 0.11 / 0.12 (47) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carlota Moreno vs Victoria Osuigwe -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259820:270436:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlota Moreno (`KXITFWMATCH-26OCT05MOROSU-MOR`) | 0.59 / 0.62 (10) | 60.5% | 54.8% | 66.6% | 57.5% [53.2%-61.1%] | -- | -- | -- | -- | PASS | -3.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Victoria Osuigwe (`KXITFWMATCH-26OCT05MOROSU-OSU`) | 0.37 / 0.41 (3115) | 39.0% | 45.2% | 33.4% | 42.5% [38.9%-46.8%] | -- | -- | -- | -- | PASS | +3.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 350.0, B 749.0; serve-point win A 56.1%, B 44.8%; Elo A 1429.2, B 1395.6; model uncertainty 0.0396
* Form inputs: days since last match A 182, B 371; matches on record A 6, B 93; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexis Nguyen vs Catherine Rennard -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260787:264061:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexis Nguyen (`KXITFWMATCH-26OCT05NGUREN-NGU`) | 0.79 / 0.84 (84) | 81.5% | 67.0% | 67.1% | 67.1% [65.6%-69.0%] | -- | -- | -- | -- | PASS | -14.4 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Catherine Rennard (`KXITFWMATCH-26OCT05NGUREN-REN`) | 0.15 / 0.17 (1) | 16.0% | 33.0% | 32.9% | 32.9% [31.0%-34.4%] | -- | -- | -- | -- | PASS | +16.9 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1010.0, B 378.0; serve-point win A 57.3%, B 46.0%; Elo A 1406.5, B 1283.4; model uncertainty 0.017
* Form inputs: days since last match A 161, B 168; matches on record A 69, B 7; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05NGUREN-REN  (YES = Catherine Rennard)
Model: 33%
Kalshi: 16%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.014, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emily Zornada vs Justina Lassaga -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:269811:270329:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justina Lassaga (`KXITFWMATCH-26OCT05ZORLAS-LAS`) | 0.05 / 0.06 (1018) | 5.5% | 30.9% | 32.4% | 30.5% [30.5%-31.0%] | -- | -- | -- | -- | PASS | +25.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Emily Zornada (`KXITFWMATCH-26OCT05ZORLAS-ZOR`) | 0.89 / 0.95 (142) | 92.0% | 69.1% | 67.6% | 69.5% [69.0%-69.5%] | -- | -- | -- | -- | PASS | -22.5 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 106.0, B 31.0; serve-point win A 58.9%, B 44.9%; Elo A 1299.7, B 1160.1; model uncertainty 0.0026
* Form inputs: days since last match A 189, B 504; matches on record A 2, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05ZORLAS-LAS  (YES = Justina Lassaga)
Model: 31%
Kalshi: 6%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jonas Forejtek vs Sandro Kopp -- ATP Challenger Palermo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05FORKOP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonas Forejtek (`KXATPCHALLENGERMATCH-26OCT05FORKOP-FOR`) | 0.60 / 0.61 (971) | 60.5% | -- | -- | -- [-----] | -- | 65.0% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sandro Kopp (`KXATPCHALLENGERMATCH-26OCT05FORKOP-KOP`) | 0.39 / 0.40 (45) | 39.5% | -- | -- | -- [-----] | -- | 47.5% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Francoise Abanda vs Charlotte Narti -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211796:270203:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francoise Abanda (`KXITFWMATCH-26OCT05ABANAR-ABA`) | 0.79 / 0.85 (70) | 82.0% | 85.6% | 70.4% | 83.6% [81.9%-86.4%] | -- | -- | -- | -- | PASS | +1.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Charlotte Narti (`KXITFWMATCH-26OCT05ABANAR-NAR`) | 0.12 / 0.18 (10) | 15.0% | 14.4% | 29.6% | 16.4% [13.6%-18.1%] | -- | -- | -- | -- | PASS | +1.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 902.0, B 300.0; serve-point win A 59.7%, B 48.3%; Elo A 1618.9, B 1309.0; model uncertainty 0.0223
* Form inputs: days since last match A 203, B 168; matches on record A 323, B 6; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.017, surface_dev_loose -0.003, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jane Dunyon vs Pietra Rivoli -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263978:266672:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jane Dunyon (`KXITFWMATCH-26OCT05DUNRIV-DUN`) | 0.31 / 0.35 (1) | 33.0% | 46.2% | 30.0% | 43.6% [40.5%-46.8%] | -- | -- | -- | -- | PASS | +10.6 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pietra Rivoli (`KXITFWMATCH-26OCT05DUNRIV-RIV`) | 0.63 / 0.68 (23) | 65.5% | 53.8% | 70.0% | 56.4% [53.2%-59.6%] | -- | -- | -- | -- | PASS | -9.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 200.0, B 500.0; serve-point win A 55.3%, B 44.0%; Elo A 1231.1, B 1257.8; model uncertainty 0.0318
* Form inputs: days since last match A 455, B 315; matches on record A 21, B 19; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tatum Evans vs Helena Buchwald -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:249679:259887:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Helena Buchwald (`KXITFWMATCH-26OCT05EVABUC-BUC`) | 0.25 / 0.26 (68) | 25.5% | 49.0% | 46.8% | 48.9% [45.7%-52.1%] | -- | -- | -- | -- | PASS | +23.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tatum Evans (`KXITFWMATCH-26OCT05EVABUC-EVA`) | 0.70 / 0.75 (17) | 72.5% | 51.0% | 53.2% | 51.1% [47.9%-54.3%] | -- | -- | -- | -- | PASS | -21.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 62.0, B 320.0; serve-point win A 55.8%, B 44.4%; Elo A 1369.3, B 1362.3; model uncertainty 0.032
* Form inputs: days since last match A 329, B 434; matches on record A 40, B 101; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05EVABUC-BUC  (YES = Helena Buchwald)
Model: 49%
Kalshi: 26%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.032, surface_pool_high +0.032, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Megan Heuser vs Kira Matushkina -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260962:262886:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Megan Heuser (`KXITFWMATCH-26OCT05HEUMAT-HEU`) | 0.20 / 0.28 (3128) | 24.0% | 17.1% | 28.7% | 19.2% [17.8%-20.7%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kira Matushkina (`KXITFWMATCH-26OCT05HEUMAT-MAT`) | 0.72 / 0.74 (52) | 73.0% | 82.9% | 71.3% | 80.8% [79.3%-82.2%] | -- | -- | -- | -- | PASS | +7.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 459.0, B 428.0; serve-point win A 52.1%, B 40.7%; Elo A 1202.2, B 1477.0; model uncertainty 0.0144
* Form inputs: days since last match A 308, B 308; matches on record A 12, B 46; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.003, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Felipe Meligeni Alves / Matheus Pucinelli de Almeida vs Milledge Cossu / Bautista de la Pena -- ATP Challenger Antofagasta R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 21:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-05T21:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05MELPDACOSDE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Milledge Cossu / Bautista de la Pena (`KXATPCHALLENGERDOUBLES-26OCT05MELPDACOSDE-COSDE`) | 0.15 / 0.16 (12) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Felipe Meligeni Alves / Matheus Pucinelli de Almeida (`KXATPCHALLENGERDOUBLES-26OCT05MELPDACOSDE-MELPDA`) | 0.81 / 0.86 (5) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Victor Bini vs Enmanuel Munoz -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-05T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210476:212192:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victor Bini (`KXITFMATCH-26OCT05BINMUN-BIN`) | 0.71 / 0.80 (3690) | 75.5% | 56.1% | 47.4% | 54.1% [53.1%-55.1%] | -- | -- | -- | -- | PASS | -21.4 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Enmanuel Munoz (`KXITFMATCH-26OCT05BINMUN-MUN`) | 0.20 / 0.24 (33) | 22.0% | 43.9% | 52.6% | 45.9% [44.9%-46.9%] | -- | -- | -- | -- | PASS | +23.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 499.0, B 386.0; serve-point win A 60.5%, B 40.7%; Elo A 1120.8, B 1078.1; model uncertainty 0.0102
* Form inputs: days since last match A 140, B 161; matches on record A 12, B 28; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT05BINMUN-MUN  (YES = Enmanuel Munoz)
Model: 46%
Kalshi: 22%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Sebastian Dominguez Collado vs Facundo Perlov -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05DOMPER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Sebastian Dominguez Collado (`KXITFMATCH-26OCT05DOMPER-DOM`) | 0.47 / 0.50 (22) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Facundo Perlov (`KXITFMATCH-26OCT05DOMPER-PER`) | 0.45 / 0.52 (3110) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diego Giraldo vs Miles Clark -- M15 Quito R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05GIRCLA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miles Clark (`KXITFMATCH-26OCT05GIRCLA-CLA`) | 0.51 / 0.57 (3141) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Diego Giraldo (`KXITFMATCH-26OCT05GIRCLA-GIR`) | 0.42 / 0.47 (6) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sol Ailin Larraya Guidi vs Ana Victoria Gobbi Monllau -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211600:260709:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ana Victoria Gobbi Monllau (`KXITFWMATCH-26OCT05LARGOB-GOB`) | 0.23 / 0.24 (32) | 23.5% | 33.2% | 50.0% | 37.4% [34.4%-40.5%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.9 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sol Ailin Larraya Guidi (`KXITFWMATCH-26OCT05LARGOB-LAR`) | 0.75 / 0.76 (2827) | 75.5% | 66.8% | 50.0% | 62.6% [59.5%-65.6%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.9 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 409.0, B 761.0; serve-point win A 58.6%, B 44.6%; Elo A 1359.6, B 1238.3; model uncertainty 0.0303
* Form inputs: days since last match A 189, B 196; matches on record A 66, B 108; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## CAIRA DELFINA VEGA GUDINO vs Guadalupe Rondinoni -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05VEGRON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guadalupe Rondinoni (`KXITFWMATCH-26OCT05VEGRON-RON`) | 0.06 / 0.11 (17) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| CAIRA DELFINA VEGA GUDINO (`KXITFWMATCH-26OCT05VEGRON-VEG`) | 0.87 / 0.92 (2) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leo Lagarrigue vs Jeremy LAUMON -- M15+H Rodez R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05LAGLAU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leo Lagarrigue (`KXITFMATCH-26OCT05LAGLAU-LAG`) | 0.89 / 0.93 (1) | 91.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeremy LAUMON (`KXITFMATCH-26OCT05LAGLAU-LAU`) | 0.06 / 0.08 (20) | 7.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Genaro Alberto Olivieri vs Valerio Aboian -- ATP Challenger Antofagasta R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-05T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05OLIABO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valerio Aboian (`KXATPCHALLENGERMATCH-26OCT05OLIABO-ABO`) | 0.37 / 0.38 (292) | 37.5% | -- | -- | -- [-----] | 38.4% | 38.8% | 38.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Genaro Alberto Olivieri (`KXATPCHALLENGERMATCH-26OCT05OLIABO-OLI`) | 0.62 / 0.63 (324) | 62.5% | -- | -- | -- [-----] | 61.6% | 61.6% | 61.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Marina Bulbarella vs Abril Pajello -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259739:266726:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marina Bulbarella (`KXITFWMATCH-26OCT05BULPAJ-BUL`) | 0.85 / 0.89 (90) | 87.0% | 40.9% | 11.5% | 40.5% [40.5%-40.5%] | -- | -- | -- | -- | PASS | -46.5 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Abril Pajello (`KXITFWMATCH-26OCT05BULPAJ-PAJ`) | 0.10 / 0.14 (1) | 12.0% | 59.1% | 88.5% | 59.5% [59.5%-59.5%] | -- | -- | -- | -- | PASS | +47.5 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 714.0, B 0.0; serve-point win A 56.1%, B 42.1%; Elo A 1149.1, B 1212.7; model uncertainty 0.0001
* Form inputs: days since last match A 196, B 945; matches on record A 112, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05BULPAJ-PAJ  (YES = Abril Pajello)
Model: 60%
Kalshi: 12%
Gap: +48 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Frey vs Bella Bergqvist Larsson -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05FREBER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bella Bergqvist Larsson (`KXITFWMATCH-26OCT05FREBER-BER`) | 0.39 / 0.40 (1) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anna Frey (`KXITFWMATCH-26OCT05FREBER-FRE`) | 0.57 / 0.62 (42) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nalah Kaler vs McKenna Schaefbauer -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05KALSCH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nalah Kaler (`KXITFWMATCH-26OCT05KALSCH-KAL`) | 0.05 / 0.54 (1) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| McKenna Schaefbauer (`KXITFWMATCH-26OCT05KALSCH-SCH`) | 0.87 / 0.92 (1) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isabella Marton vs Diana Maria Ilie -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05MARILI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diana Maria Ilie (`KXITFWMATCH-26OCT05MARILI-ILI`) | 0.11 / 0.13 (1) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Isabella Marton (`KXITFWMATCH-26OCT05MARILI-MAR`) | 0.85 / 0.89 (19) | 87.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Briley Rhoden vs Katherine Hui -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 22:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222866:267464:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katherine Hui (`KXITFWMATCH-26OCT05RHOHUI-HUI`) | 0.86 / 0.88 (17) | 87.0% | 70.3% | 60.5% | 69.4% [68.5%-70.3%] | -- | -- | -- | -- | PASS | -17.6 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Briley Rhoden (`KXITFWMATCH-26OCT05RHOHUI-RHO`) | 0.12 / 0.13 (28) | 12.5% | 29.7% | 39.5% | 30.6% [29.6%-31.6%] | -- | -- | -- | -- | PASS | +18.1 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 170.0, B 270.0; serve-point win A 53.7%, B 42.3%; Elo A 1258.7, B 1408.6; model uncertainty 0.0095
* Form inputs: days since last match A 189, B 196; matches on record A 4, B 65; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05RHOHUI-RHO  (YES = Briley Rhoden)
Model: 31%
Kalshi: 12%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jensen Diianni vs Diae El Jardi -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 23:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215696:270383:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jensen Diianni (`KXITFWMATCH-26OCT05DIIELJ-DII`) | 0.24 / 0.26 (26) | 25.0% | 57.2% | 39.6% | 55.3% [53.2%-57.4%] | -- | -- | -- | -- | PASS | +30.3 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Diae El Jardi (`KXITFWMATCH-26OCT05DIIELJ-ELJ`) | 0.71 / 0.72 (89) | 71.5% | 42.8% | 60.4% | 44.7% [42.6%-46.8%] | -- | -- | -- | -- | PASS | -26.8 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 180.0, B 1043.0; serve-point win A 56.4%, B 45.0%; Elo A 1299.6, B 1249.2; model uncertainty 0.0209
* Form inputs: days since last match A 231, B 139; matches on record A 3, B 45; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05DIIELJ-DII  (YES = Jensen Diianni)
Model: 55%
Kalshi: 25%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rosario Jurado vs Ornela Luisana Mondati -- W15 Cipolletti R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 23:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05JURMON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rosario Jurado (`KXITFWMATCH-26OCT05JURMON-JUR`) | 0.09 / 0.95 (714) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ornela Luisana Mondati (`KXITFWMATCH-26OCT05JURMON-MON`) | 0.07 / 0.84 (1003) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Misa Malkin vs Amaliia Elizarova -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 23:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-05T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05MALELI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amaliia Elizarova (`KXITFWMATCH-26OCT05MALELI-ELI`) | 0.05 / 0.07 (26) | 6.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Misa Malkin (`KXITFWMATCH-26OCT05MALELI-MAL`) | 0.90 / 0.94 (97) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Astra Sharma vs Lavinia Tanasie -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 23:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206292:245094:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Astra Sharma (`KXITFWMATCH-26OCT05SHATAN-SHA`) | 0.75 / 0.87 (19) | 81.0% | 52.2% | 40.0% | 54.8% [47.3%-67.5%] | -- | -- | -- | -- | PASS | -26.2 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lavinia Tanasie (`KXITFWMATCH-26OCT05SHATAN-TAN`) | 0.13 / 0.16 (1) | 14.5% | 47.8% | 60.0% | 45.2% [32.5%-52.7%] | -- | -- | -- | -- | PASS | +30.7 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2800.0, B 1526.0; serve-point win A 55.9%, B 44.5%; Elo A 1637.8, B 1499.6; model uncertainty 0.1008
* Form inputs: days since last match A 19, B 329; matches on record A 423, B 206; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05SHATAN-TAN  (YES = Lavinia Tanasie)
Model: 45%
Kalshi: 14%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.011, surface_dev_loose +0.016, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mia Slama vs Kate Sharabura -- W50 Lexington SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-05 23:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-05T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260693:270283:2026-10-05`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kate Sharabura (`KXITFWMATCH-26OCT05SLASHA-SHA`) | 0.10 / 0.13 (1) | 11.5% | 34.0% | 28.8% | 33.5% [32.5%-34.4%] | -- | -- | -- | -- | PASS | +22.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mia Slama (`KXITFWMATCH-26OCT05SLASHA-SLA`) | 0.83 / 0.90 (60) | 86.5% | 66.0% | 71.2% | 66.5% [65.5%-67.5%] | -- | -- | -- | -- | PASS | -20.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 435.0, B 72.0; serve-point win A 57.2%, B 45.9%; Elo A 1374.9, B 1259.3; model uncertainty 0.0097
* Form inputs: days since last match A 420, B 357; matches on record A 34, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT05SLASHA-SHA  (YES = Kate Sharabura)
Model: 33%
Kalshi: 12%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hanyu Guo vs Aliona Falei -- WTA 125K Suzhou R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-05 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-06 02:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 01:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA125 (WTA_125) · surface ? · scheduled 2026-10-05T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT04GUOFAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aliona Falei (`KXWTACHALLENGERMATCH-26OCT04GUOFAL-FAL`) | 0.54 / 0.55 (1119) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hanyu Guo (`KXWTACHALLENGERMATCH-26OCT04GUOFAL-GUO`) | 0.43 / 0.44 (49) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE

## Mananchaya Sawangkaew vs Linda Fruhvirtova -- WTA 125K Suzhou R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-05 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-06 02:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 01:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA125 (WTA_125) · surface ? · scheduled 2026-10-05T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT04SAWFRU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linda Fruhvirtova (`KXWTACHALLENGERMATCH-26OCT04SAWFRU-FRU`) | 0.39 / 0.40 (258) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mananchaya Sawangkaew (`KXWTACHALLENGERMATCH-26OCT04SAWFRU-SAW`) | 0.60 / 0.61 (135) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Moyuka Uchijima vs Zhuoxuan Bai -- WTA 125K Suzhou R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-05 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-06 02:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 01:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA125 (WTA_125) · surface ? · scheduled 2026-10-05T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT04UCHBAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zhuoxuan Bai (`KXWTACHALLENGERMATCH-26OCT04UCHBAI-BAI`) | 0.47 / 0.49 (626) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Moyuka Uchijima (`KXWTACHALLENGERMATCH-26OCT04UCHBAI-UCH`) | 0.51 / 0.52 (3482) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE

## Daria Snigur vs Mirra Andreeva -- WTA Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-06 03:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-06T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT05SNIAND:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mirra Andreeva (`KXWTAMATCH-26OCT05SNIAND-AND`) | 0.84 / 0.85 (635) | 84.5% | -- | -- | -- [-----] | 82.7% | 84.4% | 83.5% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daria Snigur (`KXWTAMATCH-26OCT05SNIAND-SNI`) | 0.15 / 0.16 (15497) | 15.5% | -- | -- | -- [-----] | 17.3% | 15.5% | 16.4% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aziz Dougaz vs Federico Cina -- ATP Shanghai Q2

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-06 04:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT06DOUCIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Cina (`KXATPMATCH-26OCT06DOUCIN-CIN`) | 0.70 / 0.71 (944) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aziz Dougaz (`KXATPMATCH-26OCT06DOUCIN-DOU`) | 0.28 / 0.29 (101) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Liam Draxl vs Nikoloz Basilashvili -- ATP Shanghai Q2

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-06 04:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT06DRABAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikoloz Basilashvili (`KXATPMATCH-26OCT06DRABAS-BAS`) | 0.56 / 0.57 (9082) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liam Draxl (`KXATPMATCH-26OCT06DRABAS-DRA`) | 0.44 / 0.45 (108) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Roman Safiullin vs Shintaro Mochizuki -- ATP Shanghai Q2

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-06 04:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT06SAFMOC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shintaro Mochizuki (`KXATPMATCH-26OCT06SAFMOC-MOC`) | 0.17 / 0.19 (5489) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Roman Safiullin (`KXATPMATCH-26OCT06SAFMOC-SAF`) | 0.81 / 0.82 (91) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Bernard Tomic vs Timofey Skatov -- ATP Shanghai Q2

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-06 04:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 03:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT06TOMSKA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Timofey Skatov (`KXATPMATCH-26OCT06TOMSKA-SKA`) | 0.45 / 0.46 (31) | 45.5% | -- | -- | -- [-----] | -- | 46.1% | 46.1% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bernard Tomic (`KXATPMATCH-26OCT06TOMSKA-TOM`) | 0.53 / 0.54 (3101) | 53.5% | -- | -- | -- [-----] | -- | 54.5% | 54.5% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; WIDE_SPREAD

## Linda Noskova vs Ekaterina Alexandrova -- WTA Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-06 04:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-06T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT05NOSALE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Alexandrova (`KXWTAMATCH-26OCT05NOSALE-ALE`) | 0.24 / 0.25 (1) | 24.5% | -- | -- | -- [-----] | 26.7% | 24.6% | 25.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Linda Noskova (`KXWTAMATCH-26OCT05NOSALE-NOS`) | 0.75 / 0.76 (18221) | 75.5% | -- | -- | -- [-----] | 73.4% | 75.8% | 74.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Austin Krajicek / Nikola Mektic vs Theo Arribage / Albano Olivetti -- ATP Tokyo F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 08:00Z
* Current expected start: 2026-10-06 05:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 04:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-06T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06KRAMEKARROLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26OCT06KRAMEKARROLI-ARROLI`) | 0.41 / 0.45 (207) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Austin Krajicek / Nikola Mektic (`KXATPDOUBLES-26OCT06KRAMEKARROLI-KRAMEK`) | 0.53 / 0.58 (350) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Emerson Jones vs Mai Hontama -- WTA 125K Suzhou R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-05 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-06 05:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 04:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA125 (WTA_125) · surface ? · scheduled 2026-10-05T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT04JONHON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mai Hontama (`KXWTACHALLENGERMATCH-26OCT04JONHON-HON`) | 0.42 / 0.43 (501) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Emerson Jones (`KXWTACHALLENGERMATCH-26OCT04JONHON-JON`) | 0.57 / 0.58 (250) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Yulia Putintseva vs Yushan Shao -- WTA 125K Suzhou R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-05 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-06 05:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 04:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA125 (WTA_125) · surface ? · scheduled 2026-10-05T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT04PUTSHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yulia Putintseva (`KXWTACHALLENGERMATCH-26OCT04PUTSHA-PUT`) | 0.92 / 0.94 (1178) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yushan Shao (`KXWTACHALLENGERMATCH-26OCT04PUTSHA-SHA`) | 0.06 / 0.07 (2) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Catherine Aulia vs Nana Onozawa -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05AULONO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Catherine Aulia (`KXITFWMATCH-26OCT05AULONO-AUL`) | 0.49 / 0.75 (100) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nana Onozawa (`KXITFWMATCH-26OCT05AULONO-ONO`) | 0.17 / 0.44 (44) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Riko Kikawada vs Himari Sato -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05KIKSAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Riko Kikawada (`KXITFWMATCH-26OCT05KIKSAT-KIK`) | 0.15 / 0.80 (50) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Himari Sato (`KXITFWMATCH-26OCT05KIKSAT-SAT`) | 0.15 / 0.63 (67) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sera Nishimoto vs Rira Kosaka -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05NISKOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rira Kosaka (`KXITFWMATCH-26OCT05NISKOS-KOS`) | 0.40 / 0.47 (21) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sera Nishimoto (`KXITFWMATCH-26OCT05NISKOS-NIS`) | 0.23 / 0.51 (51) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## I Wen Wan vs Maiko Uchijima -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05WANUCH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maiko Uchijima (`KXITFWMATCH-26OCT05WANUCH-UCH`) | 0.06 / 0.30 (35) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| I Wen Wan (`KXITFWMATCH-26OCT05WANUCH-WAN`) | 0.23 / 0.85 (166) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kyrian Jacquet vs Rei Sakamoto -- ATP Shanghai Q2

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 05:00Z
* Current expected start: 2026-10-06 05:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 04:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+30_MIN

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-06T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT05JACSAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kyrian Jacquet (`KXATPMATCH-26OCT05JACSAK-JAC`) | 0.45 / 0.55 (500) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rei Sakamoto (`KXATPMATCH-26OCT05JACSAK-SAK`) | 0.45 / 0.55 (500) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Yoshihito Nishioka vs Dalibor Svrcina -- ATP Shanghai Q2

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 05:00Z
* Current expected start: 2026-10-06 05:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 04:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+30_MIN

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-06T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT05NISSVR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yoshihito Nishioka (`KXATPMATCH-26OCT05NISSVR-NIS`) | 0.13 / 0.84 (1) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dalibor Svrcina (`KXATPMATCH-26OCT05NISSVR-SVR`) | 0.12 / 0.84 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rigele TE vs Ilia Simakin -- ATP Shanghai Q2

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-06 05:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 04:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT06RIGSIM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rigele TE (`KXATPMATCH-26OCT06RIGSIM-RIG`) | 0.15 / 0.16 (3165) | 15.5% | -- | -- | -- [-----] | -- | 16.1% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ilia Simakin (`KXATPMATCH-26OCT06RIGSIM-SIM`) | 0.84 / 0.86 (667) | 85.0% | -- | -- | -- [-----] | -- | 83.8% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Michael Zheng vs Nicolas Mejia -- ATP Shanghai Q2

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-06 05:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 04:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT06ZHEMEJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Mejia (`KXATPMATCH-26OCT06ZHEMEJ-MEJ`) | 0.14 / 0.16 (3226) | 15.0% | -- | -- | -- [-----] | -- | 14.0% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Michael Zheng (`KXATPMATCH-26OCT06ZHEMEJ-ZHE`) | 0.84 / 0.86 (81) | 85.0% | -- | -- | -- [-----] | -- | 85.9% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER

## Jasmine Adams vs Ai Maruyama -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05ADAMAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jasmine Adams (`KXITFWMATCH-26OCT05ADAMAR-ADA`) | 0.05 / 0.95 (164) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ai Maruyama (`KXITFWMATCH-26OCT05ADAMAR-MAR`) | 0.05 / 0.95 (142) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ava Beck vs Sara Mickoska -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05BECMIC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ava Beck (`KXITFWMATCH-26OCT05BECMIC-BEC`) | 0.23 / 0.95 (164) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sara Mickoska (`KXITFWMATCH-26OCT05BECMIC-MIC`) | 0.05 / 0.11 (28) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alina Charaeva vs Qinwen Zheng -- WTA Beijing R16

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-06T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT05CHAZHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Charaeva (`KXWTAMATCH-26OCT05CHAZHE-CHA`) | 0.20 / 0.22 (160) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Qinwen Zheng (`KXWTAMATCH-26OCT05CHAZHE-ZHE`) | 0.79 / 0.80 (11) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Iva Jovic vs Iga Swiatek -- WTA Beijing R16

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-06T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT05JOVSWI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iva Jovic (`KXWTAMATCH-26OCT05JOVSWI-JOV`) | 0.35 / 0.36 (10396) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Iga Swiatek (`KXWTAMATCH-26OCT05JOVSWI-SWI`) | 0.64 / 0.65 (201) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mana Kawamura vs Gurmanat Kaur Sandhu -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05KAWSAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mana Kawamura (`KXITFWMATCH-26OCT05KAWSAN-KAW`) | 0.23 / 0.81 (136) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gurmanat Kaur Sandhu (`KXITFWMATCH-26OCT05KAWSAN-SAN`) | 0.06 / 0.38 (40) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Remika Ohashi vs Yuka Hosoki -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05OHAHOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuka Hosoki (`KXITFWMATCH-26OCT05OHAHOS-HOS`) | 0.32 / 0.37 (2) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Remika Ohashi (`KXITFWMATCH-26OCT05OHAHOS-OHA`) | 0.23 / 0.69 (93) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karolina Muchova vs Naomi Osaka -- WTA Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-06 07:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 06:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-06T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT05MUCOSA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karolina Muchova (`KXWTAMATCH-26OCT05MUCOSA-MUC`) | 0.55 / 0.56 (5) | 55.5% | -- | -- | -- [-----] | 55.6% | 55.6% | 55.6% | MARKETS_AGREE | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Naomi Osaka (`KXWTAMATCH-26OCT05MUCOSA-OSA`) | 0.44 / 0.45 (12775) | 44.5% | -- | -- | -- [-----] | 44.4% | 44.3% | 44.3% | MARKETS_AGREE | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Lyudmyla Kichenok / Asia Muhammad vs Storm Hunter / Kristina Mladenovic -- WTA Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 10:00Z
* Current expected start: 2026-10-06 07:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 06:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-06T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06KICMUHHUNMLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Storm Hunter / Kristina Mladenovic (`KXWTADOUBLES-26OCT06KICMUHHUNMLA-HUNMLA`) | 0.07 / 0.84 (25) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lyudmyla Kichenok / Asia Muhammad (`KXWTADOUBLES-26OCT06KICMUHHUNMLA-KICMUH`) | 0.07 / 0.38 (50) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Nuno Borges vs Facundo Diaz Acosta -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:132686:207680:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nuno Borges (`KXATPMATCH-26OCT06BORDIA-BOR`) | 0.72 / 0.75 (20) | 73.5% | -- | 46.5% | 54.4% [50.0%-60.8%] | -- | -- | -- | -- | PASS | -19.1 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Facundo Diaz Acosta (`KXATPMATCH-26OCT06BORDIA-DIA`) | 0.24 / 0.26 (11) | 25.0% | -- | 53.5% | 45.6% [39.2%-50.0%] | -- | -- | -- | -- | PASS | +20.6 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 7297.0, B 5481.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0541
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT06BORDIA-DIA  (YES = Facundo Diaz Acosta)
Model: 46%
Kalshi: 25%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.019, surface_dev_tight -0.010
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arthur Fery vs Marin Cilic -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105227:209259:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marin Cilic (`KXATPMATCH-26OCT06FERCIL-CIL`) | 0.43 / 0.47 (200) | 45.0% | -- | 47.1% | 50.0% [48.0%-56.4%] | -- | -- | -- | -- | PASS | +5.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arthur Fery (`KXATPMATCH-26OCT06FERCIL-FER`) | 0.53 / 0.57 (250) | 55.0% | -- | 52.9% | 50.0% [43.6%-52.0%] | -- | -- | -- | -- | PASS | -5.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4203.0, B 3841.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0418
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.020, surface_dev_loose +0.005, surface_dev_tight -0.010
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE

## Arthur Gea vs Jaime Faria -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:210262:210338:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jaime Faria (`KXATPMATCH-26OCT06GEAFAR-FAR`) | 0.36 / 0.39 (1) | 37.5% | -- | 33.8% | 37.6% [34.7%-44.5%] | -- | -- | -- | -- | PASS | +0.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arthur Gea (`KXATPMATCH-26OCT06GEAFAR-GEA`) | 0.59 / 0.63 (122) | 61.0% | -- | 66.2% | 62.4% [55.5%-65.3%] | -- | -- | -- | -- | PASS | +1.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5606.0, B 5916.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0486
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.014, surface_dev_loose +0.018, surface_dev_tight -0.019
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Marcos Giron vs Sebastian Baez -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106218:202104:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Baez (`KXATPMATCH-26OCT06GIRBAE-BAE`) | 0.50 / 0.51 (15000) | 50.5% | -- | 43.4% | 41.8% [39.8%-47.4%] | -- | -- | -- | -- | PASS | -8.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marcos Giron (`KXATPMATCH-26OCT06GIRBAE-GIR`) | 0.47 / 0.48 (50) | 47.5% | -- | 56.6% | 58.2% [52.6%-60.2%] | -- | -- | -- | -- | PASS | +10.7 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6817.0, B 5101.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.038
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.025, surface_pool_high +0.020, surface_dev_loose +0.000, surface_dev_tight -0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yannick Hanfmann vs Kamil Majchrzak -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105870:111794:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yannick Hanfmann (`KXATPMATCH-26OCT06HANMAJ-HAN`) | 0.38 / 0.42 (50) | 40.0% | -- | 63.3% | 59.1% [54.9%-61.0%] | -- | -- | -- | -- | PASS | +19.1 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kamil Majchrzak (`KXATPMATCH-26OCT06HANMAJ-MAJ`) | 0.57 / 0.61 (111) | 59.0% | -- | 36.7% | 40.9% [39.0%-45.1%] | -- | -- | -- | -- | PASS | -18.1 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6000.0, B 5517.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0307
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT06HANMAJ-HAN  (YES = Yannick Hanfmann)
Model: 59%
Kalshi: 40%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.014, surface_dev_loose +0.014, surface_dev_tight -0.019
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE

## Hubert Hurkacz vs James Duckworth -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105902:128034:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Duckworth (`KXATPMATCH-26OCT06HURDUC-DUC`) | 0.26 / 0.29 (25) | 27.5% | -- | 34.4% | 31.0% [27.1%-32.6%] | -- | -- | -- | -- | PASS | +3.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hubert Hurkacz (`KXATPMATCH-26OCT06HURDUC-HUR`) | 0.69 / 0.73 (20) | 71.0% | -- | 65.6% | 69.0% [67.4%-72.9%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4552.0, B 7564.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0273
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.008, surface_dev_loose -0.000, surface_dev_tight +0.004
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Vit Kopriva vs Zizou Bergs -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200240:200267:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zizou Bergs (`KXATPMATCH-26OCT06KOPBER-BER`) | 0.71 / 0.75 (517) | 73.0% | -- | 64.9% | 65.4% [64.4%-66.3%] | -- | -- | -- | -- | PASS | -7.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vit Kopriva (`KXATPMATCH-26OCT06KOPBER-KOP`) | 0.25 / 0.28 (51) | 26.5% | -- | 35.1% | 34.6% [33.7%-35.6%] | -- | -- | -- | -- | PASS | +8.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6147.0, B 5734.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0094
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.009, surface_dev_loose -0.004, surface_dev_tight +0.004
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aleksandar Kovacevic vs Matteo Berrettini -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126610:206499:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Berrettini (`KXATPMATCH-26OCT06KOVBER-BER`) | 0.66 / 0.70 (109) | 68.0% | -- | 64.4% | 65.2% [61.3%-73.3%] | -- | -- | -- | -- | PASS | -2.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aleksandar Kovacevic (`KXATPMATCH-26OCT06KOVBER-KOV`) | 0.29 / 0.33 (100) | 31.0% | -- | 35.6% | 34.8% [26.7%-38.7%] | -- | -- | -- | -- | PASS | +3.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 7809.0, B 4565.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0598
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.037, surface_pool_high +0.039, surface_dev_loose +0.005, surface_dev_tight -0.013
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Martin Landaluce vs Jan-Lennard Struff -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105526:212021:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Landaluce (`KXATPMATCH-26OCT06LANSTR-LAN`) | 0.49 / 0.54 (249) | 51.5% | -- | 56.0% | 56.0% [49.5%-57.9%] | -- | -- | -- | -- | PASS | +4.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26OCT06LANSTR-STR`) | 0.46 / 0.50 (150) | 48.0% | -- | 44.0% | 44.0% [42.1%-50.5%] | -- | -- | -- | -- | PASS | -4.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5793.0, B 5447.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0421
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.025, surface_pool_high +0.020, surface_dev_loose +0.020, surface_dev_tight -0.030
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Fabian Marozsan vs Zachary Svajda -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:206681:208260:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fabian Marozsan (`KXATPMATCH-26OCT06MARSVA-MAR`) | 0.51 / 0.55 (238) | 53.0% | -- | 51.0% | 50.5% [48.5%-53.0%] | -- | -- | -- | -- | PASS | -2.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zachary Svajda (`KXATPMATCH-26OCT06MARSVA-SVA`) | 0.44 / 0.48 (100) | 46.0% | -- | 49.0% | 49.5% [47.0%-51.5%] | -- | -- | -- | -- | PASS | +3.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5713.0, B 5850.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0224
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose -0.005, surface_dev_tight +0.010
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jaume Munar vs Jenson Brooksby -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144719:202385:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jenson Brooksby (`KXATPMATCH-26OCT06MUNBRO-BRO`) | 0.36 / 0.40 (124) | 38.0% | -- | 23.2% | 33.0% [28.5%-38.6%] | -- | -- | -- | -- | PASS | -5.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jaume Munar (`KXATPMATCH-26OCT06MUNBRO-MUN`) | 0.59 / 0.63 (117) | 61.0% | -- | 76.8% | 67.0% [61.4%-71.5%] | -- | -- | -- | -- | PASS | +6.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4944.0, B 3246.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0503
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.036, surface_pool_high -0.028, surface_dev_loose +0.008, surface_dev_tight -0.009
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Mariano Navone vs Pablo Carreno Busta -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105807:208363:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pablo Carreno Busta (`KXATPMATCH-26OCT06NAVCAR-CAR`) | 0.52 / 0.57 (309) | 54.5% | -- | 54.1% | 55.7% [53.6%-57.7%] | -- | -- | -- | -- | PASS | +1.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mariano Navone (`KXATPMATCH-26OCT06NAVCAR-NAV`) | 0.44 / 0.47 (100) | 45.5% | -- | 45.9% | 44.3% [42.3%-46.4%] | -- | -- | -- | -- | PASS | -1.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 7341.0, B 5558.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0204
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose -0.020, surface_dev_tight +0.021
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cameron Norrie vs Denis Shapovalov -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111815:133430:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cameron Norrie (`KXATPMATCH-26OCT06NORSHA-NOR`) | 0.41 / 0.46 (100) | 43.5% | -- | 49.5% | 49.5% [48.5%-52.0%] | -- | -- | -- | -- | PASS | +6.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Denis Shapovalov (`KXATPMATCH-26OCT06NORSHA-SHA`) | 0.53 / 0.57 (330) | 55.0% | -- | 50.5% | 50.5% [48.0%-51.5%] | -- | -- | -- | -- | PASS | -4.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 7079.0, B 4723.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0175
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Holger Rune vs Daniel Altmaier -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:127157:208029:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Altmaier (`KXATPMATCH-26OCT06RUNALT-ALT`) | 0.29 / 0.32 (110) | 30.5% | -- | 17.4% | 17.7% [16.2%-25.4%] | -- | -- | -- | -- | PASS | -12.8 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Holger Rune (`KXATPMATCH-26OCT06RUNALT-RUN`) | 0.69 / 0.71 (600) | 70.0% | -- | 82.6% | 82.3% [74.6%-83.8%] | -- | -- | -- | -- | PASS | +12.3 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 7291.0, B 7026.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0463
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.006, surface_pool_high +0.006, surface_dev_loose +0.015, surface_dev_tight -0.013
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sho Shimabukuro vs Miomir Kecmanovic -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200175:200647:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miomir Kecmanovic (`KXATPMATCH-26OCT06SHIKEC-KEC`) | 0.62 / 0.65 (100) | 63.5% | -- | 66.5% | 66.1% [64.2%-67.0%] | -- | -- | -- | -- | PASS | +2.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sho Shimabukuro (`KXATPMATCH-26OCT06SHIKEC-SHI`) | 0.34 / 0.37 (100) | 35.5% | -- | 33.5% | 33.9% [33.0%-35.8%] | -- | -- | -- | -- | PASS | -1.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6423.0, B 6495.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0137
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose +0.005, surface_dev_tight +0.004
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Thiago Agustin Tirante vs Hamad Medjedovic -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:202058:209098:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hamad Medjedovic (`KXATPMATCH-26OCT06TIRMED-MED`) | 0.43 / 0.47 (207) | 45.0% | -- | 47.1% | 48.5% [47.6%-52.0%] | -- | -- | -- | -- | PASS | +3.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thiago Agustin Tirante (`KXATPMATCH-26OCT06TIRMED-TIR`) | 0.54 / 0.55 (100) | 54.5% | -- | 52.9% | 51.4% [48.0%-52.4%] | -- | -- | -- | -- | PASS | -3.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 7139.0, B 5689.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0218
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose +0.010, surface_dev_tight -0.015
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Adolfo Daniel Vallejo vs Valentin Royer -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208316:209226:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentin Royer (`KXATPMATCH-26OCT06VALROY-ROY`) | 0.43 / 0.47 (100) | 45.0% | -- | 49.0% | 50.0% [48.5%-51.5%] | -- | -- | -- | -- | PASS | +5.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Adolfo Daniel Vallejo (`KXATPMATCH-26OCT06VALROY-VAL`) | 0.52 / 0.57 (302) | 54.5% | -- | 51.0% | 50.0% [48.5%-51.5%] | -- | -- | -- | -- | PASS | -4.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5913.0, B 6682.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0154
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose -0.015, surface_dev_tight +0.015
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Botic Van de Zandschulp vs Daniel Merida -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT06VANMER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Merida (`KXATPMATCH-26OCT06VANMER-MER`) | 0.49 / 0.52 (168) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Botic Van de Zandschulp (`KXATPMATCH-26OCT06VANMER-VAN`) | 0.47 / 0.50 (50) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Luca Van Assche vs Yunchaokete Bu -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT06VANYUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luca Van Assche (`KXATPMATCH-26OCT06VANYUN-VAN`) | 0.35 / 0.37 (100) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yunchaokete Bu (`KXATPMATCH-26OCT06VANYUN-YUN`) | 0.61 / 0.63 (42) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Zhizhen Zhang vs Tomas Machac -- ATP Shanghai R128

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-07T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-10-06T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111190:207830:2026-10-06`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Machac (`KXATPMATCH-26OCT06ZHAMAC-MAC`) | 0.66 / 0.70 (100) | 68.0% | -- | 72.0% | 74.8% [73.7%-77.1%] | -- | -- | -- | -- | PASS | +6.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zhizhen Zhang (`KXATPMATCH-26OCT06ZHAMAC-ZHA`) | 0.29 / 0.33 (100) | 31.0% | -- | 28.0% | 25.2% [22.9%-26.3%] | -- | -- | -- | -- | PASS | -5.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4221.0, B 5769.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0172
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.015, surface_dev_loose -0.007, surface_dev_tight +0.003
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arakawa / Uemura vs Muramatsu / Sato -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05ARAUEMMURSAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arakawa / Uemura (`KXITFWDOUBLES-26OCT05ARAUEMMURSAT-ARAUEM`) | 0.06 / 0.63 (69) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Muramatsu / Sato (`KXITFWDOUBLES-26OCT05ARAUEMMURSAT-MURSAT`) | 0.06 / 0.60 (64) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Carbis / Swarbrick vs Schwarz / Schwarz -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05CARSWASCHSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carbis / Swarbrick (`KXITFWDOUBLES-26OCT05CARSWASCHSCH-CARSWA`) | 0.06 / 0.90 (50) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Schwarz / Schwarz (`KXITFWDOUBLES-26OCT05CARSWASCHSCH-SCHSCH`) | 0.06 / 0.90 (50) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Kitahara / Wen Wan vs Barry / Sawashiro -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05KITWENBARSAW:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barry / Sawashiro (`KXITFWDOUBLES-26OCT05KITWENBARSAW-BARSAW`) | 0.06 / 0.55 (57) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kitahara / Wen Wan (`KXITFWDOUBLES-26OCT05KITWENBARSAW-KITWEN`) | 0.06 / 0.68 (81) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Stevens / Thompson vs Aulia / Sibai -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05STETHOAULSIB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aulia / Sibai (`KXITFWDOUBLES-26OCT05STETHOAULSIB-AULSIB`) | 0.06 / 0.28 (34) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stevens / Thompson (`KXITFWDOUBLES-26OCT05STETHOAULSIB-STETHO`) | 0.06 / 0.90 (50) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Daria Egorova vs Guyu Xu -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05EGOXUX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Egorova (`KXITFWMATCH-26OCT05EGOXUX-EGO`) | 0.76 / 0.95 (142) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Guyu Xu (`KXITFWMATCH-26OCT05EGOXUX-XUX`) | 0.05 / 0.06 (26) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Junlu Sun vs Fang An Lin -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05SUNLIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fang An Lin (`KXITFWMATCH-26OCT05SUNLIN-LIN`) | 0.69 / 0.70 (7) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Junlu Sun (`KXITFWMATCH-26OCT05SUNLIN-SUN`) | 0.22 / 0.33 (18) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Satima Toregen vs Phitchayaphak Srimuk -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05TORSRI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Phitchayaphak Srimuk (`KXITFWMATCH-26OCT05TORSRI-SRI`) | 0.05 / 0.22 (32) | 13.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Satima Toregen (`KXITFWMATCH-26OCT05TORSRI-TOR`) | 0.23 / 0.95 (142) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kunwei Wang vs Jiumeng Liu -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05WANLIU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiumeng Liu (`KXITFWMATCH-26OCT05WANLIU-LIU`) | 0.05 / 0.95 (164) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kunwei Wang (`KXITFWMATCH-26OCT05WANLIU-WAN`) | 0.05 / 0.95 (142) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sander Arends / David Pel vs Julian Cash / Lloyd Glasspool -- ATP Beijing F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 11:00Z
* Current expected start: 2026-10-06 08:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 07:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-06T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT06AREPELCASGLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sander Arends / David Pel (`KXATPDOUBLES-26OCT06AREPELCASGLA-AREPEL`) | 0.06 / 0.90 (15) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Julian Cash / Lloyd Glasspool (`KXATPDOUBLES-26OCT06AREPELCASGLA-CASGLA`) | 0.06 / 0.90 (15) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jake Dembo vs Lingxi Zhao -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05DEMZHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Dembo (`KXITFMATCH-26OCT05DEMZHA-DEM`) | 0.17 / 0.37 (40) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lingxi Zhao (`KXITFMATCH-26OCT05DEMZHA-ZHA`) | 0.62 / 0.79 (62) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zhenxiong Dong vs Xin Zhou -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05DONZHO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zhenxiong Dong (`KXITFMATCH-26OCT05DONZHO-DON`) | 0.58 / 0.80 (46) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xin Zhou (`KXITFMATCH-26OCT05DONZHO-ZHO`) | 0.16 / 0.35 (39) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Markus Malaszszak vs Ko Suzuki -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05MALSUZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Markus Malaszszak (`KXITFMATCH-26OCT05MALSUZ-MAL`) | 0.56 / 0.79 (62) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ko Suzuki (`KXITFMATCH-26OCT05MALSUZ-SUZ`) | 0.14 / 0.35 (39) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## James Van Herzeele vs Anthony Susanto -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05VANSUS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anthony Susanto (`KXITFMATCH-26OCT05VANSUS-SUS`) | 0.12 / 0.36 (79) | 24.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| James Van Herzeele (`KXITFMATCH-26OCT05VANSUS-VAN`) | 0.55 / 0.82 (139) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adams / Dodaj vs Beck / Russell -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05ADADODBECRUS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adams / Dodaj (`KXITFWDOUBLES-26OCT05ADADODBECRUS-ADADOD`) | 0.06 / 0.44 (44) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Beck / Russell (`KXITFWDOUBLES-26OCT05ADADODBECRUS-BECRUS`) | 0.06 / 0.78 (117) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Arakawa / Nishimoto vs Danilova / Di Tommaso -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05ARANISDANDIT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arakawa / Nishimoto (`KXITFWDOUBLES-26OCT05ARANISDANDIT-ARANIS`) | 0.06 / 0.90 (50) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Danilova / Di Tommaso (`KXITFWDOUBLES-26OCT05ARANISDANDIT-DANDIT`) | 0.06 / 0.27 (34) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Khan / McKenzie vs Bond-Scott / Mickoska -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05KHAMCKBONMIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bond-Scott / Mickoska (`KXITFWDOUBLES-26OCT05KHAMCKBONMIC-BONMIC`) | 0.06 / 0.27 (34) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Khan / McKenzie (`KXITFWDOUBLES-26OCT05KHAMCKBONMIC-KHAMCK`) | 0.06 / 0.90 (50) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Kosaka / Liu vs Hosoki / Sato -- W35 Wagga Wagga R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-06T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05KOSLIUHOSSAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hosoki / Sato (`KXITFWDOUBLES-26OCT05KOSLIUHOSSAT-HOSSAT`) | 0.06 / 0.72 (92) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kosaka / Liu (`KXITFWDOUBLES-26OCT05KOSLIUHOSSAT-KOSLIU`) | 0.06 / 0.51 (53) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Sinja Kraus vs Nikola Bartunkova -- WTA Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-06 08:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 07:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-06T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT05KRABAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikola Bartunkova (`KXWTAMATCH-26OCT05KRABAR-BAR`) | 0.81 / 0.82 (16946) | 81.5% | -- | -- | -- [-----] | 78.6% | 81.3% | 80.0% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sinja Kraus (`KXWTAMATCH-26OCT05KRABAR-KRA`) | 0.18 / 0.19 (1) | 18.5% | -- | -- | -- [-----] | 21.4% | 19.1% | 20.2% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ellen Perez / Demi Schuurs vs Cristina Bucsa / Nicole Melichar-Martinez -- WTA Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 11:10Z
* Current expected start: 2026-10-06 08:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 07:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-06T11:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06PERSCHBUCMEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Bucsa / Nicole Melichar-Martinez (`KXWTADOUBLES-26OCT06PERSCHBUCMEL-BUCMEL`) | 0.47 / 0.52 (194) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ellen Perez / Demi Schuurs (`KXWTADOUBLES-26OCT06PERSCHBUCMEL-PERSCH`) | 0.47 / 0.52 (280) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Sydney-Nicole Clarke vs Xiao Tang -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05CLATAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sydney-Nicole Clarke (`KXITFWMATCH-26OCT05CLATAN-CLA`) | 0.05 / 0.95 (164) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xiao Tang (`KXITFWMATCH-26OCT05CLATAN-TAN`) | 0.05 / 0.95 (142) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Meiqi Guo vs Sarah Ye -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05GUOYEX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Meiqi Guo (`KXITFWMATCH-26OCT05GUOYEX-GUO`) | 0.05 / 0.85 (22) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sarah Ye (`KXITFWMATCH-26OCT05GUOYEX-YEX`) | 0.05 / 0.94 (416) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Albina Kakenova vs Kanna Soeda -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05KAKSOE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Albina Kakenova (`KXITFWMATCH-26OCT05KAKSOE-KAK`) | 0.05 / 0.95 (234) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kanna Soeda (`KXITFWMATCH-26OCT05KAKSOE-SOE`) | 0.05 / 0.95 (162) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ekaterina Kuznetsova vs Soo Ha Jang -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05KUZJAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Soo Ha Jang (`KXITFWMATCH-26OCT05KUZJAN-JAN`) | 0.05 / 0.94 (416) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ekaterina Kuznetsova (`KXITFWMATCH-26OCT05KUZJAN-KUZ`) | 0.05 / 0.86 (229) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carlos Alcaraz vs Jiri Lehecka -- ATP Tokyo F

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 12:00Z
* Current expected start: 2026-10-06 09:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 08:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-06T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT06ALCLEH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlos Alcaraz (`KXATPMATCH-26OCT06ALCLEH-ALC`) | 0.77 / 0.80 (36) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jiri Lehecka (`KXATPMATCH-26OCT06ALCLEH-LEH`) | 0.19 / 0.22 (1) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ulrikke Eikeri / Quinn Gleason vs Gabriela Dabrowski / Luisa Stefani -- WTA Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-06 12:20Z
* Current expected start: 2026-10-06 09:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-05 12:17Z
* Recommended handicap-by time: 2026-10-06 08:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-06T12:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT06EIKGLEDABSTE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela Dabrowski / Luisa Stefani (`KXWTADOUBLES-26OCT06EIKGLEDABSTE-DABSTE`) | 0.78 / 0.82 (896) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ulrikke Eikeri / Quinn Gleason (`KXWTADOUBLES-26OCT06EIKGLEDABSTE-EIKGLE`) | 0.18 / 0.21 (150) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Boris Butulija vs Siu Chi Nicholas Cheng -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05BUTCHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boris Butulija (`KXITFMATCH-26OCT05BUTCHE-BUT`) | 0.29 / 0.79 (0) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Siu Chi Nicholas Cheng (`KXITFMATCH-26OCT05BUTCHE-CHE`) | 0.05 / 0.32 (37) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tin Chen vs Yua Taka -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05CHETAK:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tin Chen (`KXITFMATCH-26OCT05CHETAK-CHE`) | 0.05 / 0.81 (132) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yua Taka (`KXITFMATCH-26OCT05CHETAK-TAK`) | 0.14 / 0.84 (0) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jordan Chiu vs Lin Hao-Yu -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05CHIHAO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jordan Chiu (`KXITFMATCH-26OCT05CHIHAO-CHI`) | 0.49 / 0.75 (0) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lin Hao-Yu (`KXITFMATCH-26OCT05CHIHAO-HAO`) | 0.19 / 0.44 (45) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maxim Shin vs Tomohiro Masabayashi -- M25 Luan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT05SHIMAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomohiro Masabayashi (`KXITFMATCH-26OCT05SHIMAS-MAS`) | 0.19 / 0.82 (0) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maxim Shin (`KXITFMATCH-26OCT05SHIMAS-SHI`) | 0.05 / 0.70 (83) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yiru Chen vs Meiling Wang -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05CHEWAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yiru Chen (`KXITFWMATCH-26OCT05CHEWAN-CHE`) | 0.05 / 0.94 (438) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Meiling Wang (`KXITFWMATCH-26OCT05CHEWAN-WAN`) | 0.05 / 0.94 (416) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## aoyi li vs Francesca Franchi -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05LIXFRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Franchi (`KXITFWMATCH-26OCT05LIXFRA-FRA`) | 0.05 / 0.95 (164) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| aoyi li (`KXITFWMATCH-26OCT05LIXFRA-LIX`) | 0.05 / 0.95 (142) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ke Ren vs Mariya Zharkikh -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05RENZHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ke Ren (`KXITFWMATCH-26OCT05RENZHA-REN`) | 0.05 / 0.95 (164) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mariya Zharkikh (`KXITFWMATCH-26OCT05RENZHA-ZHA`) | 0.05 / 0.95 (142) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marianna Shikhanova vs Jiarui Sun -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-06 09:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-06T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT05SHISUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marianna Shikhanova (`KXITFWMATCH-26OCT05SHISUN-SHI`) | 0.05 / 0.95 (164) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jiarui Sun (`KXITFWMATCH-26OCT05SHISUN-SUN`) | 0.05 / 0.95 (142) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
