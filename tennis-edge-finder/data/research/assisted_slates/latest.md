# ASSISTED SLATE -- 2026-10-01T17:39Z (`SL-20261001T173934Z-bbf2c1bc`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

177 open matches not seen started, 667 markets. Skipped: {"first_ball_already_observed": 8, "scheduled_start_over_24h_past": 1, "no_match_winner_listed": 1}. Sources: shadow board 2026-10-01T17:35:04.340157+00:00, Model 4 2026-10-01T17:35:46.118220+00:00, Gen-1 ledger 2026-10-01T17:35:00.309201+00:00, external 2026-10-01T16:58:50.030493+00:00, capture 20261001T171316Z.quotes.jsonl.gz.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 44, "HIGH_REVIEW": 43, "NORMAL": 231, "REVIEW": 79, "UNPRICED": 270}; match winners: {"EXTREME": 38, "HIGH_REVIEW": 37, "NORMAL": 138, "REVIEW": 29, "UNPRICED": 112}; quote freshness at build: {"AGING": 247, "STALE": 150}.

## Yuta Shimizu vs Bernard Tomic -- ATP Challenger Jingshan R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T07:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106071:202122:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuta Shimizu (`KXATPCHALLENGERMATCH-26OCT01SHITOM-SHI`) | 0.62 / 0.63 (350) | 62.5% | 41.8% | 37.7% | 37.7% [37.2%-39.1%] | -- | -- | -- | -- | PASS | -24.8 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Bernard Tomic (`KXATPCHALLENGERMATCH-26OCT01SHITOM-TOM`) | 0.38 / 0.39 (1332) | 38.5% | 58.2% | 62.3% | 62.3% [60.9%-62.8%] | -- | -- | -- | -- | WATCH | +23.8 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4903.0, B 5940.0; serve-point win A 61.8%, B 36.6%; Elo A 1590.1, B 1667.2; model uncertainty 0.0095
* Form inputs: days since last match A 17, B 17; matches on record A 541, B 996; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01SHITOM-TOM  (YES = Bernard Tomic)
Model: 62%
Kalshi: 38%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Elias Ymer vs Federico Cina -- ATP Challenger Jingshan R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T07:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:111200:210748:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Cina (`KXATPCHALLENGERMATCH-26OCT01YMECIN-CIN`) | 0.69 / 0.70 (900) | 69.5% | 58.0% | 60.4% | 60.9% [59.4%-62.3%] | -- | -- | -- | -- | PASS | -8.6 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elias Ymer (`KXATPCHALLENGERMATCH-26OCT01YMECIN-YME`) | 0.30 / 0.31 (641) | 30.5% | 42.0% | 39.6% | 39.1% [37.8%-40.6%] | -- | -- | -- | -- | SHADOW_BET | +8.6 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5409.0, B 3635.0; serve-point win A 61.8%, B 36.6%; Elo A 1618.1, B 1702.2; model uncertainty 0.0141
* Form inputs: days since last match A 9, B 5; matches on record A 1064, B 187; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.014, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Lloyd Harris / Cheng-Peng Hsieh vs Nathaniel Lammons / Jackson Withrow -- ATP Challenger Jingshan QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T08:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HARHSILAMWIT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lloyd Harris / Cheng-Peng Hsieh (`KXATPCHALLENGERDOUBLES-26OCT01HARHSILAMWIT-HARHSI`) | 0.23 / 0.27 (26) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nathaniel Lammons / Jackson Withrow (`KXATPCHALLENGERDOUBLES-26OCT01HARHSILAMWIT-LAMWIT`) | 0.67 / 0.77 (501) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Ryan Seggerman / Bart Stevens vs Alex Bolt / Adam Walton -- ATP Challenger Jingshan QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T08:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01SEGSTEBOLWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Bolt / Adam Walton (`KXATPCHALLENGERDOUBLES-26OCT01SEGSTEBOLWAL-BOLWAL`) | 0.19 / 0.29 (14) | 24.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ryan Seggerman / Bart Stevens (`KXATPCHALLENGERDOUBLES-26OCT01SEGSTEBOLWAL-SEGSTE`) | 0.26 / 0.73 (1) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gonzalo Escobar / Niki Kaliyanda Poonacha vs Mitsuki Wei Kang Leong / Stefanos Sakellaridis -- ATP Challenger Jingshan QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T09:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01ESCKALLEOSAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gonzalo Escobar / Niki Kaliyanda Poonacha (`KXATPCHALLENGERDOUBLES-26OCT01ESCKALLEOSAK-ESCKAL`) | 0.72 / 0.82 (500) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mitsuki Wei Kang Leong / Stefanos Sakellaridis (`KXATPCHALLENGERDOUBLES-26OCT01ESCKALLEOSAK-LEOSAK`) | 0.18 / 0.24 (24) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Arthur Reymond / Luca Sanchez vs Stefan Latinovic / Mili Poljicak -- ATP Challenger Porto 2 QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01REYSANLATPOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Latinovic / Mili Poljicak (`KXATPCHALLENGERDOUBLES-26OCT01REYSANLATPOL-LATPOL`) | 0.70 / 0.85 (57) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arthur Reymond / Luca Sanchez (`KXATPCHALLENGERDOUBLES-26OCT01REYSANLATPOL-REYSAN`) | 0.18 / 0.26 (167) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Mateus Alves vs Gonzalo Villanueva -- ATP Challenger Curitiba R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106380:127123:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateus Alves (`KXATPCHALLENGERMATCH-26OCT01ALVVIL-ALV`) | 0.58 / 0.59 (2486) | 58.5% | -- | 56.1% | 53.5% [50.5%-55.6%] | -- | 58.4% | 58.4% | MODEL_LONE_OUTLIER | PASS | -5.0 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Gonzalo Villanueva (`KXATPCHALLENGERMATCH-26OCT01ALVVIL-VIL`) | 0.42 / 0.43 (6104) | 42.5% | -- | 43.9% | 46.5% [44.4%-49.5%] | -- | 41.5% | 41.5% | MARKETS_AGREE | WATCH | +4.0 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4869.0, B 5724.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0253
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

## Clement Chidekh vs Ugo Blanchet -- ATP Challenger Mouilleron-Le-Captif R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200259:206889:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ugo Blanchet (`KXATPCHALLENGERMATCH-26OCT01CHIBLA-BLA`) | 0.01 / 0.02 (31874) | 1.5% | -- | 31.6% | 34.3% [31.6%-41.0%] | 38.4% | -- | 38.4% | KALSHI_LONE_OUTLIER | WATCH | +32.8 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Clement Chidekh (`KXATPCHALLENGERMATCH-26OCT01CHIBLA-CHI`) | 0.98 / 0.99 (88249) | 98.5% | -- | 68.4% | 65.7% [59.0%-68.4%] | 61.6% | -- | 61.6% | KALSHI_LONE_OUTLIER | PASS | -32.8 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 5365.0, B 4988.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0471
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01CHIBLA-BLA  (YES = Ugo Blanchet)
Model: 34%
Kalshi: 2%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_MODEL
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.018, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

