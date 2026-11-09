# ASSISTED SLATE -- 2026-11-09T19:32Z (`SL-20261109T193224Z-219b0fa4`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

305 open matches not seen started, 716 markets. Skipped: {"first_ball_already_observed": 4}. Sources: shadow board 2026-11-09T19:11:04.784523+00:00, Model 4 2026-11-09T19:12:05.902287+00:00, Gen-1 ledger 2026-11-09T19:11:00.658901+00:00, external 2026-11-09T18:37:25.363877+00:00, capture 20261109T183539Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-11-09 20:00Z**
* Recommended RUN TENNIS time: **2026-11-09 19:15Z**  (**OVERDUE -- run now**)
* Final price/status check time: **2026-11-09 19:50Z**
* Number of matches in window: 2 (Aryna Sabalenka vs Karolina Muchova, Mirra Andreeva vs Elina Svitolina)

* **1 main-tour match(es) have NO verified start status** (STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-11-09T19:32Z. Refresh due by: 2026-11-09 19:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 62, "HIGH_REVIEW": 69, "NORMAL": 291, "REVIEW": 69, "UNPRICED": 225}; match winners: {"EXTREME": 61, "HIGH_REVIEW": 62, "NORMAL": 211, "REVIEW": 56, "UNPRICED": 220}; quote freshness at build: {"STALE": 491}.

## Billy Harris vs Liam Broady -- ATP Challenger Matsuyama 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106281:126129:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liam Broady (`KXATPCHALLENGERMATCH-26NOV08HARBRO-BRO`) | 0.08 / 0.09 (33211) | 8.5% | 51.1% | 72.7% | 68.8% [61.9%-71.9%] | 44.6% | -- | 44.6% | MODEL_LONE_OUTLIER | WATCH | +42.6 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Billy Harris (`KXATPCHALLENGERMATCH-26NOV08HARBRO-HAR`) | 0.91 / 0.92 (22547) | 91.5% | 48.9% | 27.3% | 31.1% [28.1%-38.1%] | 55.4% | -- | 55.4% | MODEL_LONE_OUTLIER | PASS | -42.6 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 5763.0, B 4666.0; serve-point win A 62.5%, B 37.3%; Elo A 1614.3, B 1640.6; model uncertainty 0.0499
* Form inputs: days since last match A 13, B 13; matches on record A 638, B 951; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV08HARBRO-BRO  (YES = Liam Broady)
Model: 51%
Kalshi: 8%
Gap: +43 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.009, surface_dev_loose -0.004, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE

## Gonzalo Bueno vs Thiago Seyboth Wild -- ATP Challenger Lima 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:205734:208293:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gonzalo Bueno (`KXATPCHALLENGERMATCH-26NOV09BUESEY-BUE`) | 0.15 / 0.22 (1) | 18.5% | 22.2% | 12.7% | 16.4% [13.7%-20.9%] | -- | -- | -- | -- | PASS | +3.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thiago Seyboth Wild (`KXATPCHALLENGERMATCH-26NOV09BUESEY-SEY`) | 0.79 / 0.85 (1) | 82.0% | 77.8% | 87.3% | 83.6% [79.1%-86.3%] | -- | -- | -- | -- | PASS | -4.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4995.0, B 4983.0; serve-point win A 57.7%, B 36.4%; Elo A 1668.7, B 1787.4; model uncertainty 0.0358
* Form inputs: days since last match A 7, B 7; matches on record A 324, B 515; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.009, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Marco Cecchinato vs Francisco Comesana -- ATP Challenger Lima 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106065:207681:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marco Cecchinato (`KXATPCHALLENGERMATCH-26NOV09CECCOM-CEC`) | 0.40 / 0.45 (0) | 42.5% | 40.2% | 53.0% | 49.0% [44.5%-51.5%] | -- | -- | -- | -- | PASS | -2.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Francisco Comesana (`KXATPCHALLENGERMATCH-26NOV09CECCOM-COM`) | 0.52 / 0.57 (0) | 54.5% | 59.8% | 47.0% | 51.0% [48.5%-55.5%] | -- | -- | -- | -- | PASS | +5.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5798.0, B 5187.0; serve-point win A 62.0%, B 36.0%; Elo A 1694.4, B 1795.1; model uncertainty 0.0351
* Form inputs: days since last match A 7, B 7; matches on record A 998, B 466; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.015, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Liam Draxl vs Duncan Chan -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208119:211673:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Duncan Chan (`KXATPCHALLENGERMATCH-26NOV09DRACHA-CHA`) | 0.22 / 0.23 (326) | 22.5% | 16.4% | 19.8% | 16.1% [15.2%-17.1%] | -- | 23.4% | 23.4% | MODEL_LONE_OUTLIER | PASS | -6.1 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Liam Draxl (`KXATPCHALLENGERMATCH-26NOV09DRACHA-DRA`) | 0.76 / 0.78 (526) | 77.0% | 83.6% | 80.2% | 83.9% [82.9%-84.8%] | -- | 77.0% | 77.0% | MODEL_LONE_OUTLIER | WATCH | +6.6 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4913.0, B 890.0; serve-point win A 64.4%, B 43.2%; Elo A 1731.9, B 1418.0; model uncertainty 0.0094
* Form inputs: days since last match A 7, B 42; matches on record A 379, B 28; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.003, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Alexis Galarneau vs Stefan Kozlov -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111578:200008:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexis Galarneau (`KXATPCHALLENGERMATCH-26NOV09GALKOZ-GAL`) | 0.43 / 0.45 (23) | 44.0% | 44.7% | 37.8% | 43.3% [40.7%-46.4%] | -- | -- | -- | -- | PASS | +0.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefan Kozlov (`KXATPCHALLENGERMATCH-26NOV09GALKOZ-KOZ`) | 0.53 / 0.56 (0) | 54.5% | 55.3% | 62.2% | 56.7% [53.6%-59.3%] | -- | -- | -- | -- | PASS | +0.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5286.0, B 3794.0; serve-point win A 58.9%, B 40.1%; Elo A 1665.3, B 1616.3; model uncertainty 0.0282
* Form inputs: days since last match A 7, B 7; matches on record A 439, B 624; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Marcos Giron vs Maks Kasnikowski -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106218:209874:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcos Giron (`KXATPCHALLENGERMATCH-26NOV09GIRKAS-GIR`) | 0.64 / 0.66 (0) | 65.0% | 57.4% | 41.1% | 48.5% [45.1%-53.0%] | -- | -- | -- | -- | PASS | -7.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maks Kasnikowski (`KXATPCHALLENGERMATCH-26NOV09GIRKAS-KAS`) | 0.34 / 0.37 (0) | 35.5% | 42.6% | 58.9% | 51.5% [47.0%-54.9%] | -- | -- | -- | -- | PASS | +7.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4834.0, B 5094.0; serve-point win A 65.2%, B 36.3%; Elo A 1783.5, B 1627.3; model uncertainty 0.0396
* Form inputs: days since last match A 7, B 7; matches on record A 726, B 330; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.015, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Alastair Gray vs Darwin Blanch -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202400:210464:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Darwin Blanch (`KXATPCHALLENGERMATCH-26NOV09GRABLA-BLA`) | 0.68 / 0.75 (4) | 71.5% | 64.6% | 46.6% | 51.5% [48.5%-56.4%] | -- | -- | -- | -- | PASS | -6.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alastair Gray (`KXATPCHALLENGERMATCH-26NOV09GRABLA-GRA`) | 0.22 / 0.28 (0) | 25.0% | 35.4% | 53.4% | 48.5% [43.6%-51.5%] | -- | -- | -- | -- | PASS | +10.4 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3404.0, B 4786.0; serve-point win A 63.9%, B 33.0%; Elo A 1582.8, B 1676.5; model uncertainty 0.0392
* Form inputs: days since last match A 7, B 7; matches on record A 328, B 183; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Zdenek Kolar vs Joao Lucas Reis Da Silva -- ATP Challenger Lima 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144645:206307:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zdenek Kolar (`KXATPCHALLENGERMATCH-26NOV09KOLREI-KOL`) | 0.25 / 0.28 (0) | 26.5% | 37.5% | 44.9% | 44.4% [43.8%-45.4%] | -- | -- | -- | -- | PASS | +11.0 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joao Lucas Reis Da Silva (`KXATPCHALLENGERMATCH-26NOV09KOLREI-REI`) | 0.68 / 0.73 (0) | 70.5% | 62.5% | 55.1% | 55.6% [54.6%-56.2%] | -- | -- | -- | -- | PASS | -8.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5408.0, B 5010.0; serve-point win A 58.9%, B 38.7%; Elo A 1614.3, B 1671.7; model uncertainty 0.0077
* Form inputs: days since last match A 7, B 7; matches on record A 839, B 485; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Sandro Kopp vs Luka Mikrut -- ATP Challenger Monastir 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207491:210053:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sandro Kopp (`KXATPCHALLENGERMATCH-26NOV09KOPMIK-KOP`) | 0.01 / 0.02 (43476) | 1.5% | 32.1% | 44.0% | 42.1% [37.7%-46.0%] | -- | 28.6% | 28.6% | MODEL_LONE_OUTLIER | PASS | +30.6 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Luka Mikrut (`KXATPCHALLENGERMATCH-26NOV09KOPMIK-MIK`) | 0.98 / 0.99 (75768) | 98.5% | 67.8% | 56.0% | 57.9% [54.0%-62.3%] | -- | 71.7% | 71.7% | MODEL_LONE_OUTLIER | PASS | -30.6 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 4878.0, B 3647.0; serve-point win A 62.3%, B 34.0%; Elo A 1470.1, B 1555.9; model uncertainty 0.0418
* Form inputs: days since last match A 21, B 28; matches on record A 416, B 241; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV09KOPMIK-KOP  (YES = Sandro Kopp)
Model: 32%
Kalshi: 2%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_MODEL
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.040, surface_dev_tight -0.029
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Marcel Latak vs Clement Chidekh -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206889:214269:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clement Chidekh (`KXATPCHALLENGERMATCH-26NOV09LATCHI-CHI`) | 0.94 / 0.96 (2652) | 95.0% | 96.5% | 94.3% | 93.2% [92.1%-93.8%] | -- | 95.8% | 95.8% | MODEL_LONE_OUTLIER | PASS | +1.5 pp | NORMAL | STALE | F / POOR | ALL_AGREE | VERIFIED |
| Marcel Latak (`KXATPCHALLENGERMATCH-26NOV09LATCHI-LAT`) | 0.04 / 0.06 (5350) | 5.0% | 3.5% | 5.7% | 6.8% [6.2%-7.9%] | -- | 4.5% | 4.5% | MODEL_LONE_OUTLIER | PASS | -1.5 pp | NORMAL | STALE | F / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 53.0, B 5095.0; serve-point win A 53.5%, B 32.4%; Elo A 1285.9, B 1736.3; model uncertainty 0.0086
* Form inputs: days since last match A 301, B 7; matches on record A 1, B 334; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.006, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Aidan Mayo vs Michael Mmoh -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111581:208854:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aidan Mayo (`KXATPCHALLENGERMATCH-26NOV09MAYMMO-MAY`) | 0.53 / 0.56 (2) | 54.5% | 42.7% | 60.5% | 51.5% [46.5%-55.5%] | -- | -- | -- | -- | PASS | -11.8 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Michael Mmoh (`KXATPCHALLENGERMATCH-26NOV09MAYMMO-MMO`) | 0.42 / 0.46 (0) | 44.0% | 57.3% | 39.5% | 48.5% [44.5%-53.5%] | -- | -- | -- | -- | PASS | +13.3 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4152.0, B 3733.0; serve-point win A 61.7%, B 36.8%; Elo A 1595.7, B 1744.1; model uncertainty 0.0454
* Form inputs: days since last match A 7, B 21; matches on record A 265, B 575; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.015, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Nicolas Mejia vs Jack Kennedy -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200711:213605:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Kennedy (`KXATPCHALLENGERMATCH-26NOV09MEJKEN-KEN`) | 0.37 / 0.38 (54) | 37.5% | 43.6% | 45.8% | 42.7% [37.3%-45.3%] | -- | 38.6% | 38.6% | MODEL_LONE_OUTLIER | WATCH | +6.1 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Nicolas Mejia (`KXATPCHALLENGERMATCH-26NOV09MEJKEN-MEJ`) | 0.61 / 0.63 (4781) | 62.0% | 56.4% | 54.2% | 57.3% [54.7%-62.7%] | -- | 62.2% | 62.2% | MODEL_LONE_OUTLIER | PASS | -5.6 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4996.0, B 2751.0; serve-point win A 59.0%, B 42.2%; Elo A 1626.5, B 1543.8; model uncertainty 0.0401
* Form inputs: days since last match A 7, B 203; matches on record A 512, B 51; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.015, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Facundo Mena vs Max Alcala Gurri -- ATP Challenger Lima 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106057:208024:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Alcala Gurri (`KXATPCHALLENGERMATCH-26NOV09MENALC-ALC`) | 0.69 / 0.71 (29) | 70.0% | 69.5% | 76.3% | 72.1% [66.6%-75.1%] | -- | 69.7% | 69.7% | MODEL_LONE_OUTLIER | PASS | -0.5 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Facundo Mena (`KXATPCHALLENGERMATCH-26NOV09MENALC-MEN`) | 0.29 / 0.31 (9041) | 30.0% | 30.5% | 23.7% | 27.9% [24.9%-33.4%] | -- | 30.6% | 30.6% | MODEL_LONE_OUTLIER | PASS | +0.5 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4853.0, B 5263.0; serve-point win A 57.0%, B 39.0%; Elo A 1633.8, B 1675.3; model uncertainty 0.0424
* Form inputs: days since last match A 21, B 21; matches on record A 943, B 385; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose -0.004, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Elmer Moller vs Genaro Alberto Olivieri -- ATP Challenger Lima 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144821:209284:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elmer Moller (`KXATPCHALLENGERMATCH-26NOV09MOLOLI-MOL`) | 0.67 / 0.69 (0) | 68.0% | 64.4% | 67.0% | 67.0% [66.5%-68.0%] | -- | -- | -- | -- | PASS | -3.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Genaro Alberto Olivieri (`KXATPCHALLENGERMATCH-26NOV09MOLOLI-OLI`) | 0.30 / 0.33 (0) | 31.5% | 35.6% | 33.0% | 33.0% [32.0%-33.5%] | -- | -- | -- | -- | PASS | +4.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4747.0, B 5176.0; serve-point win A 55.1%, B 47.7%; Elo A 1728.0, B 1588.2; model uncertainty 0.0074
* Form inputs: days since last match A 7, B 7; matches on record A 316, B 613; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Bernardo Munk Mesa vs Aziz Dougaz -- ATP Challenger Monastir 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144826:212827:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aziz Dougaz (`KXATPCHALLENGERMATCH-26NOV09MUNDOU-DOU`) | 0.99 / -- (0) | -- | 87.2% | 84.0% | 85.8% [84.3%-87.4%] | -- | 86.3% | 86.3% | MARKETS_AGREE | PASS | -- | UNPRICED | STALE | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Bernardo Munk Mesa (`KXATPCHALLENGERMATCH-26NOV09MUNDOU-MUN`) | -- / 0.01 (38106) | -- | 12.8% | 16.0% | 14.2% [12.6%-15.7%] | -- | 16.1% | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | STALE | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 814.0, B 2640.0; serve-point win A 59.6%, B 31.2%; Elo A 1292.7, B 1614.8; model uncertainty 0.0153
* Form inputs: days since last match A 308, B 22; matches on record A 18, B 656; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.014, surface_dev_loose -0.004, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

## Abdullah Shelbayh vs Harry Wendelken -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09SHEWEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abdullah Shelbayh (`KXATPCHALLENGERMATCH-26NOV09SHEWEN-SHE`) | 0.37 / 0.48 (0) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Harry Wendelken (`KXATPCHALLENGERMATCH-26NOV09SHEWEN-WEN`) | 0.48 / 0.55 (8) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Braden Shick vs Andres Andrade -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200748:211711:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andres Andrade (`KXATPCHALLENGERMATCH-26NOV09SHIAND-AND`) | 0.34 / 0.37 (0) | 35.5% | 64.1% | 57.7% | 60.2% [57.7%-65.0%] | -- | -- | -- | -- | PASS | +28.6 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Braden Shick (`KXATPCHALLENGERMATCH-26NOV09SHIAND-SHI`) | 0.65 / 0.66 (0) | 65.5% | 35.9% | 42.3% | 39.8% [34.9%-42.3%] | -- | -- | -- | -- | PASS | -29.6 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3074.0, B 4899.0; serve-point win A 58.8%, B 38.4%; Elo A 1547.1, B 1656.1; model uncertainty 0.0368
* Form inputs: days since last match A 7, B 7; matches on record A 102, B 306; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV09SHIAND-AND  (YES = Andres Andrade)
Model: 64%
Kalshi: 36%
Gap: +29 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.020, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Trevor Svajda vs Max Hans Rehberg -- ATP Challenger Knoxville 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208819:212216:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Hans Rehberg (`KXATPCHALLENGERMATCH-26NOV09SVAREH-REH`) | 0.59 / 0.60 (31) | 59.5% | 56.6% | 61.4% | 59.5% [56.0%-62.8%] | -- | 59.0% | 59.0% | MODEL_LONE_OUTLIER | PASS | -2.9 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Trevor Svajda (`KXATPCHALLENGERMATCH-26NOV09SVAREH-SVA`) | 0.39 / 0.40 (752) | 39.5% | 43.4% | 38.6% | 40.5% [37.2%-44.0%] | -- | 41.4% | 41.4% | MODEL_LONE_OUTLIER | PASS | +3.9 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1689.0, B 4177.0; serve-point win A 62.3%, B 36.4%; Elo A 1561.1, B 1610.0; model uncertainty 0.0341
* Form inputs: days since last match A 7, B 7; matches on record A 91, B 263; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.035, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Juan Pablo Varillas vs Marcelo Tomas Barrios Vera -- ATP Challenger Lima 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09VARBAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcelo Tomas Barrios Vera (`KXATPCHALLENGERMATCH-26NOV09VARBAR-BAR`) | 0.64 / 0.69 (0) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juan Pablo Varillas (`KXATPCHALLENGERMATCH-26NOV09VARBAR-VAR`) | 0.31 / 0.32 (19) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Fabio Manuel Zavalaga Uculmana vs Alex Barrena -- ATP Challenger Lima 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-09T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09ZAVBAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Barrena (`KXATPCHALLENGERMATCH-26NOV09ZAVBAR-BAR`) | 0.97 / 0.98 (604) | 97.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fabio Manuel Zavalaga Uculmana (`KXATPCHALLENGERMATCH-26NOV09ZAVBAR-ZAV`) | 0.02 / 0.03 (116) | 2.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE

## Leo Borg vs Toby Samuel -- ATP Stockholm R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-09 21:10Z
* Current expected start: 2026-11-09 18:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 18:39Z
* Recommended handicap-by time: 2026-11-09 17:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (TOUR_500_250) · Hard · scheduled 2026-11-09T21:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:209863:210389:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leo Borg (`KXATPMATCH-26NOV09BORSAM-BOR`) | 0.10 / 0.11 (988) | 10.5% | 16.6% | 16.8% | 15.9% [13.0%-17.1%] | -- | 10.2% | 10.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.1 pp | NORMAL | STALE | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Toby Samuel (`KXATPMATCH-26NOV09BORSAM-SAM`) | 0.89 / 0.90 (7346) | 89.5% | 83.4% | 83.2% | 84.1% [82.9%-87.0%] | -- | 89.7% | 89.7% | MODEL_LONE_OUTLIER | PASS | -6.1 pp | NORMAL | STALE | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3869.0, B 4150.0; serve-point win A 58.6%, B 33.8%; Elo A 1470.5, B 1799.7; model uncertainty 0.0206
* Form inputs: days since last match A 196, B 1; matches on record A 287, B 196; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.006, surface_pool_high +0.006, surface_dev_loose -0.006, surface_dev_tight +0.006
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26NOV09BORSAM-SAM9` Will Toby Samuel win at least 8.5 more games than Leo Borg?: 0.05/0.48 mid 26.5%, model 3.5% (projection_v2.0 (prediction ledger)) -- gap -23.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPGTOTAL-26NOV09BORSAM-20` Over 19.5 games: 0.45/0.47 mid 46.0%, model 68.1% (projection_v2.0 (prediction ledger)) -- gap +22.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPGSPREAD-26NOV09BORSAM-SAM6` Will Toby Samuel win at least 5.5 more games than Leo Borg?: 0.49/0.50 mid 49.5%, model 30.5% (projection_v2.0 (prediction ledger)) -- gap -19.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26NOV09BORSAM-SAM20` Will Toby Samuel win the Leo Borg vs Toby Samuel match by a set score of 2-0?: 0.69/0.71 mid 70.0%, model 55.0% (projection_v2.0 (prediction ledger)) -- gap -15.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPGTOTAL-26NOV09BORSAM-25` Over 24.5 games: 0.25/0.26 mid 25.5%, model 40.1% (projection_v2.0 (prediction ledger)) -- gap +14.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26NOV09BORSAM-SAM21` Will Toby Samuel win the Leo Borg vs Toby Samuel match by a set score of 2-1?: 0.18/0.19 mid 18.5%, model 28.4% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPGSPREAD-26NOV09BORSAM-SAM3` Will Toby Samuel win at least 2.5 more games than Leo Borg?: 0.78/0.85 mid 81.5%, model 72.3% (projection_v2.0 (prediction ledger)) -- gap -9.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPSETWINNER-26NOV09BORSAM-1-SAM` Will Toby Samuel win set 1 in the Leo Borg vs Toby Samuel match: 0.82/0.83 mid 82.5%, model 74.2% (projection_v2.0 (prediction ledger)) -- gap -8.3 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26NOV09BORSAM-1-BOR` Will Leo Borg win set 1 in the Leo Borg vs Toby Samuel match: 0.17/0.19 mid 18.0%, model 25.8% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
  * `KXATPGTOTAL-26NOV09BORSAM-15` Over 14.5 games: 0.91/0.93 mid 92.0%, model 99.0% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPEXACTMATCH-26NOV09BORSAM-BOR21` Will Leo Borg win the Leo Borg vs Toby Samuel match by a set score of 2-1?: 0.04/0.06 mid 5.0%, model 9.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXATPSETWINNER-26NOV09BORSAM-2-BOR` Will Leo Borg win set 2 in the Leo Borg vs Toby Samuel match: 0.18/0.24 mid 21.0%, model 25.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
  * `KXATPSETWINNER-26NOV09BORSAM-2-SAM` Will Toby Samuel win set 2 in the Leo Borg vs Toby Samuel match: 0.77/0.79 mid 78.0%, model 74.2% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
  * `KXATPEXACTMATCH-26NOV09BORSAM-BOR20` Will Leo Borg win the Leo Borg vs Toby Samuel match by a set score of 2-0?: 0.05/0.07 mid 6.0%, model 6.7% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Max Houkes vs Tom Gentzsch -- ATP Challenger Orleans 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208069:210167:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tom Gentzsch (`KXATPCHALLENGERMATCH-26NOV09HOUGEN-GEN`) | 0.42 / 0.43 (59783) | 42.5% | 56.3% | 35.0% | 41.6% [38.3%-50.0%] | -- | 70.5% | 70.5% | MODEL_LONE_OUTLIER | PASS | +13.8 pp | REVIEW | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Max Houkes (`KXATPCHALLENGERMATCH-26NOV09HOUGEN-HOU`) | 0.57 / 0.58 (56699) | 57.5% | 43.7% | 65.0% | 58.4% [50.0%-61.7%] | -- | 29.9% | 29.9% | MODEL_LONE_OUTLIER | PASS | -13.8 pp | REVIEW | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 4345.0, B 5173.0; serve-point win A 63.8%, B 34.9%; Elo A 1480.4, B 1563.1; model uncertainty 0.0586
* Form inputs: days since last match A 21, B 7; matches on record A 407, B 341; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.033, surface_dev_tight -0.034
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE

## Clement Tabur vs Lukas Neumayer -- ATP Challenger Orleans 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202127:209903:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lukas Neumayer (`KXATPCHALLENGERMATCH-26NOV09TABNEU-NEU`) | 0.28 / 0.29 (3018) | 28.5% | 43.4% | 37.7% | 38.2% [37.2%-40.1%] | -- | 31.1% | 31.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +14.9 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Clement Tabur (`KXATPCHALLENGERMATCH-26NOV09TABNEU-TAB`) | 0.71 / 0.72 (31921) | 71.5% | 56.6% | 62.3% | 61.8% [59.9%-62.8%] | -- | 68.3% | 68.3% | MODEL_LONE_OUTLIER | PASS | -14.9 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4961.0, B 5459.0; serve-point win A 64.2%, B 37.1%; Elo A 1657.5, B 1585.8; model uncertainty 0.0142
* Form inputs: days since last match A 14, B 15; matches on record A 502, B 410; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.009, surface_dev_loose +0.009, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE

## Tamara Zidansek vs Julia Grabher -- WTA Challenger Sopo 1/16 F

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-09 21:00Z
* Current expected start: 2026-11-09 18:50Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 18:39Z
* Recommended handicap-by time: 2026-11-09 18:05Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (CHALLENGER) · surface ? · scheduled 2026-11-09T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV09ZIDGRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Grabher (`KXWTACHALLENGERMATCH-26NOV09ZIDGRA-GRA`) | 0.52 / 0.53 (7577) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tamara Zidansek (`KXWTACHALLENGERMATCH-26NOV09ZIDGRA-ZID`) | 0.47 / 0.48 (4628) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; STALE_QUOTE

## Yannik Kelm / Mika Petkovic vs Adam Nagoudi / Kasra Rahmani -- ATP Challenger Monastir 1/8 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-09T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09KELPETNAGRAH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yannik Kelm / Mika Petkovic (`KXATPCHALLENGERDOUBLES-26NOV09KELPETNAGRAH-KELPET`) | 0.37 / 0.46 (0) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Adam Nagoudi / Kasra Rahmani (`KXATPCHALLENGERDOUBLES-26NOV09KELPETNAGRAH-NAGRAH`) | 0.52 / 0.58 (48) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Oriol Roca Batalla vs Alex Hernandez -- ATP Challenger Lima F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-09T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09ROCHER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Hernandez (`KXATPCHALLENGERMATCH-26NOV09ROCHER-HER`) | -- / 0.01 (166261) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oriol Roca Batalla (`KXATPCHALLENGERMATCH-26NOV09ROCHER-ROC`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

## Irene Burillo Escorihuela vs Yuliana Lizarazo -- WTA Challenger Sopo 1/16 F

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-09 21:00Z
* Current expected start: 2026-11-09 19:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 18:39Z
* Recommended handicap-by time: 2026-11-09 18:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (CHALLENGER) · surface ? · scheduled 2026-11-09T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV09BURLIZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Irene Burillo Escorihuela (`KXWTACHALLENGERMATCH-26NOV09BURLIZ-BUR`) | 0.88 / 0.90 (122) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yuliana Lizarazo (`KXWTACHALLENGERMATCH-26NOV09BURLIZ-LIZ`) | 0.10 / 0.12 (1246) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; STALE_QUOTE

## Ozan Baris vs Patrick Zahraj -- ATP Challenger Knoxville F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200452:210028:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ozan Baris (`KXATPCHALLENGERMATCH-26NOV09BARZAH-BAR`) | 0.99 / -- (0) | -- | 42.5% | 44.3% | 41.7% [39.7%-43.2%] | -- | 62.0% | 62.0% | MODEL_LONE_OUTLIER | PASS | -- | UNPRICED | STALE | B / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |
| Patrick Zahraj (`KXATPCHALLENGERMATCH-26NOV09BARZAH-ZAH`) | -- / 0.01 (121969) | -- | 57.5% | 55.7% | 58.3% [56.8%-60.3%] | -- | 38.3% | 38.3% | MODEL_LONE_OUTLIER | WATCH | -- | UNPRICED | STALE | B / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 1236.0, B 3691.0; serve-point win A 57.8%, B 40.8%; Elo A 1405.9, B 1473.8; model uncertainty 0.0176
* Form inputs: days since last match A 14, B 77; matches on record A 93, B 228; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

## Nicolas Jarry vs Maximo Zeitune -- ATP Challenger Lima F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-09T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111797:212784:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Jarry (`KXATPCHALLENGERMATCH-26NOV09JARZEI-JAR`) | 0.81 / 0.85 (13) | 83.0% | 86.8% | 72.5% | 82.9% [79.3%-86.6%] | -- | 79.1% | 79.1% | MODEL_LONE_OUTLIER | PASS | +3.8 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |
| Maximo Zeitune (`KXATPCHALLENGERMATCH-26NOV09JARZEI-ZEI`) | 0.14 / 0.19 (114) | 16.5% | 13.2% | 27.5% | 17.1% [13.4%-20.7%] | -- | 21.2% | 21.2% | MODEL_LONE_OUTLIER | PASS | -3.3 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 2685.0, B 2288.0; serve-point win A 70.7%, B 38.5%; Elo A 1827.1, B 1371.7; model uncertainty 0.0366
* Form inputs: days since last match A 14, B 7; matches on record A 734, B 73; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.003, surface_dev_loose -0.003, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Timo Legout vs Emile Hudd -- ATP Challenger Knoxville F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209163:209355:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emile Hudd (`KXATPCHALLENGERMATCH-26NOV09LEGHUD-HUD`) | -- / 0.01 (144048) | -- | 39.9% | 44.9% | 41.9% [39.4%-43.4%] | -- | 16.6% | 16.6% | MODEL_LONE_OUTLIER | WATCH | -- | UNPRICED | STALE | B / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |
| Timo Legout (`KXATPCHALLENGERMATCH-26NOV09LEGHUD-LEG`) | 0.99 / -- (0) | -- | 60.1% | 55.1% | 58.1% [56.6%-60.6%] | -- | 82.7% | 82.7% | MODEL_LONE_OUTLIER | PASS | -- | UNPRICED | STALE | B / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 1269.0, B 3294.0; serve-point win A 62.1%, B 39.9%; Elo A 1562.6, B 1482.9; model uncertainty 0.0199
* Form inputs: days since last match A 14, B 77; matches on record A 185, B 173; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.015, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

## Filip Misolic vs Alan Magadan -- ATP Challenger Lima F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 19:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-09T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209209:209246:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alan Magadan (`KXATPCHALLENGERMATCH-26NOV09MISMAG-MAG`) | 0.07 / 0.08 (70980) | 7.5% | 11.1% | 18.6% | 12.8% [10.8%-14.8%] | -- | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +3.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Filip Misolic (`KXATPCHALLENGERMATCH-26NOV09MISMAG-MIS`) | 0.92 / 0.93 (27143) | 92.5% | 88.9% | 81.4% | 87.2% [85.2%-89.2%] | -- | 88.1% | 88.1% | MODEL_LONE_OUTLIER | PASS | -3.6 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3485.0, B 2107.0; serve-point win A 64.6%, B 44.9%; Elo A 1815.1, B 1361.6; model uncertainty 0.02
* Form inputs: days since last match A 7, B 7; matches on record A 332, B 86; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.010, surface_dev_loose +0.009, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE

## Sofia Costoulas vs Antonella Esquivel Usech -- WTA Challenger Sopo R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-09 19:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

WTA125 (CHALLENGER) · surface ? · scheduled 2026-11-09T19:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV09COSESQ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Costoulas (`KXWTACHALLENGERMATCH-26NOV09COSESQ-COS`) | 0.96 / 0.97 (113) | 96.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Antonella Esquivel Usech (`KXWTACHALLENGERMATCH-26NOV09COSESQ-ESQ`) | 0.01 / 0.06 (5) | 3.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Aryna Sabalenka vs Karolina Muchova -- WTA Finals (Women) RR

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-09 23:00Z
* Current expected start: 2026-11-09 20:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 18:39Z
* Recommended handicap-by time: 2026-11-09 19:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_FINALS) · Hard · scheduled 2026-11-09T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214096:214544:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karolina Muchova (`KXWTAMATCH-26NOV09SABMUC-MUC`) | 0.34 / 0.35 (244772) | 34.5% | 26.8% | 26.3% | 26.7% [26.3%-27.6%] | -- | 34.4% | 34.4% | MODEL_LONE_OUTLIER | PASS | -7.7 pp | NORMAL | STALE | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Aryna Sabalenka (`KXWTAMATCH-26NOV09SABMUC-SAB`) | 0.65 / 0.66 (122183) | 65.5% | 73.2% | 73.7% | 73.3% [72.4%-73.7%] | -- | 66.0% | 66.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.7 pp | NORMAL | STALE | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5768.0, B 3972.0; serve-point win A 64.7%, B 40.2%; Elo A 2284.6, B 2125.0; model uncertainty 0.0063
* Form inputs: days since last match A 26, B 25; matches on record A 719, B 482; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.008, surface_dev_loose -0.004, surface_dev_tight +0.001
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTASETWINNER-26NOV09SABMUC-1-MUC` Will Karolina Muchova win set 1 in the Aryna Sabalenka vs Karolina Muchova match: 0.38/0.39 mid 38.5%, model 34.0% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV09SABMUC-1-SAB` Will Aryna Sabalenka win set 1 in the Aryna Sabalenka vs Karolina Muchova match: 0.61/0.62 mid 61.5%, model 66.0% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26NOV09SABMUC-28` Over 27.5 games: 0.32/0.33 mid 32.5%, model 34.7% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26NOV09SABMUC-23` Over 22.5 games: 0.52/0.53 mid 52.5%, model 54.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26NOV09SABMUC-2-SAB` Will Aryna Sabalenka win set 2 in the Aryna Sabalenka vs Karolina Muchova match: 0.56/0.73 mid 64.5%, model 66.0% (projection_v2.0 (prediction ledger)) -- gap +1.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26NOV09SABMUC-18` Over 17.5 games: 0.86/0.90 mid 88.0%, model 89.4% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26NOV09SABMUC-2-MUC` Will Karolina Muchova win set 2 in the Aryna Sabalenka vs Karolina Muchova match: 0.27/0.42 mid 34.5%, model 34.0% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Luka Bojicic Ono vs Augusto Land -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09BOJLAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luka Bojicic Ono (`KXITFMATCH-26NOV09BOJLAN-BOJ`) | -- / 0.01 (203829) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Augusto Land (`KXITFMATCH-26NOV09BOJLAN-LAN`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Moise Kouame vs Robert Strombachs -- ATP Challenger Monastir 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207669:213608:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Moise Kouame (`KXATPCHALLENGERMATCH-26NOV09KOUSTR-KOU`) | 0.71 / 0.72 (1179) | 71.5% | 77.3% | 60.4% | 63.3% [62.8%-66.6%] | -- | 80.7% | 80.7% | MODEL_LONE_OUTLIER | PASS | +5.8 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Robert Strombachs (`KXATPCHALLENGERMATCH-26NOV09KOUSTR-STR`) | 0.28 / 0.29 (2) | 28.5% | 22.7% | 39.6% | 36.7% [33.4%-37.2%] | -- | 19.7% | 19.7% | MODEL_LONE_OUTLIER | SHADOW_BET | -5.8 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 3434.0, B 3313.0; serve-point win A 66.2%, B 39.7%; Elo A 1670.0, B 1526.7; model uncertainty 0.019
* Form inputs: days since last match A 6, B 56; matches on record A 88, B 461; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Sebastiano Cocola vs Daniel Aleksandar Amarandei -- M25 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 20:39Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-09T20:39:13Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213717:214198:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Aleksandar Amarandei (`KXITFMATCH-26NOV09COCAMA-AMA`) | 0.24 / 0.25 (7989) | 24.5% | 57.8% | 60.5% | 59.4% [58.3%-60.0%] | -- | -- | -- | -- | PASS | +33.3 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sebastiano Cocola (`KXITFMATCH-26NOV09COCAMA-COC`) | 0.75 / 0.76 (71) | 75.5% | 42.2% | 39.5% | 40.6% [40.0%-41.7%] | -- | -- | -- | -- | PASS | -33.3 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 734.0, B 329.0; serve-point win A 55.1%, B 43.4%; Elo A 1216.3, B 1281.6; model uncertainty 0.0086
* Form inputs: days since last match A 196, B 217; matches on record A 18, B 7; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09COCAMA-AMA  (YES = Daniel Aleksandar Amarandei)
Model: 58%
Kalshi: 24%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Benjamin Bonzi vs Andrea Pellegrino -- ATP Challenger Orleans 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126127:126504:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Bonzi (`KXATPCHALLENGERMATCH-26NOV09BONPEL-BON`) | 0.90 / 0.91 (2550) | 90.5% | 85.4% | 76.6% | 79.9% [77.8%-82.8%] | -- | 90.5% | 90.5% | MODEL_LONE_OUTLIER | PASS | -5.1 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Andrea Pellegrino (`KXATPCHALLENGERMATCH-26NOV09BONPEL-PEL`) | 0.09 / 0.10 (7725) | 9.5% | 14.6% | 23.4% | 20.1% [17.2%-22.2%] | -- | 10.4% | 10.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +5.1 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5541.0, B 4568.0; serve-point win A 68.0%, B 40.5%; Elo A 1833.6, B 1471.6; model uncertainty 0.0253
* Form inputs: days since last match A 6, B 21; matches on record A 803, B 643; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.014, surface_dev_loose +0.029, surface_dev_tight -0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Tomas Dummer Macedo vs Eduardo Heineberg -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09DUMHEI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Dummer Macedo (`KXITFMATCH-26NOV09DUMHEI-DUM`) | 0.90 / 0.91 (720) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eduardo Heineberg (`KXITFMATCH-26NOV09DUMHEI-HEI`) | 0.09 / 0.10 (20) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giles Hussey vs Geoffrey Blancaneaux -- ATP Challenger Knoxville F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144972:208144:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Geoffrey Blancaneaux (`KXATPCHALLENGERMATCH-26NOV09HUSBLA-BLA`) | 0.27 / 0.28 (184) | 27.5% | 40.2% | 33.6% | 35.0% [33.6%-39.9%] | -- | 43.9% | 43.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +12.7 pp | REVIEW | STALE | A / LIMITED | AGREES_WITH_MODEL | VERIFIED |
| Giles Hussey (`KXATPCHALLENGERMATCH-26NOV09HUSBLA-HUS`) | 0.72 / 0.73 (0) | 72.5% | 59.8% | 66.4% | 65.0% [60.1%-66.4%] | -- | 56.5% | 56.5% | MODEL_LONE_OUTLIER | PASS | -12.7 pp | REVIEW | STALE | A / LIMITED | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 4682.0, B 4227.0; serve-point win A 62.1%, B 39.8%; Elo A 1601.3, B 1526.1; model uncertainty 0.0314
* Form inputs: days since last match A 133, B 42; matches on record A 310, B 668; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.000, surface_dev_loose +0.004, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Daniel Milavsky vs Kenta (2004) Miyoshi -- ATP Challenger Knoxville F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-09T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09MILMIY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Milavsky (`KXATPCHALLENGERMATCH-26NOV09MILMIY-MIL`) | 0.60 / 0.61 (4147) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kenta (2004) Miyoshi (`KXATPCHALLENGERMATCH-26NOV09MILMIY-MIY`) | 0.39 / 0.40 (11808) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Mirra Andreeva vs Elina Svitolina -- WTA Finals (Women) RR

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-10 00:30Z
* Current expected start: 2026-11-09 21:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 18:39Z
* Recommended handicap-by time: 2026-11-09 20:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_FINALS) · Hard · scheduled 2026-11-10T00:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202494:259799:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mirra Andreeva (`KXWTAMATCH-26NOV09ANDSVI-AND`) | 0.64 / 0.65 (91971) | 64.5% | 56.1% | 60.4% | 56.3% [48.9%-58.8%] | -- | -- | -- | -- | PASS | -8.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elina Svitolina (`KXWTAMATCH-26NOV09ANDSVI-SVI`) | 0.36 / 0.37 (215256) | 36.5% | 43.9% | 39.6% | 43.7% [41.2%-51.0%] | -- | -- | -- | -- | SHADOW_BET | +7.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4895.0, B 4144.0; serve-point win A 58.5%, B 42.7%; Elo A 2080.4, B 2106.5; model uncertainty 0.0494
* Form inputs: days since last match A 29, B 24; matches on record A 265, B 859; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTASETWINNER-26NOV09ANDSVI-2-AND` Will Mirra Andreeva win set 2 in the Mirra Andreeva vs Elina Svitolina match: 0.54/0.74 mid 64.0%, model 54.0% (projection_v2.0 (prediction ledger)) -- gap -9.9 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV09ANDSVI-2-SVI` Will Elina Svitolina win set 2 in the Mirra Andreeva vs Elina Svitolina match: 0.25/0.47 mid 36.0%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV09ANDSVI-23` Over 22.5 games: 0.46/0.48 mid 47.0%, model 56.7% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV09ANDSVI-18` Over 17.5 games: 0.80/0.84 mid 82.0%, model 88.9% (projection_v2.0 (prediction ledger)) -- gap +6.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV09ANDSVI-28` Over 27.5 games: 0.28/0.29 mid 28.5%, model 35.4% (projection_v2.0 (prediction ledger)) -- gap +6.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV09ANDSVI-1-SVI` Will Elina Svitolina win set 1 in the Mirra Andreeva vs Elina Svitolina match: 0.39/0.40 mid 39.5%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV09ANDSVI-1-AND` Will Mirra Andreeva win set 1 in the Mirra Andreeva vs Elina Svitolina match: 0.59/0.61 mid 60.0%, model 54.0% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## David Cristian Carteputreda vs Mathias Roy -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09CARROY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Cristian Carteputreda (`KXITFMATCH-26NOV09CARROY-CAR`) | 0.96 / 0.97 (4375) | 96.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mathias Roy (`KXITFMATCH-26NOV09CARROY-ROY`) | 0.03 / 0.04 (1) | 3.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hugo Dellien vs Tristan Boyer -- ATP Challenger Lima 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-09T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106198:207729:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tristan Boyer (`KXATPCHALLENGERMATCH-26NOV09DELBOY-BOY`) | 0.33 / 0.34 (18563) | 33.5% | 39.8% | 28.5% | 29.9% [27.2%-34.9%] | -- | 32.8% | 32.8% | MODEL_LONE_OUTLIER | PASS | +6.3 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Hugo Dellien (`KXATPCHALLENGERMATCH-26NOV09DELBOY-DEL`) | 0.66 / 0.67 (2809) | 66.5% | 60.2% | 71.5% | 70.1% [65.0%-72.8%] | -- | 67.1% | 67.1% | MODEL_LONE_OUTLIER | WATCH | -6.3 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5597.0, B 4503.0; serve-point win A 61.3%, B 40.7%; Elo A 1791.3, B 1667.9; model uncertainty 0.0386
* Form inputs: days since last match A 14, B 21; matches on record A 924, B 263; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.026, surface_dev_loose +0.005, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Thomas Gerbaud vs Anirudh Rao -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212840:213652:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thomas Gerbaud (`KXITFMATCH-26NOV09GERRAO-GER`) | 0.99 / -- (0) | -- | 53.7% | 26.5% | 47.1% [47.0%-47.1%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Anirudh Rao (`KXITFMATCH-26NOV09GERRAO-RAO`) | -- / 0.01 (165) | -- | 46.3% | 73.5% | 52.9% [52.9%-53.0%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 568.0, B 0.0; serve-point win A 65.7%, B 35.0%; Elo A 1226.2, B 1247.8; model uncertainty 0.0007
* Form inputs: days since last match A 245, B 728; matches on record A 19, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diogo Morais vs Rodrigo Leal -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211587:214259:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigo Leal (`KXITFMATCH-26NOV09MORLEA-LEA`) | 0.39 / 0.40 (361) | 39.5% | 36.4% | 53.6% | 43.8% [42.7%-44.8%] | -- | -- | -- | -- | PASS | -3.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Diogo Morais (`KXITFMATCH-26NOV09MORLEA-MOR`) | 0.58 / 0.59 (96) | 58.5% | 63.6% | 46.4% | 56.2% [55.2%-57.3%] | -- | -- | -- | -- | PASS | +5.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 178.0, B 140.0; serve-point win A 59.8%, B 42.9%; Elo A 1293.4, B 1241.6; model uncertainty 0.0103
* Form inputs: days since last match A 21, B 196; matches on record A 13, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kaue Noatto vs Andrey Barbiero -- M25 Santa Cruz do Sul R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09NOABAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrey Barbiero (`KXITFMATCH-26NOV09NOABAR-BAR`) | 0.08 / 0.10 (28) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kaue Noatto (`KXITFMATCH-26NOV09NOABAR-NOA`) | 0.90 / 0.91 (650) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Barbara Ferrante vs Lais Lobo Assumpcao Euzebio -- W15 São Carlos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09FERLOB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barbara Ferrante (`KXITFWMATCH-26NOV09FERLOB-FER`) | -- / 0.01 (35866) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lais Lobo Assumpcao Euzebio (`KXITFWMATCH-26NOV09FERLOB-LOB`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nicolai Budkov Kjaer vs Sascha Gueymard Wayenburg -- ATP Challenger Orleans 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-09T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149282:209849:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolai Budkov Kjaer (`KXATPCHALLENGERMATCH-26NOV09BUDGUE-BUD`) | 0.51 / 0.52 (283) | 51.5% | 49.4% | 42.2% | 45.1% [44.2%-47.1%] | -- | 52.2% | 52.2% | MARKETS_AGREE | PASS | -2.1 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Sascha Gueymard Wayenburg (`KXATPCHALLENGERMATCH-26NOV09BUDGUE-GUE`) | 0.47 / 0.49 (6245) | 48.0% | 50.6% | 57.8% | 54.9% [52.9%-55.8%] | -- | 48.1% | 48.1% | MARKETS_AGREE | SHADOW_BET | +2.6 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4436.0, B 4524.0; serve-point win A 65.8%, B 34.1%; Elo A 1682.6, B 1651.0; model uncertainty 0.0145
* Form inputs: days since last match A 7, B 7; matches on record A 184, B 342; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.009, surface_dev_tight +0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Tomas Curras Abasolo vs Martim Bernardo -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09CURBER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martim Bernardo (`KXITFMATCH-26NOV09CURBER-BER`) | 0.07 / 0.08 (195) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tomas Curras Abasolo (`KXITFMATCH-26NOV09CURBER-CUR`) | 0.91 / 0.93 (0) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabriela Dabrowski / Luisa Stefani vs Elise Mertens / Shuai Zhang -- WTA Finals (Women) RR

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-10 02:00Z
* Current expected start: 2026-11-09 23:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-09 18:39Z
* Recommended handicap-by time: 2026-11-09 22:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-10T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09DABSTEMERZHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela Dabrowski / Luisa Stefani (`KXWTADOUBLES-26NOV09DABSTEMERZHA-DABSTE`) | 0.66 / 0.67 (123) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elise Mertens / Shuai Zhang (`KXWTADOUBLES-26NOV09DABSTEMERZHA-MERZHA`) | 0.33 / 0.34 (134) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Haig Daouidian vs Miko Lapalme -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09DAOLAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haig Daouidian (`KXITFMATCH-26NOV09DAOLAP-DAO`) | 0.04 / 0.05 (2126) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Miko Lapalme (`KXITFMATCH-26NOV09DAOLAP-LAP`) | 0.95 / 0.96 (2261) | 95.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eric David Verdes vs Kim Johannes Niethammer -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09VERNIE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kim Johannes Niethammer (`KXITFMATCH-26NOV09VERNIE-NIE`) | -- / 0.01 (191136) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eric David Verdes (`KXITFMATCH-26NOV09VERNIE-VER`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jaden Weekes vs Jonathan Bedard -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09WEEBED:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonathan Bedard (`KXITFMATCH-26NOV09WEEBED-BED`) | 0.08 / 0.14 (25) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jaden Weekes (`KXITFMATCH-26NOV09WEEBED-WEE`) | 0.89 / 0.91 (32) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabriele Pennaforti vs Flavio Salemi -- M25 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 23:08Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-09T23:08:12Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09PENSAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriele Pennaforti (`KXITFMATCH-26NOV09PENSAL-PEN`) | 0.95 / 0.96 (8993) | 95.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Flavio Salemi (`KXITFMATCH-26NOV09PENSAL-SAL`) | 0.04 / 0.06 (973) | 5.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrea Fiorentini vs Antonio Caruso -- M25 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 23:19Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-09T23:19:12Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209206:209253:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Antonio Caruso (`KXITFMATCH-26NOV09FIOCAR-CAR`) | 0.38 / 0.39 (403) | 38.5% | -- | 40.1% | 33.1% [30.5%-35.0%] | -- | -- | -- | -- | PASS | -5.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andrea Fiorentini (`KXITFMATCH-26NOV09FIOCAR-FIO`) | 0.61 / 0.62 (12138) | 61.5% | -- | 59.9% | 66.9% [65.0%-69.5%] | -- | -- | -- | -- | PASS | +5.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2736.0, B 204.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0224
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.015, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joaquin Bianchi vs Jesus Martinez Miranda -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:214129:214407:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joaquin Bianchi (`KXITFMATCH-26NOV09BIAMAR-BIA`) | 0.76 / 0.77 (6179) | 76.5% | 40.8% | 39.8% | 42.8% [41.8%-42.8%] | -- | -- | -- | -- | PASS | -35.7 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jesus Martinez Miranda (`KXITFMATCH-26NOV09BIAMAR-MAR`) | 0.23 / 0.24 (7377) | 23.5% | 59.2% | 60.2% | 57.2% [57.2%-58.2%] | -- | -- | -- | -- | PASS | +35.7 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 179.0, B 112.0; serve-point win A 58.7%, B 39.5%; Elo A 1162.1, B 1211.2; model uncertainty 0.0052
* Form inputs: days since last match A 238, B 196; matches on record A 4, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09BIAMAR-MAR  (YES = Jesus Martinez Miranda)
Model: 59%
Kalshi: 24%
Gap: +36 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matthias Uwe Kask vs Eliot Nobel -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210490:214052:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthias Uwe Kask (`KXITFMATCH-26NOV09KASNOB-KAS`) | 0.68 / 0.69 (100) | 68.5% | 47.0% | 46.9% | 42.8% [42.8%-43.3%] | -- | -- | -- | -- | PASS | -21.4 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eliot Nobel (`KXITFMATCH-26NOV09KASNOB-NOB`) | 0.31 / 0.32 (50) | 31.5% | 52.9% | 53.1% | 57.2% [56.7%-57.2%] | -- | -- | -- | -- | PASS | +21.4 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 46.0, B 63.0; serve-point win A 59.5%, B 40.0%; Elo A 1210.9, B 1258.3; model uncertainty 0.0026
* Form inputs: days since last match A 728, B 455; matches on record A 4, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09KASNOB-NOB  (YES = Eliot Nobel)
Model: 53%
Kalshi: 32%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefano Lacroce vs Tiago Silva -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09LACSIL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefano Lacroce (`KXITFMATCH-26NOV09LACSIL-LAC`) | 0.03 / 0.04 (638) | 3.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tiago Silva (`KXITFMATCH-26NOV09LACSIL-SIL`) | 0.96 / 0.98 (1768) | 97.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lance Lage vs Dante Carlos Teramo -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09LAGTER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lance Lage (`KXITFMATCH-26NOV09LAGTER-LAG`) | 0.19 / 0.21 (7494) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dante Carlos Teramo (`KXITFMATCH-26NOV09LAGTER-TER`) | 0.79 / 0.81 (10584) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Steven McCartney vs Jared Horwood -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09MCCHOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jared Horwood (`KXITFMATCH-26NOV09MCCHOR-HOR`) | 0.92 / 0.93 (1560) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Steven McCartney (`KXITFMATCH-26NOV09MCCHOR-MCC`) | 0.07 / 0.08 (3120) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jack McGary vs Luis Patino -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106250:214117:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack McGary (`KXITFMATCH-26NOV09MCGPAT-MCG`) | 0.34 / 0.35 (5916) | 34.5% | 21.5% | 53.6% | 32.1% [28.5%-35.0%] | -- | -- | -- | -- | PASS | -13.0 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Luis Patino (`KXITFMATCH-26NOV09MCGPAT-PAT`) | 0.65 / 0.66 (1570) | 65.5% | 78.5% | 46.4% | 67.8% [65.0%-71.5%] | -- | -- | -- | -- | PASS | +13.0 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 281.0, B 673.0; serve-point win A 57.5%, B 36.4%; Elo A 1181.7, B 1342.9; model uncertainty 0.032
* Form inputs: days since last match A 196, B 1624; matches on record A 5, B 354; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabriel Miller vs Lucas Hammond -- M25 Montreal R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09MILHAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Hammond (`KXITFMATCH-26NOV09MILHAM-HAM`) | 0.94 / 0.95 (7984) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabriel Miller (`KXITFMATCH-26NOV09MILHAM-MIL`) | 0.05 / 0.06 (8673) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hanyu Guo / Kristina Mladenovic vs Su-Wei Hsieh / Jelena Ostapenko -- WTA Finals (Women) RR

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-10 03:30Z
* Current expected start: 2026-11-10 00:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-09 18:39Z
* Recommended handicap-by time: 2026-11-09 23:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-10T03:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09GUOMLAHSIOST:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanyu Guo / Kristina Mladenovic (`KXWTADOUBLES-26NOV09GUOMLAHSIOST-GUOMLA`) | 0.37 / 0.40 (442) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Su-Wei Hsieh / Jelena Ostapenko (`KXWTADOUBLES-26NOV09GUOMLAHSIOST-HSIOST`) | 0.60 / 0.62 (1944) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Leonardo Primucci vs Edoardo Betti -- M25 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09PRIBET:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edoardo Betti (`KXITFMATCH-26NOV09PRIBET-BET`) | 0.29 / 0.32 (9) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leonardo Primucci (`KXITFMATCH-26NOV09PRIBET-PRI`) | 0.65 / 0.72 (64) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alberto Odiseo Alvarado Berrospi vs Axel Cabrera -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09ALVCAB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alberto Odiseo Alvarado Berrospi (`KXITFMATCH-26NOV09ALVCAB-ALV`) | 0.94 / 0.95 (1243) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Axel Cabrera (`KXITFMATCH-26NOV09ALVCAB-CAB`) | 0.05 / 0.06 (121) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ian Lucca Cervantes Tomas vs Miguel Gamborino -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209388:212486:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ian Lucca Cervantes Tomas (`KXITFMATCH-26NOV09CERGAM-CER`) | 0.87 / 0.88 (0) | 87.5% | 53.3% | 39.3% | 39.3% [38.8%-39.8%] | -- | -- | -- | -- | PASS | -34.2 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Miguel Gamborino (`KXITFMATCH-26NOV09CERGAM-GAM`) | 0.11 / 0.12 (268) | 11.5% | 46.7% | 60.7% | 60.7% [60.2%-61.2%] | -- | -- | -- | -- | PASS | +35.2 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 529.0, B 44.0; serve-point win A 60.1%, B 40.6%; Elo A 1159.9, B 1238.1; model uncertainty 0.0052
* Form inputs: days since last match A 413, B 196; matches on record A 24, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09CERGAM-GAM  (YES = Miguel Gamborino)
Model: 47%
Kalshi: 12%
Gap: +35 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tarun Karra vs Marcel Hornung -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206623:213598:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcel Hornung (`KXITFMATCH-26NOV09KARHOR-HOR`) | 0.38 / 0.39 (90) | 38.5% | 66.9% | 75.2% | 67.2% [67.0%-67.3%] | -- | -- | -- | -- | PASS | +28.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Tarun Karra (`KXITFMATCH-26NOV09KARHOR-KAR`) | 0.60 / 0.62 (1) | 61.0% | 33.1% | 24.8% | 32.8% [32.7%-33.0%] | -- | -- | -- | -- | PASS | -27.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 201.0, B 0.0; serve-point win A 56.8%, B 39.9%; Elo A 1132.3, B 1259.3; model uncertainty 0.0011
* Form inputs: days since last match A 238, B 1120; matches on record A 8, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09KARHOR-HOR  (YES = Marcel Hornung)
Model: 67%
Kalshi: 38%
Gap: +28 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Miguel Tobon vs Henrique Rocha -- ATP Challenger Lima 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-10T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:101495:210012:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Henrique Rocha (`KXATPCHALLENGERMATCH-26NOV09TOBROC-ROC`) | 0.77 / 0.79 (5689) | 78.0% | 74.0% | 63.6% | 69.7% [65.5%-82.5%] | -- | -- | -- | -- | PASS | -4.0 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Miguel Tobon (`KXATPCHALLENGERMATCH-26NOV09TOBROC-TOB`) | 0.21 / 0.22 (41) | 21.5% | 26.0% | 36.4% | 30.3% [17.5%-34.5%] | -- | -- | -- | -- | WATCH | +4.5 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3281.0, B 4833.0; serve-point win A 58.1%, B 36.9%; Elo A 1454.2, B 1702.9; model uncertainty 0.0851
* Form inputs: days since last match A 106, B 7; matches on record A 423, B 323; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.031, surface_pool_high +0.042, surface_dev_loose +0.009, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Arklon Huertas Del Pino Cordova vs Lautaro Midon -- ATP Challenger Lima 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 02:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-10T02:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207736:210510:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arklon Huertas Del Pino Cordova (`KXATPCHALLENGERMATCH-26NOV09HUEMID-HUE`) | 0.13 / 0.16 (9) | 14.5% | 11.6% | 14.0% | 13.1% [12.3%-14.6%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Lautaro Midon (`KXATPCHALLENGERMATCH-26NOV09HUEMID-MID`) | 0.84 / 0.87 (50) | 85.5% | 88.4% | 86.0% | 86.9% [85.4%-87.7%] | -- | -- | -- | -- | PASS | +2.9 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1715.0, B 4759.0; serve-point win A 54.1%, B 36.6%; Elo A 1337.4, B 1682.4; model uncertainty 0.0115
* Form inputs: days since last match A 28, B 7; matches on record A 297, B 277; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.009, surface_dev_loose -0.002, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Enzo Aguiard vs Akira Santillan -- ATP Challenger Brisbane 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:117361:212174:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enzo Aguiard (`KXATPCHALLENGERMATCH-26NOV09AGUSAN-AGU`) | 0.41 / 0.42 (877) | 41.5% | 47.8% | 45.5% | 45.6% [40.2%-49.5%] | -- | 41.7% | 41.7% | MODEL_LONE_OUTLIER | WATCH | +6.3 pp | NORMAL | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Akira Santillan (`KXATPCHALLENGERMATCH-26NOV09AGUSAN-SAN`) | 0.58 / 0.59 (161) | 58.5% | 52.2% | 54.5% | 54.4% [50.5%-59.9%] | -- | 58.7% | 58.7% | MODEL_LONE_OUTLIER | PASS | -6.3 pp | NORMAL | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1732.0, B 3639.0; serve-point win A 64.2%, B 35.4%; Elo A 1500.5, B 1531.4; model uncertainty 0.0468
* Form inputs: days since last match A 56, B 14; matches on record A 58, B 597; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.034, surface_pool_high +0.040, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Jake Delaney vs Juncheng Shang -- ATP Challenger Brisbane 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:117359:209992:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Delaney (`KXATPCHALLENGERMATCH-26NOV09DELSHA-DEL`) | 0.17 / 0.18 (3223) | 17.5% | 13.2% | 32.4% | 22.9% [17.3%-26.4%] | -- | 21.2% | 21.2% | KALSHI_LONE_OUTLIER | PASS | -4.3 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Juncheng Shang (`KXATPCHALLENGERMATCH-26NOV09DELSHA-SHA`) | 0.82 / 0.83 (45) | 82.5% | 86.8% | 67.6% | 77.1% [73.6%-82.7%] | -- | 84.9% | -- | INSUFFICIENT_INPUTS | PASS | +4.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3508.0, B 2480.0; serve-point win A 63.0%, B 27.6%; Elo A 1437.8, B 1805.1; model uncertainty 0.0451
* Form inputs: days since last match A 7, B 14; matches on record A 345, B 239; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.015, surface_dev_loose -0.006, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Sebastian Gorzny vs Charles Broom -- ATP Challenger Brisbane 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200277:210478:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charles Broom (`KXATPCHALLENGERMATCH-26NOV09GORBRO-BRO`) | 0.50 / 0.60 (3) | 55.0% | 70.3% | 79.0% | 73.6% [71.9%-75.2%] | -- | -- | -- | -- | PASS | +15.3 pp | HIGH_REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sebastian Gorzny (`KXATPCHALLENGERMATCH-26NOV09GORBRO-GOR`) | 0.47 / 0.54 (3) | 50.5% | 29.7% | 21.0% | 26.5% [24.8%-28.1%] | -- | -- | -- | -- | PASS | -20.8 pp | HIGH_REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1167.0, B 4411.0; serve-point win A 60.9%, B 34.9%; Elo A 1502.6, B 1638.2; model uncertainty 0.0165
* Form inputs: days since last match A 14, B 7; matches on record A 41, B 397; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV09GORBRO-BRO  (YES = Charles Broom)
Model: 70%
Kalshi: 55%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## August Holmgren vs Philip Sekulic -- ATP Challenger Brisbane 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200416:210340:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| August Holmgren (`KXATPCHALLENGERMATCH-26NOV09HOLSEK-HOL`) | 0.63 / 0.64 (13) | 63.5% | 62.0% | 53.4% | 54.4% [51.9%-59.7%] | -- | 63.3% | -- | INSUFFICIENT_INPUTS | PASS | -1.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Philip Sekulic (`KXATPCHALLENGERMATCH-26NOV09HOLSEK-SEK`) | 0.35 / 0.37 (631) | 36.0% | 38.0% | 46.6% | 45.6% [40.3%-48.0%] | -- | 38.7% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +2.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4476.0, B 4045.0; serve-point win A 67.2%, B 35.3%; Elo A 1609.9, B 1560.3; model uncertainty 0.0387
* Form inputs: days since last match A 7, B 48; matches on record A 320, B 272; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.024, surface_pool_high -0.024, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Naoya Honda vs Stefanos Sakellaridis -- ATP Challenger Matsuyama 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208852:211897:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naoya Honda (`KXATPCHALLENGERMATCH-26NOV09HONSAK-HON`) | 0.20 / 0.22 (197) | 21.0% | 20.4% | 20.3% | 18.9% [16.3%-21.0%] | -- | -- | -- | -- | PASS | -0.6 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefanos Sakellaridis (`KXATPCHALLENGERMATCH-26NOV09HONSAK-SAK`) | 0.79 / 0.80 (830) | 79.5% | 79.6% | 79.7% | 81.1% [79.0%-83.7%] | -- | -- | -- | -- | PASS | +0.1 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1597.0, B 4881.0; serve-point win A 61.0%, B 32.3%; Elo A 1365.9, B 1635.4; model uncertainty 0.0237
* Form inputs: days since last match A 14, B 7; matches on record A 72, B 386; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.021, surface_dev_loose -0.003, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE

## Casey Hoole vs Sam Ryan Ziegann -- ATP Challenger Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208160:211315:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Casey Hoole (`KXATPCHALLENGERMATCH-26NOV09HOORYA-HOO`) | 0.78 / 0.80 (1468) | 79.0% | 77.7% | 66.7% | 74.0% [73.0%-76.0%] | -- | 78.8% | 78.8% | MODEL_LONE_OUTLIER | PASS | -1.3 pp | NORMAL | STALE | F / POOR | ALL_AGREE | VERIFIED |
| Sam Ryan Ziegann (`KXATPCHALLENGERMATCH-26NOV09HOORYA-RYA`) | 0.20 / 0.22 (1187) | 21.0% | 22.3% | 33.3% | 26.1% [24.0%-27.0%] | -- | 21.4% | 21.4% | MODEL_LONE_OUTLIER | PASS | +1.3 pp | NORMAL | STALE | F / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 163.0, B 1167.0; serve-point win A 68.0%, B 38.2%; Elo A 1380.2, B 1190.8; model uncertainty 0.0146
* Form inputs: days since last match A 679, B 63; matches on record A 17, B 87; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.008, surface_dev_loose -0.001, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Omar Jasika vs Dhakshineswar Suresh -- ATP Challenger Brisbane 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:117357:202290:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Omar Jasika (`KXATPCHALLENGERMATCH-26NOV09JASSUR-JAS`) | 0.49 / 0.51 (2481) | 50.0% | 32.1% | 36.1% | 33.9% [32.6%-35.1%] | -- | 50.1% | 50.1% | MODEL_LONE_OUTLIER | PASS | -17.9 pp | HIGH_REVIEW | STALE | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Dhakshineswar Suresh (`KXATPCHALLENGERMATCH-26NOV09JASSUR-SUR`) | 0.49 / 0.50 (114) | 49.5% | 67.9% | 63.9% | 66.1% [64.8%-67.4%] | -- | 50.3% | 50.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +18.4 pp | HIGH_REVIEW | STALE | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4159.0, B 1964.0; serve-point win A 64.0%, B 32.2%; Elo A 1530.4, B 1674.1; model uncertainty 0.0129
* Form inputs: days since last match A 7, B 75; matches on record A 523, B 91; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV09JASSUR-SUR  (YES = Dhakshineswar Suresh)
Model: 68%
Kalshi: 50%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.004, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## James McCabe vs Jan Kumstat -- ATP Challenger Brisbane 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210317:211618:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jan Kumstat (`KXATPCHALLENGERMATCH-26NOV09MCCKUM-KUM`) | 0.65 / 0.67 (6477) | 66.0% | 68.1% | 66.1% | 63.0% [59.4%-67.4%] | -- | -- | -- | -- | PASS | +2.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| James McCabe (`KXATPCHALLENGERMATCH-26NOV09MCCKUM-MCC`) | 0.33 / 0.34 (1) | 33.5% | 31.9% | 33.9% | 37.0% [32.6%-40.6%] | -- | -- | -- | -- | WATCH | -1.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4552.0, B 3055.0; serve-point win A 66.7%, B 29.3%; Elo A 1579.4, B 1631.9; model uncertainty 0.0401
* Form inputs: days since last match A 7, B 7; matches on record A 336, B 89; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.044, surface_pool_high +0.036, surface_dev_loose +0.010, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Shunsuke Nakagawa vs David Jorda Sanchis -- ATP Challenger Matsuyama 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122554:209905:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Jorda Sanchis (`KXATPCHALLENGERMATCH-26NOV09NAKJOR-JOR`) | 0.78 / 0.79 (5095) | 78.5% | 74.2% | 71.9% | 72.7% [66.6%-78.6%] | -- | 78.8% | 78.8% | MODEL_LONE_OUTLIER | PASS | -4.3 pp | NORMAL | STALE | B / LIMITED | ALL_AGREE | VERIFIED |
| Shunsuke Nakagawa (`KXATPCHALLENGERMATCH-26NOV09NAKJOR-NAK`) | 0.20 / 0.21 (363) | 20.5% | 25.8% | 28.1% | 27.3% [21.4%-33.4%] | -- | 21.6% | 21.6% | MODEL_LONE_OUTLIER | WATCH | +5.3 pp | NORMAL | STALE | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1170.0, B 5329.0; serve-point win A 60.2%, B 34.6%; Elo A 1333.8, B 1504.2; model uncertainty 0.0601
* Form inputs: days since last match A 105, B 42; matches on record A 56, B 469; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.048, surface_pool_high +0.061, surface_dev_loose +0.004, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Carl Emil Overbeck vs Florian Broska -- ATP Challenger Brisbane 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202239:209274:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florian Broska (`KXATPCHALLENGERMATCH-26NOV09OVEBRO-BRO`) | 0.40 / 0.42 (3255) | 41.0% | 52.3% | 41.2% | 47.5% [44.6%-50.0%] | -- | 40.8% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +11.3 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carl Emil Overbeck (`KXATPCHALLENGERMATCH-26NOV09OVEBRO-OVE`) | 0.58 / 0.60 (3622) | 59.0% | 47.7% | 58.8% | 52.5% [50.0%-55.4%] | -- | 59.3% | -- | INSUFFICIENT_INPUTS | PASS | -11.3 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2038.0, B 3363.0; serve-point win A 64.8%, B 34.8%; Elo A 1505.2, B 1544.8; model uncertainty 0.027
* Form inputs: days since last match A 7, B 28; matches on record A 85, B 218; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Mili Poljicak vs Chun Hsin Tseng -- ATP Challenger Matsuyama 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202358:209890:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mili Poljicak (`KXATPCHALLENGERMATCH-26NOV09POLTSE-POL`) | 0.40 / 0.51 (1) | 45.5% | 37.5% | 41.1% | 40.6% [38.7%-41.6%] | -- | -- | -- | -- | PASS | -8.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chun Hsin Tseng (`KXATPCHALLENGERMATCH-26NOV09POLTSE-TSE`) | 0.51 / 0.60 (7) | 55.5% | 62.5% | 58.9% | 59.4% [58.4%-61.3%] | -- | -- | -- | -- | PASS | +7.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3404.0, B 4916.0; serve-point win A 62.5%, B 35.0%; Elo A 1538.8, B 1606.3; model uncertainty 0.0146
* Form inputs: days since last match A 7, B 7; matches on record A 282, B 519; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.009, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tristan Schoolkate vs Cruz Hewitt -- ATP Challenger Brisbane 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209262:213178:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cruz Hewitt (`KXATPCHALLENGERMATCH-26NOV09SCHHEW-HEW`) | 0.24 / 0.25 (614) | 24.5% | 29.4% | 27.7% | 27.3% [26.4%-28.1%] | -- | 23.0% | -- | INSUFFICIENT_INPUTS | PASS | +4.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tristan Schoolkate (`KXATPCHALLENGERMATCH-26NOV09SCHHEW-SCH`) | 0.75 / 0.76 (44) | 75.5% | 70.6% | 72.3% | 72.7% [71.9%-73.6%] | -- | 72.1% | -- | INSUFFICIENT_INPUTS | PASS | -4.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6081.0, B 2605.0; serve-point win A 69.2%, B 35.3%; Elo A 1695.1, B 1521.7; model uncertainty 0.0086
* Form inputs: days since last match A 14, B 21; matches on record A 423, B 79; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.008, surface_dev_loose -0.000, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Dane Sweeny vs Anton Shepp -- ATP Challenger Brisbane 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208013:209394:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anton Shepp (`KXATPCHALLENGERMATCH-26NOV09SWESHE-SHE`) | 0.30 / 0.31 (760) | 30.5% | 30.0% | 48.5% | 37.2% [31.1%-42.0%] | -- | 30.5% | -- | INSUFFICIENT_INPUTS | WATCH | -0.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dane Sweeny (`KXATPCHALLENGERMATCH-26NOV09SWESHE-SWE`) | 0.69 / 0.70 (239) | 69.5% | 70.0% | 51.5% | 62.8% [58.0%-68.8%] | -- | 69.5% | 69.5% | MODEL_LONE_OUTLIER | PASS | +0.5 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5456.0, B 2073.0; serve-point win A 65.4%, B 38.8%; Elo A 1650.8, B 1440.8; model uncertainty 0.0545
* Form inputs: days since last match A 28, B 50; matches on record A 432, B 69; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Yosuke Watanuki vs Taro Daniel -- ATP Challenger Matsuyama 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106121:133297:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taro Daniel (`KXATPCHALLENGERMATCH-26NOV09WATDAN-DAN`) | 0.41 / 0.42 (787) | 41.5% | 32.6% | 46.0% | 45.1% [41.1%-51.0%] | -- | 42.2% | 42.2% | MODEL_LONE_OUTLIER | WATCH | -8.8 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Yosuke Watanuki (`KXATPCHALLENGERMATCH-26NOV09WATDAN-WAT`) | 0.58 / 0.59 (835) | 58.5% | 67.3% | 54.0% | 54.9% [49.0%-58.9%] | -- | 58.0% | 58.0% | MODEL_LONE_OUTLIER | PASS | +8.8 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3355.0, B 4270.0; serve-point win A 66.2%, B 37.4%; Elo A 1717.1, B 1663.2; model uncertainty 0.0492
* Form inputs: days since last match A 7, B 14; matches on record A 454, B 1068; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.040, surface_pool_high +0.039, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Judith Hernandez Miranda vs Kennedy Gibbs -- W50 Chihuahua R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222665:249680:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kennedy Gibbs (`KXITFWMATCH-26NOV09HERGIB-GIB`) | 0.44 / 0.46 (148) | 45.0% | 64.7% | 86.1% | 61.6% [61.6%-62.6%] | -- | -- | -- | -- | PASS | +19.7 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Judith Hernandez Miranda (`KXITFWMATCH-26NOV09HERGIB-HER`) | 0.53 / 0.56 (180) | 54.5% | 35.3% | 13.9% | 38.4% [37.4%-38.4%] | -- | -- | -- | -- | PASS | -19.2 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 185.0, B 0.0; serve-point win A 51.3%, B 45.9%; Elo A 1309.8, B 1393.3; model uncertainty 0.0053
* Form inputs: days since last match A 196, B 840; matches on record A 110, B 10; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV09HERGIB-GIB  (YES = Kennedy Gibbs)
Model: 65%
Kalshi: 45%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jessica Marmorstein vs Sydney-Nicole Clarke -- W50 Chihuahua R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221478:264013:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sydney-Nicole Clarke (`KXITFWMATCH-26NOV09MARCLA-CLA`) | 0.63 / 0.65 (224) | 64.0% | 56.7% | 31.5% | 56.4% [53.2%-57.4%] | -- | -- | -- | -- | PASS | -7.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jessica Marmorstein (`KXITFWMATCH-26NOV09MARCLA-MAR`) | 0.34 / 0.36 (5) | 35.0% | 43.3% | 68.5% | 43.6% [42.6%-46.8%] | -- | -- | -- | -- | PASS | +8.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 71.0, B 65.0; serve-point win A 52.6%, B 46.2%; Elo A 1177.4, B 1225.7; model uncertainty 0.0211
* Form inputs: days since last match A 490, B 343; matches on record A 52, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Caterina Odorizzi vs Sarai Gabrielle Clarke -- W50 Chihuahua R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09ODOCLA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sarai Gabrielle Clarke (`KXITFWMATCH-26NOV09ODOCLA-CLA`) | 0.05 / 0.06 (0) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Caterina Odorizzi (`KXITFWMATCH-26NOV09ODOCLA-ODO`) | 0.94 / 0.95 (113) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Prisha Vyas vs Galia Garcia Anzures -- W50 Chihuahua R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09VYAGAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Galia Garcia Anzures (`KXITFWMATCH-26NOV09VYAGAR-GAR`) | 0.65 / 0.66 (221) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Prisha Vyas (`KXITFWMATCH-26NOV09VYAGAR-VYA`) | 0.34 / 0.35 (126) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Patricio Betancourt vs Nicolas Dagda Mireles -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T03:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09BETDAG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Patricio Betancourt (`KXITFMATCH-26NOV09BETDAG-BET`) | 0.65 / 0.66 (19) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nicolas Dagda Mireles (`KXITFMATCH-26NOV09BETDAG-DAG`) | 0.31 / 0.32 (126) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Roberto Herman vs Anders Matta -- M15 Zamora R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T03:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09HERMAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Roberto Herman (`KXITFMATCH-26NOV09HERMAT-HER`) | 0.20 / 0.23 (20) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anders Matta (`KXITFMATCH-26NOV09HERMAT-MAT`) | 0.78 / 0.80 (150) | 79.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Naoya Honda vs Chun Hsin Tseng -- ATP Challenger Matsuyama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202358:211897:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naoya Honda (`KXATPCHALLENGERMATCH-26NOV09HONTSE-HON`) | 0.25 / 0.27 (516) | 26.0% | 20.7% | 23.6% | 21.7% [16.6%-26.0%] | -- | 26.7% | 26.7% | MODEL_LONE_OUTLIER | PASS | -5.3 pp | NORMAL | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Chun Hsin Tseng (`KXATPCHALLENGERMATCH-26NOV09HONTSE-TSE`) | 0.73 / 0.74 (24) | 73.5% | 79.3% | 76.4% | 78.3% [74.0%-83.4%] | -- | 73.6% | 73.6% | MODEL_LONE_OUTLIER | WATCH | +5.8 pp | NORMAL | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1597.0, B 4916.0; serve-point win A 59.7%, B 33.9%; Elo A 1365.9, B 1606.3; model uncertainty 0.047
* Form inputs: days since last match A 14, B 7; matches on record A 72, B 519; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.038, surface_pool_high +0.043, surface_dev_loose +0.001, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Mili Poljicak vs Kaichi Uchida -- ATP Challenger Matsuyama 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111187:209890:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mili Poljicak (`KXATPCHALLENGERMATCH-26NOV09POLUCH-POL`) | 0.64 / 0.65 (617) | 64.5% | 63.2% | 55.9% | 56.3% [55.3%-57.3%] | -- | 62.4% | -- | INSUFFICIENT_INPUTS | PASS | -1.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kaichi Uchida (`KXATPCHALLENGERMATCH-26NOV09POLUCH-UCH`) | 0.35 / 0.36 (771) | 35.5% | 36.8% | 44.1% | 43.7% [42.7%-44.7%] | -- | 33.7% | -- | INSUFFICIENT_INPUTS | PASS | +1.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3404.0, B 4273.0; serve-point win A 67.1%, B 35.7%; Elo A 1538.8, B 1489.3; model uncertainty 0.0099
* Form inputs: days since last match A 7, B 14; matches on record A 282, B 836; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Hikaru Shiraishi vs Ognjen Milic -- ATP Challenger Matsuyama 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202113:212207:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ognjen Milic (`KXATPCHALLENGERMATCH-26NOV09SHIMIL-MIL`) | 0.54 / 0.56 (1321) | 55.0% | 62.8% | 60.0% | 60.5% [60.0%-61.5%] | -- | 56.2% | 56.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.8 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Hikaru Shiraishi (`KXATPCHALLENGERMATCH-26NOV09SHIMIL-SHI`) | 0.42 / 0.43 (3) | 42.5% | 37.2% | 40.0% | 39.5% [38.5%-40.0%] | -- | 42.8% | -- | INSUFFICIENT_INPUTS | PASS | -5.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2976.0, B 3142.0; serve-point win A 60.9%, B 36.5%; Elo A 1438.1, B 1527.6; model uncertainty 0.0072
* Form inputs: days since last match A 56, B 14; matches on record A 210, B 103; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.009, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Allegre / Avataneo vs Castillo Meza / Reyes Romero -- W50 Chihuahua R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09ALLAVACASREY:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Allegre / Avataneo (`KXITFWDOUBLES-26NOV09ALLAVACASREY-ALLAVA`) | 0.49 / 0.82 (4) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Castillo Meza / Reyes Romero (`KXITFWDOUBLES-26NOV09ALLAVACASREY-CASREY`) | 0.28 / 0.61 (56) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fernanda Guadalupe Regalado Macias vs Sara Lillian Chavez -- W50 Chihuahua R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09REGCHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Lillian Chavez (`KXITFWMATCH-26NOV09REGCHA-CHA`) | 0.53 / 0.55 (5) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fernanda Guadalupe Regalado Macias (`KXITFWMATCH-26NOV09REGCHA-REG`) | 0.43 / 0.48 (61) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Moerani Bouzige vs Christopher O'Connell -- ATP Challenger Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 04:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T04:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207728:tml:O483:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Moerani Bouzige (`KXATPCHALLENGERMATCH-26NOV09BOUOCO-BOU`) | 0.10 / 0.12 (629) | 11.0% | 16.8% | 38.5% | 26.7% [18.5%-31.3%] | -- | 11.9% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +5.8 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Christopher O'Connell (`KXATPCHALLENGERMATCH-26NOV09BOUOCO-OCO`) | 0.89 / 0.90 (582) | 89.5% | 83.2% | 61.5% | 73.3% [68.7%-81.5%] | -- | 88.2% | -- | INSUFFICIENT_INPUTS | PASS | -6.3 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3261.0, B 2972.0; serve-point win A 62.2%, B 29.9%; Elo A 1424.3, B 1800.7; model uncertainty 0.0641
* Form inputs: days since last match A 56, B 73; matches on record A 315, B 319; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.005, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Matthew Dellavedova vs Thomas Fancutt -- ATP Challenger Brisbane 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 04:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T04:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126573:202354:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Dellavedova (`KXATPCHALLENGERMATCH-26NOV09DELFAN-DEL`) | 0.81 / 0.82 (55) | 81.5% | 62.9% | 58.3% | 58.8% [57.4%-59.7%] | -- | 81.3% | 81.3% | MODEL_LONE_OUTLIER | PASS | -18.6 pp | HIGH_REVIEW | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Thomas Fancutt (`KXATPCHALLENGERMATCH-26NOV09DELFAN-FAN`) | 0.18 / 0.19 (752) | 18.5% | 37.1% | 41.7% | 41.2% [40.3%-42.6%] | -- | 19.0% | 19.0% | MODEL_LONE_OUTLIER | PASS | +18.6 pp | HIGH_REVIEW | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3884.0, B 1210.0; serve-point win A 66.9%, B 35.8%; Elo A 1455.0, B 1389.7; model uncertainty 0.0116
* Form inputs: days since last match A 48, B 56; matches on record A 451, B 431; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV09DELFAN-FAN  (YES = Thomas Fancutt)
Model: 37%
Kalshi: 18%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: B (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.009, surface_dev_loose -0.001, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Shintaro Imai vs Fajing Sun -- ATP Challenger Matsuyama 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 05:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T05:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111806:122495:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shintaro Imai (`KXATPCHALLENGERMATCH-26NOV09IMASUN-IMA`) | 0.31 / 0.34 (3294) | 32.5% | 35.1% | 50.0% | 46.0% [45.0%-48.0%] | -- | 32.1% | -- | INSUFFICIENT_INPUTS | PASS | +2.6 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Fajing Sun (`KXATPCHALLENGERMATCH-26NOV09IMASUN-SUN`) | 0.67 / 0.69 (820) | 68.0% | 64.9% | 50.0% | 54.0% [52.0%-55.0%] | -- | 67.9% | -- | INSUFFICIENT_INPUTS | PASS | -3.1 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1292.0, B 4332.0; serve-point win A 62.2%, B 34.7%; Elo A 1507.2, B 1555.7; model uncertainty 0.015
* Form inputs: days since last match A 14, B 14; matches on record A 461, B 528; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Niels McDonald vs Koki Matsuda -- ATP Challenger Matsuyama 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 05:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T05:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211628:213360:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Koki Matsuda (`KXATPCHALLENGERMATCH-26NOV09MCDMAT-MAT`) | 0.46 / 0.47 (5) | 46.5% | 48.5% | 60.9% | 59.9% [55.5%-62.3%] | -- | 47.7% | 47.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +2.0 pp | NORMAL | STALE | B / LIMITED | ALL_AGREE | VERIFIED |
| Niels McDonald (`KXATPCHALLENGERMATCH-26NOV09MCDMAT-MCD`) | 0.53 / 0.54 (8162) | 53.5% | 51.5% | 39.1% | 40.1% [37.7%-44.5%] | -- | 52.8% | 52.8% | MODEL_LONE_OUTLIER | PASS | -2.0 pp | NORMAL | STALE | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2065.0, B 2859.0; serve-point win A 63.7%, B 36.6%; Elo A 1396.0, B 1460.2; model uncertainty 0.0339
* Form inputs: days since last match A 70, B 14; matches on record A 41, B 147; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.024, surface_dev_loose -0.009, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Rei Sakamoto vs Renta Tokuda -- ATP Challenger Matsuyama 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 05:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T05:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126337:210536:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rei Sakamoto (`KXATPCHALLENGERMATCH-26NOV09SAKTOK-SAK`) | 0.87 / 0.88 (12320) | 87.5% | 79.4% | 56.3% | 67.1% [62.5%-75.9%] | -- | 86.6% | 86.6% | MODEL_LONE_OUTLIER | PASS | -8.1 pp | NORMAL | STALE | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Renta Tokuda (`KXATPCHALLENGERMATCH-26NOV09SAKTOK-TOK`) | 0.13 / 0.14 (666) | 13.5% | 20.6% | 43.7% | 32.9% [24.1%-37.5%] | -- | 12.8% | -- | INSUFFICIENT_INPUTS | PASS | +7.1 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4519.0, B 2892.0; serve-point win A 69.0%, B 37.7%; Elo A 1784.3, B 1509.6; model uncertainty 0.0671
* Form inputs: days since last match A 14, B 189; matches on record A 190, B 426; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.004, surface_dev_loose +0.004, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Sebastian Gorzny vs Isaac Becroft -- ATP Challenger Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 05:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T05:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208653:210478:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isaac Becroft (`KXATPCHALLENGERMATCH-26NOV09GORBEC-BEC`) | 0.28 / 0.29 (1254) | 28.5% | 22.2% | 29.2% | 26.6% [25.4%-27.9%] | -- | 28.6% | -- | INSUFFICIENT_INPUTS | PASS | -6.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sebastian Gorzny (`KXATPCHALLENGERMATCH-26NOV09GORBEC-GOR`) | 0.71 / 0.73 (612) | 72.0% | 77.8% | 70.8% | 73.4% [72.1%-74.6%] | -- | 71.2% | -- | INSUFFICIENT_INPUTS | PASS | +5.8 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1167.0, B 1698.0; serve-point win A 64.7%, B 41.3%; Elo A 1502.6, B 1311.2; model uncertainty 0.0129
* Form inputs: days since last match A 14, B 196; matches on record A 41, B 106; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.008, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE

## Kasidit Samrej vs Yuta Shimizu -- ATP Challenger Matsuyama 1/16 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202122:208937:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kasidit Samrej (`KXATPCHALLENGERMATCH-26NOV09SAMSHI-SAM`) | 0.33 / 0.35 (1566) | 34.0% | 45.2% | 49.5% | 48.5% [47.0%-49.5%] | -- | 33.2% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +11.2 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuta Shimizu (`KXATPCHALLENGERMATCH-26NOV09SAMSHI-SHI`) | 0.65 / 0.67 (1342) | 66.0% | 54.8% | 50.5% | 51.5% [50.5%-53.0%] | -- | 66.8% | -- | INSUFFICIENT_INPUTS | PASS | -11.2 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4164.0, B 4313.0; serve-point win A 63.5%, B 35.5%; Elo A 1584.5, B 1601.4; model uncertainty 0.0124
* Form inputs: days since last match A 7, B 7; matches on record A 298, B 474; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Sakura Hosogi vs Hayu Kinoshita -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220718:260171:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sakura Hosogi (`KXITFWMATCH-26NOV09HOSKIN-HOS`) | 0.41 / 0.42 (5) | 41.5% | 33.0% | 23.2% | 31.1% [27.9%-37.5%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.5 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hayu Kinoshita (`KXITFWMATCH-26NOV09HOSKIN-KIN`) | 0.56 / 0.58 (122) | 57.0% | 67.0% | 76.8% | 68.9% [62.5%-72.1%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +10.0 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2576.0, B 3494.0; serve-point win A 53.6%, B 43.1%; Elo A 1583.4, B 1614.1; model uncertainty 0.0477
* Form inputs: days since last match A 196, B 9; matches on record A 392, B 177; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.028, surface_pool_high +0.024, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## BoYoung Jeong vs Hiromi Abe -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221109:221362:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hiromi Abe (`KXITFWMATCH-26NOV09JEOABE-ABE`) | 0.74 / 0.75 (100) | 74.5% | 58.3% | 40.5% | 46.8% [42.5%-60.1%] | 76.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.2 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| BoYoung Jeong (`KXITFWMATCH-26NOV09JEOABE-JEO`) | 0.23 / 0.24 (130) | 23.5% | 41.7% | 59.5% | 53.2% [40.0%-57.5%] | 24.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +18.2 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2517.0, B 2555.0; serve-point win A 52.1%, B 46.3%; Elo A 1565.2, B 1619.2; model uncertainty 0.0875
* Form inputs: days since last match A 51, B 238; matches on record A 221, B 200; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV09JEOABE-JEO  (YES = BoYoung Jeong)
Model: 42%
Kalshi: 24%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.032, surface_pool_high +0.027, surface_dev_loose +0.011, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carol Young Suh Lee vs Aoi Ito -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221803:256684:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aoi Ito (`KXITFWMATCH-26NOV09LEEITO-ITO`) | 0.38 / 0.39 (115) | 38.5% | 37.6% | 18.8% | 28.0% [23.7%-38.5%] | 43.9% | -- | 43.9% | ALL_THREE_DISAGREE | PASS | -0.9 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |
| Carol Young Suh Lee (`KXITFWMATCH-26NOV09LEEITO-LEE`) | 0.60 / 0.62 (46) | 61.0% | 62.4% | 81.2% | 72.0% [61.5%-76.3%] | 56.1% | -- | 56.1% | MODEL_LONE_OUTLIER | PASS | +1.4 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 4047.0, B 2722.0; serve-point win A 57.4%, B 45.0%; Elo A 1774.5, B 1759.4; model uncertainty 0.0738
* Form inputs: days since last match A 7, B 16; matches on record A 160, B 304; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose +0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Takuya Kumasaka vs Yi Zhou -- ATP Challenger Matsuyama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 06:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T06:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207998:212044:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Takuya Kumasaka (`KXATPCHALLENGERMATCH-26NOV09KUMZHO-KUM`) | 0.22 / 0.23 (975) | 22.5% | 20.6% | 29.8% | 27.2% [25.5%-28.0%] | -- | 24.1% | -- | INSUFFICIENT_INPUTS | PASS | -1.9 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yi Zhou (`KXATPCHALLENGERMATCH-26NOV09KUMZHO-ZHO`) | 0.77 / 0.78 (34) | 77.5% | 79.4% | 70.2% | 72.8% [72.0%-74.5%] | -- | 75.7% | -- | INSUFFICIENT_INPUTS | PASS | +1.9 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3065.0, B 3814.0; serve-point win A 59.3%, B 34.2%; Elo A 1411.9, B 1635.1; model uncertainty 0.0125
* Form inputs: days since last match A 91, B 14; matches on record A 226, B 182; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.012, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Ryuki Matsuda vs Max Schoenhaus -- ATP Challenger Matsuyama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 06:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T06:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207987:212268:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryuki Matsuda (`KXATPCHALLENGERMATCH-26NOV09MATSCH-MAT`) | 0.17 / 0.18 (1229) | 17.5% | 13.4% | 15.1% | 16.6% [15.4%-17.8%] | -- | 17.4% | 17.4% | MARKETS_AGREE | PASS | -4.2 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Max Schoenhaus (`KXATPCHALLENGERMATCH-26NOV09MATSCH-SCH`) | 0.84 / 0.85 (10356) | 84.5% | 86.7% | 84.9% | 83.4% [82.2%-84.6%] | -- | 82.7% | 82.7% | MODEL_LONE_OUTLIER | PASS | +2.1 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2640.0, B 3062.0; serve-point win A 59.7%, B 31.4%; Elo A 1299.6, B 1553.2; model uncertainty 0.0124
* Form inputs: days since last match A 56, B 20; matches on record A 263, B 98; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.012, surface_pool_high +0.013, surface_dev_loose -0.011, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Christian Langmo vs Ymerali Ibraimi -- ATP Challenger Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 06:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T06:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132052:214192:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ymerali Ibraimi (`KXATPCHALLENGERMATCH-26NOV09LANIBR-IBR`) | 0.14 / 0.15 (1328) | 14.5% | 21.9% | 24.2% | 26.2% [23.5%-27.9%] | -- | 14.4% | -- | INSUFFICIENT_INPUTS | PASS | +7.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Christian Langmo (`KXATPCHALLENGERMATCH-26NOV09LANIBR-LAN`) | 0.85 / 0.87 (38) | 86.0% | 78.0% | 75.8% | 73.8% [72.1%-76.5%] | -- | 85.6% | -- | INSUFFICIENT_INPUTS | PASS | -8.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3910.0, B 660.0; serve-point win A 67.1%, B 39.1%; Elo A 1486.3, B 1311.9; model uncertainty 0.0221
* Form inputs: days since last match A 14, B 231; matches on record A 445, B 11; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.004, surface_dev_loose +0.008, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE

## Jayson Blando vs Ryo Minakata -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09BLAMIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jayson Blando (`KXITFMATCH-26NOV09BLAMIN-BLA`) | 0.32 / 0.51 (4) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ryo Minakata (`KXITFMATCH-26NOV09BLAMIN-MIN`) | 0.63 / 0.68 (5) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kazuma Kawachi vs Darcy Nicholls -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09KAWNIC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kazuma Kawachi (`KXITFMATCH-26NOV09KAWNIC-KAW`) | 0.47 / 0.54 (0) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Darcy Nicholls (`KXITFMATCH-26NOV09KAWNIC-NIC`) | 0.33 / 0.49 (9) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rio Noguchi vs Daniel Michalski -- ATP Challenger Matsuyama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200677:207415:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Michalski (`KXATPCHALLENGERMATCH-26NOV09NOGMIC-MIC`) | 0.47 / 0.49 (999) | 48.0% | 42.8% | 50.0% | 46.4% [43.8%-47.9%] | -- | 49.5% | 49.5% | MODEL_LONE_OUTLIER | PASS | -5.2 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Rio Noguchi (`KXATPCHALLENGERMATCH-26NOV09NOGMIC-NOG`) | 0.51 / 0.53 (842) | 52.0% | 57.2% | 50.0% | 53.6% [52.1%-56.2%] | -- | 51.9% | 51.9% | MODEL_LONE_OUTLIER | PASS | +5.2 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4350.0, B 3390.0; serve-point win A 59.0%, B 42.4%; Elo A 1603.5, B 1512.0; model uncertainty 0.0207
* Form inputs: days since last match A 14, B 7; matches on record A 575, B 490; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Gunawan Trismuwantara vs Darrshan Suresh -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207559:211326:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Darrshan Suresh (`KXITFMATCH-26NOV09TRISUR-SUR`) | 0.13 / 0.26 (5) | 19.5% | 46.7% | 31.6% | 47.9% [44.9%-50.0%] | -- | -- | -- | -- | PASS | +27.2 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gunawan Trismuwantara (`KXITFMATCH-26NOV09TRISUR-TRI`) | 0.66 / 0.80 (1) | 73.0% | 53.3% | 68.4% | 52.1% [50.0%-55.1%] | -- | -- | -- | -- | PASS | -19.7 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 301.0, B 602.0; serve-point win A 60.3%, B 40.4%; Elo A 1067.7, B 1076.4; model uncertainty 0.0257
* Form inputs: days since last match A 357, B 196; matches on record A 24, B 31; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09TRISUR-SUR  (YES = Darrshan Suresh)
Model: 47%
Kalshi: 20%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Azuma Visaya vs Shaheed Alam -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207180:210405:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shaheed Alam (`KXITFMATCH-26NOV09VISALA-ALA`) | 0.22 / 0.23 (37) | 22.5% | 34.5% | 20.9% | 32.3% [29.5%-33.9%] | -- | -- | -- | -- | PASS | +12.0 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Azuma Visaya (`KXITFMATCH-26NOV09VISALA-VIS`) | 0.71 / 0.84 (15) | 77.5% | 65.5% | 79.1% | 67.7% [66.1%-70.5%] | -- | -- | -- | -- | PASS | -12.0 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 253.0, B 112.0; serve-point win A 59.7%, B 43.3%; Elo A 1230.0, B 1109.9; model uncertainty 0.0221
* Form inputs: days since last match A 350, B 455; matches on record A 11, B 17; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ha Minh Duc Vu vs Tin Chen -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144844:210666:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tin Chen (`KXITFMATCH-26NOV09VUXCHE-CHE`) | 0.50 / 0.83 (16) | 66.5% | 62.3% | 78.7% | 60.3% [59.2%-62.4%] | -- | -- | -- | -- | PASS | -4.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ha Minh Duc Vu (`KXITFMATCH-26NOV09VUXCHE-VUX`) | 0.23 / 0.44 (2) | 33.5% | 37.7% | 21.3% | 39.7% [37.6%-40.8%] | -- | -- | -- | -- | PASS | +4.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 335.0, B 0.0; serve-point win A 57.5%, B 40.1%; Elo A 1113.0, B 1186.6; model uncertainty 0.0156
* Form inputs: days since last match A 56, B 1288; matches on record A 26, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.020, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Natsuki Yamamoto vs Konstantinos Loukopoulos -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:214325:214509:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Konstantinos Loukopoulos (`KXITFMATCH-26NOV09YAMLOU-LOU`) | 0.22 / 0.39 (6) | 30.5% | 36.5% | 30.3% | 41.8% [40.9%-42.8%] | -- | -- | -- | -- | PASS | +6.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Natsuki Yamamoto (`KXITFMATCH-26NOV09YAMLOU-YAM`) | 0.69 / 0.75 (100) | 72.0% | 63.5% | 69.7% | 58.2% [57.2%-59.1%] | -- | -- | -- | -- | PASS | -8.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 133.0, B 91.0; serve-point win A 61.9%, B 40.7%; Elo A 1270.8, B 1220.6; model uncertainty 0.0099
* Form inputs: days since last match A 210, B 343; matches on record A 2, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Beck / Sibai vs Bennemann / Kokkinis -- W75 Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09BECSIBBENKOK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beck / Sibai (`KXITFWDOUBLES-26NOV09BECSIBBENKOK-BECSIB`) | 0.39 / 0.77 (3) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bennemann / Kokkinis (`KXITFWDOUBLES-26NOV09BECSIBBENKOK-BENKOK`) | 0.44 / 0.78 (5) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Broadus / Ivanov vs Wei / Yuan -- W75 Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09BROIVAWEIYUA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Broadus / Ivanov (`KXITFWDOUBLES-26NOV09BROIVAWEIYUA-BROIVA`) | 0.06 / 0.89 (56) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Wei / Yuan (`KXITFWDOUBLES-26NOV09BROIVAWEIYUA-WEIYUA`) | 0.07 / 0.89 (56) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Tiana Tian Deng vs Yuhan Wang -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260528:264205:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tiana Tian Deng (`KXITFWMATCH-26NOV09DENWAN-DEN`) | 0.36 / 0.37 (30) | 36.5% | 26.8% | 28.2% | 30.1% [28.2%-31.5%] | -- | -- | -- | -- | PASS | -9.8 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuhan Wang (`KXITFWMATCH-26NOV09DENWAN-WAN`) | 0.57 / 0.60 (191) | 58.5% | 73.2% | 71.8% | 69.9% [68.5%-71.8%] | -- | -- | -- | -- | WATCH | +14.8 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 853.0, B 1724.0; serve-point win A 50.8%, B 44.5%; Elo A 1288.7, B 1428.1; model uncertainty 0.0163
* Form inputs: days since last match A 126, B 39; matches on record A 41, B 44; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.014, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Merel Hoedt vs Yujia Huang -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220491:264207:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Merel Hoedt (`KXITFWMATCH-26NOV09HOEHUA-HOE`) | 0.22 / 0.23 (26) | 22.5% | 40.0% | 42.1% | 42.6% [39.5%-47.9%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +17.5 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yujia Huang (`KXITFWMATCH-26NOV09HOEHUA-HUA`) | 0.75 / 0.78 (28) | 76.5% | 60.0% | 57.9% | 57.4% [52.1%-60.5%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.5 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2333.0, B 1640.0; serve-point win A 53.3%, B 44.8%; Elo A 1399.4, B 1447.1; model uncertainty 0.042
* Form inputs: days since last match A 210, B 36; matches on record A 368, B 88; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV09HOEHUA-HOE  (YES = Merel Hoedt)
Model: 40%
Kalshi: 22%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.031, surface_dev_loose -0.005, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Priska Madelyn Nugroho vs Natsuki Yoshimoto -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221187:264144:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Priska Madelyn Nugroho (`KXITFWMATCH-26NOV09NUGYOS-NUG`) | 0.69 / 0.76 (61) | 72.5% | 43.5% | 31.6% | 39.0% [33.5%-48.9%] | -- | -- | -- | -- | PASS | -29.0 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Natsuki Yoshimoto (`KXITFWMATCH-26NOV09NUGYOS-YOS`) | 0.24 / 0.28 (5) | 26.0% | 56.5% | 68.4% | 61.0% [51.1%-66.5%] | -- | -- | -- | -- | WATCH | +30.5 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2457.0, B 1600.0; serve-point win A 54.8%, B 44.0%; Elo A 1567.2, B 1591.4; model uncertainty 0.077
* Form inputs: days since last match A 224, B 203; matches on record A 235, B 50; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV09NUGYOS-YOS  (YES = Natsuki Yoshimoto)
Model: 56%
Kalshi: 26%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.020, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chia Yi Tsao vs Ekaterina Ovcharenko -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215733:259623:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Ovcharenko (`KXITFWMATCH-26NOV09TSAOVC-OVC`) | 0.41 / 0.44 (41) | 42.5% | 47.2% | 24.5% | 39.7% [30.2%-55.3%] | -- | -- | -- | -- | PASS | +4.8 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chia Yi Tsao (`KXITFWMATCH-26NOV09TSAOVC-TSA`) | 0.52 / 0.57 (1) | 54.5% | 52.8% | 75.5% | 60.3% [44.7%-69.8%] | -- | -- | -- | -- | WATCH | -1.8 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 824.0, B 1300.0; serve-point win A 59.1%, B 41.4%; Elo A 1482.7, B 1475.5; model uncertainty 0.1253
* Form inputs: days since last match A 203, B 63; matches on record A 145, B 323; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.056, surface_pool_high +0.054, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## JiaYi Wang vs Cheuk Ying Shek -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263941:265692:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cheuk Ying Shek (`KXITFWMATCH-26NOV09WANSHE-SHE`) | 0.30 / 0.34 (42) | 32.0% | 39.8% | 42.0% | 42.6% [41.5%-43.6%] | -- | -- | -- | -- | WATCH | +7.8 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| JiaYi Wang (`KXITFWMATCH-26NOV09WANSHE-WAN`) | 0.61 / 0.64 (28) | 62.5% | 60.2% | 58.0% | 57.4% [56.4%-58.5%] | -- | -- | -- | -- | PASS | -2.3 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2216.0, B 1558.0; serve-point win A 54.1%, B 47.8%; Elo A 1510.1, B 1458.4; model uncertainty 0.0105
* Form inputs: days since last match A 41, B 9; matches on record A 72, B 49; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.011, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexey Aleshchev vs Lingxi Zhao -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:134310:206789:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexey Aleshchev (`KXITFMATCH-26NOV09ALEZHA-ALE`) | 0.14 / 0.18 (4) | 16.0% | 21.2% | 14.3% | 21.4% [19.1%-23.5%] | -- | -- | -- | -- | PASS | +5.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lingxi Zhao (`KXITFMATCH-26NOV09ALEZHA-ZHA`) | 0.76 / 0.84 (197) | 80.0% | 78.8% | 85.7% | 78.6% [76.5%-80.9%] | -- | -- | -- | -- | PASS | -1.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1173.0, B 337.0; serve-point win A 56.0%, B 37.8%; Elo A 1059.7, B 1269.4; model uncertainty 0.0219
* Form inputs: days since last match A 196, B 385; matches on record A 69, B 39; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lin Hao-Yu vs masaki ishikawa -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09HAOISH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lin Hao-Yu (`KXITFMATCH-26NOV09HAOISH-HAO`) | 0.45 / 0.52 (22) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| masaki ishikawa (`KXITFMATCH-26NOV09HAOISH-ISH`) | 0.43 / 0.53 (206) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zhe Jiang vs Zhenxiong Dong -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09JIADON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zhenxiong Dong (`KXITFMATCH-26NOV09JIADON-DON`) | 0.80 / 0.84 (5) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zhe Jiang (`KXITFMATCH-26NOV09JIADON-JIA`) | 0.15 / 0.22 (23) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arjun Kadhe / Aoran Wang vs Kazushi Idogaki / Kentaro Otsuka -- ATP Challenger Matsuyama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-10T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09KADWANIDOOTS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kazushi Idogaki / Kentaro Otsuka (`KXATPCHALLENGERDOUBLES-26NOV09KADWANIDOOTS-IDOOTS`) | 0.20 / 0.39 (56) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arjun Kadhe / Aoran Wang (`KXATPCHALLENGERDOUBLES-26NOV09KADWANIDOOTS-KADWAN`) | 0.67 / 0.90 (39) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Arkhip Kozlov vs Jordan Chiu -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09KOZCHI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jordan Chiu (`KXITFMATCH-26NOV09KOZCHI-CHI`) | 0.79 / 0.85 (147) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arkhip Kozlov (`KXITFMATCH-26NOV09KOZCHI-KOZ`) | 0.13 / 0.15 (29) | 14.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yusuke Kusuhara / Shunsuke Nakagawa vs Riki Takahata / Saki Tange -- ATP Challenger Matsuyama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-10T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09KUSNAKTAKTAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yusuke Kusuhara / Shunsuke Nakagawa (`KXATPCHALLENGERDOUBLES-26NOV09KUSNAKTAKTAN-KUSNAK`) | 0.84 / 0.93 (6) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Riki Takahata / Saki Tange (`KXATPCHALLENGERDOUBLES-26NOV09KUSNAKTAKTAN-TAKTAN`) | 0.08 / 0.35 (15) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Shaoyun Liu vs Siu Chi Nicholas Cheng -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212180:213177:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Siu Chi Nicholas Cheng (`KXITFMATCH-26NOV09LIUCHE-CHE`) | 0.35 / 0.38 (47) | 36.5% | 65.4% | 55.2% | 67.0% [65.2%-67.9%] | -- | -- | -- | -- | PASS | +28.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Shaoyun Liu (`KXITFMATCH-26NOV09LIUCHE-LIU`) | 0.58 / 0.66 (5) | 62.0% | 34.6% | 44.8% | 33.0% [32.1%-34.8%] | -- | -- | -- | -- | PASS | -27.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 496.0, B 82.0; serve-point win A 57.9%, B 39.1%; Elo A 1138.5, B 1263.7; model uncertainty 0.0136
* Form inputs: days since last match A 203, B 276; matches on record A 21, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09LIUCHE-CHE  (YES = Siu Chi Nicholas Cheng)
Model: 65%
Kalshi: 36%
Gap: +29 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.009, surface_dev_loose -0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kangyuan Shi vs jintao Lan -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09SHILAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| jintao Lan (`KXITFMATCH-26NOV09SHILAN-LAN`) | 0.41 / 0.45 (45) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kangyuan Shi (`KXITFMATCH-26NOV09SHILAN-SHI`) | 0.51 / 0.52 (52) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yue Xia vs Zichen Shao -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09XIASHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zichen Shao (`KXITFMATCH-26NOV09XIASHA-SHA`) | 0.31 / 0.48 (6) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yue Xia (`KXITFMATCH-26NOV09XIASHA-XIA`) | 0.52 / 0.68 (11) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xiaoyin Yang vs Kaigaoge Kang -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 07:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T07:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212466:214011:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kaigaoge Kang (`KXITFMATCH-26NOV09YANKAN-KAN`) | 0.33 / 0.37 (39) | 35.0% | 53.9% | 68.5% | 63.5% [62.0%-64.3%] | -- | -- | -- | -- | PASS | +18.9 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xiaoyin Yang (`KXITFMATCH-26NOV09YANKAN-YAN`) | 0.57 / 0.64 (42) | 60.5% | 46.1% | 31.5% | 36.5% [35.7%-38.0%] | -- | -- | -- | -- | PASS | -14.4 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 817.0, B 207.0; serve-point win A 64.4%, B 34.8%; Elo A 1172.5, B 1261.8; model uncertainty 0.0113
* Form inputs: days since last match A 210, B 48; matches on record A 21, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09YANKAN-KAN  (YES = Kaigaoge Kang)
Model: 54%
Kalshi: 35%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose +0.001, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sohyun Park vs Naiktha Bains -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206362:216213:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naiktha Bains (`KXITFWMATCH-26NOV09PARBAI-BAI`) | 0.49 / 0.53 (17) | 51.0% | 35.9% | 41.6% | 40.1% [38.0%-42.1%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.1 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sohyun Park (`KXITFWMATCH-26NOV09PARBAI-PAR`) | 0.46 / 0.51 (169) | 48.5% | 64.0% | 58.4% | 59.9% [57.9%-62.0%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +15.6 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3623.0, B 2400.0; serve-point win A 57.4%, B 45.3%; Elo A 1658.9, B 1570.3; model uncertainty 0.0205
* Form inputs: days since last match A 47, B 46; matches on record A 366, B 483; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV09PARBAI-PAR  (YES = Sohyun Park)
Model: 64%
Kalshi: 48%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.020, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Wushuang Zheng vs Zhuoxuan Bai -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:213821:222296:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zhuoxuan Bai (`KXITFWMATCH-26NOV09ZHEBAI-BAI`) | 0.62 / 0.66 (5) | 64.0% | 85.5% | 90.5% | 85.2% [74.4%-89.1%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +21.6 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Wushuang Zheng (`KXITFWMATCH-26NOV09ZHEBAI-ZHE`) | 0.34 / 0.37 (6) | 35.5% | 14.4% | 9.5% | 14.8% [10.9%-25.6%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -21.1 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2161.0, B 1601.0; serve-point win A 48.6%, B 43.5%; Elo A 1552.0, B 1765.4; model uncertainty 0.0734
* Form inputs: days since last match A 34, B 31; matches on record A 302, B 213; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV09ZHEBAI-BAI  (YES = Zhuoxuan Bai)
Model: 86%
Kalshi: 64%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.012, surface_dev_loose -0.018, surface_dev_tight +0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adam Bajurko vs Takumi Katsuda -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09BAJKAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adam Bajurko (`KXITFMATCH-26NOV09BAJKAT-BAJ`) | 0.22 / 0.32 (1) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Takumi Katsuda (`KXITFMATCH-26NOV09BAJKAT-KAT`) | 0.63 / 0.76 (0) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## David Eichenseher vs Hao Sheng Koay -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144896:212631:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Eichenseher (`KXITFMATCH-26NOV09EICKOA-EIC`) | 0.75 / 0.78 (28) | 76.5% | 45.5% | 25.6% | 36.9% [35.0%-38.8%] | -- | -- | -- | -- | PASS | -31.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hao Sheng Koay (`KXITFMATCH-26NOV09EICKOA-KOA`) | 0.20 / 0.24 (150) | 22.0% | 54.5% | 74.4% | 63.1% [61.2%-65.0%] | -- | -- | -- | -- | PASS | +32.5 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1106.0, B 241.0; serve-point win A 60.0%, B 39.1%; Elo A 1194.2, B 1273.3; model uncertainty 0.0194
* Form inputs: days since last match A 196, B 364; matches on record A 30, B 10; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09EICKOA-KOA  (YES = Hao Sheng Koay)
Model: 55%
Kalshi: 22%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Naufal Siddiq Kamaruzzaman vs Samarth Sahita -- M15 Kuala Lumpur R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208141:213805:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naufal Siddiq Kamaruzzaman (`KXITFMATCH-26NOV09KAMSAH-KAM`) | 0.21 / 0.38 (3) | 29.5% | 35.4% | 36.5% | 36.0% [35.9%-36.9%] | -- | -- | -- | -- | PASS | +5.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Samarth Sahita (`KXITFMATCH-26NOV09KAMSAH-SAH`) | 0.65 / 0.81 (4) | 73.0% | 64.6% | 63.5% | 64.0% [63.1%-64.1%] | -- | -- | -- | -- | PASS | -8.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 188.0, B 96.0; serve-point win A 59.6%, B 37.5%; Elo A 1120.9, B 1217.6; model uncertainty 0.0048
* Form inputs: days since last match A 350, B 231; matches on record A 6, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Quoc Cuong / Phat Nguyen vs Bult / Wright -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09QUOPHABULWRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bult / Wright (`KXITFDOUBLES-26NOV09QUOPHABULWRI-BULWRI`) | 0.54 / 0.75 (100) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Quoc Cuong / Phat Nguyen (`KXITFDOUBLES-26NOV09QUOPHABULWRI-QUOPHA`) | 0.31 / 0.40 (41) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Kai-An Wu vs Hien Pham -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09WUXPHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hien Pham (`KXITFMATCH-26NOV09WUXPHA-PHA`) | 0.49 / 0.70 (5) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kai-An Wu (`KXITFMATCH-26NOV09WUXPHA-WUX`) | 0.25 / 0.46 (51) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mayuka Aikawa vs Kamonwan Yodpetch -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:219892:259907:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mayuka Aikawa (`KXITFWMATCH-26NOV09AIKYOD-AIK`) | 0.54 / 0.65 (120) | 59.5% | 50.9% | 44.8% | 56.3% [51.6%-65.5%] | -- | -- | -- | -- | PASS | -8.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kamonwan Yodpetch (`KXITFWMATCH-26NOV09AIKYOD-YOD`) | 0.36 / 0.40 (47) | 38.0% | 49.1% | 55.2% | 43.7% [34.5%-48.4%] | -- | -- | -- | -- | PASS | +11.1 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1667.0, B 1037.0; serve-point win A 56.9%, B 43.3%; Elo A 1428.9, B 1326.6; model uncertainty 0.0696
* Form inputs: days since last match A 231, B 196; matches on record A 303, B 72; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.021, surface_dev_loose -0.005, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jialan Cai vs Yajing Cao -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263764:267498:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jialan Cai (`KXITFWMATCH-26NOV09CAICAO-CAI`) | 0.48 / 0.54 (7) | 51.0% | 49.4% | 50.0% | 47.9% [46.8%-48.9%] | -- | -- | -- | -- | PASS | -1.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yajing Cao (`KXITFWMATCH-26NOV09CAICAO-CAO`) | 0.43 / 0.50 (50) | 46.5% | 50.6% | 50.0% | 52.1% [51.1%-53.2%] | -- | -- | -- | -- | PASS | +4.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 204.0, B 105.0; serve-point win A 54.3%, B 45.6%; Elo A 1218.7, B 1231.6; model uncertainty 0.0106
* Form inputs: days since last match A 210, B 196; matches on record A 11, B 55; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nagi Hanatani vs Sae Noguchi -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211544:269866:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nagi Hanatani (`KXITFWMATCH-26NOV09HANNOG-HAN`) | 0.13 / 0.16 (11) | 14.5% | 23.5% | 15.2% | 24.3% [18.1%-35.4%] | -- | -- | -- | -- | PASS | +9.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sae Noguchi (`KXITFWMATCH-26NOV09HANNOG-NOG`) | 0.80 / 0.84 (39) | 82.0% | 76.5% | 84.9% | 75.7% [64.6%-81.9%] | -- | -- | -- | -- | PASS | -5.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1219.0, B 1076.0; serve-point win A 50.3%, B 44.2%; Elo A 1328.0, B 1452.4; model uncertainty 0.0863
* Form inputs: days since last match A 196, B 210; matches on record A 446, B 33; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.012, surface_dev_loose -0.012, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuno Kitahara vs Kisa Yoshioka -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215616:263881:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuno Kitahara (`KXITFWMATCH-26NOV09KITYOS-KIT`) | 0.50 / 0.60 (52) | 55.0% | 63.1% | 70.4% | 64.6% [59.5%-69.0%] | -- | -- | -- | -- | PASS | +8.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kisa Yoshioka (`KXITFWMATCH-26NOV09KITYOS-YOS`) | 0.44 / 0.45 (52) | 44.5% | 36.9% | 29.6% | 35.4% [31.0%-40.5%] | -- | -- | -- | -- | PASS | -7.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2068.0, B 1530.0; serve-point win A 53.5%, B 49.0%; Elo A 1428.6, B 1360.1; model uncertainty 0.0475
* Form inputs: days since last match A 203, B 203; matches on record A 119, B 159; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xiaowei Li vs Ziyu Zhou -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09LIXZHO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xiaowei Li (`KXITFWMATCH-26NOV09LIXZHO-LIX`) | 0.49 / 0.56 (61) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ziyu Zhou (`KXITFWMATCH-26NOV09LIXZHO-ZHO`) | 0.40 / 0.51 (20) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elena Micic vs Lizette Cabrera -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211878:239397:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lizette Cabrera (`KXITFWMATCH-26NOV09MICCAB-CAB`) | 0.51 / 0.54 (50) | 52.5% | 66.0% | 60.0% | 60.0% [58.9%-63.0%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +13.5 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Micic (`KXITFWMATCH-26NOV09MICCAB-MIC`) | 0.46 / 0.49 (90) | 47.5% | 34.0% | 40.1% | 40.1% [37.0%-41.1%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.5 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3357.0, B 3443.0; serve-point win A 54.4%, B 42.5%; Elo A 1573.4, B 1648.1; model uncertainty 0.0205
* Form inputs: days since last match A 34, B 49; matches on record A 218, B 524; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ena Shibahara vs Mutsumi Uemura -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214262:260828:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ena Shibahara (`KXITFWMATCH-26NOV09SHIUEM-SHI`) | 0.78 / 0.83 (14) | 80.5% | 92.0% | 71.0% | 83.2% [80.8%-87.8%] | -- | -- | -- | -- | PASS | +11.5 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mutsumi Uemura (`KXITFWMATCH-26NOV09SHIUEM-UEM`) | 0.17 / 0.20 (30) | 18.5% | 8.0% | 29.0% | 16.8% [12.2%-19.2%] | -- | -- | -- | -- | PASS | -10.5 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3247.0, B 824.0; serve-point win A 62.5%, B 48.2%; Elo A 1668.7, B 1314.4; model uncertainty 0.0351
* Form inputs: days since last match A 16, B 203; matches on record A 251, B 22; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.007, surface_dev_loose +0.006, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Junlu Sun vs Ziyan Zhang -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09SUNZHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Junlu Sun (`KXITFWMATCH-26NOV09SUNZHA-SUN`) | 0.83 / 0.86 (6) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ziyan Zhang (`KXITFWMATCH-26NOV09SUNZHA-ZHA`) | 0.09 / 0.13 (33) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xiao Tang vs Jiyun Oh -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:267516:270339:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiyun Oh (`KXITFWMATCH-26NOV09TANOHX-OHX`) | 0.35 / 0.52 (2) | 43.5% | 52.1% | 53.8% | 54.3% [54.3%-55.4%] | -- | -- | -- | -- | PASS | +8.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xiao Tang (`KXITFWMATCH-26NOV09TANOHX-TAN`) | 0.48 / 0.64 (76) | 56.0% | 47.9% | 46.2% | 45.7% [44.6%-45.7%] | -- | -- | -- | -- | PASS | -8.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 206.0, B 161.0; serve-point win A 51.1%, B 48.5%; Elo A 1253.5, B 1285.1; model uncertainty 0.0054
* Form inputs: days since last match A 196, B 196; matches on record A 6, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ho Ching Wu vs Yu-Ning Tsai -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211208:267855:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yu-Ning Tsai (`KXITFWMATCH-26NOV09WUXTSA-TSA`) | 0.26 / 0.35 (43) | 30.5% | 32.3% | 68.1% | 38.9% [36.9%-42.0%] | -- | -- | -- | -- | PASS | +1.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ho Ching Wu (`KXITFWMATCH-26NOV09WUXTSA-WUX`) | 0.60 / 0.76 (11) | 68.0% | 67.7% | 31.9% | 61.1% [58.0%-63.1%] | -- | -- | -- | -- | PASS | -0.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 678.0, B 181.0; serve-point win A 54.5%, B 48.9%; Elo A 1398.9, B 1291.5; model uncertainty 0.0258
* Form inputs: days since last match A 196, B 217; matches on record A 414, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.020, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sara Yoshida vs Marianna Shikhanova -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:267419:269845:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marianna Shikhanova (`KXITFWMATCH-26NOV09YOSSHI-SHI`) | 0.35 / 0.48 (11) | 41.5% | 46.2% | 75.2% | 52.1% [51.1%-53.2%] | -- | -- | -- | -- | PASS | +4.7 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sara Yoshida (`KXITFWMATCH-26NOV09YOSSHI-YOS`) | 0.52 / 0.64 (5) | 58.0% | 53.8% | 24.8% | 47.9% [46.8%-48.9%] | -- | -- | -- | -- | PASS | -4.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 151.0, B 49.0; serve-point win A 54.3%, B 46.4%; Elo A 1200.0, B 1210.1; model uncertainty 0.0106
* Form inputs: days since last match A 203, B 378; matches on record A 8, B 6; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Wenfei Yu vs Yinuo Huang -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264184:270197:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yinuo Huang (`KXITFWMATCH-26NOV09YUXHUA-HUA`) | 0.09 / 0.11 (387) | 10.0% | 20.4% | 46.3% | 37.4% [37.4%-38.4%] | -- | -- | -- | -- | PASS | +10.4 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Wenfei Yu (`KXITFWMATCH-26NOV09YUXHUA-YUX`) | 0.87 / 0.90 (3) | 88.5% | 79.5% | 53.7% | 62.6% [61.6%-62.6%] | -- | -- | -- | -- | PASS | -8.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 238.0, B 38.0; serve-point win A 56.0%, B 50.1%; Elo A 1351.8, B 1266.3; model uncertainty 0.0052
* Form inputs: days since last match A 196, B 455; matches on record A 35, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xichen Zhao vs Noelani Sara Teso -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 08:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:252494:267873:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noelani Sara Teso (`KXITFWMATCH-26NOV09ZHATES-TES`) | 0.05 / 0.10 (5) | 7.5% | 24.8% | 50.0% | 32.4% [27.8%-36.3%] | -- | -- | -- | -- | PASS | +17.3 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xichen Zhao (`KXITFWMATCH-26NOV09ZHATES-ZHA`) | 0.85 / 0.93 (5) | 89.0% | 75.2% | 50.0% | 67.6% [63.7%-72.2%] | -- | -- | -- | -- | PASS | -13.8 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 896.0, B 471.0; serve-point win A 54.0%, B 51.0%; Elo A 1293.3, B 1129.9; model uncertainty 0.0428
* Form inputs: days since last match A 196, B 413; matches on record A 133, B 25; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV09ZHATES-TES  (YES = Noelani Sara Teso)
Model: 25%
Kalshi: 8%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Papangkorn Bunyarit vs Hong-Lin Fu -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09BUNFUX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Papangkorn Bunyarit (`KXITFMATCH-26NOV09BUNFUX-BUN`) | 0.33 / 0.34 (5) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hong-Lin Fu (`KXITFMATCH-26NOV09BUNFUX-FUX`) | 0.67 / 0.93 (1) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thanapet Chanta vs Tanakorn Srirat -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207788:213189:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thanapet Chanta (`KXITFMATCH-26NOV09CHASRI-CHA`) | 0.93 / 0.96 (573) | 94.5% | 78.5% | 71.7% | 65.2% [65.2%-67.2%] | -- | -- | -- | -- | PASS | -16.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tanakorn Srirat (`KXITFMATCH-26NOV09CHASRI-SRI`) | 0.05 / 0.06 (382) | 5.5% | 21.5% | 28.3% | 34.8% [32.8%-34.8%] | -- | -- | -- | -- | PASS | +16.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2163.0, B 108.0; serve-point win A 61.7%, B 44.4%; Elo A 1328.2, B 1218.9; model uncertainty 0.0098
* Form inputs: days since last match A 175, B 378; matches on record A 160, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09CHASRI-SRI  (YES = Tanakorn Srirat)
Model: 21%
Kalshi: 6%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fons Van Sambeek vs Thantub Suksumrarn -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209171:209913:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thantub Suksumrarn (`KXITFMATCH-26NOV09VANSUK-SUK`) | 0.37 / 0.40 (34) | 38.5% | 48.5% | 40.8% | 49.0% [45.4%-55.1%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.0 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Fons Van Sambeek (`KXITFMATCH-26NOV09VANSUK-VAN`) | 0.59 / 0.62 (32) | 60.5% | 51.5% | 59.2% | 51.0% [44.9%-54.6%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1119.0, B 1818.0; serve-point win A 60.8%, B 39.5%; Elo A 1248.8, B 1281.6; model uncertainty 0.0487
* Form inputs: days since last match A 196, B 196; matches on record A 58, B 105; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sato / Tse vs Yamalapalli / Yang -- W75 Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09SATTSEYAMYAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sato / Tse (`KXITFWDOUBLES-26NOV09SATTSEYAMYAN-SATTSE`) | 0.07 / 0.89 (56) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yamalapalli / Yang (`KXITFWDOUBLES-26NOV09SATTSEYAMYAN-YAMYAN`) | 0.06 / 0.89 (56) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Himeno Sakatsume vs Alana Subasic -- W75 Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221124:261049:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Himeno Sakatsume (`KXITFWMATCH-26NOV09SAKSUB-SAK`) | 0.85 / 0.92 (14) | 88.5% | 90.3% | 78.1% | 80.4% [79.3%-82.2%] | -- | -- | -- | -- | PASS | +1.8 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alana Subasic (`KXITFWMATCH-26NOV09SAKSUB-SUB`) | 0.08 / 0.12 (34) | 10.0% | 9.7% | 21.9% | 19.6% [17.8%-20.7%] | -- | -- | -- | -- | WATCH | -0.3 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3693.0, B 2964.0; serve-point win A 58.3%, B 51.5%; Elo A 1764.5, B 1463.4; model uncertainty 0.0146
* Form inputs: days since last match A 6, B 196; matches on record A 421, B 101; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose +0.007, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Blando / Blando vs Kamath / Suresh -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09BLABLAKAMSUR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blando / Blando (`KXITFDOUBLES-26NOV09BLABLAKAMSUR-BLABLA`) | 0.62 / 0.73 (92) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kamath / Suresh (`KXITFDOUBLES-26NOV09BLABLAKAMSUR-KAMSUR`) | 0.23 / 0.45 (45) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Kuan-Shou Chen vs Tomohiro Masabayashi -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144730:213769:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kuan-Shou Chen (`KXITFMATCH-26NOV09CHEMAS-CHE`) | 0.85 / 0.89 (100) | 87.0% | 46.8% | 76.2% | 51.1% [47.9%-54.8%] | 90.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -40.2 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tomohiro Masabayashi (`KXITFMATCH-26NOV09CHEMAS-MAS`) | 0.11 / 0.12 (22) | 11.5% | 53.2% | 23.8% | 48.9% [45.2%-52.1%] | 9.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +41.7 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 224.0, B 1636.0; serve-point win A 56.1%, B 43.3%; Elo A 1173.8, B 1192.1; model uncertainty 0.0343
* Form inputs: days since last match A 7, B 196; matches on record A 6, B 144; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09CHEMAS-MAS  (YES = Tomohiro Masabayashi)
Model: 53%
Kalshi: 12%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dong / Kose vs Qariaqus / Talic -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09DONKOSQARTAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dong / Kose (`KXITFDOUBLES-26NOV09DONKOSQARTAL-DONKOS`) | 0.47 / 0.60 (62) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Qariaqus / Talic (`KXITFDOUBLES-26NOV09DONKOSQARTAL-QARTAL`) | 0.39 / 0.60 (62) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Faleh Alhogbani / Cherie Ligniere vs Jun Kim / Murtaza -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09FALCHEJUNMUR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Faleh Alhogbani / Cherie Ligniere (`KXITFDOUBLES-26NOV09FALCHEJUNMUR-FALCHE`) | 0.31 / 0.54 (56) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jun Kim / Murtaza (`KXITFDOUBLES-26NOV09FALCHEJUNMUR-JUNMUR`) | 0.40 / 0.64 (69) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Malaszszak / Fu Wong vs Sumizawa / Vithoontien -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09MALFUWSUMVIT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Malaszszak / Fu Wong (`KXITFDOUBLES-26NOV09MALFUWSUMVIT-MALFUW`) | 0.27 / 0.44 (44) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sumizawa / Vithoontien (`KXITFDOUBLES-26NOV09MALFUWSUMVIT-SUMVIT`) | 0.60 / 0.72 (27) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Manuel Plunger vs Oscar Brown -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211708:214341:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oscar Brown (`KXITFMATCH-26NOV09PLUBRO-BRO`) | 0.50 / 0.54 (40) | 52.0% | 57.9% | 63.3% | 58.8% [57.2%-62.4%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manuel Plunger (`KXITFMATCH-26NOV09PLUBRO-PLU`) | 0.46 / 0.49 (1) | 47.5% | 42.1% | 36.7% | 41.2% [37.6%-42.8%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 306.0, B 423.0; serve-point win A 57.8%, B 40.7%; Elo A 1230.7, B 1289.3; model uncertainty 0.0257
* Form inputs: days since last match A 511, B 196; matches on record A 39, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rifqi Fitriadi / Sarksian vs Adibi Rahiman / Farhanuddin Fariz -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09RIFSARADIFAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adibi Rahiman / Farhanuddin Fariz (`KXITFDOUBLES-26NOV09RIFSARADIFAR-ADIFAR`) | 0.07 / 0.90 (1) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rifqi Fitriadi / Sarksian (`KXITFDOUBLES-26NOV09RIFSARADIFAR-RIFSAR`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Berfu Cengiz vs Miho Kuramochi -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214507:246478:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Berfu Cengiz (`KXITFWMATCH-26NOV09CENKUR-CEN`) | 0.71 / 0.76 (55) | 73.5% | 62.3% | 48.4% | 50.0% [47.9%-53.2%] | -- | -- | -- | -- | PASS | -11.2 pp | REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Miho Kuramochi (`KXITFWMATCH-26NOV09CENKUR-KUR`) | 0.24 / 0.26 (60) | 25.0% | 37.7% | 51.6% | 50.0% [46.8%-52.1%] | -- | -- | -- | -- | PASS | +12.7 pp | REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1612.0, B 3111.0; serve-point win A 54.5%, B 47.8%; Elo A 1571.0, B 1555.6; model uncertainty 0.0267
* Form inputs: days since last match A 41, B 50; matches on record A 455, B 279; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.016, surface_dev_loose +0.027, surface_dev_tight -0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jia-Jing Lu vs Caroline Werner -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:203288:espn:espn:4384:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jia-Jing Lu (`KXITFWMATCH-26NOV09LUXWER-LUX`) | 0.43 / 0.48 (8) | 45.5% | 44.7% | 78.0% | 46.8% [45.8%-46.8%] | -- | -- | -- | -- | PASS | -0.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Caroline Werner (`KXITFWMATCH-26NOV09LUXWER-WER`) | 0.52 / 0.56 (50) | 54.0% | 55.3% | 22.0% | 53.2% [53.2%-54.2%] | -- | -- | -- | -- | PASS | +1.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3089.0, B 0.0; serve-point win A 54.0%, B 45.0%; Elo A 1582.4, B 1606.9; model uncertainty 0.0053
* Form inputs: days since last match A 34, B 12; matches on record A 905, B 25; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.011, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mio Mushika vs Remika Ohashi -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222986:260957:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mio Mushika (`KXITFWMATCH-26NOV09MUSOHA-MUS`) | 0.74 / 0.81 (1) | 77.5% | 85.1% | 94.3% | 78.8% [71.7%-85.4%] | -- | -- | -- | -- | PASS | +7.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Remika Ohashi (`KXITFWMATCH-26NOV09MUSOHA-OHA`) | 0.20 / 0.23 (31) | 21.5% | 14.9% | 5.7% | 21.1% [14.6%-28.3%] | -- | -- | -- | -- | PASS | -6.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2224.0, B 421.0; serve-point win A 58.1%, B 49.8%; Elo A 1520.7, B 1357.0; model uncertainty 0.0684
* Form inputs: days since last match A 203, B 203; matches on record A 201, B 44; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.004, surface_dev_loose +0.011, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kristiana Sidorova vs YeXin Ma -- W50 Yokohama R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 10:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09SIDMAX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| YeXin Ma (`KXITFWMATCH-26NOV09SIDMAX-MAX`) | 0.49 / 0.51 (39) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kristiana Sidorova (`KXITFWMATCH-26NOV09SIDMAX-SID`) | 0.46 / 0.52 (49) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Toshiki Karigyo vs Linang Xiao -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209038:213785:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Toshiki Karigyo (`KXITFMATCH-26NOV09KARXIA-KAR`) | 0.13 / 0.15 (27) | 14.0% | 30.5% | 34.7% | 40.2% [36.7%-43.8%] | -- | -- | -- | -- | PASS | +16.5 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Linang Xiao (`KXITFMATCH-26NOV09KARXIA-XIA`) | 0.82 / 0.85 (166) | 83.5% | 69.5% | 65.3% | 59.8% [56.2%-63.3%] | -- | -- | -- | -- | PASS | -14.0 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 515.0, B 1754.0; serve-point win A 56.5%, B 39.6%; Elo A 1270.7, B 1327.4; model uncertainty 0.0359
* Form inputs: days since last match A 350, B 14; matches on record A 9, B 146; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09KARXIA-KAR  (YES = Toshiki Karigyo)
Model: 30%
Kalshi: 14%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.015, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dingzheng Nima vs Ruochen Gao -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV09NIMGAO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ruochen Gao (`KXITFMATCH-26NOV09NIMGAO-GAO`) | 0.42 / 0.67 (75) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dingzheng Nima (`KXITFMATCH-26NOV09NIMGAO-NIM`) | 0.28 / 0.52 (52) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Qian Sun vs Sheng Tang -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207463:208229:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Qian Sun (`KXITFMATCH-26NOV09SUNTAN-SUN`) | 0.69 / 0.74 (2) | 71.5% | 53.5% | 55.1% | 52.5% [51.0%-54.6%] | -- | -- | -- | -- | PASS | -18.0 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sheng Tang (`KXITFMATCH-26NOV09SUNTAN-TAN`) | 0.25 / 0.33 (37) | 29.0% | 46.5% | 44.9% | 47.4% [45.4%-49.0%] | -- | -- | -- | -- | PASS | +17.5 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1071.0, B 714.0; serve-point win A 62.0%, B 38.6%; Elo A 1192.1, B 1177.1; model uncertainty 0.0177
* Form inputs: days since last match A 21, B 203; matches on record A 76, B 92; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09SUNTAN-TAN  (YES = Sheng Tang)
Model: 47%
Kalshi: 29%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Liuyan An vs Anna Yang -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264242:265015:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liuyan An (`KXITFWMATCH-26NOV09ANXYAN-ANX`) | 0.27 / 0.30 (41) | 28.5% | 35.3% | 31.1% | 37.9% [35.4%-40.5%] | -- | -- | -- | -- | PASS | +6.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Yang (`KXITFWMATCH-26NOV09ANXYAN-YAN`) | 0.68 / 0.69 (80) | 68.5% | 64.7% | 68.9% | 62.1% [59.5%-64.6%] | -- | -- | -- | -- | PASS | -3.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 425.0, B 270.0; serve-point win A 52.7%, B 44.5%; Elo A 1230.4, B 1302.6; model uncertainty 0.0253
* Form inputs: days since last match A 196, B 378; matches on record A 13, B 21; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thasaporn Naklo vs Yiru Chen -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220597:266372:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yiru Chen (`KXITFWMATCH-26NOV09NAKCHE-CHE`) | 0.05 / 0.09 (8) | 7.0% | 18.3% | 26.9% | 24.3% [22.7%-25.2%] | -- | -- | -- | -- | PASS | +11.3 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thasaporn Naklo (`KXITFWMATCH-26NOV09NAKCHE-NAK`) | 0.92 / 0.95 (5) | 93.5% | 81.7% | 73.1% | 75.7% [74.8%-77.3%] | -- | -- | -- | -- | PASS | -11.8 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2173.0, B 625.0; serve-point win A 56.4%, B 50.4%; Elo A 1456.9, B 1245.2; model uncertainty 0.0125
* Form inputs: days since last match A 196, B 196; matches on record A 166, B 28; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.008, surface_dev_loose +0.008, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jiaqi Wang vs Naoko Eto -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 10:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:205562:221181:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naoko Eto (`KXITFWMATCH-26NOV09WANETO-ETO`) | 0.03 / 0.04 (6) | 3.5% | 1.1% | 0.1% | 2.3% [0.7%-5.5%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiaqi Wang (`KXITFWMATCH-26NOV09WANETO-WAN`) | 0.95 / 0.97 (154) | 96.0% | 98.9% | 99.9% | 97.7% [94.5%-99.3%] | -- | -- | -- | -- | PASS | +2.9 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2849.0, B 643.0; serve-point win A 60.7%, B 56.5%; Elo A 1543.7, B 1068.0; model uncertainty 0.0237
* Form inputs: days since last match A 196, B 50; matches on record A 250, B 205; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.002, surface_dev_loose +0.003, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kawachi / Noguchi vs Eichenseher / Mueller -- M15 Kuala Lumpur R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10KAWNOGEICMUE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eichenseher / Mueller (`KXITFDOUBLES-26NOV10KAWNOGEICMUE-EICMUE`) | 0.47 / 0.68 (40) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kawachi / Noguchi (`KXITFDOUBLES-26NOV10KAWNOGEICMUE-KAWNOG`) | 0.40 / 0.51 (51) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Arcon / Lakshmanan vs Nakamura / Srirat -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ARCLAKNAKSRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arcon / Lakshmanan (`KXITFDOUBLES-26NOV10ARCLAKNAKSRI-ARCLAK`) | 0.62 / 0.75 (15) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nakamura / Srirat (`KXITFDOUBLES-26NOV10ARCLAKNAKSRI-NAKSRI`) | 0.27 / 0.32 (5) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gohil / Horak vs Chanta / Sornlaksup -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10GOHHORCHASOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chanta / Sornlaksup (`KXITFDOUBLES-26NOV10GOHHORCHASOR-CHASOR`) | 0.79 / 0.89 (56) | 84.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gohil / Horak (`KXITFDOUBLES-26NOV10GOHHORCHASOR-GOHHOR`) | 0.09 / 0.76 (3) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yuta Kikuchi vs Zhao Zhao -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206888:209043:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuta Kikuchi (`KXITFMATCH-26NOV10KIKZHA-KIK`) | 0.57 / 0.61 (5) | 59.0% | 80.3% | 57.3% | 74.4% [73.1%-76.0%] | -- | -- | -- | -- | PASS | +21.3 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zhao Zhao (`KXITFMATCH-26NOV10KIKZHA-ZHA`) | 0.37 / 0.42 (66) | 39.5% | 19.7% | 42.7% | 25.6% [24.0%-26.9%] | -- | -- | -- | -- | PASS | -19.8 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1925.0, B 155.0; serve-point win A 61.2%, B 45.4%; Elo A 1381.1, B 1177.3; model uncertainty 0.0146
* Form inputs: days since last match A 56, B 217; matches on record A 137, B 25; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10KIKZHA-KIK  (YES = Yuta Kikuchi)
Model: 80%
Kalshi: 59%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Natthayut Nithithananont vs Nazar Oliynykov -- M15 Hua Hin R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209396:212138:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Natthayut Nithithananont (`KXITFMATCH-26NOV10NITOLI-NIT`) | 0.10 / 0.11 (28) | 10.5% | 52.8% | 55.7% | 48.9% [47.9%-49.5%] | 10.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +42.3 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nazar Oliynykov (`KXITFMATCH-26NOV10NITOLI-OLI`) | 0.84 / 0.89 (11) | 86.5% | 47.2% | 44.3% | 51.0% [50.5%-52.1%] | 89.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -39.3 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 108.0, B 203.0; serve-point win A 58.4%, B 42.2%; Elo A 1100.6, B 1114.2; model uncertainty 0.0078
* Form inputs: days since last match A 441, B 238; matches on record A 16, B 8; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10NITOLI-NIT  (YES = Natthayut Nithithananont)
Model: 53%
Kalshi: 10%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.011, surface_dev_loose -0.011, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Meiqi Guo vs Jiayu Xu -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216162:222606:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Meiqi Guo (`KXITFWMATCH-26NOV10GUOXUX-GUO`) | 0.82 / 0.84 (156) | 83.0% | 88.7% | 94.0% | 82.7% [77.2%-87.9%] | -- | -- | -- | -- | PASS | +5.7 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiayu Xu (`KXITFWMATCH-26NOV10GUOXUX-XUX`) | 0.12 / 0.15 (5) | 13.5% | 11.3% | 6.0% | 17.3% [12.1%-22.8%] | -- | -- | -- | -- | WATCH | -2.2 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2729.0, B 444.0; serve-point win A 59.7%, B 49.4%; Elo A 1542.5, B 1324.1; model uncertainty 0.0534
* Form inputs: days since last match A 43, B 196; matches on record A 272, B 86; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.007, surface_dev_loose +0.013, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kim / Morisaki vs Sema / Yi Tsao -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10KIMMORSEMYIT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kim / Morisaki (`KXITFWDOUBLES-26NOV10KIMMORSEMYIT-KIMMOR`) | 0.38 / 0.62 (4) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sema / Yi Tsao (`KXITFWDOUBLES-26NOV10KIMMORSEMYIT-SEMYIT`) | 0.31 / 0.57 (7) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kobori / Shimizu vs Wang / Wang -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10KOBSHIWANWAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kobori / Shimizu (`KXITFWDOUBLES-26NOV10KOBSHIWANWAN-KOBSHI`) | 0.70 / 0.75 (11) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Wang / Wang (`KXITFWDOUBLES-26NOV10KOBSHIWANWAN-WANWAN`) | 0.17 / 0.36 (56) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Matsuda / Nakashima vs Hayasaka / Naito -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10MATNAKHAYNAI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hayasaka / Naito (`KXITFWDOUBLES-26NOV10MATNAKHAYNAI-HAYNAI`) | 0.26 / 0.41 (56) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matsuda / Nakashima (`KXITFWDOUBLES-26NOV10MATNAKHAYNAI-MATNAK`) | 0.62 / 0.76 (56) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Jeong Moon vs Alexandra Malova -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10MOOMAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Malova (`KXITFWMATCH-26NOV10MOOMAL-MAL`) | 0.79 / 0.84 (12) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeong Moon (`KXITFWMATCH-26NOV10MOOMAL-MOO`) | 0.16 / 0.20 (40) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nagata / Tsutsumi vs Li / Saito -- W50 Yokohama R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10NAGTSULIXSAI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Li / Saito (`KXITFWDOUBLES-26NOV10NAGTSULIXSAI-LIXSAI`) | 0.71 / 0.90 (1) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nagata / Tsutsumi (`KXITFWDOUBLES-26NOV10NAGTSULIXSAI-NAGTSU`) | 0.06 / 0.22 (32) | 14.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Pankratova / Varaksina vs Im / Shin -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10PANVARIMXSHI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Im / Shin (`KXITFWDOUBLES-26NOV10PANVARIMXSHI-IMXSHI`) | 0.78 / 0.90 (1) | 84.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pankratova / Varaksina (`KXITFWDOUBLES-26NOV10PANVARIMXSHI-PANVAR`) | 0.06 / 0.15 (29) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Adrian Mannarino vs Aleksandr Shevchenko -- ATP Stockholm R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-10 15:00Z
* Current expected start: 2026-11-10 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 18:39Z
* Recommended handicap-by time: 2026-11-10 11:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-10T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105173:207686:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Mannarino (`KXATPMATCH-26NOV10MANSHE-MAN`) | 0.53 / 0.55 (10833) | 54.0% | 56.0% | 61.6% | 61.6% [60.7%-62.6%] | -- | 54.0% | 54.0% | MODEL_LONE_OUTLIER | PASS | +2.0 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Aleksandr Shevchenko (`KXATPMATCH-26NOV10MANSHE-SHE`) | 0.45 / 0.47 (12417) | 46.0% | 44.0% | 38.4% | 38.4% [37.4%-39.3%] | -- | 48.2% | -- | INSUFFICIENT_INPUTS | PASS | -2.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5623.0, B 5333.0; serve-point win A 65.8%, B 35.4%; Elo A 1797.4, B 1720.3; model uncertainty 0.0094
* Form inputs: days since last match A 1, B 7; matches on record A 1327, B 510; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.009, surface_dev_tight -0.004
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26NOV10MANSHE-2-MAN` Will Adrian Mannarino win set 2 in the Adrian Mannarino vs Alexander Shevchenko match: 0.01/0.98 mid 49.5%, model 54.0% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MANSHE-SHE20` Will Alexander Shevchenko win the Adrian Mannarino vs Alexander Shevchenko match by a set score of 2-0?: 0.02/0.49 mid 25.5%, model 21.1% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MANSHE-2-SHE` Will Alexander Shevchenko win set 2 in the Adrian Mannarino vs Alexander Shevchenko match: 0.01/0.98 mid 49.5%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap -3.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MANSHE-MAN20` Will Adrian Mannarino win the Adrian Mannarino vs Alexander Shevchenko match by a set score of 2-0?: 0.03/0.49 mid 26.0%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MANSHE-SHE21` Will Alexander Shevchenko win the Adrian Mannarino vs Alexander Shevchenko match by a set score of 2-1?: 0.02/0.49 mid 25.5%, model 22.8% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MANSHE-1-SHE` Will Alexander Shevchenko win set 1 in the Adrian Mannarino vs Alexander Shevchenko match: 0.46/0.50 mid 48.0%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MANSHE-MAN21` Will Adrian Mannarino win the Adrian Mannarino vs Alexander Shevchenko match by a set score of 2-1?: 0.02/0.49 mid 25.5%, model 26.8% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MANSHE-1-MAN` Will Adrian Mannarino win set 1 in the Adrian Mannarino vs Alexander Shevchenko match: 0.51/0.55 mid 53.0%, model 54.0% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alex Michelsen vs Juan Manuel Cerundolo -- ATP Stockholm R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-10 15:00Z
* Current expected start: 2026-11-10 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 18:39Z
* Recommended handicap-by time: 2026-11-10 11:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-10T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207678:210506:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel Cerundolo (`KXATPMATCH-26NOV10MICCER-CER`) | 0.25 / 0.26 (363) | 25.5% | 25.1% | 18.7% | 19.4% [17.5%-22.6%] | -- | 25.4% | -- | INSUFFICIENT_INPUTS | PASS | -0.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alex Michelsen (`KXATPMATCH-26NOV10MICCER-MIC`) | 0.73 / 0.75 (702) | 74.0% | 74.9% | 81.3% | 80.6% [77.5%-82.5%] | -- | 73.2% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +0.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5933.0, B 6143.0; serve-point win A 67.6%, B 37.8%; Elo A 1968.7, B 1749.8; model uncertainty 0.0251
* Form inputs: days since last match A 0, B 1; matches on record A 321, B 549; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.018, surface_dev_tight -0.027
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26NOV10MICCER-2-CER` Will Juan Manuel Cerundolo win set 2 in the Alex Michelsen vs Juan Manuel Cerundolo match: 0.05/0.96 mid 50.5%, model 32.7% (projection_v2.0 (prediction ledger)) -- gap -17.8 pp, HIGH_REVIEW, DATA_WARNING, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MICCER-2-MIC` Will Alex Michelsen win set 2 in the Alex Michelsen vs Juan Manuel Cerundolo match: 0.04/0.96 mid 50.0%, model 67.3% (projection_v2.0 (prediction ledger)) -- gap +17.3 pp, HIGH_REVIEW, DATA_WARNING, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MICCER-CER20` Will Juan Manuel Cerundolo win the Alex Michelsen vs Juan Manuel Cerundolo match by a set score of 2-0?: 0.13/0.31 mid 22.0%, model 10.7% (projection_v2.0 (prediction ledger)) -- gap -11.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MICCER-MIC20` Will Alex Michelsen win the Alex Michelsen vs Juan Manuel Cerundolo match by a set score of 2-0?: 0.45/0.64 mid 54.5%, model 45.2% (projection_v2.0 (prediction ledger)) -- gap -9.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10MICCER-MIC7` Will Alex Michelsen win at least 6.5 more games than Juan Manuel Cerundolo?: 0.12/0.25 mid 18.5%, model 9.4% (projection_v2.0 (prediction ledger)) -- gap -9.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV10MICCER-23` Over 22.5 games: 0.46/0.49 mid 47.5%, model 55.9% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MICCER-CER21` Will Juan Manuel Cerundolo win the Alex Michelsen vs Juan Manuel Cerundolo match by a set score of 2-1?: 0.11/0.30 mid 20.5%, model 14.4% (projection_v2.0 (prediction ledger)) -- gap -6.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV10MICCER-28` Over 27.5 games: 0.25/0.37 mid 31.0%, model 36.4% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10MICCER-MIC4` Will Alex Michelsen win at least 3.5 more games than Juan Manuel Cerundolo?: 0.51/0.54 mid 52.5%, model 47.7% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV10MICCER-18` Over 17.5 games: 0.81/0.93 mid 87.0%, model 91.7% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10MICCER-CER2` Will Juan Manuel Cerundolo win at least 1.5 more games than Alex Michelsen?: 0.14/0.27 mid 20.5%, model 19.3% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MICCER-1-MIC` Will Alex Michelsen win set 1 in the Alex Michelsen vs Juan Manuel Cerundolo match: 0.66/0.70 mid 68.0%, model 67.3% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MICCER-MIC21` Will Alex Michelsen win the Alex Michelsen vs Juan Manuel Cerundolo match by a set score of 2-1?: 0.20/0.40 mid 30.0%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MICCER-1-CER` Will Juan Manuel Cerundolo win set 1 in the Alex Michelsen vs Juan Manuel Cerundolo match: 0.31/0.34 mid 32.5%, model 32.7% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hong / Ju Kim vs Sun / Wang -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10HONJUKSUNWAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hong / Ju Kim (`KXITFDOUBLES-26NOV10HONJUKSUNWAN-HONJUK`) | 0.07 / 0.90 (1) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sun / Wang (`KXITFDOUBLES-26NOV10HONJUKSUNWAN-SUNWAN`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Vishenchuk Vishenko / Zhukov vs Connel / Hongyu -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10VISZHUCONHON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Connel / Hongyu (`KXITFDOUBLES-26NOV10VISZHUCONHON-CONHON`) | 0.66 / 0.87 (3) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vishenchuk Vishenko / Zhukov (`KXITFDOUBLES-26NOV10VISZHUCONHON-VISZHU`) | 0.22 / 0.81 (3) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Artjoms Afanasjevs vs Vito Dell'elba -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10AFADEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Artjoms Afanasjevs (`KXITFMATCH-26NOV10AFADEL-AFA`) | 0.09 / 0.15 (3) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vito Dell'elba (`KXITFMATCH-26NOV10AFADEL-DEL`) | 0.83 / 0.92 (2) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alessio Basile vs Daniil Stepanov -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211450:213905:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessio Basile (`KXITFMATCH-26NOV10BASSTE-BAS`) | 0.83 / 0.94 (35) | 88.5% | 73.2% | 74.5% | 64.4% [60.2%-69.7%] | -- | -- | -- | -- | PASS | -15.3 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniil Stepanov (`KXITFMATCH-26NOV10BASSTE-STE`) | 0.05 / 0.14 (29) | 9.5% | 26.8% | 25.5% | 35.6% [30.3%-39.8%] | -- | -- | -- | -- | PASS | +17.3 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 952.0, B 210.0; serve-point win A 59.7%, B 45.0%; Elo A 1252.5, B 1158.9; model uncertainty 0.0473
* Form inputs: days since last match A 350, B 196; matches on record A 43, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10BASSTE-STE  (YES = Daniil Stepanov)
Model: 27%
Kalshi: 10%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.029, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alessandro Bellifemine vs Patrick Jozwicki -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210110:213168:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessandro Bellifemine (`KXITFMATCH-26NOV10BELJOZ-BEL`) | 0.62 / 0.87 (18) | 74.5% | 70.0% | 32.0% | 46.8% [45.7%-48.9%] | -- | -- | -- | -- | PASS | -4.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Patrick Jozwicki (`KXITFMATCH-26NOV10BELJOZ-JOZ`) | 0.26 / 0.50 (3) | 38.0% | 30.0% | 68.0% | 53.2% [51.0%-54.3%] | -- | -- | -- | -- | PASS | -8.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 859.0, B 172.0; serve-point win A 56.1%, B 47.8%; Elo A 1176.5, B 1183.9; model uncertainty 0.016
* Form inputs: days since last match A 336, B 231; matches on record A 65, B 6; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.011, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dai / Han vs Dong / Yang -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10DAIHANDONYAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dai / Han (`KXITFDOUBLES-26NOV10DAIHANDONYAN-DAIHAN`) | 0.06 / 0.89 (56) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dong / Yang (`KXITFDOUBLES-26NOV10DAIHANDONYAN-DONYAN`) | 0.07 / 0.90 (43) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Amine Jamji vs Andrea Paolini -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212900:213026:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amine Jamji (`KXITFMATCH-26NOV10JAMPAO-JAM`) | 0.33 / 0.43 (43) | 38.0% | 59.8% | 39.1% | 48.9% [46.3%-52.1%] | -- | -- | -- | -- | PASS | +21.8 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andrea Paolini (`KXITFMATCH-26NOV10JAMPAO-PAO`) | 0.52 / 0.74 (23) | 63.0% | 40.2% | 60.9% | 51.0% [47.9%-53.7%] | -- | -- | -- | -- | PASS | -22.8 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 659.0, B 516.0; serve-point win A 57.9%, B 44.0%; Elo A 1224.0, B 1208.3; model uncertainty 0.0289
* Form inputs: days since last match A 50, B 266; matches on record A 15, B 31; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10JAMPAO-JAM  (YES = Amine Jamji)
Model: 60%
Kalshi: 38%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.011, surface_dev_loose -0.016, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vuk Radjenovic vs Felix Romeo -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207590:211366:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vuk Radjenovic (`KXITFMATCH-26NOV10RADROM-RAD`) | 0.47 / 0.66 (1) | 56.5% | 61.9% | 32.7% | 53.1% [53.1%-53.1%] | -- | -- | -- | -- | PASS | +5.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Felix Romeo (`KXITFMATCH-26NOV10RADROM-ROM`) | 0.41 / 0.44 (44) | 42.5% | 38.1% | 67.3% | 46.9% [46.9%-46.9%] | -- | -- | -- | -- | PASS | -4.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 799.0, B 0.0; serve-point win A 62.2%, B 40.2%; Elo A 1242.8, B 1223.7; model uncertainty 0.0001
* Form inputs: days since last match A 371, B 875; matches on record A 71, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Heorhii Shylov vs Gokberk Saritas -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10SHYSAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gokberk Saritas (`KXITFMATCH-26NOV10SHYSAR-SAR`) | 0.07 / 0.16 (52) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Heorhii Shylov (`KXITFMATCH-26NOV10SHYSAR-SHY`) | 0.83 / 0.95 (308) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Evgenii Tiurnev vs Aleksa Oparnica -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126185:213939:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksa Oparnica (`KXITFMATCH-26NOV10TIUOPA-OPA`) | 0.11 / 0.36 (39) | 23.5% | 14.6% | 18.8% | 19.5% [17.5%-22.3%] | -- | -- | -- | -- | PASS | -8.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Evgenii Tiurnev (`KXITFMATCH-26NOV10TIUOPA-TIU`) | 0.76 / 0.82 (138) | 79.0% | 85.4% | 81.2% | 80.5% [77.7%-82.5%] | -- | -- | -- | -- | PASS | +6.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1478.0, B 70.0; serve-point win A 69.7%, B 38.9%; Elo A 1505.2, B 1263.3; model uncertainty 0.0243
* Form inputs: days since last match A 231, B 504; matches on record A 579, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.028, surface_dev_loose -0.001, surface_dev_tight -0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexander Wagner vs Cezar Stefan Bentzel -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213138:213855:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cezar Stefan Bentzel (`KXITFMATCH-26NOV10WAGBEN-BEN`) | 0.24 / 0.42 (43) | 33.0% | 33.5% | 45.2% | 41.0% [40.0%-41.6%] | -- | -- | -- | -- | PASS | +0.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Wagner (`KXITFMATCH-26NOV10WAGBEN-WAG`) | 0.62 / 0.76 (45) | 69.0% | 66.5% | 54.8% | 59.0% [58.4%-60.0%] | -- | -- | -- | -- | PASS | -2.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 861.0, B 390.0; serve-point win A 56.7%, B 46.6%; Elo A 1196.5, B 1125.9; model uncertainty 0.0079
* Form inputs: days since last match A 196, B 336; matches on record A 22, B 6; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cao / Tikhonova vs Chen / Li -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10CAOTIKCHELIX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cao / Tikhonova (`KXITFWDOUBLES-26NOV10CAOTIKCHELIX-CAOTIK`) | 0.55 / 0.80 (125) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chen / Li (`KXITFWDOUBLES-26NOV10CAOTIKCHELIX-CHELIX`) | 0.13 / 0.38 (40) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Hou / Plipuech vs Yu / Zhou -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10HOUPLIYUXZHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hou / Plipuech (`KXITFWDOUBLES-26NOV10HOUPLIYUXZHO-HOUPLI`) | 0.06 / 0.89 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yu / Zhou (`KXITFWDOUBLES-26NOV10HOUPLIYUXZHO-YUXZHO`) | 0.07 / 0.90 (1) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Luca Van Assche vs Alexander Shevchenko -- ATP Stockholm 1/16 F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-10 13:00Z
* Current expected start: 2026-11-10 13:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-11-10 12:15Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source)

ATP (TOUR_500_250) · Hard · scheduled 2026-11-10T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207686:209414:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Shevchenko (`KXATPMATCH-26NOV10VANASHE-SHE`) | 0.40 / 0.42 (12) | 41.0% | 34.7% | 27.4% | 29.1% [28.3%-30.3%] | 43.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luca Van Assche (`KXATPMATCH-26NOV10VANASHE-VANA`) | 0.57 / 0.63 (10) | 60.0% | 65.3% | 72.6% | 70.9% [69.7%-71.7%] | 56.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6340.0, B 5333.0; serve-point win A 65.3%, B 37.9%; Elo A 1835.8, B 1720.3; model uncertainty 0.0098
* Form inputs: days since last match A 2, B 7; matches on record A 399, B 510; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose +0.007, surface_dev_tight -0.012
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV10VANASHE-18` Over 17.5 games: 0.01/0.93 mid 47.0%, model 92.6% (projection_v2.0 (prediction ledger)) -- gap +45.6 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV10VANASHE-23` Over 22.5 games: 0.01/0.94 mid 47.5%, model 59.0% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10VANASHE-VANA2` Will Luca Van Assche win at least 1.5 more games than Alexander Shevchenko?: 0.01/0.93 mid 47.0%, model 58.1% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10VANASHE-1-VANA` Will Luca Van Assche win set 1 in the Luca Van Assche vs Alexander Shevchenko match: 0.02/0.97 mid 49.5%, model 60.4% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV10VANASHE-2-VANA` Will Luca Van Assche win set 2 in the Luca Van Assche vs Alexander Shevchenko match: 0.02/0.97 mid 49.5%, model 60.4% (projection_v2.0 (prediction ledger)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10VANASHE-VANA20` Will Luca Van Assche win the Luca Van Assche vs Alexander Shevchenko match by a set score of 2-0?: 0.10/0.42 mid 26.0%, model 36.4% (projection_v2.0 (prediction ledger)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10VANASHE-1-SHE` Will Alexander Shevchenko win set 1 in the Luca Van Assche vs Alexander Shevchenko match: 0.02/0.97 mid 49.5%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV10VANASHE-2-SHE` Will Alexander Shevchenko win set 2 in the Luca Van Assche vs Alexander Shevchenko match: 0.02/0.97 mid 49.5%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV10VANASHE-28` Over 27.5 games: 0.01/0.94 mid 47.5%, model 38.9% (projection_v2.0 (prediction ledger)) -- gap -8.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ruben Hartig vs Victor Ryden -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212270:213910:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ruben Hartig (`KXITFMATCH-26NOV10HARRYD-HAR`) | 0.31 / 0.50 (4) | 40.5% | 31.8% | 56.3% | 34.7% [33.0%-35.5%] | -- | -- | -- | -- | PASS | -8.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Victor Ryden (`KXITFMATCH-26NOV10HARRYD-RYD`) | 0.43 / 0.63 (68) | 53.0% | 68.2% | 43.7% | 65.3% [64.5%-67.0%] | -- | -- | -- | -- | PASS | +15.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 109.0, B 67.0; serve-point win A 55.8%, B 40.6%; Elo A 1120.1, B 1237.4; model uncertainty 0.0129
* Form inputs: days since last match A 196, B 378; matches on record A 14, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10HARRYD-RYD  (YES = Victor Ryden)
Model: 68%
Kalshi: 53%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Huang / Lu vs Benaim / Brown -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10HUALUXBENBRO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benaim / Brown (`KXITFDOUBLES-26NOV10HUALUXBENBRO-BENBRO`) | 0.17 / 0.41 (42) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Huang / Lu (`KXITFDOUBLES-26NOV10HUALUXBENBRO-HUALUX`) | 0.51 / 0.78 (113) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Alex Jones vs Joseph Roboly -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10JONROB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Jones (`KXITFMATCH-26NOV10JONROB-JON`) | 0.93 / 0.95 (275) | 94.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Joseph Roboly (`KXITFMATCH-26NOV10JONROB-ROB`) | 0.05 / 0.07 (452) | 6.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thando Longwe-Smit vs Panagiotis-Gerasimos Grammatikakis -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10LONGRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Panagiotis-Gerasimos Grammatikakis (`KXITFMATCH-26NOV10LONGRA-GRA`) | 0.06 / 0.11 (22) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thando Longwe-Smit (`KXITFMATCH-26NOV10LONGRA-LON`) | 0.86 / 0.93 (8) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Masabayashi / Suksumrarn vs Koaykul / Navasirisomboon -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10MASSUKKOANAV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Koaykul / Navasirisomboon (`KXITFDOUBLES-26NOV10MASSUKKOANAV-KOANAV`) | 0.12 / 0.21 (31) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Masabayashi / Suksumrarn (`KXITFDOUBLES-26NOV10MASSUKKOANAV-MASSUK`) | 0.74 / 0.90 (1) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jean-Julien Rojer / Theodore Winegar vs William Rejchtman Vinciguerra / Olle Wallin -- ATP Stockholm 1/8 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-09 18:39Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-11T05:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ROJWINREJWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| William Rejchtman Vinciguerra / Olle Wallin (`KXATPDOUBLES-26NOV10ROJWINREJWAL-REJWAL`) | 0.06 / 0.19 (27) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jean-Julien Rojer / Theodore Winegar (`KXATPDOUBLES-26NOV10ROJWINREJWAL-ROJWIN`) | 0.81 / 0.94 (2) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sukjai / Sukjai vs Bunyarit / Kamput -- M15 Hua Hin R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10SUKSUKBUNKAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bunyarit / Kamput (`KXITFDOUBLES-26NOV10SUKSUKBUNKAM-BUNKAM`) | 0.07 / 0.90 (1) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sukjai / Sukjai (`KXITFDOUBLES-26NOV10SUKSUKBUNKAM-SUKSUK`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mac Visser vs Maximilian Alessandro Erhardt -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213829:213983:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maximilian Alessandro Erhardt (`KXITFMATCH-26NOV10VISERH-ERH`) | 0.32 / 0.37 (40) | 34.5% | 40.5% | 54.7% | 47.9% [47.9%-48.9%] | -- | -- | -- | -- | PASS | +6.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mac Visser (`KXITFMATCH-26NOV10VISERH-VIS`) | 0.58 / 0.78 (3) | 68.0% | 59.5% | 45.3% | 52.1% [51.0%-52.1%] | -- | -- | -- | -- | PASS | -8.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 752.0, B 70.0; serve-point win A 58.3%, B 43.5%; Elo A 1295.9, B 1283.4; model uncertainty 0.0053
* Form inputs: days since last match A 156, B 483; matches on record A 16, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Felitsata Dorofeeva-Rybas vs Eliska Tichackova -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:254748:267022:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felitsata Dorofeeva-Rybas (`KXITFWMATCH-26NOV10DORTIC-DOR`) | 0.47 / 0.58 (41) | 52.5% | 15.4% | 15.1% | 21.8% [19.5%-25.6%] | -- | -- | -- | -- | PASS | -37.1 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eliska Tichackova (`KXITFWMATCH-26NOV10DORTIC-TIC`) | 0.43 / 0.46 (14) | 44.5% | 84.6% | 84.9% | 78.2% [74.4%-80.5%] | -- | -- | -- | -- | PASS | +40.1 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 923.0, B 1647.0; serve-point win A 47.5%, B 44.9%; Elo A 1447.6, B 1623.6; model uncertainty 0.0303
* Form inputs: days since last match A 343, B 259; matches on record A 19, B 46; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10DORTIC-TIC  (YES = Eliska Tichackova)
Model: 85%
Kalshi: 44%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.016, surface_dev_loose -0.012, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marta Lombardini vs Sonja Zhenikhova -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264961:267409:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marta Lombardini (`KXITFWMATCH-26NOV10LOMZHE-LOM`) | 0.59 / 0.71 (87) | 65.0% | 64.8% | 66.1% | 61.6% [57.4%-64.1%] | -- | -- | -- | -- | PASS | -0.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sonja Zhenikhova (`KXITFWMATCH-26NOV10LOMZHE-ZHE`) | 0.27 / 0.36 (39) | 31.5% | 35.2% | 33.9% | 38.4% [35.9%-42.6%] | -- | -- | -- | -- | PASS | +3.7 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 984.0, B 1212.0; serve-point win A 53.9%, B 49.0%; Elo A 1447.1, B 1388.4; model uncertainty 0.0335
* Form inputs: days since last match A 47, B 259; matches on record A 25, B 38; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giulia Safina Popa vs Cristiana Nicoleta Todoni -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:261104:267428:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giulia Safina Popa (`KXITFWMATCH-26NOV10POPTOD-POP`) | 0.57 / 0.67 (54) | 62.0% | 82.8% | 63.1% | 72.6% [70.4%-77.3%] | -- | -- | -- | -- | PASS | +20.8 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cristiana Nicoleta Todoni (`KXITFWMATCH-26NOV10POPTOD-TOD`) | 0.29 / 0.38 (53) | 33.5% | 17.2% | 36.9% | 27.4% [22.7%-29.6%] | -- | -- | -- | -- | PASS | -16.3 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1013.0, B 865.0; serve-point win A 57.2%, B 49.9%; Elo A 1526.2, B 1304.5; model uncertainty 0.0345
* Form inputs: days since last match A 406, B 120; matches on record A 38, B 57; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10POPTOD-POP  (YES = Giulia Safina Popa)
Model: 83%
Kalshi: 62%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.000, surface_dev_loose -0.013, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Shapatava vs Teodora Miron -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202410:270171:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Teodora Miron (`KXITFWMATCH-26NOV10SHAMIR-MIR`) | 0.51 / 0.68 (79) | 59.5% | 16.7% | 31.1% | 28.7% [24.4%-32.5%] | -- | -- | -- | -- | PASS | -42.8 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofia Shapatava (`KXITFWMATCH-26NOV10SHAMIR-SHA`) | 0.34 / 0.52 (2) | 43.0% | 83.3% | 68.9% | 71.3% [67.5%-75.6%] | -- | -- | -- | -- | PASS | +40.3 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2642.0, B 136.0; serve-point win A 57.8%, B 49.5%; Elo A 1479.8, B 1320.1; model uncertainty 0.0404
* Form inputs: days since last match A 196, B 476; matches on record A 1029, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10SHAMIR-SHA  (YES = Sofia Shapatava)
Model: 83%
Kalshi: 43%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.035, surface_pool_high -0.037, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sun / Zhao vs Li / Zhang -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10SUNZHALIXZHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Li / Zhang (`KXITFWDOUBLES-26NOV10SUNZHALIXZHA-LIXZHA`) | 0.18 / 0.39 (45) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sun / Zhao (`KXITFWDOUBLES-26NOV10SUNZHALIXZHA-SUNZHA`) | 0.55 / 0.79 (5) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lorenzo Sonego vs Quentin Halys -- ATP Stockholm 1/16 F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-10 13:00Z
* Current expected start: 2026-11-10 13:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 18:39Z
* Recommended handicap-by time: 2026-11-10 12:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+30_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-10T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111460:132283:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Quentin Halys (`KXATPMATCH-26NOV10SONHAL-HAL`) | 0.54 / 0.56 (16444) | 55.0% | 57.7% | 60.6% | 60.6% [59.7%-60.7%] | -- | 54.8% | 54.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +2.7 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Lorenzo Sonego (`KXATPMATCH-26NOV10SONHAL-SON`) | 0.45 / 0.46 (15685) | 45.5% | 42.3% | 39.4% | 39.4% [39.3%-40.3%] | -- | 45.5% | 45.5% | MODEL_LONE_OUTLIER | PASS | -3.2 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4585.0, B 6418.0; serve-point win A 68.6%, B 29.7%; Elo A 1779.2, B 1843.7; model uncertainty 0.0048
* Form inputs: days since last match A 1, B 4; matches on record A 706, B 843; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV10SONHAL-30` Over 29.5 games: 0.27/0.37 mid 32.0%, model 40.0% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10SONHAL-HAL5` Will Quentin Halys win at least 4.5 more games than Lorenzo Sonego?: 0.15/0.26 mid 20.5%, model 12.8% (projection_v2.0 (prediction ledger)) -- gap -7.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10SONHAL-HAL21` Will Quentin Halys win the Lorenzo Sonego vs Quentin Halys match by a set score of 2-1?: 0.14/0.26 mid 20.0%, model 27.3% (projection_v2.0 (prediction ledger)) -- gap +7.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV10SONHAL-25` Over 24.5 games: 0.51/0.54 mid 52.5%, model 58.9% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV10SONHAL-20` Over 19.5 games: 0.80/0.86 mid 83.0%, model 89.0% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10SONHAL-SON20` Will Lorenzo Sonego win the Lorenzo Sonego vs Quentin Halys match by a set score of 2-0?: 0.24/0.26 mid 25.0%, model 20.1% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10SONHAL-2-SON` Will Lorenzo Sonego win set 2 in the Lorenzo Sonego vs Quentin Halys match: 0.02/0.97 mid 49.5%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV10SONHAL-SON2` Will Lorenzo Sonego win at least 1.5 more games than Quentin Halys?: 0.35/0.41 mid 38.0%, model 33.6% (projection_v2.0 (prediction ledger)) -- gap -4.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10SONHAL-SON21` Will Lorenzo Sonego win the Lorenzo Sonego vs Quentin Halys match by a set score of 2-1?: 0.16/0.20 mid 18.0%, model 22.2% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10SONHAL-2-HAL` Will Quentin Halys win set 2 in the Lorenzo Sonego vs Quentin Halys match: 0.05/0.97 mid 51.0%, model 55.2% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV10SONHAL-1-SON` Will Lorenzo Sonego win set 1 in the Lorenzo Sonego vs Quentin Halys match: 0.47/0.49 mid 48.0%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV10SONHAL-1-HAL` Will Quentin Halys win set 1 in the Lorenzo Sonego vs Quentin Halys match: 0.51/0.54 mid 52.5%, model 55.2% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV10SONHAL-HAL2` Will Quentin Halys win at least 1.5 more games than Lorenzo Sonego?: 0.46/0.48 mid 47.0%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10SONHAL-HAL20` Will Quentin Halys win the Lorenzo Sonego vs Quentin Halys match by a set score of 2-0?: 0.30/0.33 mid 31.5%, model 30.4% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ekaterina Agureeva vs Klara Vaja -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:265036:266852:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Agureeva (`KXITFWMATCH-26NOV10AGUVAJ-AGU`) | 0.83 / 0.93 (3) | 88.0% | 84.8% | 66.1% | 77.3% [75.6%-79.6%] | -- | -- | -- | -- | PASS | -3.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Klara Vaja (`KXITFWMATCH-26NOV10AGUVAJ-VAJ`) | 0.05 / 0.24 (41) | 14.5% | 15.2% | 33.9% | 22.7% [20.4%-24.4%] | -- | -- | -- | -- | PASS | +0.7 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 144.0, B 157.0; serve-point win A 57.9%, B 49.8%; Elo A 1386.4, B 1165.5; model uncertainty 0.0199
* Form inputs: days since last match A 434, B 343; matches on record A 17, B 33; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.016, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mariia Drobysheva vs Federica Bilardo -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214746:261061:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federica Bilardo (`KXITFWMATCH-26NOV10DROBIL-BIL`) | 0.39 / 0.77 (3) | 58.0% | 90.4% | 51.6% | 77.3% [72.6%-83.8%] | -- | -- | -- | -- | PASS | +32.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mariia Drobysheva (`KXITFWMATCH-26NOV10DROBIL-DRO`) | 0.42 / 0.78 (5) | 60.0% | 9.6% | 48.4% | 22.7% [16.2%-27.4%] | -- | -- | -- | -- | PASS | -50.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 310.0, B 471.0; serve-point win A 49.1%, B 41.1%; Elo A 1283.7, B 1546.8; model uncertainty 0.0561
* Form inputs: days since last match A 406, B 203; matches on record A 7, B 327; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10DROBIL-BIL  (YES = Federica Bilardo)
Model: 90%
Kalshi: 58%
Gap: +32 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.031, surface_pool_high +0.016, surface_dev_loose -0.008, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andreya Glushkova vs Stefanie Auer -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222558:267887:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefanie Auer (`KXITFWMATCH-26NOV10GLUAUE-AUE`) | 0.58 / 0.93 (6) | 75.5% | 82.7% | 22.2% | 60.6% [56.4%-64.6%] | -- | -- | -- | -- | PASS | +7.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andreya Glushkova (`KXITFWMATCH-26NOV10GLUAUE-GLU`) | 0.24 / 0.49 (50) | 36.5% | 17.3% | 77.8% | 39.4% [35.4%-43.6%] | -- | -- | -- | -- | PASS | -19.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 453.0; serve-point win A 49.1%, B 43.9%; Elo A 1152.5, B 1225.8; model uncertainty 0.0413
* Form inputs: days since last match A 707, B 308; matches on record A 4, B 171; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.042, surface_pool_high -0.041, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victoria Gomez O'Hayon vs Karina Maria Capuzu -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10GOMCAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karina Maria Capuzu (`KXITFWMATCH-26NOV10GOMCAP-CAP`) | 0.14 / 0.18 (31) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victoria Gomez O'Hayon (`KXITFWMATCH-26NOV10GOMCAP-GOM`) | 0.77 / 0.95 (1) | 86.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ksenia Meshcheryakova vs Alisa Ziatdinova -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222554:270317:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ksenia Meshcheryakova (`KXITFWMATCH-26NOV10MESZIA-MES`) | 0.04 / 0.96 (156) | 50.0% | 10.6% | 36.4% | 17.5% [15.5%-18.9%] | -- | -- | -- | -- | PASS | -39.4 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alisa Ziatdinova (`KXITFWMATCH-26NOV10MESZIA-ZIA`) | 0.05 / 0.96 (134) | 50.5% | 89.4% | 63.6% | 82.5% [81.1%-84.5%] | -- | -- | -- | -- | PASS | +38.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 335.0, B 165.0; serve-point win A 48.9%, B 41.8%; Elo A 980.4, B 1269.4; model uncertainty 0.0168
* Form inputs: days since last match A 196, B 350; matches on record A 75, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10MESZIA-ZIA  (YES = Alisa Ziatdinova)
Model: 89%
Kalshi: 50%
Gap: +39 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.007, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofiia Suslova vs Maria Shmeleva -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:252582:270324:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Shmeleva (`KXITFWMATCH-26NOV10SUSSHM-SHM`) | 0.04 / 0.96 (156) | 50.0% | 51.0% | 62.1% | 55.9% [55.3%-56.9%] | -- | -- | -- | -- | PASS | +1.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofiia Suslova (`KXITFWMATCH-26NOV10SUSSHM-SUS`) | 0.05 / 0.96 (134) | 50.5% | 49.0% | 37.9% | 44.1% [43.1%-44.7%] | -- | -- | -- | -- | PASS | -1.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 719.0, B 189.0; serve-point win A 51.1%, B 48.7%; Elo A 1288.2, B 1321.9; model uncertainty 0.008
* Form inputs: days since last match A 252, B 371; matches on record A 38, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentina Suvirdjonkova vs Polina Starkova -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:265035:270316:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Starkova (`KXITFWMATCH-26NOV10SUVSTA-STA`) | 0.05 / 0.96 (156) | 50.5% | 71.3% | 66.1% | 60.6% [60.6%-62.7%] | -- | -- | -- | -- | PASS | +20.8 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentina Suvirdjonkova (`KXITFWMATCH-26NOV10SUVSTA-SUV`) | 0.04 / 0.96 (134) | 50.0% | 28.7% | 33.9% | 39.4% [37.3%-39.5%] | -- | -- | -- | -- | PASS | -21.3 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 121.0, B 184.0; serve-point win A 49.5%, B 46.3%; Elo A 1217.0, B 1289.7; model uncertainty 0.0105
* Form inputs: days since last match A 308, B 301; matches on record A 5, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10SUVSTA-STA  (YES = Polina Starkova)
Model: 71%
Kalshi: 50%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.010, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Doga Turkmen vs Daniela Darta Feldmane -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220356:260159:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniela Darta Feldmane (`KXITFWMATCH-26NOV10TURFEL-FEL`) | 0.29 / 0.48 (7) | 38.5% | 44.7% | 58.5% | 45.2% [41.5%-48.4%] | -- | -- | -- | -- | PASS | +6.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Doga Turkmen (`KXITFWMATCH-26NOV10TURFEL-TUR`) | 0.58 / 0.73 (100) | 65.5% | 55.3% | 41.5% | 54.8% [51.6%-58.5%] | -- | -- | -- | -- | PASS | -10.2 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 739.0, B 630.0; serve-point win A 50.9%, B 50.1%; Elo A 1294.0, B 1221.8; model uncertainty 0.0345
* Form inputs: days since last match A 36, B 301; matches on record A 260, B 20; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mu Jie Tzeng vs Chrystal Lopez -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10TZELOP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chrystal Lopez (`KXITFWMATCH-26NOV10TZELOP-LOP`) | 0.08 / 0.77 (3) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mu Jie Tzeng (`KXITFWMATCH-26NOV10TZELOP-TZE`) | 0.78 / 0.93 (3) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Denise Valente vs Mariya Yemshanova -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223416:270167:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Denise Valente (`KXITFWMATCH-26NOV10VALYEM-VAL`) | 0.83 / 0.96 (156) | 89.5% | 75.4% | 32.9% | 58.5% [57.4%-59.5%] | -- | -- | -- | -- | PASS | -14.1 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mariya Yemshanova (`KXITFWMATCH-26NOV10VALYEM-YEM`) | 0.05 / 0.24 (50) | 14.5% | 24.6% | 67.1% | 41.5% [40.5%-42.6%] | -- | -- | -- | -- | PASS | +10.1 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1031.0, B 91.0; serve-point win A 55.6%, B 49.6%; Elo A 1297.3, B 1224.9; model uncertainty 0.0105
* Form inputs: days since last match A 203, B 196; matches on record A 157, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Angelina Wirges vs Anais Gabriel -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220493:221155:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anais Gabriel (`KXITFWMATCH-26NOV10WIRGAB-GAB`) | 0.39 / 0.61 (3) | 50.0% | 20.2% | 30.9% | 26.8% [24.3%-28.2%] | -- | -- | -- | -- | PASS | -29.9 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Angelina Wirges (`KXITFWMATCH-26NOV10WIRGAB-WIR`) | 0.48 / 0.56 (56) | 52.0% | 79.8% | 69.1% | 73.2% [71.8%-75.7%] | -- | -- | -- | -- | PASS | +27.9 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1745.0, B 534.0; serve-point win A 53.2%, B 53.0%; Elo A 1408.6, B 1217.3; model uncertainty 0.0194
* Form inputs: days since last match A 203, B 245; matches on record A 257, B 13; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10WIRGAB-WIR  (YES = Angelina Wirges)
Model: 80%
Kalshi: 52%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.022, surface_pool_high -0.013, surface_dev_loose +0.009, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## yasaman yazdani vs Theresa Stabauer -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10YAZSTA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theresa Stabauer (`KXITFWMATCH-26NOV10YAZSTA-STA`) | 0.63 / 0.88 (4) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| yasaman yazdani (`KXITFWMATCH-26NOV10YAZSTA-YAZ`) | 0.24 / 0.66 (3) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arian Barbic vs Phil Dungs -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:214211:214221:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arian Barbic (`KXITFMATCH-26NOV10BARDUN-BAR`) | 0.45 / 0.80 (3) | 62.5% | 55.2% | 59.4% | 51.0% [51.0%-52.0%] | -- | -- | -- | -- | PASS | -7.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Phil Dungs (`KXITFMATCH-26NOV10BARDUN-DUN`) | 0.39 / 0.80 (114) | 59.5% | 44.8% | 40.6% | 49.0% [48.0%-49.0%] | -- | -- | -- | -- | PASS | -14.7 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 155.0, B 38.0; serve-point win A 64.0%, B 37.1%; Elo A 1289.6, B 1282.2; model uncertainty 0.0049
* Form inputs: days since last match A 301, B 378; matches on record A 3, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## John Bothma vs Jan Kluczynski -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BOTKLU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| John Bothma (`KXITFMATCH-26NOV10BOTKLU-BOT`) | 0.80 / 0.95 (305) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jan Kluczynski (`KXITFMATCH-26NOV10BOTKLU-KLU`) | 0.08 / 0.83 (8) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martin Hammond vs Mathys Braun -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10HAMBRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mathys Braun (`KXITFMATCH-26NOV10HAMBRA-BRA`) | 0.06 / 0.94 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Martin Hammond (`KXITFMATCH-26NOV10HAMBRA-HAM`) | 0.07 / 0.94 (56) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jack Karlsson Wistrand vs Ollie Knight -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10KARKNI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Karlsson Wistrand (`KXITFMATCH-26NOV10KARKNI-KAR`) | 0.07 / 0.94 (56) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ollie Knight (`KXITFMATCH-26NOV10KARKNI-KNI`) | 0.06 / 0.94 (56) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dorian Kos vs Matyas Kozlovsky -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210057:214076:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dorian Kos (`KXITFMATCH-26NOV10KOSKOZ-KOS`) | 0.06 / 0.11 (22) | 8.5% | 50.8% | 65.9% | 52.1% [51.0%-52.1%] | -- | -- | -- | -- | PASS | +42.3 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Matyas Kozlovsky (`KXITFMATCH-26NOV10KOSKOZ-KOZ`) | 0.86 / 0.93 (27) | 89.5% | 49.2% | 34.1% | 47.9% [47.9%-48.9%] | -- | -- | -- | -- | PASS | -40.3 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 172.0; serve-point win A 56.9%, B 43.2%; Elo A 1285.0, B 1273.5; model uncertainty 0.0053
* Form inputs: days since last match A 2002, B 210; matches on record A 1, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10KOSKOZ-KOS  (YES = Dorian Kos)
Model: 51%
Kalshi: 8%
Gap: +42 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.011, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ramazan Kaan Oktay vs Brian Dal Zilio -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213958:214457:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brian Dal Zilio (`KXITFMATCH-26NOV10OKTDAL-DAL`) | 0.10 / 0.92 (100) | 51.0% | 32.2% | 46.3% | 41.7% [40.6%-41.7%] | -- | -- | -- | -- | PASS | -18.8 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ramazan Kaan Oktay (`KXITFMATCH-26NOV10OKTDAL-OKT`) | 0.79 / 0.94 (36) | 86.5% | 67.8% | 53.7% | 58.3% [58.3%-59.4%] | -- | -- | -- | -- | PASS | -18.7 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 266.0, B 181.0; serve-point win A 59.3%, B 44.2%; Elo A 1249.0, B 1183.2; model uncertainty 0.0058
* Form inputs: days since last match A 259, B 196; matches on record A 6, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gilberto Ravasio vs Lars Wagenaar -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212735:213923:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gilberto Ravasio (`KXITFMATCH-26NOV10RAVWAG-RAV`) | 0.57 / 0.80 (3) | 68.5% | 47.2% | 18.4% | 50.0% [48.4%-52.1%] | -- | -- | -- | -- | PASS | -21.3 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lars Wagenaar (`KXITFMATCH-26NOV10RAVWAG-WAG`) | 0.31 / 0.35 (38) | 33.0% | 52.8% | 81.6% | 50.0% [47.9%-51.6%] | -- | -- | -- | -- | PASS | +19.8 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 633.0, B 53.0; serve-point win A 55.5%, B 44.0%; Elo A 1182.8, B 1174.6; model uncertainty 0.0184
* Form inputs: days since last match A 196, B 448; matches on record A 16, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10RAVWAG-WAG  (YES = Lars Wagenaar)
Model: 53%
Kalshi: 33%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dominique Rolland vs Georgios Dimitriou -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ROLDIM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Georgios Dimitriou (`KXITFMATCH-26NOV10ROLDIM-DIM`) | 0.07 / 0.92 (3) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dominique Rolland (`KXITFMATCH-26NOV10ROLDIM-ROL`) | 0.84 / 0.95 (283) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Frederic Schlossmann vs Louis Herman -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206905:211612:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Louis Herman (`KXITFMATCH-26NOV10SCHHER-HER`) | 0.44 / 0.91 (114) | 67.5% | 48.2% | 15.3% | 50.0% [49.0%-52.1%] | -- | -- | -- | -- | PASS | -19.2 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Frederic Schlossmann (`KXITFMATCH-26NOV10SCHHER-SCH`) | 0.42 / 0.63 (1) | 52.5% | 51.7% | 84.7% | 50.0% [47.9%-51.0%] | -- | -- | -- | -- | PASS | -0.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 761.0; serve-point win A 59.8%, B 40.5%; Elo A 1178.2, B 1181.9; model uncertainty 0.0155
* Form inputs: days since last match A 1050, B 273; matches on record A 4, B 38; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.021, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Louis Van Herck vs Yahor Slizevich -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10VANSLI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yahor Slizevich (`KXITFMATCH-26NOV10VANSLI-SLI`) | 0.16 / 0.84 (3) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Louis Van Herck (`KXITFMATCH-26NOV10VANSLI-VAN`) | 0.70 / 0.88 (5) | 79.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Richard Zusman vs Oliwier Sterniczuk -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208890:214531:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oliwier Sterniczuk (`KXITFMATCH-26NOV10ZUSSTE-STE`) | 0.28 / 0.44 (3) | 36.0% | 82.9% | 60.4% | 81.3% [80.6%-82.5%] | -- | -- | -- | -- | PASS | +46.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Richard Zusman (`KXITFMATCH-26NOV10ZUSSTE-ZUS`) | 0.59 / 0.69 (81) | 64.0% | 17.1% | 39.6% | 18.7% [17.5%-19.4%] | -- | -- | -- | -- | PASS | -46.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 633.0, B 94.0; serve-point win A 54.2%, B 38.6%; Elo A 1045.7, B 1316.0; model uncertainty 0.0092
* Form inputs: days since last match A 441, B 196; matches on record A 61, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10ZUSSTE-STE  (YES = Oliwier Sterniczuk)
Model: 83%
Kalshi: 36%
Gap: +47 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.007, surface_dev_loose -0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Romy De Baene vs Sophie Ehrenbergerova -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10DEBEHR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romy De Baene (`KXITFWMATCH-26NOV10DEBEHR-DEB`) | 0.34 / 0.43 (43) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sophie Ehrenbergerova (`KXITFWMATCH-26NOV10DEBEHR-EHR`) | 0.53 / 0.70 (10) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Louanne Djafari vs Nadia Affelt -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260307:267735:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nadia Affelt (`KXITFWMATCH-26NOV10DJAAFF-AFF`) | 0.38 / 0.56 (1) | 47.0% | 70.7% | 50.0% | 61.6% [60.5%-62.6%] | -- | -- | -- | -- | PASS | +23.7 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Louanne Djafari (`KXITFWMATCH-26NOV10DJAAFF-DJA`) | 0.50 / 0.61 (1) | 55.5% | 29.3% | 50.0% | 38.4% [37.4%-39.5%] | -- | -- | -- | -- | PASS | -26.2 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 165.0, B 146.0; serve-point win A 52.2%, B 43.7%; Elo A 1179.4, B 1268.7; model uncertainty 0.0102
* Form inputs: days since last match A 280, B 455; matches on record A 7, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10DJAAFF-AFF  (YES = Nadia Affelt)
Model: 71%
Kalshi: 47%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Garcia Cid vs Anna Petkovic -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:225850:252571:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Garcia Cid (`KXITFWMATCH-26NOV10GARPET-GAR`) | 0.69 / 0.79 (62) | 74.0% | 84.2% | 88.3% | 79.7% [69.9%-84.2%] | -- | -- | -- | -- | PASS | +10.2 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Petkovic (`KXITFWMATCH-26NOV10GARPET-PET`) | 0.20 / 0.26 (26) | 23.0% | 15.8% | 11.7% | 20.3% [15.8%-30.1%] | -- | -- | -- | -- | PASS | -7.2 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1857.0, B 1778.0; serve-point win A 57.1%, B 50.4%; Elo A 1513.6, B 1402.9; model uncertainty 0.0715
* Form inputs: days since last match A 28, B 113; matches on record A 87, B 78; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.011, surface_dev_loose +0.021, surface_dev_tight -0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Astrid Lew Yan Foon vs Angelica Raggi -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216051:235159:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Astrid Lew Yan Foon (`KXITFWMATCH-26NOV10LEWRAG-LEW`) | 0.48 / 0.60 (63) | 54.0% | 57.8% | 39.4% | 45.7% [42.0%-53.2%] | -- | -- | -- | -- | PASS | +3.8 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Angelica Raggi (`KXITFWMATCH-26NOV10LEWRAG-RAG`) | 0.38 / 0.49 (49) | 43.5% | 42.2% | 60.6% | 54.3% [46.8%-58.0%] | -- | -- | -- | -- | PASS | -1.3 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1722.0, B 2349.0; serve-point win A 54.1%, B 47.4%; Elo A 1525.8, B 1503.9; model uncertainty 0.0558
* Form inputs: days since last match A 126, B 203; matches on record A 180, B 320; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daisy Mewett vs Leila Fabbri -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10MEWFAB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leila Fabbri (`KXITFWMATCH-26NOV10MEWFAB-FAB`) | 0.06 / 0.95 (56) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daisy Mewett (`KXITFWMATCH-26NOV10MEWFAB-MEW`) | 0.05 / 0.93 (56) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eloise Newberry vs Ariadna Garcia-Patron Canals -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10NEWGAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ariadna Garcia-Patron Canals (`KXITFWMATCH-26NOV10NEWGAR-GAR`) | 0.56 / 0.71 (86) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eloise Newberry (`KXITFWMATCH-26NOV10NEWGAR-NEW`) | 0.31 / 0.50 (13) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Serena Paris vs Luisa Fusil -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260118:269936:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luisa Fusil (`KXITFWMATCH-26NOV10PARFUS-FUS`) | 0.15 / 0.16 (29) | 15.5% | 66.6% | 50.0% | 62.6% [61.6%-62.6%] | -- | -- | -- | -- | PASS | +51.1 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Serena Paris (`KXITFWMATCH-26NOV10PARFUS-PAR`) | 0.77 / 0.96 (134) | 86.5% | 33.4% | 50.0% | 37.4% [37.4%-38.4%] | -- | -- | -- | -- | PASS | -53.1 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 52.3%, B 44.5%; Elo A 1224.7, B 1311.5; model uncertainty 0.0051
* Form inputs: days since last match A 707, B 735; matches on record A 5, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10PARFUS-FUS  (YES = Luisa Fusil)
Model: 67%
Kalshi: 16%
Gap: +51 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Laura Svatikova vs Tina Nadine Smith -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215505:220735:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tina Nadine Smith (`KXITFWMATCH-26NOV10SVASMI-SMI`) | 0.63 / 0.76 (51) | 69.5% | 90.2% | 75.6% | 78.4% [76.0%-82.1%] | -- | -- | -- | -- | PASS | +20.7 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Laura Svatikova (`KXITFWMATCH-26NOV10SVASMI-SVA`) | 0.23 / 0.32 (37) | 27.5% | 9.8% | 24.4% | 21.6% [17.9%-24.0%] | -- | -- | -- | -- | PASS | -17.7 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1657.0, B 2598.0; serve-point win A 49.8%, B 40.5%; Elo A 1303.4, B 1554.8; model uncertainty 0.0307
* Form inputs: days since last match A 357, B 294; matches on record A 244, B 342; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10SVASMI-SMI  (YES = Tina Nadine Smith)
Model: 90%
Kalshi: 70%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.024, surface_dev_loose +0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vicky Van de Peer vs Antonia Stoyanov -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220614:267422:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Antonia Stoyanov (`KXITFWMATCH-26NOV10VANSTO-STO`) | 0.87 / 0.93 (16) | 90.0% | 75.7% | 63.1% | 59.6% [55.3%-62.6%] | -- | -- | -- | -- | PASS | -14.3 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vicky Van de Peer (`KXITFWMATCH-26NOV10VANSTO-VAN`) | 0.05 / 0.09 (28) | 7.0% | 24.3% | 36.9% | 40.5% [37.4%-44.7%] | -- | -- | -- | -- | PASS | +17.3 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1898.0, B 608.0; serve-point win A 49.4%, B 45.4%; Elo A 1398.5, B 1451.4; model uncertainty 0.0366
* Form inputs: days since last match A 427, B 210; matches on record A 239, B 24; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10VANSTO-VAN  (YES = Vicky Van de Peer)
Model: 24%
Kalshi: 7%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Iliia Dashkevich vs Nehanda Thomias -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:261962:266540:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iliia Dashkevich (`KXITFWMATCH-26NOV10DASTHO-DAS`) | 0.04 / 0.96 (156) | 50.0% | 41.6% | 60.1% | 48.9% [47.9%-50.0%] | -- | -- | -- | -- | PASS | -8.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Nehanda Thomias (`KXITFWMATCH-26NOV10DASTHO-THO`) | 0.05 / 0.96 (134) | 50.5% | 58.4% | 39.9% | 51.1% [50.0%-52.1%] | -- | -- | -- | -- | PASS | +7.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 300.0; serve-point win A 51.8%, B 46.6%; Elo A 1187.5, B 1193.8; model uncertainty 0.0107
* Form inputs: days since last match A 924, B 301; matches on record A 10, B 21; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ana Giraldi Requena vs Silvia Caliman -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216198:270398:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Silvia Caliman (`KXITFWMATCH-26NOV10GIRCAL-CAL`) | 0.05 / 0.40 (42) | 22.5% | 28.4% | 63.2% | 43.6% [41.5%-44.6%] | -- | -- | -- | -- | PASS | +5.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ana Giraldi Requena (`KXITFWMATCH-26NOV10GIRCAL-GIR`) | 0.82 / 0.95 (500) | 88.5% | 71.6% | 36.8% | 56.4% [55.4%-58.5%] | -- | -- | -- | -- | PASS | -16.9 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 883.0, B 92.0; serve-point win A 51.7%, B 52.6%; Elo A 1282.0, B 1231.9; model uncertainty 0.0158
* Form inputs: days since last match A 357, B 322; matches on record A 195, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ema Harajda vs Alexandra Chapurina -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10HARCHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Chapurina (`KXITFWMATCH-26NOV10HARCHA-CHA`) | 0.05 / 0.96 (156) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ema Harajda (`KXITFWMATCH-26NOV10HARCHA-HAR`) | 0.05 / 0.96 (134) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Min Liu vs Maria Pares Bergnes de las Casas -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206205:270492:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Min Liu (`KXITFWMATCH-26NOV10LIUPAR-LIU`) | 0.05 / 0.95 (500) | 50.0% | 32.3% | 17.6% | 32.6% [30.7%-34.0%] | -- | -- | -- | -- | PASS | -17.7 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Pares Bergnes de las Casas (`KXITFWMATCH-26NOV10LIUPAR-PAR`) | 0.06 / 0.95 (500) | 50.5% | 67.7% | 82.4% | 67.4% [66.0%-69.3%] | -- | -- | -- | -- | PASS | +17.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 746.0, B 161.0; serve-point win A 53.6%, B 43.0%; Elo A 1181.5, B 1296.6; model uncertainty 0.0163
* Form inputs: days since last match A 148, B 196; matches on record A 143, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10LIUPAR-PAR  (YES = Maria Pares Bergnes de las Casas)
Model: 68%
Kalshi: 50%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ginevra Parentini Vallega Montebruno vs Cecilia Manitto -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:237481:253658:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cecilia Manitto (`KXITFWMATCH-26NOV10PARMAN-MAN`) | 0.27 / 0.48 (48) | 37.5% | 44.0% | 75.3% | 50.0% [48.9%-51.1%] | -- | -- | -- | -- | PASS | +6.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ginevra Parentini Vallega Montebruno (`KXITFWMATCH-26NOV10PARMAN-PAR`) | 0.58 / 0.71 (37) | 64.5% | 56.0% | 24.7% | 50.0% [48.9%-51.1%] | -- | -- | -- | -- | PASS | -8.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 813.0, B 52.0; serve-point win A 53.8%, B 47.4%; Elo A 1271.0, B 1264.1; model uncertainty 0.0107
* Form inputs: days since last match A 273, B 350; matches on record A 143, B 10; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marina Quesada Oyonarte vs Anna Cabassers Morros -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:269799:270075:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Cabassers Morros (`KXITFWMATCH-26NOV10QUECAB-CAB`) | 0.23 / 0.46 (46) | 34.5% | 40.0% | 43.1% | 44.7% [44.7%-44.7%] | -- | -- | -- | -- | PASS | +5.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marina Quesada Oyonarte (`KXITFWMATCH-26NOV10QUECAB-QUE`) | 0.62 / 0.82 (139) | 72.0% | 60.0% | 56.9% | 55.3% [55.3%-55.3%] | -- | -- | -- | -- | PASS | -12.0 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 116.0, B 27.0; serve-point win A 55.5%, B 46.4%; Elo A 1308.9, B 1272.2; model uncertainty 0.0001
* Form inputs: days since last match A 434, B 609; matches on record A 2, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Zhilina vs Polina Skopintseva -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259622:269773:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Skopintseva (`KXITFWMATCH-26NOV10ZHISKO-SKO`) | 0.04 / 0.96 (156) | 50.0% | 41.1% | 19.9% | 50.0% [48.9%-50.0%] | -- | -- | -- | -- | PASS | -8.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Anastasia Zhilina (`KXITFWMATCH-26NOV10ZHISKO-ZHI`) | 0.05 / 0.96 (134) | 50.5% | 58.9% | 80.1% | 50.0% [50.0%-51.1%] | -- | -- | -- | -- | PASS | +8.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 312.0; serve-point win A 53.5%, B 48.2%; Elo A 1249.1, B 1247.7; model uncertainty 0.0054
* Form inputs: days since last match A 1428, B 196; matches on record A 42, B 10; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arthur Rinderknech vs Miomir Kecmanovic -- ATP Stockholm 1/16 F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-09 14:00Z
* Current expected start: 2026-11-10 15:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 18:39Z
* Recommended handicap-by time: 2026-11-10 14:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1500_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-09T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126239:200175:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miomir Kecmanovic (`KXATPMATCH-26NOV09RINKEC-KEC`) | 0.33 / 0.34 (221) | 33.5% | 45.5% | 40.1% | 40.6% [39.6%-41.5%] | -- | -- | -- | -- | SHADOW_BET | +12.0 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arthur Rinderknech (`KXATPMATCH-26NOV09RINKEC-RIN`) | 0.66 / 0.67 (4364) | 66.5% | 54.5% | 59.9% | 59.5% [58.5%-60.4%] | -- | -- | -- | -- | PASS | -12.0 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5579.0, B 5445.0; serve-point win A 68.2%, B 32.8%; Elo A 1830.2, B 1771.1; model uncertainty 0.0091
* Form inputs: days since last match A 4, B 8; matches on record A 572, B 619; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.005, surface_dev_loose +0.009, surface_dev_tight -0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26NOV09RINKEC-RIN3` Will Arthur Rinderknech win at least 2.5 more games than Miomir Kecmanovic?: 0.53/0.55 mid 54.0%, model 36.8% (projection_v2.0 (prediction ledger)) -- gap -17.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RINKEC-RIN20` Will Arthur Rinderknech win the Arthur Rinderknech vs Miomir Kecmanovic match by a set score of 2-0?: 0.42/0.45 mid 43.5%, model 28.1% (projection_v2.0 (prediction ledger)) -- gap -15.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RINKEC-2-KEC` Will Miomir Kecmanovic win set 2 in the Arthur Rinderknech vs Miomir Kecmanovic match: 0.17/0.52 mid 34.5%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV09RINKEC-23` Over 22.5 games: 0.54/0.56 mid 55.0%, model 66.4% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV09RINKEC-RIN6` Will Arthur Rinderknech win at least 5.5 more games than Miomir Kecmanovic?: 0.16/0.19 mid 17.5%, model 6.2% (projection_v2.0 (prediction ledger)) -- gap -11.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09RINKEC-28` Over 27.5 games: 0.34/0.35 mid 34.5%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RINKEC-2-RIN` Will Arthur Rinderknech win set 2 in the Arthur Rinderknech vs Miomir Kecmanovic match: 0.42/0.83 mid 62.5%, model 53.0% (projection_v2.0 (prediction ledger)) -- gap -9.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RINKEC-1-KEC` Will Miomir Kecmanovic win set 1 in the Arthur Rinderknech vs Miomir Kecmanovic match: 0.38/0.39 mid 38.5%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap +8.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RINKEC-1-RIN` Will Arthur Rinderknech win set 1 in the Arthur Rinderknech vs Miomir Kecmanovic match: 0.61/0.62 mid 61.5%, model 53.0% (projection_v2.0 (prediction ledger)) -- gap -8.5 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV09RINKEC-KEC2` Will Miomir Kecmanovic win at least 1.5 more games than Arthur Rinderknech?: 0.27/0.31 mid 29.0%, model 37.2% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RINKEC-KEC21` Will Miomir Kecmanovic win the Arthur Rinderknech vs Miomir Kecmanovic match by a set score of 2-1?: 0.15/0.16 mid 15.5%, model 23.4% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09RINKEC-18` Over 17.5 games: 0.89/0.92 mid 90.5%, model 96.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RINKEC-KEC20` Will Miomir Kecmanovic win the Arthur Rinderknech vs Miomir Kecmanovic match by a set score of 2-0?: 0.17/0.19 mid 18.0%, model 22.1% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RINKEC-RIN21` Will Arthur Rinderknech win the Arthur Rinderknech vs Miomir Kecmanovic match by a set score of 2-1?: 0.23/0.25 mid 24.0%, model 26.4% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ole Bredschneijder vs Nicolas Ulrich -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BREULR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ole Bredschneijder (`KXITFMATCH-26NOV10BREULR-BRE`) | 0.58 / 0.76 (2) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nicolas Ulrich (`KXITFMATCH-26NOV10BREULR-ULR`) | 0.29 / 0.84 (3) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yassine Dlimi vs Ali Yazdani -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209120:212070:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yassine Dlimi (`KXITFMATCH-26NOV10DLIYAZ-DLI`) | 0.73 / 0.93 (3) | 83.0% | 84.3% | 91.2% | 86.2% [78.7%-89.5%] | -- | -- | -- | -- | PASS | +1.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ali Yazdani (`KXITFMATCH-26NOV10DLIYAZ-YAZ`) | 0.06 / 0.29 (35) | 17.5% | 15.7% | 8.8% | 13.8% [10.5%-21.3%] | -- | -- | -- | -- | PASS | -1.8 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1862.0, B 2400.0; serve-point win A 66.0%, B 41.9%; Elo A 1463.9, B 1240.0; model uncertainty 0.0543
* Form inputs: days since last match A 51, B 224; matches on record A 115, B 70; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.003, surface_dev_loose +0.011, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Remy Dugardin vs Arman Dubreuil -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10DUGDUB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arman Dubreuil (`KXITFMATCH-26NOV10DUGDUB-DUB`) | 0.05 / 0.94 (28) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Remy Dugardin (`KXITFMATCH-26NOV10DUGDUB-DUG`) | 0.07 / 0.94 (56) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dzmitry Dziubailau vs Dmytro Vterkovskiy -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10DZIVTE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dzmitry Dziubailau (`KXITFMATCH-26NOV10DZIVTE-DZI`) | 0.28 / 0.79 (10) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dmytro Vterkovskiy (`KXITFMATCH-26NOV10DZIVTE-VTE`) | 0.53 / 0.77 (1) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ammar Elamin vs Hugo Maurice -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208197:214119:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ammar Elamin (`KXITFMATCH-26NOV10ELAMAU-ELA`) | 0.74 / 0.93 (30) | 83.5% | 38.8% | 41.4% | 32.3% [31.4%-33.2%] | -- | -- | -- | -- | PASS | -44.7 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Hugo Maurice (`KXITFMATCH-26NOV10ELAMAU-MAU`) | 0.12 / 0.87 (114) | 49.5% | 61.2% | 58.6% | 67.7% [66.8%-68.6%] | -- | -- | -- | -- | PASS | +11.7 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 528.0, B 48.0; serve-point win A 60.3%, B 37.4%; Elo A 1142.0, B 1272.1; model uncertainty 0.0092
* Form inputs: days since last match A 203, B 385; matches on record A 47, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.009, surface_dev_loose -0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Veljko Krstic vs Matyas Cerny -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210063:210112:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matyas Cerny (`KXITFMATCH-26NOV10KRSCER-CER`) | 0.67 / 0.77 (23) | 72.0% | 90.2% | 90.7% | 78.7% [75.2%-82.1%] | -- | -- | -- | -- | PASS | +18.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Veljko Krstic (`KXITFMATCH-26NOV10KRSCER-KRS`) | 0.18 / 0.40 (41) | 29.0% | 9.8% | 9.3% | 21.3% [17.9%-24.8%] | -- | -- | -- | -- | PASS | -19.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 106.0, B 1849.0; serve-point win A 50.8%, B 39.4%; Elo A 1205.2, B 1417.0; model uncertainty 0.0344
* Form inputs: days since last match A 518, B 105; matches on record A 7, B 103; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10KRSCER-CER  (YES = Matyas Cerny)
Model: 90%
Kalshi: 72%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.024, surface_pool_high -0.011, surface_dev_loose +0.000, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cem Christopher Kucukhuseyin vs Jonas Gundacker -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10KUCGUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonas Gundacker (`KXITFMATCH-26NOV10KUCGUN-GUN`) | 0.77 / 0.89 (22) | 83.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cem Christopher Kucukhuseyin (`KXITFMATCH-26NOV10KUCGUN-KUC`) | 0.06 / 0.31 (36) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Melvin Kumar vs Charlie Bazil -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10KUMBAZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charlie Bazil (`KXITFMATCH-26NOV10KUMBAZ-BAZ`) | 0.16 / 0.66 (114) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Melvin Kumar (`KXITFMATCH-26NOV10KUMBAZ-KUM`) | 0.71 / 0.94 (3) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Noah Lopez vs Dragos Nicolae Madaras -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200096:210055:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noah Lopez (`KXITFMATCH-26NOV10LOPMAD-LOP`) | 0.14 / 0.34 (37) | 24.0% | 6.4% | 2.3% | 5.1% [3.3%-8.4%] | -- | -- | -- | -- | PASS | -17.6 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dragos Nicolae Madaras (`KXITFMATCH-26NOV10LOPMAD-MAD`) | 0.71 / 0.86 (178) | 78.5% | 93.6% | 97.7% | 94.9% [91.6%-96.7%] | -- | -- | -- | -- | PASS | +15.1 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 919.0, B 1412.0; serve-point win A 50.4%, B 38.0%; Elo A 1218.7, B 1644.1; model uncertainty 0.0252
* Form inputs: days since last match A 196, B 224; matches on record A 113, B 453; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10LOPMAD-MAD  (YES = Dragos Nicolae Madaras)
Model: 94%
Kalshi: 78%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.001, surface_pool_high +0.001, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vladimir Osminkin vs Antoni Fabre -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209858:212934:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Antoni Fabre (`KXITFMATCH-26NOV10OSMFAB-FAB`) | 0.74 / 0.94 (1) | 84.0% | 57.9% | 41.1% | 48.9% [47.9%-50.0%] | -- | -- | -- | -- | PASS | -26.1 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Vladimir Osminkin (`KXITFMATCH-26NOV10OSMFAB-OSM`) | 0.11 / 0.21 (31) | 16.0% | 42.1% | 58.9% | 51.0% [50.0%-52.1%] | -- | -- | -- | -- | PASS | +26.1 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 944.0; serve-point win A 56.2%, B 42.3%; Elo A 1271.0, B 1264.7; model uncertainty 0.0105
* Form inputs: days since last match A 2457, B 196; matches on record A 1, B 24; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10OSMFAB-OSM  (YES = Vladimir Osminkin)
Model: 42%
Kalshi: 16%
Gap: +26 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniil Piatrouski vs Barney Fitzpatrick -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207167:212853:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barney Fitzpatrick (`KXITFMATCH-26NOV10PIAFIT-FIT`) | 0.43 / 0.88 (114) | 65.5% | 52.0% | 56.7% | 57.2% [56.2%-57.2%] | -- | -- | -- | -- | PASS | -13.4 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Daniil Piatrouski (`KXITFMATCH-26NOV10PIAFIT-PIA`) | 0.45 / 0.80 (86) | 62.5% | 47.9% | 43.3% | 42.8% [42.8%-43.8%] | -- | -- | -- | -- | PASS | -14.6 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 250.0, B 76.0; serve-point win A 60.0%, B 39.6%; Elo A 1165.6, B 1212.6; model uncertainty 0.0051
* Form inputs: days since last match A 252, B 441; matches on record A 7, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karim Sherif Abdellatif Abdo vs Cedric Stanke -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210453:214091:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karim Sherif Abdellatif Abdo (`KXITFMATCH-26NOV10SHESTA-SHE`) | 0.08 / 0.77 (3) | 42.5% | 49.4% | 50.0% | 62.2% [60.2%-64.1%] | -- | -- | -- | -- | PASS | +6.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Cedric Stanke (`KXITFMATCH-26NOV10SHESTA-STA`) | 0.84 / 0.95 (283) | 89.5% | 50.6% | 50.0% | 37.8% [35.9%-39.8%] | -- | -- | -- | -- | PASS | -38.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 68.0, B 375.0; serve-point win A 59.9%, B 40.0%; Elo A 1244.1, B 1152.8; model uncertainty 0.0195
* Form inputs: days since last match A 308, B 203; matches on record A 2, B 30; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matthias Ujvary vs Stefan Adrian Andreescu -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210650:210745:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Adrian Andreescu (`KXITFMATCH-26NOV10UJVAND-AND`) | 0.56 / 0.76 (30) | 66.0% | 77.5% | 83.2% | 82.5% [78.2%-84.2%] | -- | -- | -- | -- | PASS | +11.6 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matthias Ujvary (`KXITFMATCH-26NOV10UJVAND-UJV`) | 0.21 / 0.43 (5) | 32.0% | 22.4% | 16.8% | 17.5% [15.8%-21.8%] | -- | -- | -- | -- | PASS | -9.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2120.0, B 3228.0; serve-point win A 51.2%, B 43.1%; Elo A 1189.0, B 1441.5; model uncertainty 0.0298
* Form inputs: days since last match A 196, B 259; matches on record A 116, B 144; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high +0.000, surface_dev_loose -0.003, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martin Van Der Meerschen vs Viacheslav Bielinskyi -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207592:209907:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viacheslav Bielinskyi (`KXITFMATCH-26NOV10VANBIE-BIE`) | 0.58 / 0.68 (78) | 63.0% | 84.1% | 89.5% | 86.6% [80.5%-89.3%] | -- | -- | -- | -- | PASS | +21.1 pp | HIGH_REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Martin Van Der Meerschen (`KXITFMATCH-26NOV10VANBIE-VAN`) | 0.28 / 0.52 (3) | 40.0% | 15.9% | 10.5% | 13.4% [10.7%-19.5%] | -- | -- | -- | -- | PASS | -24.1 pp | HIGH_REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2032.0, B 2937.0; serve-point win A 50.5%, B 42.0%; Elo A 1326.4, B 1588.9; model uncertainty 0.0436
* Form inputs: days since last match A 196, B 210; matches on record A 103, B 231; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10VANBIE-BIE  (YES = Viacheslav Bielinskyi)
Model: 84%
Kalshi: 63%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.006, surface_dev_loose -0.003, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sonia Cassani vs Zeinab Ayadi -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222700:267857:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zeinab Ayadi (`KXITFWMATCH-26NOV10CASAYA-AYA`) | 0.13 / 0.32 (36) | 22.5% | 27.8% | 49.5% | 55.3% [54.2%-55.3%] | -- | -- | -- | -- | PASS | +5.3 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sonia Cassani (`KXITFWMATCH-26NOV10CASAYA-CAS`) | 0.73 / 0.85 (9) | 79.0% | 72.2% | 50.5% | 44.7% [44.7%-45.8%] | -- | -- | -- | -- | PASS | -6.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 84.0, B 140.0; serve-point win A 56.8%, B 47.6%; Elo A 1176.3, B 1214.0; model uncertainty 0.0053
* Form inputs: days since last match A 364, B 315; matches on record A 85, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leire De Ezcurra vs Daria Barsukov -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10DEEBAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Barsukov (`KXITFWMATCH-26NOV10DEEBAR-BAR`) | 0.52 / 0.84 (1) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leire De Ezcurra (`KXITFWMATCH-26NOV10DEEBAR-DEE`) | 0.34 / 0.72 (1) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chelsea Fontenel vs Capucine Cedillo- Vayson de Pradenne -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:239454:266808:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Capucine Cedillo- Vayson de Pradenne (`KXITFWMATCH-26NOV10FONCED-CED`) | 0.06 / 0.16 (22) | 11.0% | 12.7% | 48.4% | 35.5% [33.5%-37.5%] | -- | -- | -- | -- | PASS | +1.7 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Chelsea Fontenel (`KXITFWMATCH-26NOV10FONCED-FON`) | 0.83 / 0.88 (4) | 85.5% | 87.3% | 51.6% | 64.5% [62.5%-66.5%] | -- | -- | -- | -- | PASS | +1.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 2027.0, B 0.0; serve-point win A 59.9%, B 48.7%; Elo A 1321.2, B 1216.2; model uncertainty 0.0199
* Form inputs: days since last match A 203, B 966; matches on record A 114, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amelia Honer vs Jade Groen -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264192:267722:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jade Groen (`KXITFWMATCH-26NOV10HONGRO-GRO`) | 0.20 / 0.21 (37) | 20.5% | 6.3% | 17.1% | 11.4% [10.0%-12.5%] | -- | -- | -- | -- | PASS | -14.2 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amelia Honer (`KXITFWMATCH-26NOV10HONGRO-HON`) | 0.73 / 0.87 (15) | 80.0% | 93.7% | 83.0% | 88.6% [87.5%-90.0%] | -- | -- | -- | -- | PASS | +13.7 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1349.0, B 470.0; serve-point win A 57.7%, B 53.8%; Elo A 1670.2, B 1292.1; model uncertainty 0.0123
* Form inputs: days since last match A 196, B 364; matches on record A 48, B 9; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.011, surface_dev_loose +0.007, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victoria Kapcia vs Ranim Rassil -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:246519:259999:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victoria Kapcia (`KXITFWMATCH-26NOV10KAPRAS-KAP`) | 0.65 / 0.95 (5) | 80.0% | 38.2% | 20.8% | 42.6% [41.5%-43.6%] | -- | -- | -- | -- | PASS | -41.8 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ranim Rassil (`KXITFWMATCH-26NOV10KAPRAS-RAS`) | 0.20 / 0.71 (3) | 45.5% | 61.8% | 79.2% | 57.4% [56.4%-58.5%] | -- | -- | -- | -- | PASS | +16.3 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 358.0, B 70.0; serve-point win A 52.5%, B 45.2%; Elo A 1131.9, B 1175.0; model uncertainty 0.0105
* Form inputs: days since last match A 231, B 469; matches on record A 12, B 81; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10KAPRAS-RAS  (YES = Ranim Rassil)
Model: 62%
Kalshi: 46%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria Kuczer vs Estella Jaeger -- W15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214784:219972:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Estella Jaeger (`KXITFWMATCH-26NOV10KUCJAE-JAE`) | 0.06 / 0.77 (3) | 41.5% | 10.0% | 15.1% | 16.0% [13.6%-18.8%] | -- | -- | -- | -- | PASS | -31.5 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Daria Kuczer (`KXITFWMATCH-26NOV10KUCJAE-KUC`) | 0.84 / 0.96 (134) | 90.0% | 90.0% | 84.9% | 84.0% [81.2%-86.5%] | -- | -- | -- | -- | PASS | +0.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 816.0, B 391.0; serve-point win A 54.9%, B 54.7%; Elo A 1451.2, B 1165.5; model uncertainty 0.0261
* Form inputs: days since last match A 462, B 196; matches on record A 172, B 75; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.028, surface_dev_loose +0.003, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katarina Kujovic vs Marie Vogt -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223100:268778:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katarina Kujovic (`KXITFWMATCH-26NOV10KUJVOG-KUJ`) | 0.08 / 0.23 (32) | 15.5% | 10.4% | 5.8% | 13.4% [9.5%-20.4%] | -- | -- | -- | -- | PASS | -5.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marie Vogt (`KXITFWMATCH-26NOV10KUJVOG-VOG`) | 0.79 / 0.89 (25) | 84.0% | 89.6% | 94.2% | 86.6% [79.6%-90.5%] | -- | -- | -- | -- | PASS | +5.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 711.0, B 2280.0; serve-point win A 48.6%, B 42.0%; Elo A 1283.7, B 1534.7; model uncertainty 0.0541
* Form inputs: days since last match A 308, B 29; matches on record A 15, B 164; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.003, surface_dev_loose -0.014, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Milla Sequeira vs Lya Fernandez -- W15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223435:259749:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lya Fernandez (`KXITFWMATCH-26NOV10SEQFER-FER`) | 0.84 / 0.95 (1) | 89.5% | 88.8% | 92.8% | 87.0% [82.6%-91.0%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Milla Sequeira (`KXITFWMATCH-26NOV10SEQFER-SEQ`) | 0.04 / 0.22 (50) | 13.0% | 11.2% | 7.2% | 13.0% [9.0%-17.4%] | -- | -- | -- | -- | PASS | -1.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 623.0, B 463.0; serve-point win A 46.4%, B 44.5%; Elo A 1053.6, B 1351.0; model uncertainty 0.0421
* Form inputs: days since last match A 231, B 196; matches on record A 119, B 66; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.012, surface_pool_high -0.011, surface_dev_loose -0.011, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ilay Yoruk vs Anamaria Federica Oana -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215879:260254:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anamaria Federica Oana (`KXITFWMATCH-26NOV10YOROAN-OAN`) | 0.23 / 0.41 (12) | 32.0% | 76.4% | 94.4% | 83.0% [61.6%-90.1%] | -- | -- | -- | -- | PASS | +44.4 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ilay Yoruk (`KXITFWMATCH-26NOV10YOROAN-YOR`) | 0.63 / 0.79 (119) | 71.0% | 23.6% | 5.6% | 17.0% [9.9%-38.4%] | -- | -- | -- | -- | PASS | -47.4 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1694.0, B 1406.0; serve-point win A 48.7%, B 46.0%; Elo A 1423.6, B 1517.3; model uncertainty 0.1424
* Form inputs: days since last match A 36, B 259; matches on record A 466, B 86; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10YOROAN-OAN  (YES = Anamaria Federica Oana)
Model: 76%
Kalshi: 32%
Gap: +44 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.013, surface_dev_loose -0.023, surface_dev_tight +0.025
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dan Brand vs Jakub Filip -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210623:214242:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dan Brand (`KXITFMATCH-26NOV10BRAFIL-BRA`) | 0.23 / 0.36 (40) | 29.5% | 34.0% | 37.6% | 40.6% [38.6%-43.7%] | -- | -- | -- | -- | PASS | +4.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jakub Filip (`KXITFMATCH-26NOV10BRAFIL-FIL`) | 0.62 / 0.73 (54) | 67.5% | 66.0% | 62.4% | 59.4% [56.3%-61.4%] | -- | -- | -- | -- | PASS | -1.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 160.0, B 1554.0; serve-point win A 56.0%, B 40.9%; Elo A 1247.7, B 1309.2; model uncertainty 0.0256
* Form inputs: days since last match A 231, B 84; matches on record A 2, B 92; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.031, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ioannis Kountourakis vs Julio Cesar Porras -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210076:210132:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ioannis Kountourakis (`KXITFMATCH-26NOV10KOUPOR-KOU`) | 0.21 / 0.29 (36) | 25.0% | 13.5% | 16.5% | 13.2% [12.2%-15.6%] | -- | -- | -- | -- | PASS | -11.5 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julio Cesar Porras (`KXITFMATCH-26NOV10KOUPOR-POR`) | 0.69 / 0.74 (96) | 71.5% | 86.5% | 83.5% | 86.8% [84.4%-87.8%] | -- | -- | -- | -- | PASS | +15.0 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1589.0, B 1554.0; serve-point win A 55.0%, B 36.5%; Elo A 1119.6, B 1485.8; model uncertainty 0.0171
* Form inputs: days since last match A 210, B 350; matches on record A 63, B 115; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10KOUPOR-POR  (YES = Julio Cesar Porras)
Model: 87%
Kalshi: 72%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.001, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matias Reyniak vs Matthew Thomson -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10REYTHO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matias Reyniak (`KXITFMATCH-26NOV10REYTHO-REY`) | 0.46 / 0.56 (42) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matthew Thomson (`KXITFMATCH-26NOV10REYTHO-THO`) | 0.37 / 0.49 (49) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Flynn Thomas vs Dimitris Azoidis -- M15 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213151:tml:A0C5:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dimitris Azoidis (`KXITFMATCH-26NOV10THOAZO-AZO`) | 0.32 / 0.45 (45) | 38.5% | 69.0% | 75.7% | 75.7% [75.7%-75.7%] | -- | -- | -- | -- | PASS | +30.5 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Flynn Thomas (`KXITFMATCH-26NOV10THOAZO-THO`) | 0.49 / 0.62 (8) | 55.5% | 31.0% | 24.3% | 24.3% [24.3%-24.3%] | -- | -- | -- | -- | PASS | -24.5 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 723.0, B 0.0; serve-point win A 58.1%, B 38.1%; Elo A 1283.7, B 1487.0; model uncertainty 0.0
* Form inputs: days since last match A 217, B 786; matches on record A 16, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10THOAZO-AZO  (YES = Dimitris Azoidis)
Model: 69%
Kalshi: 38%
Gap: +30 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Justine Bretnacher vs Helene Pellicano -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220532:267401:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justine Bretnacher (`KXITFWMATCH-26NOV10BREPEL-BRE`) | 0.51 / 0.72 (90) | 61.5% | 11.3% | 51.6% | 28.7% [26.0%-30.5%] | -- | -- | -- | -- | PASS | -50.2 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Helene Pellicano (`KXITFWMATCH-26NOV10BREPEL-PEL`) | 0.35 / 0.56 (43) | 45.5% | 88.7% | 48.4% | 71.3% [69.5%-74.0%] | -- | -- | -- | -- | PASS | +43.2 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 222.0, B 43.0; serve-point win A 47.8%, B 43.1%; Elo A 1206.2, B 1374.1; model uncertainty 0.0226
* Form inputs: days since last match A 350, B 595; matches on record A 22, B 117; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10BREPEL-PEL  (YES = Helene Pellicano)
Model: 89%
Kalshi: 46%
Gap: +43 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.027, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mar Cabassers Morros vs Lucia Ros Parres -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260668:270068:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mar Cabassers Morros (`KXITFWMATCH-26NOV10CABROS-CAB`) | 0.06 / 0.95 (500) | 50.5% | 28.9% | 42.0% | 41.5% [40.5%-41.5%] | -- | -- | -- | -- | PASS | -21.6 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lucia Ros Parres (`KXITFWMATCH-26NOV10CABROS-ROS`) | 0.05 / 0.94 (416) | 49.5% | 71.1% | 58.0% | 58.5% [58.5%-59.5%] | -- | -- | -- | -- | PASS | +21.6 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 144.0, B 375.0; serve-point win A 50.8%, B 45.0%; Elo A 1221.4, B 1281.8; model uncertainty 0.0053
* Form inputs: days since last match A 427, B 343; matches on record A 3, B 43; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10CABROS-ROS  (YES = Lucia Ros Parres)
Model: 71%
Kalshi: 50%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Delia Gaillard vs Sofia Tatu -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10GAITAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Delia Gaillard (`KXITFWMATCH-26NOV10GAITAT-GAI`) | 0.07 / 0.93 (357) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofia Tatu (`KXITFWMATCH-26NOV10GAITAT-TAT`) | 0.04 / 0.93 (357) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dimitra Georgakopoulou vs Alisa Oktiabreva -- W35 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260765:266815:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dimitra Georgakopoulou (`KXITFWMATCH-26NOV10GEOOKT-GEO`) | 0.03 / 0.08 (375) | 5.5% | 0.8% | 4.3% | 7.4% [5.4%-9.9%] | -- | -- | -- | -- | PASS | -4.7 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alisa Oktiabreva (`KXITFWMATCH-26NOV10GEOOKT-OKT`) | 0.94 / 0.96 (25) | 95.0% | 99.2% | 95.7% | 92.6% [90.1%-94.6%] | -- | -- | -- | -- | PASS | +4.2 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 78.0, B 1999.0; serve-point win A 40.5%, B 41.4%; Elo A 1218.0, B 1652.3; model uncertainty 0.0225
* Form inputs: days since last match A 371, B 112; matches on record A 3, B 67; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.025, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matilde Paoletti vs Cristina Diaz Adrover -- W35 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222396:232881:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Diaz Adrover (`KXITFWMATCH-26NOV10PAODIA-DIA`) | 0.07 / 0.19 (31) | 13.0% | 25.1% | 61.6% | 40.5% [35.4%-44.7%] | -- | -- | -- | -- | PASS | +12.1 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matilde Paoletti (`KXITFWMATCH-26NOV10PAODIA-PAO`) | 0.79 / 0.91 (30) | 85.0% | 75.0% | 38.4% | 59.6% [55.3%-64.6%] | -- | -- | -- | -- | PASS | -10.1 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 466.0, B 3491.0; serve-point win A 54.6%, B 50.5%; Elo A 1577.0, B 1462.3; model uncertainty 0.0465
* Form inputs: days since last match A 217, B 28; matches on record A 103, B 204; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sapfo Sakellaridi vs Anja Stankovic -- W35 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220364:244087:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sapfo Sakellaridi (`KXITFWMATCH-26NOV10SAKSTA-SAK`) | 0.36 / 0.40 (41) | 38.0% | 47.1% | 70.1% | 58.2% [49.5%-63.1%] | -- | -- | -- | -- | WATCH | +9.2 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anja Stankovic (`KXITFWMATCH-26NOV10SAKSTA-STA`) | 0.53 / 0.71 (7) | 62.0% | 52.8% | 29.9% | 41.8% [36.9%-50.5%] | -- | -- | -- | -- | PASS | -9.2 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4165.0, B 2297.0; serve-point win A 60.1%, B 39.4%; Elo A 1427.4, B 1499.8; model uncertainty 0.0682
* Form inputs: days since last match A 14, B 259; matches on record A 705, B 192; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.040, surface_pool_high -0.030, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Natalija Senic vs Elena Korokozidi -- W35 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222481:239476:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Korokozidi (`KXITFWMATCH-26NOV10SENKOR-KOR`) | 0.48 / 0.58 (41) | 53.0% | 25.7% | 21.8% | 25.1% [21.8%-30.0%] | -- | -- | -- | -- | PASS | -27.3 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Natalija Senic (`KXITFWMATCH-26NOV10SENKOR-SEN`) | 0.42 / 0.46 (10) | 44.0% | 74.3% | 78.2% | 74.9% [70.0%-78.2%] | -- | -- | -- | -- | WATCH | +30.3 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2163.0, B 2005.0; serve-point win A 53.2%, B 51.7%; Elo A 1564.9, B 1418.7; model uncertainty 0.0412
* Form inputs: days since last match A 196, B 196; matches on record A 257, B 149; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10SENKOR-SEN  (YES = Natalija Senic)
Model: 74%
Kalshi: 44%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Trujillo Garnica vs Isabel Adrover Gallego -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 15:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220289:264186:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isabel Adrover Gallego (`KXITFWMATCH-26NOV10TRUADR-ADR`) | 0.06 / 0.93 (357) | 49.5% | 79.3% | 62.6% | 59.5% [57.4%-62.6%] | -- | -- | -- | -- | PASS | +29.8 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Trujillo Garnica (`KXITFWMATCH-26NOV10TRUADR-TRU`) | 0.05 / 0.92 (313) | 48.5% | 20.7% | 37.4% | 40.5% [37.4%-42.6%] | -- | -- | -- | -- | PASS | -27.8 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 185.0, B 516.0; serve-point win A 50.3%, B 43.6%; Elo A 1195.2, B 1260.2; model uncertainty 0.0258
* Form inputs: days since last match A 329, B 364; matches on record A 5, B 83; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10TRUADR-ADR  (YES = Isabel Adrover Gallego)
Model: 79%
Kalshi: 50%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.031, surface_pool_high +0.021, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mario Arce Fernandez vs Manuel Belda -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ARCBEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mario Arce Fernandez (`KXITFMATCH-26NOV10ARCBEL-ARC`) | 0.80 / 0.95 (305) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Manuel Belda (`KXITFMATCH-26NOV10ARCBEL-BEL`) | 0.06 / 0.92 (3) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adam Kaczmarek vs Alberto Garcia Garcia -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212527:213742:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alberto Garcia Garcia (`KXITFMATCH-26NOV10KACGAR-GAR`) | 0.54 / 0.92 (3) | 73.0% | 40.5% | 22.1% | 38.7% [38.6%-39.8%] | -- | -- | -- | -- | PASS | -32.5 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Adam Kaczmarek (`KXITFMATCH-26NOV10KACGAR-KAC`) | 0.32 / 0.92 (3) | 62.0% | 59.5% | 77.9% | 61.3% [60.2%-61.4%] | -- | -- | -- | -- | PASS | -2.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 294.0; serve-point win A 59.5%, B 42.3%; Elo A 1262.0, B 1185.8; model uncertainty 0.0055
* Form inputs: days since last match A 1120, B 231; matches on record A 1, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alejandro Manzanera Pertusa vs Ian Pedersen Lozano -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209904:214533:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alejandro Manzanera Pertusa (`KXITFMATCH-26NOV10MANPED-MAN`) | 0.06 / 0.95 (305) | 50.5% | 81.5% | 64.1% | 72.8% [71.5%-74.5%] | -- | -- | -- | -- | PASS | +31.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ian Pedersen Lozano (`KXITFMATCH-26NOV10MANPED-PED`) | 0.05 / 0.95 (283) | 50.0% | 18.5% | 35.9% | 27.2% [25.5%-28.5%] | -- | -- | -- | -- | PASS | -31.5 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1670.0, B 60.0; serve-point win A 63.3%, B 43.6%; Elo A 1453.7, B 1280.2; model uncertainty 0.015
* Form inputs: days since last match A 203, B 203; matches on record A 190, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10MANPED-MAN  (YES = Alejandro Manzanera Pertusa)
Model: 82%
Kalshi: 50%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.017, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Simone Massucco vs Jacopo Berrettini -- M25 San Gregorio di Catania R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202235:213179:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacopo Berrettini (`KXITFMATCH-26NOV10MASBER-BER`) | 0.70 / 0.90 (250) | 80.0% | 91.9% | 75.3% | 86.2% [85.9%-86.8%] | -- | -- | -- | -- | PASS | +11.9 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Simone Massucco (`KXITFMATCH-26NOV10MASBER-MAS`) | 0.18 / 0.36 (40) | 27.0% | 8.1% | 24.7% | 13.8% [13.2%-14.1%] | -- | -- | -- | -- | PASS | -18.9 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 69.0, B 3742.0; serve-point win A 52.3%, B 37.0%; Elo A 1245.3, B 1571.4; model uncertainty 0.0043
* Form inputs: days since last match A 364, B 224; matches on record A 2, B 386; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.006, surface_dev_loose -0.003, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Javier Molino vs Mustapha El Natour -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149285:208315:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mustapha El Natour (`KXITFMATCH-26NOV10MOLELN-ELN`) | 0.10 / 0.92 (3) | 51.0% | 55.5% | 45.8% | 63.7% [60.3%-66.1%] | -- | -- | -- | -- | PASS | +4.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Javier Molino (`KXITFMATCH-26NOV10MOLELN-MOL`) | 0.75 / 0.94 (2) | 84.5% | 44.5% | 54.2% | 36.2% [33.9%-39.7%] | -- | -- | -- | -- | PASS | -40.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 329.0, B 227.0; serve-point win A 58.2%, B 40.7%; Elo A 1198.7, B 1317.9; model uncertainty 0.029
* Form inputs: days since last match A 266, B 231; matches on record A 39, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose +0.004, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adrian Oetzbach vs Radu David Turcanu -- M25 San Gregorio di Catania R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144907:212886:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Oetzbach (`KXITFMATCH-26NOV10OETTUR-OET`) | 0.37 / 0.57 (58) | 47.0% | 36.9% | 44.8% | 42.2% [41.2%-43.2%] | -- | -- | -- | -- | PASS | -10.1 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Radu David Turcanu (`KXITFMATCH-26NOV10OETTUR-TUR`) | 0.50 / 0.68 (1) | 59.0% | 63.1% | 55.2% | 57.8% [56.8%-58.8%] | -- | -- | -- | -- | PASS | +4.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3595.0, B 2023.0; serve-point win A 56.7%, B 40.7%; Elo A 1388.5, B 1468.2; model uncertainty 0.0103
* Form inputs: days since last match A 196, B 217; matches on record A 303, B 62; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Alekseeva vs Marfa Mylnikova -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:269818:270215:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Alekseeva (`KXITFWMATCH-26NOV10ALEMYL-ALE`) | 0.05 / 0.96 (156) | 50.5% | 57.6% | 31.6% | 46.8% [45.2%-47.9%] | -- | -- | -- | -- | PASS | +7.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marfa Mylnikova (`KXITFWMATCH-26NOV10ALEMYL-MYL`) | 0.04 / 0.96 (134) | 50.0% | 42.4% | 68.4% | 53.2% [52.1%-54.8%] | -- | -- | -- | -- | PASS | -7.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 339.0, B 129.0; serve-point win A 56.1%, B 45.3%; Elo A 1252.5, B 1265.2; model uncertainty 0.0131
* Form inputs: days since last match A 238, B 245; matches on record A 8, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Brunet-Brady vs Hanna Bougouffa -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:230121:270452:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanna Bougouffa (`KXITFWMATCH-26NOV10BRUBOU-BOU`) | 0.61 / 0.78 (53) | 69.5% | 56.5% | 40.5% | 48.9% [47.3%-51.1%] | -- | -- | -- | -- | PASS | -13.0 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Brunet-Brady (`KXITFWMATCH-26NOV10BRUBOU-BRU`) | 0.26 / 0.45 (45) | 35.5% | 43.5% | 59.6% | 51.1% [48.9%-52.7%] | -- | -- | -- | -- | PASS | +8.0 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 135.0, B 245.0; serve-point win A 51.4%, B 47.4%; Elo A 1259.2, B 1259.9; model uncertainty 0.0187
* Form inputs: days since last match A 238, B 469; matches on record A 2, B 134; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tilwith Di Girolami vs Meline Lataste -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:228910:267625:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tilwith Di Girolami (`KXITFWMATCH-26NOV10DIGLAT-DIG`) | 0.80 / 0.92 (1) | 86.0% | 93.4% | 92.7% | 80.4% [79.6%-82.6%] | -- | -- | -- | -- | PASS | +7.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Meline Lataste (`KXITFWMATCH-26NOV10DIGLAT-LAT`) | 0.08 / 0.26 (34) | 17.0% | 6.6% | 7.3% | 19.6% [17.4%-20.4%] | -- | -- | -- | -- | PASS | -10.4 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1533.0, B 62.0; serve-point win A 58.5%, B 52.8%; Elo A 1473.7, B 1236.1; model uncertainty 0.0147
* Form inputs: days since last match A 196, B 518; matches on record A 202, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Efremova / Meshcheryakova vs Belkova / Kuharenko -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10EFRMESBELKUH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Belkova / Kuharenko (`KXITFWDOUBLES-26NOV10EFRMESBELKUH-BELKUH`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Efremova / Meshcheryakova (`KXITFWDOUBLES-26NOV10EFRMESBELKUH-EFRMES`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Elkady / Nosei vs Ezzat / Salem -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10ELKNOSEZZSAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elkady / Nosei (`KXITFWDOUBLES-26NOV10ELKNOSEZZSAL-ELKNOS`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ezzat / Salem (`KXITFWDOUBLES-26NOV10ELKNOSEZZSAL-EZZSAL`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Zoe Ulrich vs Amelie Brooks -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259608:270429:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amelie Brooks (`KXITFWMATCH-26NOV10ULRBRO-BRO`) | 0.30 / 0.52 (3) | 41.0% | 40.1% | 51.1% | 44.7% [43.6%-45.2%] | -- | -- | -- | -- | PASS | -0.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zoe Ulrich (`KXITFWMATCH-26NOV10ULRBRO-ULR`) | 0.58 / 0.70 (83) | 64.0% | 59.9% | 48.9% | 55.3% [54.8%-56.4%] | -- | -- | -- | -- | PASS | -4.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 169.0, B 164.0; serve-point win A 53.8%, B 48.1%; Elo A 1257.9, B 1211.6; model uncertainty 0.0079
* Form inputs: days since last match A 273, B 196; matches on record A 2, B 19; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Robert Galloway / Andre Goransson vs Marc Polmans / Jan Zielinski -- ATP Stockholm 1/8 F

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-10 13:00Z
* Current expected start: 2026-11-10 16:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-09 18:39Z
* Recommended handicap-by time: 2026-11-10 15:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10GALGORPOLZIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robert Galloway / Andre Goransson (`KXATPDOUBLES-26NOV10GALGORPOLZIE-GALGOR`) | 0.43 / 0.46 (343) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marc Polmans / Jan Zielinski (`KXATPDOUBLES-26NOV10GALGORPOLZIE-POLZIE`) | 0.54 / 0.57 (529) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Holger Rune vs Zizou Bergs -- ATP Stockholm 1/16 F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-09 14:00Z
* Current expected start: 2026-11-10 17:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 18:39Z
* Recommended handicap-by time: 2026-11-10 16:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1620_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-09T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200267:208029:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zizou Bergs (`KXATPMATCH-26NOV09RUNBER-BER`) | 0.40 / 0.42 (12891) | 41.0% | 43.9% | 52.0% | 45.6% [42.2%-48.0%] | -- | -- | -- | -- | WATCH | +2.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Holger Rune (`KXATPMATCH-26NOV09RUNBER-RUN`) | 0.58 / 0.60 (15820) | 59.0% | 56.1% | 48.0% | 54.4% [52.0%-57.8%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3242.0, B 5856.0; serve-point win A 66.2%, B 35.1%; Elo A 1959.8, B 1830.4; model uncertainty 0.0292
* Form inputs: days since last match A 6, B 7; matches on record A 449, B 573; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26NOV09RUNBER-2-BER` Will Zizou Bergs win set 2 in the Holger Rune vs Zizou Bergs match: 0.36/0.77 mid 56.5%, model 45.9% (projection_v2.0 (prediction ledger)) -- gap -10.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV09RUNBER-RUN5` Will Holger Rune win at least 4.5 more games than Zizou Bergs?: 0.24/0.28 mid 26.0%, model 17.5% (projection_v2.0 (prediction ledger)) -- gap -8.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09RUNBER-29` Over 28.5 games: 0.28/0.32 mid 30.0%, model 38.3% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09RUNBER-24` Over 23.5 games: 0.49/0.50 mid 49.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RUNBER-RUN21` Will Holger Rune win the Holger Rune vs Zizou Bergs match by a set score of 2-1?: 0.24/0.42 mid 33.0%, model 26.9% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09RUNBER-19` Over 18.5 games: 0.83/0.87 mid 85.0%, model 90.5% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RUNBER-2-RUN` Will Holger Rune win set 2 in the Holger Rune vs Zizou Bergs match: 0.21/0.77 mid 49.0%, model 54.1% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV09RUNBER-RUN2` Will Holger Rune win at least 1.5 more games than Zizou Bergs?: 0.52/0.54 mid 53.0%, model 48.2% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RUNBER-RUN20` Will Holger Rune win the Holger Rune vs Zizou Bergs match by a set score of 2-0?: 0.12/0.37 mid 24.5%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RUNBER-BER21` Will Zizou Bergs win the Holger Rune vs Zizou Bergs match by a set score of 2-1?: 0.17/0.23 mid 20.0%, model 22.8% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RUNBER-BER20` Will Zizou Bergs win the Holger Rune vs Zizou Bergs match by a set score of 2-0?: 0.14/0.23 mid 18.5%, model 21.1% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RUNBER-1-BER` Will Zizou Bergs win set 1 in the Holger Rune vs Zizou Bergs match: 0.43/0.45 mid 44.0%, model 45.9% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RUNBER-1-RUN` Will Holger Rune win set 1 in the Holger Rune vs Zizou Bergs match: 0.54/0.56 mid 55.0%, model 54.1% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV09RUNBER-BER2` Will Zizou Bergs win at least 1.5 more games than Holger Rune?: 0.34/0.38 mid 36.0%, model 36.2% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nikola Mektic / Edouard Roger-Vasselin vs Robert Cash / Alexander Erler -- ATP Stockholm 1/8 F

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-10 13:00Z
* Current expected start: 2026-11-10 18:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-09 18:39Z
* Recommended handicap-by time: 2026-11-10 17:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10MEKROGCASERL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robert Cash / Alexander Erler (`KXATPDOUBLES-26NOV10MEKROGCASERL-CASERL`) | 0.30 / 0.35 (53) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nikola Mektic / Edouard Roger-Vasselin (`KXATPDOUBLES-26NOV10MEKROGCASERL-MEKROG`) | 0.62 / 0.67 (106) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
