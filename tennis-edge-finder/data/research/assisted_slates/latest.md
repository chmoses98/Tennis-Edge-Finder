# ASSISTED SLATE -- 2026-11-10T00:03Z (`SL-20261110T000313Z-3f22a257`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

399 open matches not seen started, 896 markets. Skipped: {}. Sources: shadow board 2026-11-09T23:49:18.119779+00:00, Model 4 2026-11-09T23:50:11.763289+00:00, Gen-1 ledger 2026-11-09T23:49:14.912207+00:00, external 2026-11-09T23:15:21.012787+00:00, capture 20261109T231333Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-11-10 12:00Z**
* Recommended RUN TENNIS time: **2026-11-10 11:15Z**
* Final price/status check time: **2026-11-10 11:50Z**
* Number of matches in window: 4 (Adrian Mannarino vs Aleksandr Shevchenko, Alex Michelsen vs Juan Manuel Cerundolo, Tomas Martin Etcheverry vs Thiago Agustin Tirante, Lorenzo Sonego vs Quentin Halys)

Slate built 2026-11-10T00:03Z. Refresh due by: 2026-11-10 11:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 67, "HIGH_REVIEW": 89, "NORMAL": 294, "REVIEW": 114, "UNPRICED": 332}; match winners: {"EXTREME": 66, "HIGH_REVIEW": 85, "NORMAL": 221, "REVIEW": 94, "UNPRICED": 332}; quote freshness at build: {"AGING": 564}.

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
| Liam Broady (`KXATPCHALLENGERMATCH-26NOV08HARBRO-BRO`) | 0.08 / 0.09 (36365) | 8.5% | 51.1% | 72.7% | 68.8% [61.9%-71.9%] | 44.6% | -- | 44.6% | MODEL_LONE_OUTLIER | WATCH | +42.6 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Billy Harris (`KXATPCHALLENGERMATCH-26NOV08HARBRO-HAR`) | 0.91 / 0.92 (32150) | 91.5% | 48.9% | 27.3% | 31.1% [28.1%-38.1%] | 55.4% | -- | 55.4% | MODEL_LONE_OUTLIER | PASS | -42.6 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 5763.0, B 4666.0; serve-point win A 62.5%, B 37.3%; Elo A 1614.3, B 1640.6; model uncertainty 0.0499
* Form inputs: days since last match A 13, B 13; matches on record A 638, B 951; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV08HARBRO-BRO  (YES = Liam Broady)
Model: 51%
Kalshi: 8%
Gap: +43 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.009, surface_dev_loose -0.004, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

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
| Marco Cecchinato (`KXATPCHALLENGERMATCH-26NOV09CECCOM-CEC`) | 0.39 / 0.44 (3) | 41.5% | 40.2% | 53.0% | 49.0% [44.5%-51.5%] | -- | -- | -- | -- | WATCH | -1.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Francisco Comesana (`KXATPCHALLENGERMATCH-26NOV09CECCOM-COM`) | 0.55 / 0.57 (0) | 56.0% | 59.8% | 47.0% | 51.0% [48.5%-55.5%] | -- | -- | -- | -- | PASS | +3.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5798.0, B 5187.0; serve-point win A 62.0%, B 36.0%; Elo A 1694.4, B 1795.1; model uncertainty 0.0351
* Form inputs: days since last match A 7, B 7; matches on record A 998, B 466; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.015, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

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
| Duncan Chan (`KXATPCHALLENGERMATCH-26NOV09DRACHA-CHA`) | 0.01 / 0.02 (24119) | 1.5% | 16.4% | 19.8% | 16.1% [15.2%-17.1%] | 25.0% | 22.6% | 23.8% | MODEL_LONE_OUTLIER | WATCH | +14.9 pp | REVIEW | AGING | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Liam Draxl (`KXATPCHALLENGERMATCH-26NOV09DRACHA-DRA`) | 0.98 / 0.99 (4343) | 98.5% | 83.6% | 80.2% | 83.9% [82.9%-84.8%] | 75.0% | 77.3% | 76.1% | MODEL_LONE_OUTLIER | PASS | -14.9 pp | REVIEW | AGING | C / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 4913.0, B 890.0; serve-point win A 64.4%, B 43.2%; Elo A 1731.9, B 1418.0; model uncertainty 0.0094
* Form inputs: days since last match A 7, B 42; matches on record A 379, B 28; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.003, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER

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
| Alexis Galarneau (`KXATPCHALLENGERMATCH-26NOV09GALKOZ-GAL`) | 0.41 / 0.43 (56) | 42.0% | 44.7% | 37.8% | 43.3% [40.7%-46.4%] | -- | -- | -- | -- | PASS | +2.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefan Kozlov (`KXATPCHALLENGERMATCH-26NOV09GALKOZ-KOZ`) | 0.56 / 0.59 (8) | 57.5% | 55.3% | 62.2% | 56.7% [53.6%-59.3%] | -- | -- | -- | -- | PASS | -2.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5286.0, B 3794.0; serve-point win A 58.9%, B 40.1%; Elo A 1665.3, B 1616.3; model uncertainty 0.0282
* Form inputs: days since last match A 7, B 7; matches on record A 439, B 624; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.010, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

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
| Marcos Giron (`KXATPCHALLENGERMATCH-26NOV09GIRKAS-GIR`) | 0.64 / 0.66 (505) | 65.0% | 57.4% | 41.1% | 48.5% [45.1%-53.0%] | -- | -- | -- | -- | PASS | -7.6 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maks Kasnikowski (`KXATPCHALLENGERMATCH-26NOV09GIRKAS-KAS`) | 0.34 / 0.37 (0) | 35.5% | 42.6% | 58.9% | 51.5% [47.0%-54.9%] | -- | -- | -- | -- | PASS | +7.1 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4834.0, B 5094.0; serve-point win A 65.2%, B 36.3%; Elo A 1783.5, B 1627.3; model uncertainty 0.0396
* Form inputs: days since last match A 7, B 7; matches on record A 726, B 330; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.015, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

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
| Darwin Blanch (`KXATPCHALLENGERMATCH-26NOV09GRABLA-BLA`) | 0.62 / 0.69 (3) | 65.5% | 64.6% | 46.6% | 51.5% [48.5%-56.4%] | -- | -- | -- | -- | PASS | -0.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alastair Gray (`KXATPCHALLENGERMATCH-26NOV09GRABLA-GRA`) | 0.27 / 0.37 (3) | 32.0% | 35.4% | 53.4% | 48.5% [43.6%-51.5%] | -- | -- | -- | -- | PASS | +3.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3404.0, B 4786.0; serve-point win A 63.9%, B 33.0%; Elo A 1582.8, B 1676.5; model uncertainty 0.0392
* Form inputs: days since last match A 7, B 7; matches on record A 328, B 183; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Zdenek Kolar (`KXATPCHALLENGERMATCH-26NOV09KOLREI-KOL`) | 0.23 / 0.29 (2) | 26.0% | 37.5% | 44.9% | 44.4% [43.8%-45.4%] | -- | -- | -- | -- | PASS | +11.5 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joao Lucas Reis Da Silva (`KXATPCHALLENGERMATCH-26NOV09KOLREI-REI`) | 0.67 / 0.73 (3) | 70.0% | 62.5% | 55.1% | 55.6% [54.6%-56.2%] | -- | -- | -- | -- | PASS | -7.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5408.0, B 5010.0; serve-point win A 58.9%, B 38.7%; Elo A 1614.3, B 1671.7; model uncertainty 0.0077
* Form inputs: days since last match A 7, B 7; matches on record A 839, B 485; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

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
| Clement Chidekh (`KXATPCHALLENGERMATCH-26NOV09LATCHI-CHI`) | 0.94 / 0.95 (40243) | 94.5% | 96.5% | 94.3% | 93.2% [92.1%-93.8%] | 92.7% | 95.3% | 94.0% | MODEL_LONE_OUTLIER | PASS | +2.0 pp | NORMAL | AGING | F / POOR | ALL_AGREE | VERIFIED |
| Marcel Latak (`KXATPCHALLENGERMATCH-26NOV09LATCHI-LAT`) | 0.05 / 0.06 (3284) | 5.5% | 3.5% | 5.7% | 6.8% [6.2%-7.9%] | 7.3% | 4.6% | 6.0% | MODEL_LONE_OUTLIER | PASS | -2.0 pp | NORMAL | AGING | F / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 53.0, B 5095.0; serve-point win A 53.5%, B 32.4%; Elo A 1285.9, B 1736.3; model uncertainty 0.0086
* Form inputs: days since last match A 301, B 7; matches on record A 1, B 334; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.006, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER

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
| Aidan Mayo (`KXATPCHALLENGERMATCH-26NOV09MAYMMO-MAY`) | 0.51 / 0.54 (0) | 52.5% | 42.7% | 60.5% | 51.5% [46.5%-55.5%] | -- | -- | -- | -- | PASS | -9.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Michael Mmoh (`KXATPCHALLENGERMATCH-26NOV09MAYMMO-MMO`) | 0.45 / 0.48 (8) | 46.5% | 57.3% | 39.5% | 48.5% [44.5%-53.5%] | -- | -- | -- | -- | PASS | +10.8 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4152.0, B 3733.0; serve-point win A 61.7%, B 36.8%; Elo A 1595.7, B 1744.1; model uncertainty 0.0454
* Form inputs: days since last match A 7, B 21; matches on record A 265, B 575; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.015, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

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
| Elmer Moller (`KXATPCHALLENGERMATCH-26NOV09MOLOLI-MOL`) | 0.63 / 0.68 (1) | 65.5% | 64.4% | 67.0% | 67.0% [66.5%-68.0%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Genaro Alberto Olivieri (`KXATPCHALLENGERMATCH-26NOV09MOLOLI-OLI`) | 0.30 / 0.34 (0) | 32.0% | 35.6% | 33.0% | 33.0% [32.0%-33.5%] | -- | -- | -- | -- | PASS | +3.6 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4747.0, B 5176.0; serve-point win A 55.1%, B 47.7%; Elo A 1728.0, B 1588.2; model uncertainty 0.0074
* Form inputs: days since last match A 7, B 7; matches on record A 316, B 613; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

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
| Abdullah Shelbayh (`KXATPCHALLENGERMATCH-26NOV09SHEWEN-SHE`) | 0.45 / 0.50 (53) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Harry Wendelken (`KXATPCHALLENGERMATCH-26NOV09SHEWEN-WEN`) | 0.46 / 0.51 (0) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

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
| Andres Andrade (`KXATPCHALLENGERMATCH-26NOV09SHIAND-AND`) | 0.33 / 0.36 (0) | 34.5% | 64.1% | 57.7% | 60.2% [57.7%-65.0%] | -- | -- | -- | -- | PASS | +29.6 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Braden Shick (`KXATPCHALLENGERMATCH-26NOV09SHIAND-SHI`) | 0.62 / 0.64 (0) | 63.0% | 35.9% | 42.3% | 39.8% [34.9%-42.3%] | -- | -- | -- | -- | PASS | -27.1 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3074.0, B 4899.0; serve-point win A 58.8%, B 38.4%; Elo A 1547.1, B 1656.1; model uncertainty 0.0368
* Form inputs: days since last match A 7, B 7; matches on record A 102, B 306; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV09SHIAND-AND  (YES = Andres Andrade)
Model: 64%
Kalshi: 34%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.020, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

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
| Marcelo Tomas Barrios Vera (`KXATPCHALLENGERMATCH-26NOV09VARBAR-BAR`) | 0.62 / 0.69 (3) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juan Pablo Varillas (`KXATPCHALLENGERMATCH-26NOV09VARBAR-VAR`) | 0.31 / 0.32 (14) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Alex Barrena (`KXATPCHALLENGERMATCH-26NOV09ZAVBAR-BAR`) | 0.96 / 0.97 (550) | 96.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fabio Manuel Zavalaga Uculmana (`KXATPCHALLENGERMATCH-26NOV09ZAVBAR-ZAV`) | 0.03 / 0.04 (249) | 3.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Diogo Morais vs Rodrigo Leal -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-09 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-09T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211587:214259:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigo Leal (`KXITFMATCH-26NOV09MORLEA-LEA`) | 0.39 / 0.40 (551) | 39.5% | 36.4% | 53.6% | 43.8% [42.7%-44.8%] | -- | -- | -- | -- | PASS | -3.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Diogo Morais (`KXITFMATCH-26NOV09MORLEA-MOR`) | 0.59 / 0.60 (80) | 59.5% | 63.6% | 46.4% | 56.2% [55.2%-57.3%] | -- | -- | -- | -- | PASS | +4.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 178.0, B 140.0; serve-point win A 59.8%, B 42.9%; Elo A 1293.4, B 1241.6; model uncertainty 0.0103
* Form inputs: days since last match A 21, B 196; matches on record A 13, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

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
| Martim Bernardo (`KXITFMATCH-26NOV09CURBER-BER`) | 0.08 / 0.10 (8) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tomas Curras Abasolo (`KXITFMATCH-26NOV09CURBER-CUR`) | 0.90 / 0.91 (0) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabriela Dabrowski / Luisa Stefani vs Elise Mertens / Shuai Zhang -- WTA Finals (Women) RR

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-10 02:00Z
* Current expected start: 2026-11-09 23:28Z
* Source: COURT_PROGRESSION: preceding match on Indian Wells Tennis Garden in progress (set 1 of best-of-3); confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-09 22:48Z
* Recommended handicap-by time: 2026-11-09 22:43Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-10T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09DABSTEMERZHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela Dabrowski / Luisa Stefani (`KXWTADOUBLES-26NOV09DABSTEMERZHA-DABSTE`) | 0.68 / 0.71 (12661) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elise Mertens / Shuai Zhang (`KXWTADOUBLES-26NOV09DABSTEMERZHA-MERZHA`) | 0.29 / 0.31 (4791) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Hanyu Guo / Kristina Mladenovic vs Su-Wei Hsieh / Jelena Ostapenko -- WTA Finals (Women) RR

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-10 03:30Z
* Current expected start: 2026-11-10 00:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-09 22:48Z
* Recommended handicap-by time: 2026-11-09 23:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-10T03:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV09GUOMLAHSIOST:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hanyu Guo / Kristina Mladenovic (`KXWTADOUBLES-26NOV09GUOMLAHSIOST-GUOMLA`) | 0.35 / 0.37 (0) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Su-Wei Hsieh / Jelena Ostapenko (`KXWTADOUBLES-26NOV09GUOMLAHSIOST-HSIOST`) | 0.61 / 0.63 (37) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

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
| Henrique Rocha (`KXATPCHALLENGERMATCH-26NOV09TOBROC-ROC`) | 0.45 / 0.46 (24720) | 45.5% | 74.0% | 63.6% | 69.7% [65.5%-82.5%] | -- | -- | -- | -- | PASS | +28.5 pp | EXTREME (DATA_WARNING) | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Miguel Tobon (`KXATPCHALLENGERMATCH-26NOV09TOBROC-TOB`) | 0.54 / 0.55 (93188) | 54.5% | 26.0% | 36.4% | 30.3% [17.5%-34.5%] | -- | -- | -- | -- | PASS | -28.5 pp | EXTREME (DATA_WARNING) | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3281.0, B 4833.0; serve-point win A 58.1%, B 36.9%; Elo A 1454.2, B 1702.9; model uncertainty 0.0851
* Form inputs: days since last match A 106, B 7; matches on record A 423, B 323; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV09TOBROC-ROC  (YES = Henrique Rocha)
Model: 74%
Kalshi: 46%
Gap: +29 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.031, surface_pool_high +0.042, surface_dev_loose +0.009, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

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
| Arklon Huertas Del Pino Cordova (`KXATPCHALLENGERMATCH-26NOV09HUEMID-HUE`) | 0.10 / 0.18 (1) | 14.0% | 11.6% | 14.0% | 13.1% [12.3%-14.6%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Lautaro Midon (`KXATPCHALLENGERMATCH-26NOV09HUEMID-MID`) | 0.80 / 0.85 (11) | 82.5% | 88.4% | 86.0% | 86.9% [85.4%-87.7%] | -- | -- | -- | -- | PASS | +5.9 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1715.0, B 4759.0; serve-point win A 54.1%, B 36.6%; Elo A 1337.4, B 1682.4; model uncertainty 0.0115
* Form inputs: days since last match A 28, B 7; matches on record A 297, B 277; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.009, surface_dev_loose -0.002, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Enzo Aguiard (`KXATPCHALLENGERMATCH-26NOV09AGUSAN-AGU`) | 0.41 / 0.42 (288) | 41.5% | 47.8% | 45.5% | 45.6% [40.2%-49.5%] | 41.6% | 41.9% | 41.9% | MODEL_LONE_OUTLIER | WATCH | +6.3 pp | NORMAL | AGING | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Akira Santillan (`KXATPCHALLENGERMATCH-26NOV09AGUSAN-SAN`) | 0.58 / 0.59 (2604) | 58.5% | 52.2% | 54.5% | 54.4% [50.5%-59.9%] | 58.4% | 58.5% | 58.5% | MODEL_LONE_OUTLIER | PASS | -6.3 pp | NORMAL | AGING | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 1732.0, B 3639.0; serve-point win A 64.2%, B 35.4%; Elo A 1500.5, B 1531.4; model uncertainty 0.0468
* Form inputs: days since last match A 56, B 14; matches on record A 58, B 597; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.034, surface_pool_high +0.040, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

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
| Jake Delaney (`KXATPCHALLENGERMATCH-26NOV09DELSHA-DEL`) | 0.17 / 0.18 (5425) | 17.5% | 13.2% | 32.4% | 22.9% [17.3%-26.4%] | 18.8% | 16.6% | 17.7% | MODEL_LONE_OUTLIER | WATCH | -4.3 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Juncheng Shang (`KXATPCHALLENGERMATCH-26NOV09DELSHA-SHA`) | 0.82 / 0.83 (787) | 82.5% | 86.8% | 67.6% | 77.1% [73.6%-82.7%] | 81.2% | 83.0% | 82.1% | MODEL_LONE_OUTLIER | PASS | +4.3 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3508.0, B 2480.0; serve-point win A 63.0%, B 27.6%; Elo A 1437.8, B 1805.1; model uncertainty 0.0451
* Form inputs: days since last match A 7, B 14; matches on record A 345, B 239; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.015, surface_dev_loose -0.006, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

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
| Charles Broom (`KXATPCHALLENGERMATCH-26NOV09GORBRO-BRO`) | 0.50 / 0.61 (4) | 55.5% | 70.3% | 79.0% | 73.6% [71.9%-75.2%] | -- | -- | -- | -- | WATCH | +14.8 pp | REVIEW | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sebastian Gorzny (`KXATPCHALLENGERMATCH-26NOV09GORBRO-GOR`) | 0.45 / 0.47 (1) | 46.0% | 29.7% | 21.0% | 26.5% [24.8%-28.1%] | -- | -- | -- | -- | PASS | -16.3 pp | HIGH_REVIEW | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1167.0, B 4411.0; serve-point win A 60.9%, B 34.9%; Elo A 1502.6, B 1638.2; model uncertainty 0.0165
* Form inputs: days since last match A 14, B 7; matches on record A 41, B 397; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| August Holmgren (`KXATPCHALLENGERMATCH-26NOV09HOLSEK-HOL`) | 0.63 / 0.64 (2394) | 63.5% | 62.0% | 53.4% | 54.4% [51.9%-59.7%] | 63.1% | 63.1% | 63.1% | MODEL_LONE_OUTLIER | PASS | -1.5 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Philip Sekulic (`KXATPCHALLENGERMATCH-26NOV09HOLSEK-SEK`) | 0.35 / 0.37 (3510) | 36.0% | 38.0% | 46.6% | 45.6% [40.3%-48.0%] | 36.9% | 37.1% | 37.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +2.0 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4476.0, B 4045.0; serve-point win A 67.2%, B 35.3%; Elo A 1609.9, B 1560.3; model uncertainty 0.0387
* Form inputs: days since last match A 7, B 48; matches on record A 320, B 272; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.024, surface_pool_high -0.024, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

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
| Naoya Honda (`KXATPCHALLENGERMATCH-26NOV09HONSAK-HON`) | 0.20 / 0.21 (124) | 20.5% | 20.4% | 20.3% | 18.9% [16.3%-21.0%] | -- | -- | -- | -- | PASS | -0.1 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefanos Sakellaridis (`KXATPCHALLENGERMATCH-26NOV09HONSAK-SAK`) | 0.79 / 0.82 (133) | 80.5% | 79.6% | 79.7% | 81.1% [79.0%-83.7%] | -- | -- | -- | -- | PASS | -0.9 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1597.0, B 4881.0; serve-point win A 61.0%, B 32.3%; Elo A 1365.9, B 1635.4; model uncertainty 0.0237
* Form inputs: days since last match A 14, B 7; matches on record A 72, B 386; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.021, surface_dev_loose -0.003, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

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
| Casey Hoole (`KXATPCHALLENGERMATCH-26NOV09HOORYA-HOO`) | 0.78 / 0.80 (6920) | 79.0% | 77.7% | 66.7% | 74.0% [73.0%-76.0%] | 77.4% | 79.1% | 79.1% | MODEL_LONE_OUTLIER | PASS | -1.3 pp | NORMAL | AGING | F / POOR | EXTERNAL_STALE | VERIFIED |
| Sam Ryan Ziegann (`KXATPCHALLENGERMATCH-26NOV09HOORYA-RYA`) | 0.20 / 0.21 (55) | 20.5% | 22.3% | 33.3% | 26.1% [24.0%-27.0%] | 22.6% | 21.8% | 21.8% | MODEL_LONE_OUTLIER | PASS | +1.8 pp | NORMAL | AGING | F / POOR | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 163.0, B 1167.0; serve-point win A 68.0%, B 38.2%; Elo A 1380.2, B 1190.8; model uncertainty 0.0146
* Form inputs: days since last match A 679, B 63; matches on record A 17, B 87; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.008, surface_dev_loose -0.001, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

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
| Omar Jasika (`KXATPCHALLENGERMATCH-26NOV09JASSUR-JAS`) | 0.49 / 0.50 (4193) | 49.5% | 32.1% | 36.1% | 33.9% [32.6%-35.1%] | 49.0% | 49.4% | 49.4% | MODEL_LONE_OUTLIER | PASS | -17.4 pp | HIGH_REVIEW | AGING | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Dhakshineswar Suresh (`KXATPCHALLENGERMATCH-26NOV09JASSUR-SUR`) | 0.49 / 0.51 (1821) | 50.0% | 67.9% | 63.9% | 66.1% [64.8%-67.4%] | 51.0% | 50.4% | 50.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +17.9 pp | HIGH_REVIEW | AGING | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4159.0, B 1964.0; serve-point win A 64.0%, B 32.2%; Elo A 1530.4, B 1674.1; model uncertainty 0.0129
* Form inputs: days since last match A 7, B 75; matches on record A 523, B 91; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV09JASSUR-SUR  (YES = Dhakshineswar Suresh)
Model: 68%
Kalshi: 50%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: EXTERNAL_STALE
Data quality: A (LIMITED)
Reasons: STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.004, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

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
| Jan Kumstat (`KXATPCHALLENGERMATCH-26NOV09MCCKUM-KUM`) | 0.65 / 0.66 (6159) | 65.5% | 68.1% | 66.1% | 63.0% [59.4%-67.4%] | -- | -- | -- | -- | PASS | +2.6 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| James McCabe (`KXATPCHALLENGERMATCH-26NOV09MCCKUM-MCC`) | 0.34 / 0.35 (285) | 34.5% | 31.9% | 33.9% | 37.0% [32.6%-40.6%] | -- | -- | -- | -- | PASS | -2.6 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4552.0, B 3055.0; serve-point win A 66.7%, B 29.3%; Elo A 1579.4, B 1631.9; model uncertainty 0.0401
* Form inputs: days since last match A 7, B 7; matches on record A 336, B 89; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.044, surface_pool_high +0.036, surface_dev_loose +0.010, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

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
| David Jorda Sanchis (`KXATPCHALLENGERMATCH-26NOV09NAKJOR-JOR`) | 0.78 / 0.80 (8795) | 79.0% | 74.2% | 71.9% | 72.7% [66.6%-78.6%] | 77.7% | 78.5% | 78.5% | MODEL_LONE_OUTLIER | PASS | -4.8 pp | NORMAL | AGING | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Shunsuke Nakagawa (`KXATPCHALLENGERMATCH-26NOV09NAKJOR-NAK`) | 0.20 / 0.21 (133) | 20.5% | 25.8% | 28.1% | 27.3% [21.4%-33.4%] | 22.3% | 21.4% | 21.4% | MODEL_LONE_OUTLIER | WATCH | +5.3 pp | NORMAL | AGING | B / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 1170.0, B 5329.0; serve-point win A 60.2%, B 34.6%; Elo A 1333.8, B 1504.2; model uncertainty 0.0601
* Form inputs: days since last match A 105, B 42; matches on record A 56, B 469; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.048, surface_pool_high +0.061, surface_dev_loose +0.004, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

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
| Florian Broska (`KXATPCHALLENGERMATCH-26NOV09OVEBRO-BRO`) | 0.39 / 0.41 (848) | 40.0% | 52.3% | 41.2% | 47.5% [44.6%-50.0%] | 40.8% | 41.0% | 41.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +12.3 pp | REVIEW | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Carl Emil Overbeck (`KXATPCHALLENGERMATCH-26NOV09OVEBRO-OVE`) | 0.59 / 0.60 (2175) | 59.5% | 47.7% | 58.8% | 52.5% [50.0%-55.4%] | 59.2% | 59.0% | 59.0% | MODEL_LONE_OUTLIER | PASS | -11.8 pp | REVIEW | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2038.0, B 3363.0; serve-point win A 64.8%, B 34.8%; Elo A 1505.2, B 1544.8; model uncertainty 0.027
* Form inputs: days since last match A 7, B 28; matches on record A 85, B 218; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

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
| Cruz Hewitt (`KXATPCHALLENGERMATCH-26NOV09SCHHEW-HEW`) | 0.23 / 0.25 (2407) | 24.0% | 29.4% | 27.7% | 27.3% [26.4%-28.1%] | 26.0% | 23.0% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +5.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tristan Schoolkate (`KXATPCHALLENGERMATCH-26NOV09SCHHEW-SCH`) | 0.75 / 0.77 (1607) | 76.0% | 70.6% | 72.3% | 72.7% [71.9%-73.6%] | 74.0% | 74.6% | -- | INSUFFICIENT_INPUTS | PASS | -5.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6081.0, B 2605.0; serve-point win A 69.2%, B 35.3%; Elo A 1695.1, B 1521.7; model uncertainty 0.0086
* Form inputs: days since last match A 14, B 21; matches on record A 423, B 79; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.008, surface_dev_loose -0.000, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

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
| Anton Shepp (`KXATPCHALLENGERMATCH-26NOV09SWESHE-SHE`) | 0.30 / 0.31 (1465) | 30.5% | 30.0% | 48.5% | 37.2% [31.1%-42.0%] | -- | 31.1% | 31.1% | MODEL_LONE_OUTLIER | WATCH | -0.5 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Dane Sweeny (`KXATPCHALLENGERMATCH-26NOV09SWESHE-SWE`) | 0.69 / 0.70 (493) | 69.5% | 70.0% | 51.5% | 62.8% [58.0%-68.8%] | -- | 69.0% | 69.0% | MODEL_LONE_OUTLIER | PASS | +0.5 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5456.0, B 2073.0; serve-point win A 65.4%, B 38.8%; Elo A 1650.8, B 1440.8; model uncertainty 0.0545
* Form inputs: days since last match A 28, B 50; matches on record A 432, B 69; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

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
| Taro Daniel (`KXATPCHALLENGERMATCH-26NOV09WATDAN-DAN`) | 0.41 / 0.42 (1371) | 41.5% | 32.6% | 46.0% | 45.1% [41.1%-51.0%] | 42.8% | 42.2% | 42.2% | MODEL_LONE_OUTLIER | WATCH | -8.8 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Yosuke Watanuki (`KXATPCHALLENGERMATCH-26NOV09WATDAN-WAT`) | 0.58 / 0.59 (524) | 58.5% | 67.3% | 54.0% | 54.9% [49.0%-58.9%] | 57.2% | 58.2% | 58.2% | MODEL_LONE_OUTLIER | PASS | +8.8 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3355.0, B 4270.0; serve-point win A 66.2%, B 37.4%; Elo A 1717.1, B 1663.2; model uncertainty 0.0492
* Form inputs: days since last match A 7, B 14; matches on record A 454, B 1068; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.040, surface_pool_high +0.039, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Jessica Marmorstein vs Sydney-Nicole Clarke -- W50 Chihuahua R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221478:264013:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sydney-Nicole Clarke (`KXITFWMATCH-26NOV09MARCLA-CLA`) | 0.46 / 0.51 (80) | 48.5% | 56.7% | 31.5% | 56.4% [53.2%-57.4%] | -- | -- | -- | -- | PASS | +8.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jessica Marmorstein (`KXITFWMATCH-26NOV09MARCLA-MAR`) | 0.49 / 0.53 (27) | 51.0% | 43.3% | 68.5% | 43.6% [42.6%-46.8%] | -- | -- | -- | -- | PASS | -7.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 71.0, B 65.0; serve-point win A 52.6%, B 46.2%; Elo A 1177.4, B 1225.7; model uncertainty 0.0211
* Form inputs: days since last match A 490, B 343; matches on record A 52, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
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
| Naoya Honda (`KXATPCHALLENGERMATCH-26NOV09HONTSE-HON`) | 0.25 / 0.26 (124) | 25.5% | 20.7% | 23.6% | 21.7% [16.6%-26.0%] | 28.4% | 26.9% | 26.9% | MODEL_LONE_OUTLIER | PASS | -4.8 pp | NORMAL | AGING | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Chun Hsin Tseng (`KXATPCHALLENGERMATCH-26NOV09HONTSE-TSE`) | 0.73 / 0.75 (2261) | 74.0% | 79.3% | 76.4% | 78.3% [74.0%-83.4%] | 71.6% | 73.3% | 73.3% | MODEL_LONE_OUTLIER | WATCH | +5.3 pp | NORMAL | AGING | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 1597.0, B 4916.0; serve-point win A 59.7%, B 33.9%; Elo A 1365.9, B 1606.3; model uncertainty 0.047
* Form inputs: days since last match A 14, B 7; matches on record A 72, B 519; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.038, surface_pool_high +0.043, surface_dev_loose +0.001, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Mili Poljicak (`KXATPCHALLENGERMATCH-26NOV09POLUCH-POL`) | 0.64 / 0.65 (24) | 64.5% | 63.2% | 55.9% | 56.3% [55.3%-57.3%] | 63.1% | 65.0% | 65.0% | MODEL_LONE_OUTLIER | PASS | -1.3 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Kaichi Uchida (`KXATPCHALLENGERMATCH-26NOV09POLUCH-UCH`) | 0.34 / 0.35 (239) | 34.5% | 36.8% | 44.1% | 43.7% [42.7%-44.7%] | 36.9% | 35.5% | 35.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +2.3 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3404.0, B 4273.0; serve-point win A 67.1%, B 35.7%; Elo A 1538.8, B 1489.3; model uncertainty 0.0099
* Form inputs: days since last match A 7, B 14; matches on record A 282, B 836; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Ognjen Milic (`KXATPCHALLENGERMATCH-26NOV09SHIMIL-MIL`) | 0.55 / 0.56 (2495) | 55.5% | 62.8% | 60.0% | 60.5% [60.0%-61.5%] | 55.4% | 55.4% | 55.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.3 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Hikaru Shiraishi (`KXATPCHALLENGERMATCH-26NOV09SHIMIL-SHI`) | 0.44 / 0.45 (3548) | 44.5% | 37.2% | 40.0% | 39.5% [38.5%-40.0%] | 44.6% | 44.9% | 44.9% | MODEL_LONE_OUTLIER | PASS | -7.3 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2976.0, B 3142.0; serve-point win A 60.9%, B 36.5%; Elo A 1438.1, B 1527.6; model uncertainty 0.0072
* Form inputs: days since last match A 56, B 14; matches on record A 210, B 103; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.009, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Allegre / Avataneo (`KXITFWDOUBLES-26NOV09ALLAVACASREY-ALLAVA`) | 0.98 / 0.99 (687) | 98.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Castillo Meza / Reyes Romero (`KXITFWDOUBLES-26NOV09ALLAVACASREY-CASREY`) | -- / 0.01 (1198) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

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
| Sara Lillian Chavez (`KXITFWMATCH-26NOV09REGCHA-CHA`) | 0.81 / 0.82 (14020) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fernanda Guadalupe Regalado Macias (`KXITFWMATCH-26NOV09REGCHA-REG`) | 0.18 / 0.19 (2131) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
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
| Moerani Bouzige (`KXATPCHALLENGERMATCH-26NOV09BOUOCO-BOU`) | 0.12 / 0.14 (6378) | 13.0% | 16.8% | 38.5% | 26.7% [18.5%-31.3%] | 15.6% | 12.0% | 15.6% | KALSHI_LONE_OUTLIER | SHADOW_BET | +3.8 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |
| Christopher O'Connell (`KXATPCHALLENGERMATCH-26NOV09BOUOCO-OCO`) | 0.87 / 0.88 (12374) | 87.5% | 83.2% | 61.5% | 73.3% [68.7%-81.5%] | 84.4% | 87.5% | 84.4% | KALSHI_LONE_OUTLIER | PASS | -4.3 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3261.0, B 2972.0; serve-point win A 62.2%, B 29.9%; Elo A 1424.3, B 1800.7; model uncertainty 0.0641
* Form inputs: days since last match A 56, B 73; matches on record A 315, B 319; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.005, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

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
| Matthew Dellavedova (`KXATPCHALLENGERMATCH-26NOV09DELFAN-DEL`) | 0.80 / 0.81 (5100) | 80.5% | 62.9% | 58.3% | 58.8% [57.4%-59.7%] | 78.0% | 81.0% | 81.0% | MODEL_LONE_OUTLIER | PASS | -17.6 pp | HIGH_REVIEW | AGING | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Thomas Fancutt (`KXATPCHALLENGERMATCH-26NOV09DELFAN-FAN`) | 0.18 / 0.19 (89) | 18.5% | 37.1% | 41.7% | 41.2% [40.3%-42.6%] | 22.0% | 19.3% | 19.3% | MODEL_LONE_OUTLIER | WATCH | +18.6 pp | HIGH_REVIEW | AGING | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3884.0, B 1210.0; serve-point win A 66.9%, B 35.8%; Elo A 1455.0, B 1389.7; model uncertainty 0.0116
* Form inputs: days since last match A 48, B 56; matches on record A 451, B 431; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV09DELFAN-FAN  (YES = Thomas Fancutt)
Model: 37%
Kalshi: 18%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: EXTERNAL_STALE
Data quality: B (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.009, surface_dev_loose -0.001, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Shintaro Imai (`KXATPCHALLENGERMATCH-26NOV09IMASUN-IMA`) | 0.31 / 0.33 (4824) | 32.0% | 35.1% | 50.0% | 46.0% [45.0%-48.0%] | 32.9% | 32.0% | 32.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.1 pp | NORMAL | AGING | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Fajing Sun (`KXATPCHALLENGERMATCH-26NOV09IMASUN-SUN`) | 0.67 / 0.68 (426) | 67.5% | 64.9% | 50.0% | 54.0% [52.0%-55.0%] | 67.1% | 68.3% | 68.3% | MODEL_LONE_OUTLIER | PASS | -2.6 pp | NORMAL | AGING | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 1292.0, B 4332.0; serve-point win A 62.2%, B 34.7%; Elo A 1507.2, B 1555.7; model uncertainty 0.015
* Form inputs: days since last match A 14, B 14; matches on record A 461, B 528; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Koki Matsuda (`KXATPCHALLENGERMATCH-26NOV09MCDMAT-MAT`) | 0.46 / 0.48 (1441) | 47.0% | 48.5% | 60.9% | 59.9% [55.5%-62.3%] | 46.9% | 47.2% | 47.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +1.5 pp | NORMAL | AGING | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Niels McDonald (`KXATPCHALLENGERMATCH-26NOV09MCDMAT-MCD`) | 0.52 / 0.53 (124) | 52.5% | 51.5% | 39.1% | 40.1% [37.7%-44.5%] | 53.1% | 53.5% | 53.5% | MODEL_LONE_OUTLIER | PASS | -1.0 pp | NORMAL | AGING | B / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2065.0, B 2859.0; serve-point win A 63.7%, B 36.6%; Elo A 1396.0, B 1460.2; model uncertainty 0.0339
* Form inputs: days since last match A 70, B 14; matches on record A 41, B 147; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.024, surface_dev_loose -0.009, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Rei Sakamoto (`KXATPCHALLENGERMATCH-26NOV09SAKTOK-SAK`) | 0.85 / 0.86 (5777) | 85.5% | 79.4% | 56.3% | 67.1% [62.5%-75.9%] | 82.9% | 84.4% | 83.7% | MODEL_LONE_OUTLIER | PASS | -6.1 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Renta Tokuda (`KXATPCHALLENGERMATCH-26NOV09SAKTOK-TOK`) | 0.14 / 0.15 (598) | 14.5% | 20.6% | 43.7% | 32.9% [24.1%-37.5%] | 17.1% | 15.8% | 16.5% | MODEL_LONE_OUTLIER | WATCH | +6.1 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4519.0, B 2892.0; serve-point win A 69.0%, B 37.7%; Elo A 1784.3, B 1509.6; model uncertainty 0.0671
* Form inputs: days since last match A 14, B 189; matches on record A 190, B 426; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.004, surface_dev_loose +0.004, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

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
| Isaac Becroft (`KXATPCHALLENGERMATCH-26NOV09GORBEC-BEC`) | 0.27 / 0.28 (493) | 27.5% | 22.2% | 29.2% | 26.6% [25.4%-27.9%] | 29.4% | 28.3% | 28.3% | MODEL_LONE_OUTLIER | PASS | -5.3 pp | NORMAL | AGING | C / LIMITED | EXTERNAL_STALE | VERIFIED |
| Sebastian Gorzny (`KXATPCHALLENGERMATCH-26NOV09GORBEC-GOR`) | 0.71 / 0.72 (1329) | 71.5% | 77.8% | 70.8% | 73.4% [72.1%-74.6%] | 70.6% | 73.0% | 73.0% | MODEL_LONE_OUTLIER | PASS | +6.3 pp | NORMAL | AGING | C / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 1167.0, B 1698.0; serve-point win A 64.7%, B 41.3%; Elo A 1502.6, B 1311.2; model uncertainty 0.0129
* Form inputs: days since last match A 14, B 196; matches on record A 41, B 106; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.008, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

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
| Kasidit Samrej (`KXATPCHALLENGERMATCH-26NOV09SAMSHI-SAM`) | 0.33 / 0.34 (1712) | 33.5% | 45.2% | 49.5% | 48.5% [47.0%-49.5%] | 35.4% | 34.4% | 34.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +11.7 pp | REVIEW | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Yuta Shimizu (`KXATPCHALLENGERMATCH-26NOV09SAMSHI-SHI`) | 0.66 / 0.67 (4955) | 66.5% | 54.8% | 50.5% | 51.5% [50.5%-53.0%] | 64.6% | 65.9% | 65.9% | MODEL_LONE_OUTLIER | PASS | -11.7 pp | REVIEW | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4164.0, B 4313.0; serve-point win A 63.5%, B 35.5%; Elo A 1584.5, B 1601.4; model uncertainty 0.0124
* Form inputs: days since last match A 7, B 7; matches on record A 298, B 474; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Sakura Hosogi (`KXITFWMATCH-26NOV09HOSKIN-HOS`) | 0.41 / 0.44 (132) | 42.5% | 33.0% | 23.2% | 31.1% [27.9%-37.5%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.5 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hayu Kinoshita (`KXITFWMATCH-26NOV09HOSKIN-KIN`) | 0.56 / 0.58 (35) | 57.0% | 67.0% | 76.8% | 68.9% [62.5%-72.1%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.0 pp | REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2576.0, B 3494.0; serve-point win A 53.6%, B 43.1%; Elo A 1583.4, B 1614.1; model uncertainty 0.0477
* Form inputs: days since last match A 196, B 9; matches on record A 392, B 177; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.028, surface_pool_high +0.024, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
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
| Hiromi Abe (`KXITFWMATCH-26NOV09JEOABE-ABE`) | 0.74 / 0.75 (100) | 74.5% | 58.3% | 40.5% | 46.8% [42.5%-60.1%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.2 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| BoYoung Jeong (`KXITFWMATCH-26NOV09JEOABE-JEO`) | 0.23 / 0.24 (124) | 23.5% | 41.7% | 59.5% | 53.2% [40.0%-57.5%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +18.2 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2517.0, B 2555.0; serve-point win A 52.1%, B 46.3%; Elo A 1565.2, B 1619.2; model uncertainty 0.0875
* Form inputs: days since last match A 51, B 238; matches on record A 221, B 200; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV09JEOABE-JEO  (YES = BoYoung Jeong)
Model: 42%
Kalshi: 24%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.032, surface_pool_high +0.027, surface_dev_loose +0.011, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
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
| Aoi Ito (`KXITFWMATCH-26NOV09LEEITO-ITO`) | 0.38 / 0.40 (33) | 39.0% | 37.6% | 18.8% | 28.0% [23.7%-38.5%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carol Young Suh Lee (`KXITFWMATCH-26NOV09LEEITO-LEE`) | 0.58 / 0.60 (28) | 59.0% | 62.4% | 81.2% | 72.0% [61.5%-76.3%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4047.0, B 2722.0; serve-point win A 57.4%, B 45.0%; Elo A 1774.5, B 1759.4; model uncertainty 0.0738
* Form inputs: days since last match A 7, B 16; matches on record A 160, B 304; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose +0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
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
| Takuya Kumasaka (`KXATPCHALLENGERMATCH-26NOV09KUMZHO-KUM`) | 0.21 / 0.22 (482) | 21.5% | 20.6% | 29.8% | 27.2% [25.5%-28.0%] | 24.3% | 23.9% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | -0.9 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yi Zhou (`KXATPCHALLENGERMATCH-26NOV09KUMZHO-ZHO`) | 0.77 / 0.78 (26) | 77.5% | 79.4% | 70.2% | 72.8% [72.0%-74.5%] | 75.7% | 76.1% | -- | INSUFFICIENT_INPUTS | PASS | +1.9 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3065.0, B 3814.0; serve-point win A 59.3%, B 34.2%; Elo A 1411.9, B 1635.1; model uncertainty 0.0125
* Form inputs: days since last match A 91, B 14; matches on record A 226, B 182; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.012, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Ryuki Matsuda (`KXATPCHALLENGERMATCH-26NOV09MATSCH-MAT`) | 0.17 / 0.18 (3922) | 17.5% | 13.4% | 15.1% | 16.6% [15.4%-17.8%] | 19.7% | 17.8% | 17.8% | MARKETS_AGREE | PASS | -4.2 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Max Schoenhaus (`KXATPCHALLENGERMATCH-26NOV09MATSCH-SCH`) | 0.84 / 0.85 (21380) | 84.5% | 86.7% | 84.9% | 83.4% [82.2%-84.6%] | 80.3% | 83.0% | 83.0% | MODEL_LONE_OUTLIER | PASS | +2.1 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2640.0, B 3062.0; serve-point win A 59.7%, B 31.4%; Elo A 1299.6, B 1553.2; model uncertainty 0.0124
* Form inputs: days since last match A 56, B 20; matches on record A 263, B 98; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.012, surface_pool_high +0.013, surface_dev_loose -0.011, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Ymerali Ibraimi (`KXATPCHALLENGERMATCH-26NOV09LANIBR-IBR`) | 0.14 / 0.15 (1) | 14.5% | 21.9% | 24.2% | 26.2% [23.5%-27.9%] | 17.1% | 15.2% | 17.1% | KALSHI_LONE_OUTLIER | PASS | +7.5 pp | NORMAL | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Christian Langmo (`KXATPCHALLENGERMATCH-26NOV09LANIBR-LAN`) | 0.84 / 0.86 (4203) | 85.0% | 78.0% | 75.8% | 73.8% [72.1%-76.5%] | 82.9% | 84.8% | 83.9% | MODEL_LONE_OUTLIER | PASS | -7.0 pp | NORMAL | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3910.0, B 660.0; serve-point win A 67.1%, B 39.1%; Elo A 1486.3, B 1311.9; model uncertainty 0.0221
* Form inputs: days since last match A 14, B 231; matches on record A 445, B 11; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.004, surface_dev_loose +0.008, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; THIN_DISPLAYED_SIZE

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
| Jayson Blando (`KXITFMATCH-26NOV09BLAMIN-BLA`) | 0.36 / 0.40 (5) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ryo Minakata (`KXITFMATCH-26NOV09BLAMIN-MIN`) | 0.62 / 0.63 (200) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Kazuma Kawachi (`KXITFMATCH-26NOV09KAWNIC-KAW`) | 0.60 / 0.63 (18) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Darcy Nicholls (`KXITFMATCH-26NOV09KAWNIC-NIC`) | 0.35 / 0.41 (808) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Daniel Michalski (`KXATPCHALLENGERMATCH-26NOV09NOGMIC-MIC`) | 0.46 / 0.48 (4480) | 47.0% | 42.8% | 50.0% | 46.4% [43.8%-47.9%] | 46.9% | 46.6% | 46.6% | MODEL_LONE_OUTLIER | PASS | -4.2 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Rio Noguchi (`KXATPCHALLENGERMATCH-26NOV09NOGMIC-NOG`) | 0.52 / 0.54 (750) | 53.0% | 57.2% | 50.0% | 53.6% [52.1%-56.2%] | 53.1% | 53.6% | 53.6% | MODEL_LONE_OUTLIER | PASS | +4.2 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4350.0, B 3390.0; serve-point win A 59.0%, B 42.4%; Elo A 1603.5, B 1512.0; model uncertainty 0.0207
* Form inputs: days since last match A 14, B 7; matches on record A 575, B 490; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Darrshan Suresh (`KXITFMATCH-26NOV09TRISUR-SUR`) | 0.20 / 0.23 (4) | 21.5% | 46.7% | 31.6% | 47.9% [44.9%-50.0%] | -- | -- | -- | -- | PASS | +25.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gunawan Trismuwantara (`KXITFMATCH-26NOV09TRISUR-TRI`) | 0.76 / 0.81 (658) | 78.5% | 53.3% | 68.4% | 52.1% [50.0%-55.1%] | -- | -- | -- | -- | PASS | -25.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 301.0, B 602.0; serve-point win A 60.3%, B 40.4%; Elo A 1067.7, B 1076.4; model uncertainty 0.0257
* Form inputs: days since last match A 357, B 196; matches on record A 24, B 31; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09TRISUR-SUR  (YES = Darrshan Suresh)
Model: 47%
Kalshi: 22%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Shaheed Alam (`KXITFMATCH-26NOV09VISALA-ALA`) | 0.16 / 0.19 (35) | 17.5% | 34.5% | 20.9% | 32.3% [29.5%-33.9%] | -- | -- | -- | -- | PASS | +17.0 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Azuma Visaya (`KXITFMATCH-26NOV09VISALA-VIS`) | 0.78 / 0.83 (13) | 80.5% | 65.5% | 79.1% | 67.7% [66.1%-70.5%] | -- | -- | -- | -- | PASS | -15.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 253.0, B 112.0; serve-point win A 59.7%, B 43.3%; Elo A 1230.0, B 1109.9; model uncertainty 0.0221
* Form inputs: days since last match A 350, B 455; matches on record A 11, B 17; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09VISALA-ALA  (YES = Shaheed Alam)
Model: 34%
Kalshi: 18%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Tin Chen (`KXITFMATCH-26NOV09VUXCHE-CHE`) | 0.64 / 0.72 (9) | 68.0% | 62.3% | 78.7% | 60.3% [59.2%-62.4%] | -- | -- | -- | -- | PASS | -5.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ha Minh Duc Vu (`KXITFMATCH-26NOV09VUXCHE-VUX`) | 0.30 / 0.34 (406) | 32.0% | 37.7% | 21.3% | 39.7% [37.6%-40.8%] | -- | -- | -- | -- | PASS | +5.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 335.0, B 0.0; serve-point win A 57.5%, B 40.1%; Elo A 1113.0, B 1186.6; model uncertainty 0.0156
* Form inputs: days since last match A 56, B 1288; matches on record A 26, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.020, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Konstantinos Loukopoulos (`KXITFMATCH-26NOV09YAMLOU-LOU`) | 0.24 / 0.29 (100) | 26.5% | 36.5% | 30.3% | 41.8% [40.9%-42.8%] | -- | -- | -- | -- | PASS | +10.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Natsuki Yamamoto (`KXITFMATCH-26NOV09YAMLOU-YAM`) | 0.69 / 0.72 (12) | 70.5% | 63.5% | 69.7% | 58.2% [57.2%-59.1%] | -- | -- | -- | -- | PASS | -7.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 133.0, B 91.0; serve-point win A 61.9%, B 40.7%; Elo A 1270.8, B 1220.6; model uncertainty 0.0099
* Form inputs: days since last match A 210, B 343; matches on record A 2, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Beck / Sibai (`KXITFWDOUBLES-26NOV09BECSIBBENKOK-BECSIB`) | 0.39 / 0.78 (4) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bennemann / Kokkinis (`KXITFWDOUBLES-26NOV09BECSIBBENKOK-BENKOK`) | 0.44 / 0.81 (2) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Broadus / Ivanov (`KXITFWDOUBLES-26NOV09BROIVAWEIYUA-BROIVA`) | 0.06 / 0.89 (56) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Wei / Yuan (`KXITFWDOUBLES-26NOV09BROIVAWEIYUA-WEIYUA`) | 0.06 / 0.89 (56) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Tiana Tian Deng (`KXITFWMATCH-26NOV09DENWAN-DEN`) | 0.37 / 0.39 (2056) | 38.0% | 26.8% | 28.2% | 30.1% [28.2%-31.5%] | -- | -- | -- | -- | PASS | -11.2 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuhan Wang (`KXITFWMATCH-26NOV09DENWAN-WAN`) | 0.59 / 0.60 (62) | 59.5% | 73.2% | 71.8% | 69.9% [68.5%-71.8%] | -- | -- | -- | -- | WATCH | +13.8 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 853.0, B 1724.0; serve-point win A 50.8%, B 44.5%; Elo A 1288.7, B 1428.1; model uncertainty 0.0163
* Form inputs: days since last match A 126, B 39; matches on record A 41, B 44; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.014, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Merel Hoedt (`KXITFWMATCH-26NOV09HOEHUA-HOE`) | 0.22 / 0.24 (26) | 23.0% | 40.0% | 42.1% | 42.6% [39.5%-47.9%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +17.0 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yujia Huang (`KXITFWMATCH-26NOV09HOEHUA-HUA`) | 0.75 / 0.79 (193) | 77.0% | 60.0% | 57.9% | 57.4% [52.1%-60.5%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -17.0 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2333.0, B 1640.0; serve-point win A 53.3%, B 44.8%; Elo A 1399.4, B 1447.1; model uncertainty 0.042
* Form inputs: days since last match A 210, B 36; matches on record A 368, B 88; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV09HOEHUA-HOE  (YES = Merel Hoedt)
Model: 40%
Kalshi: 23%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.031, surface_dev_loose -0.005, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
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
| Priska Madelyn Nugroho (`KXITFWMATCH-26NOV09NUGYOS-NUG`) | 0.71 / 0.76 (97) | 73.5% | 43.5% | 31.6% | 39.0% [33.5%-48.9%] | -- | -- | -- | -- | PASS | -30.0 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Natsuki Yoshimoto (`KXITFWMATCH-26NOV09NUGYOS-YOS`) | 0.23 / 0.26 (129) | 24.5% | 56.5% | 68.4% | 61.0% [51.1%-66.5%] | -- | -- | -- | -- | WATCH | +32.0 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2457.0, B 1600.0; serve-point win A 54.8%, B 44.0%; Elo A 1567.2, B 1591.4; model uncertainty 0.077
* Form inputs: days since last match A 224, B 203; matches on record A 235, B 50; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV09NUGYOS-YOS  (YES = Natsuki Yoshimoto)
Model: 56%
Kalshi: 24%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.020, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Ekaterina Ovcharenko (`KXITFWMATCH-26NOV09TSAOVC-OVC`) | 0.42 / 0.44 (1) | 43.0% | 47.2% | 24.5% | 39.7% [30.2%-55.3%] | -- | -- | -- | -- | PASS | +4.2 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chia Yi Tsao (`KXITFWMATCH-26NOV09TSAOVC-TSA`) | 0.53 / 0.56 (135) | 54.5% | 52.8% | 75.5% | 60.3% [44.7%-69.8%] | -- | -- | -- | -- | WATCH | -1.8 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 824.0, B 1300.0; serve-point win A 59.1%, B 41.4%; Elo A 1482.7, B 1475.5; model uncertainty 0.1253
* Form inputs: days since last match A 203, B 63; matches on record A 145, B 323; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.056, surface_pool_high +0.054, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Cheuk Ying Shek (`KXITFWMATCH-26NOV09WANSHE-SHE`) | 0.34 / 0.35 (38) | 34.5% | 39.8% | 42.0% | 42.6% [41.5%-43.6%] | -- | -- | -- | -- | WATCH | +5.3 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| JiaYi Wang (`KXITFWMATCH-26NOV09WANSHE-WAN`) | 0.59 / 0.65 (6) | 62.0% | 60.2% | 58.0% | 57.4% [56.4%-58.5%] | -- | -- | -- | -- | PASS | -1.8 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2216.0, B 1558.0; serve-point win A 54.1%, B 47.8%; Elo A 1510.1, B 1458.4; model uncertainty 0.0105
* Form inputs: days since last match A 41, B 9; matches on record A 72, B 49; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.011, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Alexey Aleshchev (`KXITFMATCH-26NOV09ALEZHA-ALE`) | 0.14 / 0.18 (8) | 16.0% | 21.2% | 14.3% | 21.4% [19.1%-23.5%] | -- | -- | -- | -- | PASS | +5.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lingxi Zhao (`KXITFMATCH-26NOV09ALEZHA-ZHA`) | 0.80 / 0.84 (313) | 82.0% | 78.8% | 85.7% | 78.6% [76.5%-80.9%] | -- | -- | -- | -- | PASS | -3.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1173.0, B 337.0; serve-point win A 56.0%, B 37.8%; Elo A 1059.7, B 1269.4; model uncertainty 0.0219
* Form inputs: days since last match A 196, B 385; matches on record A 69, B 39; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Lin Hao-Yu (`KXITFMATCH-26NOV09HAOISH-HAO`) | 0.46 / 0.53 (2055) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| masaki ishikawa (`KXITFMATCH-26NOV09HAOISH-ISH`) | 0.48 / 0.51 (102) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Zhenxiong Dong (`KXITFMATCH-26NOV09JIADON-DON`) | 0.80 / 0.82 (330) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zhe Jiang (`KXITFMATCH-26NOV09JIADON-JIA`) | 0.17 / 0.22 (3) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Kazushi Idogaki / Kentaro Otsuka (`KXATPCHALLENGERDOUBLES-26NOV09KADWANIDOOTS-IDOOTS`) | 0.20 / 0.39 (56) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arjun Kadhe / Aoran Wang (`KXATPCHALLENGERDOUBLES-26NOV09KADWANIDOOTS-KADWAN`) | 0.67 / 0.83 (34) | 75.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Jordan Chiu (`KXITFMATCH-26NOV09KOZCHI-CHI`) | 0.79 / 0.85 (2198) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arkhip Kozlov (`KXITFMATCH-26NOV09KOZCHI-KOZ`) | 0.14 / 0.17 (8) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Yusuke Kusuhara / Shunsuke Nakagawa (`KXATPCHALLENGERDOUBLES-26NOV09KUSNAKTAKTAN-KUSNAK`) | 0.82 / 0.94 (4) | 88.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Riki Takahata / Saki Tange (`KXATPCHALLENGERDOUBLES-26NOV09KUSNAKTAKTAN-TAKTAN`) | 0.06 / 0.20 (10) | 13.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Siu Chi Nicholas Cheng (`KXITFMATCH-26NOV09LIUCHE-CHE`) | 0.35 / 0.36 (5) | 35.5% | 65.4% | 55.2% | 67.0% [65.2%-67.9%] | -- | -- | -- | -- | PASS | +29.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Shaoyun Liu (`KXITFMATCH-26NOV09LIUCHE-LIU`) | 0.61 / 0.66 (73) | 63.5% | 34.6% | 44.8% | 33.0% [32.1%-34.8%] | -- | -- | -- | -- | PASS | -28.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 496.0, B 82.0; serve-point win A 57.9%, B 39.1%; Elo A 1138.5, B 1263.7; model uncertainty 0.0136
* Form inputs: days since last match A 203, B 276; matches on record A 21, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09LIUCHE-CHE  (YES = Siu Chi Nicholas Cheng)
Model: 65%
Kalshi: 36%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.009, surface_dev_loose -0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| jintao Lan (`KXITFMATCH-26NOV09SHILAN-LAN`) | 0.42 / 0.46 (3) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kangyuan Shi (`KXITFMATCH-26NOV09SHILAN-SHI`) | 0.50 / 0.56 (41) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Zichen Shao (`KXITFMATCH-26NOV09XIASHA-SHA`) | 0.41 / 0.45 (8) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yue Xia (`KXITFMATCH-26NOV09XIASHA-XIA`) | 0.52 / 0.60 (8) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Kaigaoge Kang (`KXITFMATCH-26NOV09YANKAN-KAN`) | 0.33 / 0.35 (38) | 34.0% | 53.9% | 68.5% | 63.5% [62.0%-64.3%] | -- | -- | -- | -- | PASS | +19.9 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xiaoyin Yang (`KXITFMATCH-26NOV09YANKAN-YAN`) | 0.59 / 0.64 (40) | 61.5% | 46.1% | 31.5% | 36.5% [35.7%-38.0%] | -- | -- | -- | -- | PASS | -15.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 817.0, B 207.0; serve-point win A 64.4%, B 34.8%; Elo A 1172.5, B 1261.8; model uncertainty 0.0113
* Form inputs: days since last match A 210, B 48; matches on record A 21, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09YANKAN-KAN  (YES = Kaigaoge Kang)
Model: 54%
Kalshi: 34%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose +0.001, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Naiktha Bains (`KXITFWMATCH-26NOV09PARBAI-BAI`) | 0.50 / 0.52 (100) | 51.0% | 35.9% | 41.6% | 40.1% [38.0%-42.1%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.1 pp | HIGH_REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sohyun Park (`KXITFWMATCH-26NOV09PARBAI-PAR`) | 0.47 / 0.50 (107) | 48.5% | 64.0% | 58.4% | 59.9% [57.9%-62.0%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +15.6 pp | HIGH_REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3623.0, B 2400.0; serve-point win A 57.4%, B 45.3%; Elo A 1658.9, B 1570.3; model uncertainty 0.0205
* Form inputs: days since last match A 47, B 46; matches on record A 366, B 483; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV09PARBAI-PAR  (YES = Sohyun Park)
Model: 64%
Kalshi: 48%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.020, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
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
| Zhuoxuan Bai (`KXITFWMATCH-26NOV09ZHEBAI-BAI`) | 0.63 / 0.66 (2178) | 64.5% | 85.5% | 90.5% | 85.2% [74.4%-89.1%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +21.1 pp | HIGH_REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Wushuang Zheng (`KXITFWMATCH-26NOV09ZHEBAI-ZHE`) | 0.34 / 0.37 (44) | 35.5% | 14.4% | 9.5% | 14.8% [10.9%-25.6%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -21.1 pp | HIGH_REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2161.0, B 1601.0; serve-point win A 48.6%, B 43.5%; Elo A 1552.0, B 1765.4; model uncertainty 0.0734
* Form inputs: days since last match A 34, B 31; matches on record A 302, B 213; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV09ZHEBAI-BAI  (YES = Zhuoxuan Bai)
Model: 86%
Kalshi: 64%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.012, surface_dev_loose -0.018, surface_dev_tight +0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
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
| Adam Bajurko (`KXITFMATCH-26NOV09BAJKAT-BAJ`) | 0.27 / 0.29 (3) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Takumi Katsuda (`KXITFMATCH-26NOV09BAJKAT-KAT`) | 0.70 / 0.73 (2054) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| David Eichenseher (`KXITFMATCH-26NOV09EICKOA-EIC`) | 0.75 / 0.79 (509) | 77.0% | 45.5% | 25.6% | 36.9% [35.0%-38.8%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -31.5 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hao Sheng Koay (`KXITFMATCH-26NOV09EICKOA-KOA`) | 0.21 / 0.24 (281) | 22.5% | 54.5% | 74.4% | 63.1% [61.2%-65.0%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +32.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1106.0, B 241.0; serve-point win A 60.0%, B 39.1%; Elo A 1194.2, B 1273.3; model uncertainty 0.0194
* Form inputs: days since last match A 196, B 364; matches on record A 30, B 10; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09EICKOA-KOA  (YES = Hao Sheng Koay)
Model: 55%
Kalshi: 22%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
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
| Naufal Siddiq Kamaruzzaman (`KXITFMATCH-26NOV09KAMSAH-KAM`) | 0.21 / 0.23 (37) | 22.0% | 35.4% | 36.5% | 36.0% [35.9%-36.9%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.4 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Samarth Sahita (`KXITFMATCH-26NOV09KAMSAH-SAH`) | 0.77 / 0.79 (57) | 78.0% | 64.6% | 63.5% | 64.0% [63.1%-64.1%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.4 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 188.0, B 96.0; serve-point win A 59.6%, B 37.5%; Elo A 1120.9, B 1217.6; model uncertainty 0.0048
* Form inputs: days since last match A 350, B 231; matches on record A 6, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
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
| Bult / Wright (`KXITFDOUBLES-26NOV09QUOPHABULWRI-BULWRI`) | 0.56 / 0.73 (5) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Quoc Cuong / Phat Nguyen (`KXITFDOUBLES-26NOV09QUOPHABULWRI-QUOPHA`) | 0.31 / 0.37 (44) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Hien Pham (`KXITFMATCH-26NOV09WUXPHA-PHA`) | 0.80 / 0.81 (122) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kai-An Wu (`KXITFMATCH-26NOV09WUXPHA-WUX`) | 0.17 / 0.23 (162) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Mayuka Aikawa (`KXITFWMATCH-26NOV09AIKYOD-AIK`) | 0.58 / 0.62 (5) | 60.0% | 50.9% | 44.8% | 56.3% [51.6%-65.5%] | -- | -- | -- | -- | PASS | -9.1 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kamonwan Yodpetch (`KXITFWMATCH-26NOV09AIKYOD-YOD`) | 0.36 / 0.40 (47) | 38.0% | 49.1% | 55.2% | 43.7% [34.5%-48.4%] | -- | -- | -- | -- | WATCH | +11.1 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1667.0, B 1037.0; serve-point win A 56.9%, B 43.3%; Elo A 1428.9, B 1326.6; model uncertainty 0.0696
* Form inputs: days since last match A 231, B 196; matches on record A 303, B 72; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.021, surface_dev_loose -0.005, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Jialan Cai (`KXITFWMATCH-26NOV09CAICAO-CAI`) | 0.48 / 0.53 (5) | 50.5% | 49.4% | 50.0% | 47.9% [46.8%-48.9%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yajing Cao (`KXITFWMATCH-26NOV09CAICAO-CAO`) | 0.44 / 0.47 (52) | 45.5% | 50.6% | 50.0% | 52.1% [51.1%-53.2%] | -- | -- | -- | -- | PASS | +5.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 204.0, B 105.0; serve-point win A 54.3%, B 45.6%; Elo A 1218.7, B 1231.6; model uncertainty 0.0106
* Form inputs: days since last match A 210, B 196; matches on record A 11, B 55; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Nagi Hanatani (`KXITFWMATCH-26NOV09HANNOG-HAN`) | 0.15 / 0.18 (8) | 16.5% | 23.5% | 15.2% | 24.3% [18.1%-35.4%] | -- | -- | -- | -- | WATCH | +7.0 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sae Noguchi (`KXITFWMATCH-26NOV09HANNOG-NOG`) | 0.81 / 0.83 (17) | 82.0% | 76.5% | 84.9% | 75.7% [64.6%-81.9%] | -- | -- | -- | -- | PASS | -5.5 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1219.0, B 1076.0; serve-point win A 50.3%, B 44.2%; Elo A 1328.0, B 1452.4; model uncertainty 0.0863
* Form inputs: days since last match A 196, B 210; matches on record A 446, B 33; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.012, surface_dev_loose -0.012, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Yuno Kitahara (`KXITFWMATCH-26NOV09KITYOS-KIT`) | 0.52 / 0.58 (5) | 55.0% | 63.1% | 70.4% | 64.6% [59.5%-69.0%] | -- | -- | -- | -- | WATCH | +8.1 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kisa Yoshioka (`KXITFWMATCH-26NOV09KITYOS-YOS`) | 0.44 / 0.45 (169) | 44.5% | 36.9% | 29.6% | 35.4% [31.0%-40.5%] | -- | -- | -- | -- | PASS | -7.6 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2068.0, B 1530.0; serve-point win A 53.5%, B 49.0%; Elo A 1428.6, B 1360.1; model uncertainty 0.0475
* Form inputs: days since last match A 203, B 203; matches on record A 119, B 159; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Xiaowei Li (`KXITFWMATCH-26NOV09LIXZHO-LIX`) | 0.52 / 0.53 (53) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ziyu Zhou (`KXITFWMATCH-26NOV09LIXZHO-ZHO`) | 0.41 / 0.47 (1305) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Lizette Cabrera (`KXITFWMATCH-26NOV09MICCAB-CAB`) | 0.51 / 0.54 (422) | 52.5% | 66.0% | 60.0% | 60.0% [58.9%-63.0%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +13.5 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Micic (`KXITFWMATCH-26NOV09MICCAB-MIC`) | 0.46 / 0.47 (47) | 46.5% | 34.0% | 40.1% | 40.1% [37.0%-41.1%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.5 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3357.0, B 3443.0; serve-point win A 54.4%, B 42.5%; Elo A 1573.4, B 1648.1; model uncertainty 0.0205
* Form inputs: days since last match A 34, B 49; matches on record A 218, B 524; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
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
| Ena Shibahara (`KXITFWMATCH-26NOV09SHIUEM-SHI`) | 0.78 / 0.83 (194) | 80.5% | 92.0% | 71.0% | 83.2% [80.8%-87.8%] | -- | -- | -- | -- | PASS | +11.5 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mutsumi Uemura (`KXITFWMATCH-26NOV09SHIUEM-UEM`) | 0.16 / 0.20 (130) | 18.0% | 8.0% | 29.0% | 16.8% [12.2%-19.2%] | -- | -- | -- | -- | PASS | -10.0 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3247.0, B 824.0; serve-point win A 62.5%, B 48.2%; Elo A 1668.7, B 1314.4; model uncertainty 0.0351
* Form inputs: days since last match A 16, B 203; matches on record A 251, B 22; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.007, surface_dev_loose +0.006, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Junlu Sun (`KXITFWMATCH-26NOV09SUNZHA-SUN`) | 0.85 / 0.88 (23) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ziyan Zhang (`KXITFWMATCH-26NOV09SUNZHA-ZHA`) | 0.09 / 0.12 (45) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Jiyun Oh (`KXITFWMATCH-26NOV09TANOHX-OHX`) | 0.44 / 0.47 (5) | 45.5% | 52.1% | 53.8% | 54.3% [54.3%-55.4%] | -- | -- | -- | -- | PASS | +6.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xiao Tang (`KXITFWMATCH-26NOV09TANOHX-TAN`) | 0.50 / 0.57 (12) | 53.5% | 47.9% | 46.2% | 45.7% [44.6%-45.7%] | -- | -- | -- | -- | PASS | -5.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 206.0, B 161.0; serve-point win A 51.1%, B 48.5%; Elo A 1253.5, B 1285.1; model uncertainty 0.0054
* Form inputs: days since last match A 196, B 196; matches on record A 6, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Yu-Ning Tsai (`KXITFWMATCH-26NOV09WUXTSA-TSA`) | 0.33 / 0.34 (37) | 33.5% | 32.3% | 68.1% | 38.9% [36.9%-42.0%] | -- | -- | -- | -- | PASS | -1.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ho Ching Wu (`KXITFWMATCH-26NOV09WUXTSA-WUX`) | 0.61 / 0.67 (1) | 64.0% | 67.7% | 31.9% | 61.1% [58.0%-63.1%] | -- | -- | -- | -- | PASS | +3.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 678.0, B 181.0; serve-point win A 54.5%, B 48.9%; Elo A 1398.9, B 1291.5; model uncertainty 0.0258
* Form inputs: days since last match A 196, B 217; matches on record A 414, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.020, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Marianna Shikhanova (`KXITFWMATCH-26NOV09YOSSHI-SHI`) | 0.35 / 0.42 (2005) | 38.5% | 46.2% | 75.2% | 52.1% [51.1%-53.2%] | -- | -- | -- | -- | PASS | +7.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sara Yoshida (`KXITFWMATCH-26NOV09YOSSHI-YOS`) | 0.56 / 0.63 (72) | 59.5% | 53.8% | 24.8% | 47.9% [46.8%-48.9%] | -- | -- | -- | -- | PASS | -5.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 151.0, B 49.0; serve-point win A 54.3%, B 46.4%; Elo A 1200.0, B 1210.1; model uncertainty 0.0106
* Form inputs: days since last match A 203, B 378; matches on record A 8, B 6; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Yinuo Huang (`KXITFWMATCH-26NOV09YUXHUA-HUA`) | 0.08 / 0.10 (432) | 9.0% | 20.4% | 46.3% | 37.4% [37.4%-38.4%] | -- | -- | -- | -- | PASS | +11.4 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Wenfei Yu (`KXITFWMATCH-26NOV09YUXHUA-YUX`) | 0.88 / 0.90 (2059) | 89.0% | 79.5% | 53.7% | 62.6% [61.6%-62.6%] | -- | -- | -- | -- | PASS | -9.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 238.0, B 38.0; serve-point win A 56.0%, B 50.1%; Elo A 1351.8, B 1266.3; model uncertainty 0.0052
* Form inputs: days since last match A 196, B 455; matches on record A 35, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Noelani Sara Teso (`KXITFWMATCH-26NOV09ZHATES-TES`) | 0.07 / 0.10 (30) | 8.5% | 24.8% | 50.0% | 32.4% [27.8%-36.3%] | -- | -- | -- | -- | PASS | +16.3 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xichen Zhao (`KXITFWMATCH-26NOV09ZHATES-ZHA`) | 0.86 / 0.92 (5) | 89.0% | 75.2% | 50.0% | 67.6% [63.7%-72.2%] | -- | -- | -- | -- | PASS | -13.8 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 896.0, B 471.0; serve-point win A 54.0%, B 51.0%; Elo A 1293.3, B 1129.9; model uncertainty 0.0428
* Form inputs: days since last match A 196, B 413; matches on record A 133, B 25; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV09ZHATES-TES  (YES = Noelani Sara Teso)
Model: 25%
Kalshi: 8%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Papangkorn Bunyarit (`KXITFMATCH-26NOV09BUNFUX-BUN`) | 0.05 / 0.08 (5) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hong-Lin Fu (`KXITFMATCH-26NOV09BUNFUX-FUX`) | 0.94 / 0.95 (560) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Thanapet Chanta (`KXITFMATCH-26NOV09CHASRI-CHA`) | 0.95 / 0.96 (541) | 95.5% | 78.5% | 71.7% | 65.2% [65.2%-67.2%] | -- | -- | -- | -- | PASS | -17.0 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tanakorn Srirat (`KXITFMATCH-26NOV09CHASRI-SRI`) | 0.04 / 0.05 (27) | 4.5% | 21.5% | 28.3% | 34.8% [32.8%-34.8%] | -- | -- | -- | -- | PASS | +17.0 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2163.0, B 108.0; serve-point win A 61.7%, B 44.4%; Elo A 1328.2, B 1218.9; model uncertainty 0.0098
* Form inputs: days since last match A 175, B 378; matches on record A 160, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09CHASRI-SRI  (YES = Tanakorn Srirat)
Model: 21%
Kalshi: 4%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
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
| Thantub Suksumrarn (`KXITFMATCH-26NOV09VANSUK-SUK`) | 0.35 / 0.37 (32) | 36.0% | 48.5% | 40.8% | 49.0% [45.4%-55.1%] | 37.0% | -- | 37.0% | MODEL_LONE_OUTLIER | WATCH | +12.5 pp | REVIEW | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Fons Van Sambeek (`KXITFMATCH-26NOV09VANSUK-VAN`) | 0.62 / 0.64 (1341) | 63.0% | 51.5% | 59.2% | 51.0% [44.9%-54.6%] | 63.0% | -- | 63.0% | MODEL_LONE_OUTLIER | PASS | -11.5 pp | REVIEW | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1119.0, B 1818.0; serve-point win A 60.8%, B 39.5%; Elo A 1248.8, B 1281.6; model uncertainty 0.0487
* Form inputs: days since last match A 196, B 196; matches on record A 58, B 105; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY
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
| Sato / Tse (`KXITFWDOUBLES-26NOV09SATTSEYAMYAN-SATTSE`) | 0.08 / 0.89 (56) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yamalapalli / Yang (`KXITFWDOUBLES-26NOV09SATTSEYAMYAN-YAMYAN`) | 0.07 / 0.89 (56) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Alafia Ayeni / Kokoro Isomura vs Jake Delaney / Jesse Delaney -- ATP Challenger Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-10T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10AVEISODELDEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alafia Ayeni / Kokoro Isomura (`KXATPCHALLENGERDOUBLES-26NOV10AVEISODELDEL-AVEISO`) | 0.36 / 0.55 (56) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jake Delaney / Jesse Delaney (`KXATPCHALLENGERDOUBLES-26NOV10AVEISODELDEL-DELDEL`) | 0.51 / 0.67 (15) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Blake Bayldon / Thomas Fancutt vs Florian Broska / Jan Kumstat -- ATP Challenger Brisbane R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-10T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BAYFANBROKUM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blake Bayldon / Thomas Fancutt (`KXATPCHALLENGERDOUBLES-26NOV10BAYFANBROKUM-BAYFAN`) | 0.36 / 0.68 (7) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Florian Broska / Jan Kumstat (`KXATPCHALLENGERDOUBLES-26NOV10BAYFANBROKUM-BROKUM`) | 0.40 / 0.69 (56) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hiroki Moriya vs Alex Bolt -- ATP Challenger Brisbane R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105655:106109:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Bolt (`KXATPCHALLENGERMATCH-26NOV10MORBOL-BOL`) | 0.70 / 0.71 (2369) | 70.5% | 73.3% | 67.5% | 68.5% [66.6%-71.1%] | 68.8% | 70.0% | 68.8% | MARKETS_AGREE | PASS | +2.8 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Hiroki Moriya (`KXATPCHALLENGERMATCH-26NOV10MORBOL-MOR`) | 0.29 / 0.31 (2762) | 30.0% | 26.7% | 32.5% | 31.5% [28.9%-33.4%] | 31.2% | 28.0% | 31.2% | MODEL_LONE_OUTLIER | PASS | -3.3 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3697.0, B 4203.0; serve-point win A 60.2%, B 34.9%; Elo A 1506.9, B 1658.2; model uncertainty 0.0224
* Form inputs: days since last match A 14, B 35; matches on record A 1074, B 782; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.022, surface_pool_high +0.018, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

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
| Himeno Sakatsume (`KXITFWMATCH-26NOV09SAKSUB-SAK`) | 0.91 / 0.92 (4) | 91.5% | 90.3% | 78.1% | 80.4% [79.3%-82.2%] | 89.6% | -- | 89.6% | MODEL_LONE_OUTLIER | PASS | -1.2 pp | NORMAL | AGING | B / LIMITED | ALL_AGREE | VERIFIED |
| Alana Subasic (`KXITFWMATCH-26NOV09SAKSUB-SUB`) | 0.07 / 0.09 (1) | 8.0% | 9.7% | 21.9% | 19.6% [17.8%-20.7%] | 10.4% | -- | 10.4% | KALSHI_LONE_OUTLIER | WATCH | +1.7 pp | NORMAL | AGING | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3693.0, B 2964.0; serve-point win A 58.3%, B 51.5%; Elo A 1764.5, B 1463.4; model uncertainty 0.0146
* Form inputs: days since last match A 6, B 196; matches on record A 421, B 101; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose +0.007, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE
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
| Blando / Blando (`KXITFDOUBLES-26NOV09BLABLAKAMSUR-BLABLA`) | 0.62 / 0.71 (86) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kamath / Suresh (`KXITFDOUBLES-26NOV09BLABLAKAMSUR-KAMSUR`) | 0.24 / 0.42 (43) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Kuan-Shou Chen (`KXITFMATCH-26NOV09CHEMAS-CHE`) | 0.86 / 0.89 (1046) | 87.5% | 46.8% | 76.2% | 51.1% [47.9%-54.8%] | 83.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -40.7 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tomohiro Masabayashi (`KXITFMATCH-26NOV09CHEMAS-MAS`) | 0.10 / 0.12 (101) | 11.0% | 53.2% | 23.8% | 48.9% [45.2%-52.1%] | 16.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +42.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 224.0, B 1636.0; serve-point win A 56.1%, B 43.3%; Elo A 1173.8, B 1192.1; model uncertainty 0.0343
* Form inputs: days since last match A 7, B 196; matches on record A 6, B 144; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09CHEMAS-MAS  (YES = Tomohiro Masabayashi)
Model: 53%
Kalshi: 11%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
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
| Dong / Kose (`KXITFDOUBLES-26NOV09DONKOSQARTAL-DONKOS`) | 0.47 / 0.56 (34) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Qariaqus / Talic (`KXITFDOUBLES-26NOV09DONKOSQARTAL-QARTAL`) | 0.40 / 0.56 (17) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Faleh Alhogbani / Cherie Ligniere (`KXITFDOUBLES-26NOV09FALCHEJUNMUR-FALCHE`) | 0.32 / 0.51 (56) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jun Kim / Murtaza (`KXITFDOUBLES-26NOV09FALCHEJUNMUR-JUNMUR`) | 0.46 / 0.62 (65) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Malaszszak / Fu Wong (`KXITFDOUBLES-26NOV09MALFUWSUMVIT-MALFUW`) | 0.27 / 0.42 (77) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sumizawa / Vithoontien (`KXITFDOUBLES-26NOV09MALFUWSUMVIT-SUMVIT`) | 0.59 / 0.71 (86) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Oscar Brown (`KXITFMATCH-26NOV09PLUBRO-BRO`) | 0.50 / 0.54 (111) | 52.0% | 57.9% | 63.3% | 58.8% [57.2%-62.4%] | 51.9% | -- | 51.9% | MODEL_LONE_OUTLIER | PASS | +5.9 pp | NORMAL | AGING | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Manuel Plunger (`KXITFMATCH-26NOV09PLUBRO-PLU`) | 0.46 / 0.50 (147) | 48.0% | 42.1% | 36.7% | 41.2% [37.6%-42.8%] | 48.1% | -- | 48.1% | MODEL_LONE_OUTLIER | PASS | -5.9 pp | NORMAL | AGING | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 306.0, B 423.0; serve-point win A 57.8%, B 40.7%; Elo A 1230.7, B 1289.3; model uncertainty 0.0257
* Form inputs: days since last match A 511, B 196; matches on record A 39, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
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
| Adibi Rahiman / Farhanuddin Fariz (`KXITFDOUBLES-26NOV09RIFSARADIFAR-ADIFAR`) | 0.89 / 0.91 (3) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rifqi Fitriadi / Sarksian (`KXITFDOUBLES-26NOV09RIFSARADIFAR-RIFSAR`) | 0.05 / 0.85 (5) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Berfu Cengiz (`KXITFWMATCH-26NOV09CENKUR-CEN`) | 0.72 / 0.76 (108) | 74.0% | 62.3% | 48.4% | 50.0% [47.9%-53.2%] | -- | -- | -- | -- | PASS | -11.7 pp | REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Miho Kuramochi (`KXITFWMATCH-26NOV09CENKUR-KUR`) | 0.23 / 0.24 (32) | 23.5% | 37.7% | 51.6% | 50.0% [46.8%-52.1%] | -- | -- | -- | -- | WATCH | +14.2 pp | REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1612.0, B 3111.0; serve-point win A 54.5%, B 47.8%; Elo A 1571.0, B 1555.6; model uncertainty 0.0267
* Form inputs: days since last match A 41, B 50; matches on record A 455, B 279; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.016, surface_dev_loose +0.027, surface_dev_tight -0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Jia-Jing Lu (`KXITFWMATCH-26NOV09LUXWER-LUX`) | 0.42 / 0.48 (5) | 45.0% | 44.7% | 78.0% | 46.8% [45.8%-46.8%] | -- | -- | -- | -- | PASS | -0.3 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Caroline Werner (`KXITFWMATCH-26NOV09LUXWER-WER`) | 0.51 / 0.55 (60) | 53.0% | 55.3% | 22.0% | 53.2% [53.2%-54.2%] | -- | -- | -- | -- | PASS | +2.3 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3089.0, B 0.0; serve-point win A 54.0%, B 45.0%; Elo A 1582.4, B 1606.9; model uncertainty 0.0053
* Form inputs: days since last match A 34, B 12; matches on record A 905, B 25; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.011, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Mio Mushika (`KXITFWMATCH-26NOV09MUSOHA-MUS`) | 0.77 / 0.79 (4) | 78.0% | 85.1% | 94.3% | 78.8% [71.7%-85.4%] | -- | -- | -- | -- | PASS | +7.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Remika Ohashi (`KXITFWMATCH-26NOV09MUSOHA-OHA`) | 0.20 / 0.23 (130) | 21.5% | 14.9% | 5.7% | 21.1% [14.6%-28.3%] | -- | -- | -- | -- | PASS | -6.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2224.0, B 421.0; serve-point win A 58.1%, B 49.8%; Elo A 1520.7, B 1357.0; model uncertainty 0.0684
* Form inputs: days since last match A 203, B 203; matches on record A 201, B 44; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.004, surface_dev_loose +0.011, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| YeXin Ma (`KXITFWMATCH-26NOV09SIDMAX-MAX`) | 0.49 / 0.52 (47) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kristiana Sidorova (`KXITFWMATCH-26NOV09SIDMAX-SID`) | 0.46 / 0.52 (7) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Toshiki Karigyo (`KXITFMATCH-26NOV09KARXIA-KAR`) | 0.13 / 0.15 (161) | 14.0% | 30.5% | 34.7% | 40.2% [36.7%-43.8%] | 14.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +16.5 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Linang Xiao (`KXITFMATCH-26NOV09KARXIA-XIA`) | 0.83 / 0.84 (156) | 83.5% | 69.5% | 65.3% | 59.8% [56.2%-63.3%] | 85.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 515.0, B 1754.0; serve-point win A 56.5%, B 39.6%; Elo A 1270.7, B 1327.4; model uncertainty 0.0359
* Form inputs: days since last match A 350, B 14; matches on record A 9, B 146; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09KARXIA-KAR  (YES = Toshiki Karigyo)
Model: 30%
Kalshi: 14%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.015, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
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
| Ruochen Gao (`KXITFMATCH-26NOV09NIMGAO-GAO`) | 0.48 / 0.64 (8) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dingzheng Nima (`KXITFMATCH-26NOV09NIMGAO-NIM`) | 0.34 / 0.47 (1) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Qian Sun (`KXITFMATCH-26NOV09SUNTAN-SUN`) | 0.71 / 0.74 (133) | 72.5% | 53.5% | 55.1% | 52.5% [51.0%-54.6%] | 72.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.0 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sheng Tang (`KXITFMATCH-26NOV09SUNTAN-TAN`) | 0.25 / 0.29 (240) | 27.0% | 46.5% | 44.9% | 47.4% [45.4%-49.0%] | 28.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +19.5 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1071.0, B 714.0; serve-point win A 62.0%, B 38.6%; Elo A 1192.1, B 1177.1; model uncertainty 0.0177
* Form inputs: days since last match A 21, B 203; matches on record A 76, B 92; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV09SUNTAN-TAN  (YES = Sheng Tang)
Model: 47%
Kalshi: 27%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
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
| Liuyan An (`KXITFWMATCH-26NOV09ANXYAN-ANX`) | 0.26 / 0.30 (105) | 28.0% | 35.3% | 31.1% | 37.9% [35.4%-40.5%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.3 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Yang (`KXITFWMATCH-26NOV09ANXYAN-YAN`) | 0.69 / 0.70 (83) | 69.5% | 64.7% | 68.9% | 62.1% [59.5%-64.6%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 425.0, B 270.0; serve-point win A 52.7%, B 44.5%; Elo A 1230.4, B 1302.6; model uncertainty 0.0253
* Form inputs: days since last match A 196, B 378; matches on record A 13, B 21; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
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
| Yiru Chen (`KXITFWMATCH-26NOV09NAKCHE-CHE`) | 0.07 / 0.08 (1) | 7.5% | 18.3% | 26.9% | 24.3% [22.7%-25.2%] | 10.4% | -- | 10.4% | KALSHI_LONE_OUTLIER | PASS | +10.8 pp | REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Thasaporn Naklo (`KXITFWMATCH-26NOV09NAKCHE-NAK`) | 0.92 / 0.93 (216) | 92.5% | 81.7% | 73.1% | 75.7% [74.8%-77.3%] | 89.6% | -- | 89.6% | KALSHI_LONE_OUTLIER | PASS | -10.8 pp | REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2173.0, B 625.0; serve-point win A 56.4%, B 50.4%; Elo A 1456.9, B 1245.2; model uncertainty 0.0125
* Form inputs: days since last match A 196, B 196; matches on record A 166, B 28; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.008, surface_dev_loose +0.008, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; THIN_DISPLAYED_SIZE
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
| Naoko Eto (`KXITFWMATCH-26NOV09WANETO-ETO`) | 0.03 / 0.04 (687) | 3.5% | 1.1% | 0.1% | 2.3% [0.7%-5.5%] | 7.8% | -- | 7.8% | EXTERNAL_LONE_OUTLIER | PASS | -2.4 pp | NORMAL | AGING | C / LIMITED | EXTERNAL_OUTLIER | VERIFIED |
| Jiaqi Wang (`KXITFWMATCH-26NOV09WANETO-WAN`) | 0.96 / 0.97 (946) | 96.5% | 98.9% | 99.9% | 97.7% [94.5%-99.3%] | 92.2% | -- | 92.2% | EXTERNAL_LONE_OUTLIER | PASS | +2.4 pp | NORMAL | AGING | C / LIMITED | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 2849.0, B 643.0; serve-point win A 60.7%, B 56.5%; Elo A 1543.7, B 1068.0; model uncertainty 0.0237
* Form inputs: days since last match A 196, B 50; matches on record A 250, B 205; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.002, surface_dev_loose +0.003, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lorenzo Angelini vs Robin Bertrand -- ATP Challenger Hersonissos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149117:209850:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Angelini (`KXATPCHALLENGERMATCH-26NOV10ANGBER-ANG`) | 0.28 / 0.30 (2019) | 29.0% | 36.6% | 30.6% | 29.7% [28.0%-31.1%] | -- | 29.3% | 29.3% | MARKETS_AGREE | PASS | +7.7 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Robin Bertrand (`KXATPCHALLENGERMATCH-26NOV10ANGBER-BER`) | 0.70 / 0.72 (5084) | 71.0% | 63.3% | 69.4% | 70.3% [69.0%-72.0%] | -- | 71.5% | 71.5% | MARKETS_AGREE | PASS | -7.7 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2397.0, B 5699.0; serve-point win A 52.8%, B 44.6%; Elo A 1370.3, B 1536.1; model uncertainty 0.0151
* Form inputs: days since last match A 203, B 175; matches on record A 69, B 440; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.014, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Michael Geerts vs Juan Cruz Martin Manzano -- ATP Challenger Hersonissos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126107:212305:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michael Geerts (`KXATPCHALLENGERMATCH-26NOV10GEEMAR-GEE`) | 0.66 / 0.67 (4018) | 66.5% | 44.2% | 56.7% | 57.2% [54.6%-60.2%] | -- | 66.5% | 66.5% | MODEL_LONE_OUTLIER | PASS | -22.3 pp | HIGH_REVIEW | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Juan Cruz Martin Manzano (`KXATPCHALLENGERMATCH-26NOV10GEEMAR-MAR`) | 0.33 / 0.34 (805) | 33.5% | 55.8% | 43.3% | 42.8% [39.8%-45.4%] | -- | 33.7% | 33.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +22.3 pp | HIGH_REVIEW | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4303.0, B 3299.0; serve-point win A 59.3%, B 39.6%; Elo A 1552.9, B 1487.2; model uncertainty 0.0278
* Form inputs: days since last match A 14, B 42; matches on record A 718, B 120; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV10GEEMAR-MAR  (YES = Juan Cruz Martin Manzano)
Model: 56%
Kalshi: 34%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: A (LIMITED)
Reasons: SURFACE_DATA_THIN, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.005, surface_dev_loose +0.030, surface_dev_tight -0.025
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

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
| Eichenseher / Mueller (`KXITFDOUBLES-26NOV10KAWNOGEICMUE-EICMUE`) | 0.47 / 0.66 (22) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kawachi / Noguchi (`KXITFDOUBLES-26NOV10KAWNOGEICMUE-KAWNOG`) | 0.40 / 0.48 (48) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ioannis Xilas vs Sergey Fomin -- ATP Challenger Hersonissos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200672:209354:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sergey Fomin (`KXATPCHALLENGERMATCH-26NOV10XILFOM-FOM`) | 0.33 / 0.35 (1001) | 34.0% | 45.4% | 39.2% | 42.2% [39.2%-49.5%] | 34.3% | 34.3% | 34.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +11.4 pp | REVIEW | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Ioannis Xilas (`KXATPCHALLENGERMATCH-26NOV10XILFOM-XIL`) | 0.65 / 0.67 (1901) | 66.0% | 54.6% | 60.8% | 57.8% [50.5%-60.8%] | 65.7% | 66.8% | 65.7% | MODEL_LONE_OUTLIER | PASS | -11.4 pp | REVIEW | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2979.0, B 4117.0; serve-point win A 59.3%, B 41.6%; Elo A 1508.4, B 1494.9; model uncertainty 0.0515
* Form inputs: days since last match A 119, B 14; matches on record A 147, B 422; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.020, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

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
| Arcon / Lakshmanan (`KXITFDOUBLES-26NOV10ARCLAKNAKSRI-ARCLAK`) | 0.64 / 0.76 (27) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nakamura / Srirat (`KXITFDOUBLES-26NOV10ARCLAKNAKSRI-NAKSRI`) | 0.27 / 0.29 (5) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Chanta / Sornlaksup (`KXITFDOUBLES-26NOV10GOHHORCHASOR-CHASOR`) | 0.80 / 0.89 (56) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gohil / Horak (`KXITFDOUBLES-26NOV10GOHHORCHASOR-GOHHOR`) | 0.07 / 0.50 (3) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Yuta Kikuchi (`KXITFMATCH-26NOV10KIKZHA-KIK`) | 0.58 / 0.62 (230) | 60.0% | 80.3% | 57.3% | 74.4% [73.1%-76.0%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.3 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zhao Zhao (`KXITFMATCH-26NOV10KIKZHA-ZHA`) | 0.38 / 0.40 (1) | 39.0% | 19.7% | 42.7% | 25.6% [24.0%-26.9%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.3 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1925.0, B 155.0; serve-point win A 61.2%, B 45.4%; Elo A 1381.1, B 1177.3; model uncertainty 0.0146
* Form inputs: days since last match A 56, B 217; matches on record A 137, B 25; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10KIKZHA-KIK  (YES = Yuta Kikuchi)
Model: 80%
Kalshi: 60%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
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
| Natthayut Nithithananont (`KXITFMATCH-26NOV10NITOLI-NIT`) | 0.10 / 0.11 (28) | 10.5% | 52.8% | 55.7% | 48.9% [47.9%-49.5%] | 15.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +42.3 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nazar Oliynykov (`KXITFMATCH-26NOV10NITOLI-OLI`) | 0.85 / 0.89 (100) | 87.0% | 47.2% | 44.3% | 51.0% [50.5%-52.1%] | 84.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -39.8 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 108.0, B 203.0; serve-point win A 58.4%, B 42.2%; Elo A 1100.6, B 1114.2; model uncertainty 0.0078
* Form inputs: days since last match A 441, B 238; matches on record A 16, B 8; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10NITOLI-NIT  (YES = Natthayut Nithithananont)
Model: 53%
Kalshi: 10%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.011, surface_dev_loose -0.011, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
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
| Meiqi Guo (`KXITFWMATCH-26NOV10GUOXUX-GUO`) | 0.84 / 0.85 (166) | 84.5% | 88.7% | 94.0% | 82.7% [77.2%-87.9%] | 84.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.2 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiayu Xu (`KXITFWMATCH-26NOV10GUOXUX-XUX`) | 0.13 / 0.15 (101) | 14.0% | 11.3% | 6.0% | 17.3% [12.1%-22.8%] | 15.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -2.7 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2729.0, B 444.0; serve-point win A 59.7%, B 49.4%; Elo A 1542.5, B 1324.1; model uncertainty 0.0534
* Form inputs: days since last match A 43, B 196; matches on record A 272, B 86; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.007, surface_dev_loose +0.013, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
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
| Kim / Morisaki (`KXITFWDOUBLES-26NOV10KIMMORSEMYIT-KIMMOR`) | 0.39 / 0.60 (25) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sema / Yi Tsao (`KXITFWDOUBLES-26NOV10KIMMORSEMYIT-SEMYIT`) | 0.35 / 0.55 (27) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Kobori / Shimizu (`KXITFWDOUBLES-26NOV10KOBSHIWANWAN-KOBSHI`) | 0.70 / 0.75 (100) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Wang / Wang (`KXITFWDOUBLES-26NOV10KOBSHIWANWAN-WANWAN`) | 0.22 / 0.32 (2) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Hayasaka / Naito (`KXITFWDOUBLES-26NOV10MATNAKHAYNAI-HAYNAI`) | 0.26 / 0.39 (56) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matsuda / Nakashima (`KXITFWDOUBLES-26NOV10MATNAKHAYNAI-MATNAK`) | 0.62 / 0.75 (27) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Alexandra Malova (`KXITFWMATCH-26NOV10MOOMAL-MAL`) | 0.80 / 0.83 (31) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeong Moon (`KXITFWMATCH-26NOV10MOOMAL-MOO`) | 0.16 / 0.19 (406) | 17.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
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
| Li / Saito (`KXITFWDOUBLES-26NOV10NAGTSULIXSAI-LIXSAI`) | 0.73 / 0.90 (1) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nagata / Tsutsumi (`KXITFWDOUBLES-26NOV10NAGTSULIXSAI-NAGTSU`) | 0.05 / 0.20 (31) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Im / Shin (`KXITFWDOUBLES-26NOV10PANVARIMXSHI-IMXSHI`) | 0.81 / 0.90 (1) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pankratova / Varaksina (`KXITFWDOUBLES-26NOV10PANVARIMXSHI-PANVAR`) | 0.05 / 0.13 (28) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Adrian Mannarino vs Aleksandr Shevchenko -- ATP Stockholm R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-10 15:00Z
* Current expected start: 2026-11-10 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 22:48Z
* Recommended handicap-by time: 2026-11-10 11:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-10T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105173:207686:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Mannarino (`KXATPMATCH-26NOV10MANSHE-MAN`) | 0.53 / 0.54 (104) | 53.5% | 56.0% | 61.6% | 61.6% [60.7%-62.6%] | 53.2% | 53.8% | 53.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +2.5 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Aleksandr Shevchenko (`KXATPMATCH-26NOV10MANSHE-SHE`) | 0.46 / 0.47 (14008) | 46.5% | 44.0% | 38.4% | 38.4% [37.4%-39.3%] | 46.8% | 46.8% | 46.8% | MODEL_LONE_OUTLIER | PASS | -2.5 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5623.0, B 5333.0; serve-point win A 65.8%, B 35.4%; Elo A 1797.4, B 1720.3; model uncertainty 0.0094
* Form inputs: days since last match A 1, B 7; matches on record A 1327, B 510; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.009, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26NOV10MANSHE-MAN5` Will Adrian Mannarino win at least 4.5 more games than Alexander Shevchenko?: 0.03/0.92 mid 47.5%, model 17.9% (projection_v2.0 (prediction ledger)) -- gap -29.6 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV10MANSHE-19` Over 18.5 games: 0.38/0.93 mid 65.5%, model 90.1% (projection_v2.0 (prediction ledger)) -- gap +24.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV10MANSHE-24` Over 23.5 games: 0.44/0.46 mid 45.0%, model 55.5% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MANSHE-SHE21` Will Alexander Shevchenko win the Adrian Mannarino vs Alexander Shevchenko match by a set score of 2-1?: 0.03/0.22 mid 12.5%, model 22.8% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10MANSHE-SHE2` Will Alexander Shevchenko win at least 1.5 more games than Adrian Mannarino?: 0.39/0.44 mid 41.5%, model 36.4% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MANSHE-2-MAN` Will Adrian Mannarino win set 2 in the Adrian Mannarino vs Alexander Shevchenko match: 0.03/0.95 mid 49.0%, model 54.0% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MANSHE-MAN21` Will Adrian Mannarino win the Adrian Mannarino vs Alexander Shevchenko match by a set score of 2-1?: 0.17/0.27 mid 22.0%, model 26.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MANSHE-MAN20` Will Adrian Mannarino win the Adrian Mannarino vs Alexander Shevchenko match by a set score of 2-0?: 0.11/0.38 mid 24.5%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MANSHE-1-SHE` Will Alexander Shevchenko win set 1 in the Adrian Mannarino vs Alexander Shevchenko match: 0.46/0.50 mid 48.0%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MANSHE-2-SHE` Will Alexander Shevchenko win set 2 in the Adrian Mannarino vs Alexander Shevchenko match: 0.01/0.95 mid 48.0%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MANSHE-1-MAN` Will Adrian Mannarino win set 1 in the Adrian Mannarino vs Alexander Shevchenko match: 0.51/0.55 mid 53.0%, model 54.0% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV10MANSHE-29` Over 28.5 games: 0.03/0.71 mid 37.0%, model 37.9% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MANSHE-SHE20` Will Alexander Shevchenko win the Adrian Mannarino vs Alexander Shevchenko match by a set score of 2-0?: 0.11/0.33 mid 22.0%, model 21.1% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10MANSHE-MAN2` Will Adrian Mannarino win at least 1.5 more games than Alexander Shevchenko?: 0.47/0.49 mid 48.0%, model 48.2% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alex Michelsen vs Juan Manuel Cerundolo -- ATP Stockholm R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-10 15:00Z
* Current expected start: 2026-11-10 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 22:48Z
* Recommended handicap-by time: 2026-11-10 11:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-10T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207678:210506:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel Cerundolo (`KXATPMATCH-26NOV10MICCER-CER`) | 0.26 / 0.27 (72951) | 26.5% | 25.1% | 18.7% | 19.4% [17.5%-22.6%] | 25.5% | 24.1% | 24.8% | MODEL_LONE_OUTLIER | PASS | -1.4 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Alex Michelsen (`KXATPMATCH-26NOV10MICCER-MIC`) | 0.75 / 0.76 (904) | 75.5% | 74.9% | 81.3% | 80.6% [77.5%-82.5%] | 74.5% | 76.4% | 75.4% | MODEL_LONE_OUTLIER | WATCH | -0.6 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5933.0, B 6143.0; serve-point win A 67.6%, B 37.8%; Elo A 1968.7, B 1749.8; model uncertainty 0.0251
* Form inputs: days since last match A 0, B 1; matches on record A 321, B 549; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.018, surface_dev_tight -0.027
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV10MICCER-18` Over 17.5 games: 0.64/0.93 mid 78.5%, model 91.7% (projection_v2.0 (prediction ledger)) -- gap +13.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV10MICCER-23` Over 22.5 games: 0.45/0.47 mid 46.0%, model 55.9% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MICCER-CER20` Will Juan Manuel Cerundolo win the Alex Michelsen vs Juan Manuel Cerundolo match by a set score of 2-0?: 0.13/0.28 mid 20.5%, model 10.7% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10MICCER-MIC7` Will Alex Michelsen win at least 6.5 more games than Juan Manuel Cerundolo?: 0.15/0.20 mid 17.5%, model 9.4% (projection_v2.0 (prediction ledger)) -- gap -8.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10MICCER-MIC4` Will Alex Michelsen win at least 3.5 more games than Juan Manuel Cerundolo?: 0.53/0.56 mid 54.5%, model 47.7% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MICCER-MIC20` Will Alex Michelsen win the Alex Michelsen vs Juan Manuel Cerundolo match by a set score of 2-0?: 0.47/0.57 mid 52.0%, model 45.2% (projection_v2.0 (prediction ledger)) -- gap -6.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MICCER-2-MIC` Will Alex Michelsen win set 2 in the Alex Michelsen vs Juan Manuel Cerundolo match: 0.72/0.76 mid 74.0%, model 67.3% (projection_v2.0 (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MICCER-MIC21` Will Alex Michelsen win the Alex Michelsen vs Juan Manuel Cerundolo match by a set score of 2-1?: 0.20/0.27 mid 23.5%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MICCER-2-CER` Will Juan Manuel Cerundolo win set 2 in the Alex Michelsen vs Juan Manuel Cerundolo match: 0.23/0.31 mid 27.0%, model 32.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV10MICCER-28` Over 27.5 games: 0.29/0.33 mid 31.0%, model 36.4% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MICCER-CER21` Will Juan Manuel Cerundolo win the Alex Michelsen vs Juan Manuel Cerundolo match by a set score of 2-1?: 0.11/0.28 mid 19.5%, model 14.4% (projection_v2.0 (prediction ledger)) -- gap -5.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MICCER-1-CER` Will Juan Manuel Cerundolo win set 1 in the Alex Michelsen vs Juan Manuel Cerundolo match: 0.29/0.32 mid 30.5%, model 32.7% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MICCER-1-MIC` Will Alex Michelsen win set 1 in the Alex Michelsen vs Juan Manuel Cerundolo match: 0.68/0.71 mid 69.5%, model 67.3% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV10MICCER-CER2` Will Juan Manuel Cerundolo win at least 1.5 more games than Alex Michelsen?: 0.18/0.22 mid 20.0%, model 19.3% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Hong / Ju Kim (`KXITFDOUBLES-26NOV10HONJUKSUNWAN-HONJUK`) | 0.07 / 0.90 (1) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sun / Wang (`KXITFDOUBLES-26NOV10HONJUKSUNWAN-SUNWAN`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Connel / Hongyu (`KXITFDOUBLES-26NOV10VISZHUCONHON-CONHON`) | 0.66 / 0.86 (2) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vishenchuk Vishenko / Zhukov (`KXITFDOUBLES-26NOV10VISZHUCONHON-VISZHU`) | 0.22 / 0.77 (3) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Karim Bennani vs Sumit Nagal -- ATP Challenger Hersonissos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 12:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111576:211558:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karim Bennani (`KXATPCHALLENGERMATCH-26NOV10BENNAG-BEN`) | 0.26 / 0.27 (3523) | 26.5% | 42.5% | 59.7% | 49.5% [35.0%-56.6%] | -- | 25.4% | 25.4% | MODEL_LONE_OUTLIER | WATCH | +16.0 pp | HIGH_REVIEW | AGING | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Sumit Nagal (`KXATPCHALLENGERMATCH-26NOV10BENNAG-NAG`) | 0.73 / 0.75 (1586) | 74.0% | 57.5% | 40.4% | 50.5% [43.4%-65.0%] | -- | 74.7% | 74.7% | MODEL_LONE_OUTLIER | PASS | -16.5 pp | HIGH_REVIEW | AGING | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1876.0, B 4831.0; serve-point win A 60.0%, B 38.5%; Elo A 1496.5, B 1585.9; model uncertainty 0.1083
* Form inputs: days since last match A 51, B 21; matches on record A 60, B 659; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV10BENNAG-BEN  (YES = Karim Bennani)
Model: 42%
Kalshi: 26%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: B (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.031, surface_pool_high +0.036, surface_dev_loose +0.015, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Felix Gill vs Menelaos Efstathiou -- ATP Challenger Hersonissos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 12:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144949:208269:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Menelaos Efstathiou (`KXATPCHALLENGERMATCH-26NOV10GILEFS-EFS`) | 0.16 / 0.17 (1) | 16.5% | 18.6% | 29.5% | 21.3% [13.8%-27.3%] | -- | 18.1% | 18.1% | MODEL_LONE_OUTLIER | WATCH | +2.0 pp | NORMAL | AGING | C / POOR | ALL_AGREE | VERIFIED |
| Felix Gill (`KXATPCHALLENGERMATCH-26NOV10GILEFS-GIL`) | 0.82 / 0.84 (3945) | 83.0% | 81.5% | 70.5% | 78.7% [72.7%-86.2%] | -- | 84.2% | -- | INSUFFICIENT_INPUTS | PASS | -1.6 pp | NORMAL | AGING | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4787.0, B 386.0; serve-point win A 64.3%, B 42.7%; Elo A 1554.2, B 1306.3; model uncertainty 0.0679
* Form inputs: days since last match A 21, B 50; matches on record A 359, B 105; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.051, surface_pool_high -0.060, surface_dev_loose -0.003, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; THIN_DISPLAYED_SIZE

## Francesco Maestrelli vs Jack Loge -- ATP Challenger Hersonissos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 12:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T12:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208353:211504:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack Loge (`KXATPCHALLENGERMATCH-26NOV10MAELOG-LOG`) | 0.32 / 0.34 (6517) | 33.0% | 35.6% | 50.0% | 43.5% [35.3%-47.5%] | 34.3% | 32.8% | 33.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +2.6 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |
| Francesco Maestrelli (`KXATPCHALLENGERMATCH-26NOV10MAELOG-MAE`) | 0.66 / 0.68 (2824) | 67.0% | 64.4% | 50.0% | 56.5% [52.5%-64.7%] | 65.7% | 68.5% | 67.1% | MODEL_LONE_OUTLIER | PASS | -2.6 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5128.0, B 3551.0; serve-point win A 64.9%, B 38.0%; Elo A 1600.6, B 1442.6; model uncertainty 0.0608
* Form inputs: days since last match A 14, B 98; matches on record A 370, B 184; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

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
| Artjoms Afanasjevs (`KXITFMATCH-26NOV10AFADEL-AFA`) | 0.09 / 0.12 (3) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vito Dell'elba (`KXITFMATCH-26NOV10AFADEL-DEL`) | 0.88 / 0.92 (17) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Alessio Basile (`KXITFMATCH-26NOV10BASSTE-BAS`) | 0.83 / 0.94 (5) | 88.5% | 73.2% | 74.5% | 64.4% [60.2%-69.7%] | -- | -- | -- | -- | PASS | -15.3 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniil Stepanov (`KXITFMATCH-26NOV10BASSTE-STE`) | 0.05 / 0.13 (33) | 9.0% | 26.8% | 25.5% | 35.6% [30.3%-39.8%] | -- | -- | -- | -- | PASS | +17.8 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 952.0, B 210.0; serve-point win A 59.7%, B 45.0%; Elo A 1252.5, B 1158.9; model uncertainty 0.0473
* Form inputs: days since last match A 350, B 196; matches on record A 43, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10BASSTE-STE  (YES = Daniil Stepanov)
Model: 27%
Kalshi: 9%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.029, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Alessandro Bellifemine (`KXITFMATCH-26NOV10BELJOZ-BEL`) | 0.62 / 0.75 (1) | 68.5% | 70.0% | 32.0% | 46.8% [45.7%-48.9%] | -- | -- | -- | -- | PASS | +1.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Patrick Jozwicki (`KXITFMATCH-26NOV10BELJOZ-JOZ`) | 0.25 / 0.30 (5) | 27.5% | 30.0% | 68.0% | 53.2% [51.0%-54.3%] | -- | -- | -- | -- | PASS | +2.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 859.0, B 172.0; serve-point win A 56.1%, B 47.8%; Elo A 1176.5, B 1183.9; model uncertainty 0.016
* Form inputs: days since last match A 336, B 231; matches on record A 65, B 6; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.011, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Dai / Han (`KXITFDOUBLES-26NOV10DAIHANDONYAN-DAIHAN`) | 0.05 / 0.89 (56) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dong / Yang (`KXITFDOUBLES-26NOV10DAIHANDONYAN-DONYAN`) | 0.07 / 0.90 (1) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Amine Jamji (`KXITFMATCH-26NOV10JAMPAO-JAM`) | 0.34 / 0.41 (42) | 37.5% | 59.8% | 39.1% | 48.9% [46.3%-52.1%] | -- | -- | -- | -- | PASS | +22.3 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andrea Paolini (`KXITFMATCH-26NOV10JAMPAO-PAO`) | 0.52 / 0.65 (6) | 58.5% | 40.2% | 60.9% | 51.0% [47.9%-53.7%] | -- | -- | -- | -- | PASS | -18.3 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 659.0, B 516.0; serve-point win A 57.9%, B 44.0%; Elo A 1224.0, B 1208.3; model uncertainty 0.0289
* Form inputs: days since last match A 50, B 266; matches on record A 15, B 31; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10JAMPAO-JAM  (YES = Amine Jamji)
Model: 60%
Kalshi: 38%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.011, surface_dev_loose -0.016, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Vuk Radjenovic (`KXITFMATCH-26NOV10RADROM-RAD`) | 0.51 / 0.71 (9) | 61.0% | 61.9% | 32.7% | 53.1% [53.1%-53.1%] | -- | -- | -- | -- | PASS | +0.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Felix Romeo (`KXITFMATCH-26NOV10RADROM-ROM`) | 0.41 / 0.42 (43) | 41.5% | 38.1% | 67.3% | 46.9% [46.9%-46.9%] | -- | -- | -- | -- | PASS | -3.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 799.0, B 0.0; serve-point win A 62.2%, B 40.2%; Elo A 1242.8, B 1223.7; model uncertainty 0.0001
* Form inputs: days since last match A 371, B 875; matches on record A 71, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Gokberk Saritas (`KXITFMATCH-26NOV10SHYSAR-SAR`) | 0.06 / 0.13 (107) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Heorhii Shylov (`KXITFMATCH-26NOV10SHYSAR-SHY`) | 0.85 / 0.94 (5) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Aleksa Oparnica (`KXITFMATCH-26NOV10TIUOPA-OPA`) | 0.16 / 0.32 (2) | 24.0% | 14.6% | 18.8% | 19.5% [17.5%-22.3%] | -- | -- | -- | -- | PASS | -9.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Evgenii Tiurnev (`KXITFMATCH-26NOV10TIUOPA-TIU`) | 0.76 / 0.81 (131) | 78.5% | 85.4% | 81.2% | 80.5% [77.7%-82.5%] | -- | -- | -- | -- | PASS | +6.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1478.0, B 70.0; serve-point win A 69.7%, B 38.9%; Elo A 1505.2, B 1263.3; model uncertainty 0.0243
* Form inputs: days since last match A 231, B 504; matches on record A 579, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.028, surface_dev_loose -0.001, surface_dev_tight -0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Cezar Stefan Bentzel (`KXITFMATCH-26NOV10WAGBEN-BEN`) | 0.24 / 0.38 (55) | 31.0% | 33.5% | 45.2% | 41.0% [40.0%-41.6%] | -- | -- | -- | -- | PASS | +2.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Wagner (`KXITFMATCH-26NOV10WAGBEN-WAG`) | 0.63 / 0.74 (6) | 68.5% | 66.5% | 54.8% | 59.0% [58.4%-60.0%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 861.0, B 390.0; serve-point win A 56.7%, B 46.6%; Elo A 1196.5, B 1125.9; model uncertainty 0.0079
* Form inputs: days since last match A 196, B 336; matches on record A 22, B 6; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Cao / Tikhonova (`KXITFWDOUBLES-26NOV10CAOTIKCHELIX-CAOTIK`) | 0.57 / 0.79 (119) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chen / Li (`KXITFWDOUBLES-26NOV10CAOTIKCHELIX-CHELIX`) | 0.18 / 0.35 (38) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Hou / Plipuech (`KXITFWDOUBLES-26NOV10HOUPLIYUXZHO-HOUPLI`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yu / Zhou (`KXITFWDOUBLES-26NOV10HOUPLIYUXZHO-YUXZHO`) | 0.07 / 0.90 (1) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Ruben Hartig (`KXITFMATCH-26NOV10HARRYD-HAR`) | 0.33 / 0.41 (14) | 37.0% | 31.8% | 56.3% | 34.7% [33.0%-35.5%] | -- | -- | -- | -- | PASS | -5.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Victor Ryden (`KXITFMATCH-26NOV10HARRYD-RYD`) | 0.55 / 0.62 (44) | 58.5% | 68.2% | 43.7% | 65.3% [64.5%-67.0%] | -- | -- | -- | -- | PASS | +9.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 109.0, B 67.0; serve-point win A 55.8%, B 40.6%; Elo A 1120.1, B 1237.4; model uncertainty 0.0129
* Form inputs: days since last match A 196, B 378; matches on record A 14, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Benaim / Brown (`KXITFDOUBLES-26NOV10HUALUXBENBRO-BENBRO`) | 0.19 / 0.38 (40) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Huang / Lu (`KXITFDOUBLES-26NOV10HUALUXBENBRO-HUALUX`) | 0.56 / 0.77 (108) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Alex Jones (`KXITFMATCH-26NOV10JONROB-JON`) | 0.93 / 0.95 (510) | 94.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Joseph Roboly (`KXITFMATCH-26NOV10JONROB-ROB`) | 0.05 / 0.06 (559) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Panagiotis-Gerasimos Grammatikakis (`KXITFMATCH-26NOV10LONGRA-GRA`) | 0.06 / 0.11 (109) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thando Longwe-Smit (`KXITFMATCH-26NOV10LONGRA-LON`) | 0.86 / 0.94 (83) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Koaykul / Navasirisomboon (`KXITFDOUBLES-26NOV10MASSUKKOANAV-KOANAV`) | 0.12 / 0.17 (31) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Masabayashi / Suksumrarn (`KXITFDOUBLES-26NOV10MASSUKKOANAV-MASSUK`) | 0.77 / 0.90 (1) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jean-Julien Rojer / Theodore Winegar vs William Rejchtman Vinciguerra / Olle Wallin -- ATP Stockholm 1/8 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-09 22:48Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-11T05:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ROJWINREJWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| William Rejchtman Vinciguerra / Olle Wallin (`KXATPDOUBLES-26NOV10ROJWINREJWAL-REJWAL`) | 0.06 / 0.19 (53) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jean-Julien Rojer / Theodore Winegar (`KXATPDOUBLES-26NOV10ROJWINREJWAL-ROJWIN`) | 0.81 / 0.94 (56) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Bunyarit / Kamput (`KXITFDOUBLES-26NOV10SUKSUKBUNKAM-BUNKAM`) | 0.07 / 0.90 (1) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sukjai / Sukjai (`KXITFDOUBLES-26NOV10SUKSUKBUNKAM-SUKSUK`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dalibor Svrcina vs Vitaliy Sachko -- ATP Challenger Orleans R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126964:207494:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vitaliy Sachko (`KXATPCHALLENGERMATCH-26NOV10SVRSAC-SAC`) | 0.36 / 0.38 (4045) | 37.0% | 28.7% | 28.9% | 28.9% [27.2%-31.7%] | 38.4% | 37.1% | 37.1% | MARKETS_AGREE | PASS | -8.2 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Dalibor Svrcina (`KXATPCHALLENGERMATCH-26NOV10SVRSAC-SVR`) | 0.62 / 0.64 (1074) | 63.0% | 71.2% | 71.1% | 71.1% [68.3%-72.8%] | 61.6% | 63.9% | 63.9% | MARKETS_AGREE | SHADOW_BET | +8.2 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5358.0, B 4786.0; serve-point win A 58.4%, B 45.8%; Elo A 1773.1, B 1619.7; model uncertainty 0.0225
* Form inputs: days since last match A 7, B 7; matches on record A 430, B 566; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose +0.018, surface_dev_tight -0.027
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Otto Virtanen vs Dino Prizmic -- ATP Challenger Orleans R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202261:209976:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dino Prizmic (`KXATPCHALLENGERMATCH-26NOV10VIRPRI-PRI`) | 0.54 / 0.55 (961) | 54.5% | 61.0% | 51.5% | 54.5% [53.0%-56.9%] | 54.1% | 54.7% | 54.4% | MODEL_LONE_OUTLIER | PASS | +6.5 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Otto Virtanen (`KXATPCHALLENGERMATCH-26NOV10VIRPRI-VIR`) | 0.44 / 0.47 (2906) | 45.5% | 39.0% | 48.5% | 45.5% [43.1%-47.0%] | 45.9% | 46.1% | 46.0% | MODEL_LONE_OUTLIER | PASS | -6.5 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5328.0, B 4564.0; serve-point win A 63.2%, B 34.5%; Elo A 1768.4, B 1853.2; model uncertainty 0.0198
* Form inputs: days since last match A 7, B 14; matches on record A 439, B 257; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.015, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

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
| Maximilian Alessandro Erhardt (`KXITFMATCH-26NOV10VISERH-ERH`) | 0.21 / 0.25 (27) | 23.0% | 40.5% | 54.7% | 47.9% [47.9%-48.9%] | -- | -- | -- | -- | PASS | +17.5 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mac Visser (`KXITFMATCH-26NOV10VISERH-VIS`) | 0.71 / 0.79 (150) | 75.0% | 59.5% | 45.3% | 52.1% [51.0%-52.1%] | -- | -- | -- | -- | PASS | -15.5 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 752.0, B 70.0; serve-point win A 58.3%, B 43.5%; Elo A 1295.9, B 1283.4; model uncertainty 0.0053
* Form inputs: days since last match A 156, B 483; matches on record A 16, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10VISERH-ERH  (YES = Maximilian Alessandro Erhardt)
Model: 41%
Kalshi: 23%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Felitsata Dorofeeva-Rybas (`KXITFWMATCH-26NOV10DORTIC-DOR`) | 0.49 / 0.51 (56) | 50.0% | 15.4% | 15.1% | 21.8% [19.5%-25.6%] | -- | -- | -- | -- | PASS | -34.6 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eliska Tichackova (`KXITFWMATCH-26NOV10DORTIC-TIC`) | 0.43 / 0.47 (52) | 45.0% | 84.6% | 84.9% | 78.2% [74.4%-80.5%] | -- | -- | -- | -- | PASS | +39.6 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 923.0, B 1647.0; serve-point win A 47.5%, B 44.9%; Elo A 1447.6, B 1623.6; model uncertainty 0.0303
* Form inputs: days since last match A 343, B 259; matches on record A 19, B 46; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10DORTIC-TIC  (YES = Eliska Tichackova)
Model: 85%
Kalshi: 45%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.016, surface_dev_loose -0.012, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Marta Lombardini (`KXITFWMATCH-26NOV10LOMZHE-LOM`) | 0.62 / 0.67 (52) | 64.5% | 64.8% | 66.1% | 61.6% [57.4%-64.1%] | -- | -- | -- | -- | PASS | +0.3 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sonja Zhenikhova (`KXITFWMATCH-26NOV10LOMZHE-ZHE`) | 0.31 / 0.33 (37) | 32.0% | 35.2% | 33.9% | 38.4% [35.9%-42.6%] | -- | -- | -- | -- | PASS | +3.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 984.0, B 1212.0; serve-point win A 53.9%, B 49.0%; Elo A 1447.1, B 1388.4; model uncertainty 0.0335
* Form inputs: days since last match A 47, B 259; matches on record A 25, B 38; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Giulia Safina Popa (`KXITFWMATCH-26NOV10POPTOD-POP`) | 0.59 / 0.67 (63) | 63.0% | 82.8% | 63.1% | 72.6% [70.4%-77.3%] | -- | -- | -- | -- | PASS | +19.8 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cristiana Nicoleta Todoni (`KXITFWMATCH-26NOV10POPTOD-TOD`) | 0.33 / 0.38 (45) | 35.5% | 17.2% | 36.9% | 27.4% [22.7%-29.6%] | -- | -- | -- | -- | PASS | -18.3 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1013.0, B 865.0; serve-point win A 57.2%, B 49.9%; Elo A 1526.2, B 1304.5; model uncertainty 0.0345
* Form inputs: days since last match A 406, B 120; matches on record A 38, B 57; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10POPTOD-POP  (YES = Giulia Safina Popa)
Model: 83%
Kalshi: 63%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.000, surface_dev_loose -0.013, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Teodora Miron (`KXITFWMATCH-26NOV10SHAMIR-MIR`) | 0.52 / 0.66 (73) | 59.0% | 16.7% | 31.1% | 28.7% [24.4%-32.5%] | -- | -- | -- | -- | PASS | -42.3 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofia Shapatava (`KXITFWMATCH-26NOV10SHAMIR-SHA`) | 0.34 / 0.48 (15) | 41.0% | 83.3% | 68.9% | 71.3% [67.5%-75.6%] | -- | -- | -- | -- | PASS | +42.3 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2642.0, B 136.0; serve-point win A 57.8%, B 49.5%; Elo A 1479.8, B 1320.1; model uncertainty 0.0404
* Form inputs: days since last match A 196, B 476; matches on record A 1029, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10SHAMIR-SHA  (YES = Sofia Shapatava)
Model: 83%
Kalshi: 41%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.035, surface_pool_high -0.037, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Li / Zhang (`KXITFWDOUBLES-26NOV10SUNZHALIXZHA-LIXZHA`) | 0.24 / 0.35 (38) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sun / Zhao (`KXITFWDOUBLES-26NOV10SUNZHALIXZHA-SUNZHA`) | 0.58 / 0.78 (10) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Remy Bertola vs Lorenzo Carboni -- ATP Challenger Hersonissos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T13:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200329:212077:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Remy Bertola (`KXATPCHALLENGERMATCH-26NOV10BERCAR-BER`) | 0.71 / 0.73 (2064) | 72.0% | 67.7% | 60.2% | 63.1% [60.2%-67.8%] | -- | 71.7% | -- | INSUFFICIENT_INPUTS | PASS | -4.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorenzo Carboni (`KXATPCHALLENGERMATCH-26NOV10BERCAR-CAR`) | 0.28 / 0.29 (605) | 28.5% | 32.3% | 39.8% | 36.9% [32.2%-39.8%] | -- | 28.2% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +3.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4817.0, B 3055.0; serve-point win A 62.3%, B 41.2%; Elo A 1605.6, B 1476.3; model uncertainty 0.0382
* Form inputs: days since last match A 12, B 28; matches on record A 472, B 176; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.029, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Victor Vlad Cornea / Kai Wehnelt vs Umberto Giuseppe Capitanio / Tyler Haddorff -- ATP Challenger Hersonissos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-10T13:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10CORWEHCAPHAD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Umberto Giuseppe Capitanio / Tyler Haddorff (`KXATPCHALLENGERDOUBLES-26NOV10CORWEHCAPHAD-CAPHAD`) | 0.05 / 0.50 (3) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victor Vlad Cornea / Kai Wehnelt (`KXATPCHALLENGERDOUBLES-26NOV10CORWEHCAPHAD-CORWEH`) | 0.89 / 0.95 (325) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Oskari Paldanius vs Raul Brancaccio -- ATP Challenger Hersonissos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 13:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T13:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:134840:213619:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raul Brancaccio (`KXATPCHALLENGERMATCH-26NOV10PALBRA-BRA`) | 0.48 / 0.50 (24) | 49.0% | 70.1% | 73.6% | 72.8% [68.8%-77.6%] | -- | 49.8% | -- | INSUFFICIENT_INPUTS | WATCH | +21.1 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oskari Paldanius (`KXATPCHALLENGERMATCH-26NOV10PALBRA-PAL`) | 0.44 / 0.52 (89) | 48.0% | 29.9% | 26.4% | 27.3% [22.4%-31.2%] | -- | 49.4% | -- | INSUFFICIENT_INPUTS | PASS | -18.1 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1146.0, B 5606.0; serve-point win A 58.5%, B 37.4%; Elo A 1363.6, B 1529.6; model uncertainty 0.0442
* Form inputs: days since last match A 112, B 21; matches on record A 32, B 654; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV10PALBRA-BRA  (YES = Raul Brancaccio)
Model: 70%
Kalshi: 49%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.041, surface_pool_high +0.040, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; WIDE_SPREAD

## Tomas Martin Etcheverry vs Thiago Agustin Tirante -- ATP Stockholm R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-10 16:30Z
* Current expected start: 2026-11-10 13:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 22:48Z
* Recommended handicap-by time: 2026-11-10 12:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-10T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144869:202058:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Martin Etcheverry (`KXATPMATCH-26NOV10ETCTIR-ETC`) | 0.55 / 0.56 (1549) | 55.5% | 47.1% | 49.5% | 50.9% [50.0%-52.4%] | 55.6% | 54.5% | 55.6% | MODEL_LONE_OUTLIER | PASS | -8.4 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Thiago Agustin Tirante (`KXATPMATCH-26NOV10ETCTIR-TIR`) | 0.44 / 0.45 (12) | 44.5% | 52.9% | 50.5% | 49.1% [47.6%-50.0%] | 44.4% | 52.5% | 44.4% | MODEL_LONE_OUTLIER | WATCH | +8.4 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5740.0, B 5643.0; serve-point win A 68.6%, B 30.8%; Elo A 1781.4, B 1739.0; model uncertainty 0.0118
* Form inputs: days since last match A 4, B 1; matches on record A 652, B 494; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.014, surface_dev_loose -0.005, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV10ETCTIR-25` Over 24.5 games: 0.46/0.48 mid 47.0%, model 58.6% (projection_v2.0 (prediction ledger)) -- gap +11.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10ETCTIR-ETC2` Will Tomas Martin Etcheverry win at least 1.5 more games than Thiago Agustin Tirante?: 0.48/0.51 mid 49.5%, model 38.3% (projection_v2.0 (prediction ledger)) -- gap -11.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10ETCTIR-ETC5` Will Tomas Martin Etcheverry win at least 4.5 more games than Thiago Agustin Tirante?: 0.17/0.23 mid 20.0%, model 9.4% (projection_v2.0 (prediction ledger)) -- gap -10.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10ETCTIR-TIR21` Will Thiago Agustin Tirante win the Tomas Martin Etcheverry vs Thiago Agustin Tirante match by a set score of 2-1?: 0.11/0.21 mid 16.0%, model 25.9% (projection_v2.0 (prediction ledger)) -- gap +9.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV10ETCTIR-30` Over 29.5 games: 0.31/0.35 mid 33.0%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10ETCTIR-1-ETC` Will Tomas Martin Etcheverry win set 1 in the Tomas Martin Etcheverry vs Thiago Agustin Tirante match: 0.53/0.56 mid 54.5%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap -6.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10ETCTIR-ETC20` Will Tomas Martin Etcheverry win the Tomas Martin Etcheverry vs Thiago Agustin Tirante match by a set score of 2-0?: 0.23/0.36 mid 29.5%, model 23.1% (projection_v2.0 (prediction ledger)) -- gap -6.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10ETCTIR-1-TIR` Will Thiago Agustin Tirante win set 1 in the Tomas Martin Etcheverry vs Thiago Agustin Tirante match: 0.44/0.48 mid 46.0%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV10ETCTIR-20` Over 19.5 games: 0.79/0.87 mid 83.0%, model 88.5% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10ETCTIR-TIR2` Will Thiago Agustin Tirante win at least 1.5 more games than Tomas Martin Etcheverry?: 0.36/0.42 mid 39.0%, model 43.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10ETCTIR-2-TIR` Will Thiago Agustin Tirante win set 2 in the Tomas Martin Etcheverry vs Thiago Agustin Tirante match: 0.01/0.95 mid 48.0%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10ETCTIR-TIR20` Will Thiago Agustin Tirante win the Tomas Martin Etcheverry vs Thiago Agustin Tirante match by a set score of 2-0?: 0.25/0.31 mid 28.0%, model 27.0% (projection_v2.0 (prediction ledger)) -- gap -1.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10ETCTIR-ETC21` Will Tomas Martin Etcheverry win the Tomas Martin Etcheverry vs Thiago Agustin Tirante match by a set score of 2-1?: 0.18/0.28 mid 23.0%, model 24.0% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10ETCTIR-2-ETC` Will Tomas Martin Etcheverry win set 2 in the Tomas Martin Etcheverry vs Thiago Agustin Tirante match: 0.03/0.95 mid 49.0%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lorenzo Sonego vs Quentin Halys -- ATP Stockholm 1/16 F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-10 13:00Z
* Current expected start: 2026-11-10 13:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 22:48Z
* Recommended handicap-by time: 2026-11-10 12:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+30_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-10T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111460:132283:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Quentin Halys (`KXATPMATCH-26NOV10SONHAL-HAL`) | 0.53 / 0.55 (32033) | 54.0% | 57.7% | 60.6% | 60.6% [59.7%-60.7%] | 54.3% | 53.6% | 53.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.7 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Lorenzo Sonego (`KXATPMATCH-26NOV10SONHAL-SON`) | 0.46 / 0.47 (382) | 46.5% | 42.3% | 39.4% | 39.4% [39.3%-40.3%] | 45.7% | 46.3% | 46.0% | MODEL_LONE_OUTLIER | PASS | -4.2 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4585.0, B 6418.0; serve-point win A 68.6%, B 29.7%; Elo A 1779.2, B 1843.7; model uncertainty 0.0048
* Form inputs: days since last match A 1, B 4; matches on record A 706, B 843; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV10SONHAL-HAL21` Will Quentin Halys win the Lorenzo Sonego vs Quentin Halys match by a set score of 2-1?: 0.15/0.23 mid 19.0%, model 27.3% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10SONHAL-HAL5` Will Quentin Halys win at least 4.5 more games than Lorenzo Sonego?: 0.14/0.27 mid 20.5%, model 12.8% (projection_v2.0 (prediction ledger)) -- gap -7.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV10SONHAL-30` Over 29.5 games: 0.30/0.35 mid 32.5%, model 40.0% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10SONHAL-SON20` Will Lorenzo Sonego win the Lorenzo Sonego vs Quentin Halys match by a set score of 2-0?: 0.25/0.28 mid 26.5%, model 20.1% (projection_v2.0 (prediction ledger)) -- gap -6.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10SONHAL-2-HAL` Will Quentin Halys win set 2 in the Lorenzo Sonego vs Quentin Halys match: 0.04/0.94 mid 49.0%, model 55.2% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV10SONHAL-SON2` Will Lorenzo Sonego win at least 1.5 more games than Quentin Halys?: 0.38/0.41 mid 39.5%, model 33.6% (projection_v2.0 (prediction ledger)) -- gap -5.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV10SONHAL-25` Over 24.5 games: 0.53/0.54 mid 53.5%, model 58.9% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV10SONHAL-20` Over 19.5 games: 0.82/0.87 mid 84.5%, model 89.0% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10SONHAL-SON21` Will Lorenzo Sonego win the Lorenzo Sonego vs Quentin Halys match by a set score of 2-1?: 0.17/0.20 mid 18.5%, model 22.2% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10SONHAL-1-HAL` Will Quentin Halys win set 1 in the Lorenzo Sonego vs Quentin Halys match: 0.50/0.53 mid 51.5%, model 55.2% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV10SONHAL-1-SON` Will Lorenzo Sonego win set 1 in the Lorenzo Sonego vs Quentin Halys match: 0.47/0.50 mid 48.5%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV10SONHAL-2-SON` Will Lorenzo Sonego win set 2 in the Lorenzo Sonego vs Quentin Halys match: 0.03/0.94 mid 48.5%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV10SONHAL-HAL2` Will Quentin Halys win at least 1.5 more games than Lorenzo Sonego?: 0.44/0.47 mid 45.5%, model 48.6% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10SONHAL-HAL20` Will Quentin Halys win the Lorenzo Sonego vs Quentin Halys match by a set score of 2-0?: 0.29/0.32 mid 30.5%, model 30.4% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Ekaterina Agureeva (`KXITFWMATCH-26NOV10AGUVAJ-AGU`) | 0.83 / 0.88 (6) | 85.5% | 84.8% | 66.1% | 77.3% [75.6%-79.6%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Klara Vaja (`KXITFWMATCH-26NOV10AGUVAJ-VAJ`) | 0.12 / 0.17 (35) | 14.5% | 15.2% | 33.9% | 22.7% [20.4%-24.4%] | -- | -- | -- | -- | PASS | +0.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 144.0, B 157.0; serve-point win A 57.9%, B 49.8%; Elo A 1386.4, B 1165.5; model uncertainty 0.0199
* Form inputs: days since last match A 434, B 343; matches on record A 17, B 33; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.016, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Federica Bilardo (`KXITFWMATCH-26NOV10DROBIL-BIL`) | 0.31 / 0.46 (10) | 38.5% | 90.4% | 51.6% | 77.3% [72.6%-83.8%] | -- | -- | -- | -- | PASS | +51.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mariia Drobysheva (`KXITFWMATCH-26NOV10DROBIL-DRO`) | 0.50 / 0.65 (5) | 57.5% | 9.6% | 48.4% | 22.7% [16.2%-27.4%] | -- | -- | -- | -- | PASS | -47.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 310.0, B 471.0; serve-point win A 49.1%, B 41.1%; Elo A 1283.7, B 1546.8; model uncertainty 0.0561
* Form inputs: days since last match A 406, B 203; matches on record A 7, B 327; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10DROBIL-BIL  (YES = Federica Bilardo)
Model: 90%
Kalshi: 38%
Gap: +52 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.031, surface_pool_high +0.016, surface_dev_loose -0.008, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Stefanie Auer (`KXITFWMATCH-26NOV10GLUAUE-AUE`) | 0.44 / 0.74 (1) | 59.0% | 82.7% | 22.2% | 60.6% [56.4%-64.6%] | -- | -- | -- | -- | PASS | +23.7 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andreya Glushkova (`KXITFWMATCH-26NOV10GLUAUE-GLU`) | 0.29 / 0.53 (1) | 41.0% | 17.3% | 77.8% | 39.4% [35.4%-43.6%] | -- | -- | -- | -- | PASS | -23.7 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 453.0; serve-point win A 49.1%, B 43.9%; Elo A 1152.5, B 1225.8; model uncertainty 0.0413
* Form inputs: days since last match A 707, B 308; matches on record A 4, B 171; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10GLUAUE-AUE  (YES = Stefanie Auer)
Model: 83%
Kalshi: 59%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.042, surface_pool_high -0.041, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Karina Maria Capuzu (`KXITFWMATCH-26NOV10GOMCAP-CAP`) | 0.09 / 0.15 (29) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Victoria Gomez O'Hayon (`KXITFWMATCH-26NOV10GOMCAP-GOM`) | 0.87 / 0.91 (5) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Ksenia Meshcheryakova (`KXITFWMATCH-26NOV10MESZIA-MES`) | 0.50 / 0.69 (80) | 59.5% | 10.6% | 36.4% | 17.5% [15.5%-18.9%] | -- | -- | -- | -- | PASS | -48.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alisa Ziatdinova (`KXITFWMATCH-26NOV10MESZIA-ZIA`) | 0.37 / 0.48 (48) | 42.5% | 89.4% | 63.6% | 82.5% [81.1%-84.5%] | -- | -- | -- | -- | PASS | +46.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 335.0, B 165.0; serve-point win A 48.9%, B 41.8%; Elo A 980.4, B 1269.4; model uncertainty 0.0168
* Form inputs: days since last match A 196, B 350; matches on record A 75, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10MESZIA-ZIA  (YES = Alisa Ziatdinova)
Model: 89%
Kalshi: 42%
Gap: +47 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.007, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Maria Shmeleva (`KXITFWMATCH-26NOV10SUSSHM-SHM`) | 0.71 / 0.76 (109) | 73.5% | 51.0% | 62.1% | 55.9% [55.3%-56.9%] | -- | -- | -- | -- | PASS | -22.5 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofiia Suslova (`KXITFWMATCH-26NOV10SUSSHM-SUS`) | 0.21 / 0.23 (30) | 22.0% | 49.0% | 37.9% | 44.1% [43.1%-44.7%] | -- | -- | -- | -- | PASS | +27.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 719.0, B 189.0; serve-point win A 51.1%, B 48.7%; Elo A 1288.2, B 1321.9; model uncertainty 0.008
* Form inputs: days since last match A 252, B 371; matches on record A 38, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10SUSSHM-SUS  (YES = Sofiia Suslova)
Model: 49%
Kalshi: 22%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Polina Starkova (`KXITFWMATCH-26NOV10SUVSTA-STA`) | 0.77 / 0.89 (5) | 83.0% | 71.3% | 66.1% | 60.6% [60.6%-62.7%] | -- | -- | -- | -- | PASS | -11.7 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentina Suvirdjonkova (`KXITFWMATCH-26NOV10SUVSTA-SUV`) | 0.12 / 0.17 (35) | 14.5% | 28.7% | 33.9% | 39.4% [37.3%-39.5%] | -- | -- | -- | -- | PASS | +14.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 121.0, B 184.0; serve-point win A 49.5%, B 46.3%; Elo A 1217.0, B 1289.7; model uncertainty 0.0105
* Form inputs: days since last match A 308, B 301; matches on record A 5, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.010, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Daniela Darta Feldmane (`KXITFWMATCH-26NOV10TURFEL-FEL`) | 0.30 / 0.36 (44) | 33.0% | 44.7% | 58.5% | 45.2% [41.5%-48.4%] | -- | -- | -- | -- | PASS | +11.7 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Doga Turkmen (`KXITFWMATCH-26NOV10TURFEL-TUR`) | 0.61 / 0.70 (9) | 65.5% | 55.3% | 41.5% | 54.8% [51.6%-58.5%] | -- | -- | -- | -- | PASS | -10.2 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 739.0, B 630.0; serve-point win A 50.9%, B 50.1%; Elo A 1294.0, B 1221.8; model uncertainty 0.0345
* Form inputs: days since last match A 36, B 301; matches on record A 260, B 20; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Chrystal Lopez (`KXITFWMATCH-26NOV10TZELOP-LOP`) | 0.18 / 0.25 (39) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mu Jie Tzeng (`KXITFWMATCH-26NOV10TZELOP-TZE`) | 0.78 / 0.79 (6) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Denise Valente (`KXITFWMATCH-26NOV10VALYEM-VAL`) | 0.86 / 0.95 (10) | 90.5% | 75.4% | 32.9% | 58.5% [57.4%-59.5%] | -- | -- | -- | -- | PASS | -15.1 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mariya Yemshanova (`KXITFWMATCH-26NOV10VALYEM-YEM`) | 0.05 / 0.11 (33) | 8.0% | 24.6% | 67.1% | 41.5% [40.5%-42.6%] | -- | -- | -- | -- | PASS | +16.6 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1031.0, B 91.0; serve-point win A 55.6%, B 49.6%; Elo A 1297.3, B 1224.9; model uncertainty 0.0105
* Form inputs: days since last match A 203, B 196; matches on record A 157, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10VALYEM-YEM  (YES = Mariya Yemshanova)
Model: 25%
Kalshi: 8%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Anais Gabriel (`KXITFWMATCH-26NOV10WIRGAB-GAB`) | 0.49 / 0.56 (6) | 52.5% | 20.2% | 30.9% | 26.8% [24.3%-28.2%] | -- | -- | -- | -- | PASS | -32.4 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Angelina Wirges (`KXITFWMATCH-26NOV10WIRGAB-WIR`) | 0.48 / 0.51 (7) | 49.5% | 79.8% | 69.1% | 73.2% [71.8%-75.7%] | -- | -- | -- | -- | PASS | +30.4 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1745.0, B 534.0; serve-point win A 53.2%, B 53.0%; Elo A 1408.6, B 1217.3; model uncertainty 0.0194
* Form inputs: days since last match A 203, B 245; matches on record A 257, B 13; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10WIRGAB-WIR  (YES = Angelina Wirges)
Model: 80%
Kalshi: 50%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.022, surface_pool_high -0.013, surface_dev_loose +0.009, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Theresa Stabauer (`KXITFWMATCH-26NOV10YAZSTA-STA`) | 0.63 / 0.83 (1) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| yasaman yazdani (`KXITFWMATCH-26NOV10YAZSTA-YAZ`) | 0.22 / 0.71 (3) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Arian Barbic (`KXITFMATCH-26NOV10BARDUN-BAR`) | 0.59 / 0.72 (5) | 65.5% | 55.2% | 59.4% | 51.0% [51.0%-52.0%] | -- | -- | -- | -- | PASS | -10.3 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Phil Dungs (`KXITFMATCH-26NOV10BARDUN-DUN`) | 0.36 / 0.37 (44) | 36.5% | 44.8% | 40.6% | 49.0% [48.0%-49.0%] | -- | -- | -- | -- | PASS | +8.3 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 155.0, B 38.0; serve-point win A 64.0%, B 37.1%; Elo A 1289.6, B 1282.2; model uncertainty 0.0049
* Form inputs: days since last match A 301, B 378; matches on record A 3, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| John Bothma (`KXITFMATCH-26NOV10BOTKLU-BOT`) | 0.83 / 0.89 (3) | 86.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jan Kluczynski (`KXITFMATCH-26NOV10BOTKLU-KLU`) | 0.07 / 0.13 (28) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Mathys Braun (`KXITFMATCH-26NOV10HAMBRA-BRA`) | 0.31 / 0.39 (42) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Martin Hammond (`KXITFMATCH-26NOV10HAMBRA-HAM`) | 0.57 / 0.65 (9) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Jack Karlsson Wistrand (`KXITFMATCH-26NOV10KARKNI-KAR`) | 0.76 / 0.85 (136) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ollie Knight (`KXITFMATCH-26NOV10KARKNI-KNI`) | 0.13 / 0.19 (24) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Dorian Kos (`KXITFMATCH-26NOV10KOSKOZ-KOS`) | 0.07 / 0.11 (110) | 9.0% | 50.8% | 65.9% | 52.1% [51.0%-52.1%] | -- | -- | -- | -- | PASS | +41.8 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Matyas Kozlovsky (`KXITFMATCH-26NOV10KOSKOZ-KOZ`) | 0.87 / 0.93 (39) | 90.0% | 49.2% | 34.1% | 47.9% [47.9%-48.9%] | -- | -- | -- | -- | PASS | -40.8 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 172.0; serve-point win A 56.9%, B 43.2%; Elo A 1285.0, B 1273.5; model uncertainty 0.0053
* Form inputs: days since last match A 2002, B 210; matches on record A 1, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10KOSKOZ-KOS  (YES = Dorian Kos)
Model: 51%
Kalshi: 9%
Gap: +42 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.011, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Brian Dal Zilio (`KXITFMATCH-26NOV10OKTDAL-DAL`) | 0.09 / 0.19 (30) | 14.0% | 32.2% | 46.3% | 41.7% [40.6%-41.7%] | -- | -- | -- | -- | PASS | +18.2 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ramazan Kaan Oktay (`KXITFMATCH-26NOV10OKTDAL-OKT`) | 0.82 / 0.85 (18) | 83.5% | 67.8% | 53.7% | 58.3% [58.3%-59.4%] | -- | -- | -- | -- | PASS | -15.7 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 266.0, B 181.0; serve-point win A 59.3%, B 44.2%; Elo A 1249.0, B 1183.2; model uncertainty 0.0058
* Form inputs: days since last match A 259, B 196; matches on record A 6, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10OKTDAL-DAL  (YES = Brian Dal Zilio)
Model: 32%
Kalshi: 14%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Gilberto Ravasio (`KXITFMATCH-26NOV10RAVWAG-RAV`) | 0.61 / 0.73 (1) | 67.0% | 47.2% | 18.4% | 50.0% [48.4%-52.1%] | -- | -- | -- | -- | PASS | -19.8 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lars Wagenaar (`KXITFMATCH-26NOV10RAVWAG-WAG`) | 0.31 / 0.32 (36) | 31.5% | 52.8% | 81.6% | 50.0% [47.9%-51.6%] | -- | -- | -- | -- | PASS | +21.3 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 633.0, B 53.0; serve-point win A 55.5%, B 44.0%; Elo A 1182.8, B 1174.6; model uncertainty 0.0184
* Form inputs: days since last match A 196, B 448; matches on record A 16, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10RAVWAG-WAG  (YES = Lars Wagenaar)
Model: 53%
Kalshi: 32%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Georgios Dimitriou (`KXITFMATCH-26NOV10ROLDIM-DIM`) | 0.07 / 0.13 (28) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dominique Rolland (`KXITFMATCH-26NOV10ROLDIM-ROL`) | 0.84 / 0.95 (319) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Louis Herman (`KXITFMATCH-26NOV10SCHHER-HER`) | 0.45 / 0.48 (48) | 46.5% | 48.2% | 15.3% | 50.0% [49.0%-52.1%] | -- | -- | -- | -- | PASS | +1.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Frederic Schlossmann (`KXITFMATCH-26NOV10SCHHER-SCH`) | 0.43 / 0.56 (10) | 49.5% | 51.7% | 84.7% | 50.0% [47.9%-51.0%] | -- | -- | -- | -- | PASS | +2.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 761.0; serve-point win A 59.8%, B 40.5%; Elo A 1178.2, B 1181.9; model uncertainty 0.0155
* Form inputs: days since last match A 1050, B 273; matches on record A 4, B 38; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.021, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Yahor Slizevich (`KXITFMATCH-26NOV10VANSLI-SLI`) | 0.24 / 0.32 (1) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Louis Van Herck (`KXITFMATCH-26NOV10VANSLI-VAN`) | 0.64 / 0.71 (0) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Oliwier Sterniczuk (`KXITFMATCH-26NOV10ZUSSTE-STE`) | 0.35 / 0.44 (10) | 39.5% | 82.9% | 60.4% | 81.3% [80.6%-82.5%] | -- | -- | -- | -- | PASS | +43.4 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Richard Zusman (`KXITFMATCH-26NOV10ZUSSTE-ZUS`) | 0.58 / 0.59 (3) | 58.5% | 17.1% | 39.6% | 18.7% [17.5%-19.4%] | -- | -- | -- | -- | PASS | -41.4 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 633.0, B 94.0; serve-point win A 54.2%, B 38.6%; Elo A 1045.7, B 1316.0; model uncertainty 0.0092
* Form inputs: days since last match A 441, B 196; matches on record A 61, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10ZUSSTE-STE  (YES = Oliwier Sterniczuk)
Model: 83%
Kalshi: 40%
Gap: +43 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.007, surface_dev_loose -0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Romy De Baene (`KXITFWMATCH-26NOV10DEBEHR-DEB`) | 0.34 / 0.40 (41) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sophie Ehrenbergerova (`KXITFWMATCH-26NOV10DEBEHR-EHR`) | 0.53 / 0.59 (3) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Nadia Affelt (`KXITFWMATCH-26NOV10DJAAFF-AFF`) | 0.38 / 0.44 (50) | 41.0% | 70.7% | 50.0% | 61.6% [60.5%-62.6%] | -- | -- | -- | -- | PASS | +29.7 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Louanne Djafari (`KXITFWMATCH-26NOV10DJAAFF-DJA`) | 0.52 / 0.59 (60) | 55.5% | 29.3% | 50.0% | 38.4% [37.4%-39.5%] | -- | -- | -- | -- | PASS | -26.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 165.0, B 146.0; serve-point win A 52.2%, B 43.7%; Elo A 1179.4, B 1268.7; model uncertainty 0.0102
* Form inputs: days since last match A 280, B 455; matches on record A 7, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10DJAAFF-AFF  (YES = Nadia Affelt)
Model: 71%
Kalshi: 41%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Maria Garcia Cid (`KXITFWMATCH-26NOV10GARPET-GAR`) | 0.70 / 0.78 (5) | 74.0% | 84.2% | 88.3% | 79.7% [69.9%-84.2%] | -- | -- | -- | -- | PASS | +10.2 pp | REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Petkovic (`KXITFWMATCH-26NOV10GARPET-PET`) | 0.21 / 0.26 (36) | 23.5% | 15.8% | 11.7% | 20.3% [15.8%-30.1%] | -- | -- | -- | -- | PASS | -7.7 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1857.0, B 1778.0; serve-point win A 57.1%, B 50.4%; Elo A 1513.6, B 1402.9; model uncertainty 0.0715
* Form inputs: days since last match A 28, B 113; matches on record A 87, B 78; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.011, surface_dev_loose +0.021, surface_dev_tight -0.019
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Astrid Lew Yan Foon (`KXITFWMATCH-26NOV10LEWRAG-LEW`) | 0.49 / 0.56 (48) | 52.5% | 57.8% | 39.4% | 45.7% [42.0%-53.2%] | -- | -- | -- | -- | PASS | +5.3 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Angelica Raggi (`KXITFWMATCH-26NOV10LEWRAG-RAG`) | 0.42 / 0.49 (54) | 45.5% | 42.2% | 60.6% | 54.3% [46.8%-58.0%] | -- | -- | -- | -- | PASS | -3.3 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1722.0, B 2349.0; serve-point win A 54.1%, B 47.4%; Elo A 1525.8, B 1503.9; model uncertainty 0.0558
* Form inputs: days since last match A 126, B 203; matches on record A 180, B 320; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Leila Fabbri (`KXITFWMATCH-26NOV10MEWFAB-FAB`) | 0.33 / 0.42 (48) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daisy Mewett (`KXITFWMATCH-26NOV10MEWFAB-MEW`) | 0.54 / 0.67 (72) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Ariadna Garcia-Patron Canals (`KXITFWMATCH-26NOV10NEWGAR-GAR`) | 0.56 / 0.67 (81) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eloise Newberry (`KXITFWMATCH-26NOV10NEWGAR-NEW`) | 0.31 / 0.48 (101) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Luisa Fusil (`KXITFWMATCH-26NOV10PARFUS-FUS`) | 0.13 / 0.14 (155) | 13.5% | 66.6% | 50.0% | 62.6% [61.6%-62.6%] | -- | -- | -- | -- | PASS | +53.1 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Serena Paris (`KXITFWMATCH-26NOV10PARFUS-PAR`) | 0.84 / 0.92 (5) | 88.0% | 33.4% | 50.0% | 37.4% [37.4%-38.4%] | -- | -- | -- | -- | PASS | -54.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 52.3%, B 44.5%; Elo A 1224.7, B 1311.5; model uncertainty 0.0051
* Form inputs: days since last match A 707, B 735; matches on record A 5, B 3; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10PARFUS-FUS  (YES = Luisa Fusil)
Model: 67%
Kalshi: 14%
Gap: +53 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Tina Nadine Smith (`KXITFWMATCH-26NOV10SVASMI-SMI`) | 0.66 / 0.76 (56) | 71.0% | 90.2% | 75.6% | 78.4% [76.0%-82.1%] | -- | -- | -- | -- | PASS | +19.2 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Laura Svatikova (`KXITFWMATCH-26NOV10SVASMI-SVA`) | 0.23 / 0.29 (44) | 26.0% | 9.8% | 24.4% | 21.6% [17.9%-24.0%] | -- | -- | -- | -- | PASS | -16.2 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1657.0, B 2598.0; serve-point win A 49.8%, B 40.5%; Elo A 1303.4, B 1554.8; model uncertainty 0.0307
* Form inputs: days since last match A 357, B 294; matches on record A 244, B 342; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10SVASMI-SMI  (YES = Tina Nadine Smith)
Model: 90%
Kalshi: 71%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.024, surface_dev_loose +0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Antonia Stoyanov (`KXITFWMATCH-26NOV10VANSTO-STO`) | 0.88 / 0.93 (7) | 90.5% | 75.7% | 63.1% | 59.6% [55.3%-62.6%] | -- | -- | -- | -- | PASS | -14.8 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vicky Van de Peer (`KXITFWMATCH-26NOV10VANSTO-VAN`) | 0.05 / 0.08 (28) | 6.5% | 24.3% | 36.9% | 40.5% [37.4%-44.7%] | -- | -- | -- | -- | PASS | +17.8 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1898.0, B 608.0; serve-point win A 49.4%, B 45.4%; Elo A 1398.5, B 1451.4; model uncertainty 0.0366
* Form inputs: days since last match A 427, B 210; matches on record A 239, B 24; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10VANSTO-VAN  (YES = Vicky Van de Peer)
Model: 24%
Kalshi: 6%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mattia Bellucci vs Cosme Rolland de Ravel -- ATP Challenger Orleans R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T14:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BELROL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mattia Bellucci (`KXATPCHALLENGERMATCH-26NOV10BELROL-BEL`) | 0.76 / 0.78 (1451) | 77.0% | 87.2% | -- | -- [-----] | -- | -- | -- | -- | -- | +10.2 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Cosme Rolland de Ravel (`KXATPCHALLENGERMATCH-26NOV10BELROL-ROL`) | 0.22 / 0.24 (1389) | 23.0% | 12.8% | -- | -- [-----] | -- | -- | -- | -- | -- | -10.2 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 68.1%, B 41.0%; Elo A 1824.5, B 1508.9; model uncertainty None
* Form inputs: days since last match A 5, B 21; matches on record A 435, B 14; data quality C
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE

## Buvaysar Gadamauri vs Dusan Lajovic -- ATP Challenger Orleans R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T14:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10GADLAJ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Buvaysar Gadamauri (`KXATPCHALLENGERMATCH-26NOV10GADLAJ-GAD`) | 0.49 / 0.50 (24) | 49.5% | 51.8% | -- | -- [-----] | -- | -- | -- | -- | -- | +2.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Dusan Lajovic (`KXATPCHALLENGERMATCH-26NOV10GADLAJ-LAJ`) | 0.51 / 0.52 (1521) | 51.5% | 48.2% | -- | -- [-----] | -- | -- | -- | -- | -- | -3.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 64.2%, B 36.1%; Elo A 1574.5, B 1668.8; model uncertainty None
* Form inputs: days since last match A 28, B 22; matches on record A 312, B 1071; data quality A
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Adrian Andreev vs Benjamin Pietri -- ATP Challenger Hersonissos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ANDPIE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Andreev (`KXATPCHALLENGERMATCH-26NOV10ANDPIE-AND`) | 0.66 / 0.68 (624) | 67.0% | 77.2% | -- | -- [-----] | -- | -- | -- | -- | -- | +10.2 pp | REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Benjamin Pietri (`KXATPCHALLENGERMATCH-26NOV10ANDPIE-PIE`) | 0.32 / 0.35 (585) | 33.5% | 22.8% | -- | -- [-----] | -- | -- | -- | -- | -- | -10.7 pp | REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 61.9%, B 43.8%; Elo A 1532.7, B 1291.0; model uncertainty None
* Form inputs: days since last match A 49, B 63; matches on record A 361, B 233; data quality A
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Carlo Alberto Caniato vs Gilles Arnaud Bailly -- ATP Challenger Hersonissos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10CANARN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gilles Arnaud Bailly (`KXATPCHALLENGERMATCH-26NOV10CANARN-ARN`) | 0.36 / 0.37 (584) | 36.5% | 41.3% | -- | -- [-----] | -- | -- | -- | -- | -- | +4.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Carlo Alberto Caniato (`KXATPCHALLENGERMATCH-26NOV10CANARN-CAN`) | 0.63 / 0.64 (584) | 63.5% | 58.7% | -- | -- [-----] | -- | -- | -- | -- | -- | -4.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 65.3%, B 36.4%; Elo A 1462.2, B 1517.4; model uncertainty None
* Form inputs: days since last match A 21, B 23; matches on record A 154, B 212; data quality A
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Pavlos Tsitsipas vs Cezar Cretu (b. 2001) -- ATP Challenger Hersonissos R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-10T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10TSICRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cezar Cretu (b. 2001) (`KXATPCHALLENGERMATCH-26NOV10TSICRE-CRE`) | 0.89 / 0.91 (662) | 90.0% | 88.7% | -- | -- [-----] | -- | -- | -- | -- | -- | -1.3 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Pavlos Tsitsipas (`KXATPCHALLENGERMATCH-26NOV10TSICRE-TSI`) | 0.10 / 0.11 (584) | 10.5% | 11.3% | -- | -- [-----] | -- | -- | -- | -- | -- | +0.8 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 56.3%, B 34.2%; Elo A 1177.4, B 1482.5; model uncertainty None
* Form inputs: days since last match A 196, B 28; matches on record A 86, B 422; data quality B
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

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
| Iliia Dashkevich (`KXITFWMATCH-26NOV10DASTHO-DAS`) | 0.30 / 0.75 (3) | 52.5% | 41.6% | 60.1% | 48.9% [47.9%-50.0%] | -- | -- | -- | -- | PASS | -10.9 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Nehanda Thomias (`KXITFWMATCH-26NOV10DASTHO-THO`) | 0.55 / 0.83 (3) | 69.0% | 58.4% | 39.9% | 51.1% [50.0%-52.1%] | -- | -- | -- | -- | PASS | -10.6 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 300.0; serve-point win A 51.8%, B 46.6%; Elo A 1187.5, B 1193.8; model uncertainty 0.0107
* Form inputs: days since last match A 924, B 301; matches on record A 10, B 21; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Silvia Caliman (`KXITFWMATCH-26NOV10GIRCAL-CAL`) | 0.14 / 0.18 (30) | 16.0% | 28.4% | 63.2% | 43.6% [41.5%-44.6%] | -- | -- | -- | -- | PASS | +12.4 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ana Giraldi Requena (`KXITFWMATCH-26NOV10GIRCAL-GIR`) | 0.82 / 0.86 (36) | 84.0% | 71.6% | 36.8% | 56.4% [55.4%-58.5%] | -- | -- | -- | -- | PASS | -12.4 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 883.0, B 92.0; serve-point win A 51.7%, B 52.6%; Elo A 1282.0, B 1231.9; model uncertainty 0.0158
* Form inputs: days since last match A 357, B 322; matches on record A 195, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Alexandra Chapurina (`KXITFWMATCH-26NOV10HARCHA-CHA`) | 0.69 / 0.75 (5) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ema Harajda (`KXITFWMATCH-26NOV10HARCHA-HAR`) | 0.23 / 0.27 (20) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Min Liu (`KXITFWMATCH-26NOV10LIUPAR-LIU`) | 0.58 / 0.63 (52) | 60.5% | 32.3% | 17.6% | 32.6% [30.7%-34.0%] | -- | -- | -- | -- | PASS | -28.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Pares Bergnes de las Casas (`KXITFWMATCH-26NOV10LIUPAR-PAR`) | 0.35 / 0.36 (39) | 35.5% | 67.7% | 82.4% | 67.4% [66.0%-69.3%] | -- | -- | -- | -- | PASS | +32.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 746.0, B 161.0; serve-point win A 53.6%, B 43.0%; Elo A 1181.5, B 1296.6; model uncertainty 0.0163
* Form inputs: days since last match A 148, B 196; matches on record A 143, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10LIUPAR-PAR  (YES = Maria Pares Bergnes de las Casas)
Model: 68%
Kalshi: 36%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Cecilia Manitto (`KXITFWMATCH-26NOV10PARMAN-MAN`) | 0.21 / 0.29 (40) | 25.0% | 44.0% | 75.3% | 50.0% [48.9%-51.1%] | -- | -- | -- | -- | PASS | +19.0 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ginevra Parentini Vallega Montebruno (`KXITFWMATCH-26NOV10PARMAN-PAR`) | 0.67 / 0.75 (18) | 71.0% | 56.0% | 24.7% | 50.0% [48.9%-51.1%] | -- | -- | -- | -- | PASS | -15.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 813.0, B 52.0; serve-point win A 53.8%, B 47.4%; Elo A 1271.0, B 1264.1; model uncertainty 0.0107
* Form inputs: days since last match A 273, B 350; matches on record A 143, B 10; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10PARMAN-MAN  (YES = Cecilia Manitto)
Model: 44%
Kalshi: 25%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Anna Cabassers Morros (`KXITFWMATCH-26NOV10QUECAB-CAB`) | 0.23 / 0.29 (5) | 26.0% | 40.0% | 43.1% | 44.7% [44.7%-44.7%] | -- | -- | -- | -- | PASS | +14.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marina Quesada Oyonarte (`KXITFWMATCH-26NOV10QUECAB-QUE`) | 0.66 / 0.75 (57) | 70.5% | 60.0% | 56.9% | 55.3% [55.3%-55.3%] | -- | -- | -- | -- | PASS | -10.5 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 116.0, B 27.0; serve-point win A 55.5%, B 46.4%; Elo A 1308.9, B 1272.2; model uncertainty 0.0001
* Form inputs: days since last match A 434, B 609; matches on record A 2, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Polina Skopintseva (`KXITFWMATCH-26NOV10ZHISKO-SKO`) | 0.14 / 0.19 (32) | 16.5% | 41.1% | 19.9% | 50.0% [48.9%-50.0%] | -- | -- | -- | -- | PASS | +24.6 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Anastasia Zhilina (`KXITFWMATCH-26NOV10ZHISKO-ZHI`) | 0.80 / 0.85 (141) | 82.5% | 58.9% | 80.1% | 50.0% [50.0%-51.1%] | -- | -- | -- | -- | PASS | -23.6 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 312.0; serve-point win A 53.5%, B 48.2%; Elo A 1249.1, B 1247.7; model uncertainty 0.0054
* Form inputs: days since last match A 1428, B 196; matches on record A 42, B 10; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10ZHISKO-SKO  (YES = Polina Skopintseva)
Model: 41%
Kalshi: 16%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arthur Rinderknech vs Miomir Kecmanovic -- ATP Stockholm 1/16 F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-09 14:00Z
* Current expected start: 2026-11-10 15:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 22:48Z
* Recommended handicap-by time: 2026-11-10 14:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1500_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-09T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126239:200175:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miomir Kecmanovic (`KXATPMATCH-26NOV09RINKEC-KEC`) | 0.34 / 0.35 (470) | 34.5% | 45.5% | 40.1% | 40.6% [39.6%-41.5%] | -- | -- | -- | -- | SHADOW_BET | +11.0 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arthur Rinderknech (`KXATPMATCH-26NOV09RINKEC-RIN`) | 0.65 / 0.66 (2797) | 65.5% | 54.5% | 59.9% | 59.5% [58.5%-60.4%] | -- | -- | -- | -- | PASS | -11.0 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5579.0, B 5445.0; serve-point win A 68.2%, B 32.8%; Elo A 1830.2, B 1771.1; model uncertainty 0.0091
* Form inputs: days since last match A 4, B 8; matches on record A 572, B 619; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.005, surface_dev_loose +0.009, surface_dev_tight -0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26NOV09RINKEC-RIN3` Will Arthur Rinderknech win at least 2.5 more games than Miomir Kecmanovic?: 0.52/0.54 mid 53.0%, model 36.8% (projection_v2.0 (prediction ledger)) -- gap -16.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RINKEC-RIN20` Will Arthur Rinderknech win the Arthur Rinderknech vs Miomir Kecmanovic match by a set score of 2-0?: 0.15/0.67 mid 41.0%, model 28.1% (projection_v2.0 (prediction ledger)) -- gap -12.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RINKEC-2-KEC` Will Miomir Kecmanovic win set 2 in the Arthur Rinderknech vs Miomir Kecmanovic match: 0.17/0.52 mid 34.5%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV09RINKEC-RIN6` Will Arthur Rinderknech win at least 5.5 more games than Miomir Kecmanovic?: 0.16/0.20 mid 18.0%, model 6.2% (projection_v2.0 (prediction ledger)) -- gap -11.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09RINKEC-23` Over 22.5 games: 0.54/0.56 mid 55.0%, model 66.4% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RINKEC-1-KEC` Will Miomir Kecmanovic win set 1 in the Arthur Rinderknech vs Miomir Kecmanovic match: 0.36/0.39 mid 37.5%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap +9.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RINKEC-2-RIN` Will Arthur Rinderknech win set 2 in the Arthur Rinderknech vs Miomir Kecmanovic match: 0.42/0.83 mid 62.5%, model 53.0% (projection_v2.0 (prediction ledger)) -- gap -9.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV09RINKEC-28` Over 27.5 games: 0.32/0.40 mid 36.0%, model 44.8% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09RINKEC-18` Over 17.5 games: 0.85/0.92 mid 88.5%, model 96.7% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV09RINKEC-KEC2` Will Miomir Kecmanovic win at least 1.5 more games than Arthur Rinderknech?: 0.27/0.32 mid 29.5%, model 37.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RINKEC-1-RIN` Will Arthur Rinderknech win set 1 in the Arthur Rinderknech vs Miomir Kecmanovic match: 0.59/0.62 mid 60.5%, model 53.0% (projection_v2.0 (prediction ledger)) -- gap -7.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RINKEC-KEC20` Will Miomir Kecmanovic win the Arthur Rinderknech vs Miomir Kecmanovic match by a set score of 2-0?: 0.11/0.38 mid 24.5%, model 22.1% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RINKEC-KEC21` Will Miomir Kecmanovic win the Arthur Rinderknech vs Miomir Kecmanovic match by a set score of 2-1?: 0.13/0.38 mid 25.5%, model 23.4% (projection_v2.0 (prediction ledger)) -- gap -2.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RINKEC-RIN21` Will Arthur Rinderknech win the Arthur Rinderknech vs Miomir Kecmanovic match by a set score of 2-1?: 0.12/0.43 mid 27.5%, model 26.4% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Ole Bredschneijder (`KXITFMATCH-26NOV10BREULR-BRE`) | 0.58 / 0.64 (6) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nicolas Ulrich (`KXITFMATCH-26NOV10BREULR-ULR`) | 0.40 / 0.54 (59) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Yassine Dlimi (`KXITFMATCH-26NOV10DLIYAZ-DLI`) | 0.73 / 0.82 (5) | 77.5% | 84.3% | 91.2% | 86.2% [78.7%-89.5%] | -- | -- | -- | -- | PASS | +6.8 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ali Yazdani (`KXITFMATCH-26NOV10DLIYAZ-YAZ`) | 0.14 / 0.25 (5) | 19.5% | 15.7% | 8.8% | 13.8% [10.5%-21.3%] | -- | -- | -- | -- | PASS | -3.8 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1862.0, B 2400.0; serve-point win A 66.0%, B 41.9%; Elo A 1463.9, B 1240.0; model uncertainty 0.0543
* Form inputs: days since last match A 51, B 224; matches on record A 115, B 70; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.003, surface_dev_loose +0.011, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Arman Dubreuil (`KXITFMATCH-26NOV10DUGDUB-DUB`) | 0.07 / 0.12 (28) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Remy Dugardin (`KXITFMATCH-26NOV10DUGDUB-DUG`) | 0.83 / 0.90 (12) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Dzmitry Dziubailau (`KXITFMATCH-26NOV10DZIVTE-DZI`) | 0.32 / 0.47 (47) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dmytro Vterkovskiy (`KXITFMATCH-26NOV10DZIVTE-VTE`) | 0.53 / 0.67 (1) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Ammar Elamin (`KXITFMATCH-26NOV10ELAMAU-ELA`) | 0.74 / 0.80 (39) | 77.0% | 38.8% | 41.4% | 32.3% [31.4%-33.2%] | -- | -- | -- | -- | PASS | -38.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hugo Maurice (`KXITFMATCH-26NOV10ELAMAU-MAU`) | 0.16 / 0.22 (26) | 19.0% | 61.2% | 58.6% | 67.7% [66.8%-68.6%] | -- | -- | -- | -- | PASS | +42.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 528.0, B 48.0; serve-point win A 60.3%, B 37.4%; Elo A 1142.0, B 1272.1; model uncertainty 0.0092
* Form inputs: days since last match A 203, B 385; matches on record A 47, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10ELAMAU-MAU  (YES = Hugo Maurice)
Model: 61%
Kalshi: 19%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.009, surface_dev_loose -0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Matyas Cerny (`KXITFMATCH-26NOV10KRSCER-CER`) | 0.68 / 0.78 (8) | 73.0% | 90.2% | 90.7% | 78.7% [75.2%-82.1%] | -- | -- | -- | -- | PASS | +17.2 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Veljko Krstic (`KXITFMATCH-26NOV10KRSCER-KRS`) | 0.22 / 0.36 (4) | 29.0% | 9.8% | 9.3% | 21.3% [17.9%-24.8%] | -- | -- | -- | -- | PASS | -19.2 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 106.0, B 1849.0; serve-point win A 50.8%, B 39.4%; Elo A 1205.2, B 1417.0; model uncertainty 0.0344
* Form inputs: days since last match A 518, B 105; matches on record A 7, B 103; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10KRSCER-CER  (YES = Matyas Cerny)
Model: 90%
Kalshi: 73%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.024, surface_pool_high -0.011, surface_dev_loose +0.000, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Jonas Gundacker (`KXITFMATCH-26NOV10KUCGUN-GUN`) | 0.82 / 0.88 (3) | 85.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cem Christopher Kucukhuseyin (`KXITFMATCH-26NOV10KUCGUN-KUC`) | 0.09 / 0.20 (5) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Charlie Bazil (`KXITFMATCH-26NOV10KUMBAZ-BAZ`) | 0.16 / 0.20 (132) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Melvin Kumar (`KXITFMATCH-26NOV10KUMBAZ-KUM`) | 0.75 / 0.82 (33) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Noah Lopez (`KXITFMATCH-26NOV10LOPMAD-LOP`) | 0.21 / 0.31 (37) | 26.0% | 6.4% | 2.3% | 5.1% [3.3%-8.4%] | -- | -- | -- | -- | PASS | -19.6 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dragos Nicolae Madaras (`KXITFMATCH-26NOV10LOPMAD-MAD`) | 0.65 / 0.73 (1) | 69.0% | 93.6% | 97.7% | 94.9% [91.6%-96.7%] | -- | -- | -- | -- | PASS | +24.6 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 919.0, B 1412.0; serve-point win A 50.4%, B 38.0%; Elo A 1218.7, B 1644.1; model uncertainty 0.0252
* Form inputs: days since last match A 196, B 224; matches on record A 113, B 453; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10LOPMAD-MAD  (YES = Dragos Nicolae Madaras)
Model: 94%
Kalshi: 69%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.001, surface_pool_high +0.001, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Antoni Fabre (`KXITFMATCH-26NOV10OSMFAB-FAB`) | 0.77 / 0.94 (3) | 85.5% | 57.9% | 41.1% | 48.9% [47.9%-50.0%] | -- | -- | -- | -- | PASS | -27.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Vladimir Osminkin (`KXITFMATCH-26NOV10OSMFAB-OSM`) | 0.08 / 0.18 (15) | 13.0% | 42.1% | 58.9% | 51.0% [50.0%-52.1%] | -- | -- | -- | -- | PASS | +29.1 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 944.0; serve-point win A 56.2%, B 42.3%; Elo A 1271.0, B 1264.7; model uncertainty 0.0105
* Form inputs: days since last match A 2457, B 196; matches on record A 1, B 24; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10OSMFAB-OSM  (YES = Vladimir Osminkin)
Model: 42%
Kalshi: 13%
Gap: +29 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Barney Fitzpatrick (`KXITFMATCH-26NOV10PIAFIT-FIT`) | 0.43 / 0.56 (4) | 49.5% | 52.0% | 56.7% | 57.2% [56.2%-57.2%] | -- | -- | -- | -- | PASS | +2.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniil Piatrouski (`KXITFMATCH-26NOV10PIAFIT-PIA`) | 0.46 / 0.53 (53) | 49.5% | 47.9% | 43.3% | 42.8% [42.8%-43.8%] | -- | -- | -- | -- | PASS | -1.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 250.0, B 76.0; serve-point win A 60.0%, B 39.6%; Elo A 1165.6, B 1212.6; model uncertainty 0.0051
* Form inputs: days since last match A 252, B 441; matches on record A 7, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Karim Sherif Abdellatif Abdo (`KXITFMATCH-26NOV10SHESTA-SHE`) | 0.07 / 0.12 (28) | 9.5% | 49.4% | 50.0% | 62.2% [60.2%-64.1%] | -- | -- | -- | -- | PASS | +39.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cedric Stanke (`KXITFMATCH-26NOV10SHESTA-STA`) | 0.84 / 0.94 (100) | 89.0% | 50.6% | 50.0% | 37.8% [35.9%-39.8%] | -- | -- | -- | -- | PASS | -38.4 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 68.0, B 375.0; serve-point win A 59.9%, B 40.0%; Elo A 1244.1, B 1152.8; model uncertainty 0.0195
* Form inputs: days since last match A 308, B 203; matches on record A 2, B 30; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10SHESTA-SHE  (YES = Karim Sherif Abdellatif Abdo)
Model: 49%
Kalshi: 10%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Stefan Adrian Andreescu (`KXITFMATCH-26NOV10UJVAND-AND`) | 0.57 / 0.75 (105) | 66.0% | 77.5% | 83.2% | 82.5% [78.2%-84.2%] | -- | -- | -- | -- | PASS | +11.6 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matthias Ujvary (`KXITFMATCH-26NOV10UJVAND-UJV`) | 0.23 / 0.39 (2) | 31.0% | 22.4% | 16.8% | 17.5% [15.8%-21.8%] | -- | -- | -- | -- | PASS | -8.6 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2120.0, B 3228.0; serve-point win A 51.2%, B 43.1%; Elo A 1189.0, B 1441.5; model uncertainty 0.0298
* Form inputs: days since last match A 196, B 259; matches on record A 116, B 144; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high +0.000, surface_dev_loose -0.003, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Viacheslav Bielinskyi (`KXITFMATCH-26NOV10VANBIE-BIE`) | 0.60 / 0.65 (71) | 62.5% | 84.1% | 89.5% | 86.6% [80.5%-89.3%] | -- | -- | -- | -- | WATCH | +21.6 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Martin Van Der Meerschen (`KXITFMATCH-26NOV10VANBIE-VAN`) | 0.30 / 0.46 (10) | 38.0% | 15.9% | 10.5% | 13.4% [10.7%-19.5%] | -- | -- | -- | -- | PASS | -22.1 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2032.0, B 2937.0; serve-point win A 50.5%, B 42.0%; Elo A 1326.4, B 1588.9; model uncertainty 0.0436
* Form inputs: days since last match A 196, B 210; matches on record A 103, B 231; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10VANBIE-BIE  (YES = Viacheslav Bielinskyi)
Model: 84%
Kalshi: 62%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.006, surface_dev_loose -0.003, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Zeinab Ayadi (`KXITFWMATCH-26NOV10CASAYA-AYA`) | 0.16 / 0.41 (1) | 28.5% | 27.8% | 49.5% | 55.3% [54.2%-55.3%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sonia Cassani (`KXITFWMATCH-26NOV10CASAYA-CAS`) | 0.61 / 0.77 (1) | 69.0% | 72.2% | 50.5% | 44.7% [44.7%-45.8%] | -- | -- | -- | -- | PASS | +3.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 84.0, B 140.0; serve-point win A 56.8%, B 47.6%; Elo A 1176.3, B 1214.0; model uncertainty 0.0053
* Form inputs: days since last match A 364, B 315; matches on record A 85, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Daria Barsukov (`KXITFWMATCH-26NOV10DEEBAR-BAR`) | 0.20 / 0.24 (32) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leire De Ezcurra (`KXITFWMATCH-26NOV10DEEBAR-DEE`) | 0.73 / 0.76 (99) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Capucine Cedillo- Vayson de Pradenne (`KXITFWMATCH-26NOV10FONCED-CED`) | 0.07 / 0.10 (26) | 8.5% | 12.7% | 48.4% | 35.5% [33.5%-37.5%] | -- | -- | -- | -- | PASS | +4.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Chelsea Fontenel (`KXITFWMATCH-26NOV10FONCED-FON`) | 0.86 / 0.92 (9) | 89.0% | 87.3% | 51.6% | 64.5% [62.5%-66.5%] | -- | -- | -- | -- | PASS | -1.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 2027.0, B 0.0; serve-point win A 59.9%, B 48.7%; Elo A 1321.2, B 1216.2; model uncertainty 0.0199
* Form inputs: days since last match A 203, B 966; matches on record A 114, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Jade Groen (`KXITFWMATCH-26NOV10HONGRO-GRO`) | 0.19 / 0.20 (5) | 19.5% | 6.3% | 17.1% | 11.4% [10.0%-12.5%] | -- | -- | -- | -- | PASS | -13.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amelia Honer (`KXITFWMATCH-26NOV10HONGRO-HON`) | 0.81 / 0.82 (58) | 81.5% | 93.7% | 83.0% | 88.6% [87.5%-90.0%] | -- | -- | -- | -- | PASS | +12.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1349.0, B 470.0; serve-point win A 57.7%, B 53.8%; Elo A 1670.2, B 1292.1; model uncertainty 0.0123
* Form inputs: days since last match A 196, B 364; matches on record A 48, B 9; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.011, surface_dev_loose +0.007, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Victoria Kapcia (`KXITFWMATCH-26NOV10KAPRAS-KAP`) | 0.62 / 0.84 (3) | 73.0% | 38.2% | 20.8% | 42.6% [41.5%-43.6%] | -- | -- | -- | -- | PASS | -34.8 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ranim Rassil (`KXITFWMATCH-26NOV10KAPRAS-RAS`) | 0.24 / 0.75 (3) | 49.5% | 61.8% | 79.2% | 57.4% [56.4%-58.5%] | -- | -- | -- | -- | PASS | +12.3 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 358.0, B 70.0; serve-point win A 52.5%, B 45.2%; Elo A 1131.9, B 1175.0; model uncertainty 0.0105
* Form inputs: days since last match A 231, B 469; matches on record A 12, B 81; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Estella Jaeger (`KXITFWMATCH-26NOV10KUCJAE-JAE`) | 0.07 / 0.09 (5) | 8.0% | 10.0% | 15.1% | 16.0% [13.6%-18.8%] | -- | -- | -- | -- | PASS | +2.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daria Kuczer (`KXITFWMATCH-26NOV10KUCJAE-KUC`) | 0.91 / 0.93 (353) | 92.0% | 90.0% | 84.9% | 84.0% [81.2%-86.5%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 816.0, B 391.0; serve-point win A 54.9%, B 54.7%; Elo A 1451.2, B 1165.5; model uncertainty 0.0261
* Form inputs: days since last match A 462, B 196; matches on record A 172, B 75; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.028, surface_dev_loose +0.003, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Katarina Kujovic (`KXITFWMATCH-26NOV10KUJVOG-KUJ`) | 0.11 / 0.12 (28) | 11.5% | 10.4% | 5.8% | 13.4% [9.5%-20.4%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marie Vogt (`KXITFWMATCH-26NOV10KUJVOG-VOG`) | 0.84 / 0.87 (5) | 85.5% | 89.6% | 94.2% | 86.6% [79.6%-90.5%] | -- | -- | -- | -- | PASS | +4.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 711.0, B 2280.0; serve-point win A 48.6%, B 42.0%; Elo A 1283.7, B 1534.7; model uncertainty 0.0541
* Form inputs: days since last match A 308, B 29; matches on record A 15, B 164; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.003, surface_dev_loose -0.014, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Lya Fernandez (`KXITFWMATCH-26NOV10SEQFER-FER`) | 0.88 / 0.93 (454) | 90.5% | 88.8% | 92.8% | 87.0% [82.6%-91.0%] | -- | -- | -- | -- | PASS | -1.7 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Milla Sequeira (`KXITFWMATCH-26NOV10SEQFER-SEQ`) | 0.05 / 0.11 (403) | 8.0% | 11.2% | 7.2% | 13.0% [9.0%-17.4%] | -- | -- | -- | -- | PASS | +3.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 623.0, B 463.0; serve-point win A 46.4%, B 44.5%; Elo A 1053.6, B 1351.0; model uncertainty 0.0421
* Form inputs: days since last match A 231, B 196; matches on record A 119, B 66; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.012, surface_pool_high -0.011, surface_dev_loose -0.011, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Anamaria Federica Oana (`KXITFWMATCH-26NOV10YOROAN-OAN`) | 0.23 / 0.38 (3) | 30.5% | 76.4% | 94.4% | 83.0% [61.6%-90.1%] | -- | -- | -- | -- | PASS | +45.9 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ilay Yoruk (`KXITFWMATCH-26NOV10YOROAN-YOR`) | 0.63 / 0.77 (108) | 70.0% | 23.6% | 5.6% | 17.0% [9.9%-38.4%] | -- | -- | -- | -- | PASS | -46.4 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1694.0, B 1406.0; serve-point win A 48.7%, B 46.0%; Elo A 1423.6, B 1517.3; model uncertainty 0.1424
* Form inputs: days since last match A 36, B 259; matches on record A 466, B 86; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10YOROAN-OAN  (YES = Anamaria Federica Oana)
Model: 76%
Kalshi: 30%
Gap: +46 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.013, surface_dev_loose -0.023, surface_dev_tight +0.025
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Dan Brand (`KXITFMATCH-26NOV10BRAFIL-BRA`) | 0.30 / 0.35 (2) | 32.5% | 34.0% | 37.6% | 40.6% [38.6%-43.7%] | -- | -- | -- | -- | PASS | +1.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jakub Filip (`KXITFMATCH-26NOV10BRAFIL-FIL`) | 0.62 / 0.71 (88) | 66.5% | 66.0% | 62.4% | 59.4% [56.3%-61.4%] | -- | -- | -- | -- | PASS | -0.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 160.0, B 1554.0; serve-point win A 56.0%, B 40.9%; Elo A 1247.7, B 1309.2; model uncertainty 0.0256
* Form inputs: days since last match A 231, B 84; matches on record A 2, B 92; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.031, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Ioannis Kountourakis (`KXITFMATCH-26NOV10KOUPOR-KOU`) | 0.19 / 0.23 (125) | 21.0% | 13.5% | 16.5% | 13.2% [12.2%-15.6%] | -- | -- | -- | -- | PASS | -7.5 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julio Cesar Porras (`KXITFMATCH-26NOV10KOUPOR-POR`) | 0.78 / 0.79 (153) | 78.5% | 86.5% | 83.5% | 86.8% [84.4%-87.8%] | -- | -- | -- | -- | PASS | +8.0 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1589.0, B 1554.0; serve-point win A 55.0%, B 36.5%; Elo A 1119.6, B 1485.8; model uncertainty 0.0171
* Form inputs: days since last match A 210, B 350; matches on record A 63, B 115; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.001, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Matias Reyniak (`KXITFMATCH-26NOV10REYTHO-REY`) | 0.62 / 0.65 (21) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matthew Thomson (`KXITFMATCH-26NOV10REYTHO-THO`) | 0.31 / 0.37 (52) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Dimitris Azoidis (`KXITFMATCH-26NOV10THOAZO-AZO`) | 0.39 / 0.44 (10) | 41.5% | 69.0% | 75.7% | 75.7% [75.7%-75.7%] | -- | -- | -- | -- | PASS | +27.5 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Flynn Thomas (`KXITFMATCH-26NOV10THOAZO-THO`) | 0.53 / 0.57 (25) | 55.0% | 31.0% | 24.3% | 24.3% [24.3%-24.3%] | -- | -- | -- | -- | PASS | -24.0 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 723.0, B 0.0; serve-point win A 58.1%, B 38.1%; Elo A 1283.7, B 1487.0; model uncertainty 0.0
* Form inputs: days since last match A 217, B 786; matches on record A 16, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10THOAZO-AZO  (YES = Dimitris Azoidis)
Model: 69%
Kalshi: 42%
Gap: +27 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Justine Bretnacher (`KXITFWMATCH-26NOV10BREPEL-BRE`) | 0.51 / 0.60 (50) | 55.5% | 11.3% | 51.6% | 28.7% [26.0%-30.5%] | -- | -- | -- | -- | PASS | -44.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Helene Pellicano (`KXITFWMATCH-26NOV10BREPEL-PEL`) | 0.38 / 0.45 (50) | 41.5% | 88.7% | 48.4% | 71.3% [69.5%-74.0%] | -- | -- | -- | -- | PASS | +47.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 222.0, B 43.0; serve-point win A 47.8%, B 43.1%; Elo A 1206.2, B 1374.1; model uncertainty 0.0226
* Form inputs: days since last match A 350, B 595; matches on record A 22, B 117; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10BREPEL-PEL  (YES = Helene Pellicano)
Model: 89%
Kalshi: 42%
Gap: +47 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.027, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Mar Cabassers Morros (`KXITFWMATCH-26NOV10CABROS-CAB`) | 0.20 / 0.26 (27) | 23.0% | 28.9% | 42.0% | 41.5% [40.5%-41.5%] | -- | -- | -- | -- | PASS | +5.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lucia Ros Parres (`KXITFWMATCH-26NOV10CABROS-ROS`) | 0.68 / 0.78 (149) | 73.0% | 71.1% | 58.0% | 58.5% [58.5%-59.5%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 144.0, B 375.0; serve-point win A 50.8%, B 45.0%; Elo A 1221.4, B 1281.8; model uncertainty 0.0053
* Form inputs: days since last match A 427, B 343; matches on record A 3, B 43; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Delia Gaillard (`KXITFWMATCH-26NOV10GAITAT-GAI`) | 0.35 / 0.43 (5) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofia Tatu (`KXITFWMATCH-26NOV10GAITAT-TAT`) | 0.50 / 0.63 (73) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Dimitra Georgakopoulou (`KXITFWMATCH-26NOV10GEOOKT-GEO`) | 0.03 / 0.04 (22685) | 3.5% | 0.8% | 4.3% | 7.4% [5.4%-9.9%] | -- | -- | -- | -- | PASS | -2.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alisa Oktiabreva (`KXITFWMATCH-26NOV10GEOOKT-OKT`) | 0.96 / 0.97 (362) | 96.5% | 99.2% | 95.7% | 92.6% [90.1%-94.6%] | -- | -- | -- | -- | PASS | +2.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 78.0, B 1999.0; serve-point win A 40.5%, B 41.4%; Elo A 1218.0, B 1652.3; model uncertainty 0.0225
* Form inputs: days since last match A 371, B 112; matches on record A 3, B 67; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.025, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Cristina Diaz Adrover (`KXITFWMATCH-26NOV10PAODIA-DIA`) | 0.12 / 0.15 (43) | 13.5% | 25.1% | 61.6% | 40.5% [35.4%-44.7%] | -- | -- | -- | -- | WATCH | +11.6 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matilde Paoletti (`KXITFWMATCH-26NOV10PAODIA-PAO`) | 0.85 / 0.86 (1) | 85.5% | 75.0% | 38.4% | 59.6% [55.3%-64.6%] | -- | -- | -- | -- | PASS | -10.6 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 466.0, B 3491.0; serve-point win A 54.6%, B 50.5%; Elo A 1577.0, B 1462.3; model uncertainty 0.0465
* Form inputs: days since last match A 217, B 28; matches on record A 103, B 204; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Sapfo Sakellaridi (`KXITFWMATCH-26NOV10SAKSTA-SAK`) | 0.34 / 0.37 (77) | 35.5% | 47.1% | 70.1% | 58.2% [49.5%-63.1%] | -- | -- | -- | -- | PASS | +11.7 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anja Stankovic (`KXITFWMATCH-26NOV10SAKSTA-STA`) | 0.62 / 0.65 (39) | 63.5% | 52.8% | 29.9% | 41.8% [36.9%-50.5%] | -- | -- | -- | -- | PASS | -10.7 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4165.0, B 2297.0; serve-point win A 60.1%, B 39.4%; Elo A 1427.4, B 1499.8; model uncertainty 0.0682
* Form inputs: days since last match A 14, B 259; matches on record A 705, B 192; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.040, surface_pool_high -0.030, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Elena Korokozidi (`KXITFWMATCH-26NOV10SENKOR-KOR`) | 0.48 / 0.51 (55) | 49.5% | 25.7% | 21.8% | 25.1% [21.8%-30.0%] | -- | -- | -- | -- | PASS | -23.8 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Natalija Senic (`KXITFWMATCH-26NOV10SENKOR-SEN`) | 0.48 / 0.51 (30) | 49.5% | 74.3% | 78.2% | 74.9% [70.0%-78.2%] | -- | -- | -- | -- | WATCH | +24.8 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2163.0, B 2005.0; serve-point win A 53.2%, B 51.7%; Elo A 1564.9, B 1418.7; model uncertainty 0.0412
* Form inputs: days since last match A 196, B 196; matches on record A 257, B 149; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10SENKOR-SEN  (YES = Natalija Senic)
Model: 74%
Kalshi: 50%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Isabel Adrover Gallego (`KXITFWMATCH-26NOV10TRUADR-ADR`) | 0.78 / 0.84 (42) | 81.0% | 79.3% | 62.6% | 59.5% [57.4%-62.6%] | -- | -- | -- | -- | PASS | -1.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Trujillo Garnica (`KXITFWMATCH-26NOV10TRUADR-TRU`) | 0.13 / 0.21 (29) | 17.0% | 20.7% | 37.4% | 40.5% [37.4%-42.6%] | -- | -- | -- | -- | PASS | +3.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 185.0, B 516.0; serve-point win A 50.3%, B 43.6%; Elo A 1195.2, B 1260.2; model uncertainty 0.0258
* Form inputs: days since last match A 329, B 364; matches on record A 5, B 83; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.031, surface_pool_high +0.021, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
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
| Mario Arce Fernandez (`KXITFMATCH-26NOV10ARCBEL-ARC`) | 0.82 / 0.86 (56) | 84.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Manuel Belda (`KXITFMATCH-26NOV10ARCBEL-BEL`) | 0.11 / 0.19 (81) | 15.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tiago Cacao vs Goncalo Da Rosa Castro -- M25 Vale do Lobo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132310:213984:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tiago Cacao (`KXITFMATCH-26NOV10CACDAR-CAC`) | 0.84 / 0.94 (140) | 89.0% | 77.7% | 80.6% | 72.0% [70.6%-73.2%] | -- | -- | -- | -- | PASS | -11.3 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Goncalo Da Rosa Castro (`KXITFMATCH-26NOV10CACDAR-DAR`) | 0.06 / 0.13 (29) | 9.5% | 22.3% | 19.4% | 28.1% [26.8%-29.4%] | -- | -- | -- | -- | PASS | +12.8 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1430.0, B 149.0; serve-point win A 63.1%, B 42.8%; Elo A 1377.4, B 1220.4; model uncertainty 0.013
* Form inputs: days since last match A 70, B 114; matches on record A 327, B 4; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.004, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rafael Izquierdo Luque vs Pedro Rodenas -- M25 Vale do Lobo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202258:210203:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael Izquierdo Luque (`KXITFMATCH-26NOV10IZQROD-IZQ`) | 0.36 / 0.39 (16) | 37.5% | 38.3% | 39.0% | 38.0% [35.2%-40.0%] | 37.8% | -- | 37.8% | MODEL_LONE_OUTLIER | PASS | +0.8 pp | NORMAL | AGING | D / POOR | ALL_AGREE | VERIFIED |
| Pedro Rodenas (`KXITFMATCH-26NOV10IZQROD-ROD`) | 0.59 / 0.63 (50) | 61.0% | 61.7% | 61.0% | 62.0% [60.0%-64.8%] | 62.2% | -- | 62.2% | MODEL_LONE_OUTLIER | PASS | +0.7 pp | NORMAL | AGING | D / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1966.0, B 1623.0; serve-point win A 54.4%, B 43.3%; Elo A 1384.2, B 1475.3; model uncertainty 0.0242
* Form inputs: days since last match A 196, B 350; matches on record A 83, B 98; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.020, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
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
| Alberto Garcia Garcia (`KXITFMATCH-26NOV10KACGAR-GAR`) | 0.57 / 0.61 (33) | 59.0% | 40.5% | 22.1% | 38.7% [38.6%-39.8%] | -- | -- | -- | -- | PASS | -18.5 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Adam Kaczmarek (`KXITFMATCH-26NOV10KACGAR-KAC`) | 0.35 / 0.37 (39) | 36.0% | 59.5% | 77.9% | 61.3% [60.2%-61.4%] | -- | -- | -- | -- | PASS | +23.5 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 294.0; serve-point win A 59.5%, B 42.3%; Elo A 1262.0, B 1185.8; model uncertainty 0.0055
* Form inputs: days since last match A 1120, B 231; matches on record A 1, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10KACGAR-KAC  (YES = Adam Kaczmarek)
Model: 59%
Kalshi: 36%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Alejandro Manzanera Pertusa (`KXITFMATCH-26NOV10MANPED-MAN`) | 0.93 / 0.95 (10) | 94.0% | 81.5% | 64.1% | 72.8% [71.5%-74.5%] | -- | -- | -- | -- | PASS | -12.5 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ian Pedersen Lozano (`KXITFMATCH-26NOV10MANPED-PED`) | 0.05 / 0.08 (1519) | 6.5% | 18.5% | 35.9% | 27.2% [25.5%-28.5%] | -- | -- | -- | -- | PASS | +12.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1670.0, B 60.0; serve-point win A 63.3%, B 43.6%; Elo A 1453.7, B 1280.2; model uncertainty 0.015
* Form inputs: days since last match A 203, B 203; matches on record A 190, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.017, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Jacopo Berrettini (`KXITFMATCH-26NOV10MASBER-BER`) | 0.76 / 0.81 (1) | 78.5% | 91.9% | 75.3% | 86.2% [85.9%-86.8%] | -- | -- | -- | -- | PASS | +13.4 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Simone Massucco (`KXITFMATCH-26NOV10MASBER-MAS`) | 0.18 / 0.25 (56) | 21.5% | 8.1% | 24.7% | 13.8% [13.2%-14.1%] | -- | -- | -- | -- | PASS | -13.4 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 69.0, B 3742.0; serve-point win A 52.3%, B 37.0%; Elo A 1245.3, B 1571.4; model uncertainty 0.0043
* Form inputs: days since last match A 364, B 224; matches on record A 2, B 386; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.006, surface_dev_loose -0.003, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Mustapha El Natour (`KXITFMATCH-26NOV10MOLELN-ELN`) | 0.16 / 0.21 (22) | 18.5% | 55.5% | 45.8% | 63.7% [60.3%-66.1%] | -- | -- | -- | -- | PASS | +37.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Javier Molino (`KXITFMATCH-26NOV10MOLELN-MOL`) | 0.78 / 0.82 (66) | 80.0% | 44.5% | 54.2% | 36.2% [33.9%-39.7%] | -- | -- | -- | -- | PASS | -35.5 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 329.0, B 227.0; serve-point win A 58.2%, B 40.7%; Elo A 1198.7, B 1317.9; model uncertainty 0.029
* Form inputs: days since last match A 266, B 231; matches on record A 39, B 7; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10MOLELN-ELN  (YES = Mustapha El Natour)
Model: 56%
Kalshi: 18%
Gap: +37 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose +0.004, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
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
| Adrian Oetzbach (`KXITFMATCH-26NOV10OETTUR-OET`) | 0.37 / 0.41 (3) | 39.0% | 36.9% | 44.8% | 42.2% [41.2%-43.2%] | -- | -- | -- | -- | PASS | -2.1 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Radu David Turcanu (`KXITFMATCH-26NOV10OETTUR-TUR`) | 0.55 / 0.62 (53) | 58.5% | 63.1% | 55.2% | 57.8% [56.8%-58.8%] | -- | -- | -- | -- | PASS | +4.6 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3595.0, B 2023.0; serve-point win A 56.7%, B 40.7%; Elo A 1388.5, B 1468.2; model uncertainty 0.0103
* Form inputs: days since last match A 196, B 217; matches on record A 303, B 62; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Sofia Alekseeva (`KXITFWMATCH-26NOV10ALEMYL-ALE`) | 0.39 / 0.56 (7) | 47.5% | 57.6% | 31.6% | 46.8% [45.2%-47.9%] | -- | -- | -- | -- | PASS | +10.1 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marfa Mylnikova (`KXITFWMATCH-26NOV10ALEMYL-MYL`) | 0.50 / 0.56 (5) | 53.0% | 42.4% | 68.4% | 53.2% [52.1%-54.8%] | -- | -- | -- | -- | PASS | -10.6 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 339.0, B 129.0; serve-point win A 56.1%, B 45.3%; Elo A 1252.5, B 1265.2; model uncertainty 0.0131
* Form inputs: days since last match A 238, B 245; matches on record A 8, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
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
| Hanna Bougouffa (`KXITFWMATCH-26NOV10BRUBOU-BOU`) | 0.64 / 0.67 (4) | 65.5% | 56.5% | 40.5% | 48.9% [47.3%-51.1%] | -- | -- | -- | -- | PASS | -9.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Brunet-Brady (`KXITFWMATCH-26NOV10BRUBOU-BRU`) | 0.32 / 0.34 (13) | 33.0% | 43.5% | 59.6% | 51.1% [48.9%-52.7%] | -- | -- | -- | -- | PASS | +10.5 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 135.0, B 245.0; serve-point win A 51.4%, B 47.4%; Elo A 1259.2, B 1259.9; model uncertainty 0.0187
* Form inputs: days since last match A 238, B 469; matches on record A 2, B 134; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Tilwith Di Girolami (`KXITFWMATCH-26NOV10DIGLAT-DIG`) | 0.86 / 0.91 (65) | 88.5% | 93.4% | 92.7% | 80.4% [79.6%-82.6%] | -- | -- | -- | -- | PASS | +4.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Meline Lataste (`KXITFWMATCH-26NOV10DIGLAT-LAT`) | 0.09 / 0.12 (6) | 10.5% | 6.6% | 7.3% | 19.6% [17.4%-20.4%] | -- | -- | -- | -- | PASS | -3.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1533.0, B 62.0; serve-point win A 58.5%, B 52.8%; Elo A 1473.7, B 1236.1; model uncertainty 0.0147
* Form inputs: days since last match A 196, B 518; matches on record A 202, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Belkova / Kuharenko (`KXITFWDOUBLES-26NOV10EFRMESBELKUH-BELKUH`) | 0.55 / 0.67 (75) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Efremova / Meshcheryakova (`KXITFWDOUBLES-26NOV10EFRMESBELKUH-EFRMES`) | 0.30 / 0.51 (2) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Elkady / Nosei (`KXITFWDOUBLES-26NOV10ELKNOSEZZSAL-ELKNOS`) | 0.12 / 0.29 (5) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ezzat / Salem (`KXITFWDOUBLES-26NOV10ELKNOSEZZSAL-EZZSAL`) | 0.63 / 0.84 (6) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Amelie Brooks (`KXITFWMATCH-26NOV10ULRBRO-BRO`) | 0.39 / 0.41 (14) | 40.0% | 40.1% | 51.1% | 44.7% [43.6%-45.2%] | -- | -- | -- | -- | PASS | +0.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zoe Ulrich (`KXITFWMATCH-26NOV10ULRBRO-ULR`) | 0.58 / 0.60 (37) | 59.0% | 59.9% | 48.9% | 55.3% [54.8%-56.4%] | -- | -- | -- | -- | PASS | +0.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 169.0, B 164.0; serve-point win A 53.8%, B 48.1%; Elo A 1257.9, B 1211.6; model uncertainty 0.0079
* Form inputs: days since last match A 273, B 196; matches on record A 2, B 19; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Robert Galloway / Andre Goransson vs Marc Polmans / Jan Zielinski -- ATP Stockholm 1/8 F

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-10 13:00Z
* Current expected start: 2026-11-10 16:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-09 22:48Z
* Recommended handicap-by time: 2026-11-10 15:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10GALGORPOLZIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robert Galloway / Andre Goransson (`KXATPDOUBLES-26NOV10GALGORPOLZIE-GALGOR`) | 0.42 / 0.45 (183) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marc Polmans / Jan Zielinski (`KXATPDOUBLES-26NOV10GALGORPOLZIE-POLZIE`) | 0.53 / 0.58 (2977) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Alharrasi / Shanan Zayed vs Belozertsev / Schell -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ALHSHABELSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alharrasi / Shanan Zayed (`KXITFDOUBLES-26NOV10ALHSHABELSCH-ALHSHA`) | 0.04 / 0.89 (56) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Belozertsev / Schell (`KXITFDOUBLES-26NOV10ALHSHABELSCH-BELSCH`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Bakshi / Purtseladze vs Ianin / Trongcharoenchaikul -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BAKPURIANTRO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bakshi / Purtseladze (`KXITFDOUBLES-26NOV10BAKPURIANTRO-BAKPUR`) | 0.47 / 0.63 (67) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ianin / Trongcharoenchaikul (`KXITFDOUBLES-26NOV10BAKPURIANTRO-IANTRO`) | 0.39 / 0.58 (59) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Blazka / Gengel vs Ariel Hidalgo Aguirre / Andres Macias Elizalde -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BLAGENARIAND:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ariel Hidalgo Aguirre / Andres Macias Elizalde (`KXITFDOUBLES-26NOV10BLAGENARIAND-ARIAND`) | 0.07 / 0.37 (56) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Blazka / Gengel (`KXITFDOUBLES-26NOV10BLAGENARIAND-BLAGEN`) | 0.87 / 0.90 (35) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Bocchi / Mugelli vs Mabrouk / Reilly -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BOCMUGMABREI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bocchi / Mugelli (`KXITFDOUBLES-26NOV10BOCMUGMABREI-BOCMUG`) | 0.61 / 0.77 (56) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mabrouk / Reilly (`KXITFDOUBLES-26NOV10BOCMUGMABREI-MABREI`) | 0.26 / 0.40 (25) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Andrea Colombo vs Ntungamili Raguin -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10COLRAG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Colombo (`KXITFMATCH-26NOV10COLRAG-COL`) | 0.74 / 0.78 (113) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ntungamili Raguin (`KXITFMATCH-26NOV10COLRAG-RAG`) | 0.19 / 0.22 (25) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabelic / Huggins vs Abderrahman / van Wyk -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10GABHUGABDVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abderrahman / van Wyk (`KXITFDOUBLES-26NOV10GABHUGABDVAN-ABDVAN`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabelic / Huggins (`KXITFDOUBLES-26NOV10GABHUGABDVAN-GABHUG`) | 0.07 / 0.89 (31) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dominique Graf vs Alessandro Mondazzi -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208687:213782:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dominique Graf (`KXITFMATCH-26NOV10GRAMON-GRA`) | 0.22 / 0.29 (28) | 25.5% | 41.9% | 71.4% | 47.9% [45.9%-51.0%] | -- | -- | -- | -- | PASS | +16.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alessandro Mondazzi (`KXITFMATCH-26NOV10GRAMON-MON`) | 0.70 / 0.75 (120) | 72.5% | 58.1% | 28.6% | 52.0% [49.0%-54.1%] | -- | -- | -- | -- | PASS | -14.4 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 103.0, B 182.0; serve-point win A 60.0%, B 38.4%; Elo A 1168.7, B 1199.0; model uncertainty 0.0256
* Form inputs: days since last match A 539, B 238; matches on record A 8, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10GRAMON-GRA  (YES = Dominique Graf)
Model: 42%
Kalshi: 26%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ibrahim / Yuan vs Senn / Wygona -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10IBRYUASENWYG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ibrahim / Yuan (`KXITFDOUBLES-26NOV10IBRYUASENWYG-IBRYUA`) | 0.07 / 0.50 (34) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Senn / Wygona (`KXITFDOUBLES-26NOV10IBRYUASENWYG-SENWYG`) | 0.84 / 0.90 (1) | 87.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Popko / Tiurnev vs Andrei Golescu / Horia Haita -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10POPTIUANDHOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrei Golescu / Horia Haita (`KXITFDOUBLES-26NOV10POPTIUANDHOR-ANDHOR`) | 0.21 / 0.51 (3) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Popko / Tiurnev (`KXITFDOUBLES-26NOV10POPTIUANDHOR-POPTIU`) | 0.65 / 0.86 (2) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Andrei Radu vs Jacopo Denitto -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10RADDEN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacopo Denitto (`KXITFMATCH-26NOV10RADDEN-DEN`) | 0.46 / 0.50 (38) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Andrei Radu (`KXITFMATCH-26NOV10RADDEN-RAD`) | 0.44 / 0.52 (28) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mathieu Scaglia vs Milledge Galphin Cossu -- M15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10SCACOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Milledge Galphin Cossu (`KXITFMATCH-26NOV10SCACOS-COS`) | 0.07 / 0.09 (1) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mathieu Scaglia (`KXITFMATCH-26NOV10SCACOS-SCA`) | 0.90 / 0.94 (1049) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arystanbekova / Yesypchuk vs Negishi / Jagatdeo Verma -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10ARYYESNEGJAG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arystanbekova / Yesypchuk (`KXITFWDOUBLES-26NOV10ARYYESNEGJAG-ARYYES`) | 0.90 / 0.93 (2) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Negishi / Jagatdeo Verma (`KXITFWDOUBLES-26NOV10ARYYESNEGJAG-NEGJAG`) | 0.05 / 0.38 (1) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Keisija Berzina vs Viola Bedini -- W15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:270207:270393:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viola Bedini (`KXITFWMATCH-26NOV10BERBED-BED`) | 0.34 / 0.37 (8) | 35.5% | 52.8% | 45.2% | 51.6% [50.5%-52.7%] | -- | -- | -- | -- | PASS | +17.3 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Keisija Berzina (`KXITFWMATCH-26NOV10BERBED-BER`) | 0.60 / 0.64 (24) | 62.0% | 47.2% | 54.8% | 48.4% [47.3%-49.5%] | -- | -- | -- | -- | PASS | -14.8 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 148.0, B 465.0; serve-point win A 51.5%, B 48.0%; Elo A 1275.2, B 1288.1; model uncertainty 0.0107
* Form inputs: days since last match A 336, B 203; matches on record A 2, B 12; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10BERBED-BED  (YES = Viola Bedini)
Model: 53%
Kalshi: 36%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emilia Carlotta Brune vs Yoana Moneva -- W15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:246492:267633:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emilia Carlotta Brune (`KXITFWMATCH-26NOV10BRUMON-BRU`) | 0.95 / 0.97 (2730) | 96.0% | 93.6% | 80.3% | 83.5% [82.5%-85.1%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yoana Moneva (`KXITFWMATCH-26NOV10BRUMON-MON`) | 0.04 / 0.05 (562) | 4.5% | 6.4% | 19.7% | 16.5% [14.9%-17.5%] | -- | -- | -- | -- | PASS | +1.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 93.0, B 180.0; serve-point win A 60.0%, B 51.4%; Elo A 1222.6, B 939.6; model uncertainty 0.0132
* Form inputs: days since last match A 434, B 196; matches on record A 3, B 66; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.010, surface_dev_loose +0.003, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kaegi / Wahler vs Gomez O'Hayon / Solar Donoso -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10KAEWAHGOMSOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gomez O'Hayon / Solar Donoso (`KXITFWDOUBLES-26NOV10KAEWAHGOMSOL-GOMSOL`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kaegi / Wahler (`KXITFWDOUBLES-26NOV10KAEWAHGOMSOL-KAEWAH`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kakenova / Toregen vs Bojica / Safta -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10KAKTORBOJSAF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bojica / Safta (`KXITFWDOUBLES-26NOV10KAKTORBOJSAF-BOJSAF`) | 0.79 / 0.90 (1) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kakenova / Toregen (`KXITFWDOUBLES-26NOV10KAKTORBOJSAF-KAKTOR`) | 0.09 / 0.54 (3) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Marija Lauva vs Alja Senica -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263808:264264:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marija Lauva (`KXITFWMATCH-26NOV10LAUSEN-LAU`) | 0.27 / 0.32 (16) | 29.5% | 24.8% | 44.7% | 47.3% [46.2%-47.9%] | -- | -- | -- | -- | PASS | -4.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alja Senica (`KXITFWMATCH-26NOV10LAUSEN-SEN`) | 0.64 / 0.71 (91) | 67.5% | 75.2% | 55.3% | 52.7% [52.1%-53.8%] | -- | -- | -- | -- | PASS | +7.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 232.0, B 989.0; serve-point win A 49.1%, B 45.8%; Elo A 1311.7, B 1329.2; model uncertainty 0.008
* Form inputs: days since last match A 371, B 14; matches on record A 4, B 52; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ustiniya Lekomtseva vs Sara Victoria Balan -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:261098:267431:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Victoria Balan (`KXITFWMATCH-26NOV10LEKBAL-BAL`) | 0.74 / 0.81 (7) | 77.5% | 58.2% | 48.4% | 54.3% [51.6%-58.0%] | -- | -- | -- | -- | PASS | -19.3 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ustiniya Lekomtseva (`KXITFWMATCH-26NOV10LEKBAL-LEK`) | 0.19 / 0.27 (7) | 23.0% | 41.8% | 51.6% | 45.7% [42.0%-48.4%] | -- | -- | -- | -- | PASS | +18.8 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1512.0, B 1045.0; serve-point win A 48.9%, B 49.5%; Elo A 1303.4, B 1362.1; model uncertainty 0.0319
* Form inputs: days since last match A 196, B 322; matches on record A 98, B 37; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10LEKBAL-LEK  (YES = Ustiniya Lekomtseva)
Model: 42%
Kalshi: 23%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.027, surface_pool_high -0.027, surface_dev_loose +0.011, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasiia Nikolaieva vs Andreea Prisacariu -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10NIKPRI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasiia Nikolaieva (`KXITFWMATCH-26NOV10NIKPRI-NIK`) | 0.23 / 0.51 (151) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Andreea Prisacariu (`KXITFWMATCH-26NOV10NIKPRI-PRI`) | 0.50 / 0.73 (6) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Federica Trevisan vs Ksenia Laskutova -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215372:220081:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ksenia Laskutova (`KXITFWMATCH-26NOV10TRELAS-LAS`) | 0.20 / 0.32 (5) | 26.0% | 76.8% | 62.1% | 74.8% [74.8%-75.6%] | -- | -- | -- | -- | PASS | +50.8 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Federica Trevisan (`KXITFWMATCH-26NOV10TRELAS-TRE`) | 0.67 / 0.82 (5) | 74.5% | 23.2% | 37.9% | 25.2% [24.4%-25.2%] | -- | -- | -- | -- | PASS | -51.3 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 1449.0; serve-point win A 51.6%, B 42.9%; Elo A 1248.4, B 1439.0; model uncertainty 0.0044
* Form inputs: days since last match A 1554, B 196; matches on record A 21, B 372; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10TRELAS-LAS  (YES = Ksenia Laskutova)
Model: 77%
Kalshi: 26%
Gap: +51 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Holger Rune vs Zizou Bergs -- ATP Stockholm 1/16 F

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-09 14:00Z
* Current expected start: 2026-11-10 17:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 22:48Z
* Recommended handicap-by time: 2026-11-10 16:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1620_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-09T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200267:208029:2026-11-09`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zizou Bergs (`KXATPMATCH-26NOV09RUNBER-BER`) | 0.39 / 0.40 (2082) | 39.5% | 43.9% | 52.0% | 45.6% [42.2%-48.0%] | -- | -- | -- | -- | SHADOW_BET | +4.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Holger Rune (`KXATPMATCH-26NOV09RUNBER-RUN`) | 0.60 / 0.61 (14402) | 60.5% | 56.1% | 48.0% | 54.4% [52.0%-57.8%] | -- | -- | -- | -- | PASS | -4.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3242.0, B 5856.0; serve-point win A 66.2%, B 35.1%; Elo A 1959.8, B 1830.4; model uncertainty 0.0292
* Form inputs: days since last match A 6, B 7; matches on record A 449, B 573; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26NOV09RUNBER-2-BER` Will Zizou Bergs win set 2 in the Holger Rune vs Zizou Bergs match: 0.36/0.77 mid 56.5%, model 45.9% (projection_v2.0 (prediction ledger)) -- gap -10.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV09RUNBER-RUN5` Will Holger Rune win at least 4.5 more games than Zizou Bergs?: 0.25/0.28 mid 26.5%, model 17.5% (projection_v2.0 (prediction ledger)) -- gap -9.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09RUNBER-29` Over 28.5 games: 0.28/0.32 mid 30.0%, model 38.3% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09RUNBER-24` Over 23.5 games: 0.48/0.49 mid 48.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV09RUNBER-19` Over 18.5 games: 0.80/0.87 mid 83.5%, model 90.5% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RUNBER-BER20` Will Zizou Bergs win the Holger Rune vs Zizou Bergs match by a set score of 2-0?: 0.12/0.41 mid 26.5%, model 21.1% (projection_v2.0 (prediction ledger)) -- gap -5.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV09RUNBER-RUN2` Will Holger Rune win at least 1.5 more games than Zizou Bergs?: 0.53/0.54 mid 53.5%, model 48.2% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RUNBER-BER21` Will Zizou Bergs win the Holger Rune vs Zizou Bergs match by a set score of 2-1?: 0.17/0.39 mid 28.0%, model 22.8% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RUNBER-RUN21` Will Holger Rune win the Holger Rune vs Zizou Bergs match by a set score of 2-1?: 0.22/0.42 mid 32.0%, model 26.9% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RUNBER-2-RUN` Will Holger Rune win set 2 in the Holger Rune vs Zizou Bergs match: 0.21/0.78 mid 49.5%, model 54.1% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RUNBER-1-BER` Will Zizou Bergs win set 1 in the Holger Rune vs Zizou Bergs match: 0.41/0.43 mid 42.0%, model 45.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV09RUNBER-RUN20` Will Holger Rune win the Holger Rune vs Zizou Bergs match by a set score of 2-0?: 0.12/0.43 mid 27.5%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV09RUNBER-1-RUN` Will Holger Rune win set 1 in the Holger Rune vs Zizou Bergs match: 0.55/0.56 mid 55.5%, model 54.1% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV09RUNBER-BER2` Will Zizou Bergs win at least 1.5 more games than Holger Rune?: 0.34/0.38 mid 36.0%, model 36.2% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Pablo Aunion Duran vs Karim Al-Amin -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213100:213758:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karim Al-Amin (`KXITFMATCH-26NOV10AUNALA-ALA`) | 0.54 / 0.64 (13) | 59.0% | 55.6% | 55.1% | 61.1% [60.6%-61.2%] | -- | -- | -- | -- | PASS | -3.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Pablo Aunion Duran (`KXITFMATCH-26NOV10AUNALA-AUN`) | 0.41 / 0.64 (3) | 52.5% | 44.4% | 44.9% | 38.9% [38.8%-39.4%] | -- | -- | -- | -- | PASS | -8.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 396.0, B 74.0; serve-point win A 60.3%, B 38.6%; Elo A 1191.7, B 1268.1; model uncertainty 0.0031
* Form inputs: days since last match A 259, B 483; matches on record A 8, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aleksandr Braynin vs Francisco Rocha -- M25 Vale do Lobo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202089:209095:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksandr Braynin (`KXITFMATCH-26NOV10BRAROC-BRA`) | 0.39 / 0.41 (57) | 40.0% | 51.0% | 62.8% | 56.8% [50.5%-59.8%] | -- | -- | -- | -- | WATCH | +11.1 pp | REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Francisco Rocha (`KXITFMATCH-26NOV10BRAROC-ROC`) | 0.55 / 0.60 (14) | 57.5% | 48.9% | 37.2% | 43.2% [40.2%-49.5%] | -- | -- | -- | -- | PASS | -8.6 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3428.0, B 1919.0; serve-point win A 58.6%, B 41.6%; Elo A 1350.3, B 1353.9; model uncertainty 0.0465
* Form inputs: days since last match A 210, B 28; matches on record A 231, B 147; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Caruso / Cocola vs Aleksandar Amarandei / Fiorentini -- M25 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10CARCOCALEFIO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksandar Amarandei / Fiorentini (`KXITFDOUBLES-26NOV10CARCOCALEFIO-ALEFIO`) | 0.23 / 0.43 (75) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Caruso / Cocola (`KXITFDOUBLES-26NOV10CARCOCALEFIO-CARCOC`) | 0.62 / 0.78 (10) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Cooper / Vanshelboim vs Angeloni / Robinson -- M25 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10COOVANANGROB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Angeloni / Robinson (`KXITFDOUBLES-26NOV10COOVANANGROB-ANGROB`) | 0.49 / 0.87 (8) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cooper / Vanshelboim (`KXITFDOUBLES-26NOV10COOVANANGROB-COOVAN`) | 0.35 / 0.68 (3) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mario Gonzalez Fernandez vs Joao Dinis Silva -- M25 Vale do Lobo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208605:212947:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mario Gonzalez Fernandez (`KXITFMATCH-26NOV10GONSIL-GON`) | 0.58 / 0.61 (1) | 59.5% | 80.0% | 80.3% | 74.5% [73.5%-77.7%] | -- | -- | -- | -- | PASS | +20.5 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joao Dinis Silva (`KXITFMATCH-26NOV10GONSIL-SIL`) | 0.36 / 0.42 (55) | 39.0% | 20.0% | 19.7% | 25.6% [22.3%-26.5%] | -- | -- | -- | -- | PASS | -19.0 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2442.0, B 226.0; serve-point win A 60.8%, B 45.6%; Elo A 1419.2, B 1238.1; model uncertainty 0.0208
* Form inputs: days since last match A 77, B 196; matches on record A 236, B 12; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10GONSIL-GON  (YES = Mario Gonzalez Fernandez)
Model: 80%
Kalshi: 60%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.008, surface_dev_loose +0.008, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marc Martin Roca vs Marcos Diaz Revuelta -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10MARDIA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcos Diaz Revuelta (`KXITFMATCH-26NOV10MARDIA-DIA`) | 0.09 / 0.83 (4) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marc Martin Roca (`KXITFMATCH-26NOV10MARDIA-MAR`) | 0.11 / 0.94 (104) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## David Naharro vs Maties Torres Ramis -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211762:212922:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Naharro (`KXITFMATCH-26NOV10NAHTOR-NAH`) | 0.70 / 0.76 (47) | 73.0% | 52.0% | 35.8% | 46.9% [45.3%-49.0%] | -- | -- | -- | -- | PASS | -21.0 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maties Torres Ramis (`KXITFMATCH-26NOV10NAHTOR-TOR`) | 0.20 / 0.27 (34) | 23.5% | 48.0% | 64.2% | 53.1% [51.0%-54.7%] | -- | -- | -- | -- | PASS | +24.5 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 589.0, B 248.0; serve-point win A 59.2%, B 41.2%; Elo A 1170.4, B 1178.9; model uncertainty 0.0182
* Form inputs: days since last match A 196, B 280; matches on record A 21, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10NAHTOR-TOR  (YES = Maties Torres Ramis)
Model: 48%
Kalshi: 24%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carles Rojas vs Alessandro Del Francia -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ROJDEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessandro Del Francia (`KXITFMATCH-26NOV10ROJDEL-DEL`) | 0.06 / 0.75 (15) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Carles Rojas (`KXITFMATCH-26NOV10ROJDEL-ROJ`) | 0.26 / 0.94 (5) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lourenco Silva E Costa vs Sebastian Sorger -- M25 Vale do Lobo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10SILSOR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lourenco Silva E Costa (`KXITFMATCH-26NOV10SILSOR-SIL`) | 0.04 / 0.05 (120) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sebastian Sorger (`KXITFMATCH-26NOV10SILSOR-SOR`) | 0.92 / 0.96 (461) | 94.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eero Vasa vs Goncalo Marques -- M25 Vale do Lobo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144814:149128:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Goncalo Marques (`KXITFMATCH-26NOV10VASMAR-MAR`) | 0.50 / 0.54 (23) | 52.0% | 19.9% | 41.0% | 28.0% [22.0%-33.8%] | -- | -- | -- | -- | PASS | -32.1 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eero Vasa (`KXITFMATCH-26NOV10VASMAR-VAS`) | 0.45 / 0.47 (11) | 46.0% | 80.1% | 59.0% | 72.0% [66.2%-78.0%] | -- | -- | -- | -- | WATCH | +34.1 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2846.0, B 652.0; serve-point win A 65.9%, B 40.8%; Elo A 1421.5, B 1216.6; model uncertainty 0.059
* Form inputs: days since last match A 7, B 35; matches on record A 267, B 31; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10VASMAR-VAS  (YES = Eero Vasa)
Model: 80%
Kalshi: 46%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.033, surface_pool_high -0.044, surface_dev_loose -0.009, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Defne Cirpanli vs Carlotta Moccia -- W15 Nules R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222856:223411:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Defne Cirpanli (`KXITFWMATCH-26NOV10CIRMOC-CIR`) | 0.21 / 0.25 (32) | 23.0% | 33.4% | 35.9% | 38.4% [37.4%-39.5%] | -- | -- | -- | -- | WATCH | +10.4 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carlotta Moccia (`KXITFWMATCH-26NOV10CIRMOC-MOC`) | 0.72 / 0.78 (68) | 75.0% | 66.6% | 64.1% | 61.6% [60.5%-62.6%] | -- | -- | -- | -- | PASS | -8.4 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1730.0, B 644.0; serve-point win A 52.4%, B 44.4%; Elo A 1207.0, B 1283.6; model uncertainty 0.0102
* Form inputs: days since last match A 191, B 252; matches on record A 224, B 120; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mireia Sagrista Bermejo vs Franziska Sziedat -- W15 Nules R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220645:267392:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mireia Sagrista Bermejo (`KXITFWMATCH-26NOV10SAGSZI-SAG`) | 0.12 / 0.17 (28) | 14.5% | 14.3% | 25.5% | 30.5% [30.5%-31.5%] | 17.0% | -- | 17.0% | KALSHI_LONE_OUTLIER | PASS | -0.2 pp | NORMAL | AGING | D / POOR | ALL_AGREE | VERIFIED |
| Franziska Sziedat (`KXITFWMATCH-26NOV10SAGSZI-SZI`) | 0.81 / 0.85 (20) | 83.0% | 85.7% | 74.5% | 69.5% [68.5%-69.5%] | 83.0% | -- | 83.0% | MODEL_LONE_OUTLIER | PASS | +2.7 pp | NORMAL | AGING | D / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 175.0, B 2098.0; serve-point win A 48.0%, B 44.0%; Elo A 1256.6, B 1389.2; model uncertainty 0.005
* Form inputs: days since last match A 29, B 5; matches on record A 5, B 212; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.009, surface_dev_loose -0.000, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Meritxell Teixido Garcia vs Astrid Wanja Brune Olsen -- W15 Nules R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214934:269254:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Astrid Wanja Brune Olsen (`KXITFWMATCH-26NOV10TEIBRU-BRU`) | 0.64 / 0.70 (31) | 67.0% | 61.1% | 71.8% | 66.6% [62.6%-69.5%] | -- | -- | -- | -- | PASS | -5.9 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Meritxell Teixido Garcia (`KXITFWMATCH-26NOV10TEIBRU-TEI`) | 0.29 / 0.32 (79) | 30.5% | 38.9% | 28.2% | 33.4% [30.5%-37.4%] | -- | -- | -- | -- | PASS | +8.4 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1300.0, B 1262.0; serve-point win A 48.8%, B 49.1%; Elo A 1307.3, B 1387.2; model uncertainty 0.0345
* Form inputs: days since last match A 196, B 196; matches on record A 45, B 171; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Toma vs Esther Lopez Alcaraz -- W15 Nules R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215701:215966:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Esther Lopez Alcaraz (`KXITFWMATCH-26NOV10TOMLOP-LOP`) | 0.48 / 0.52 (46) | 50.0% | 50.5% | 48.9% | 48.9% [47.9%-51.1%] | -- | -- | -- | -- | PASS | +0.5 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Toma (`KXITFWMATCH-26NOV10TOMLOP-TOM`) | 0.49 / 0.50 (19) | 49.5% | 49.5% | 51.1% | 51.1% [48.9%-52.1%] | -- | -- | -- | -- | PASS | -0.0 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1852.0, B 243.0; serve-point win A 53.0%, B 46.9%; Elo A 1355.3, B 1351.0; model uncertainty 0.016
* Form inputs: days since last match A 50, B 385; matches on record A 252, B 101; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.021, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maria Andrienko vs Ando Tiantsoa Ratre -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10ANDRAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Andrienko (`KXITFWMATCH-26NOV10ANDRAT-AND`) | 0.85 / 0.88 (48) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ando Tiantsoa Ratre (`KXITFWMATCH-26NOV10ANDRAT-RAT`) | 0.12 / 0.13 (29) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Biolay / Bornay vs Abanda / Mattel -- W15 Paris QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10BIOBORABAMAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abanda / Mattel (`KXITFWDOUBLES-26NOV10BIOBORABAMAT-ABAMAT`) | 0.70 / 0.89 (2) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Biolay / Bornay (`KXITFWDOUBLES-26NOV10BIOBORABAMAT-BIOBOR`) | 0.16 / 0.51 (3) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Chen / Jie Tzeng vs Khramtsova / Utkina -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10CHEJIEKHRUTK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chen / Jie Tzeng (`KXITFWDOUBLES-26NOV10CHEJIEKHRUTK-CHEJIE`) | 0.57 / 0.86 (4) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Khramtsova / Utkina (`KXITFWDOUBLES-26NOV10CHEJIEKHRUTK-KHRUTK`) | 0.28 / 0.75 (3) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tamila Gadamauri vs Beatrise Zeltina -- W15 Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260339:260446:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tamila Gadamauri (`KXITFWMATCH-26NOV10GADZEL-GAD`) | 0.18 / 0.21 (30) | 19.5% | 40.7% | 41.5% | 43.1% [41.0%-45.7%] | -- | -- | -- | -- | PASS | +21.2 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Beatrise Zeltina (`KXITFWMATCH-26NOV10GADZEL-ZEL`) | 0.75 / 0.81 (69) | 78.0% | 59.3% | 58.5% | 56.9% [54.3%-59.0%] | -- | -- | -- | -- | PASS | -18.7 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2577.0, B 1940.0; serve-point win A 53.2%, B 45.0%; Elo A 1485.5, B 1523.4; model uncertainty 0.0236
* Form inputs: days since last match A 259, B 210; matches on record A 57, B 64; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10GADZEL-GAD  (YES = Tamila Gadamauri)
Model: 41%
Kalshi: 20%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose -0.011, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Starkova / Suslova vs Bosman / Reguer -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10STASUSBOSREG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bosman / Reguer (`KXITFWDOUBLES-26NOV10STASUSBOSREG-BOSREG`) | 0.77 / 0.79 (119) | 78.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Starkova / Suslova (`KXITFWDOUBLES-26NOV10STASUSBOSREG-STASUS`) | 0.14 / 0.39 (2) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Thomias / Vasileva vs Kochta / Sousa Salazar -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 17:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10THOVASKOCSOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kochta / Sousa Salazar (`KXITFWDOUBLES-26NOV10THOVASKOCSOU-KOCSOU`) | 0.52 / 0.66 (9) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thomias / Vasileva (`KXITFWDOUBLES-26NOV10THOVASKOCSOU-THOVAS`) | 0.35 / 0.53 (31) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nikola Mektic / Edouard Roger-Vasselin vs Robert Cash / Alexander Erler -- ATP Stockholm 1/8 F

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-10 13:00Z
* Current expected start: 2026-11-10 18:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-09 22:48Z
* Recommended handicap-by time: 2026-11-10 17:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-10T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10MEKROGCASERL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robert Cash / Alexander Erler (`KXATPDOUBLES-26NOV10MEKROGCASERL-CASERL`) | 0.32 / 0.38 (54) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nikola Mektic / Edouard Roger-Vasselin (`KXATPDOUBLES-26NOV10MEKROGCASERL-MEKROG`) | 0.62 / 0.65 (9) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Bothma / Gabet vs Belkovics / Naw -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BOTGABBELNAW:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Belkovics / Naw (`KXITFDOUBLES-26NOV10BOTGABBELNAW-BELNAW`) | 0.30 / 0.57 (58) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bothma / Gabet (`KXITFDOUBLES-26NOV10BOTGABBELNAW-BOTGAB`) | 0.37 / 0.65 (71) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Campbell / Kalaitzis vs Gannon / Taguchi -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10CAMKALGANTAG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Campbell / Kalaitzis (`KXITFDOUBLES-26NOV10CAMKALGANTAG-CAMKAL`) | 0.05 / 0.07 (22) | 6.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gannon / Taguchi (`KXITFDOUBLES-26NOV10CAMKALGANTAG-GANTAG`) | 0.87 / 0.93 (1) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## valentino conte vs Tobia Grandinetti -- M15 Roldan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211634:214331:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| valentino conte (`KXITFMATCH-26NOV10CONGRA-CON`) | 0.39 / 0.94 (107) | 66.5% | 53.3% | 39.7% | 56.2% [54.2%-58.2%] | -- | -- | -- | -- | PASS | -13.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tobia Grandinetti (`KXITFMATCH-26NOV10CONGRA-GRA`) | 0.05 / 0.66 (10) | 35.5% | 46.7% | 60.3% | 43.8% [41.8%-45.8%] | -- | -- | -- | -- | PASS | +11.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 115.0, B 160.0; serve-point win A 58.8%, B 41.8%; Elo A 1323.0, B 1265.5; model uncertainty 0.02
* Form inputs: days since last match A 350, B 357; matches on record A 3, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentin Garay vs Facundo Perlov -- M15 Roldan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10GARPER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentin Garay (`KXITFMATCH-26NOV10GARPER-GAR`) | 0.37 / 0.91 (7) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Facundo Perlov (`KXITFMATCH-26NOV10GARPER-PER`) | 0.06 / 0.63 (5) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joseph hernandez vs Lautaro Rocha -- M15 Roldan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:214261:214279:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joseph hernandez (`KXITFMATCH-26NOV10HERROC-HER`) | 0.26 / 0.27 (39) | 26.5% | 46.2% | 56.2% | 52.1% [52.1%-52.1%] | -- | -- | -- | -- | PASS | +19.7 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lautaro Rocha (`KXITFMATCH-26NOV10HERROC-ROC`) | 0.67 / 0.94 (5) | 80.5% | 53.8% | 43.8% | 47.9% [47.9%-47.9%] | -- | -- | -- | -- | PASS | -26.7 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 59.0, B 189.0; serve-point win A 58.0%, B 41.3%; Elo A 1259.0, B 1243.7; model uncertainty 0.0002
* Form inputs: days since last match A 357, B 245; matches on record A 1, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10HERROC-HER  (YES = Joseph hernandez)
Model: 46%
Kalshi: 26%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hopp / Longwe-Smit vs Alessandro Erhardt / Hartig -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10HOPLONALEHAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessandro Erhardt / Hartig (`KXITFDOUBLES-26NOV10HOPLONALEHAR-ALEHAR`) | 0.16 / 0.39 (3) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hopp / Longwe-Smit (`KXITFDOUBLES-26NOV10HOPLONALEHAR-HOPLON`) | 0.69 / 0.89 (15) | 79.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jones / Jones vs Dermenjyan / Schinas -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10JONJONDERSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dermenjyan / Schinas (`KXITFDOUBLES-26NOV10JONJONDERSCH-DERSCH`) | 0.04 / 0.89 (56) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jones / Jones (`KXITFDOUBLES-26NOV10JONJONDERSCH-JONJON`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kaan Oktay / Schlossmann vs Yves Bailly / Herman -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10KAASCHYVEHER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kaan Oktay / Schlossmann (`KXITFDOUBLES-26NOV10KAASCHYVEHER-KAASCH`) | 0.13 / 0.39 (42) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yves Bailly / Herman (`KXITFDOUBLES-26NOV10KAASCHYVEHER-YVEHER`) | 0.76 / 0.80 (125) | 78.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kaouk / Trufelli vs Knitter / Sterniczuk -- M15 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10KAOTRUKNISTE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kaouk / Trufelli (`KXITFDOUBLES-26NOV10KAOTRUKNISTE-KAOTRU`) | 0.70 / 0.81 (131) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Knitter / Sterniczuk (`KXITFDOUBLES-26NOV10KAOTRUKNISTE-KNISTE`) | 0.15 / 0.36 (3) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tadeo Meneo vs Gonzalo Zeitune -- M15 Roldan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211698:212745:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tadeo Meneo (`KXITFMATCH-26NOV10MENZEI-MEN`) | 0.38 / 0.59 (14) | 48.5% | 57.0% | 37.0% | 45.9% [45.4%-46.9%] | -- | -- | -- | -- | PASS | +8.4 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gonzalo Zeitune (`KXITFMATCH-26NOV10MENZEI-ZEI`) | 0.35 / 0.58 (5) | 46.5% | 43.0% | 63.0% | 54.1% [53.0%-54.6%] | -- | -- | -- | -- | PASS | -3.5 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1020.0, B 170.0; serve-point win A 62.0%, B 39.4%; Elo A 1107.5, B 1126.4; model uncertainty 0.0076
* Form inputs: days since last match A 196, B 245; matches on record A 36, B 13; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yshai Oliel vs Daniel Jade -- M25 Vale do Lobo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200075:212711:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Jade (`KXITFMATCH-26NOV10OLIJAD-JAD`) | 0.58 / 0.64 (41) | 61.0% | 27.0% | 45.9% | 28.4% [19.9%-32.8%] | -- | -- | -- | -- | PASS | -34.0 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yshai Oliel (`KXITFMATCH-26NOV10OLIJAD-OLI`) | 0.37 / 0.41 (43) | 39.0% | 73.0% | 54.1% | 71.6% [67.2%-80.1%] | -- | -- | -- | -- | PASS | +34.0 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 703.0, B 691.0; serve-point win A 64.2%, B 40.6%; Elo A 1437.4, B 1212.1; model uncertainty 0.0647
* Form inputs: days since last match A 364, B 28; matches on record A 433, B 23; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10OLIJAD-OLI  (YES = Yshai Oliel)
Model: 73%
Kalshi: 39%
Gap: +34 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.018, surface_dev_loose -0.009, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Omarkhanov / Paganetti vs Bredschneijder / Pontjodikromo -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10OMAPAGBREPON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bredschneijder / Pontjodikromo (`KXITFDOUBLES-26NOV10OMAPAGBREPON-BREPON`) | 0.41 / 0.75 (3) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Omarkhanov / Paganetti (`KXITFDOUBLES-26NOV10OMAPAGBREPON-OMAPAG`) | 0.44 / 0.78 (3) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sergi Perez Contri vs John Sperle -- M25 San Gregorio di Catania R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:133997:210145:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sergi Perez Contri (`KXITFMATCH-26NOV10PERSPE-PER`) | 0.58 / 0.64 (46) | 61.0% | 65.2% | 65.0% | 62.5% [60.5%-64.6%] | -- | -- | -- | -- | PASS | +4.2 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| John Sperle (`KXITFMATCH-26NOV10PERSPE-SPE`) | 0.33 / 0.40 (1) | 36.5% | 34.8% | 34.9% | 37.5% [35.4%-39.5%] | -- | -- | -- | -- | PASS | -1.7 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3673.0, B 2038.0; serve-point win A 56.1%, B 46.8%; Elo A 1483.0, B 1418.7; model uncertainty 0.0204
* Form inputs: days since last match A 196, B 42; matches on record A 359, B 177; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Potenza / Tabacco vs La Vela / Marino -- M25 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10POTTABLAVMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| La Vela / Marino (`KXITFDOUBLES-26NOV10POTTABLAVMAR-LAVMAR`) | 0.09 / 0.34 (18) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Potenza / Tabacco (`KXITFDOUBLES-26NOV10POTTABLAVMAR-POTTAB`) | 0.76 / 0.88 (6) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Stanke / Van Herck vs Karpinski / Piasek -- M15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10STAVANKARPIA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karpinski / Piasek (`KXITFDOUBLES-26NOV10STAVANKARPIA-KARPIA`) | 0.05 / 0.20 (6) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stanke / Van Herck (`KXITFDOUBLES-26NOV10STAVANKARPIA-STAVAN`) | 0.83 / 0.95 (37) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Benesova / Velits vs De Baene / Djafari -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10BENVELDEBDJA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benesova / Velits (`KXITFWDOUBLES-26NOV10BENVELDEBDJA-BENVEL`) | 0.09 / 0.85 (53) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| De Baene / Djafari (`KXITFWDOUBLES-26NOV10BENVELDEBDJA-DEBDJA`) | 0.10 / 0.88 (41) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Anastasia Bertacchi vs Maja Wrobel -- W15 Monastir R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264130:270208:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Bertacchi (`KXITFWMATCH-26NOV10BERWRO-BER`) | 0.71 / 0.76 (61) | 73.5% | 85.2% | 45.2% | 63.6% [60.6%-67.5%] | -- | -- | -- | -- | PASS | +11.7 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maja Wrobel (`KXITFWMATCH-26NOV10BERWRO-WRO`) | 0.23 / 0.27 (3) | 25.0% | 14.8% | 54.8% | 36.4% [32.5%-39.5%] | -- | -- | -- | -- | PASS | -10.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1382.0, B 62.0; serve-point win A 57.4%, B 50.5%; Elo A 1369.6, B 1264.4; model uncertainty 0.0348
* Form inputs: days since last match A 114, B 448; matches on record A 81, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.030, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bhopal / Cai vs Ehrenbergerova / Fusil -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10BHOCAIEHRFUS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bhopal / Cai (`KXITFWDOUBLES-26NOV10BHOCAIEHRFUS-BHOCAI`) | 0.07 / 0.90 (1) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ehrenbergerova / Fusil (`KXITFWDOUBLES-26NOV10BHOCAIEHRFUS-EHRFUS`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cheong / Watanabe vs Husar / Lizunova -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10CHEWATHUSLIZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cheong / Watanabe (`KXITFWDOUBLES-26NOV10CHEWATHUSLIZ-CHEWAT`) | 0.33 / 0.67 (3) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Husar / Lizunova (`KXITFWDOUBLES-26NOV10CHEWATHUSLIZ-HUSLIZ`) | 0.46 / 0.75 (6) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dorofeeva-Rybas / Zhenikhova vs Andronicou / Safina Popa -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10DORZHEANDSAF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andronicou / Safina Popa (`KXITFWDOUBLES-26NOV10DORZHEANDSAF-ANDSAF`) | 0.08 / 0.22 (32) | 15.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dorofeeva-Rybas / Zhenikhova (`KXITFWDOUBLES-26NOV10DORZHEANDSAF-DORZHE`) | 0.78 / 0.90 (1) | 84.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Georgiana Goina / Ogescu vs Jovanovic / Spasova -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10GEOOGEJOVSPA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Georgiana Goina / Ogescu (`KXITFWDOUBLES-26NOV10GEOOGEJOVSPA-GEOOGE`) | 0.81 / 0.90 (1) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jovanovic / Spasova (`KXITFWDOUBLES-26NOV10GEOOGEJOVSPA-JOVSPA`) | 0.06 / 0.24 (2) | 15.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Luciano / Mariani vs Donnell / Mewett -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10LUCMARDONMEW:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Donnell / Mewett (`KXITFWDOUBLES-26NOV10LUCMARDONMEW-DONMEW`) | 0.05 / 0.89 (56) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luciano / Mariani (`KXITFWDOUBLES-26NOV10LUCMARDONMEW-LUCMAR`) | 0.06 / 0.95 (101) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Miron / Nicoleta Todoni vs Argyrokastriti / Cortez Llorca -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10MIRNICARGCOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Argyrokastriti / Cortez Llorca (`KXITFWDOUBLES-26NOV10MIRNICARGCOR-ARGCOR`) | 0.78 / 0.92 (41) | 85.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Miron / Nicoleta Todoni (`KXITFWDOUBLES-26NOV10MIRNICARGCOR-MIRNIC`) | 0.14 / 0.17 (30) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Pochtovyk / Sagmar vs Karatancheva / Shapatava -- W35 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10POCSAGKARSHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karatancheva / Shapatava (`KXITFWDOUBLES-26NOV10POCSAGKARSHA-KARSHA`) | 0.85 / 0.94 (10) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pochtovyk / Sagmar (`KXITFWDOUBLES-26NOV10POCSAGKARSHA-POCSAG`) | 0.05 / 0.19 (131) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Lorenzo Musetti vs Toby Samuel -- ATP Stockholm R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-10 21:10Z
* Current expected start: 2026-11-10 18:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-09 22:48Z
* Recommended handicap-by time: 2026-11-10 17:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (TOUR_500_250) · Hard · scheduled 2026-11-10T21:10:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207518:210389:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Musetti (`KXATPMATCH-26NOV10MUSSAM-MUS`) | 0.73 / 0.79 (125) | 76.0% | 69.5% | 50.5% | 56.5% [51.0%-66.0%] | 71.8% | -- | 71.8% | MODEL_LONE_OUTLIER | PASS | -6.5 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Toby Samuel (`KXATPMATCH-26NOV10MUSSAM-SAM`) | 0.21 / 0.27 (5) | 24.0% | 30.6% | 49.5% | 43.5% [34.0%-49.0%] | 28.2% | -- | 28.2% | MODEL_LONE_OUTLIER | PASS | +6.5 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 5369.0, B 4150.0; serve-point win A 66.0%, B 38.0%; Elo A 1960.0, B 1799.7; model uncertainty 0.0749
* Form inputs: days since last match A 4, B 1; matches on record A 493, B 196; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.039, surface_pool_high -0.040, surface_dev_loose -0.015, surface_dev_tight +0.020
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV10MUSSAM-SAM20` Will Toby Samuel win the Lorenzo Musetti vs Toby Samuel match by a set score of 2-0?: 0.04/0.72 mid 38.0%, model 13.5% (projection_v2.0 (prediction ledger)) -- gap -24.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MUSSAM-SAM21` Will Toby Samuel win the Lorenzo Musetti vs Toby Samuel match by a set score of 2-1?: 0.04/0.72 mid 38.0%, model 17.1% (projection_v2.0 (prediction ledger)) -- gap -20.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MUSSAM-2-MUS` Will Lorenzo Musetti win set 2 in the Lorenzo Musetti vs Toby Samuel match: 0.03/0.95 mid 49.0%, model 63.3% (projection_v2.0 (prediction ledger)) -- gap +14.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MUSSAM-1-MUS` Will Lorenzo Musetti win set 1 in the Lorenzo Musetti vs Toby Samuel match: 0.05/0.94 mid 49.5%, model 63.3% (projection_v2.0 (prediction ledger)) -- gap +13.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MUSSAM-MUS21` Will Lorenzo Musetti win the Lorenzo Musetti vs Toby Samuel match by a set score of 2-1?: 0.02/0.31 mid 16.5%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +12.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10MUSSAM-MUS4` Will Lorenzo Musetti win at least 3.5 more games than Toby Samuel?: 0.52/0.59 mid 55.5%, model 43.0% (projection_v2.0 (prediction ledger)) -- gap -12.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MUSSAM-1-SAM` Will Toby Samuel win set 1 in the Lorenzo Musetti vs Toby Samuel match: 0.03/0.94 mid 48.5%, model 36.7% (projection_v2.0 (prediction ledger)) -- gap -11.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV10MUSSAM-MUS20` Will Lorenzo Musetti win the Lorenzo Musetti vs Toby Samuel match by a set score of 2-0?: 0.03/0.54 mid 28.5%, model 40.0% (projection_v2.0 (prediction ledger)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV10MUSSAM-2-SAM` Will Toby Samuel win set 2 in the Lorenzo Musetti vs Toby Samuel match: 0.01/0.95 mid 48.0%, model 36.7% (projection_v2.0 (prediction ledger)) -- gap -11.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV10MUSSAM-28` Over 27.5 games: 0.20/0.35 mid 27.5%, model 37.9% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10MUSSAM-MUS7` Will Lorenzo Musetti win at least 6.5 more games than Toby Samuel?: 0.11/0.26 mid 18.5%, model 8.5% (projection_v2.0 (prediction ledger)) -- gap -10.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV10MUSSAM-23` Over 22.5 games: 0.42/0.54 mid 48.0%, model 57.7% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV10MUSSAM-18` Over 17.5 games: 0.79/0.93 mid 86.0%, model 92.1% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV10MUSSAM-SAM2` Will Toby Samuel win at least 1.5 more games than Lorenzo Musetti?: 0.13/0.28 mid 20.5%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Caliman / Sarganella Verdu vs Ferrer Perez / Camila Rojas -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10CALSARFERCAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caliman / Sarganella Verdu (`KXITFWDOUBLES-26NOV10CALSARFERCAM-CALSAR`) | 0.05 / 0.27 (2) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ferrer Perez / Camila Rojas (`KXITFWDOUBLES-26NOV10CALSARFERCAM-FERCAM`) | 0.79 / 0.95 (101) | 87.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Natal / Ros Parres vs Pares Bergnes de las Casas / Quesada Oyonarte -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10NATROSPARQUE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Natal / Ros Parres (`KXITFWDOUBLES-26NOV10NATROSPARQUE-NATROS`) | 0.55 / 0.77 (2) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pares Bergnes de las Casas / Quesada Oyonarte (`KXITFWDOUBLES-26NOV10NATROSPARQUE-PARQUE`) | 0.31 / 0.51 (14) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Pozarenko / Torner Sensano vs Boron / Litvinova -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10POZTORBORLIT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boron / Litvinova (`KXITFWDOUBLES-26NOV10POZTORBORLIT-BORLIT`) | 0.05 / 0.17 (2) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pozarenko / Torner Sensano (`KXITFWDOUBLES-26NOV10POZTORBORLIT-POZTOR`) | 0.85 / 0.94 (56) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## David Aguiar Johansson vs David Vega Hernandez -- M15 Las Palmas de Gran Canaria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:110754:214253:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Aguiar Johansson (`KXITFMATCH-26NOV10AGUVEG-AGU`) | 0.25 / 0.77 (3) | 51.0% | 22.2% | 59.4% | 27.3% [22.6%-32.6%] | -- | -- | -- | -- | PASS | -28.8 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| David Vega Hernandez (`KXITFMATCH-26NOV10AGUVEG-VEG`) | 0.60 / 0.84 (4) | 72.0% | 77.8% | 40.6% | 72.7% [67.4%-77.4%] | -- | -- | -- | -- | PASS | +5.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 85.0, B 111.0; serve-point win A 54.5%, B 39.7%; Elo A 1248.1, B 1431.9; model uncertainty 0.0501
* Form inputs: days since last match A 364, B 238; matches on record A 1, B 418; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.036, surface_dev_loose -0.001, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alberto Barroso Campos vs Samuele Seghetti -- M15 Las Palmas de Gran Canaria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132744:213064:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alberto Barroso Campos (`KXITFMATCH-26NOV10BARSEG-BAR`) | 0.63 / 0.69 (42) | 66.0% | 68.7% | 70.5% | 68.7% [64.4%-72.7%] | -- | -- | -- | -- | PASS | +2.6 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Samuele Seghetti (`KXITFMATCH-26NOV10BARSEG-SEG`) | 0.31 / 0.34 (1) | 32.5% | 31.4% | 29.5% | 31.3% [27.3%-35.6%] | -- | -- | -- | -- | PASS | -1.1 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2471.0, B 1318.0; serve-point win A 59.2%, B 44.5%; Elo A 1325.2, B 1205.0; model uncertainty 0.0418
* Form inputs: days since last match A 42, B 196; matches on record A 365, B 39; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.041, surface_pool_high -0.043, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giovanni Branchetti vs Agustin Fernandez Badia -- M15 Roldan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BRAFER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giovanni Branchetti (`KXITFMATCH-26NOV10BRAFER-BRA`) | 0.08 / 0.92 (25) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Agustin Fernandez Badia (`KXITFMATCH-26NOV10BRAFER-FER`) | 0.08 / 0.95 (328) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carles Cordoba vs Valentin Gonzalez-Galino -- M15 Las Palmas de Gran Canaria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213059:213228:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carles Cordoba (`KXITFMATCH-26NOV10CORGON-COR`) | 0.71 / 0.74 (39) | 72.5% | 76.2% | 54.2% | 64.5% [63.4%-65.7%] | -- | -- | -- | -- | PASS | +3.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentin Gonzalez-Galino (`KXITFMATCH-26NOV10CORGON-GON`) | 0.23 / 0.30 (3) | 26.5% | 23.8% | 45.8% | 35.5% [34.3%-36.6%] | -- | -- | -- | -- | PASS | -2.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1490.0, B 169.0; serve-point win A 58.7%, B 46.7%; Elo A 1289.8, B 1178.6; model uncertainty 0.0115
* Form inputs: days since last match A 203, B 364; matches on record A 42, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francisco Crosio vs Juan Ignacio Centurion Delvalle -- M15 Roldan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213660:214284:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Ignacio Centurion Delvalle (`KXITFMATCH-26NOV10CROCEN-CEN`) | 0.06 / 0.95 (315) | 50.5% | 38.5% | 36.2% | 40.7% [40.6%-40.8%] | -- | -- | -- | -- | PASS | -12.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Francisco Crosio (`KXITFMATCH-26NOV10CROCEN-CRO`) | 0.05 / 0.95 (293) | 50.0% | 61.5% | 63.8% | 59.3% [59.2%-59.4%] | -- | -- | -- | -- | PASS | +11.5 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 51.0, B 100.0; serve-point win A 59.8%, B 42.5%; Elo A 1262.5, B 1200.8; model uncertainty 0.0008
* Form inputs: days since last match A 357, B 364; matches on record A 1, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Knis / Robas vs Carroll / Elamin -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10KNIROBCARELA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carroll / Elamin (`KXITFDOUBLES-26NOV10KNIROBCARELA-CARELA`) | 0.58 / 0.82 (5) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Knis / Robas (`KXITFDOUBLES-26NOV10KNIROBCARELA-KNIROB`) | 0.26 / 0.46 (8) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Leal / Lima Sanches vs Da Rosa Castro / Monteiro -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10LEALIMDARMON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Da Rosa Castro / Monteiro (`KXITFDOUBLES-26NOV10LEALIMDARMON-DARMON`) | 0.54 / 0.87 (4) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leal / Lima Sanches (`KXITFDOUBLES-26NOV10LEALIMDARMON-LEALIM`) | 0.30 / 0.78 (3) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maurice / Raynel vs Karlsson Wistrand / Kumar -- M15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10MAURAYKARKUM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karlsson Wistrand / Kumar (`KXITFDOUBLES-26NOV10MAURAYKARKUM-KARKUM`) | 0.54 / 0.86 (1) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maurice / Raynel (`KXITFDOUBLES-26NOV10MAURAYKARKUM-MAURAY`) | 0.32 / 0.73 (3) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Manuel Mouilleron Salvo vs Tomas Giangrasso -- M15 Roldan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10MOUGIA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Giangrasso (`KXITFMATCH-26NOV10MOUGIA-GIA`) | 0.06 / 0.95 (315) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Manuel Mouilleron Salvo (`KXITFMATCH-26NOV10MOUGIA-MOU`) | 0.05 / 0.95 (293) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pablo Perez Ramos vs Tyler Zink -- M25 Vale do Lobo R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10PERZIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pablo Perez Ramos (`KXITFMATCH-26NOV10PERZIN-PER`) | 0.23 / 0.26 (26) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tyler Zink (`KXITFMATCH-26NOV10PERZIN-ZIN`) | 0.72 / 0.74 (96) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Santiago Pesino vs Ian Vertberger -- M15 Roldan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212868:213955:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Santiago Pesino (`KXITFMATCH-26NOV10PESVER-PES`) | 0.06 / 0.95 (315) | 50.5% | 65.0% | 58.8% | 62.4% [62.0%-62.5%] | -- | -- | -- | -- | PASS | +14.5 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ian Vertberger (`KXITFMATCH-26NOV10PESVER-VER`) | 0.05 / 0.95 (293) | 50.0% | 35.0% | 41.2% | 37.6% [37.5%-38.0%] | -- | -- | -- | -- | PASS | -15.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 121.0, B 366.0; serve-point win A 59.0%, B 43.9%; Elo A 1211.5, B 1118.1; model uncertainty 0.0025
* Form inputs: days since last match A 196, B 350; matches on record A 2, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matias Ponce de leon gomila vs Iliyan Radulov -- M15 Las Palmas de Gran Canaria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210038:210721:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matias Ponce de leon gomila (`KXITFMATCH-26NOV10PONRAD-PON`) | 0.25 / 0.26 (34) | 25.5% | 25.6% | 57.8% | 24.8% [19.4%-30.9%] | -- | -- | -- | -- | PASS | +0.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Iliyan Radulov (`KXITFMATCH-26NOV10PONRAD-RAD`) | 0.76 / 0.82 (2) | 79.0% | 74.4% | 42.2% | 75.2% [69.1%-80.5%] | -- | -- | -- | -- | PASS | -4.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 397.0, B 2013.0; serve-point win A 55.5%, B 39.5%; Elo A 1265.0, B 1523.1; model uncertainty 0.0571
* Form inputs: days since last match A 413, B 49; matches on record A 13, B 147; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.000, surface_dev_loose +0.008, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Poritskyy / Qabazard vs Facek / Panik -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10PORQABFACPAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Facek / Panik (`KXITFDOUBLES-26NOV10PORQABFACPAN-FACPAN`) | 0.55 / 0.72 (4) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Poritskyy / Qabazard (`KXITFDOUBLES-26NOV10PORQABFACPAN-PORQAB`) | 0.32 / 0.71 (3) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lorenzo Joaquin Rodriguez vs Javier Barranco Cosano -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200266:202271:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Javier Barranco Cosano (`KXITFMATCH-26NOV10RODBAR-BAR`) | 0.23 / 0.88 (208) | 55.5% | 65.8% | 51.0% | 57.3% [54.7%-61.9%] | -- | -- | -- | -- | PASS | +10.3 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorenzo Joaquin Rodriguez (`KXITFMATCH-26NOV10RODBAR-ROD`) | 0.13 / 0.81 (132) | 47.0% | 34.2% | 48.9% | 42.7% [38.1%-45.3%] | -- | -- | -- | -- | PASS | -12.8 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3239.0, B 2822.0; serve-point win A 55.1%, B 41.8%; Elo A 1451.1, B 1596.4; model uncertainty 0.0359
* Form inputs: days since last match A 7, B 35; matches on record A 264, B 571; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pedro Sakamoto vs Victor Braga -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106203:212786:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victor Braga (`KXITFMATCH-26NOV10SAKBRA-BRA`) | 0.07 / 0.75 (14) | 41.0% | 8.7% | 3.9% | 6.6% [4.5%-9.3%] | -- | -- | -- | -- | PASS | -32.3 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Pedro Sakamoto (`KXITFMATCH-26NOV10SAKBRA-SAK`) | 0.63 / 0.95 (293) | 79.0% | 91.3% | 96.1% | 93.4% [90.7%-95.5%] | -- | -- | -- | -- | PASS | +12.3 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 3163.0, B 1053.0; serve-point win A 62.6%, B 47.7%; Elo A 1521.4, B 1132.3; model uncertainty 0.0241
* Form inputs: days since last match A 42, B 196; matches on record A 717, B 26; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.009, surface_dev_loose +0.008, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luna Maria Cinalli vs Barbara Krupek Soccol -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10CINKRU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luna Maria Cinalli (`KXITFWMATCH-26NOV10CINKRU-CIN`) | 0.05 / 0.36 (1) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Barbara Krupek Soccol (`KXITFWMATCH-26NOV10CINKRU-KRU`) | 0.58 / 0.93 (5) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jaeger / Masiianskaia vs Dupasquier-Picci / Kokotuha -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10JAEMASDUPKOK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dupasquier-Picci / Kokotuha (`KXITFWDOUBLES-26NOV10JAEMASDUPKOK-DUPKOK`) | 0.06 / 0.94 (56) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jaeger / Masiianskaia (`KXITFWDOUBLES-26NOV10JAEMASDUPKOK-JAEMAS`) | 0.08 / 0.94 (56) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Julia Julia Cerqueira Carvalho Farias Lima vs Laura Goncalves Portela Borges -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:267383:269739:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Julia Cerqueira Carvalho Farias Lima (`KXITFWMATCH-26NOV10JULPOR-JUL`) | 0.90 / 0.95 (10) | 92.5% | 76.1% | 50.0% | 54.3% [54.3%-54.3%] | -- | -- | -- | -- | PASS | -16.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Laura Goncalves Portela Borges (`KXITFWMATCH-26NOV10JULPOR-POR`) | 0.04 / 0.13 (2) | 8.5% | 23.8% | 50.0% | 45.7% [45.7%-45.7%] | -- | -- | -- | -- | PASS | +15.3 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 56.5%, B 48.8%; Elo A 1167.2, B 1139.6; model uncertainty 0.0
* Form inputs: days since last match A 714, B 700; matches on record A 6, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10JULPOR-POR  (YES = Laura Goncalves Portela Borges)
Model: 24%
Kalshi: 8%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sophia Santos vs Kauany Rodrigues -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10SANROD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kauany Rodrigues (`KXITFWMATCH-26NOV10SANROD-ROD`) | 0.45 / 0.66 (74) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sophia Santos (`KXITFWMATCH-26NOV10SANROD-SAN`) | 0.28 / 0.53 (184) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mariana de Jesus Ribeiro Silveira vs Lais Lobo Assumpcao Euzebio -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10SILLOB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lais Lobo Assumpcao Euzebio (`KXITFWMATCH-26NOV10SILLOB-LOB`) | 0.08 / 0.91 (1) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mariana de Jesus Ribeiro Silveira (`KXITFWMATCH-26NOV10SILLOB-SIL`) | 0.05 / 0.88 (1) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Brunet-Brady / Dournes vs Brooks / Ngounoue -- W15 Paris QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10BRUDOUBRONGO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brooks / Ngounoue (`KXITFWDOUBLES-26NOV10BRUDOUBRONGO-BRONGO`) | 0.05 / 0.95 (76) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Brunet-Brady / Dournes (`KXITFWDOUBLES-26NOV10BRUDOUBRONGO-BRUDOU`) | 0.05 / 0.95 (76) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Brady / Howse vs Marques / Rocha -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10BRAHOWMARROC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brady / Howse (`KXITFDOUBLES-26NOV10BRAHOWMARROC-BRAHOW`) | 0.32 / 0.51 (17) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marques / Rocha (`KXITFDOUBLES-26NOV10BRAHOWMARROC-MARROC`) | 0.55 / 0.71 (12) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Forcano / Izquierdo Luque vs Cacao / Dinis Silva -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10FORIZQCACDIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cacao / Dinis Silva (`KXITFDOUBLES-26NOV10FORIZQCACDIN-CACDIN`) | 0.13 / 0.29 (7) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Forcano / Izquierdo Luque (`KXITFDOUBLES-26NOV10FORIZQCACDIN-FORIZQ`) | 0.75 / 0.90 (36) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Johns / Rodenas vs Maia / Valdoleiros -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10JOHRODMAIVAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Johns / Rodenas (`KXITFDOUBLES-26NOV10JOHRODMAIVAL-JOHROD`) | 0.72 / 0.89 (5) | 80.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maia / Valdoleiros (`KXITFDOUBLES-26NOV10JOHRODMAIVAL-MAIVAL`) | 0.14 / 0.30 (2) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Augusto Land vs Gabriel Augusto Carvalho -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10LANCAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriel Augusto Carvalho (`KXITFMATCH-26NOV10LANCAR-CAR`) | 0.05 / 0.95 (315) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Augusto Land (`KXITFMATCH-26NOV10LANCAR-LAN`) | 0.05 / 0.95 (293) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Massucco / Mecarelli vs Condorelli / Frost -- M25 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10MASMECCONFRO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Condorelli / Frost (`KXITFDOUBLES-26NOV10MASMECCONFRO-CONFRO`) | 0.04 / 0.95 (10) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Massucco / Mecarelli (`KXITFDOUBLES-26NOV10MASMECCONFRO-MASMEC`) | 0.04 / 0.95 (10) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Thiago Horacio Messa vs Breno Braga -- M25 Santa Cruz do Sul R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10MESBRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Breno Braga (`KXITFMATCH-26NOV10MESBRA-BRA`) | 0.05 / 0.95 (315) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thiago Horacio Messa (`KXITFMATCH-26NOV10MESBRA-MES`) | 0.05 / 0.95 (293) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Molleker / Sorger vs Almazan Valiente / Lagutin -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10MOLSORALMLAG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Almazan Valiente / Lagutin (`KXITFDOUBLES-26NOV10MOLSORALMLAG-ALMLAG`) | 0.53 / 0.71 (12) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Molleker / Sorger (`KXITFDOUBLES-26NOV10MOLSORALMLAG-MOLSOR`) | 0.33 / 0.53 (20) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Adrover Gallego / Sagrista Bermejo vs Cabassers Morros / Cabassers Morros -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10ADRSAGCABCAB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrover Gallego / Sagrista Bermejo (`KXITFWDOUBLES-26NOV10ADRSAGCABCAB-ADRSAG`) | 0.74 / 0.90 (9) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cabassers Morros / Cabassers Morros (`KXITFWDOUBLES-26NOV10ADRSAGCABCAB-CABCAB`) | 0.13 / 0.30 (56) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Iankovskaia / Toma vs Paula Bastos-Sousa Betanzos / Trujillo Garnica -- W15 Nules R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10IANTOMPAUTRU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iankovskaia / Toma (`KXITFWDOUBLES-26NOV10IANTOMPAUTRU-IANTOM`) | 0.76 / 0.88 (208) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Paula Bastos-Sousa Betanzos / Trujillo Garnica (`KXITFWDOUBLES-26NOV10IANTOMPAUTRU-PAUTRU`) | 0.10 / 0.29 (56) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sofia Merlos Cardoso vs Giulia Gomes Ferreira -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10MERGOM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giulia Gomes Ferreira (`KXITFWMATCH-26NOV10MERGOM-GOM`) | 0.04 / 0.95 (10) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofia Merlos Cardoso (`KXITFWMATCH-26NOV10MERGOM-MER`) | 0.04 / 0.95 (110) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lara Moreira Kanadani vs Eduarda Gomes -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10MORGOM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eduarda Gomes (`KXITFWMATCH-26NOV10MORGOM-GOM`) | 0.04 / 0.95 (10) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lara Moreira Kanadani (`KXITFWMATCH-26NOV10MORGOM-MOR`) | 0.04 / 0.95 (110) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dominiquea Romanholi vs Julia Pretti -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10ROMPRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Pretti (`KXITFWMATCH-26NOV10ROMPRE-PRE`) | 0.12 / 0.57 (58) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dominiquea Romanholi (`KXITFWMATCH-26NOV10ROMPRE-ROM`) | 0.40 / 0.81 (132) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isadora Sigrist vs Larissa Lopes Missato -- W15 São Carlos R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10SIGLOP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Larissa Lopes Missato (`KXITFWMATCH-26NOV10SIGLOP-LOP`) | 0.07 / 0.41 (43) | 24.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Isadora Sigrist (`KXITFWMATCH-26NOV10SIGLOP-SIG`) | 0.55 / 0.87 (6) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Allen / Kaczmarek vs Garcia Longo / Miletich -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ALLKACGARMIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Allen / Kaczmarek (`KXITFDOUBLES-26NOV10ALLKACGARMIL-ALLKAC`) | 0.09 / 0.78 (3) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Garcia Longo / Miletich (`KXITFDOUBLES-26NOV10ALLKACGARMIL-GARMIL`) | 0.77 / 0.94 (2) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arce Fernandez / Belda vs Berto Bosca / Montero Nicolau -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ARCBELBERMON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arce Fernandez / Belda (`KXITFDOUBLES-26NOV10ARCBELBERMON-ARCBEL`) | 0.78 / 0.95 (12) | 86.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Berto Bosca / Montero Nicolau (`KXITFDOUBLES-26NOV10ARCBELBERMON-BERMON`) | 0.08 / 0.78 (3) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Camara / Sajjid Koothrat vs Naharro / Pujol Navarro -- M15 Las Palmas de Gran Canaria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10CAMSAJNAHPUJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Camara / Sajjid Koothrat (`KXITFDOUBLES-26NOV10CAMSAJNAHPUJ-CAMSAJ`) | 0.04 / 0.95 (10) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Naharro / Pujol Navarro (`KXITFDOUBLES-26NOV10CAMSAJNAHPUJ-NAHPUJ`) | 0.04 / 0.95 (10) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Thomas Gimenez vs Marcel Zielinski -- M15 Las Palmas de Gran Canaria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210505:213645:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thomas Gimenez (`KXITFMATCH-26NOV10GIMZIE-GIM`) | 0.05 / 0.06 (26) | 5.5% | 16.4% | 23.2% | 27.9% [25.2%-30.4%] | -- | -- | -- | -- | PASS | +10.9 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marcel Zielinski (`KXITFMATCH-26NOV10GIMZIE-ZIE`) | 0.90 / 0.95 (294) | 92.5% | 83.6% | 76.8% | 72.1% [69.6%-74.8%] | -- | -- | -- | -- | PASS | -8.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 106.0, B 2564.0; serve-point win A 51.3%, B 41.4%; Elo A 1232.1, B 1392.0; model uncertainty 0.0261
* Form inputs: days since last match A 273, B 224; matches on record A 3, B 151; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.018, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alhussein Abdel Aziz / Samir vs Janssen / Lopez -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10ALHSAMJANLOP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alhussein Abdel Aziz / Samir (`KXITFWDOUBLES-26NOV10ALHSAMJANLOP-ALHSAM`) | 0.89 / 0.95 (76) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Janssen / Lopez (`KXITFWDOUBLES-26NOV10ALHSAMJANLOP-JANLOP`) | 0.06 / 0.11 (42) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Dmitrichenko / Kurt vs Snigireva / Ziatdinova -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10DMIKURSNIZIA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dmitrichenko / Kurt (`KXITFWDOUBLES-26NOV10DMIKURSNIZIA-DMIKUR`) | 0.13 / 0.91 (42) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Snigireva / Ziatdinova (`KXITFWDOUBLES-26NOV10DMIKURSNIZIA-SNIZIA`) | 0.11 / 0.90 (20) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ivanovic / Smart vs Sedenkova / Shmeleva -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10IVASMASEDSHM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ivanovic / Smart (`KXITFWDOUBLES-26NOV10IVASMASEDSHM-IVASMA`) | 0.40 / 0.69 (36) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sedenkova / Shmeleva (`KXITFWDOUBLES-26NOV10IVASMASEDSHM-SEDSHM`) | 0.37 / 0.63 (14) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mateo Del Pino vs Valentin Basel -- M15 Roldan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10DELBAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentin Basel (`KXITFMATCH-26NOV10DELBAS-BAS`) | 0.42 / 0.49 (49) | 45.5% | 39.4% | -- | -- [-----] | -- | -- | -- | -- | -- | -6.1 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mateo Del Pino (`KXITFMATCH-26NOV10DELBAS-DEL`) | 0.48 / 0.52 (43) | 50.0% | 60.6% | -- | -- [-----] | -- | -- | -- | -- | -- | +10.6 pp | REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 57.5%, B 44.5%; Elo A 1220.0, B 1141.1; model uncertainty None
* Form inputs: days since last match A 7, B 140; matches on record A 96, B 73; data quality B
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Estevez vs Federico Aguilar Cardozo -- M15 Roldan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10ESTAGU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Aguilar Cardozo (`KXITFMATCH-26NOV10ESTAGU-AGU`) | 0.32 / 0.37 (40) | 34.5% | 23.8% | -- | -- [-----] | -- | -- | -- | -- | -- | -10.7 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Juan Estevez (`KXITFMATCH-26NOV10ESTAGU-EST`) | 0.62 / 0.68 (156) | 65.0% | 76.2% | -- | -- [-----] | -- | -- | -- | -- | -- | +11.2 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 57.6%, B 47.8%; Elo A 1474.8, B 1278.4; model uncertainty None
* Form inputs: days since last match A 7, B 7; matches on record A 197, B 50; data quality C
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jerrid Gaines Jr vs Sulaiman Syed -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:214264:214503:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jerrid Gaines Jr (`KXITFMATCH-26NOV10GAISYE-GAI`) | 0.06 / 0.95 (315) | 50.5% | 57.7% | 61.8% | 50.0% [48.4%-50.0%] | -- | -- | -- | -- | PASS | +7.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sulaiman Syed (`KXITFMATCH-26NOV10GAISYE-SYE`) | 0.05 / 0.95 (293) | 50.0% | 42.3% | 38.2% | 50.0% [50.0%-51.6%] | -- | -- | -- | -- | PASS | -7.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 623.0, B 73.0; serve-point win A 59.0%, B 42.5%; Elo A 1247.9, B 1256.4; model uncertainty 0.0078
* Form inputs: days since last match A 210, B 217; matches on record A 9, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.016, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thomas Gerbaud vs Daniel Kliebhan -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212840:213695:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thomas Gerbaud (`KXITFMATCH-26NOV10GERKLI-GER`) | 0.54 / 0.86 (3) | 70.0% | 51.4% | 35.6% | 48.0% [46.6%-49.0%] | -- | -- | -- | -- | PASS | -18.6 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Daniel Kliebhan (`KXITFMATCH-26NOV10GERKLI-KLI`) | 0.32 / 0.75 (3) | 53.5% | 48.6% | 64.4% | 52.0% [51.0%-53.4%] | -- | -- | -- | -- | PASS | -4.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 568.0, B 132.0; serve-point win A 65.5%, B 34.7%; Elo A 1226.2, B 1234.6; model uncertainty 0.0119
* Form inputs: days since last match A 245, B 252; matches on record A 19, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leote Prata / Morais vs Braynin / Pecak -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10LEOMORBRAPEC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Braynin / Pecak (`KXITFDOUBLES-26NOV10LEOMORBRAPEC-BRAPEC`) | 0.24 / 0.76 (3) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leote Prata / Morais (`KXITFDOUBLES-26NOV10LEOMORBRAPEC-LEOMOR`) | 0.61 / 0.92 (3) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lucca Liu vs Balthazar Orsanic -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213175:214432:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucca Liu (`KXITFMATCH-26NOV10LIUORS-LIU`) | 0.05 / 0.95 (315) | 50.0% | 67.9% | 71.9% | 53.1% [52.1%-54.2%] | -- | -- | -- | -- | PASS | +17.9 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Balthazar Orsanic (`KXITFMATCH-26NOV10LIUORS-ORS`) | 0.05 / 0.95 (293) | 50.0% | 32.1% | 28.1% | 46.9% [45.8%-47.9%] | -- | -- | -- | -- | PASS | -17.9 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 620.0, B 56.0; serve-point win A 59.2%, B 44.3%; Elo A 1280.2, B 1267.4; model uncertainty 0.0107
* Form inputs: days since last match A 238, B 266; matches on record A 16, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10LIUORS-LIU  (YES = Lucca Liu)
Model: 68%
Kalshi: 50%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joshua Peck vs Lucas Hammond -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200234:212661:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Hammond (`KXITFMATCH-26NOV10PECHAM-HAM`) | 0.17 / 0.75 (3) | 46.0% | 64.7% | 69.5% | 68.6% [67.6%-69.6%] | -- | -- | -- | -- | PASS | +18.7 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Joshua Peck (`KXITFMATCH-26NOV10PECHAM-PEC`) | 0.69 / 0.92 (2) | 80.5% | 35.3% | 30.5% | 31.4% [30.4%-32.4%] | -- | -- | -- | -- | PASS | -45.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1103.0, B 56.0; serve-point win A 60.2%, B 36.9%; Elo A 1149.6, B 1282.5; model uncertainty 0.0098
* Form inputs: days since last match A 196, B 196; matches on record A 78, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10PECHAM-HAM  (YES = Lucas Hammond)
Model: 65%
Kalshi: 46%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose +0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Perez Ramos / Wright vs Domingues / Marques -- M25 Vale do Lobo R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10PERWRIDOMMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Domingues / Marques (`KXITFDOUBLES-26NOV10PERWRIDOMMAR-DOMMAR`) | 0.24 / 0.41 (2) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Perez Ramos / Wright (`KXITFDOUBLES-26NOV10PERWRIDOMMAR-PERWRI`) | 0.63 / 0.80 (8) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tomas Re vs Thiago Cigarran -- M15 Roldan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV10REXCIG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thiago Cigarran (`KXITFMATCH-26NOV10REXCIG-CIG`) | 0.80 / 0.87 (57) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tomas Re (`KXITFMATCH-26NOV10REXCIG-REX`) | 0.12 / 0.18 (24) | 15.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mitchell Sheldon vs Joao Portugal -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213071:213146:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Portugal (`KXITFMATCH-26NOV10SHEPOR-POR`) | 0.07 / 0.95 (315) | 51.0% | 30.7% | 27.2% | 35.9% [34.0%-35.9%] | -- | -- | -- | -- | PASS | -20.3 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mitchell Sheldon (`KXITFMATCH-26NOV10SHEPOR-SHE`) | 0.05 / 0.95 (293) | 50.0% | 69.3% | 72.8% | 64.1% [64.1%-66.0%] | -- | -- | -- | -- | PASS | +19.3 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 65.0, B 130.0; serve-point win A 62.3%, B 41.6%; Elo A 1263.7, B 1159.2; model uncertainty 0.0095
* Form inputs: days since last match A 371, B 196; matches on record A 4, B 10; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10SHEPOR-SHE  (YES = Mitchell Sheldon)
Model: 69%
Kalshi: 50%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.010, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Niels Peter Van Noord vs Stephen Slocombe -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207725:213723:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stephen Slocombe (`KXITFMATCH-26NOV10VANSLO-SLO`) | 0.28 / 0.75 (3) | 51.5% | 38.1% | 52.1% | 52.1% [51.5%-53.1%] | -- | -- | -- | -- | PASS | -13.4 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Niels Peter Van Noord (`KXITFMATCH-26NOV10VANSLO-VAN`) | 0.57 / 0.87 (4) | 72.0% | 61.9% | 47.9% | 47.9% [46.9%-48.4%] | -- | -- | -- | -- | PASS | -10.1 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 458.0, B 127.0; serve-point win A 61.4%, B 40.9%; Elo A 1202.2, B 1217.9; model uncertainty 0.0077
* Form inputs: days since last match A 252, B 252; matches on record A 13, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Robert Watzka vs Kabeer Kapasi -- M15 Naples FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212905:213862:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kabeer Kapasi (`KXITFMATCH-26NOV10WATKAP-KAP`) | 0.05 / 0.95 (315) | 50.0% | 39.5% | 64.1% | 45.9% [45.9%-45.9%] | -- | -- | -- | -- | PASS | -10.6 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Robert Watzka (`KXITFMATCH-26NOV10WATKAP-WAT`) | 0.05 / 0.95 (293) | 50.0% | 60.6% | 35.9% | 54.1% [54.1%-54.1%] | -- | -- | -- | -- | PASS | +10.6 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 176.0, B 0.0; serve-point win A 60.9%, B 41.1%; Elo A 1239.0, B 1208.5; model uncertainty 0.0
* Form inputs: days since last match A 238, B 756; matches on record A 3, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jaden Weekes vs Eric David Verdes -- M25 Montreal R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210653:211647:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eric David Verdes (`KXITFMATCH-26NOV10WEEVER-VER`) | 0.65 / 0.92 (3) | 78.5% | 28.3% | 72.8% | 37.8% [36.8%-37.8%] | -- | -- | -- | -- | PASS | -50.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Jaden Weekes (`KXITFMATCH-26NOV10WEEVER-WEE`) | 0.20 / 0.76 (3) | 48.0% | 71.7% | 27.2% | 62.2% [62.2%-63.2%] | -- | -- | -- | -- | PASS | +23.7 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 553.0, B 0.0; serve-point win A 62.3%, B 42.1%; Elo A 1299.0, B 1211.2; model uncertainty 0.0049
* Form inputs: days since last match A 469, B 868; matches on record A 34, B 8; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV10WEEVER-WEE  (YES = Jaden Weekes)
Model: 72%
Kalshi: 48%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Brooke Black vs Romina Ccuno -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10BLACCU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brooke Black (`KXITFWMATCH-26NOV10BLACCU-BLA`) | 0.04 / 0.95 (10) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Romina Ccuno (`KXITFWMATCH-26NOV10BLACCU-CCU`) | 0.04 / 0.95 (10) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jana Hossam Salah vs Paula Ormaechea -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202440:266764:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jana Hossam Salah (`KXITFWMATCH-26NOV10HOSORM-HOS`) | 0.04 / 0.95 (10) | 49.5% | 34.7% | 80.2% | 34.0% [24.4%-44.2%] | -- | -- | -- | -- | PASS | -14.8 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Paula Ormaechea (`KXITFWMATCH-26NOV10HOSORM-ORM`) | 0.04 / 0.93 (3) | 48.5% | 65.3% | 19.8% | 66.0% [55.8%-75.6%] | -- | -- | -- | -- | PASS | +16.8 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 378.0, B 761.0; serve-point win A 53.8%, B 43.2%; Elo A 1371.0, B 1577.5; model uncertainty 0.0991
* Form inputs: days since last match A 322, B 441; matches on record A 19, B 657; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10HOSORM-ORM  (YES = Paula Ormaechea)
Model: 65%
Kalshi: 48%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lexington Reed vs Rachel Gailis -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222037:239186:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rachel Gailis (`KXITFWMATCH-26NOV10REEGAI-GAI`) | 0.04 / 0.95 (10) | 49.5% | 75.7% | 61.5% | 69.3% [67.4%-73.0%] | -- | -- | -- | -- | PASS | +26.2 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lexington Reed (`KXITFWMATCH-26NOV10REEGAI-REE`) | 0.04 / 0.95 (10) | 49.5% | 24.3% | 38.5% | 30.6% [27.0%-32.6%] | -- | -- | -- | -- | PASS | -25.2 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 144.0, B 857.0; serve-point win A 52.4%, B 42.4%; Elo A 1321.7, B 1473.4; model uncertainty 0.0281
* Form inputs: days since last match A 343, B 104; matches on record A 98, B 113; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV10REEGAI-GAI  (YES = Rachel Gailis)
Model: 76%
Kalshi: 50%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.019, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Margaret Sohns vs Malwina Rowinska -- W35 Weston FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-10 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-10T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260764:269734:2026-11-10`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Malwina Rowinska (`KXITFWMATCH-26NOV10SOHROW-ROW`) | 0.04 / 0.95 (10) | 49.5% | 37.1% | 30.0% | 41.5% [37.9%-43.6%] | -- | -- | -- | -- | PASS | -12.4 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Margaret Sohns (`KXITFWMATCH-26NOV10SOHROW-SOH`) | 0.04 / 0.95 (15) | 49.5% | 62.9% | 70.0% | 58.5% [56.4%-62.1%] | -- | -- | -- | -- | PASS | +13.4 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 287.0, B 297.0; serve-point win A 51.6%, B 50.9%; Elo A 1238.9, B 1194.7; model uncertainty 0.0287
* Form inputs: days since last match A 217, B 217; matches on record A 9, B 27; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katerina Siniakova / Taylor Townsend vs Ellen Perez / Demi Schuurs -- WTA Finals Women Doubles Group

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-11 01:20Z
* Current expected start: 2026-11-10 23:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-09 22:48Z
* Recommended handicap-by time: 2026-11-10 22:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-11T01:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10SINTOWPERSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ellen Perez / Demi Schuurs (`KXWTADOUBLES-26NOV10SINTOWPERSCH-PERSCH`) | 0.13 / 0.53 (28) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katerina Siniakova / Taylor Townsend (`KXWTADOUBLES-26NOV10SINTOWPERSCH-SINTOW`) | 0.48 / 0.87 (8) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cristina Bucsa / Nicole Melichar-Martinez vs Sara Errani / Jasmine Paolini -- WTA Finals Women Doubles Group

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-11 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_FINALS) · surface ? · scheduled 2026-11-11T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV10BUCMELERRPAO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Bucsa / Nicole Melichar-Martinez (`KXWTADOUBLES-26NOV10BUCMELERRPAO-BUCMEL`) | 0.24 / 0.84 (1) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sara Errani / Jasmine Paolini (`KXWTADOUBLES-26NOV10BUCMELERRPAO-ERRPAO`) | 0.33 / 0.88 (5) | 60.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