## Mariano Kestelboim / Marcelo Zormann vs Brandon Perez / Paulo Andre Saraiva Dos Santos -- ATP Challenger Curitiba QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01KESZORPERSAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariano Kestelboim / Marcelo Zormann (`KXATPCHALLENGERDOUBLES-26OCT01KESZORPERSAR-KESZOR`) | 0.63 / 0.72 (500) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Brandon Perez / Paulo Andre Saraiva Dos Santos (`KXATPCHALLENGERDOUBLES-26OCT01KESZORPERSAR-PERSAR`) | 0.29 / 0.37 (14) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Bryce Nakashima vs Keegan Smith -- ATP Challenger Columbus R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202333:210416:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bryce Nakashima (`KXATPCHALLENGERMATCH-26OCT01NAKSMI-NAK`) | 0.87 / 0.88 (45320) | 87.5% | -- | 15.6% | 14.4% [12.8%-16.3%] | 42.8% | 43.3% | 43.1% | MODEL_LONE_OUTLIER | PASS | -73.0 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Keegan Smith (`KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI`) | 0.12 / 0.13 (110172) | 12.5% | -- | 84.4% | 85.5% [83.7%-87.2%] | 57.2% | 56.5% | 56.9% | MODEL_LONE_OUTLIER | PASS | +73.0 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 451.0, B 5491.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0174
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI  (YES = Keegan Smith)
Model: 86%
Kalshi: 12%
Gap: +73 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.016, surface_dev_loose -0.002, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Samuel Heredia / Miguel Tobon vs Bruno (2002) Oliveira / Natan Rodrigues -- ATP Challenger Curitiba QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T18:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HERTOBOLIROD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samuel Heredia / Miguel Tobon (`KXATPCHALLENGERDOUBLES-26OCT01HERTOBOLIROD-HERTOB`) | 0.33 / 0.37 (41) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bruno (2002) Oliveira / Natan Rodrigues (`KXATPCHALLENGERDOUBLES-26OCT01HERTOBOLIROD-OLIROD`) | 0.58 / 0.66 (4) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Joao Eduardo Schiessl vs Luis Guto Miguel -- ATP Challenger Curitiba R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T18:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210214:213036:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Guto Miguel (`KXATPCHALLENGERMATCH-26OCT01SCHMIG-MIG`) | 0.78 / 0.79 (349) | 78.5% | -- | 64.0% | 51.5% [42.9%-56.6%] | 76.9% | 78.4% | 76.9% | MODEL_LONE_OUTLIER | PASS | -27.0 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Joao Eduardo Schiessl (`KXATPCHALLENGERMATCH-26OCT01SCHMIG-SCH`) | 0.21 / 0.22 (24689) | 21.5% | -- | 36.0% | 48.5% [43.4%-57.1%] | 23.1% | 20.5% | 21.8% | MODEL_LONE_OUTLIER | WATCH | +27.0 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3018.0, B 1185.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0688
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01SCHMIG-SCH  (YES = Joao Eduardo Schiessl)
Model: 48%
Kalshi: 22%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Aidan Mayo vs Colton Smith -- ATP Challenger Columbus R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T19:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208854:212256:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aidan Mayo (`KXATPCHALLENGERMATCH-26OCT01MAYSMI-MAY`) | 0.35 / 0.36 (7048) | 35.5% | -- | 46.9% | 40.9% [38.0%-43.9%] | 37.5% | 36.1% | 36.8% | MARKETS_AGREE | WATCH | +5.4 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Colton Smith (`KXATPCHALLENGERMATCH-26OCT01MAYSMI-SMI`) | 0.64 / 0.66 (4173) | 65.0% | -- | 53.0% | 59.1% [56.1%-62.0%] | 62.5% | 63.9% | 63.2% | MARKETS_AGREE | PASS | -5.9 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3962.0, B 3806.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0297
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Abdullah Shelbayh vs Daniil Ostapenkov -- ATP Challenger Columbus R16

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-01T19:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01SHEOST:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniil Ostapenkov (`KXATPCHALLENGERMATCH-26OCT01SHEOST-OST`) | 0.07 / 0.08 (8435) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Abdullah Shelbayh (`KXATPCHALLENGERMATCH-26OCT01SHEOST-SHE`) | 0.92 / 0.93 (14490) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Guido Ivan Justo vs Pedro Sakamoto -- ATP Challenger Curitiba R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T19:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106203:207815:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guido Ivan Justo (`KXATPCHALLENGERMATCH-26OCT01JUSSAK-JUS`) | 0.68 / 0.69 (2022) | 68.5% | -- | 79.7% | 75.8% [69.8%-78.6%] | 68.8% | 69.7% | 69.2% | MARKETS_AGREE | WATCH | +7.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Pedro Sakamoto (`KXATPCHALLENGERMATCH-26OCT01JUSSAK-SAK`) | 0.30 / 0.31 (6308) | 30.5% | -- | 20.3% | 24.2% [21.4%-30.2%] | 31.2% | 30.8% | 31.0% | MARKETS_AGREE | PASS | -6.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4964.0, B 4530.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0439
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.008, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Franco Roncadelli / Gonzalo Villanueva vs Boris Arias / Ignacio Carou -- ATP Challenger Curitiba QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T19:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01RONVILARICAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boris Arias / Ignacio Carou (`KXATPCHALLENGERDOUBLES-26OCT01RONVILARICAR-ARICAR`) | 0.51 / 0.58 (51) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Franco Roncadelli / Gonzalo Villanueva (`KXATPCHALLENGERDOUBLES-26OCT01RONVILARICAR-RONVIL`) | 0.41 / 0.47 (45) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Jonah Braswell vs Jordan Lee -- M15 Fayetteville AR R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:211738:214265:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonah Braswell (`KXITFMATCH-26OCT01BRALEE-BRA`) | 0.54 / 0.57 (90) | 55.5% | 42.9% | 31.4% | 41.7% [38.6%-42.8%] | 21.9% | -- | 21.9% | MODEL_LONE_OUTLIER | PASS | -13.8 pp | REVIEW | STALE | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Jordan Lee (`KXITFMATCH-26OCT01BRALEE-LEE`) | 0.44 / 0.46 (189) | 45.0% | 57.1% | 68.6% | 58.3% [57.2%-61.4%] | 78.1% | -- | 78.1% | MODEL_LONE_OUTLIER | PASS | +13.3 pp | REVIEW | STALE | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 298.0, B 252.0; serve-point win A 61.9%, B 36.7%; Elo A 1291.2, B 1341.1; model uncertainty 0.021
* Form inputs: days since last match A 318, B 36; matches on record A 17, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Harold Mayot vs Tristan Schoolkate -- ATP Challenger Mouilleron-Le-Captif R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208004:209262:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harold Mayot (`KXATPCHALLENGERMATCH-26OCT01MAYSCH-MAY`) | 0.58 / 0.59 (7449) | 58.5% | -- | 60.8% | 59.3% [58.4%-60.3%] | -- | 58.8% | 58.8% | MARKETS_AGREE | PASS | +0.8 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Tristan Schoolkate (`KXATPCHALLENGERMATCH-26OCT01MAYSCH-SCH`) | 0.41 / 0.42 (15117) | 41.5% | -- | 39.2% | 40.7% [39.7%-41.6%] | -- | 41.4% | 41.4% | MARKETS_AGREE | PASS | -0.8 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5745.0, B 6276.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0096
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.009, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Max Sheldon vs Olaf Pieczkowski -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210142:210376:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Olaf Pieczkowski (`KXITFMATCH-26OCT01SHEPIE-PIE`) | 0.82 / 0.83 (5497) | 82.5% | 76.5% | 63.4% | 74.9% [70.6%-79.8%] | 63.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Sheldon (`KXITFMATCH-26OCT01SHEPIE-SHE`) | 0.17 / 0.18 (13280) | 17.5% | 23.5% | 36.6% | 25.1% [20.2%-29.4%] | 36.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 264.0, B 2433.0; serve-point win A 59.7%, B 34.5%; Elo A 1229.6, B 1435.1; model uncertainty 0.0457
* Form inputs: days since last match A 486, B 59; matches on record A 13, B 234; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.028, surface_pool_high +0.035, surface_dev_loose -0.000, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alvin Nicholas Tudorica vs Neo Niedner -- M15 Fayetteville AR R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210102:212202:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Neo Niedner (`KXITFMATCH-26OCT01TUDNIE-NIE`) | 0.20 / 0.21 (16145) | 20.5% | 20.3% | 64.0% | 27.1% [23.2%-31.7%] | 37.8% | -- | 37.8% | MODEL_LONE_OUTLIER | PASS | +6.6 pp | NORMAL | AGING | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Alvin Nicholas Tudorica (`KXITFMATCH-26OCT01TUDNIE-TUD`) | 0.79 / 0.80 (14416) | 79.5% | 79.7% | 36.0% | 72.9% [68.3%-76.8%] | 62.2% | -- | 62.2% | MODEL_LONE_OUTLIER | PASS | -6.6 pp | NORMAL | AGING | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1789.0, B 335.0; serve-point win A 65.9%, B 40.7%; Elo A 1409.1, B 1171.4; model uncertainty 0.0425
* Form inputs: days since last match A 206, B 122; matches on record A 106, B 29; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.017, surface_dev_loose -0.004, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefan Kozlov vs Mitchell Krueger -- ATP Challenger Columbus R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T20:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106283:111578:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Kozlov (`KXATPCHALLENGERMATCH-26OCT01KOZKRU-KOZ`) | 0.56 / 0.57 (6667) | 56.5% | -- | 51.0% | 50.5% [47.9%-51.5%] | 56.3% | 57.0% | 56.7% | MODEL_LONE_OUTLIER | PASS | -6.0 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Mitchell Krueger (`KXATPCHALLENGERMATCH-26OCT01KOZKRU-KRU`) | 0.43 / 0.44 (2909) | 43.5% | -- | 49.0% | 49.5% [48.4%-52.1%] | 43.7% | 42.8% | 43.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.0 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4126.0, B 5011.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0181
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Daniel Milavsky / Braden Shick vs Matthew Forbes / Denis Petak -- ATP Challenger Columbus QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T20:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01MILSHIFORPET:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Forbes / Denis Petak (`KXATPCHALLENGERDOUBLES-26OCT01MILSHIFORPET-FORPET`) | 0.32 / 0.39 (66) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Milavsky / Braden Shick (`KXATPCHALLENGERDOUBLES-26OCT01MILSHIFORPET-MILSHI`) | 0.60 / 0.68 (25) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Pedro Boscardin Dias vs Genaro Alberto Olivieri -- ATP Challenger Curitiba R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T20:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:144821:208046:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Boscardin Dias (`KXATPCHALLENGERMATCH-26OCT01BOSOLI-BOS`) | 0.57 / 0.58 (9902) | 57.5% | -- | 47.9% | 47.9% [47.9%-48.4%] | 56.3% | 57.0% | 56.7% | MODEL_LONE_OUTLIER | PASS | -9.6 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Genaro Alberto Olivieri (`KXATPCHALLENGERMATCH-26OCT01BOSOLI-OLI`) | 0.42 / 0.43 (359) | 42.5% | -- | 52.1% | 52.1% [51.6%-52.1%] | 43.7% | 43.2% | 43.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +9.6 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4852.0, B 5465.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0026
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Coppez / Tran vs Leonard / Martynov -- W35 Reims SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T20:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01COPTRALEOMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coppez / Tran (`KXITFWDOUBLES-26OCT01COPTRALEOMAR-COPTRA`) | 0.73 / 0.78 (7) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leonard / Martynov (`KXITFWDOUBLES-26OCT01COPTRALEOMAR-LEOMAR`) | 0.20 / 0.23 (796) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Oliver Bonding vs Marko Mesarovic -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:211670:212839:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oliver Bonding (`KXITFMATCH-26OCT01BONMES-BON`) | 0.81 / 0.87 (3) | 84.0% | 62.0% | 54.6% | 67.3% [64.0%-69.7%] | 81.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.7 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marko Mesarovic (`KXITFMATCH-26OCT01BONMES-MES`) | 0.12 / 0.16 (87) | 14.0% | 38.0% | 45.4% | 32.7% [30.3%-36.0%] | 18.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +18.7 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1207.0, B 745.0; serve-point win A 63.8%, B 38.6%; Elo A 1440.2, B 1267.9; model uncertainty 0.0282
* Form inputs: days since last match A 38, B 122; matches on record A 42, B 24; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01BONMES-MES  (YES = Marko Mesarovic)
Model: 33%
Kalshi: 14%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Micah Braswell vs Hugo Coquelin -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209334:213042:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Micah Braswell (`KXITFMATCH-26OCT01BRACOQ-BRA`) | 0.40 / 0.46 (5) | 43.0% | 79.1% | 74.5% | 78.1% [76.8%-79.4%] | 57.0% | -- | 57.0% | MODEL_LONE_OUTLIER | PASS | +35.1 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Hugo Coquelin (`KXITFMATCH-26OCT01BRACOQ-COQ`) | 0.49 / 0.57 (11) | 53.0% | 20.9% | 25.5% | 21.9% [20.6%-23.2%] | 43.0% | -- | 43.0% | MODEL_LONE_OUTLIER | PASS | -31.1 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 2173.0, B 446.0; serve-point win A 65.8%, B 40.6%; Elo A 1508.7, B 1277.2; model uncertainty 0.0126
* Form inputs: days since last match A 241, B 122; matches on record A 99, B 17; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01BRACOQ-BRA  (YES = Micah Braswell)
Model: 78%
Kalshi: 43%
Gap: +35 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.008, surface_dev_loose +0.008, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dragos Nicolae Cazacu vs Alexander Rozin -- M15 Fayetteville AR R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01CAZROZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dragos Nicolae Cazacu (`KXITFMATCH-26OCT01CAZROZ-CAZ`) | 0.61 / 0.65 (3519) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Rozin (`KXITFMATCH-26OCT01CAZROZ-ROZ`) | 0.36 / 0.37 (12) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikola Djosic vs Thanaphat Boosarawongse -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:212149:213051:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thanaphat Boosarawongse (`KXITFMATCH-26OCT01DJOBOO-BOO`) | 0.65 / 0.66 (6177) | 65.5% | 39.7% | 29.9% | 38.6% [35.6%-40.2%] | 63.0% | -- | 63.0% | MODEL_LONE_OUTLIER | PASS | -26.9 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Nikola Djosic (`KXITFMATCH-26OCT01DJOBOO-DJO`) | 0.34 / 0.35 (1344) | 34.5% | 60.3% | 70.0% | 61.4% [59.8%-64.4%] | 37.0% | -- | 37.0% | MODEL_LONE_OUTLIER | PASS | +26.9 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1313.0, B 249.0; serve-point win A 63.6%, B 38.4%; Elo A 1289.1, B 1216.5; model uncertainty 0.023
* Form inputs: days since last match A 129, B 269; matches on record A 39, B 13; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01DJOBOO-DJO  (YES = Nikola Djosic)
Model: 61%
Kalshi: 34%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Theo Papamalamis vs Tito Chavez -- M15 Fayetteville AR R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210494:214377:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tito Chavez (`KXITFMATCH-26OCT01PAPCHA-CHA`) | 0.23 / 0.27 (5) | 25.0% | 34.7% | 26.2% | 32.1% [30.2%-34.7%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Theo Papamalamis (`KXITFMATCH-26OCT01PAPCHA-PAP`) | 0.72 / 0.76 (26) | 74.0% | 65.3% | 73.8% | 67.9% [65.3%-69.8%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1643.0, B 499.0; serve-point win A 64.1%, B 39.0%; Elo A 1427.8, B 1317.9; model uncertainty 0.0226
* Form inputs: days since last match A 122, B 129; matches on record A 97, B 10; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose +0.019, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Johan Alexander Rodriguez vs Alejandro Melero Kretzer -- M15 Fayetteville AR R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01RODMEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alejandro Melero Kretzer (`KXITFMATCH-26OCT01RODMEL-MEL`) | 0.17 / 0.24 (455) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Johan Alexander Rodriguez (`KXITFMATCH-26OCT01RODMEL-ROD`) | 0.76 / 0.80 (1) | 78.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Damir Zhalgasbay vs Felix Corwin -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200228:212846:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Corwin (`KXITFMATCH-26OCT01ZHACOR-COR`) | 0.31 / 0.32 (3235) | 31.5% | 80.5% | 67.7% | 79.2% [77.6%-80.0%] | 50.9% | -- | 50.9% | MODEL_LONE_OUTLIER | PASS | +47.7 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Damir Zhalgasbay (`KXITFMATCH-26OCT01ZHACOR-ZHA`) | 0.68 / 0.69 (2040) | 68.5% | 19.5% | 32.3% | 20.8% [20.0%-22.4%] | 49.0% | -- | 49.0% | MODEL_LONE_OUTLIER | PASS | -47.7 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 222.0, B 3231.0; serve-point win A 59.2%, B 34.0%; Elo A 1156.7, B 1403.3; model uncertainty 0.0117
* Form inputs: days since last match A 157, B 171; matches on record A 6, B 382; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01ZHACOR-COR  (YES = Felix Corwin)
Model: 79%
Kalshi: 32%
Gap: +48 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pilar Da Silva vs Marina Bulbarella -- W15 Trelew R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01DASBUL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marina Bulbarella (`KXITFWMATCH-26OCT01DASBUL-BUL`) | 0.43 / 0.44 (10197) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pilar Da Silva (`KXITFWMATCH-26OCT01DASBUL-DAS`) | 0.56 / 0.57 (6624) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## CAIRA DELFINA VEGA GUDINO vs Maria Florencia Urrutia -- W15 Trelew R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220447:270267:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Florencia Urrutia (`KXITFWMATCH-26OCT01VEGURR-URR`) | 0.99 / -- (0) | -- | 81.5% | 81.2% | 81.9% [81.2%-82.6%] | -- | -- | -- | -- | PASS | -- | UNPRICED | AGING | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| CAIRA DELFINA VEGA GUDINO (`KXITFWMATCH-26OCT01VEGURR-VEG`) | -- / 0.01 (800) | -- | 18.5% | 18.8% | 18.1% [17.4%-18.8%] | -- | -- | -- | -- | PASS | -- | UNPRICED | AGING | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 120.0, B 2454.0; serve-point win A 52.3%, B 40.9%; Elo A 1228.4, B 1486.5; model uncertainty 0.007
* Form inputs: days since last match A 255, B 157; matches on record A 2, B 106; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.007, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tom Hands / Matthew Summers vs Karl Poling / Joshua Sheehy -- ATP Challenger Mouilleron-Le-Captif QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T21:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HANSUMPOLSHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tom Hands / Matthew Summers (`KXATPCHALLENGERDOUBLES-26OCT01HANSUMPOLSHE-HANSUM`) | 0.49 / 0.54 (619) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karl Poling / Joshua Sheehy (`KXATPCHALLENGERDOUBLES-26OCT01HANSUMPOLSHE-POLSHE`) | 0.46 / 0.50 (53) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Brandon Carpico / Nikita Samuel Filin vs Luis David Martinez / James Kent Trotter -- ATP Challenger Columbus QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T21:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01CARFILMARTRO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brandon Carpico / Nikita Samuel Filin (`KXATPCHALLENGERDOUBLES-26OCT01CARFILMARTRO-CARFIL`) | 0.62 / 0.63 (358) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luis David Martinez / James Kent Trotter (`KXATPCHALLENGERDOUBLES-26OCT01CARFILMARTRO-MARTRO`) | 0.37 / 0.38 (89) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## James Mackinlay / Oliver Okonkwo vs Alex Rybakov / Keegan Smith -- ATP Challenger Columbus QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T21:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01MACOKORYBSMI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Mackinlay / Oliver Okonkwo (`KXATPCHALLENGERDOUBLES-26OCT01MACOKORYBSMI-MACOKO`) | 0.42 / 0.46 (43) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alex Rybakov / Keegan Smith (`KXATPCHALLENGERDOUBLES-26OCT01MACOKORYBSMI-RYBSMI`) | 0.50 / 0.56 (55) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Ashley Lahey vs Raquel Caballero Chica -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216076:231636:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raquel Caballero Chica (`KXITFWMATCH-26OCT01LAHCAB-CAB`) | 0.08 / 0.09 (290) | 8.5% | 8.4% | 25.0% | 9.3% [8.8%-9.8%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ashley Lahey (`KXITFWMATCH-26OCT01LAHCAB-LAH`) | 0.91 / 0.92 (6600) | 91.5% | 91.6% | 75.0% | 90.7% [90.2%-91.2%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1883.0, B 74.0; serve-point win A 62.2%, B 48.2%; Elo A 1627.6, B 1213.5; model uncertainty 0.0048
* Form inputs: days since last match A 381, B 500; matches on record A 239, B 25; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eszter Meri vs Astra Sharma -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:206292:221150:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eszter Meri (`KXITFWMATCH-26OCT01MERSHA-MER`) | 0.21 / 0.22 (4571) | 21.5% | 31.5% | 48.9% | 35.4% [31.6%-39.0%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.9 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Astra Sharma (`KXITFWMATCH-26OCT01MERSHA-SHA`) | 0.78 / 0.79 (4253) | 78.5% | 68.5% | 51.1% | 64.6% [61.1%-68.4%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.9 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 402.0, B 2800.0; serve-point win A 55.2%, B 41.2%; Elo A 1563.2, B 1698.2; model uncertainty 0.0368
* Form inputs: days since last match A 465, B 15; matches on record A 258, B 423; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rose Marie Nijkamp vs Francesca Mattioli -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:260150:260225:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Mattioli (`KXITFWMATCH-26OCT01NIJMAT-MAT`) | 0.47 / 0.49 (9) | 48.0% | 49.1% | 39.4% | 46.8% [44.1%-48.9%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rose Marie Nijkamp (`KXITFWMATCH-26OCT01NIJMAT-NIJ`) | 0.48 / 0.53 (401) | 50.5% | 50.9% | 60.6% | 53.2% [51.1%-55.9%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1080.0, B 492.0; serve-point win A 57.1%, B 43.1%; Elo A 1482.4, B 1476.0; model uncertainty 0.0241
* Form inputs: days since last match A 164, B 423; matches on record A 54, B 28; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Podhajecka / Sharabura vs Pearce / Yamakita -- W15 Nashville TN QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T21:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01PODSHAPEAYAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pearce / Yamakita (`KXITFWDOUBLES-26OCT01PODSHAPEAYAM-PEAYAM`) | 0.63 / 0.70 (665) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Podhajecka / Sharabura (`KXITFWDOUBLES-26OCT01PODSHAPEAYAM-PODSHA`) | 0.30 / 0.37 (1) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ganchev / Maes vs Ifi / Stanke -- M25 Zaragoza QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01GANMAEIFISTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ganchev / Maes (`KXITFDOUBLES-26OCT01GANMAEIFISTA-GANMAE`) | 0.05 / 0.06 (591) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ifi / Stanke (`KXITFDOUBLES-26OCT01GANMAEIFISTA-IFISTA`) | 0.92 / 0.97 (153) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Horwood / Vrba vs Roddick / Tokac -- M15 Fayetteville AR QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HORVRBRODTOK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Horwood / Vrba (`KXITFDOUBLES-26OCT01HORVRBRODTOK-HORVRB`) | 0.44 / 0.54 (47) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Roddick / Tokac (`KXITFDOUBLES-26OCT01HORVRBRODTOK-RODTOK`) | 0.41 / 0.48 (48) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Pawlak / Pujol Navarro vs Lopez Martos / Palomar -- M25 Zaragoza QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01PAWPUJLOPPAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lopez Martos / Palomar (`KXITFDOUBLES-26OCT01PAWPUJLOPPAL-LOPPAL`) | 0.58 / 0.62 (67) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pawlak / Pujol Navarro (`KXITFDOUBLES-26OCT01PAWPUJLOPPAL-PAWPUJ`) | 0.35 / 0.42 (1) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexander Ritschard vs samuel arauzo martinez -- M25 Zaragoza R16

ITF (ITF) · Clay · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106310:213124:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| samuel arauzo martinez (`KXITFMATCH-26OCT01RITARA-ARA`) | -- / 0.01 (4381) | -- | 4.6% | 16.8% | 4.6% [3.9%-5.4%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | F / POOR | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Ritschard (`KXITFMATCH-26OCT01RITARA-RIT`) | 0.99 / -- (0) | -- | 95.4% | 83.2% | 95.4% [94.6%-96.1%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | F / POOR | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A 3172.0, B 0.0; serve-point win A 66.5%, B 46.7%; Elo A 1773.1, B 1244.9; model uncertainty 0.0074
* Form inputs: days since last match A 24, B 787; matches on record A 681, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.008, surface_dev_loose -0.002, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Charlie Robertson vs Hoyoung Roh -- M15 Fayetteville AR R16

ITF (ITF) · Hard · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:212115:212127:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charlie Robertson (`KXITFMATCH-26OCT01ROBROH-ROB`) | 0.49 / 0.51 (8) | 50.0% | 52.7% | 56.8% | 54.7% [52.1%-56.8%] | 50.9% | -- | 50.9% | MODEL_LONE_OUTLIER | WATCH | +4.7 pp | NORMAL | AGING | C / LIMITED | ALL_AGREE | VERIFIED |
| Hoyoung Roh (`KXITFMATCH-26OCT01ROBROH-ROH`) | 0.48 / 0.51 (1) | 49.5% | 47.3% | 43.2% | 45.3% [43.2%-47.9%] | 49.0% | -- | 49.0% | MODEL_LONE_OUTLIER | PASS | -4.2 pp | NORMAL | AGING | C / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1222.0, B 1129.0; serve-point win A 62.9%, B 37.7%; Elo A 1348.8, B 1325.4; model uncertainty 0.0236
* Form inputs: days since last match A 178, B 122; matches on record A 38, B 36; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aryan Shah vs Evan Bynoe -- M15 Fayetteville AR R16

ITF (ITF) · Hard · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208466:211325:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Evan Bynoe (`KXITFMATCH-26OCT01SHABYN-BYN`) | 0.26 / 0.29 (311) | 27.5% | 23.5% | 24.6% | 23.8% [22.1%-26.3%] | 26.4% | -- | 26.4% | MODEL_LONE_OUTLIER | PASS | -3.7 pp | NORMAL | AGING | B / LIMITED | ALL_AGREE | VERIFIED |
| Aryan Shah (`KXITFMATCH-26OCT01SHABYN-SHA`) | 0.71 / 0.74 (1) | 72.5% | 76.5% | 75.4% | 76.2% [73.7%-77.9%] | 73.6% | -- | 73.6% | MODEL_LONE_OUTLIER | WATCH | +3.7 pp | NORMAL | AGING | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2442.0, B 1889.0; serve-point win A 65.5%, B 40.3%; Elo A 1455.1, B 1243.8; model uncertainty 0.0206
* Form inputs: days since last match A 68, B 143; matches on record A 130, B 102; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.004, surface_dev_loose -0.008, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juliana Giaccio vs Mathilde Lollia -- W35 Baza R16

ITF (ITF) · Hard · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221443:269835:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juliana Giaccio (`KXITFWMATCH-26OCT01GIALOL-GIA`) | 0.47 / 0.48 (1820) | 47.5% | 29.8% | 26.6% | 26.6% [22.8%-31.1%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.9 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mathilde Lollia (`KXITFWMATCH-26OCT01GIALOL-LOL`) | 0.52 / 0.53 (1565) | 52.5% | 70.2% | 73.4% | 73.4% [68.8%-77.2%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.9 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 776.0, B 2163.0; serve-point win A 53.7%, B 42.3%; Elo A 1236.6, B 1409.2; model uncertainty 0.0419
* Form inputs: days since last match A 192, B 171; matches on record A 22, B 173; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01GIALOL-LOL  (YES = Mathilde Lollia)
Model: 73%
Kalshi: 52%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.034, surface_pool_high +0.045, surface_dev_loose -0.008, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Friedman / Sohns vs Bartel / Justine Hejtmanek -- W15 Nashville TN QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T22:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01FRISOHBARJUS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bartel / Justine Hejtmanek (`KXITFWDOUBLES-26OCT01FRISOHBARJUS-BARJUS`) | 0.46 / 0.63 (1246) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Friedman / Sohns (`KXITFWDOUBLES-26OCT01FRISOHBARJUS-FRISOH`) | 0.37 / 0.54 (1172) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Luciana Moyano vs Sofia Meabe -- W15 Trelew R16

ITF (ITF) · Hard · scheduled 2026-10-01T22:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:237454:266446:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Meabe (`KXITFWMATCH-26OCT01MOYMEA-MEA`) | 0.28 / 0.31 (3) | 29.5% | 40.2% | 21.8% | 37.3% [34.3%-40.4%] | 28.9% | -- | 28.9% | KALSHI_LONE_OUTLIER | PASS | +7.8 pp | NORMAL | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Luciana Moyano (`KXITFWMATCH-26OCT01MOYMEA-MOY`) | 0.70 / 0.73 (38) | 71.5% | 59.8% | 78.2% | 62.7% [59.6%-65.7%] | 71.1% | -- | 71.1% | MODEL_LONE_OUTLIER | PASS | -8.8 pp | NORMAL | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2452.0, B 235.0; serve-point win A 56.6%, B 45.2%; Elo A 1405.3, B 1336.4; model uncertainty 0.0305
* Form inputs: days since last match A 157, B 255; matches on record A 106, B 18; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.031, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emily Zornada vs Ana Victoria Gobbi Monllau -- W15 Trelew R16

ITF (ITF) · Hard · scheduled 2026-10-01T22:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211600:270329:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ana Victoria Gobbi Monllau (`KXITFWMATCH-26OCT01ZORGOB-GOB`) | 0.59 / 0.63 (2) | 61.0% | 42.5% | 32.4% | 42.0% [41.0%-42.6%] | 52.9% | -- | 52.9% | MODEL_LONE_OUTLIER | PASS | -19.0 pp | HIGH_REVIEW | AGING | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Emily Zornada (`KXITFWMATCH-26OCT01ZORGOB-ZOR`) | 0.36 / 0.41 (32) | 38.5% | 57.5% | 67.6% | 58.0% [57.4%-59.0%] | 47.1% | -- | 47.1% | MODEL_LONE_OUTLIER | PASS | +19.5 pp | HIGH_REVIEW | AGING | F / POOR | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 106.0, B 761.0; serve-point win A 56.4%, B 45.0%; Elo A 1299.7, B 1247.0; model uncertainty 0.008
* Form inputs: days since last match A 185, B 192; matches on record A 2, B 108; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01ZORGOB-ZOR  (YES = Emily Zornada)
Model: 58%
Kalshi: 38%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Boland / Smillie vs Lestir / Milosavljevic -- M15 Fayetteville AR QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BOLSMILESMIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boland / Smillie (`KXITFDOUBLES-26OCT01BOLSMILESMIL-BOLSMI`) | 0.04 / 0.53 (554) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lestir / Milosavljevic (`KXITFDOUBLES-26OCT01BOLSMILESMIL-LESMIL`) | 0.44 / 0.53 (554) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Tatjana Maria vs Lea Ma -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-01T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:213583:221220:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tatjana Maria (`KXITFWMATCH-26OCT01MARMAX-MAR`) | 0.84 / 0.85 (349) | 84.5% | 54.0% | 28.5% | 42.3% [33.5%-65.7%] | 82.2% | -- | 82.2% | KALSHI_LONE_OUTLIER | PASS | -42.2 pp | EXTREME (DATA_WARNING) | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Lea Ma (`KXITFWMATCH-26OCT01MARMAX-MAX`) | 0.15 / 0.16 (1634) | 15.5% | 46.0% | 71.5% | 57.7% [34.3%-66.5%] | 17.8% | -- | 17.8% | KALSHI_LONE_OUTLIER | WATCH | +42.2 pp | EXTREME (DATA_WARNING) | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4444.0, B 2727.0; serve-point win A 56.1%, B 44.7%; Elo A 1749.9, B 1608.9; model uncertainty 0.161
* Form inputs: days since last match A 17, B 19; matches on record A 1257, B 167; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01MARMAX-MAX  (YES = Lea Ma)
Model: 58%
Kalshi: 16%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: A (LIMITED)
Reasons: SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.041, surface_pool_high -0.045, surface_dev_loose -0.015, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Whitney Osuigwe vs Ella McDonald -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-01T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215992:259591:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ella McDonald (`KXITFWMATCH-26OCT01OSUMCD-MCD`) | 0.52 / 0.56 (1079) | 54.0% | 44.2% | 56.9% | 47.9% [39.9%-52.7%] | 46.2% | -- | 46.2% | MODEL_LONE_OUTLIER | PASS | -6.1 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_MODEL | VERIFIED |
| Whitney Osuigwe (`KXITFWMATCH-26OCT01OSUMCD-OSU`) | 0.45 / 0.48 (125) | 46.5% | 55.8% | 43.1% | 52.1% [47.3%-60.1%] | 53.8% | -- | 53.8% | MODEL_LONE_OUTLIER | WATCH | +5.6 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 3327.0, B 1341.0; serve-point win A 56.2%, B 44.9%; Elo A 1644.5, B 1577.9; model uncertainty 0.0637
* Form inputs: days since last match A 18, B 100; matches on record A 411, B 146; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.021, surface_dev_loose -0.021, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Malaika Rapolu vs Akasha Urhobo -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-01T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222837:259857:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Malaika Rapolu (`KXITFWMATCH-26OCT01RAPURH-RAP`) | 0.53 / 0.55 (5632) | 54.0% | 40.9% | 43.1% | 45.2% [40.0%-48.4%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Akasha Urhobo (`KXITFWMATCH-26OCT01RAPURH-URH`) | 0.45 / 0.46 (58) | 45.5% | 59.1% | 56.9% | 54.8% [51.6%-60.0%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +9.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1761.0, B 3335.0; serve-point win A 54.8%, B 43.5%; Elo A 1612.4, B 1631.7; model uncertainty 0.0421
* Form inputs: days since last match A 14, B 38; matches on record A 133, B 177; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.042, surface_pool_high +0.032, surface_dev_loose +0.005, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Azar / Cairo vs Klimas / Mikovic -- M15 Ann Arbor MI QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01AZACAIKLIMIK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Azar / Cairo (`KXITFDOUBLES-26OCT01AZACAIKLIMIK-AZACAI`) | 0.21 / 0.50 (1) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Klimas / Mikovic (`KXITFDOUBLES-26OCT01AZACAIKLIMIK-KLIMIK`) | 0.12 / 0.54 (54) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fradkin / Kuhar vs Albieri / Heng -- M15 Ann Arbor MI QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01FRAKUHALBHEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Albieri / Heng (`KXITFDOUBLES-26OCT01FRAKUHALBHEN-ALBHEN`) | 0.23 / 0.29 (57) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fradkin / Kuhar (`KXITFDOUBLES-26OCT01FRAKUHALBHEN-FRAKUH`) | 0.69 / 0.75 (73) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sheldon / Swenson vs Matta / Peck -- M15 Ann Arbor MI QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01SHESWEMATPEC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matta / Peck (`KXITFDOUBLES-26OCT01SHESWEMATPEC-MATPEC`) | 0.31 / 0.34 (38) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sheldon / Swenson (`KXITFDOUBLES-26OCT01SHESWEMATPEC-SHESWE`) | 0.17 / 0.68 (1) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Carrocera / Maria Maruca vs Ayala / Fiorella Britez Risso -- W15 Trelew QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01CARMARAYAFIO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayala / Fiorella Britez Risso (`KXITFWDOUBLES-26OCT01CARMARAYAFIO-AYAFIO`) | 0.88 / 0.92 (91) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Carrocera / Maria Maruca (`KXITFWDOUBLES-26OCT01CARMARAYAFIO-CARMAR`) | 0.06 / 0.12 (22) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Doldan / Celina Sosa vs Ailin Larraya Guidi / Sousa Salazar -- W15 Trelew QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01DOLCELAILSOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ailin Larraya Guidi / Sousa Salazar (`KXITFWDOUBLES-26OCT01DOLCELAILSOU-AILSOU`) | 0.88 / 0.94 (144) | 91.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Doldan / Celina Sosa (`KXITFWDOUBLES-26OCT01DOLCELAILSOU-DOLCEL`) | 0.06 / 0.12 (29) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Carolina Kuhl vs Kristina Penickova -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-02T00:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:230882:266381:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carolina Kuhl (`KXITFWMATCH-26OCT01KUHPEN-KUH`) | 0.35 / 0.37 (73) | 36.0% | -- | 28.5% | 36.1% [30.4%-45.8%] | -- | -- | -- | -- | PASS | +0.1 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kristina Penickova (`KXITFWMATCH-26OCT01KUHPEN-PEN`) | 0.62 / 0.65 (165) | 63.5% | -- | 71.5% | 63.9% [54.2%-69.6%] | -- | -- | -- | -- | PASS | +0.4 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1139.0, B 1178.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0769
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.029, surface_dev_loose -0.004, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francesca Pace vs Amelie Van Impe -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-02T00:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:228909:256673:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Pace (`KXITFWMATCH-26OCT01PACVAN-PAC`) | 0.56 / 0.58 (1483) | 57.0% | -- | 62.0% | 55.3% [50.5%-57.9%] | -- | -- | -- | -- | PASS | -1.7 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amelie Van Impe (`KXITFWMATCH-26OCT01PACVAN-VAN`) | 0.42 / 0.44 (4342) | 43.0% | -- | 38.0% | 44.7% [42.1%-49.5%] | -- | -- | -- | -- | PASS | +1.7 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2585.0, B 1949.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0367
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.016, surface_dev_loose +0.026, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Julieta Pareja vs Mary Stoiana -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-02T00:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:223168:264075:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julieta Pareja (`KXITFWMATCH-26OCT01PARSTO-PAR`) | 0.42 / 0.43 (64) | 42.5% | -- | 35.5% | 36.5% [36.0%-37.5%] | -- | -- | -- | -- | PASS | -6.0 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mary Stoiana (`KXITFWMATCH-26OCT01PARSTO-STO`) | 0.57 / 0.58 (4) | 57.5% | -- | 64.5% | 63.5% [62.5%-64.0%] | -- | -- | -- | -- | WATCH | +6.0 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1273.0, B 2840.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0074
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Henrique Pissetti Vialle / Leonardo Storck Franca vs Luis Guto Miguel / Eduardo Ribeiro -- ATP Challenger Curitiba QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-02T00:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01PISSTOMIGRIB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Guto Miguel / Eduardo Ribeiro (`KXATPCHALLENGERDOUBLES-26OCT01PISSTOMIGRIB-MIGRIB`) | 0.83 / 0.88 (53) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Henrique Pissetti Vialle / Leonardo Storck Franca (`KXATPCHALLENGERDOUBLES-26OCT01PISSTOMIGRIB-PISSTO`) | 0.10 / 0.17 (114) | 13.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Broadus / Zamarripa vs Chang / Hu -- W100 Templeton CA QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T01:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01BROZAMCHAHUX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Broadus / Zamarripa (`KXITFWDOUBLES-26OCT01BROZAMCHAHUX-BROZAM`) | 0.07 / 0.76 (72) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chang / Hu (`KXITFWDOUBLES-26OCT01BROZAMCHAHUX-CHAHUX`) | 0.15 / 0.28 (1) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Madison Brengle vs Arianna Zucchini -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-02T02:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:201483:222369:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madison Brengle (`KXITFWMATCH-26OCT01BREZUC-BRE`) | 0.76 / 0.78 (213) | 77.0% | -- | 48.9% | 63.2% [58.0%-75.3%] | -- | -- | -- | -- | PASS | -13.8 pp | REVIEW | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arianna Zucchini (`KXITFWMATCH-26OCT01BREZUC-ZUC`) | 0.22 / 0.24 (3146) | 23.0% | -- | 51.1% | 36.8% [24.7%-42.0%] | -- | -- | -- | -- | WATCH | +13.8 pp | REVIEW | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2464.0, B 2652.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0866
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.005, surface_dev_loose -0.015, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hewitt / Strakhova vs Frodin / Sahdiieva -- W100 Templeton CA QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T02:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01HEWSTRFROSAH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Frodin / Sahdiieva (`KXITFWDOUBLES-26OCT01HEWSTRFROSAH-FROSAH`) | 0.36 / 0.40 (41) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hewitt / Strakhova (`KXITFWDOUBLES-26OCT01HEWSTRFROSAH-HEWSTR`) | 0.07 / 0.66 (1574) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kawano Cho / Tarantola vs Meabe / Florencia Urrutia -- W15 Trelew QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T02:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01KAWTARMEAFLO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kawano Cho / Tarantola (`KXITFWDOUBLES-26OCT01KAWTARMEAFLO-KAWTAR`) | 0.06 / 0.93 (357) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Meabe / Florencia Urrutia (`KXITFWDOUBLES-26OCT01KAWTARMEAFLO-MEAFLO`) | 0.07 / 0.93 (100) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Moyano / Sofia Sanchez vs Bhatia / Belen Moron -- W15 Trelew QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T02:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01MOYSOFBHABEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bhatia / Belen Moron (`KXITFWDOUBLES-26OCT01MOYSOFBHABEL-BHABEL`) | 0.08 / 0.36 (40) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Moyano / Sofia Sanchez (`KXITFWDOUBLES-26OCT01MOYSOFBHABEL-MOYSOF`) | 0.61 / 0.92 (72) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Penickova / Penickova vs Osuigwe / Urhobo -- W100 Templeton CA QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T03:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01PENPENOSUURH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Osuigwe / Urhobo (`KXITFWDOUBLES-26OCT01PENPENOSUURH-OSUURH`) | 0.51 / 0.52 (10) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Penickova / Penickova (`KXITFWDOUBLES-26OCT01PENPENOSUURH-PENPEN`) | 0.41 / 0.50 (1100) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Arthur Fils vs Frances Tiafoe -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126207:209950:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fils (`KXATPMATCH-26OCT01FILTIA-FIL`) | 0.71 / 0.72 (1638) | 71.5% | -- | 69.5% | 67.8% [64.3%-69.0%] | 70.6% | 71.5% | 71.0% | MODEL_LONE_OUTLIER | PASS | -3.7 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Frances Tiafoe (`KXATPMATCH-26OCT01FILTIA-TIA`) | 0.28 / 0.29 (26451) | 28.5% | -- | 30.5% | 32.2% [31.0%-35.7%] | 29.4% | 29.0% | 29.2% | MODEL_LONE_OUTLIER | WATCH | +3.7 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5009.0, B 5884.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0235
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.000, surface_dev_loose +0.012, surface_dev_tight -0.013
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01FILTIA-29` Over 28.5 games: 0.22/0.29 mid 25.5%, model 36.1% (market_conditioned_v1 (model4_board_v1)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01FILTIA-FIL6` Will Arthur Fils win at least 5.5 more games than Frances Tiafoe?: 0.22/0.25 mid 23.5%, model 13.4% (market_conditioned_v1 (model4_board_v1)) -- gap -10.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01FILTIA-24` Over 23.5 games: 0.42/0.44 mid 43.0%, model 52.3% (market_conditioned_v1 (model4_board_v1)) -- gap +9.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01FILTIA-19` Over 18.5 games: 0.79/0.85 mid 82.0%, model 89.4% (market_conditioned_v1 (model4_board_v1)) -- gap +7.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01FILTIA-FIL21` Will Arthur Fils win the Arthur Fils vs Frances Tiafoe match by a set score of 2-1?: 0.22/0.25 mid 23.5%, model 29.5% (market_conditioned_v1 (model4_board_v1)) -- gap +6.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01FILTIA-FIL20` Will Arthur Fils win the Arthur Fils vs Frances Tiafoe match by a set score of 2-0?: 0.45/0.48 mid 46.5%, model 41.7% (market_conditioned_v1 (model4_board_v1)) -- gap -4.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01FILTIA-FIL3` Will Arthur Fils win at least 2.5 more games than Frances Tiafoe?: 0.58/0.60 mid 59.0%, model 54.7% (market_conditioned_v1 (model4_board_v1)) -- gap -4.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01FILTIA-TIA21` Will Frances Tiafoe win the Arthur Fils vs Frances Tiafoe match by a set score of 2-1?: 0.12/0.16 mid 14.0%, model 16.2% (market_conditioned_v1 (model4_board_v1)) -- gap +2.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01FILTIA-TIA20` Will Frances Tiafoe win the Arthur Fils vs Frances Tiafoe match by a set score of 2-0?: 0.13/0.16 mid 14.5%, model 12.5% (market_conditioned_v1 (model4_board_v1)) -- gap -2.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01FILTIA-TIA2` Will Frances Tiafoe win at least 1.5 more games than Arthur Fils?: 0.22/0.25 mid 23.5%, model 22.1% (market_conditioned_v1 (model4_board_v1)) -- gap -1.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ugo Humbert vs Jiri Lehecka -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200005:208103:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ugo Humbert (`KXATPMATCH-26OCT01HUMLEH-HUM`) | 0.35 / 0.36 (964) | 35.5% | -- | 45.3% | 45.8% [43.4%-47.2%] | -- | -- | -- | -- | SHADOW_BET | +10.3 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiri Lehecka (`KXATPMATCH-26OCT01HUMLEH-LEH`) | 0.63 / 0.64 (7963) | 63.5% | -- | 54.7% | 54.2% [52.8%-56.6%] | -- | -- | -- | -- | PASS | -9.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5799.0, B 5765.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0192
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.014, surface_dev_loose -0.004, surface_dev_tight -0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01HUMLEH-24` Over 23.5 games: 0.42/0.44 mid 43.0%, model 57.8% (market_conditioned_v1 (model4_board_v1)) -- gap +14.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01HUMLEH-19` Over 18.5 games: 0.63/0.99 mid 81.0%, model 94.2% (market_conditioned_v1 (model4_board_v1)) -- gap +13.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01HUMLEH-29` Over 28.5 games: 0.16/0.47 mid 31.5%, model 41.8% (market_conditioned_v1 (model4_board_v1)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01HUMLEH-LEH6` Will Jiri Lehecka win at least 5.5 more games than Ugo Humbert?: 0.05/0.21 mid 13.0%, model 6.9% (market_conditioned_v1 (model4_board_v1)) -- gap -6.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01HUMLEH-LEH3` Will Jiri Lehecka win at least 2.5 more games than Ugo Humbert?: 0.49/0.51 mid 50.0%, model 44.1% (market_conditioned_v1 (model4_board_v1)) -- gap -5.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01HUMLEH-LEH21` Will Jiri Lehecka win the Ugo Humbert vs Jiri Lehecka match by a set score of 2-1?: 0.21/0.26 mid 23.5%, model 28.7% (market_conditioned_v1 (model4_board_v1)) -- gap +5.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01HUMLEH-LEH20` Will Jiri Lehecka win the Ugo Humbert vs Jiri Lehecka match by a set score of 2-0?: 0.38/0.42 mid 40.0%, model 35.3% (market_conditioned_v1 (model4_board_v1)) -- gap -4.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01HUMLEH-HUM21` Will Ugo Humbert win the Ugo Humbert vs Jiri Lehecka match by a set score of 2-1?: 0.15/0.19 mid 17.0%, model 19.6% (market_conditioned_v1 (model4_board_v1)) -- gap +2.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01HUMLEH-HUM20` Will Ugo Humbert win the Ugo Humbert vs Jiri Lehecka match by a set score of 2-0?: 0.17/0.19 mid 18.0%, model 16.4% (market_conditioned_v1 (model4_board_v1)) -- gap -1.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01HUMLEH-HUM2` Will Ugo Humbert win at least 1.5 more games than Jiri Lehecka?: 0.25/0.33 mid 29.0%, model 27.9% (market_conditioned_v1 (model4_board_v1)) -- gap -1.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kyrian Jacquet vs Luciano Darderi -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208021:209260:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciano Darderi (`KXATPMATCH-26OCT01JACDAR-DAR`) | 0.56 / 0.57 (32038) | 56.5% | -- | 39.2% | 41.6% [37.8%-49.5%] | 55.6% | 56.0% | -- | INSUFFICIENT_INPUTS | PASS | -14.9 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kyrian Jacquet (`KXATPMATCH-26OCT01JACDAR-JAC`) | 0.43 / 0.44 (1747) | 43.5% | -- | 60.8% | 58.4% [50.5%-62.2%] | 44.4% | 44.5% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +14.9 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4700.0, B 7374.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0584
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.029, surface_dev_loose +0.038, surface_dev_tight -0.039
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01JACDAR-24` Over 23.5 games: 0.44/0.46 mid 45.0%, model 54.8% (market_conditioned_v1 (model4_board_v1)) -- gap +9.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01JACDAR-29` Over 28.5 games: 0.24/0.31 mid 27.5%, model 36.6% (market_conditioned_v1 (model4_board_v1)) -- gap +9.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01JACDAR-19` Over 18.5 games: 0.79/0.86 mid 82.5%, model 88.8% (market_conditioned_v1 (model4_board_v1)) -- gap +6.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01JACDAR-DAR21` Will Luciano Darderi win the Kyrian Jacquet vs Luciano Darderi match by a set score of 2-1?: 0.19/0.24 mid 21.5%, model 27.0% (market_conditioned_v1 (model4_board_v1)) -- gap +5.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01JACDAR-JAC20` Will Kyrian Jacquet win the Kyrian Jacquet vs Luciano Darderi match by a set score of 2-0?: 0.23/0.27 mid 25.0%, model 20.9% (market_conditioned_v1 (model4_board_v1)) -- gap -4.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01JACDAR-DAR5` Will Luciano Darderi win at least 4.5 more games than Kyrian Jacquet?: 0.20/0.27 mid 23.5%, model 19.4% (market_conditioned_v1 (model4_board_v1)) -- gap -4.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01JACDAR-DAR20` Will Luciano Darderi win the Kyrian Jacquet vs Luciano Darderi match by a set score of 2-0?: 0.31/0.36 mid 33.5%, model 29.5% (market_conditioned_v1 (model4_board_v1)) -- gap -4.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01JACDAR-JAC21` Will Kyrian Jacquet win the Kyrian Jacquet vs Luciano Darderi match by a set score of 2-1?: 0.18/0.22 mid 20.0%, model 22.7% (market_conditioned_v1 (model4_board_v1)) -- gap +2.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01JACDAR-JAC2` Will Kyrian Jacquet win at least 1.5 more games than Luciano Darderi?: 0.36/0.41 mid 38.5%, model 36.1% (market_conditioned_v1 (model4_board_v1)) -- gap -2.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01JACDAR-DAR2` Will Luciano Darderi win at least 1.5 more games than Kyrian Jacquet?: 0.48/0.51 mid 49.5%, model 48.8% (market_conditioned_v1 (model4_board_v1)) -- gap -0.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Jaume Munar vs Jaime Faria -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144719:210262:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jaime Faria (`KXATPMATCH-26OCT01MUNFAR-FAR`) | 0.37 / 0.38 (7743) | 37.5% | -- | 34.1% | 38.8% [35.9%-42.1%] | 37.7% | 36.8% | 37.2% | MARKETS_AGREE | PASS | +1.3 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Jaume Munar (`KXATPMATCH-26OCT01MUNFAR-MUN`) | 0.61 / 0.62 (261) | 61.5% | -- | 65.9% | 61.2% [57.9%-64.0%] | 62.3% | 63.1% | 62.7% | MARKETS_AGREE | PASS | -0.3 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4944.0, B 5916.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0306
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.001, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01MUNFAR-28` Over 27.5 games: 0.26/0.32 mid 29.0%, model 40.6% (market_conditioned_v1 (model4_board_v1)) -- gap +11.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01MUNFAR-23` Over 22.5 games: 0.50/0.51 mid 50.5%, model 60.8% (market_conditioned_v1 (model4_board_v1)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01MUNFAR-MUN6` Will Jaume Munar win at least 5.5 more games than Jaime Faria?: 0.20/0.23 mid 21.5%, model 12.2% (market_conditioned_v1 (model4_board_v1)) -- gap -9.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01MUNFAR-18` Over 17.5 games: 0.85/0.90 mid 87.5%, model 93.7% (market_conditioned_v1 (model4_board_v1)) -- gap +6.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01MUNFAR-MUN3` Will Jaume Munar win at least 2.5 more games than Jaime Faria?: 0.51/0.53 mid 52.0%, model 46.5% (market_conditioned_v1 (model4_board_v1)) -- gap -5.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MUNFAR-MUN21` Will Jaume Munar win the Jaume Munar vs Jaime Faria match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 28.3% (market_conditioned_v1 (model4_board_v1)) -- gap +5.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MUNFAR-MUN20` Will Jaume Munar win the Jaume Munar vs Jaime Faria match by a set score of 2-0?: 0.37/0.40 mid 38.5%, model 33.7% (market_conditioned_v1 (model4_board_v1)) -- gap -4.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MUNFAR-FAR21` Will Jaime Faria win the Jaume Munar vs Jaime Faria match by a set score of 2-1?: 0.15/0.18 mid 16.5%, model 20.4% (market_conditioned_v1 (model4_board_v1)) -- gap +3.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MUNFAR-FAR20` Will Jaime Faria win the Jaume Munar vs Jaime Faria match by a set score of 2-0?: 0.18/0.22 mid 20.0%, model 17.6% (market_conditioned_v1 (model4_board_v1)) -- gap -2.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01MUNFAR-FAR2` Will Jaime Faria win at least 1.5 more games than Jaume Munar?: 0.31/0.33 mid 32.0%, model 30.9% (market_conditioned_v1 (model4_board_v1)) -- gap -1.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE

## Denis Shapovalov vs Alejandro Tabilo -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126214:133430:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Denis Shapovalov (`KXATPMATCH-26OCT01SHATAB-SHA`) | 0.57 / 0.59 (21375) | 58.0% | -- | 48.5% | 52.0% [49.5%-53.4%] | -- | -- | -- | -- | PASS | -6.0 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Tabilo (`KXATPMATCH-26OCT01SHATAB-TAB`) | 0.41 / 0.43 (17116) | 42.0% | -- | 51.5% | 48.0% [46.6%-50.5%] | -- | -- | -- | -- | SHADOW_BET | +6.0 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4723.0, B 7913.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0196
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.015
* Derivatives listed: 6 (GAME_SPREAD, MATCH_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXATPGTOTAL-26OCT01SHATAB-24` Over 23.5 games: 0.43/0.45 mid 44.0%, model 55.4% (market_conditioned_v1 (model4_board_v1)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01SHATAB-19` Over 18.5 games: 0.64/0.99 mid 81.5%, model 90.1% (market_conditioned_v1 (model4_board_v1)) -- gap +8.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01SHATAB-29` Over 28.5 games: 0.11/0.50 mid 30.5%, model 37.9% (market_conditioned_v1 (model4_board_v1)) -- gap +7.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01SHATAB-SHA3` Will Denis Shapovalov win at least 2.5 more games than Alejandro Tabilo?: 0.45/0.47 mid 46.0%, model 41.9% (market_conditioned_v1 (model4_board_v1)) -- gap -4.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01SHATAB-SHA6` Will Denis Shapovalov win at least 5.5 more games than Alejandro Tabilo?: 0.01/0.25 mid 13.0%, model 9.6% (market_conditioned_v1 (model4_board_v1)) -- gap -3.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01SHATAB-TAB2` Will Alejandro Tabilo win at least 1.5 more games than Denis Shapovalov?: 0.34/0.39 mid 36.5%, model 34.6% (market_conditioned_v1 (model4_board_v1)) -- gap -1.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Valentin Vacherot vs Stefanos Tsitsipas -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126774:200473:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefanos Tsitsipas (`KXATPMATCH-26OCT01VACTSI-TSI`) | 0.59 / 0.60 (9958) | 59.5% | -- | 48.1% | 49.1% [47.2%-56.1%] | 58.3% | 58.8% | 58.3% | MARKETS_AGREE | PASS | -10.4 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Valentin Vacherot (`KXATPMATCH-26OCT01VACTSI-VAC`) | 0.40 / 0.41 (475) | 40.5% | -- | 51.9% | 50.9% [43.9%-52.8%] | 41.7% | 40.5% | 41.7% | MARKETS_AGREE | SHADOW_BET | +10.4 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5393.0, B 5388.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0446
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.019, surface_dev_loose +0.009, surface_dev_tight -0.019
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01VACTSI-29` Over 28.5 games: 0.26/0.35 mid 30.5%, model 43.5% (market_conditioned_v1 (model4_board_v1)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01VACTSI-24` Over 23.5 games: 0.48/0.49 mid 48.5%, model 59.8% (market_conditioned_v1 (model4_board_v1)) -- gap +11.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01VACTSI-19` Over 18.5 games: 0.84/0.89 mid 86.5%, model 95.4% (market_conditioned_v1 (model4_board_v1)) -- gap +8.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01VACTSI-TSI6` Will Stefanos Tsitsipas win at least 5.5 more games than Valentin Vacherot?: 0.02/0.25 mid 13.5%, model 5.1% (market_conditioned_v1 (model4_board_v1)) -- gap -8.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01VACTSI-TSI3` Will Stefanos Tsitsipas win at least 2.5 more games than Valentin Vacherot?: 0.43/0.44 mid 43.5%, model 38.9% (market_conditioned_v1 (model4_board_v1)) -- gap -4.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01VACTSI-TSI20` Will Stefanos Tsitsipas win the Valentin Vacherot vs Stefanos Tsitsipas match by a set score of 2-0?: 0.35/0.37 mid 36.0%, model 31.7% (market_conditioned_v1 (model4_board_v1)) -- gap -4.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01VACTSI-TSI21` Will Stefanos Tsitsipas win the Valentin Vacherot vs Stefanos Tsitsipas match by a set score of 2-1?: 0.22/0.25 mid 23.5%, model 27.7% (market_conditioned_v1 (model4_board_v1)) -- gap +4.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01VACTSI-VAC21` Will Valentin Vacherot win the Valentin Vacherot vs Stefanos Tsitsipas match by a set score of 2-1?: 0.16/0.19 mid 17.5%, model 21.5% (market_conditioned_v1 (model4_board_v1)) -- gap +4.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01VACTSI-VAC2` Will Valentin Vacherot win at least 1.5 more games than Stefanos Tsitsipas?: 0.34/0.37 mid 35.5%, model 31.8% (market_conditioned_v1 (model4_board_v1)) -- gap -3.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01VACTSI-VAC20` Will Valentin Vacherot win the Valentin Vacherot vs Stefanos Tsitsipas match by a set score of 2-0?: 0.21/0.23 mid 22.0%, model 19.1% (market_conditioned_v1 (model4_board_v1)) -- gap -2.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Alex de Minaur vs Quentin Halys -- ATP Beijing R16

ATP (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111460:200282:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex de Minaur (`KXATPMATCH-26OCT01DEHAL-DE`) | 0.72 / 0.73 (10) | 72.5% | -- | 79.4% | 78.7% [77.7%-79.4%] | -- | -- | -- | -- | SHADOW_BET | +6.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Quentin Halys (`KXATPMATCH-26OCT01DEHAL-HAL`) | 0.27 / 0.28 (8123) | 27.5% | -- | 20.6% | 21.3% [20.6%-22.3%] | -- | -- | -- | -- | PASS | -6.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 7096.0, B 7371.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0086
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.000, surface_dev_loose +0.003, surface_dev_tight +0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01DEHAL-22` Over 21.5 games: 0.54/0.57 mid 55.5%, model 67.2% (market_conditioned_v1 (model4_board_v1)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01DEHAL-27` Over 26.5 games: 0.27/0.35 mid 31.0%, model 41.4% (market_conditioned_v1 (model4_board_v1)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01DEHAL-DE8` Will Alex de Minaur win at least 7.5 more games than Quentin Halys?: 0.02/0.24 mid 13.0%, model 2.8% (market_conditioned_v1 (model4_board_v1)) -- gap -10.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01DEHAL-DE21` Will Alex de Minaur win the Alex de Minaur vs Quentin Halys match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 29.6% (market_conditioned_v1 (model4_board_v1)) -- gap +6.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01DEHAL-DE20` Will Alex de Minaur win the Alex de Minaur vs Quentin Halys match by a set score of 2-0?: 0.48/0.50 mid 49.0%, model 42.7% (market_conditioned_v1 (model4_board_v1)) -- gap -6.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01DEHAL-DE5` Will Alex de Minaur win at least 4.5 more games than Quentin Halys?: 0.33/0.34 mid 33.5%, model 28.2% (market_conditioned_v1 (model4_board_v1)) -- gap -5.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01DEHAL-17` Over 16.5 games: 0.91/0.97 mid 94.0%, model 97.4% (market_conditioned_v1 (model4_board_v1)) -- gap +3.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01DEHAL-HAL21` Will Quentin Halys win the Alex de Minaur vs Quentin Halys match by a set score of 2-1?: 0.11/0.14 mid 12.5%, model 15.7% (market_conditioned_v1 (model4_board_v1)) -- gap +3.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01DEHAL-DE2` Will Alex de Minaur win at least 1.5 more games than Quentin Halys?: 0.62/0.71 mid 66.5%, model 65.3% (market_conditioned_v1 (model4_board_v1)) -- gap -1.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01DEHAL-HAL20` Will Quentin Halys win the Alex de Minaur vs Quentin Halys match by a set score of 2-0?: 0.11/0.15 mid 13.0%, model 12.0% (market_conditioned_v1 (model4_board_v1)) -- gap -1.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alex Molcan vs Karen Khachanov -- ATP Beijing R16

ATP (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111575:144684:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karen Khachanov (`KXATPMATCH-26OCT01MOLKHA-KHA`) | 0.79 / 0.80 (62613) | 79.5% | -- | 70.7% | 71.2% [66.9%-72.3%] | 77.5% | 77.2% | 77.4% | KALSHI_LONE_OUTLIER | PASS | -8.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Alex Molcan (`KXATPMATCH-26OCT01MOLKHA-MOL`) | 0.21 / 0.22 (5395) | 21.5% | -- | 29.3% | 28.8% [27.7%-33.1%] | 22.5% | 22.5% | 22.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3805.0, B 5981.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0271
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.008, surface_dev_loose -0.012, surface_dev_tight +0.016
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01MOLKHA-22` Over 21.5 games: 0.48/0.50 mid 49.0%, model 61.6% (market_conditioned_v1 (model4_board_v1)) -- gap +12.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01MOLKHA-27` Over 26.5 games: 0.22/0.30 mid 26.0%, model 37.3% (market_conditioned_v1 (model4_board_v1)) -- gap +11.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01MOLKHA-KHA5` Will Karen Khachanov win at least 4.5 more games than Alex Molcan?: 0.45/0.47 mid 46.0%, model 36.1% (market_conditioned_v1 (model4_board_v1)) -- gap -9.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01MOLKHA-KHA8` Will Karen Khachanov win at least 7.5 more games than Alex Molcan?: 0.02/0.25 mid 13.5%, model 4.6% (market_conditioned_v1 (model4_board_v1)) -- gap -8.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MOLKHA-KHA21` Will Karen Khachanov win the Alex Molcan vs Karen Khachanov match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 29.4% (market_conditioned_v1 (model4_board_v1)) -- gap +7.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MOLKHA-KHA20` Will Karen Khachanov win the Alex Molcan vs Karen Khachanov match by a set score of 2-0?: 0.54/0.57 mid 55.5%, model 49.0% (market_conditioned_v1 (model4_board_v1)) -- gap -6.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01MOLKHA-17` Over 16.5 games: 0.89/0.93 mid 91.0%, model 95.7% (market_conditioned_v1 (model4_board_v1)) -- gap +4.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01MOLKHA-KHA2` Will Karen Khachanov win at least 1.5 more games than Alex Molcan?: 0.74/0.78 mid 76.0%, model 72.5% (market_conditioned_v1 (model4_board_v1)) -- gap -3.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MOLKHA-MOL21` Will Alex Molcan win the Alex Molcan vs Karen Khachanov match by a set score of 2-1?: 0.09/0.12 mid 10.5%, model 12.6% (market_conditioned_v1 (model4_board_v1)) -- gap +2.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MOLKHA-MOL20` Will Alex Molcan win the Alex Molcan vs Karen Khachanov match by a set score of 2-0?: 0.08/0.12 mid 10.0%, model 9.0% (market_conditioned_v1 (model4_board_v1)) -- gap -1.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yunchaokete Bu vs Novak Djokovic -- ATP Beijing R16

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT01YUNDJO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Novak Djokovic (`KXATPMATCH-26OCT01YUNDJO-DJO`) | 0.76 / 0.77 (39972) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yunchaokete Bu (`KXATPMATCH-26OCT01YUNDJO-YUN`) | 0.24 / 0.25 (26492) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexander Zverev vs Juncheng Shang -- ATP Beijing R16

ATP (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:100644:209992:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juncheng Shang (`KXATPMATCH-26OCT01ZVESHA-SHA`) | 0.10 / 0.11 (29953) | 10.5% | -- | 11.4% | 12.8% [11.1%-14.7%] | -- | -- | -- | -- | WATCH | +2.4 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Zverev (`KXATPMATCH-26OCT01ZVESHA-ZVE`) | 0.90 / 0.91 (11407) | 90.5% | -- | 88.6% | 87.2% [85.3%-88.9%] | -- | -- | -- | -- | PASS | -3.4 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 8165.0, B 3774.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0182
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.018, surface_dev_loose -0.001, surface_dev_tight +0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGSPREAD-26OCT01ZVESHA-ZVE6` Will Alexander Zverev win at least 5.5 more games than Juncheng Shang?: 0.37/0.39 mid 38.0%, model 24.3% (market_conditioned_v1 (model4_board_v1)) -- gap -13.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01ZVESHA-20` Over 19.5 games: 0.58/0.61 mid 59.5%, model 72.4% (market_conditioned_v1 (model4_board_v1)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01ZVESHA-15` Over 14.5 games: 0.77/0.99 mid 88.0%, model 99.6% (market_conditioned_v1 (model4_board_v1)) -- gap +11.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01ZVESHA-ZVE9` Will Alexander Zverev win at least 8.5 more games than Juncheng Shang?: 0.01/0.25 mid 13.0%, model 1.8% (market_conditioned_v1 (model4_board_v1)) -- gap -11.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01ZVESHA-25` Over 24.5 games: 0.24/0.32 mid 28.0%, model 37.9% (market_conditioned_v1 (model4_board_v1)) -- gap +9.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01ZVESHA-ZVE21` Will Alexander Zverev win the Alexander Zverev vs Juncheng Shang match by a set score of 2-1?: 0.17/0.21 mid 19.0%, model 25.9% (market_conditioned_v1 (model4_board_v1)) -- gap +6.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01ZVESHA-ZVE20` Will Alexander Zverev win the Alexander Zverev vs Juncheng Shang match by a set score of 2-0?: 0.68/0.69 mid 68.5%, model 63.4% (market_conditioned_v1 (model4_board_v1)) -- gap -5.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01ZVESHA-ZVE3` Will Alexander Zverev win at least 2.5 more games than Juncheng Shang?: 0.79/0.83 mid 81.0%, model 76.5% (market_conditioned_v1 (model4_board_v1)) -- gap -4.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01ZVESHA-SHA21` Will Juncheng Shang win the Alexander Zverev vs Juncheng Shang match by a set score of 2-1?: 0.03/0.06 mid 4.5%, model 6.6% (market_conditioned_v1 (model4_board_v1)) -- gap +2.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01ZVESHA-SHA20` Will Juncheng Shang win the Alexander Zverev vs Juncheng Shang match by a set score of 2-0?: 0.02/0.06 mid 4.0%, model 4.2% (market_conditioned_v1 (model4_board_v1)) -- gap +0.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ekaterina Alexandrova vs Aliaksandra Sasnovich -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:205925:206420:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Alexandrova (`KXWTAMATCH-26OCT01ALESAS-ALE`) | 0.59 / 0.60 (15747) | 59.5% | -- | 60.4% | 61.4% [59.9%-64.9%] | 58.3% | 59.2% | 58.8% | MODEL_LONE_OUTLIER | PASS | +1.9 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |
| Aliaksandra Sasnovich (`KXWTAMATCH-26OCT01ALESAS-SAS`) | 0.40 / 0.41 (3105) | 40.5% | -- | 39.6% | 38.6% [35.1%-40.1%] | 41.7% | 41.2% | 41.4% | MODEL_LONE_OUTLIER | PASS | -1.9 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4877.0, B 4822.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0251
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose -0.010, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01ALESAS-28` Over 27.5 games: 0.21/0.26 mid 23.5%, model 34.2% (market_conditioned_v1 (model4_board_v1)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01ALESAS-23` Over 22.5 games: 0.44/0.46 mid 45.0%, model 55.7% (market_conditioned_v1 (model4_board_v1)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01ALESAS-18` Over 17.5 games: 0.73/0.84 mid 78.5%, model 87.8% (market_conditioned_v1 (model4_board_v1)) -- gap +9.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Nikola Bartunkova vs Magdalena Frech -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211684:223360:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikola Bartunkova (`KXWTAMATCH-26OCT01BARFRE-BAR`) | 0.58 / 0.59 (3592) | 58.5% | -- | 57.8% | 56.3% [50.5%-58.9%] | 58.3% | 59.0% | 58.7% | MODEL_LONE_OUTLIER | PASS | -2.2 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Magdalena Frech (`KXWTAMATCH-26OCT01BARFRE-FRE`) | 0.41 / 0.42 (7779) | 41.5% | -- | 42.2% | 43.7% [41.1%-49.5%] | 41.7% | 41.2% | 41.4% | MODEL_LONE_OUTLIER | PASS | +2.2 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3248.0, B 4552.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0416
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.021, surface_dev_loose +0.005, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01BARFRE-27` Over 26.5 games: 0.27/0.33 mid 30.0%, model 39.6% (market_conditioned_v1 (model4_board_v1)) -- gap +9.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01BARFRE-22` Over 21.5 games: 0.53/0.55 mid 54.0%, model 62.8% (market_conditioned_v1 (model4_board_v1)) -- gap +8.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01BARFRE-17` Over 16.5 games: 0.82/0.92 mid 87.0%, model 93.9% (market_conditioned_v1 (model4_board_v1)) -- gap +6.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Sara Bejlek vs Maddison Inglis -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213666:239383:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Bejlek (`KXWTAMATCH-26OCT01BEJING-BEJ`) | 0.75 / 0.76 (22617) | 75.5% | -- | 76.3% | 73.8% [69.7%-74.6%] | 73.4% | 74.7% | 74.0% | MARKETS_AGREE | PASS | -1.7 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |
| Maddison Inglis (`KXWTAMATCH-26OCT01BEJING-ING`) | 0.24 / 0.25 (1359) | 24.5% | -- | 23.7% | 26.2% [25.4%-30.3%] | 26.7% | 26.0% | 26.3% | MARKETS_AGREE | PASS | +1.7 pp | NORMAL | AGING | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3433.0, B 3027.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0244
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.018, surface_dev_loose +0.009, surface_dev_tight -0.009
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01BEJING-21` Over 20.5 games: 0.47/0.49 mid 48.0%, model 60.9% (market_conditioned_v1 (model4_board_v1)) -- gap +12.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01BEJING-26` Over 25.5 games: 0.23/0.32 mid 27.5%, model 38.4% (market_conditioned_v1 (model4_board_v1)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01BEJING-16` Over 15.5 games: 0.84/0.96 mid 90.0%, model 95.3% (market_conditioned_v1 (model4_board_v1)) -- gap +5.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
* Warnings: STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Belinda Bencic vs Anastasia Zakharova -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202505:220435:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Belinda Bencic (`KXWTAMATCH-26OCT01BENZAK-BEN`) | 0.79 / 0.81 (9306) | 80.0% | -- | 77.8% | 79.3% [77.0%-82.6%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Zakharova (`KXWTAMATCH-26OCT01BENZAK-ZAK`) | 0.20 / 0.21 (7899) | 20.5% | -- | 22.2% | 20.7% [17.4%-23.0%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3571.0, B 4628.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0279
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.023, surface_dev_loose +0.004, surface_dev_tight -0.000
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Marie Bouzkova vs Kimberly Birrell -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213631:214040:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kimberly Birrell (`KXWTAMATCH-26OCT01BOUBIR-BIR`) | 0.33 / 0.34 (3216) | 33.5% | -- | 45.8% | 43.6% [39.5%-45.8%] | -- | -- | -- | -- | SHADOW_BET | +10.2 pp | REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marie Bouzkova (`KXWTAMATCH-26OCT01BOUBIR-BOU`) | 0.65 / 0.67 (454) | 66.0% | -- | 54.2% | 56.4% [54.2%-60.5%] | -- | -- | -- | -- | PASS | -9.7 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4089.0, B 5020.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0313
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.021, surface_dev_loose -0.011, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01BOUBIR-17` Over 16.5 games: 0.02/0.99 mid 50.5%, model 91.9% (market_conditioned_v1 (model4_board_v1)) -- gap +41.4 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01BOUBIR-27` Over 26.5 games: 0.02/0.99 mid 50.5%, model 36.7% (market_conditioned_v1 (model4_board_v1)) -- gap -13.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01BOUBIR-22` Over 21.5 games: 0.45/0.48 mid 46.5%, model 59.6% (market_conditioned_v1 (model4_board_v1)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Linda Fruhvirtova vs Liudmila Samsonova -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214643:222258:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linda Fruhvirtova (`KXWTAMATCH-26OCT01FRUSAM-FRU`) | 0.18 / 0.19 (1706) | 18.5% | -- | 43.7% | 39.6% [28.0%-43.7%] | 20.2% | 19.1% | 19.1% | MODEL_LONE_OUTLIER | WATCH | +21.1 pp | HIGH_REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Liudmila Samsonova (`KXWTAMATCH-26OCT01FRUSAM-SAM`) | 0.81 / 0.82 (17370) | 81.5% | -- | 56.3% | 60.4% [56.3%-72.0%] | 79.8% | 81.7% | 81.7% | MODEL_LONE_OUTLIER | PASS | -21.1 pp | HIGH_REVIEW | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4353.0, B 3968.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0785
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01FRUSAM-FRU  (YES = Linda Fruhvirtova)
Model: 40%
Kalshi: 18%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.040, surface_pool_high +0.041, surface_dev_loose +0.021, surface_dev_tight -0.020
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01FRUSAM-21` Over 20.5 games: 0.44/0.46 mid 45.0%, model 56.9% (market_conditioned_v1 (model4_board_v1)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01FRUSAM-26` Over 25.5 games: 0.22/0.29 mid 25.5%, model 34.9% (market_conditioned_v1 (model4_board_v1)) -- gap +9.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01FRUSAM-16` Over 15.5 games: 0.82/0.95 mid 88.5%, model 94.2% (market_conditioned_v1 (model4_board_v1)) -- gap +5.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Viktorija Golubic vs Peyton Stearns -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:203530:220548:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viktorija Golubic (`KXWTAMATCH-26OCT01GOLSTE-GOL`) | 0.40 / 0.41 (7430) | 40.5% | -- | 45.8% | 47.4% [46.8%-48.4%] | 40.6% | 40.7% | 40.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.9 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Peyton Stearns (`KXWTAMATCH-26OCT01GOLSTE-STE`) | 0.59 / 0.60 (357) | 59.5% | -- | 54.2% | 52.6% [51.6%-53.2%] | 59.4% | 59.6% | 59.5% | MODEL_LONE_OUTLIER | PASS | -6.9 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4714.0, B 4027.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0079
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01GOLSTE-26` Over 25.5 games: 0.28/0.36 mid 32.0%, model 43.7% (market_conditioned_v1 (model4_board_v1)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01GOLSTE-21` Over 20.5 games: 0.55/0.56 mid 55.5%, model 66.9% (market_conditioned_v1 (model4_board_v1)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01GOLSTE-16` Over 15.5 games: 0.88/0.97 mid 92.5%, model 97.0% (market_conditioned_v1 (model4_board_v1)) -- gap +4.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Sonay Kartal vs Xinyu Wang -- WTA Beijing R64

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT01KARWAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sonay Kartal (`KXWTAMATCH-26OCT01KARWAN-KAR`) | 0.50 / 0.51 (1735) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xinyu Wang (`KXWTAMATCH-26OCT01KARWAN-WAN`) | 0.49 / 0.50 (10822) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; STALE_QUOTE

## Ashlyn Krueger vs Ann Li -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215983:221909:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ann Li (`KXWTAMATCH-26OCT01KRUANN-ANN`) | 0.56 / 0.57 (6766) | 56.5% | -- | 63.7% | 59.7% [55.7%-61.7%] | -- | -- | -- | -- | WATCH | +3.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ashlyn Krueger (`KXWTAMATCH-26OCT01KRUANN-KRU`) | 0.43 / 0.45 (5259) | 44.0% | -- | 36.3% | 40.3% [38.3%-44.3%] | -- | -- | -- | -- | PASS | -3.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4211.0, B 4567.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0301
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01KRUANN-18` Over 17.5 games: 0.02/0.99 mid 50.5%, model 90.1% (market_conditioned_v1 (model4_board_v1)) -- gap +39.6 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01KRUANN-28` Over 27.5 games: 0.03/0.99 mid 51.0%, model 36.7% (market_conditioned_v1 (model4_board_v1)) -- gap -14.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01KRUANN-23` Over 22.5 games: 0.45/0.48 mid 46.5%, model 57.7% (market_conditioned_v1 (model4_board_v1)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Karolina Muchova vs Katie Boulter -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211107:214096:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katie Boulter (`KXWTAMATCH-26OCT01MUCBOU-BOU`) | 0.12 / 0.13 (10) | 12.5% | -- | 24.1% | 22.9% [22.1%-23.7%] | 14.7% | 12.1% | 12.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.4 pp | REVIEW | AGING | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Karolina Muchova (`KXWTAMATCH-26OCT01MUCBOU-MUC`) | 0.87 / 0.88 (12093) | 87.5% | -- | 75.9% | 77.1% [76.3%-77.9%] | 85.3% | 87.4% | 87.4% | MODEL_LONE_OUTLIER | PASS | -10.4 pp | REVIEW | AGING | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3972.0, B 3928.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0078
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high +0.000, surface_dev_loose +0.008, surface_dev_tight -0.008
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT01MUCBOU-19` Over 18.5 games: 0.50/0.52 mid 51.0%, model 68.7% (market_conditioned_v1 (model4_board_v1)) -- gap +17.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01MUCBOU-24` Over 23.5 games: 0.18/0.27 mid 22.5%, model 36.5% (market_conditioned_v1 (model4_board_v1)) -- gap +14.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mio Mushika vs Yuno Kitahara -- W35 Wagga Wagga QF

ITF (ITF) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222986:263881:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuno Kitahara (`KXITFWMATCH-26OCT01MUSKIT-KIT`) | 0.38 / 0.43 (28) | 40.5% | -- | 33.9% | 35.4% [34.4%-37.4%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.1 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mio Mushika (`KXITFWMATCH-26OCT01MUSKIT-MUS`) | 0.55 / 0.60 (4) | 57.5% | -- | 66.1% | 64.6% [62.6%-65.6%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +7.1 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2224.0, B 2068.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.015
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Linda Noskova vs Elena-Gabriela Ruse -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211817:222328:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linda Noskova (`KXWTAMATCH-26OCT01NOSRUS-NOS`) | 0.77 / 0.78 (43832) | 77.5% | -- | 64.5% | 67.8% [66.9%-70.5%] | 74.5% | 76.1% | 75.3% | KALSHI_LONE_OUTLIER | PASS | -9.7 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Elena-Gabriela Ruse (`KXWTAMATCH-26OCT01NOSRUS-RUS`) | 0.22 / 0.23 (995) | 22.5% | -- | 35.5% | 32.2% [29.5%-33.1%] | 25.5% | 23.9% | 24.7% | KALSHI_LONE_OUTLIER | SHADOW_BET | +9.7 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4568.0, B 4254.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0182
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.018, surface_dev_loose +0.009, surface_dev_tight -0.004
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01NOSRUS-16` Over 15.5 games: 0.47/0.95 mid 71.0%, model 97.0% (market_conditioned_v1 (model4_board_v1)) -- gap +26.0 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01NOSRUS-21` Over 20.5 games: 0.50/0.53 mid 51.5%, model 63.3% (market_conditioned_v1 (model4_board_v1)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01NOSRUS-26` Over 25.5 games: 0.12/0.58 mid 35.0%, model 40.0% (market_conditioned_v1 (model4_board_v1)) -- gap +5.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kyoka Okamura vs Emerson Jones -- WTA 125K Jingshan QF

WTA125 (WTA_125) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211846:263644:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emerson Jones (`KXWTACHALLENGERMATCH-26OCT01OKAJON-JON`) | 0.78 / 0.81 (3570) | 79.5% | -- | 80.4% | 77.7% [73.3%-80.0%] | -- | 78.6% | -- | INSUFFICIENT_INPUTS | PASS | -1.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kyoka Okamura (`KXWTACHALLENGERMATCH-26OCT01OKAJON-OKA`) | 0.20 / 0.21 (14) | 20.5% | -- | 19.6% | 22.3% [20.0%-26.7%] | -- | 21.5% | -- | INSUFFICIENT_INPUTS | PASS | +1.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2971.0, B 3547.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0335
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Jelena Ostapenko vs Paula Badosa -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211533:211651:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Paula Badosa (`KXWTAMATCH-26OCT01OSTBAD-BAD`) | 0.61 / 0.62 (6755) | 61.5% | -- | 63.5% | 62.0% [57.9%-63.0%] | -- | -- | -- | -- | PASS | +0.5 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jelena Ostapenko (`KXWTAMATCH-26OCT01OSTBAD-OST`) | 0.38 / 0.39 (1323) | 38.5% | -- | 36.5% | 38.0% [37.0%-42.1%] | -- | -- | -- | -- | PASS | -0.5 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3919.0, B 3479.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0255
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.010
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE

## Jasmine Paolini vs Daria Snigur -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211148:220750:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jasmine Paolini (`KXWTAMATCH-26OCT01PAOSNI-PAO`) | 0.58 / 0.59 (3953) | 58.5% | -- | 23.2% | 33.5% [27.4%-53.7%] | 59.4% | 59.4% | 59.4% | MODEL_LONE_OUTLIER | PASS | -25.0 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Daria Snigur (`KXWTAMATCH-26OCT01PAOSNI-SNI`) | 0.40 / 0.41 (92) | 40.5% | -- | 76.8% | 66.5% [46.3%-72.6%] | 40.6% | 40.5% | 40.6% | MODEL_LONE_OUTLIER | WATCH | +26.0 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4852.0, B 4190.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1314
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01PAOSNI-SNI  (YES = Daria Snigur)
Model: 67%
Kalshi: 40%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.019, surface_dev_loose -0.024, surface_dev_tight +0.029
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01PAOSNI-22` Over 21.5 games: 0.48/0.49 mid 48.5%, model 61.5% (market_conditioned_v1 (model4_board_v1)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01PAOSNI-27` Over 26.5 games: 0.23/0.32 mid 27.5%, model 38.2% (market_conditioned_v1 (model4_board_v1)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01PAOSNI-17` Over 16.5 games: 0.81/0.94 mid 87.5%, model 92.8% (market_conditioned_v1 (model4_board_v1)) -- gap +5.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Anastasia Potapova vs Sinja Kraus -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215713:221257:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sinja Kraus (`KXWTAMATCH-26OCT01POTKRA-KRA`) | 0.25 / 0.26 (926) | 25.5% | -- | 54.2% | 45.8% [35.5%-49.5%] | 26.7% | 26.5% | 26.5% | MODEL_LONE_OUTLIER | WATCH | +20.3 pp | HIGH_REVIEW | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Anastasia Potapova (`KXWTAMATCH-26OCT01POTKRA-POT`) | 0.73 / 0.75 (25008) | 74.0% | -- | 45.8% | 54.2% [50.5%-64.5%] | 73.4% | 73.8% | 73.8% | MODEL_LONE_OUTLIER | PASS | -19.8 pp | HIGH_REVIEW | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4594.0, B 5054.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.07
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01POTKRA-KRA  (YES = Sinja Kraus)
Model: 46%
Kalshi: 26%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.016
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01POTKRA-15` Over 14.5 games: 0.02/0.99 mid 50.5%, model 98.2% (market_conditioned_v1 (model4_board_v1)) -- gap +47.7 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01POTKRA-25` Over 24.5 games: 0.27/0.35 mid 31.0%, model 42.9% (market_conditioned_v1 (model4_board_v1)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01POTKRA-20` Over 19.5 games: 0.55/0.57 mid 56.0%, model 67.8% (market_conditioned_v1 (model4_board_v1)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Taylah Preston vs Diane Parry -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220348:223194:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diane Parry (`KXWTAMATCH-26OCT01PREPAR-PAR`) | 0.56 / 0.57 (3906) | 56.5% | -- | 19.4% | 24.8% [19.7%-43.7%] | 55.6% | 56.5% | 56.1% | MODEL_LONE_OUTLIER | PASS | -31.7 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Taylah Preston (`KXWTAMATCH-26OCT01PREPAR-PRE`) | 0.42 / 0.43 (300) | 42.5% | -- | 80.7% | 75.2% [56.3%-80.3%] | 44.4% | 43.5% | 44.0% | MODEL_LONE_OUTLIER | WATCH | +32.7 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5098.0, B 3742.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1199
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01PREPAR-PRE  (YES = Taylah Preston)
Model: 75%
Kalshi: 42%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.043, surface_pool_high +0.040, surface_dev_loose +0.012, surface_dev_tight -0.012
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01PREPAR-23` Over 22.5 games: 0.46/0.47 mid 46.5%, model 56.6% (market_conditioned_v1 (model4_board_v1)) -- gap +10.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01PREPAR-28` Over 27.5 games: 0.21/0.32 mid 26.5%, model 35.3% (market_conditioned_v1 (model4_board_v1)) -- gap +8.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01PREPAR-18` Over 17.5 games: 0.76/0.87 mid 81.5%, model 88.8% (market_conditioned_v1 (model4_board_v1)) -- gap +7.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Kamilla Rakhimova vs Leylah Fernandez -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215872:220367:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leylah Fernandez (`KXWTAMATCH-26OCT01RAKFER-FER`) | 0.76 / 0.77 (8279) | 76.5% | -- | 66.3% | 67.7% [65.8%-68.7%] | -- | -- | -- | -- | PASS | -8.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kamilla Rakhimova (`KXWTAMATCH-26OCT01RAKFER-RAK`) | 0.25 / 0.26 (10484) | 25.5% | -- | 33.7% | 32.3% [31.4%-34.2%] | -- | -- | -- | -- | SHADOW_BET | +6.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5718.0, B 4828.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0142
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Elena Rybakina vs Alina Charaeva -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214981:221406:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Charaeva (`KXWTAMATCH-26OCT01RYBCHA-CHA`) | 0.04 / 0.05 (6184) | 4.5% | -- | 5.3% | 5.2% [4.9%-5.9%] | -- | -- | -- | -- | PASS | +0.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Rybakina (`KXWTAMATCH-26OCT01RYBCHA-RYB`) | 0.95 / 0.96 (7135) | 95.5% | -- | 94.7% | 94.8% [94.1%-95.1%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6087.0, B 3668.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0048
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.003, surface_dev_loose -0.001, surface_dev_tight -0.003
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT01RYBCHA-23` Over 22.5 games: 0.02/0.99 mid 50.5%, model 28.9% (market_conditioned_v1 (model4_board_v1)) -- gap -21.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01RYBCHA-18` Over 17.5 games: 0.51/0.54 mid 52.5%, model 71.3% (market_conditioned_v1 (model4_board_v1)) -- gap +18.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maria Sakkari vs Storm Hunter -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:204411:206289:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Storm Hunter (`KXWTAMATCH-26OCT01SAKHUN-HUN`) | 0.32 / 0.33 (53) | 32.5% | -- | 27.6% | 30.3% [28.0%-32.2%] | -- | -- | -- | -- | PASS | -2.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Sakkari (`KXWTAMATCH-26OCT01SAKHUN-SAK`) | 0.67 / 0.68 (4948) | 67.5% | -- | 72.4% | 69.7% [67.8%-72.0%] | -- | -- | -- | -- | PASS | +2.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3640.0, B 2089.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0207
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.019, surface_dev_loose -0.005, surface_dev_tight +0.000
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Naho Sato vs Hikaru Sato -- W35 Wagga Wagga QF

ITF (ITF) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220997:221141:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naho Sato (`KXITFWMATCH-26OCT01SATSAT2-SAT`) | 0.54 / 0.57 (1) | 55.5% | -- | 46.8% | 48.9% [47.9%-50.5%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.6 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hikaru Sato (`KXITFWMATCH-26OCT01SATSAT2-SAT2`) | 0.40 / 0.45 (1) | 42.5% | -- | 53.2% | 51.1% [49.5%-52.1%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +8.6 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1522.0, B 1807.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0133
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kanon Sawashiro vs Nagi Hanatani -- W35 Wagga Wagga QF

ITF (ITF) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211544:263905:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nagi Hanatani (`KXITFWMATCH-26OCT01SAWHAN-HAN`) | 0.15 / 0.19 (36) | 17.0% | -- | 19.5% | 36.4% [28.2%-47.3%] | -- | -- | -- | -- | WATCH | +19.4 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kanon Sawashiro (`KXITFWMATCH-26OCT01SAWHAN-SAW`) | 0.79 / 0.84 (1) | 81.5% | -- | 80.5% | 63.6% [52.7%-71.8%] | -- | -- | -- | -- | PASS | -17.9 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 827.0, B 1219.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0958
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01SAWHAN-HAN  (YES = Nagi Hanatani)
Model: 36%
Kalshi: 17%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katerina Siniakova vs Elina Svitolina -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202494:211701:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katerina Siniakova (`KXWTAMATCH-26OCT01SINSVI-SIN`) | 0.23 / 0.24 (6963) | 23.5% | -- | 29.9% | 29.0% [27.2%-29.9%] | -- | -- | -- | -- | SHADOW_BET | +5.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elina Svitolina (`KXWTAMATCH-26OCT01SINSVI-SVI`) | 0.77 / 0.78 (11435) | 77.5% | -- | 70.1% | 71.0% [70.1%-72.8%] | -- | -- | -- | -- | PASS | -6.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4278.0, B 4144.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0137
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.009, surface_dev_tight +0.004
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Clara Tauson vs Polina Kudermetova -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220704:221236:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Kudermetova (`KXWTAMATCH-26OCT01TAUKUD-KUD`) | 0.35 / 0.36 (1562) | 35.5% | -- | 32.9% | 34.3% [32.4%-40.2%] | 37.7% | 36.4% | 37.0% | MARKETS_AGREE | PASS | -1.2 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Clara Tauson (`KXWTAMATCH-26OCT01TAUKUD-TAU`) | 0.63 / 0.64 (13006) | 63.5% | -- | 67.1% | 65.7% [59.8%-67.6%] | 62.3% | 63.5% | 62.9% | MARKETS_AGREE | PASS | +2.2 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4452.0, B 4285.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0386
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.009, surface_dev_loose -0.000, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01TAUKUD-21` Over 20.5 games: 0.55/0.57 mid 56.0%, model 67.8% (market_conditioned_v1 (model4_board_v1)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TAUKUD-26` Over 25.5 games: 0.27/0.40 mid 33.5%, model 44.5% (market_conditioned_v1 (model4_board_v1)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TAUKUD-16` Over 15.5 games: 0.88/0.97 mid 92.5%, model 97.6% (market_conditioned_v1 (model4_board_v1)) -- gap +5.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Maria Timofeeva vs Naomi Osaka -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211768:221237:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naomi Osaka (`KXWTAMATCH-26OCT01TIMOSA-OSA`) | 0.77 / 0.78 (14375) | 77.5% | -- | 76.0% | 80.3% [78.0%-81.7%] | 75.5% | 77.2% | 76.4% | MODEL_LONE_OUTLIER | WATCH | +2.8 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Maria Timofeeva (`KXWTAMATCH-26OCT01TIMOSA-TIM`) | 0.22 / 0.23 (1826) | 22.5% | -- | 24.0% | 19.7% [18.3%-22.0%] | 24.5% | 23.0% | 23.8% | MODEL_LONE_OUTLIER | PASS | -2.8 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3737.0, B 2986.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0182
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.004, surface_dev_loose -0.004, surface_dev_tight +0.004
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01TIMOSA-26` Over 25.5 games: 0.20/0.30 mid 25.0%, model 38.3% (market_conditioned_v1 (model4_board_v1)) -- gap +13.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TIMOSA-21` Over 20.5 games: 0.49/0.51 mid 50.0%, model 60.9% (market_conditioned_v1 (model4_board_v1)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TIMOSA-16` Over 15.5 games: 0.84/0.97 mid 90.5%, model 95.8% (market_conditioned_v1 (model4_board_v1)) -- gap +5.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Janice Tjen vs Diana Shnaider -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:222145:223670:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diana Shnaider (`KXWTAMATCH-26OCT01TJESHN-SHN`) | 0.72 / 0.73 (40328) | 72.5% | -- | 42.4% | 47.4% [42.4%-63.2%] | 70.1% | 71.7% | 70.9% | MODEL_LONE_OUTLIER | PASS | -25.1 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Janice Tjen (`KXWTAMATCH-26OCT01TJESHN-TJE`) | 0.26 / 0.27 (915) | 26.5% | -- | 57.6% | 52.5% [36.8%-57.6%] | 29.9% | 28.8% | 29.3% | KALSHI_LONE_OUTLIER | WATCH | +26.1 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3631.0, B 4846.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1039
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01TJESHN-TJE  (YES = Janice Tjen)
Model: 53%
Kalshi: 26%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.041, surface_pool_high +0.041, surface_dev_loose -0.000, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01TJESHN-21` Over 20.5 games: 0.52/0.54 mid 53.0%, model 66.1% (market_conditioned_v1 (model4_board_v1)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TJESHN-26` Over 25.5 games: 0.26/0.34 mid 30.0%, model 42.5% (market_conditioned_v1 (model4_board_v1)) -- gap +12.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TJESHN-16` Over 15.5 games: 0.86/0.96 mid 91.0%, model 97.6% (market_conditioned_v1 (model4_board_v1)) -- gap +6.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mutsumi Uemura vs Ashleigh Simes -- W35 Wagga Wagga QF

ITF (ITF) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221929:260828:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashleigh Simes (`KXITFWMATCH-26OCT01UEMSIM-SIM`) | 0.28 / 0.31 (2) | 29.5% | -- | 74.3% | 70.7% [68.5%-74.2%] | -- | -- | -- | -- | PASS | +41.2 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mutsumi Uemura (`KXITFWMATCH-26OCT01UEMSIM-UEM`) | 0.68 / 0.71 (3) | 69.5% | -- | 25.7% | 29.3% [25.8%-31.6%] | -- | -- | -- | -- | PASS | -40.2 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 824.0, B 942.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.029
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01UEMSIM-SIM  (YES = Ashleigh Simes)
Model: 71%
Kalshi: 30%
Gap: +41 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katie Volynets vs Elise Mertens -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:210722:220465:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elise Mertens (`KXWTAMATCH-26OCT01VOLMER-MER`) | 0.53 / 0.54 (4235) | 53.5% | -- | 76.4% | 73.0% [67.9%-75.1%] | -- | -- | -- | -- | WATCH | +19.5 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katie Volynets (`KXWTAMATCH-26OCT01VOLMER-VOL`) | 0.46 / 0.47 (1880) | 46.5% | -- | 23.6% | 27.0% [24.9%-32.1%] | -- | -- | -- | -- | PASS | -19.5 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5386.0, B 3838.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0359
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01VOLMER-MER  (YES = Elise Mertens)
Model: 73%
Kalshi: 54%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, UNKNOWN
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.009, surface_dev_loose -0.009, surface_dev_tight +0.009
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01VOLMER-18` Over 17.5 games: 0.02/0.99 mid 50.5%, model 87.6% (market_conditioned_v1 (model4_board_v1)) -- gap +37.1 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01VOLMER-28` Over 27.5 games: 0.03/0.99 mid 51.0%, model 34.0% (market_conditioned_v1 (model4_board_v1)) -- gap -17.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01VOLMER-23` Over 22.5 games: 0.43/0.46 mid 44.5%, model 55.9% (market_conditioned_v1 (model4_board_v1)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dayana Yastremska vs Maja Chwalinska -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215035:216081:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maja Chwalinska (`KXWTAMATCH-26OCT01YASCHW-CHW`) | 0.60 / 0.61 (30206) | 60.5% | -- | 81.1% | 72.6% [59.0%-77.3%] | 60.9% | 60.3% | 60.6% | MODEL_LONE_OUTLIER | WATCH | +12.1 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Dayana Yastremska (`KXWTAMATCH-26OCT01YASCHW-YAS`) | 0.38 / 0.39 (15229) | 38.5% | -- | 18.9% | 27.4% [22.7%-41.0%] | 39.1% | 39.6% | 39.3% | MODEL_LONE_OUTLIER | PASS | -11.1 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4632.0, B 3543.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0914
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.022, surface_dev_tight +0.027
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01YASCHW-22` Over 21.5 games: 0.48/0.49 mid 48.5%, model 60.9% (market_conditioned_v1 (model4_board_v1)) -- gap +12.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01YASCHW-27` Over 26.5 games: 0.24/0.30 mid 27.0%, model 37.7% (market_conditioned_v1 (model4_board_v1)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01YASCHW-17` Over 16.5 games: 0.79/0.90 mid 84.5%, model 92.4% (market_conditioned_v1 (model4_board_v1)) -- gap +7.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Yue Yuan vs Mirra Andreeva -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:206294:259799:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mirra Andreeva (`KXWTAMATCH-26OCT01YUAAND-AND`) | 0.92 / 0.93 (9498) | 92.5% | -- | 89.4% | 87.9% [85.1%-88.9%] | 91.3% | 92.2% | 91.8% | MODEL_LONE_OUTLIER | PASS | -4.6 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Yue Yuan (`KXWTAMATCH-26OCT01YUAAND-YUA`) | 0.08 / 0.09 (23005) | 8.5% | -- | 10.6% | 12.1% [11.1%-14.9%] | 8.7% | 8.0% | 8.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.6 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4806.0, B 4895.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0192
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.014, surface_dev_loose -0.005, surface_dev_tight +0.008
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT01YUAAND-19` Over 18.5 games: 0.43/0.44 mid 43.5%, model 61.0% (market_conditioned_v1 (model4_board_v1)) -- gap +17.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01YUAAND-24` Over 23.5 games: 0.05/0.58 mid 31.5%, model 30.6% (market_conditioned_v1 (model4_board_v1)) -- gap -0.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Renata Zarazua vs Aryna Sabalenka -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213887:214544:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aryna Sabalenka (`KXWTAMATCH-26OCT01ZARSAB-SAB`) | 0.96 / 0.97 (17456) | 96.5% | -- | 95.1% | 95.1% [94.2%-95.5%] | 94.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.4 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Renata Zarazua (`KXWTAMATCH-26OCT01ZARSAB-ZAR`) | 0.03 / 0.04 (11827) | 3.5% | -- | 4.9% | 4.9% [4.5%-5.8%] | 5.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.4 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4923.0, B 5768.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0064
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.003, surface_dev_loose -0.002, surface_dev_tight +0.004
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT01ZARSAB-22` Over 21.5 games: 0.11/0.21 mid 16.0%, model 29.7% (market_conditioned_v1 (model4_board_v1)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01ZARSAB-17` Over 16.5 games: 0.62/0.63 mid 62.5%, model 75.5% (market_conditioned_v1 (model4_board_v1)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Qinwen Zheng vs Anna Kalinskaya -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214939:221012:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Kalinskaya (`KXWTAMATCH-26OCT01ZHEKAL-KAL`) | 0.38 / 0.39 (511) | 38.5% | -- | 35.8% | 37.8% [35.8%-40.2%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Qinwen Zheng (`KXWTAMATCH-26OCT01ZHEKAL-ZHE`) | 0.61 / 0.63 (10821) | 62.0% | -- | 64.2% | 62.2% [59.8%-64.2%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3151.0, B 4015.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0217
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01ZHEKAL-18` Over 17.5 games: 0.03/0.95 mid 49.0%, model 89.3% (market_conditioned_v1 (model4_board_v1)) -- gap +40.3 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01ZHEKAL-28` Over 27.5 games: 0.03/0.99 mid 51.0%, model 35.6% (market_conditioned_v1 (model4_board_v1)) -- gap -15.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01ZHEKAL-23` Over 22.5 games: 0.44/0.47 mid 45.5%, model 56.5% (market_conditioned_v1 (model4_board_v1)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arakawa / Tse vs Di Tommaso / Simes -- W35 Wagga Wagga SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01ARATSEDITSIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arakawa / Tse (`KXITFWDOUBLES-26OCT01ARATSEDITSIM-ARATSE`) | 0.07 / 0.94 (160) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Di Tommaso / Simes (`KXITFWDOUBLES-26OCT01ARATSEDITSIM-DITSIM`) | 0.06 / 0.17 (30) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Caroline Dolehide vs Kate Fakih -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-02T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214452:261278:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caroline Dolehide (`KXITFWMATCH-26OCT01DOLFAK-DOL`) | 0.85 / 0.86 (3) | 85.5% | -- | 88.0% | 87.5% [84.8%-89.7%] | -- | -- | -- | -- | PASS | +2.0 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kate Fakih (`KXITFWMATCH-26OCT01DOLFAK-FAK`) | 0.13 / 0.15 (3530) | 14.0% | -- | 12.0% | 12.5% [10.3%-15.2%] | -- | -- | -- | -- | PASS | -1.5 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3771.0, B 215.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0244
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.026, surface_dev_loose +0.003, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aliona Falei vs Sara Sorribes Tormo -- WTA 125K Jingshan QF

WTA125 (WTA_125) · Hard · scheduled 2026-10-02T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:204427:221434:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aliona Falei (`KXWTACHALLENGERMATCH-26OCT02FALSOR-FAL`) | 0.41 / 0.43 (3107) | 42.0% | -- | 80.8% | 71.4% [54.8%-77.0%] | -- | 40.4% | -- | INSUFFICIENT_INPUTS | WATCH | +29.4 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sara Sorribes Tormo (`KXWTACHALLENGERMATCH-26OCT02FALSOR-SOR`) | 0.57 / 0.59 (74) | 58.0% | -- | 19.2% | 28.6% [23.0%-45.2%] | -- | 59.6% | -- | INSUFFICIENT_INPUTS | PASS | -29.4 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3528.0, B 3334.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1109
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT02FALSOR-FAL  (YES = Aliona Falei)
Model: 71%
Kalshi: 42%
Gap: +29 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.013, surface_dev_loose +0.022, surface_dev_tight -0.028
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## David Stevenson / Marcus Willis vs Hugo Nys / Edouard Roger-Vasselin -- ATP Tokyo R16

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-02T07:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02STEWILNYSROG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Nys / Edouard Roger-Vasselin (`KXATPDOUBLES-26OCT02STEWILNYSROG-NYSROG`) | 0.66 / 0.69 (1356) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| David Stevenson / Marcus Willis (`KXATPDOUBLES-26OCT02STEWILNYSROG-STEWIL`) | 0.31 / 0.34 (873) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Nino Ehrenschneider vs Taisei Ichikawa -- M15 Luan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207383:209510:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nino Ehrenschneider (`KXITFMATCH-26OCT01EHRICH-EHR`) | 0.68 / 0.71 (1) | 69.5% | -- | 59.1% | 57.6% [56.6%-58.6%] | -- | -- | -- | -- | PASS | -11.9 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Taisei Ichikawa (`KXITFMATCH-26OCT01EHRICH-ICH`) | 0.29 / 0.32 (88) | 30.5% | -- | 40.9% | 42.4% [41.4%-43.4%] | -- | -- | -- | -- | WATCH | +11.9 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3879.0, B 3136.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.01
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ryuki Matsuda vs Kosuke Ogura -- M15 Luan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202124:207987:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryuki Matsuda (`KXITFMATCH-26OCT01MATOGU-MAT`) | 0.62 / 0.65 (2) | 63.5% | -- | 41.7% | 46.9% [44.3%-52.1%] | -- | -- | -- | -- | PASS | -16.6 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kosuke Ogura (`KXITFMATCH-26OCT01MATOGU-OGU`) | 0.34 / 0.38 (41) | 36.0% | -- | 58.3% | 53.1% [47.9%-55.7%] | -- | -- | -- | -- | WATCH | +17.1 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3092.0, B 3515.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0389
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01MATOGU-OGU  (YES = Kosuke Ogura)
Model: 53%
Kalshi: 36%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.015, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kai-i Wang vs Isaac Becroft -- M15 Luan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208653:212459:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isaac Becroft (`KXITFMATCH-26OCT01WANBEC-BEC`) | 0.73 / 0.79 (2) | 76.0% | -- | 63.8% | 70.5% [69.1%-72.1%] | -- | -- | -- | -- | PASS | -5.5 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kai-i Wang (`KXITFMATCH-26OCT01WANBEC-WAN`) | 0.20 / 0.24 (33) | 22.0% | -- | 36.1% | 29.5% [27.9%-30.9%] | -- | -- | -- | -- | PASS | +7.5 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 553.0, B 1967.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0151
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Taiyo Yamanaka vs Max Purcell -- M15 Luan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:126845:208277:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Purcell (`KXITFMATCH-26OCT01YAMPUR-PUR`) | 0.89 / 0.92 (130) | 90.5% | -- | 79.1% | 87.7% [85.0%-89.9%] | -- | -- | -- | -- | PASS | -2.8 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Taiyo Yamanaka (`KXITFMATCH-26OCT01YAMPUR-YAM`) | 0.08 / 0.09 (38) | 8.5% | -- | 20.9% | 12.3% [10.1%-15.0%] | -- | -- | -- | -- | WATCH | +3.8 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2646.0, B 1721.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0245
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alex Bolt vs Dane Sweeny -- ATP Challenger Jingshan QF

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106109:208013:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Bolt (`KXATPCHALLENGERMATCH-26OCT02BOLSWE-BOL`) | 0.39 / 0.44 (3250) | 41.5% | -- | 46.5% | 48.0% [44.5%-54.0%] | -- | -- | -- | -- | WATCH | +6.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dane Sweeny (`KXATPCHALLENGERMATCH-26OCT02BOLSWE-SWE`) | 0.56 / 0.61 (3250) | 58.5% | -- | 53.5% | 52.0% [46.0%-55.5%] | -- | -- | -- | -- | PASS | -6.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5430.0, B 5839.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0476
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.035, surface_dev_loose -0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Lloyd Harris vs Andre Ilagan -- ATP Challenger Jingshan QF

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:144750:210318:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lloyd Harris (`KXATPCHALLENGERMATCH-26OCT02HARILA-HAR`) | 0.74 / 0.81 (750) | 77.5% | -- | 66.3% | 70.3% [68.5%-72.9%] | -- | -- | -- | -- | PASS | -7.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andre Ilagan (`KXATPCHALLENGERMATCH-26OCT02HARILA-ILA`) | 0.19 / 0.28 (250) | 23.5% | -- | 33.7% | 29.7% [27.2%-31.4%] | -- | -- | -- | -- | PASS | +6.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4129.0, B 5539.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0215
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Eva Marie Desvignes vs Zijun Jiang -- W15 Maanshan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:223214:261082:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eva Marie Desvignes (`KXITFWMATCH-26OCT01DESJIA-DES`) | 0.55 / 0.58 (144) | 56.5% | -- | 22.1% | 31.6% [28.4%-33.5%] | -- | -- | -- | -- | PASS | -24.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zijun Jiang (`KXITFWMATCH-26OCT01DESJIA-JIA`) | 0.41 / 0.45 (3196) | 43.0% | -- | 77.9% | 68.4% [66.5%-71.6%] | -- | -- | -- | -- | PASS | +25.4 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1379.0, B 178.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0252
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01DESJIA-JIA  (YES = Zijun Jiang)
Model: 68%
Kalshi: 43%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.019, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ha Eum Lee vs Ke Ren -- W15 Maanshan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:260621:270449:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ha Eum Lee (`KXITFWMATCH-26OCT01LEEREN-LEE`) | 0.86 / 0.89 (2) | 87.5% | -- | 73.0% | 69.4% [67.5%-72.1%] | -- | -- | -- | -- | PASS | -18.1 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ke Ren (`KXITFWMATCH-26OCT01LEEREN-REN`) | 0.11 / 0.14 (3228) | 12.5% | -- | 27.0% | 30.6% [27.9%-32.5%] | -- | -- | -- | -- | PASS | +18.1 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1048.0, B 366.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0232
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01LEEREN-REN  (YES = Ke Ren)
Model: 31%
Kalshi: 12%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.009, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xi Luo vs Ha Yoon Son -- W15 Maanshan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:260607:264069:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xi Luo (`KXITFWMATCH-26OCT01LUOSON-LUO`) | 0.75 / 0.78 (3563) | 76.5% | -- | 80.8% | 77.3% [76.5%-79.7%] | -- | -- | -- | -- | PASS | +0.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ha Yoon Son (`KXITFWMATCH-26OCT01LUOSON-SON`) | 0.22 / 0.24 (960) | 23.0% | -- | 19.2% | 22.7% [20.3%-23.5%] | -- | -- | -- | -- | PASS | -0.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 827.0, B 90.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.016
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.016, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stevens / Thompson vs Kitahara / Wen Wan -- W35 Wagga Wagga SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01STETHOKITWEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kitahara / Wen Wan (`KXITFWDOUBLES-26OCT01STETHOKITWEN-KITWEN`) | 0.07 / 0.42 (43) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stevens / Thompson (`KXITFWDOUBLES-26OCT01STETHOKITWEN-STETHO`) | 0.07 / 0.76 (104) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Yingqun Sun vs Jiayu Xu -- W15 Maanshan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222606:264029:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yingqun Sun (`KXITFWMATCH-26OCT01SUNXUX-SUN`) | 0.72 / 0.75 (4217) | 73.5% | -- | 78.4% | 64.5% [58.5%-69.8%] | -- | -- | -- | -- | PASS | -9.0 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiayu Xu (`KXITFWMATCH-26OCT01SUNXUX-XUX`) | 0.26 / 0.29 (3318) | 27.5% | -- | 21.6% | 35.5% [30.2%-41.5%] | -- | -- | -- | -- | WATCH | +8.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1826.0, B 444.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0568
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose +0.015, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## HSUN LIN / Yang vs SUN / Wang -- M15 Luan SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T10:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02HSUYANSUNWAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HSUN LIN / Yang (`KXITFDOUBLES-26OCT02HSUYANSUNWAN-HSUYAN`) | 0.06 / 0.94 (160) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| SUN / Wang (`KXITFDOUBLES-26OCT02HSUYANSUNWAN-SUNWAN`) | 0.06 / 0.85 (100) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Maximo Gonzalez / Andres Molteni vs Alexander Bublik / Juncheng Shang -- ATP Beijing QF

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-02T10:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02GONMOLBUBSHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Bublik / Juncheng Shang (`KXATPDOUBLES-26OCT02GONMOLBUBSHA-BUBSHA`) | 0.40 / 0.42 (108) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maximo Gonzalez / Andres Molteni (`KXATPDOUBLES-26OCT02GONMOLBUBSHA-GONMOL`) | 0.55 / 0.61 (200) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Yi Chen / Luo vs Choi / Suvirdjonkova -- W15 Maanshan SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02YICLUOCHOSUV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Choi / Suvirdjonkova (`KXITFWDOUBLES-26OCT02YICLUOCHOSUV-CHOSUV`) | 0.06 / 0.50 (52) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yi Chen / Luo (`KXITFWDOUBLES-26OCT02YICLUOCHOSUV-YICLUO`) | 0.06 / 0.71 (89) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Yi Liu / Sun vs Chen / Tang -- W15 Maanshan SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02YILSUNCHETAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chen / Tang (`KXITFWDOUBLES-26OCT02YILSUNCHETAN-CHETAN`) | 0.06 / 0.52 (54) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yi Liu / Sun (`KXITFWDOUBLES-26OCT02YILSUNCHETAN-YILSUN`) | 0.06 / 0.69 (83) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Casey Hoole vs Colin Sinclair -- M25 Darwin QF

ITF (ITF) · Hard · scheduled 2026-10-02T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:124040:211315:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Casey Hoole (`KXITFMATCH-26OCT02HOOSIN-HOO`) | 0.51 / 0.59 (100) | 55.0% | -- | 46.6% | 43.2% [36.4%-49.0%] | -- | -- | -- | -- | PASS | -11.8 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Colin Sinclair (`KXITFMATCH-26OCT02HOOSIN-SIN`) | 0.40 / 0.44 (55) | 42.0% | -- | 53.4% | 56.8% [51.0%-63.6%] | -- | -- | -- | -- | PASS | +14.8 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 187.0, B 4093.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0631
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.057, surface_pool_high +0.058, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Philip Sekulic vs Herman Hoeyeraal -- M25 Darwin QF

ITF (ITF) · Hard · scheduled 2026-10-02T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208382:210340:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Herman Hoeyeraal (`KXITFMATCH-26OCT02SEKHOE-HOE`) | 0.15 / 0.19 (27) | 17.0% | -- | 31.7% | 26.2% [24.4%-28.6%] | -- | -- | -- | -- | WATCH | +9.2 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Philip Sekulic (`KXITFMATCH-26OCT02SEKHOE-SEK`) | 0.79 / 0.83 (2) | 81.0% | -- | 68.3% | 73.9% [71.4%-75.6%] | -- | -- | -- | -- | PASS | -7.2 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4539.0, B 1869.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.021
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.008, surface_dev_loose -0.008, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arda Azkara vs Digvijay Pratap Singh -- M15 Baku QF

ITF (ITF) · surface ? · scheduled 2026-10-02T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200014:207907:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arda Azkara (`KXITFMATCH-26OCT02AZKSIN-AZK`) | 0.50 / 0.55 (101) | 52.5% | -- | 55.4% | 57.8% [56.8%-58.4%] | -- | -- | -- | -- | WATCH | +5.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Digvijay Pratap Singh (`KXITFMATCH-26OCT02AZKSIN-SIN`) | 0.45 / 0.49 (151) | 47.0% | -- | 44.6% | 42.2% [41.6%-43.2%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1821.0, B 2204.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0076
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matic Dimic vs Dmitry Popko -- M15 Telavi SF

ITF (ITF) · Clay · scheduled 2026-10-02T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:122078:210174:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matic Dimic (`KXITFMATCH-26OCT02DIMPOP-DIM`) | 0.05 / 0.15 (35) | 10.0% | -- | 17.0% | 7.4% [4.9%-9.6%] | -- | -- | -- | -- | PASS | -2.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Dmitry Popko (`KXITFMATCH-26OCT02DIMPOP-POP`) | 0.09 / 0.90 (5) | 49.5% | -- | 83.0% | 92.6% [90.4%-95.2%] | -- | -- | -- | -- | PASS | +43.1 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 459.0, B 4384.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0239
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02DIMPOP-POP  (YES = Dmitry Popko)
Model: 93%
Kalshi: 50%
Gap: +43 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.022, surface_dev_loose -0.004, surface_dev_tight +0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Millen Hurrion vs Louis Larue -- M15 Baku QF

ITF (ITF) · surface ? · scheduled 2026-10-02T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209140:211646:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Millen Hurrion (`KXITFMATCH-26OCT02HURLAR-HUR`) | 0.47 / 0.90 (5) | 68.5% | -- | 82.2% | 80.1% [76.4%-82.9%] | -- | -- | -- | -- | PASS | +11.6 pp | REVIEW | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Louis Larue (`KXITFMATCH-26OCT02HURLAR-LAR`) | 0.05 / 0.15 (36) | 10.0% | -- | 17.8% | 19.9% [17.1%-23.5%] | -- | -- | -- | -- | PASS | +9.9 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 3153.0, B 1681.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0323
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dragos Nicolae Madaras vs Stijn Paardekooper -- M15 Telavi SF

ITF (ITF) · Clay · scheduled 2026-10-02T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200096:212311:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dragos Nicolae Madaras (`KXITFMATCH-26OCT02MADPAA-MAD`) | 0.05 / 0.83 (152) | 44.0% | -- | 93.2% | 89.5% [85.3%-92.1%] | -- | -- | -- | -- | PASS | +45.5 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Stijn Paardekooper (`KXITFMATCH-26OCT02MADPAA-PAA`) | 0.10 / 0.37 (39) | 23.5% | -- | 6.8% | 10.5% [7.9%-14.7%] | -- | -- | -- | -- | PASS | -13.0 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1481.0, B 1300.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0339
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02MADPAA-MAD  (YES = Dragos Nicolae Madaras)
Model: 90%
Kalshi: 44%
Gap: +46 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nannelli / Seleznev vs Mishkin / Shvets -- M15 Telavi F

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02NANSELMISSHV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mishkin / Shvets (`KXITFDOUBLES-26OCT02NANSELMISSHV-MISSHV`) | 0.06 / 0.66 (75) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nannelli / Seleznev (`KXITFDOUBLES-26OCT02NANSELMISSHV-NANSEL`) | 0.06 / 0.55 (57) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Marcus Walters vs James Connel -- M15 Baku QF

ITF (ITF) · surface ? · scheduled 2026-10-02T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:126971:212250:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Connel (`KXITFMATCH-26OCT02WALCON-CON`) | 0.71 / 0.74 (23) | 72.5% | -- | 62.6% | 63.5% [62.6%-64.5%] | -- | -- | -- | -- | PASS | -9.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marcus Walters (`KXITFMATCH-26OCT02WALCON-WAL`) | 0.25 / 0.29 (1) | 27.0% | -- | 37.4% | 36.5% [35.5%-37.4%] | -- | -- | -- | -- | WATCH | +9.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2102.0, B 868.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0096
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Scott Jones vs Hayden Jones -- M25 Darwin QF

ITF (ITF) · Hard · scheduled 2026-10-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:206921:210436:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Scott Jones (`KXITFMATCH-26OCT02JONJON2-JON`) | 0.49 / 0.50 (3575) | 49.5% | -- | 72.8% | 66.5% [60.2%-69.3%] | -- | -- | -- | -- | WATCH | +17.0 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hayden Jones (`KXITFMATCH-26OCT02JONJON2-JON2`) | 0.49 / 0.50 (50) | 49.5% | -- | 27.2% | 33.5% [30.7%-39.8%] | -- | -- | -- | -- | PASS | -16.0 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1787.0, B 1969.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0455
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02JONJON2-JON  (YES = Scott Jones)
Model: 67%
Kalshi: 50%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.009, surface_dev_loose +0.001, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Derek Pham vs Jake Delaney -- M25 Darwin QF

ITF (ITF) · Hard · scheduled 2026-10-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:117359:210613:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Delaney (`KXITFMATCH-26OCT02PHADEL-DEL`) | 0.61 / 0.66 (1) | 63.5% | -- | 72.7% | 69.7% [69.0%-71.3%] | -- | -- | -- | -- | PASS | +6.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Derek Pham (`KXITFMATCH-26OCT02PHADEL-PHA`) | 0.32 / 0.33 (37) | 32.5% | -- | 27.3% | 30.3% [28.7%-31.0%] | -- | -- | -- | -- | PASS | -2.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 178.0, B 4278.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0113
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.004, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anton Arzhankin vs Karan Singh -- M15 Sharm ElSheikh QF

ITF (ITF) · Hard · scheduled 2026-10-02T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210000:213996:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anton Arzhankin (`KXITFMATCH-26OCT02ARZSIN-ARZ`) | 0.26 / 0.59 (6) | 42.5% | -- | 75.6% | 67.7% [57.5%-72.3%] | -- | -- | -- | -- | PASS | +25.2 pp | EXTREME (DATA_WARNING) | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Karan Singh (`KXITFMATCH-26OCT02ARZSIN-SIN`) | 0.43 / 0.67 (34) | 55.0% | -- | 24.4% | 32.3% [27.7%-42.5%] | -- | -- | -- | -- | PASS | -22.7 pp | HIGH_REVIEW | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1841.0, B 3601.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0743
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02ARZSIN-ARZ  (YES = Anton Arzhankin)
Model: 68%
Kalshi: 42%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.004, surface_dev_loose +0.021, surface_dev_tight -0.027
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Volodymyr Iakubenko vs Kerem Yilmaz -- M15 Baku QF

ITF (ITF) · surface ? · scheduled 2026-10-02T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:212030:212246:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Volodymyr Iakubenko (`KXITFMATCH-26OCT02IAKYIL-IAK`) | 0.45 / 0.51 (3209) | 48.0% | -- | 60.2% | 59.2% [58.7%-60.7%] | -- | -- | -- | -- | WATCH | +11.2 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kerem Yilmaz (`KXITFMATCH-26OCT02IAKYIL-YIL`) | 0.49 / 0.54 (3105) | 51.5% | -- | 39.8% | 40.8% [39.3%-41.3%] | -- | -- | -- | -- | PASS | -10.7 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1553.0, B 1537.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0099
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Paul Jubb vs Amr Elsayed -- M15 Sharm ElSheikh QF

ITF (ITF) · surface ? · scheduled 2026-10-02T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02JUBELS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amr Elsayed (`KXITFMATCH-26OCT02JUBELS-ELS`) | 0.11 / 0.23 (32) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Paul Jubb (`KXITFMATCH-26OCT02JUBELS-JUB`) | 0.68 / 0.89 (100) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Robert Strombachs vs Michal Krajci -- M15 Sharm ElSheikh QF

ITF (ITF) · Hard · scheduled 2026-10-02T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207669:211756:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michal Krajci (`KXITFMATCH-26OCT02STRKRA-KRA`) | 0.28 / 0.44 (45) | 36.0% | -- | 30.3% | 31.2% [29.9%-32.1%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Robert Strombachs (`KXITFMATCH-26OCT02STRKRA-STR`) | 0.49 / 0.69 (3275) | 59.0% | -- | 69.7% | 68.8% [67.9%-70.1%] | -- | -- | -- | -- | PASS | +9.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3812.0, B 3305.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.011
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.009, surface_dev_loose +0.009, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aleshchev / Dolzhenkov vs Delicata / Stamatopoulos -- M15 Baku SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02ALEDOLDELSTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleshchev / Dolzhenkov (`KXITFDOUBLES-26OCT02ALEDOLDELSTA-ALEDOL`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Delicata / Stamatopoulos (`KXITFDOUBLES-26OCT02ALEDOLDELSTA-DELSTA`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Astrid Wanja Brune Olsen vs Felitsata Dorofeeva-Rybas -- W15 Varna QF

ITF (ITF) · Clay · scheduled 2026-10-02T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214934:267022:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Astrid Wanja Brune Olsen (`KXITFWMATCH-26OCT02BRUDOR-BRU`) | 0.11 / 0.18 (0) | 14.5% | -- | 37.9% | 38.9% [37.9%-39.9%] | -- | -- | -- | -- | PASS | +24.4 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Felitsata Dorofeeva-Rybas (`KXITFWMATCH-26OCT02BRUDOR-DOR`) | 0.82 / 0.89 (21) | 85.5% | -- | 62.2% | 61.1% [60.1%-62.1%] | -- | -- | -- | -- | PASS | -24.4 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1262.0, B 923.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0103
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02BRUDOR-BRU  (YES = Astrid Wanja Brune Olsen)
Model: 39%
Kalshi: 14%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valeria Garnevska vs Sapfo Sakellaridi -- W15 Varna QF

ITF (ITF) · Clay · scheduled 2026-10-02T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220364:270109:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valeria Garnevska (`KXITFWMATCH-26OCT02GARSAK-GAR`) | 0.14 / 0.54 (3000) | 34.0% | -- | 10.1% | 16.2% [14.9%-17.2%] | -- | -- | -- | -- | PASS | -17.8 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sapfo Sakellaridi (`KXITFWMATCH-26OCT02GARSAK-SAK`) | 0.46 / 0.86 (0) | 66.0% | -- | 89.9% | 83.8% [82.8%-85.1%] | -- | -- | -- | -- | PASS | +17.8 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 149.0, B 4165.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0112
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02GARSAK-SAK  (YES = Sapfo Sakellaridi)
Model: 84%
Kalshi: 66%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.010, surface_dev_loose -0.003, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabi Adrian Boitan vs Florian Broska -- M25 Slobozia QF

ITF (ITF) · surface ? · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02BOIBRO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabi Adrian Boitan (`KXITFMATCH-26OCT02BOIBRO-BOI`) | 0.22 / 0.47 (47) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Florian Broska (`KXITFMATCH-26OCT02BOIBRO-BRO`) | 0.41 / 0.62 (30) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Castagnola / Orlando Fellin vs Lorusso / Senn -- M15 Sharm ElSheikh SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02CASORLLORSEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Castagnola / Orlando Fellin (`KXITFDOUBLES-26OCT02CASORLLORSEN-CASORL`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lorusso / Senn (`KXITFDOUBLES-26OCT02CASORLLORSEN-LORSEN`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Sebastian Gima vs Jannik Opitz -- M25 Slobozia QF

ITF (ITF) · Clay · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200457:209142:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Gima (`KXITFMATCH-26OCT02GIMOPI-GIM`) | 0.21 / 0.61 (129) | 41.0% | -- | 60.5% | 69.4% [67.1%-72.2%] | -- | -- | -- | -- | PASS | +28.4 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Jannik Opitz (`KXITFMATCH-26OCT02GIMOPI-OPI`) | 0.29 / 0.42 (43) | 35.5% | -- | 39.5% | 30.6% [27.8%-32.9%] | -- | -- | -- | -- | PASS | -4.9 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 3345.0, B 858.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0256
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02GIMOPI-GIM  (YES = Sebastian Gima)
Model: 69%
Kalshi: 41%
Gap: +28 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.004, surface_dev_loose +0.012, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Houkes vs Alec Beckley -- M25 Kigali QF

ITF (ITF) · Clay · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208069:209278:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alec Beckley (`KXITFMATCH-26OCT02HOUBEC-BEC`) | 0.07 / 0.18 (30) | 12.5% | -- | 30.7% | 28.4% [26.7%-29.3%] | -- | -- | -- | -- | PASS | +15.9 pp | HIGH_REVIEW (DATA_WARNING) | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Max Houkes (`KXITFMATCH-26OCT02HOUBEC-HOU`) | 0.18 / 0.89 (3) | 53.5% | -- | 69.3% | 71.6% [70.7%-73.3%] | -- | -- | -- | -- | PASS | +18.1 pp | HIGH_REVIEW (DATA_WARNING) | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 5070.0, B 3000.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0131
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02HOUBEC-BEC  (YES = Alec Beckley)
Model: 28%
Kalshi: 12%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02HOUBEC-HOU  (YES = Max Houkes)
Model: 72%
Kalshi: 54%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, EVENT_MAPPING_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.017, surface_dev_loose +0.013, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hrazdil / Lanik vs Arzhankin / Kunitsyn -- M15 Sharm ElSheikh SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02HRALANARZKUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arzhankin / Kunitsyn (`KXITFDOUBLES-26OCT02HRALANARZKUN-ARZKUN`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hrazdil / Lanik (`KXITFDOUBLES-26OCT02HRALANARZKUN-HRALAN`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Hubert Hurkacz vs Arthur Gea -- ATP Beijing R16

ATP (MASTERS_1000) · Hard · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:128034:210338:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Gea (`KXATPMATCH-26OCT02HURGEA-GEA`) | 0.42 / 0.43 (4207) | 42.5% | -- | 47.1% | 41.7% [34.6%-45.1%] | 43.4% | -- | 43.4% | MODEL_LONE_OUTLIER | PASS | -0.8 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Hubert Hurkacz (`KXATPMATCH-26OCT02HURGEA-HUR`) | 0.57 / 0.58 (525) | 57.5% | -- | 52.9% | 58.3% [54.9%-65.3%] | 56.6% | -- | 56.6% | MODEL_LONE_OUTLIER | PASS | +0.8 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4552.0, B 5606.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0524
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.024, surface_dev_loose -0.034, surface_dev_tight +0.038
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT02HURGEA-23` Over 22.5 games: 0.52/0.53 mid 52.5%, model 63.1% (market_conditioned_v1 (model4_board_v1)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02HURGEA-28` Over 27.5 games: 0.28/0.38 mid 33.0%, model 42.5% (market_conditioned_v1 (model4_board_v1)) -- gap +9.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02HURGEA-HUR6` Will Hubert Hurkacz win at least 5.5 more games than Arthur Gea?: 0.02/0.30 mid 16.0%, model 9.1% (market_conditioned_v1 (model4_board_v1)) -- gap -6.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02HURGEA-HUR21` Will Hubert Hurkacz win the Hubert Hurkacz vs Arthur Gea match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 27.2% (market_conditioned_v1 (model4_board_v1)) -- gap +5.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02HURGEA-GEA21` Will Arthur Gea win the Hubert Hurkacz vs Arthur Gea match by a set score of 2-1?: 0.16/0.20 mid 18.0%, model 22.3% (market_conditioned_v1 (model4_board_v1)) -- gap +4.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02HURGEA-HUR3` Will Hubert Hurkacz win at least 2.5 more games than Arthur Gea?: 0.44/0.46 mid 45.0%, model 41.2% (market_conditioned_v1 (model4_board_v1)) -- gap -3.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02HURGEA-18` Over 17.5 games: 0.89/0.94 mid 91.5%, model 95.0% (market_conditioned_v1 (model4_board_v1)) -- gap +3.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02HURGEA-HUR20` Will Hubert Hurkacz win the Hubert Hurkacz vs Arthur Gea match by a set score of 2-0?: 0.31/0.36 mid 33.5%, model 30.2% (market_conditioned_v1 (model4_board_v1)) -- gap -3.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02HURGEA-GEA20` Will Arthur Gea win the Hubert Hurkacz vs Arthur Gea match by a set score of 2-0?: 0.22/0.25 mid 23.5%, model 20.3% (market_conditioned_v1 (model4_board_v1)) -- gap -3.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02HURGEA-GEA2` Will Arthur Gea win at least 1.5 more games than Hubert Hurkacz?: 0.34/0.40 mid 37.0%, model 34.9% (market_conditioned_v1 (model4_board_v1)) -- gap -2.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Filip Cristian Jianu vs Radu David Turcanu -- M25 Slobozia QF

ITF (ITF) · Clay · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202262:212886:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Cristian Jianu (`KXITFMATCH-26OCT02JIATUR-JIA`) | 0.21 / 0.64 (27) | 42.5% | -- | 70.0% | 69.6% [69.1%-70.5%] | -- | -- | -- | -- | PASS | +27.1 pp | EXTREME (DATA_WARNING) | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Radu David Turcanu (`KXITFMATCH-26OCT02JIATUR-TUR`) | 0.18 / 0.40 (42) | 29.0% | -- | 30.0% | 30.4% [29.5%-30.9%] | -- | -- | -- | -- | PASS | +1.4 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 5523.0, B 2393.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0068
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02JIATUR-JIA  (YES = Filip Cristian Jianu)
Model: 70%
Kalshi: 42%
Gap: +27 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, EVENT_MAPPING_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.005, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Filip Krolo vs Noah Lopez -- M15 Sibenik QF

ITF (ITF) · Clay · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210055:212593:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Krolo (`KXITFMATCH-26OCT02KROLOP-KRO`) | 0.37 / 0.46 (46) | 41.5% | -- | 33.8% | 36.7% [33.3%-40.3%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Noah Lopez (`KXITFMATCH-26OCT02KROLOP-LOP`) | 0.28 / 0.63 (5) | 45.5% | -- | 66.2% | 63.3% [59.7%-66.7%] | -- | -- | -- | -- | PASS | +17.8 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 442.0, B 1139.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0347
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02KROLOP-LOP  (YES = Noah Lopez)
Model: 63%
Kalshi: 46%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikita Mashtakov vs Jeffrey Von Der Schulenburg -- M15 Sibenik QF

ITF (ITF) · surface ? · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02MASVON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikita Mashtakov (`KXITFMATCH-26OCT02MASVON-MAS`) | 0.08 / 0.73 (17) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeffrey Von Der Schulenburg (`KXITFMATCH-26OCT02MASVON-VON`) | 0.06 / 0.47 (47) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jakub Nicod vs Charles Bertimon -- M15 Sibenik QF

ITF (ITF) · Clay · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202293:210556:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charles Bertimon (`KXITFMATCH-26OCT02NICBER-BER`) | 0.05 / 0.30 (35) | 17.5% | -- | 5.3% | 8.3% [6.7%-11.0%] | -- | -- | -- | -- | PASS | -9.2 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Jakub Nicod (`KXITFMATCH-26OCT02NICBER-NIC`) | 0.05 / 0.90 (5) | 47.5% | -- | 94.7% | 91.7% [89.0%-93.3%] | -- | -- | -- | -- | PASS | +44.2 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1919.0, B 976.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0219
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02NICBER-NIC  (YES = Jakub Nicod)
Model: 92%
Kalshi: 48%
Gap: +44 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.017, surface_dev_loose +0.006, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Manuel Plunger vs Benjamin Lock -- M25 Kigali QF

ITF (ITF) · Clay · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:111761:211708:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Lock (`KXITFMATCH-26OCT02PLULOC-LOC`) | 0.06 / 0.89 (3) | 47.5% | -- | 77.9% | 77.5% [73.5%-81.2%] | -- | -- | -- | -- | PASS | +30.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manuel Plunger (`KXITFMATCH-26OCT02PLULOC-PLU`) | 0.06 / 0.89 (3) | 47.5% | -- | 22.1% | 22.5% [18.9%-26.5%] | -- | -- | -- | -- | PASS | -25.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 330.0, B 4430.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0383
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02PLULOC-LOC  (YES = Benjamin Lock)
Model: 78%
Kalshi: 48%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.036, surface_pool_high +0.040, surface_dev_loose -0.004, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fares Zakaria vs Romain Faucon -- M15 Sharm ElSheikh QF

ITF (ITF) · surface ? · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02ZAKFAU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romain Faucon (`KXITFMATCH-26OCT02ZAKFAU-FAU`) | 0.40 / 0.63 (37) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fares Zakaria (`KXITFMATCH-26OCT02ZAKFAU-ZAK`) | 0.27 / 0.60 (37) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cadence Brace vs Amandine Hesse -- W35 Baza QF

ITF (ITF) · Hard · scheduled 2026-10-02T14:15:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:203281:223335:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cadence Brace (`KXITFWMATCH-26OCT02BRAHES-BRA`) | 0.07 / 0.94 (17) | 50.5% | -- | 70.0% | 65.6% [56.4%-70.4%] | -- | -- | -- | -- | PASS | +15.2 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amandine Hesse (`KXITFWMATCH-26OCT02BRAHES-HES`) | 0.06 / 0.93 (0) | 49.5% | -- | 30.0% | 34.4% [29.6%-43.6%] | -- | -- | -- | -- | PASS | -15.2 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2165.0, B 2021.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0702
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02BRAHES-BRA  (YES = Cadence Brace)
Model: 66%
Kalshi: 50%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.024, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentina Ryser vs Charo Esquiva Banuls -- W35 Baza QF

ITF (ITF) · Hard · scheduled 2026-10-02T14:15:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220489:264962:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charo Esquiva Banuls (`KXITFWMATCH-26OCT02RYSESQ-ESQ`) | 0.06 / 0.94 (14) | 50.0% | -- | 33.5% | 31.6% [27.9%-34.5%] | -- | -- | -- | -- | PASS | -18.4 pp | HIGH_REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentina Ryser (`KXITFWMATCH-26OCT02RYSESQ-RYS`) | 0.06 / 0.94 (14) | 50.0% | -- | 66.5% | 68.4% [65.5%-72.1%] | -- | -- | -- | -- | PASS | +18.4 pp | HIGH_REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3017.0, B 1005.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.033
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02RYSESQ-RYS  (YES = Valentina Ryser)
Model: 68%
Kalshi: 50%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.028, surface_pool_high -0.029, surface_dev_loose +0.005, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bulte / Talic vs Beale / Vujic -- M25 Darwin SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02BULTALBEAVUJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beale / Vujic (`KXITFDOUBLES-26OCT02BULTALBEAVUJ-BEAVUJ`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bulte / Talic (`KXITFDOUBLES-26OCT02BULTALBEAVUJ-BULTAL`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Connel / Walters vs Bessonov / Gretskiy -- M15 Baku SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02CONWALBESGRE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bessonov / Gretskiy (`KXITFDOUBLES-26OCT02CONWALBESGRE-BESGRE`) | 0.06 / 0.40 (41) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Connel / Walters (`KXITFDOUBLES-26OCT02CONWALBESGRE-CONWAL`) | 0.06 / 0.81 (136) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Cook / Leonard Sach vs Hoeyeraal / Padgham -- M25 Darwin SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02COOLEOHOEPAD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cook / Leonard Sach (`KXITFDOUBLES-26OCT02COOLEOHOEPAD-COOLEO`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hoeyeraal / Padgham (`KXITFDOUBLES-26OCT02COOLEOHOEPAD-HOEPAD`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Tuncay Duran vs Jack Loge -- M15 Monastir QF

ITF (ITF) · Hard · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210513:211504:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tuncay Duran (`KXITFMATCH-26OCT02DURLOG-DUR`) | 0.30 / 0.62 (67) | 46.0% | -- | 61.1% | 56.1% [46.9%-61.1%] | -- | -- | -- | -- | PASS | +10.1 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jack Loge (`KXITFMATCH-26OCT02DURLOG-LOG`) | 0.29 / 0.64 (2) | 46.5% | -- | 38.9% | 43.9% [38.9%-53.1%] | -- | -- | -- | -- | PASS | -2.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2317.0, B 3866.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0706
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.040, surface_dev_loose +0.015, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kris van Wyk vs Liam Branger -- M15 Monastir QF

ITF (ITF) · Hard · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:144748:210605:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liam Branger (`KXITFMATCH-26OCT02VANBRA-BRA`) | 0.58 / 0.79 (4) | 68.5% | -- | 77.3% | 62.7% [56.7%-67.5%] | -- | -- | -- | -- | PASS | -5.8 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kris van Wyk (`KXITFMATCH-26OCT02VANBRA-VAN`) | 0.05 / 0.42 (3000) | 23.5% | -- | 22.7% | 37.3% [32.5%-43.3%] | -- | -- | -- | -- | PASS | +13.8 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2787.0, B 1201.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0538
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.030, surface_dev_loose -0.010, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Polina Berezina vs Sophia Biolay -- W15 Monastir QF

ITF (ITF) · Hard · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221192:269754:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Berezina (`KXITFWMATCH-26OCT02BERBIO-BER`) | 0.05 / 0.95 (194) | 50.0% | -- | 7.7% | 36.4% [33.4%-38.4%] | -- | -- | -- | -- | PASS | -13.6 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sophia Biolay (`KXITFWMATCH-26OCT02BERBIO-BIO`) | 0.05 / 0.95 (142) | 50.0% | -- | 92.3% | 63.6% [61.6%-66.6%] | -- | -- | -- | -- | PASS | +13.6 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 71.0, B 766.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.025
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.020, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lan Mi vs Jessica Hinojosa Gomez -- W15 Monastir QF

ITF (ITF) · Hard · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:213739:260141:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jessica Hinojosa Gomez (`KXITFWMATCH-26OCT02MIXHIN-HIN`) | 0.05 / 0.95 (164) | 50.0% | -- | 34.8% | 34.4% [32.4%-36.8%] | -- | -- | -- | -- | PASS | -15.7 pp | HIGH_REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lan Mi (`KXITFWMATCH-26OCT02MIXHIN-MIX`) | 0.05 / 0.95 (142) | 50.0% | -- | 65.2% | 65.6% [63.2%-67.6%] | -- | -- | -- | -- | PASS | +15.7 pp | HIGH_REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2699.0, B 1620.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0222
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02MIXHIN-MIX  (YES = Lan Mi)
Model: 66%
Kalshi: 50%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.019, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giulia Safina Popa vs Oana Georgeta Simion -- W15 Varna QF

ITF (ITF) · Clay · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211646:267428:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giulia Safina Popa (`KXITFWMATCH-26OCT02POPSIM-POP`) | 0.43 / 0.77 (0) | 60.0% | -- | 67.1% | 59.0% [53.7%-62.6%] | -- | -- | -- | -- | PASS | -1.0 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oana Georgeta Simion (`KXITFWMATCH-26OCT02POPSIM-SIM`) | 0.23 / 0.57 (3000) | 40.0% | -- | 32.9% | 41.0% [37.4%-46.3%] | -- | -- | -- | -- | PASS | +1.0 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1013.0, B 1762.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0444
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose +0.016, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marta Soriano Santiago vs Astrid Cirotte -- W15 Monastir QF

ITF (ITF) · Hard · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:236980:259105:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Astrid Cirotte (`KXITFWMATCH-26OCT02SORCIR-CIR`) | 0.05 / 0.95 (164) | 50.0% | -- | 43.1% | 45.2% [43.6%-46.8%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marta Soriano Santiago (`KXITFWMATCH-26OCT02SORCIR-SOR`) | 0.05 / 0.95 (142) | 50.0% | -- | 56.9% | 54.8% [53.2%-56.4%] | -- | -- | -- | -- | PASS | +4.8 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1358.0, B 2379.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0158
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.005, surface_dev_loose +0.016, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tara Wuerth vs Sonja Zhenikhova -- W15 Varna QF

ITF (ITF) · surface ? · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02WUEZHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tara Wuerth (`KXITFWMATCH-26OCT02WUEZHE-WUE`) | 0.64 / 0.79 (0) | 71.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sonja Zhenikhova (`KXITFWMATCH-26OCT02WUEZHE-ZHE`) | 0.21 / 0.36 (0) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dev Javia vs Calvin Hemery -- M25 Kigali QF

ITF (ITF) · Clay · scheduled 2026-10-02T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:123921:209956:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Calvin Hemery (`KXITFMATCH-26OCT02JAVHEM-HEM`) | 0.08 / 0.93 (5) | 50.5% | -- | 67.5% | 76.4% [73.2%-83.6%] | -- | -- | -- | -- | PASS | +25.9 pp | EXTREME (DATA_WARNING) | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dev Javia (`KXITFMATCH-26OCT02JAVHEM-JAV`) | 0.08 / 0.93 (5) | 50.5% | -- | 32.5% | 23.6% [16.4%-26.8%] | -- | -- | -- | -- | PASS | -26.9 pp | EXTREME (DATA_WARNING) | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2032.0, B 5909.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.052
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02JAVHEM-HEM  (YES = Calvin Hemery)
Model: 76%
Kalshi: 50%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.016, surface_dev_loose +0.012, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yshai Oliel vs Florent Bax -- M25 Kigali QF

ITF (ITF) · Clay · scheduled 2026-10-02T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200075:202147:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florent Bax (`KXITFMATCH-26OCT02OLIBAX-BAX`) | 0.06 / 0.94 (25) | 50.0% | -- | 93.6% | 79.2% [68.3%-85.8%] | -- | -- | -- | -- | PASS | +29.2 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Yshai Oliel (`KXITFMATCH-26OCT02OLIBAX-OLI`) | 0.06 / 0.33 (37) | 19.5% | -- | 6.4% | 20.8% [14.2%-31.7%] | -- | -- | -- | -- | PASS | +1.3 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 932.0, B 4639.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0875
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02OLIBAX-BAX  (YES = Florent Bax)
Model: 79%
Kalshi: 50%
Gap: +29 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.007, surface_dev_loose -0.014, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Borys Zgola vs Radu Mihai Papoe -- M25 Slobozia QF

ITF (ITF) · Clay · scheduled 2026-10-02T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208457:210169:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Radu Mihai Papoe (`KXITFMATCH-26OCT02ZGOPAP-PAP`) | 0.05 / 0.95 (81) | 50.0% | -- | 92.8% | 93.7% [91.9%-94.7%] | -- | -- | -- | -- | PASS | +43.7 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Borys Zgola (`KXITFMATCH-26OCT02ZGOPAP-ZGO`) | 0.05 / 0.95 (81) | 50.0% | -- | 7.1% | 6.3% [5.3%-8.1%] | -- | -- | -- | -- | PASS | -43.7 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 63.0, B 3052.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0143
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02ZGOPAP-PAP  (YES = Radu Mihai Papoe)
Model: 94%
Kalshi: 50%
Gap: +44 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.018, surface_dev_loose -0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alicia Dudeney vs Katie Swan -- W75 Quinta do Lago QF

ITF (ITF) · Hard · scheduled 2026-10-02T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215042:260206:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alicia Dudeney (`KXITFWMATCH-26OCT02DUDSWA-DUD`) | 0.06 / 0.94 (25) | 50.0% | -- | 57.8% | 51.6% [43.2%-54.7%] | -- | -- | -- | -- | PASS | +1.6 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katie Swan (`KXITFWMATCH-26OCT02DUDSWA-SWA`) | 0.06 / 0.94 (25) | 50.0% | -- | 42.2% | 48.4% [45.3%-56.8%] | -- | -- | -- | -- | PASS | -1.6 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3238.0, B 2343.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0577
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose +0.011, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sada Nahimana vs Diana Martynov -- W35 Reims QF

ITF (ITF) · Hard · scheduled 2026-10-02T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216367:221157:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diana Martynov (`KXITFWMATCH-26OCT02NAHMAR-MAR`) | 0.10 / 0.78 (25) | 44.0% | -- | 48.9% | 44.7% [40.5%-47.9%] | -- | -- | -- | -- | PASS | +0.7 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sada Nahimana (`KXITFWMATCH-26OCT02NAHMAR-NAH`) | 0.10 / 0.78 (25) | 44.0% | -- | 51.1% | 55.3% [52.1%-59.5%] | -- | -- | -- | -- | PASS | +11.3 pp | REVIEW | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2636.0, B 1861.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0368
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.005, surface_dev_loose -0.032, surface_dev_tight +0.032
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Margaux Rouvroy vs Susan Bandecchi -- W75 Quinta do Lago QF

ITF (ITF) · Hard · scheduled 2026-10-02T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214826:221191:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Susan Bandecchi (`KXITFWMATCH-26OCT02ROUBAN-BAN`) | 0.05 / 0.95 (81) | 50.0% | -- | 49.5% | 53.7% [50.5%-62.5%] | -- | -- | -- | -- | PASS | +3.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Margaux Rouvroy (`KXITFWMATCH-26OCT02ROUBAN-ROU`) | 0.05 / 0.95 (111) | 50.0% | -- | 50.5% | 46.3% [37.5%-49.5%] | -- | -- | -- | -- | PASS | -3.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3212.0, B 3884.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0599
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
