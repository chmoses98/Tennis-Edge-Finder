# ASSISTED SLATE -- 2026-10-01T13:55Z (`SL-20261001T135518Z-35bae44f`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

218 open matches not seen started, 721 markets. Skipped: {"first_ball_already_observed": 14, "scheduled_start_over_24h_past": 2, "no_match_winner_listed": 1}. Sources: shadow board 2026-10-01T13:51:43.225758+00:00, Model 4 2026-10-01T13:52:19.302541+00:00, Gen-1 ledger 2026-10-01T13:51:40.442967+00:00, external 2026-10-01T13:01:31.464710+00:00, capture 20261001T125654Z.quotes.jsonl.gz.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 55, "HIGH_REVIEW": 47, "NORMAL": 214, "REVIEW": 83, "UNPRICED": 322}; match winners: {"EXTREME": 54, "HIGH_REVIEW": 43, "NORMAL": 131, "REVIEW": 41, "UNPRICED": 167}; quote freshness at build: {"STALE": 399}.

## Alexander Ikenna Okonkwo / Preston Stearns vs Reid Jarvis / Jack Vance -- ATP Challenger Columbus R16

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-09-30T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26SEP30OKOSTEJARVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reid Jarvis / Jack Vance (`KXATPCHALLENGERDOUBLES-26SEP30OKOSTEJARVAN-JARVAN`) | 0.01 / 0.05 (2) | 3.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Ikenna Okonkwo / Preston Stearns (`KXATPCHALLENGERDOUBLES-26SEP30OKOSTEJARVAN-OKOSTE`) | 0.96 / 0.99 (279) | 97.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Andre Ilagan vs Marat Sharipov -- ATP Challenger Jingshan R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T07:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:129911:210318:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andre Ilagan (`KXATPCHALLENGERMATCH-26OCT01ILASHA-ILA`) | 0.25 / 0.26 (488) | 25.5% | 33.1% | 26.8% | 28.5% [26.9%-29.7%] | -- | 26.6% | 26.6% | MODEL_LONE_OUTLIER | WATCH | +3.0 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Marat Sharipov (`KXATPCHALLENGERMATCH-26OCT01ILASHA-SHA`) | 0.74 / 0.75 (35) | 74.5% | 66.9% | 73.2% | 71.5% [70.3%-73.1%] | -- | 73.3% | 73.3% | MODEL_LONE_OUTLIER | PASS | -3.0 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5539.0, B 3891.0; serve-point win A 60.9%, B 35.7%; Elo A 1608.9, B 1737.5; model uncertainty 0.0143
* Form inputs: days since last match A 9, B 17; matches on record A 236, B 317; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high -0.000, surface_dev_loose -0.016, surface_dev_tight +0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE

## Yuta Shimizu vs Bernard Tomic -- ATP Challenger Jingshan R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T07:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106071:202122:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuta Shimizu (`KXATPCHALLENGERMATCH-26OCT01SHITOM-SHI`) | 0.67 / 0.68 (173) | 67.5% | 41.8% | 37.7% | 37.7% [37.2%-39.1%] | -- | -- | -- | -- | PASS | -29.8 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Bernard Tomic (`KXATPCHALLENGERMATCH-26OCT01SHITOM-TOM`) | 0.33 / 0.36 (45) | 34.5% | 58.2% | 62.3% | 62.3% [60.9%-62.8%] | -- | -- | -- | -- | WATCH | +27.8 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4903.0, B 5940.0; serve-point win A 61.8%, B 36.6%; Elo A 1590.1, B 1667.2; model uncertainty 0.0095
* Form inputs: days since last match A 17, B 17; matches on record A 541, B 996; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01SHITOM-TOM  (YES = Bernard Tomic)
Model: 62%
Kalshi: 34%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE

## Elias Ymer vs Federico Cina -- ATP Challenger Jingshan R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T07:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:111200:210748:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Cina (`KXATPCHALLENGERMATCH-26OCT01YMECIN-CIN`) | 0.64 / 0.72 (9) | 68.0% | 58.0% | 60.4% | 60.9% [59.4%-62.3%] | -- | -- | -- | -- | PASS | -7.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elias Ymer (`KXATPCHALLENGERMATCH-26OCT01YMECIN-YME`) | 0.29 / 0.30 (5) | 29.5% | 42.0% | 39.6% | 39.1% [37.8%-40.6%] | -- | -- | -- | -- | SHADOW_BET | +9.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5409.0, B 3635.0; serve-point win A 61.8%, B 36.6%; Elo A 1618.1, B 1702.2; model uncertainty 0.0141
* Form inputs: days since last match A 9, B 5; matches on record A 1064, B 187; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.014, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lloyd Harris / Cheng-Peng Hsieh vs Nathaniel Lammons / Jackson Withrow -- ATP Challenger Jingshan QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T08:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HARHSILAMWIT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lloyd Harris / Cheng-Peng Hsieh (`KXATPCHALLENGERDOUBLES-26OCT01HARHSILAMWIT-HARHSI`) | 0.23 / 0.27 (26) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nathaniel Lammons / Jackson Withrow (`KXATPCHALLENGERDOUBLES-26OCT01HARHSILAMWIT-LAMWIT`) | 0.67 / 0.77 (501) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Ryan Seggerman / Bart Stevens vs Alex Bolt / Adam Walton -- ATP Challenger Jingshan QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T08:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01SEGSTEBOLWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Bolt / Adam Walton (`KXATPCHALLENGERDOUBLES-26OCT01SEGSTEBOLWAL-BOLWAL`) | 0.24 / 0.29 (18) | 26.5% | 91.9% | -- | -- [-----] | -- | -- | -- | -- | -- | +65.4 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Ryan Seggerman / Bart Stevens (`KXATPCHALLENGERDOUBLES-26OCT01SEGSTEBOLWAL-SEGSTE`) | 0.66 / 0.74 (84) | 70.0% | 8.1% | -- | -- [-----] | -- | -- | -- | -- | -- | -61.9 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERDOUBLES-26OCT01SEGSTEBOLWAL-BOLWAL  (YES = Alex Bolt / Adam Walton)
Model: 92%
Kalshi: 26%
Gap: +65 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Gonzalo Escobar / Niki Kaliyanda Poonacha vs Mitsuki Wei Kang Leong / Stefanos Sakellaridis -- ATP Challenger Jingshan QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T09:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01ESCKALLEOSAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gonzalo Escobar / Niki Kaliyanda Poonacha (`KXATPCHALLENGERDOUBLES-26OCT01ESCKALLEOSAK-ESCKAL`) | 0.73 / 0.83 (500) | 78.0% | 31.8% | -- | -- [-----] | -- | -- | -- | -- | -- | -46.2 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Mitsuki Wei Kang Leong / Stefanos Sakellaridis (`KXATPCHALLENGERDOUBLES-26OCT01ESCKALLEOSAK-LEOSAK`) | 0.18 / 0.24 (24) | 21.0% | 68.2% | -- | -- [-----] | -- | -- | -- | -- | -- | +47.2 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERDOUBLES-26OCT01ESCKALLEOSAK-LEOSAK  (YES = Mitsuki Wei Kang Leong / Stefanos Sakellaridis)
Model: 68%
Kalshi: 21%
Gap: +47 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Luis Carlos Alvarez Valdes / Adrian Oetzbach vs Buvaysar Gadamauri / Dimitris Sakellaridis -- ATP Challenger Bari QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T13:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01ALVAOETGADSAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Carlos Alvarez Valdes / Adrian Oetzbach (`KXATPCHALLENGERDOUBLES-26OCT01ALVAOETGADSAK-ALVAOET`) | 0.99 / -- (0) | -- | 33.1% | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | C / LIMITED | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Buvaysar Gadamauri / Dimitris Sakellaridis (`KXATPCHALLENGERDOUBLES-26OCT01ALVAOETGADSAK-GADSAK`) | -- / 0.01 (14789) | -- | 66.9% | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | C / LIMITED | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

## Juan Jose Bianchi / Kody Pearson vs Fabrizio Andaloro / Volodoymyr Uzhylovskyi -- ATP Challenger Bari QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T13:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BIAPEAANDUZV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fabrizio Andaloro / Volodoymyr Uzhylovskyi (`KXATPCHALLENGERDOUBLES-26OCT01BIAPEAANDUZV-ANDUZV`) | 0.45 / 0.50 (120) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Juan Jose Bianchi / Kody Pearson (`KXATPCHALLENGERDOUBLES-26OCT01BIAPEAANDUZV-BIAPEA`) | 0.55 / 0.89 (10) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lorenzo Giustino vs Matthew William Donald -- ATP Challenger Bari R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T13:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:105841:210054:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew William Donald (`KXATPCHALLENGERMATCH-26OCT01GIUDON-DON`) | 0.09 / 0.10 (2138) | 9.5% | 35.9% | 47.4% | 39.2% [33.8%-42.7%] | 44.6% | -- | 44.6% | KALSHI_LONE_OUTLIER | WATCH | +29.7 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Lorenzo Giustino (`KXATPCHALLENGERMATCH-26OCT01GIUDON-GIU`) | 0.90 / 0.91 (397) | 90.5% | 64.0% | 52.6% | 60.8% [57.3%-66.2%] | 55.4% | -- | 55.4% | KALSHI_LONE_OUTLIER | PASS | -29.7 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 6491.0, B 2929.0; serve-point win A 61.3%, B 41.5%; Elo A 1636.0, B 1435.7; model uncertainty 0.0445
* Form inputs: days since last match A 37, B 10; matches on record A 1390, B 205; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01GIUDON-DON  (YES = Matthew William Donald)
Model: 39%
Kalshi: 10%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE

## Filip Jeff Planinsek vs Borys Zgola -- M25 Slobozia R16

ITF (ITF) · Clay · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210169:210731:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Jeff Planinsek (`KXITFMATCH-26OCT01PLAZGO-PLA`) | -- / 0.01 (182271) | -- | 87.4% | 75.2% | 86.6% [86.0%-87.2%] | 86.7% | -- | 86.7% | KALSHI_LONE_OUTLIER | PASS | -- | UNPRICED | STALE | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Borys Zgola (`KXITFMATCH-26OCT01PLAZGO-ZGO`) | 0.99 / -- (0) | -- | 12.6% | 24.8% | 13.4% [12.8%-14.0%] | 13.3% | -- | 13.3% | KALSHI_LONE_OUTLIER | PASS | -- | UNPRICED | STALE | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 2530.0, B 63.0; serve-point win A 64.3%, B 44.5%; Elo A 1454.7, B 1118.3; model uncertainty 0.0061
* Form inputs: days since last match A 87, B 192; matches on record A 110, B 14; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giulia Safina Popa vs Beatris Spasova -- W15 Varna R16

ITF (ITF) · Clay · scheduled 2026-10-01T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221315:267428:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giulia Safina Popa (`KXITFWMATCH-26OCT01POPSPA-POP`) | 0.93 / 0.94 (6595) | 93.5% | 85.4% | 98.4% | 90.5% [85.5%-95.0%] | 93.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Beatris Spasova (`KXITFWMATCH-26OCT01POPSPA-SPA`) | 0.06 / 0.07 (8427) | 6.5% | 14.6% | 1.6% | 9.5% [5.0%-14.5%] | 6.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1013.0, B 520.0; serve-point win A 58.0%, B 50.0%; Elo A 1546.3, B 1239.2; model uncertainty 0.0476
* Form inputs: days since last match A 367, B 213; matches on record A 38, B 195; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.000, surface_dev_loose +0.017, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Edas Butvilas vs Moez Echargui -- ATP Challenger Porto 2 R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T14:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:121411:210220:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edas Butvilas (`KXATPCHALLENGERMATCH-26OCT01BUTECH-BUT`) | 0.92 / 0.93 (3541) | 92.5% | 63.3% | 67.2% | 66.2% [65.3%-66.7%] | -- | 67.1% | 67.1% | MODEL_LONE_OUTLIER | PASS | -26.3 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Moez Echargui (`KXATPCHALLENGERMATCH-26OCT01BUTECH-ECH`) | 0.07 / 0.08 (26677) | 7.5% | 36.7% | 32.9% | 33.8% [33.3%-34.7%] | -- | 32.8% | 32.8% | MODEL_LONE_OUTLIER | WATCH | +26.3 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 5196.0, B 5190.0; serve-point win A 63.9%, B 38.8%; Elo A 1695.1, B 1598.1; model uncertainty 0.007
* Form inputs: days since last match A 10, B 10; matches on record A 293, B 704; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01BUTECH-ECH  (YES = Moez Echargui)
Model: 34%
Kalshi: 8%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_MODEL
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Inaki Montes-de la Torre vs Jacob Fearnley -- ATP Challenger Porto 2 R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T14:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207985:208540:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacob Fearnley (`KXATPCHALLENGERMATCH-26OCT01MONFEA-FEA`) | 0.62 / 0.63 (9747) | 62.5% | 59.3% | 45.3% | 51.6% [48.4%-55.7%] | 73.1% | 74.4% | 73.8% | MODEL_LONE_OUTLIER | PASS | -10.9 pp | REVIEW | STALE | A / ADEQUATE | ALL_DISAGREE | VERIFIED |
| Inaki Montes-de la Torre (`KXATPCHALLENGERMATCH-26OCT01MONFEA-MON`) | 0.37 / 0.38 (15949) | 37.5% | 40.7% | 54.7% | 48.4% [44.3%-51.6%] | 26.9% | 26.2% | 26.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.9 pp | REVIEW | STALE | A / ADEQUATE | ALL_DISAGREE | VERIFIED |

* Serve evidence (points): A 4378.0, B 5299.0; serve-point win A 61.7%, B 36.5%; Elo A 1650.2, B 1780.7; model uncertainty 0.0365
* Form inputs: days since last match A 17, B 29; matches on record A 245, B 234; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.005, surface_dev_loose +0.016, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Felix Balshaw vs Nicolai Budkov Kjaer -- ATP Challenger Mouilleron-Le-Captif R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T14:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:149282:213149:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Balshaw (`KXATPCHALLENGERMATCH-26OCT01BALBUD-BAL`) | 0.33 / 0.39 (161) | 36.0% | 51.9% | 64.7% | 58.0% [53.5%-60.9%] | 41.6% | 39.6% | 40.6% | MODEL_LONE_OUTLIER | WATCH | +22.0 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Nicolai Budkov Kjaer (`KXATPCHALLENGERMATCH-26OCT01BALBUD-BUD`) | 0.60 / 0.66 (268) | 63.0% | 48.1% | 35.3% | 42.0% [39.1%-46.5%] | 58.4% | 60.4% | 59.4% | MODEL_LONE_OUTLIER | PASS | -21.0 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4079.0, B 4328.0; serve-point win A 62.8%, B 37.6%; Elo A 1604.7, B 1685.3; model uncertainty 0.037
* Form inputs: days since last match A 24, B 10; matches on record A 117, B 192; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01BALBUD-BAL  (YES = Felix Balshaw)
Model: 58%
Kalshi: 36%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE; WIDE_SPREAD

## Hoeyeraal / Padgham vs Dong / Jones -- M25 Darwin QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HOEPADDONJON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dong / Jones (`KXITFDOUBLES-26OCT01HOEPADDONJON-DONJON`) | 0.25 / 0.35 (1097) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hoeyeraal / Padgham (`KXITFDOUBLES-26OCT01HOEPADDONJON-HOEPAD`) | 0.65 / 0.75 (1) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Benjamin Hassan / Skander Mansouri vs Gianluca Cadenasso / Massimo Giunta -- ATP Challenger Bari QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T14:50:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HASMANCADGIU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gianluca Cadenasso / Massimo Giunta (`KXATPCHALLENGERDOUBLES-26OCT01HASMANCADGIU-CADGIU`) | 0.37 / 0.44 (62) | 40.5% | 44.0% | -- | -- [-----] | -- | -- | -- | -- | -- | +3.5 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Benjamin Hassan / Skander Mansouri (`KXATPCHALLENGERDOUBLES-26OCT01HASMANCADGIU-HASMAN`) | 0.53 / 0.61 (32) | 57.0% | 56.0% | -- | -- [-----] | -- | -- | -- | -- | -- | -1.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Hrazdil / Lanik vs Harsh / Singh -- M15 Sharm ElSheikh QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HRALANHARSIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harsh / Singh (`KXITFDOUBLES-26OCT01HRALANHARSIN-HARSIN`) | 0.35 / 0.39 (1) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hrazdil / Lanik (`KXITFDOUBLES-26OCT01HRALANHARSIN-HRALAN`) | 0.61 / 0.65 (1) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Maximilian Neuchrist / David Poljak vs Finn Bass / Scott Duncan -- ATP Challenger Mouilleron-Le-Captif QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01NEUPOLBASDUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Finn Bass / Scott Duncan (`KXATPCHALLENGERDOUBLES-26OCT01NEUPOLBASDUN-BASDUN`) | 0.38 / 0.46 (148) | 42.0% | 11.7% | -- | -- [-----] | -- | -- | -- | -- | -- | -30.3 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maximilian Neuchrist / David Poljak (`KXATPCHALLENGERDOUBLES-26OCT01NEUPOLBASDUN-NEUPOL`) | 0.54 / 0.62 (1) | 58.0% | 88.3% | -- | -- [-----] | -- | -- | -- | -- | -- | +30.3 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERDOUBLES-26OCT01NEUPOLBASDUN-NEUPOL  (YES = Maximilian Neuchrist / David Poljak)
Model: 88%
Kalshi: 58%
Gap: +30 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mili Poljicak vs Henrique Rocha -- ATP Challenger Porto 2 R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209890:210012:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mili Poljicak (`KXATPCHALLENGERMATCH-26OCT01POLROC-POL`) | -- / 0.01 (5613) | -- | 36.2% | 43.0% | 38.1% [33.8%-40.0%] | 26.9% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | -- | UNPRICED | STALE | A / ADEQUATE | INSUFFICIENT_INPUTS | VERIFIED |
| Henrique Rocha (`KXATPCHALLENGERMATCH-26OCT01POLROC-ROC`) | 0.99 / -- (0) | -- | 63.8% | 57.0% | 61.9% [60.0%-66.2%] | 73.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | STALE | A / ADEQUATE | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 3989.0, B 5037.0; serve-point win A 61.2%, B 36.0%; Elo A 1548.4, B 1721.6; model uncertainty 0.0311
* Form inputs: days since last match A 24, B 24; matches on record A 306, B 353; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.004, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

## Maddalena Giordano vs Ksenia Smirnova -- W15 Sharm ElSheikh R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220642:269968:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maddalena Giordano (`KXITFWMATCH-26OCT01GIOSMI-GIO`) | 0.05 / 0.07 (1702) | 6.0% | 13.6% | 5.1% | 11.7% [8.0%-15.5%] | -- | -- | -- | -- | PASS | +5.7 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ksenia Smirnova (`KXITFWMATCH-26OCT01GIOSMI-SMI`) | 0.92 / 0.94 (1843) | 93.0% | 86.4% | 95.0% | 88.3% [84.5%-92.0%] | -- | -- | -- | -- | PASS | -4.7 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1760.0, B 692.0; serve-point win A 51.5%, B 40.2%; Elo A 1179.5, B 1461.8; model uncertainty 0.0373
* Form inputs: days since last match A 157, B 164; matches on record A 144, B 17; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.003, surface_dev_loose -0.010, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniel Cukierman / Fernando Romboli vs Nicolas Barrientos / Szymon Walkow -- ATP Challenger Porto 2 QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T15:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01CUKROMBARWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Barrientos / Szymon Walkow (`KXATPCHALLENGERDOUBLES-26OCT01CUKROMBARWAL-BARWAL`) | 0.34 / 0.44 (545) | 39.0% | 49.6% | -- | -- [-----] | -- | -- | -- | -- | -- | +10.6 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Daniel Cukierman / Fernando Romboli (`KXATPCHALLENGERDOUBLES-26OCT01CUKROMBARWAL-CUKROM`) | 0.56 / 0.65 (56) | 60.5% | 50.4% | -- | -- [-----] | -- | -- | -- | -- | -- | -10.1 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## August Holmgren vs Andrea Guerrieri -- ATP Challenger Porto 2 R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T15:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200416:200462:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrea Guerrieri (`KXATPCHALLENGERMATCH-26OCT01HOLGUE-GUE`) | 0.61 / 0.62 (190) | 61.5% | 58.5% | 63.1% | 61.2% [59.3%-62.6%] | 59.2% | 61.4% | 61.4% | MODEL_LONE_OUTLIER | PASS | -0.3 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| August Holmgren (`KXATPCHALLENGERMATCH-26OCT01HOLGUE-HOL`) | 0.39 / 0.40 (2465) | 39.5% | 41.5% | 36.9% | 38.8% [37.4%-40.7%] | 40.8% | 38.8% | 38.8% | MODEL_LONE_OUTLIER | PASS | -0.7 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5043.0, B 4580.0; serve-point win A 61.8%, B 36.6%; Elo A 1614.1, B 1659.3; model uncertainty 0.0164
* Form inputs: days since last match A 24, B 10; matches on record A 350, B 417; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Maxime Chazal vs Kris van Wyk -- M15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106172:144748:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxime Chazal (`KXITFMATCH-26OCT01CHAVAN-CHA`) | 0.03 / 0.04 (978) | 3.5% | 71.3% | 91.0% | 83.8% [78.1%-87.1%] | 86.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +80.3 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kris van Wyk (`KXITFMATCH-26OCT01CHAVAN-VAN`) | 0.96 / 0.97 (131) | 96.5% | 28.7% | 9.0% | 16.2% [12.9%-21.9%] | 13.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -80.3 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3315.0, B 2787.0; serve-point win A 64.8%, B 39.6%; Elo A 1400.4, B 1308.5; model uncertainty 0.0452
* Form inputs: days since last match A 10, B 122; matches on record A 869, B 330; data quality A

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01CHAVAN-CHA  (YES = Maxime Chazal)
Model: 84%
Kalshi: 4%
Gap: +80 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.024, surface_dev_loose +0.021, surface_dev_tight -0.024
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carles Hernandez vs Samir Hamza Reguig -- M15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208264:209360:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samir Hamza Reguig (`KXITFMATCH-26OCT01HERHAM-HAM`) | 0.10 / 0.11 (410) | 10.5% | 56.8% | 64.9% | 61.9% [57.3%-63.4%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +51.4 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carles Hernandez (`KXITFMATCH-26OCT01HERHAM-HER`) | 0.88 / 0.89 (3) | 88.5% | 43.2% | 35.1% | 38.1% [36.6%-42.7%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -50.4 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2103.0, B 2818.0; serve-point win A 61.9%, B 36.7%; Elo A 1251.7, B 1301.2; model uncertainty 0.0306
* Form inputs: days since last match A 136, B 24; matches on record A 85, B 216; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01HERHAM-HAM  (YES = Samir Hamza Reguig)
Model: 62%
Kalshi: 10%
Gap: +51 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose -0.010, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mak Mikovic vs Piotr Galus -- M15 Sibenik R16

ITF (ITF) · Clay · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:206893:212951:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Piotr Galus (`KXITFMATCH-26OCT01MIKGAL-GAL`) | 0.24 / 0.31 (14) | 27.5% | 48.6% | 50.5% | 48.9% [47.9%-49.5%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +21.4 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mak Mikovic (`KXITFMATCH-26OCT01MIKGAL-MIK`) | 0.68 / 0.74 (37) | 71.0% | 51.4% | 49.5% | 51.1% [50.5%-52.1%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 608.0, B 305.0; serve-point win A 60.0%, B 40.2%; Elo A 1195.3, B 1185.6; model uncertainty 0.008
* Form inputs: days since last match A 122, B 122; matches on record A 16, B 19; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01MIKGAL-GAL  (YES = Piotr Galus)
Model: 49%
Kalshi: 28%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jakub Nicod vs Samuele Seghetti -- M15 Sibenik R16

ITF (ITF) · Clay · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210556:213064:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jakub Nicod (`KXITFMATCH-26OCT01NICSEG-NIC`) | 0.82 / 0.83 (52) | 82.5% | 83.4% | 89.0% | 88.2% [86.5%-89.7%] | 78.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.7 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Samuele Seghetti (`KXITFMATCH-26OCT01NICSEG-SEG`) | 0.16 / 0.18 (200) | 17.0% | 16.6% | 11.0% | 11.8% [10.3%-13.5%] | 21.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.2 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1919.0, B 1318.0; serve-point win A 63.7%, B 43.9%; Elo A 1548.3, B 1204.3; model uncertainty 0.0157
* Form inputs: days since last match A 122, B 157; matches on record A 152, B 39; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.016, surface_dev_loose +0.011, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jeffrey Von Der Schulenburg vs Michel Hopp -- M15 Sibenik R16

ITF (ITF) · Clay · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209882:210424:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michel Hopp (`KXITFMATCH-26OCT01VONHOP-HOP`) | 0.04 / 0.06 (536) | 5.0% | 48.1% | 50.0% | 46.3% [45.3%-47.9%] | 33.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +41.3 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jeffrey Von Der Schulenburg (`KXITFMATCH-26OCT01VONHOP-VON`) | 0.94 / 0.96 (889) | 95.0% | 51.9% | 50.0% | 53.7% [52.1%-54.7%] | 67.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -41.3 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1301.0, B 2440.0; serve-point win A 60.1%, B 40.3%; Elo A 1370.3, B 1330.2; model uncertainty 0.013
* Form inputs: days since last match A 45, B 122; matches on record A 102, B 88; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01VONHOP-HOP  (YES = Michel Hopp)
Model: 46%
Kalshi: 5%
Gap: +41 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matilde Mariani vs Polina Berezina -- W15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220343:269754:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Berezina (`KXITFWMATCH-26OCT01MARBER-BER`) | 0.47 / 0.49 (729) | 48.0% | 51.1% | 53.7% | 51.1% [47.9%-55.3%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matilde Mariani (`KXITFWMATCH-26OCT01MARBER-MAR`) | 0.51 / 0.52 (226) | 51.5% | 48.9% | 46.3% | 48.9% [44.7%-52.1%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 616.0, B 71.0; serve-point win A 55.6%, B 44.2%; Elo A 1368.6, B 1376.6; model uncertainty 0.0374
* Form inputs: days since last match A 171, B 220; matches on record A 146, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.032, surface_pool_high -0.043, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lan Mi vs Ophelie Boullay -- W15 Monastir R16

ITF (ITF) · Hard · scheduled 2026-10-01T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:260141:267400:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ophelie Boullay (`KXITFWMATCH-26OCT01MIXBOU-BOU`) | 0.47 / 0.48 (1627) | 47.5% | 57.1% | 60.6% | 58.0% [55.4%-60.6%] | 30.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.5 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lan Mi (`KXITFWMATCH-26OCT01MIXBOU-MIX`) | 0.52 / 0.53 (3381) | 52.5% | 42.9% | 39.4% | 42.0% [39.4%-44.6%] | 69.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.5 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2699.0, B 774.0; serve-point win A 55.0%, B 43.6%; Elo A 1444.9, B 1486.1; model uncertainty 0.0263
* Form inputs: days since last match A 157, B 339; matches on record A 89, B 16; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.011, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ehab / El Feky vs Castagnola / Orlando Fellin -- M15 Sharm ElSheikh QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01EHAELFCASORL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Castagnola / Orlando Fellin (`KXITFDOUBLES-26OCT01EHAELFCASORL-CASORL`) | 0.86 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ehab / El Feky (`KXITFDOUBLES-26OCT01EHAELFCASORL-EHAELF`) | 0.01 / 0.04 (675) | 2.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

## Opitz / Wessels vs Broska / Schaefer -- M25 Slobozia QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01OPIWESBROSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Broska / Schaefer (`KXITFDOUBLES-26OCT01OPIWESBROSCH-BROSCH`) | 0.49 / 0.55 (12) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Opitz / Wessels (`KXITFDOUBLES-26OCT01OPIWESBROSCH-OPIWES`) | 0.45 / 0.50 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Valeria Garnevska vs Adriana Tkachenko -- W15 Varna R16

ITF (ITF) · Clay · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:263751:270109:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valeria Garnevska (`KXITFWMATCH-26OCT01GARTKA-GAR`) | 0.76 / 0.80 (24) | 78.0% | 42.0% | 22.2% | 39.4% [37.9%-41.5%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -38.6 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Adriana Tkachenko (`KXITFWMATCH-26OCT01GARTKA-TKA`) | 0.20 / 0.22 (11) | 21.0% | 58.0% | 77.8% | 60.6% [58.5%-62.1%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +39.6 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 149.0, B 1179.0; serve-point win A 53.2%, B 45.2%; Elo A 1261.3, B 1317.2; model uncertainty 0.0182
* Form inputs: days since last match A 367, B 353; matches on record A 5, B 26; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01GARTKA-TKA  (YES = Adriana Tkachenko)
Model: 61%
Kalshi: 21%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.021, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francisca Jorge vs Kylie Collins -- W75 Quinta do Lago R16

ITF (ITF) · Hard · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216055:220891:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kylie Collins (`KXITFWMATCH-26OCT01JORCOL-COL`) | 0.13 / 0.16 (186) | 14.5% | 31.2% | 29.5% | 26.4% [25.1%-27.7%] | 44.8% | -- | 44.8% | ALL_THREE_DISAGREE | PASS | +11.9 pp | REVIEW | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Francisca Jorge (`KXITFWMATCH-26OCT01JORCOL-JOR`) | 0.83 / 0.85 (2) | 84.0% | 68.8% | 70.5% | 73.6% [72.3%-74.9%] | 55.2% | -- | 55.2% | MODEL_LONE_OUTLIER | PASS | -10.4 pp | REVIEW | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 3145.0, B 2145.0; serve-point win A 57.5%, B 46.2%; Elo A 1652.2, B 1438.5; model uncertainty 0.0131
* Form inputs: days since last match A 9, B 10; matches on record A 457, B 126; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.004, surface_dev_loose +0.009, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Linda Klimovicova vs Alicia Dudeney -- W75 Quinta do Lago R16

ITF (ITF) · Hard · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221626:260206:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alicia Dudeney (`KXITFWMATCH-26OCT01KLIDUD-DUD`) | 0.83 / 0.84 (4160) | 83.5% | 55.1% | 74.0% | 63.3% [47.9%-69.5%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.1 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Linda Klimovicova (`KXITFWMATCH-26OCT01KLIDUD-KLI`) | 0.16 / 0.17 (11) | 16.5% | 44.9% | 26.0% | 36.6% [30.5%-52.1%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +20.1 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2873.0, B 3238.0; serve-point win A 55.2%, B 43.8%; Elo A 1725.3, B 1659.9; model uncertainty 0.1082
* Form inputs: days since last match A 36, B 94; matches on record A 261, B 92; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01KLIDUD-KLI  (YES = Linda Klimovicova)
Model: 37%
Kalshi: 16%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.020, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Galena Krastenova vs Oana Georgeta Simion -- W15 Varna R16

ITF (ITF) · Clay · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211646:265603:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Galena Krastenova (`KXITFWMATCH-26OCT01KRASIM-KRA`) | -- / 0.01 (1022) | -- | 19.7% | 29.1% | 20.3% [19.5%-21.8%] | 14.4% | -- | 14.4% | KALSHI_LONE_OUTLIER | PASS | -- | UNPRICED | STALE | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Oana Georgeta Simion (`KXITFWMATCH-26OCT01KRASIM-SIM`) | 0.99 / -- (0) | -- | 80.3% | 70.9% | 79.7% [78.2%-80.5%] | 85.6% | -- | 85.6% | KALSHI_LONE_OUTLIER | PASS | -- | UNPRICED | STALE | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 135.0, B 1762.0; serve-point win A 50.8%, B 42.8%; Elo A 1276.6, B 1520.4; model uncertainty 0.0116
* Form inputs: days since last match A 388, B 178; matches on record A 24, B 543; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.007, surface_dev_loose -0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Manon Leonard vs Clara Vlasselaer -- W35 Reims R16

ITF (ITF) · Hard · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215807:221003:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manon Leonard (`KXITFWMATCH-26OCT01LEOVLA-LEO`) | 0.96 / 0.97 (4294) | 96.5% | 66.5% | 69.8% | 70.2% [66.7%-71.5%] | 68.7% | -- | 68.7% | MODEL_LONE_OUTLIER | PASS | -26.3 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | AGREES_WITH_MODEL | VERIFIED |
| Clara Vlasselaer (`KXITFWMATCH-26OCT01LEOVLA-VLA`) | 0.03 / 0.04 (6386) | 3.5% | 33.5% | 30.2% | 29.8% [28.5%-33.3%] | 31.3% | -- | 31.3% | MODEL_LONE_OUTLIER | WATCH | +26.3 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 3201.0, B 1490.0; serve-point win A 57.3%, B 45.9%; Elo A 1629.8, B 1481.5; model uncertainty 0.0235
* Form inputs: days since last match A 108, B 157; matches on record A 347, B 332; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01LEOVLA-VLA  (YES = Clara Vlasselaer)
Model: 30%
Kalshi: 4%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_MODEL
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.009, surface_dev_loose +0.004, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lisa Pigato vs Adrienn Nagy -- W75 Quinta do Lago R16

ITF (ITF) · Hard · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215909:221354:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrienn Nagy (`KXITFWMATCH-26OCT01PIGNAG-NAG`) | 0.02 / 0.03 (40001) | 2.5% | 20.6% | 16.2% | 18.3% [16.6%-20.1%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +15.8 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lisa Pigato (`KXITFWMATCH-26OCT01PIGNAG-PIG`) | 0.97 / 0.98 (2283) | 97.5% | 79.4% | 83.8% | 81.7% [79.9%-83.4%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.8 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4114.0, B 1856.0; serve-point win A 58.8%, B 47.4%; Elo A 1654.6, B 1421.1; model uncertainty 0.0176
* Form inputs: days since last match A 12, B 25; matches on record A 353, B 313; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01PIGNAG-NAG  (YES = Adrienn Nagy)
Model: 18%
Kalshi: 2%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.018, surface_dev_loose +0.003, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sakellaridi / Vilar vs Veleva / Williams -- W15 Varna QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01SAKVILVELWIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sakellaridi / Vilar (`KXITFWDOUBLES-26OCT01SAKVILVELWIL-SAKVIL`) | 0.69 / 0.71 (1) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Veleva / Williams (`KXITFWDOUBLES-26OCT01SAKVILVELWIL-VELWIL`) | 0.29 / 0.31 (39) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Isabella Maria Serban vs Marie Weckerle -- W35 Reims R16

ITF (ITF) · Hard · scheduled 2026-10-01T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220946:265197:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isabella Maria Serban (`KXITFWMATCH-26OCT01SERWEC-SER`) | 0.83 / 0.85 (1) | 84.0% | 47.8% | 39.4% | 42.5% [39.9%-47.3%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -41.5 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marie Weckerle (`KXITFWMATCH-26OCT01SERWEC-WEC`) | 0.14 / 0.17 (6) | 15.5% | 52.2% | 60.6% | 57.5% [52.7%-60.1%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +42.0 pp | EXTREME (DATA_WARNING) | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2134.0, B 1952.0; serve-point win A 55.5%, B 44.1%; Elo A 1459.0, B 1478.0; model uncertainty 0.037
* Form inputs: days since last match A 8, B 157; matches on record A 114, B 223; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01SERWEC-WEC  (YES = Marie Weckerle)
Model: 57%
Kalshi: 16%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.026, surface_dev_tight +0.026
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tiago Pereira vs Hugo Grenier -- ATP Challenger Porto 2 R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T16:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:126409:211500:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Grenier (`KXATPCHALLENGERMATCH-26OCT01PERGRE-GRE`) | 0.55 / 0.56 (3171) | 55.5% | 59.2% | 45.9% | 51.0% [49.0%-57.6%] | 55.4% | 55.4% | 55.4% | MARKETS_AGREE | PASS | -4.5 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Tiago Pereira (`KXATPCHALLENGERMATCH-26OCT01PERGRE-PER`) | 0.43 / 0.45 (1429) | 44.0% | 40.8% | 54.1% | 49.0% [42.4%-51.0%] | 44.6% | 44.9% | 44.9% | MARKETS_AGREE | WATCH | +5.0 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5117.0, B 4799.0; serve-point win A 61.7%, B 36.5%; Elo A 1539.0, B 1658.2; model uncertainty 0.0432
* Form inputs: days since last match A 72, B 10; matches on record A 280, B 946; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.015, surface_dev_tight -0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Aleshchev / Dolzhenkov vs Azizov / Mert Ozdemir -- M15 Baku QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01ALEDOLAZIMER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleshchev / Dolzhenkov (`KXITFDOUBLES-26OCT01ALEDOLAZIMER-ALEDOL`) | 0.64 / 0.72 (1) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Azizov / Mert Ozdemir (`KXITFDOUBLES-26OCT01ALEDOLAZIMER-AZIMER`) | 0.28 / 0.36 (1069) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ariel Behar / Joshua Paris vs Alexander Donski / Filip Pieczonka -- ATP Challenger Porto 2 QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BEHPARDONPIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ariel Behar / Joshua Paris (`KXATPCHALLENGERDOUBLES-26OCT01BEHPARDONPIE-BEHPAR`) | 0.41 / 0.50 (50) | 45.5% | 18.7% | -- | -- [-----] | -- | -- | -- | -- | -- | -26.8 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Alexander Donski / Filip Pieczonka (`KXATPCHALLENGERDOUBLES-26OCT01BEHPARDONPIE-DONPIE`) | 0.49 / 0.58 (62) | 53.5% | 81.3% | -- | -- [-----] | -- | -- | -- | -- | -- | +27.8 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERDOUBLES-26OCT01BEHPARDONPIE-DONPIE  (YES = Alexander Donski / Filip Pieczonka)
Model: 81%
Kalshi: 54%
Gap: +28 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Pierre Delage vs Ryan Nijboer -- M25 Zaragoza R16

ITF (ITF) · Clay · scheduled 2026-10-01T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207764:208265:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pierre Delage (`KXITFMATCH-26OCT01DELNIJ-DEL`) | 0.10 / 0.13 (1) | 11.5% | 41.9% | 47.9% | 43.2% [41.1%-45.3%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +31.7 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ryan Nijboer (`KXITFMATCH-26OCT01DELNIJ-NIJ`) | 0.86 / 0.90 (181) | 88.0% | 58.1% | 52.1% | 56.8% [54.7%-58.9%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -31.2 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2897.0, B 4005.0; serve-point win A 59.1%, B 39.3%; Elo A 1385.0, B 1482.5; model uncertainty 0.0206
* Form inputs: days since last match A 108, B 10; matches on record A 215, B 484; data quality A

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01DELNIJ-DEL  (YES = Pierre Delage)
Model: 43%
Kalshi: 12%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nicolas Ifi vs Pedro Rodenas -- M25 Zaragoza R16

ITF (ITF) · Clay · scheduled 2026-10-01T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210203:212552:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Ifi (`KXITFMATCH-26OCT01IFIROD-IFI`) | 0.29 / 0.32 (1) | 30.5% | 18.5% | 12.7% | 15.5% [13.5%-19.4%] | 13.3% | -- | 13.3% | MODEL_LONE_OUTLIER | PASS | -15.0 pp | HIGH_REVIEW | STALE | C / LIMITED | AGREES_WITH_MODEL | VERIFIED |
| Pedro Rodenas (`KXITFMATCH-26OCT01IFIROD-ROD`) | 0.67 / 0.71 (232) | 69.0% | 81.5% | 87.3% | 84.5% [80.6%-86.5%] | 86.7% | -- | 86.7% | MODEL_LONE_OUTLIER | WATCH | +15.5 pp | HIGH_REVIEW | STALE | C / LIMITED | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 1923.0, B 1623.0; serve-point win A 56.4%, B 36.6%; Elo A 1239.5, B 1490.7; model uncertainty 0.0295
* Form inputs: days since last match A 129, B 311; matches on record A 78, B 98; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01IFIROD-ROD  (YES = Pedro Rodenas)
Model: 85%
Kalshi: 69%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_MODEL
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, STALE_PLAYER_DATA, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.012, surface_pool_high +0.012, surface_dev_loose -0.008, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arthur Reymond / Luca Sanchez vs Stefan Latinovic / Mili Poljicak -- ATP Challenger Porto 2 QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01REYSANLATPOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Latinovic / Mili Poljicak (`KXATPCHALLENGERDOUBLES-26OCT01REYSANLATPOL-LATPOL`) | 0.34 / 0.39 (42) | 36.5% | 77.1% | -- | -- [-----] | -- | -- | -- | -- | -- | +40.6 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Arthur Reymond / Luca Sanchez (`KXATPCHALLENGERDOUBLES-26OCT01REYSANLATPOL-REYSAN`) | 0.58 / 0.66 (77) | 62.0% | 22.9% | -- | -- [-----] | -- | -- | -- | -- | -- | -39.1 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERDOUBLES-26OCT01REYSANLATPOL-LATPOL  (YES = Stefan Latinovic / Mili Poljicak)
Model: 77%
Kalshi: 36%
Gap: +41 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Mateus Alves vs Gonzalo Villanueva -- ATP Challenger Curitiba R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106380:127123:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateus Alves (`KXATPCHALLENGERMATCH-26OCT01ALVVIL-ALV`) | 0.57 / 0.58 (16734) | 57.5% | -- | 56.1% | 53.5% [50.5%-55.6%] | 57.2% | 58.0% | 58.0% | MARKETS_AGREE | PASS | -4.0 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Gonzalo Villanueva (`KXATPCHALLENGERMATCH-26OCT01ALVVIL-VIL`) | 0.43 / 0.44 (28270) | 43.5% | -- | 43.9% | 46.5% [44.4%-49.5%] | 42.8% | 42.1% | 42.1% | MARKETS_AGREE | WATCH | +3.0 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4869.0, B 5724.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0253
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Bangargi / Chaurasia vs Beckley / Sahtali -- M25 Kigali QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BANCHABECSAH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bangargi / Chaurasia (`KXITFDOUBLES-26OCT01BANCHABECSAH-BANCHA`) | 0.05 / 0.09 (1066) | 7.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Beckley / Sahtali (`KXITFDOUBLES-26OCT01BANCHABECSAH-BECSAH`) | 0.91 / 0.95 (1097) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Brown / De Alba vs Gatoto / Shalin Shah -- M25 Kigali QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BRODEAGATSHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brown / De Alba (`KXITFDOUBLES-26OCT01BRODEAGATSHA-BRODEA`) | 0.36 / 0.41 (3) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gatoto / Shalin Shah (`KXITFDOUBLES-26OCT01BRODEAGATSHA-GATSHA`) | 0.59 / 0.64 (1) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Clement Chidekh vs Ugo Blanchet -- ATP Challenger Mouilleron-Le-Captif R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200259:206889:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ugo Blanchet (`KXATPCHALLENGERMATCH-26OCT01CHIBLA-BLA`) | 0.32 / 0.33 (646) | 32.5% | -- | 31.6% | 34.3% [31.6%-41.0%] | 35.4% | 35.9% | 35.9% | KALSHI_LONE_OUTLIER | PASS | +1.8 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Clement Chidekh (`KXATPCHALLENGERMATCH-26OCT01CHIBLA-CHI`) | 0.66 / 0.67 (8414) | 66.5% | -- | 68.4% | 65.7% [59.0%-68.4%] | 64.6% | 64.3% | 64.3% | KALSHI_LONE_OUTLIER | PASS | -0.8 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5365.0, B 4988.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0471
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.018, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Mariano Kestelboim / Marcelo Zormann vs Brandon Perez / Paulo Andre Saraiva Dos Santos -- ATP Challenger Curitiba QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01KESZORPERSAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariano Kestelboim / Marcelo Zormann (`KXATPCHALLENGERDOUBLES-26OCT01KESZORPERSAR-KESZOR`) | 0.63 / 0.74 (10) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Brandon Perez / Paulo Andre Saraiva Dos Santos (`KXATPCHALLENGERDOUBLES-26OCT01KESZORPERSAR-PERSAR`) | 0.22 / 0.37 (10) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Nefve / Schachter vs Lock / John Lock -- M25 Kigali QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01NEFSCHLOCJOH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lock / John Lock (`KXITFDOUBLES-26OCT01NEFSCHLOCJOH-LOCJOH`) | 0.28 / 0.41 (71) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nefve / Schachter (`KXITFDOUBLES-26OCT01NEFSCHLOCJOH-NEFSCH`) | 0.66 / 0.73 (1) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Van Herck / Vankan vs Denolly / Plunger -- M25 Kigali QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01VANVANDENPLU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Denolly / Plunger (`KXITFDOUBLES-26OCT01VANVANDENPLU-DENPLU`) | 0.05 / 0.69 (1) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Van Herck / Vankan (`KXITFDOUBLES-26OCT01VANVANDENPLU-VANVAN`) | 0.04 / 0.77 (1) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Akli / Brantmeier vs Da Silva Fick / Voloshchuk -- W75 Quinta do Lago SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01AKLBRADASVOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Akli / Brantmeier (`KXITFWDOUBLES-26OCT01AKLBRADASVOL-AKLBRA`) | 0.21 / 0.86 (1) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Da Silva Fick / Voloshchuk (`KXITFWDOUBLES-26OCT01AKLBRADASVOL-DASVOL`) | 0.06 / 0.74 (1) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Naiktha Bains vs Polona Hercog -- W75 Quinta do Lago R16

ITF (ITF) · Hard · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:201555:206362:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naiktha Bains (`KXITFWMATCH-26OCT01BAIHER-BAI`) | 0.39 / 0.49 (14) | 44.0% | 35.6% | 37.3% | 37.8% [36.4%-39.2%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.2 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Polona Hercog (`KXITFWMATCH-26OCT01BAIHER-HER`) | 0.47 / 0.59 (4481) | 53.0% | 64.4% | 62.7% | 62.2% [60.8%-63.6%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.2 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2400.0, B 2590.0; serve-point win A 54.3%, B 42.9%; Elo A 1567.7, B 1647.9; model uncertainty 0.0144
* Form inputs: days since last match A 7, B 10; matches on record A 482, B 863; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.011, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Im / Kim vs Nahimana / Weckerle -- W35 Reims SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01IMXKIMNAHWEC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Im / Kim (`KXITFWDOUBLES-26OCT01IMXKIMNAHWEC-IMXKIM`) | 0.02 / 0.82 (1) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nahimana / Weckerle (`KXITFWDOUBLES-26OCT01IMXKIMNAHWEC-NAHWEC`) | 0.02 / 0.76 (1) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Harmony Tan vs Eva Vedder -- W75 Quinta do Lago R16

ITF (ITF) · Hard · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211552:220770:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harmony Tan (`KXITFWMATCH-26OCT01TANVED-TAN`) | 0.59 / 0.74 (4) | 66.5% | 66.8% | 79.9% | 76.0% [69.2%-78.3%] | 60.6% | -- | 60.6% | EXTERNAL_LONE_OUTLIER | PASS | +9.5 pp | NORMAL | STALE | A / LIMITED | ALL_DISAGREE | VERIFIED |
| Eva Vedder (`KXITFWMATCH-26OCT01TANVED-VED`) | 0.23 / 0.41 (2) | 32.0% | 33.2% | 20.1% | 24.0% [21.6%-30.8%] | 39.4% | -- | 39.4% | KALSHI_LONE_OUTLIER | PASS | -8.0 pp | NORMAL | STALE | A / LIMITED | ALL_DISAGREE | VERIFIED |

* Serve evidence (points): A 3731.0, B 3271.0; serve-point win A 57.3%, B 46.0%; Elo A 1712.2, B 1586.1; model uncertainty 0.0458
* Form inputs: days since last match A 7, B 16; matches on record A 649, B 432; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.008, surface_dev_loose +0.011, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Klara Veldman vs Britt Du Pree -- W35 Reims R16

ITF (ITF) · Hard · scheduled 2026-10-01T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:223418:264228:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Britt Du Pree (`KXITFWMATCH-26OCT01VELDUP-DUP`) | 0.84 / 0.85 (2619) | 84.5% | 82.8% | 89.1% | 85.2% [81.5%-87.8%] | 86.7% | -- | 86.7% | KALSHI_LONE_OUTLIER | PASS | +0.7 pp | NORMAL | STALE | B / LIMITED | ALL_AGREE | VERIFIED |
| Klara Veldman (`KXITFWMATCH-26OCT01VELDUP-VEL`) | 0.15 / 0.16 (3) | 15.5% | 17.2% | 10.9% | 14.8% [12.2%-18.5%] | 13.3% | -- | 13.3% | KALSHI_LONE_OUTLIER | PASS | -0.7 pp | NORMAL | STALE | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1299.0, B 2691.0; serve-point win A 52.1%, B 40.7%; Elo A 1331.3, B 1580.2; model uncertainty 0.0314
* Form inputs: days since last match A 157, B 157; matches on record A 141, B 85; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.006, surface_dev_loose -0.003, surface_dev_tight +0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Romain Arneodo / Benjamin Kittay vs Alexandru Jecan / Szymon Kielan -- ATP Challenger Porto 2 QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T17:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01ARNKITJECKIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romain Arneodo / Benjamin Kittay (`KXATPCHALLENGERDOUBLES-26OCT01ARNKITJECKIE-ARNKIT`) | 0.63 / 0.71 (306) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexandru Jecan / Szymon Kielan (`KXATPCHALLENGERDOUBLES-26OCT01ARNKITJECKIE-JECKIE`) | 0.29 / 0.33 (29) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Adrian Andreescu / Claudiu Schinteie vs Ghetu / Melnic -- M25 Slobozia QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01ADRCLAGHEMEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Andreescu / Claudiu Schinteie (`KXITFDOUBLES-26OCT01ADRCLAGHEMEL-ADRCLA`) | 0.26 / 0.45 (1333) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ghetu / Melnic (`KXITFDOUBLES-26OCT01ADRCLAGHEMEL-GHEMEL`) | 0.55 / 0.74 (1516) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Pierluigi Basile vs Martin Krumich -- ATP Challenger Bari R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209322:213003:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pierluigi Basile (`KXATPCHALLENGERMATCH-26OCT01BASKRU-BAS`) | 0.39 / 0.40 (2222) | 39.5% | -- | 25.6% | 29.5% [27.8%-30.8%] | 40.1% | 39.4% | 39.7% | MODEL_LONE_OUTLIER | PASS | -10.0 pp | REVIEW | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Martin Krumich (`KXATPCHALLENGERMATCH-26OCT01BASKRU-KRU`) | 0.59 / 0.60 (3103) | 59.5% | -- | 74.4% | 70.5% [69.2%-72.2%] | 59.9% | 60.5% | 60.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +11.0 pp | REVIEW | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1898.0, B 5732.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0155
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.009, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Biletic / Kajin vs Behr / Curavic -- M15 Sibenik QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BILKAJBEHCUR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Behr / Curavic (`KXITFDOUBLES-26OCT01BILKAJBEHCUR-BEHCUR`) | 0.11 / 0.79 (1) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Biletic / Kajin (`KXITFDOUBLES-26OCT01BILKAJBEHCUR-BILKAJ`) | 0.05 / 0.84 (1) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Florin Breazu / Cristian Breazu vs Pokorny / Tsitsipas -- M25 Slobozia QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01FLOCRIPOKTSI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florin Breazu / Cristian Breazu (`KXITFDOUBLES-26OCT01FLOCRIPOKTSI-FLOCRI`) | 0.49 / 0.57 (1) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pokorny / Tsitsipas (`KXITFDOUBLES-26OCT01FLOCRIPOKTSI-POKTSI`) | 0.43 / 0.52 (52) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kuperstein / Peter Van Noord vs Jeran / Kupcic -- M15 Sibenik QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01KUPPETJERKUP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jeran / Kupcic (`KXITFDOUBLES-26OCT01KUPPETJERKUP-JERKUP`) | 0.11 / 0.81 (1) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kuperstein / Peter Van Noord (`KXITFDOUBLES-26OCT01KUPPETJERKUP-KUPPET`) | 0.04 / 0.69 (1) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mashtakov / Savano vs Chayka / Yi Qing -- M15 Sibenik QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01MASSAVCHAYIQ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chayka / Yi Qing (`KXITFDOUBLES-26OCT01MASSAVCHAYIQ-CHAYIQ`) | 0.09 / 0.13 (95) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mashtakov / Savano (`KXITFDOUBLES-26OCT01MASSAVCHAYIQ-MASSAV`) | 0.87 / 0.91 (1) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Liam Broady / Emile Hudd vs Jarno Jans / Joran Vliegen -- ATP Challenger Mouilleron-Le-Captif QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BROHUDJANVLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liam Broady / Emile Hudd (`KXATPCHALLENGERDOUBLES-26OCT01BROHUDJANVLI-BROHUD`) | 0.31 / 0.35 (35) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jarno Jans / Joran Vliegen (`KXATPCHALLENGERDOUBLES-26OCT01BROHUDJANVLI-JANVLI`) | 0.61 / 0.69 (548) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Garcia Mestre / Naharro vs Giovannini / Maria Giovannini -- M25 Zaragoza QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01GARNAHGIOMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Garcia Mestre / Naharro (`KXITFDOUBLES-26OCT01GARNAHGIOMAR-GARNAH`) | 0.05 / 0.88 (622) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Giovannini / Maria Giovannini (`KXITFDOUBLES-26OCT01GARNAHGIOMAR-GIOMAR`) | 0.13 / 0.17 (1) | 15.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lucca Cervantes Tomas / Alejandro Reyes Tirado vs Meneses Perny / Perez socas -- M25 Zaragoza QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01LUCALEMENPER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucca Cervantes Tomas / Alejandro Reyes Tirado (`KXITFDOUBLES-26OCT01LUCALEMENPER-LUCALE`) | 0.31 / 0.69 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Meneses Perny / Perez socas (`KXITFDOUBLES-26OCT01LUCALEMENPER-MENPER`) | 0.11 / 0.69 (1) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Bryce Nakashima vs Keegan Smith -- ATP Challenger Columbus R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202333:210416:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bryce Nakashima (`KXATPCHALLENGERMATCH-26OCT01NAKSMI-NAK`) | 0.42 / 0.43 (2339) | 42.5% | -- | 15.6% | 14.4% [12.8%-16.3%] | 42.8% | 43.1% | 43.1% | MODEL_LONE_OUTLIER | PASS | -28.1 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | EXTERNAL_STALE | VERIFIED |
| Keegan Smith (`KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI`) | 0.57 / 0.58 (659) | 57.5% | -- | 84.4% | 85.5% [83.7%-87.2%] | 57.2% | 56.7% | 56.7% | MODEL_LONE_OUTLIER | PASS | +28.1 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 451.0, B 5491.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0174
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI  (YES = Keegan Smith)
Model: 86%
Kalshi: 57%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: EXTERNAL_STALE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.016, surface_dev_loose -0.002, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Alexander Ikenna Okonkwo / Preston Stearns vs Alafia Ayeni / Billy Suarez -- ATP Challenger Columbus QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01OKOSTEAVESUA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alafia Ayeni / Billy Suarez (`KXATPCHALLENGERDOUBLES-26OCT01OKOSTEAVESUA-AVESUA`) | 0.57 / 0.65 (215) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Ikenna Okonkwo / Preston Stearns (`KXATPCHALLENGERDOUBLES-26OCT01OKOSTEAVESUA-OKOSTE`) | 0.35 / 0.42 (43) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Xavi Palomar vs Miguel Damas -- M25 Zaragoza R16

ITF (ITF) · Clay · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207732:214015:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miguel Damas (`KXITFMATCH-26OCT01PALDAM-DAM`) | 0.99 / -- (0) | -- | 90.2% | 93.7% | 92.6% [91.2%-94.2%] | 89.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | STALE | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Xavi Palomar (`KXITFMATCH-26OCT01PALDAM-PAL`) | -- / 0.01 (5485) | -- | 9.8% | 6.3% | 7.4% [5.8%-8.8%] | 10.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | STALE | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 617.0, B 5726.0; serve-point win A 54.9%, B 35.1%; Elo A 1160.8, B 1584.0; model uncertainty 0.0149
* Form inputs: days since last match A 164, B 24; matches on record A 12, B 410; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.004, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andrienko / Georgiana Goina vs Ksandinov / Stamatova -- W15 Varna QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01ANDGEOKSASTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrienko / Georgiana Goina (`KXITFWDOUBLES-26OCT01ANDGEOKSASTA-ANDGEO`) | 0.03 / 0.93 (400) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ksandinov / Stamatova (`KXITFWDOUBLES-26OCT01ANDGEOKSASTA-KSASTA`) | 0.12 / 0.62 (100) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Charo Esquiva Banuls vs Radka Zelnickova -- W35 Baza R16

ITF (ITF) · Hard · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222092:264962:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charo Esquiva Banuls (`KXITFWMATCH-26OCT01ESQZEL-ESQ`) | 0.91 / 0.92 (1343) | 91.5% | 40.6% | 28.1% | 35.6% [33.1%-39.0%] | 67.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -55.9 pp | EXTREME (DATA_WARNING) | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Radka Zelnickova (`KXITFWMATCH-26OCT01ESQZEL-ZEL`) | 0.08 / 0.09 (225) | 8.5% | 59.4% | 72.0% | 64.4% [61.0%-66.9%] | 33.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +55.9 pp | EXTREME (DATA_WARNING) | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1005.0, B 2730.0; serve-point win A 54.8%, B 43.4%; Elo A 1466.2, B 1530.5; model uncertainty 0.0295
* Form inputs: days since last match A 16, B 16; matches on record A 35, B 304; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01ESQZEL-ZEL  (YES = Radka Zelnickova)
Model: 64%
Kalshi: 8%
Gap: +56 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.025, surface_dev_loose -0.019, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hatouka / Zelinskaya vs Groen / Van Zonneveld -- W15 Sharm ElSheikh QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01HATZELGROVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Groen / Van Zonneveld (`KXITFWDOUBLES-26OCT01HATZELGROVAN-GROVAN`) | 0.14 / 0.31 (62) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hatouka / Zelinskaya (`KXITFWDOUBLES-26OCT01HATZELGROVAN-HATZEL`) | 0.73 / 0.86 (40) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Ilinca Burcescu / Dorofeeva-Rybas vs Elena Barbulescu / Wanja Brune Olsen -- W15 Varna QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01ILIDORELEWAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Barbulescu / Wanja Brune Olsen (`KXITFWDOUBLES-26OCT01ILIDORELEWAN-ELEWAN`) | 0.06 / 0.76 (1) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ilinca Burcescu / Dorofeeva-Rybas (`KXITFWDOUBLES-26OCT01ILIDORELEWAN-ILIDOR`) | 0.06 / 0.85 (1) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Valentina Ivanov vs Alba Maria Coromina Boluda -- W35 Baza R16

ITF (ITF) · Hard · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221173:269270:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alba Maria Coromina Boluda (`KXITFWMATCH-26OCT01IVACOR-COR`) | 0.01 / 0.02 (4666) | 1.5% | 15.0% | 11.4% | 14.4% [11.9%-16.7%] | 14.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.9 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentina Ivanov (`KXITFWMATCH-26OCT01IVACOR-IVA`) | 0.99 / -- (0) | -- | 85.0% | 88.6% | 85.5% [83.3%-88.1%] | 85.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | STALE | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 1892.0, B 174.0; serve-point win A 59.6%, B 48.2%; Elo A 1496.4, B 1195.6; model uncertainty 0.0243
* Form inputs: days since last match A 164, B 304; matches on record A 135, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.009, surface_dev_loose +0.003, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rasim / Velikova vs Mair / Peer -- W15 Varna QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01RASVELMAIPEE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mair / Peer (`KXITFWDOUBLES-26OCT01RASVELMAIPEE-MAIPEE`) | 0.03 / 0.75 (1) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rasim / Velikova (`KXITFWDOUBLES-26OCT01RASVELMAIPEE-RASVEL`) | 0.02 / 0.68 (1) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Samuel Heredia / Miguel Tobon vs Bruno (2002) Oliveira / Natan Rodrigues -- ATP Challenger Curitiba QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T18:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HERTOBOLIROD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samuel Heredia / Miguel Tobon (`KXATPCHALLENGERDOUBLES-26OCT01HERTOBOLIROD-HERTOB`) | 0.32 / 0.37 (40) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bruno (2002) Oliveira / Natan Rodrigues (`KXATPCHALLENGERDOUBLES-26OCT01HERTOBOLIROD-OLIROD`) | 0.61 / 0.68 (41) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Joao Eduardo Schiessl vs Luis Guto Miguel -- ATP Challenger Curitiba R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T18:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210214:213036:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Guto Miguel (`KXATPCHALLENGERMATCH-26OCT01SCHMIG-MIG`) | 0.80 / 0.81 (6331) | 80.5% | -- | 64.0% | 51.5% [42.9%-56.6%] | 79.2% | 79.4% | 79.2% | MODEL_LONE_OUTLIER | PASS | -29.0 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Joao Eduardo Schiessl (`KXATPCHALLENGERMATCH-26OCT01SCHMIG-SCH`) | 0.19 / 0.20 (4030) | 19.5% | -- | 36.0% | 48.5% [43.4%-57.1%] | 20.8% | 19.2% | 20.8% | MODEL_LONE_OUTLIER | WATCH | +29.0 pp | EXTREME (DATA_WARNING) | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3018.0, B 1185.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0688
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT01SCHMIG-SCH  (YES = Joao Eduardo Schiessl)
Model: 48%
Kalshi: 20%
Gap: +29 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE

## Colombo / Demanet vs Branger / Dugardin -- M15 Monastir QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01COLDEMBRADUG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Branger / Dugardin (`KXITFDOUBLES-26OCT01COLDEMBRADUG-BRADUG`) | 0.34 / 0.58 (707) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Colombo / Demanet (`KXITFDOUBLES-26OCT01COLDEMBRADUG-COLDEM`) | 0.42 / 0.66 (541) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Duran / Ouakaa vs Ali Abibsi / Dell'elba -- M15 Monastir QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01DUROUAALIDEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ali Abibsi / Dell'elba (`KXITFDOUBLES-26OCT01DUROUAALIDEL-ALIDEL`) | 0.03 / 0.79 (40) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Duran / Ouakaa (`KXITFDOUBLES-26OCT01DUROUAALIDEL-DUROUA`) | 0.13 / 0.95 (78) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Heisnam / Rathi vs Nagoudi / Piatti -- M15 Monastir QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HEIRATNAGPIA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Heisnam / Rathi (`KXITFDOUBLES-26OCT01HEIRATNAGPIA-HEIRAT`) | 0.05 / 0.27 (35) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nagoudi / Piatti (`KXITFDOUBLES-26OCT01HEIRATNAGPIA-NAGPIA`) | 0.71 / 0.80 (1001) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Knis / Vildeuil vs Lumsden / Nortey -- M15 Monastir QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01KNIVILLUMNOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Knis / Vildeuil (`KXITFDOUBLES-26OCT01KNIVILLUMNOR-KNIVIL`) | 0.04 / 0.95 (1052) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lumsden / Nortey (`KXITFDOUBLES-26OCT01KNIVILLUMNOR-LUMNOR`) | 0.06 / 0.91 (1100) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Bazderova / Belyaeva vs Biolay / Cirotte -- W15 Monastir QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01BAZBELBIOCIR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bazderova / Belyaeva (`KXITFWDOUBLES-26OCT01BAZBELBIOCIR-BAZBEL`) | 0.15 / 0.41 (43) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Biolay / Cirotte (`KXITFWDOUBLES-26OCT01BAZBELBIOCIR-BIOCIR`) | 0.58 / 0.71 (86) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Bhopal / sahnoun vs Kroitor / Mi -- W15 Monastir QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01BHOSAHKROMIX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bhopal / sahnoun (`KXITFWDOUBLES-26OCT01BHOSAHKROMIX-BHOSAH`) | 0.04 / 0.73 (1) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kroitor / Mi (`KXITFWDOUBLES-26OCT01BHOSAHKROMIX-KROMIX`) | 0.28 / 0.90 (1151) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hinojosa Gomez / Losciale vs Bertacchi / Dibenedetto -- W15 Monastir QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01HINLOSBERDIB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bertacchi / Dibenedetto (`KXITFWDOUBLES-26OCT01HINLOSBERDIB-BERDIB`) | 0.28 / 0.41 (4) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hinojosa Gomez / Losciale (`KXITFWDOUBLES-26OCT01HINLOSBERDIB-HINLOS`) | 0.50 / 0.68 (100) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Efremova / Meshcheryakova vs Favier / Sushkova -- W15 Sharm ElSheikh QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T18:45:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01EFRMESFAVSUS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Efremova / Meshcheryakova (`KXITFWDOUBLES-26OCT01EFRMESFAVSUS-EFRMES`) | 0.03 / 0.74 (1) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Favier / Sushkova (`KXITFWDOUBLES-26OCT01EFRMESFAVSUS-FAVSUS`) | 0.03 / 0.95 (169) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aidan Mayo vs Colton Smith -- ATP Challenger Columbus R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T19:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208854:212256:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aidan Mayo (`KXATPCHALLENGERMATCH-26OCT01MAYSMI-MAY`) | 0.35 / 0.36 (2428) | 35.5% | -- | 46.9% | 40.9% [38.0%-43.9%] | 38.4% | 36.8% | 36.8% | MODEL_LONE_OUTLIER | WATCH | +5.4 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Colton Smith (`KXATPCHALLENGERMATCH-26OCT01MAYSMI-SMI`) | 0.63 / 0.64 (662) | 63.5% | -- | 53.0% | 59.1% [56.1%-62.0%] | 61.6% | 63.4% | 63.4% | MARKETS_AGREE | PASS | -4.4 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3962.0, B 3806.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0297
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Abdullah Shelbayh vs Daniil Ostapenkov -- ATP Challenger Columbus R16

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-01T19:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01SHEOST:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniil Ostapenkov (`KXATPCHALLENGERMATCH-26OCT01SHEOST-OST`) | 0.24 / 0.25 (1964) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Abdullah Shelbayh (`KXATPCHALLENGERMATCH-26OCT01SHEOST-SHE`) | 0.74 / 0.75 (2798) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Guido Ivan Justo vs Pedro Sakamoto -- ATP Challenger Curitiba R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T19:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106203:207815:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guido Ivan Justo (`KXATPCHALLENGERMATCH-26OCT01JUSSAK-JUS`) | 0.68 / 0.69 (4145) | 68.5% | -- | 79.7% | 75.8% [69.8%-78.6%] | 67.7% | 69.5% | 69.5% | MARKETS_AGREE | WATCH | +7.3 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Pedro Sakamoto (`KXATPCHALLENGERMATCH-26OCT01JUSSAK-SAK`) | 0.30 / 0.31 (1449) | 30.5% | -- | 20.3% | 24.2% [21.4%-30.2%] | 32.3% | 31.1% | 31.1% | MARKETS_AGREE | PASS | -6.3 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4964.0, B 4530.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0439
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.008, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Franco Roncadelli / Gonzalo Villanueva vs Boris Arias / Ignacio Carou -- ATP Challenger Curitiba QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T19:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01RONVILARICAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boris Arias / Ignacio Carou (`KXATPCHALLENGERDOUBLES-26OCT01RONVILARICAR-ARICAR`) | 0.51 / 0.59 (195) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Franco Roncadelli / Gonzalo Villanueva (`KXATPCHALLENGERDOUBLES-26OCT01RONVILARICAR-RONVIL`) | 0.42 / 0.50 (33) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Collins / Tanguilig vs Bayerlova / Gimbrere -- W75 Quinta do Lago SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T19:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01COLTANBAYGIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bayerlova / Gimbrere (`KXITFWDOUBLES-26OCT01COLTANBAYGIM-BAYGIM`) | 0.10 / 0.71 (600) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Collins / Tanguilig (`KXITFWDOUBLES-26OCT01COLTANBAYGIM-COLTAN`) | 0.06 / 0.89 (501) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Salma Djoubri vs Amandine Monnot -- W35 Reims R16

ITF (ITF) · Hard · scheduled 2026-10-01T19:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220305:221486:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Salma Djoubri (`KXITFWMATCH-26OCT01DJOMON-DJO`) | 0.17 / 0.19 (395) | 18.0% | 26.6% | 15.7% | 25.3% [23.3%-27.1%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amandine Monnot (`KXITFWMATCH-26OCT01DJOMON-MON`) | 0.81 / 0.83 (4972) | 82.0% | 73.4% | 84.3% | 74.7% [72.9%-76.7%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 169.0, B 3095.0; serve-point win A 53.3%, B 42.0%; Elo A 1467.4, B 1643.5; model uncertainty 0.019
* Form inputs: days since last match A 318, B 25; matches on record A 168, B 272; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.000, surface_dev_loose -0.004, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carmen Gallardo Guevara vs Celia Cervino Ruiz -- W35 Baza R16

ITF (ITF) · Hard · scheduled 2026-10-01T19:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216078:222239:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Celia Cervino Ruiz (`KXITFWMATCH-26OCT01GALCER-CER`) | 0.41 / 0.42 (198) | 41.5% | 46.9% | 39.0% | 46.8% [42.1%-54.8%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +5.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carmen Gallardo Guevara (`KXITFWMATCH-26OCT01GALCER-GAL`) | 0.56 / 0.59 (2022) | 57.5% | 53.1% | 61.0% | 53.2% [45.2%-57.9%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.3 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1358.0, B 1450.0; serve-point win A 56.0%, B 44.6%; Elo A 1410.1, B 1439.1; model uncertainty 0.0635
* Form inputs: days since last match A 157, B 9; matches on record A 48, B 265; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.016, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rabl / Marlies Rothensteiner vs Abouelsaad / Wildgruber -- W15 Sharm ElSheikh QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T19:31:46Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01RABMARABOWIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abouelsaad / Wildgruber (`KXITFWDOUBLES-26OCT01RABMARABOWIL-ABOWIL`) | 0.04 / 0.54 (2) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rabl / Marlies Rothensteiner (`KXITFWDOUBLES-26OCT01RABMARABOWIL-RABMAR`) | 0.03 / 0.58 (2) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jonah Braswell vs Jordan Lee -- M15 Fayetteville AR R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:211738:214265:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonah Braswell (`KXITFMATCH-26OCT01BRALEE-BRA`) | 0.21 / 0.23 (3676) | 22.0% | 42.9% | 31.4% | 41.7% [38.6%-42.8%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +19.7 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jordan Lee (`KXITFMATCH-26OCT01BRALEE-LEE`) | 0.76 / 0.77 (108) | 76.5% | 57.1% | 68.6% | 58.3% [57.2%-61.4%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.2 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 298.0, B 252.0; serve-point win A 61.9%, B 36.7%; Elo A 1291.2, B 1341.1; model uncertainty 0.021
* Form inputs: days since last match A 318, B 36; matches on record A 17, B 8; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01BRALEE-BRA  (YES = Jonah Braswell)
Model: 42%
Kalshi: 22%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Dahlin vs Alexander Bernard -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209060:211609:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Bernard (`KXITFMATCH-26OCT01DAHBER-BER`) | 0.16 / 0.18 (4562) | 17.0% | 36.8% | 18.8% | 33.6% [28.2%-38.9%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +16.6 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Dahlin (`KXITFMATCH-26OCT01DAHBER-DAH`) | 0.81 / 0.84 (1192) | 82.5% | 63.2% | 81.2% | 66.4% [61.1%-71.8%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.1 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 583.0, B 797.0; serve-point win A 63.9%, B 38.7%; Elo A 1424.0, B 1355.4; model uncertainty 0.0536
* Form inputs: days since last match A 66, B 325; matches on record A 41, B 108; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01DAHBER-BER  (YES = Alexander Bernard)
Model: 34%
Kalshi: 17%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.005, surface_dev_loose +0.028, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## John Hallquist Lithen vs Benjamin Azar -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208925:214449:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Azar (`KXITFMATCH-26OCT01HALAZA-AZA`) | 0.10 / 0.11 (4210) | 10.5% | 32.2% | 14.8% | 31.0% [26.5%-32.9%] | 13.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.5 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| John Hallquist Lithen (`KXITFMATCH-26OCT01HALAZA-HAL`) | 0.88 / 0.90 (4560) | 89.0% | 67.8% | 85.2% | 69.0% [67.1%-73.5%] | 86.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2695.0, B 108.0; serve-point win A 64.4%, B 39.2%; Elo A 1354.3, B 1225.3; model uncertainty 0.0318
* Form inputs: days since last match A 129, B 206; matches on record A 94, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01HALAZA-AZA  (YES = Benjamin Azar)
Model: 31%
Kalshi: 10%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.018, surface_dev_loose +0.009, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Harold Mayot vs Tristan Schoolkate -- ATP Challenger Mouilleron-Le-Captif R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208004:209262:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harold Mayot (`KXATPCHALLENGERMATCH-26OCT01MAYSCH-MAY`) | 0.58 / 0.60 (13617) | 59.0% | -- | 60.8% | 59.3% [58.4%-60.3%] | 59.2% | 59.0% | 59.1% | MODEL_LONE_OUTLIER | PASS | +0.3 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Tristan Schoolkate (`KXATPCHALLENGERMATCH-26OCT01MAYSCH-SCH`) | 0.40 / 0.41 (5060) | 40.5% | -- | 39.2% | 40.7% [39.7%-41.6%] | 40.8% | 41.0% | 40.9% | MODEL_LONE_OUTLIER | PASS | +0.2 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5745.0, B 6276.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0096
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.009, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Dominick Mosejczuk vs Vlado Jankanj -- M15 Fayetteville AR R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:212892:213771:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vlado Jankanj (`KXITFMATCH-26OCT01MOSJAN-JAN`) | 0.31 / 0.32 (2012) | 31.5% | 46.9% | 38.2% | 45.3% [43.8%-46.9%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.8 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dominick Mosejczuk (`KXITFMATCH-26OCT01MOSJAN-MOS`) | 0.67 / 0.68 (237) | 67.5% | 53.1% | 61.8% | 54.7% [53.1%-56.2%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.8 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 379.0, B 875.0; serve-point win A 62.9%, B 37.7%; Elo A 1266.4, B 1244.6; model uncertainty 0.0157
* Form inputs: days since last match A 367, B 122; matches on record A 7, B 27; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high +0.000, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Sheldon vs Olaf Pieczkowski -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210142:210376:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Olaf Pieczkowski (`KXITFMATCH-26OCT01SHEPIE-PIE`) | 0.63 / 0.66 (2) | 64.5% | 76.5% | 63.4% | 74.9% [70.6%-79.8%] | 63.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.4 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Sheldon (`KXITFMATCH-26OCT01SHEPIE-SHE`) | 0.34 / 0.37 (3369) | 35.5% | 23.5% | 36.6% | 25.1% [20.2%-29.4%] | 36.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.4 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 264.0, B 2433.0; serve-point win A 59.7%, B 34.5%; Elo A 1229.6, B 1435.1; model uncertainty 0.0457
* Form inputs: days since last match A 486, B 59; matches on record A 13, B 234; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.028, surface_pool_high +0.035, surface_dev_loose -0.000, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Naoto Tomizawa vs Matt Kuhar -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208386:214236:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matt Kuhar (`KXITFMATCH-26OCT01TOMKUH-KUH`) | 0.58 / 0.60 (1764) | 59.0% | 51.7% | 64.4% | 52.1% [49.0%-55.8%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Naoto Tomizawa (`KXITFMATCH-26OCT01TOMKUH-TOM`) | 0.40 / 0.41 (4308) | 40.5% | 48.3% | 35.6% | 47.9% [44.2%-51.0%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.4 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 62.0, B 2542.0; serve-point win A 62.4%, B 37.2%; Elo A 1263.2, B 1274.9; model uncertainty 0.0341
* Form inputs: days since last match A 339, B 129; matches on record A 1, B 139; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.021, surface_dev_loose -0.011, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alvin Nicholas Tudorica vs Neo Niedner -- M15 Fayetteville AR R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210102:212202:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Neo Niedner (`KXITFMATCH-26OCT01TUDNIE-NIE`) | 0.35 / 0.39 (1379) | 37.0% | 20.3% | 64.0% | 27.1% [23.2%-31.7%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alvin Nicholas Tudorica (`KXITFMATCH-26OCT01TUDNIE-TUD`) | 0.62 / 0.64 (4332) | 63.0% | 79.7% | 36.0% | 72.9% [68.3%-76.8%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1789.0, B 335.0; serve-point win A 65.9%, B 40.7%; Elo A 1409.1, B 1171.4; model uncertainty 0.0425
* Form inputs: days since last match A 206, B 122; matches on record A 106, B 29; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.017, surface_dev_loose -0.004, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diva Bhatia vs Lourdes Ayala -- W15 Trelew R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:236968:263876:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lourdes Ayala (`KXITFWMATCH-26OCT01BHAAYA-AYA`) | 0.92 / 0.95 (5138) | 93.5% | 61.8% | 46.8% | 60.6% [60.6%-62.6%] | 92.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -32.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Diva Bhatia (`KXITFWMATCH-26OCT01BHAAYA-BHA`) | 0.07 / 0.08 (4014) | 7.5% | 38.2% | 53.2% | 39.4% [37.4%-39.4%] | 7.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +31.9 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 49.0, B 813.0; serve-point win A 54.6%, B 43.2%; Elo A 1132.4, B 1215.8; model uncertainty 0.0102
* Form inputs: days since last match A 381, B 185; matches on record A 19, B 105; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01BHAAYA-BHA  (YES = Diva Bhatia)
Model: 39%
Kalshi: 8%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leyla Fiorella Britez Risso vs Maria Sofia Madrid Rocca -- W15 Trelew R16

ITF (ITF) · Hard · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222513:237458:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leyla Fiorella Britez Risso (`KXITFWMATCH-26OCT01BRIMAD-BRI`) | 0.89 / 0.92 (5758) | 90.5% | 75.2% | 21.9% | 75.7% [74.9%-75.7%] | -- | -- | -- | -- | PASS | -14.8 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maria Sofia Madrid Rocca (`KXITFWMATCH-26OCT01BRIMAD-MAD`) | 0.08 / 0.10 (4065) | 9.0% | 24.8% | 78.1% | 24.3% [24.3%-25.1%] | -- | -- | -- | -- | PASS | +15.3 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 257.0, B 0.0; serve-point win A 58.2%, B 46.9%; Elo A 1408.3, B 1215.7; model uncertainty 0.0043
* Form inputs: days since last match A 843, B 1200; matches on record A 44, B 25; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01BRIMAD-MAD  (YES = Maria Sofia Madrid Rocca)
Model: 24%
Kalshi: 9%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.008, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Salma Drugdova vs Carlota Moreno -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:235160:270436:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Salma Drugdova (`KXITFWMATCH-26OCT01DRUMOR-DRU`) | 0.25 / 0.27 (4018) | 26.0% | 54.4% | 42.0% | 52.1% [48.9%-53.7%] | 27.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +26.1 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Carlota Moreno (`KXITFWMATCH-26OCT01DRUMOR-MOR`) | 0.73 / 0.75 (17) | 74.0% | 45.6% | 58.0% | 47.9% [46.3%-51.1%] | 72.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -26.1 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1429.0, B 350.0; serve-point win A 57.4%, B 43.4%; Elo A 1459.7, B 1429.2; model uncertainty 0.024
* Form inputs: days since last match A 423, B 178; matches on record A 158, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01DRUMOR-DRU  (YES = Salma Drugdova)
Model: 52%
Kalshi: 26%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valeria Ray vs Chiara Di Genova -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221414:263760:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chiara Di Genova (`KXITFWMATCH-26OCT01RAYDIG-DIG`) | 0.09 / 0.10 (3860) | 9.5% | 37.6% | 50.5% | 38.5% [37.4%-39.5%] | 11.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +29.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valeria Ray (`KXITFWMATCH-26OCT01RAYDIG-RAY`) | 0.89 / 0.91 (20) | 90.0% | 62.4% | 49.5% | 61.5% [60.5%-62.6%] | 88.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -28.5 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 223.0, B 146.0; serve-point win A 58.2%, B 44.2%; Elo A 1402.1, B 1314.1; model uncertainty 0.0106
* Form inputs: days since last match A 423, B 500; matches on record A 5, B 69; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01RAYDIG-DIG  (YES = Chiara Di Genova)
Model: 38%
Kalshi: 10%
Gap: +29 pp
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
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Merna Refaat vs Sophia Webster -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221473:260046:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Merna Refaat (`KXITFWMATCH-26OCT01REFWEB-REF`) | 0.71 / 0.72 (1) | 71.5% | 55.6% | 47.3% | 55.3% [55.3%-55.3%] | 69.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.2 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Sophia Webster (`KXITFWMATCH-26OCT01REFWEB-WEB`) | 0.27 / 0.28 (1096) | 27.5% | 44.4% | 52.7% | 44.7% [44.7%-44.7%] | 30.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +17.2 pp | HIGH_REVIEW (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 556.0, B 0.0; serve-point win A 57.5%, B 43.5%; Elo A 1376.3, B 1337.0; model uncertainty 0.0001
* Form inputs: days since last match A 353, B 836; matches on record A 201, B 16; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01REFWEB-WEB  (YES = Sophia Webster)
Model: 45%
Kalshi: 28%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefani Webb vs Ashton Bowers -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:248665:259567:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashton Bowers (`KXITFWMATCH-26OCT01WEBBOW-BOW`) | 0.50 / 0.53 (4285) | 51.5% | 52.0% | 35.9% | 52.1% [52.1%-52.1%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.6 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefani Webb (`KXITFWMATCH-26OCT01WEBBOW-WEB`) | 0.47 / 0.49 (1910) | 48.0% | 48.0% | 64.1% | 47.9% [47.9%-47.9%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1878.0, B 0.0; serve-point win A 56.8%, B 42.8%; Elo A 1405.8, B 1419.7; model uncertainty 0.0
* Form inputs: days since last match A 255, B 710; matches on record A 101, B 46; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Liv Zingg vs Luna Maria Cinalli -- W15 Trelew R16

ITF (ITF) · surface ? · scheduled 2026-10-01T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01ZINCIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luna Maria Cinalli (`KXITFWMATCH-26OCT01ZINCIN-CIN`) | 0.75 / 0.77 (2158) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liv Zingg (`KXITFWMATCH-26OCT01ZINCIN-ZIN`) | 0.22 / 0.24 (1118) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefan Kozlov vs Mitchell Krueger -- ATP Challenger Columbus R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T20:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106283:111578:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Kozlov (`KXATPCHALLENGERMATCH-26OCT01KOZKRU-KOZ`) | 0.56 / 0.57 (4432) | 56.5% | -- | 51.0% | 50.5% [47.9%-51.5%] | 56.3% | 56.0% | 56.0% | MODEL_LONE_OUTLIER | PASS | -6.0 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Mitchell Krueger (`KXATPCHALLENGERMATCH-26OCT01KOZKRU-KRU`) | 0.43 / 0.44 (4607) | 43.5% | -- | 49.0% | 49.5% [48.4%-52.1%] | 43.7% | 43.9% | 43.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.0 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4126.0, B 5011.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0181
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Daniel Milavsky / Braden Shick vs Matthew Forbes / Denis Petak -- ATP Challenger Columbus QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T20:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01MILSHIFORPET:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew Forbes / Denis Petak (`KXATPCHALLENGERDOUBLES-26OCT01MILSHIFORPET-FORPET`) | 0.32 / 0.40 (25) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Milavsky / Braden Shick (`KXATPCHALLENGERDOUBLES-26OCT01MILSHIFORPET-MILSHI`) | 0.60 / 0.68 (46) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Pedro Boscardin Dias vs Genaro Alberto Olivieri -- ATP Challenger Curitiba R16

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-01T20:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:144821:208046:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Boscardin Dias (`KXATPCHALLENGERMATCH-26OCT01BOSOLI-BOS`) | 0.55 / 0.56 (208) | 55.5% | -- | 47.9% | 47.9% [47.9%-48.4%] | 55.4% | 56.7% | 56.1% | MODEL_LONE_OUTLIER | PASS | -7.6 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Genaro Alberto Olivieri (`KXATPCHALLENGERMATCH-26OCT01BOSOLI-OLI`) | 0.45 / 0.46 (17176) | 45.5% | -- | 52.1% | 52.1% [51.6%-52.1%] | 44.6% | 43.6% | 44.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.6 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4852.0, B 5465.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0026
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Coppez / Tran vs Leonard / Martynov -- W35 Reims SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T20:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01COPTRALEOMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coppez / Tran (`KXITFWDOUBLES-26OCT01COPTRALEOMAR-COPTRA`) | 0.08 / 0.74 (615) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leonard / Martynov (`KXITFWDOUBLES-26OCT01COPTRALEOMAR-LEOMAR`) | 0.27 / 0.56 (659) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Oliver Bonding vs Marko Mesarovic -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:211670:212839:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oliver Bonding (`KXITFMATCH-26OCT01BONMES-BON`) | 0.80 / 0.81 (853) | 80.5% | 62.0% | 54.6% | 67.3% [64.0%-69.7%] | 81.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.2 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marko Mesarovic (`KXITFMATCH-26OCT01BONMES-MES`) | 0.16 / 0.19 (3408) | 17.5% | 38.0% | 45.4% | 32.7% [30.3%-36.0%] | 18.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +15.2 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1207.0, B 745.0; serve-point win A 63.8%, B 38.6%; Elo A 1440.2, B 1267.9; model uncertainty 0.0282
* Form inputs: days since last match A 38, B 122; matches on record A 42, B 24; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01BONMES-MES  (YES = Marko Mesarovic)
Model: 33%
Kalshi: 18%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Micah Braswell vs Hugo Coquelin -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209334:213042:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Micah Braswell (`KXITFMATCH-26OCT01BRACOQ-BRA`) | 0.60 / 0.61 (44) | 60.5% | 79.1% | 74.5% | 78.1% [76.8%-79.4%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +17.6 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hugo Coquelin (`KXITFMATCH-26OCT01BRACOQ-COQ`) | 0.37 / 0.38 (748) | 37.5% | 20.9% | 25.5% | 21.9% [20.6%-23.2%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.7 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2173.0, B 446.0; serve-point win A 65.8%, B 40.6%; Elo A 1508.7, B 1277.2; model uncertainty 0.0126
* Form inputs: days since last match A 241, B 122; matches on record A 99, B 17; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01BRACOQ-BRA  (YES = Micah Braswell)
Model: 78%
Kalshi: 60%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.008, surface_dev_loose +0.008, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dragos Nicolae Cazacu vs Alexander Rozin -- M15 Fayetteville AR R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01CAZROZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dragos Nicolae Cazacu (`KXITFMATCH-26OCT01CAZROZ-CAZ`) | 0.20 / 0.22 (915) | 21.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Rozin (`KXITFMATCH-26OCT01CAZROZ-ROZ`) | 0.76 / 0.79 (11) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikola Djosic vs Thanaphat Boosarawongse -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:212149:213051:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thanaphat Boosarawongse (`KXITFMATCH-26OCT01DJOBOO-BOO`) | 0.59 / 0.60 (377) | 59.5% | 39.7% | 29.9% | 38.6% [35.6%-40.2%] | 58.1% | -- | 58.1% | MODEL_LONE_OUTLIER | PASS | -20.9 pp | HIGH_REVIEW | STALE | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Nikola Djosic (`KXITFMATCH-26OCT01DJOBOO-DJO`) | 0.39 / 0.40 (1897) | 39.5% | 60.3% | 70.0% | 61.4% [59.8%-64.4%] | 41.9% | -- | 41.9% | KALSHI_LONE_OUTLIER | PASS | +21.9 pp | HIGH_REVIEW | STALE | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1313.0, B 249.0; serve-point win A 63.6%, B 38.4%; Elo A 1289.1, B 1216.5; model uncertainty 0.023
* Form inputs: days since last match A 129, B 269; matches on record A 39, B 13; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01DJOBOO-DJO  (YES = Nikola Djosic)
Model: 61%
Kalshi: 40%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Theo Papamalamis vs Tito Chavez -- M15 Fayetteville AR R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210494:214377:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tito Chavez (`KXITFMATCH-26OCT01PAPCHA-CHA`) | 0.23 / 0.26 (68) | 24.5% | 34.7% | 26.2% | 32.1% [30.2%-34.7%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Theo Papamalamis (`KXITFMATCH-26OCT01PAPCHA-PAP`) | 0.74 / 0.76 (3380) | 75.0% | 65.3% | 73.8% | 67.9% [65.3%-69.8%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.1 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1643.0, B 499.0; serve-point win A 64.1%, B 39.0%; Elo A 1427.8, B 1317.9; model uncertainty 0.0226
* Form inputs: days since last match A 122, B 129; matches on record A 97, B 10; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.010, surface_dev_loose +0.019, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Johan Alexander Rodriguez vs Alejandro Melero Kretzer -- M15 Fayetteville AR R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01RODMEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alejandro Melero Kretzer (`KXITFMATCH-26OCT01RODMEL-MEL`) | 0.22 / 0.24 (184) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Johan Alexander Rodriguez (`KXITFMATCH-26OCT01RODMEL-ROD`) | 0.76 / 0.79 (4189) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Damir Zhalgasbay vs Felix Corwin -- M15 Ann Arbor MI R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200228:212846:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Corwin (`KXITFMATCH-26OCT01ZHACOR-COR`) | 0.51 / 0.53 (63) | 52.0% | 80.5% | 67.7% | 79.2% [77.6%-80.0%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +27.2 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Damir Zhalgasbay (`KXITFMATCH-26OCT01ZHACOR-ZHA`) | 0.47 / 0.50 (62) | 48.5% | 19.5% | 32.3% | 20.8% [20.0%-22.4%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -27.7 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 222.0, B 3231.0; serve-point win A 59.2%, B 34.0%; Elo A 1156.7, B 1403.3; model uncertainty 0.0117
* Form inputs: days since last match A 157, B 171; matches on record A 6, B 382; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01ZHACOR-COR  (YES = Felix Corwin)
Model: 79%
Kalshi: 52%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Berecoechea / Candiotto vs Hietaranta / Zelnickova -- W35 Baza SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01BERCANHIEZEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Berecoechea / Candiotto (`KXITFWDOUBLES-26OCT01BERCANHIEZEL-BERCAN`) | 0.07 / 0.60 (562) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hietaranta / Zelnickova (`KXITFWDOUBLES-26OCT01BERCANHIEZEL-HIEZEL`) | 0.31 / 0.52 (52) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Pilar Da Silva vs Marina Bulbarella -- W15 Trelew R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01DASBUL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marina Bulbarella (`KXITFWMATCH-26OCT01DASBUL-BUL`) | 0.38 / 0.41 (6247) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pilar Da Silva (`KXITFWMATCH-26OCT01DASBUL-DAS`) | 0.60 / 0.62 (255) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emma Kamper vs Kristina Paskauskas -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:241715:258195:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emma Kamper (`KXITFWMATCH-26OCT01KAMPAS-KAM`) | 0.60 / 0.62 (29) | 61.0% | 38.3% | 78.9% | 47.3% [39.5%-56.9%] | 61.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.7 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kristina Paskauskas (`KXITFWMATCH-26OCT01KAMPAS-PAS`) | 0.38 / 0.39 (2) | 38.5% | 61.7% | 21.1% | 52.7% [43.1%-60.6%] | 38.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.2 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 510.0, B 382.0; serve-point win A 55.9%, B 41.9%; Elo A 1354.7, B 1437.4; model uncertainty 0.0873
* Form inputs: days since last match A 332, B 304; matches on record A 33, B 101; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ana Sofia Sanchez vs Florencia Belen Moron -- W15 Trelew R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:204419:260357:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florencia Belen Moron (`KXITFWMATCH-26OCT01SANMOR-MOR`) | 0.05 / 0.06 (64) | 5.5% | 6.9% | 13.3% | 7.4% [6.0%-8.4%] | -- | -- | -- | -- | PASS | +1.9 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ana Sofia Sanchez (`KXITFWMATCH-26OCT01SANMOR-SAN`) | 0.91 / 0.95 (120) | 93.0% | 93.1% | 86.7% | 92.6% [91.6%-94.0%] | -- | -- | -- | -- | PASS | -0.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3191.0, B 144.0; serve-point win A 61.3%, B 49.9%; Elo A 1573.4, B 1120.4; model uncertainty 0.0117
* Form inputs: days since last match A 19, B 255; matches on record A 856, B 77; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.010, surface_dev_loose +0.002, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## CAIRA DELFINA VEGA GUDINO vs Maria Florencia Urrutia -- W15 Trelew R16

ITF (ITF) · Hard · scheduled 2026-10-01T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220447:270267:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Florencia Urrutia (`KXITFWMATCH-26OCT01VEGURR-URR`) | 0.93 / 0.95 (838) | 94.0% | 81.5% | 81.2% | 81.9% [81.2%-82.6%] | -- | -- | -- | -- | PASS | -12.1 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| CAIRA DELFINA VEGA GUDINO (`KXITFWMATCH-26OCT01VEGURR-VEG`) | 0.05 / 0.06 (1071) | 5.5% | 18.5% | 18.8% | 18.1% [17.4%-18.8%] | -- | -- | -- | -- | PASS | +12.6 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 120.0, B 2454.0; serve-point win A 52.3%, B 40.9%; Elo A 1228.4, B 1486.5; model uncertainty 0.007
* Form inputs: days since last match A 255, B 157; matches on record A 2, B 106; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.007, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tom Hands / Matthew Summers vs Karl Poling / Joshua Sheehy -- ATP Challenger Mouilleron-Le-Captif QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T21:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HANSUMPOLSHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tom Hands / Matthew Summers (`KXATPCHALLENGERDOUBLES-26OCT01HANSUMPOLSHE-HANSUM`) | 0.49 / 0.52 (5) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karl Poling / Joshua Sheehy (`KXATPCHALLENGERDOUBLES-26OCT01HANSUMPOLSHE-POLSHE`) | 0.46 / 0.51 (0) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Brandon Carpico / Nikita Samuel Filin vs Luis David Martinez / James Kent Trotter -- ATP Challenger Columbus QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T21:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01CARFILMARTRO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brandon Carpico / Nikita Samuel Filin (`KXATPCHALLENGERDOUBLES-26OCT01CARFILMARTRO-CARFIL`) | 0.53 / 0.62 (52) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luis David Martinez / James Kent Trotter (`KXATPCHALLENGERDOUBLES-26OCT01CARFILMARTRO-MARTRO`) | 0.37 / 0.46 (46) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## James Mackinlay / Oliver Okonkwo vs Alex Rybakov / Keegan Smith -- ATP Challenger Columbus QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T21:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01MACOKORYBSMI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Mackinlay / Oliver Okonkwo (`KXATPCHALLENGERDOUBLES-26OCT01MACOKORYBSMI-MACOKO`) | 0.42 / 0.47 (5) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alex Rybakov / Keegan Smith (`KXATPCHALLENGERDOUBLES-26OCT01MACOKORYBSMI-RYBSMI`) | 0.48 / 0.56 (57) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ashley Lahey vs Raquel Caballero Chica -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216076:231636:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raquel Caballero Chica (`KXITFWMATCH-26OCT01LAHCAB-CAB`) | 0.23 / 0.24 (1) | 23.5% | 8.4% | 25.0% | 9.3% [8.8%-9.8%] | 25.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.2 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ashley Lahey (`KXITFWMATCH-26OCT01LAHCAB-LAH`) | 0.75 / 0.77 (347) | 76.0% | 91.6% | 75.0% | 90.7% [90.2%-91.2%] | 74.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.7 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1883.0, B 74.0; serve-point win A 62.2%, B 48.2%; Elo A 1627.6, B 1213.5; model uncertainty 0.0048
* Form inputs: days since last match A 381, B 500; matches on record A 239, B 25; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eszter Meri vs Astra Sharma -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:206292:221150:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eszter Meri (`KXITFWMATCH-26OCT01MERSHA-MER`) | 0.27 / 0.29 (101) | 28.0% | 31.5% | 48.9% | 35.4% [31.6%-39.0%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Astra Sharma (`KXITFWMATCH-26OCT01MERSHA-SHA`) | 0.70 / 0.74 (1734) | 72.0% | 68.5% | 51.1% | 64.6% [61.1%-68.4%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.4 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 402.0, B 2800.0; serve-point win A 55.2%, B 41.2%; Elo A 1563.2, B 1698.2; model uncertainty 0.0368
* Form inputs: days since last match A 465, B 15; matches on record A 258, B 423; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rose Marie Nijkamp vs Francesca Mattioli -- W15 Nashville TN R16

ITF (ITF) · surface ? · scheduled 2026-10-01T21:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:260150:260225:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Mattioli (`KXITFWMATCH-26OCT01NIJMAT-MAT`) | 0.30 / 0.33 (3152) | 31.5% | 49.1% | 39.4% | 46.8% [44.1%-48.9%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +15.3 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rose Marie Nijkamp (`KXITFWMATCH-26OCT01NIJMAT-NIJ`) | 0.67 / 0.70 (1158) | 68.5% | 50.9% | 60.6% | 53.2% [51.1%-55.9%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.3 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1080.0, B 492.0; serve-point win A 57.1%, B 43.1%; Elo A 1482.4, B 1476.0; model uncertainty 0.0241
* Form inputs: days since last match A 164, B 423; matches on record A 54, B 28; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01NIJMAT-MAT  (YES = Francesca Mattioli)
Model: 47%
Kalshi: 32%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Podhajecka / Sharabura vs Pearce / Yamakita -- W15 Nashville TN QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T21:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01PODSHAPEAYAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pearce / Yamakita (`KXITFWDOUBLES-26OCT01PODSHAPEAYAM-PEAYAM`) | 0.17 / 0.46 (27) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Podhajecka / Sharabura (`KXITFWDOUBLES-26OCT01PODSHAPEAYAM-PODSHA`) | 0.07 / 0.83 (647) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Ganchev / Maes vs Ifi / Stanke -- M25 Zaragoza QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01GANMAEIFISTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ganchev / Maes (`KXITFDOUBLES-26OCT01GANMAEIFISTA-GANMAE`) | 0.18 / 0.78 (1085) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ifi / Stanke (`KXITFDOUBLES-26OCT01GANMAEIFISTA-IFISTA`) | 0.23 / 0.64 (520) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Horwood / Vrba vs Roddick / Tokac -- M15 Fayetteville AR QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HORVRBRODTOK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Horwood / Vrba (`KXITFDOUBLES-26OCT01HORVRBRODTOK-HORVRB`) | 0.07 / 0.65 (571) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Roddick / Tokac (`KXITFDOUBLES-26OCT01HORVRBRODTOK-RODTOK`) | 0.22 / 0.48 (48) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Pawlak / Pujol Navarro vs Lopez Martos / Palomar -- M25 Zaragoza QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01PAWPUJLOPPAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lopez Martos / Palomar (`KXITFDOUBLES-26OCT01PAWPUJLOPPAL-LOPPAL`) | 0.32 / 0.45 (109) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pawlak / Pujol Navarro (`KXITFDOUBLES-26OCT01PAWPUJLOPPAL-PAWPUJ`) | 0.48 / 0.66 (0) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexander Ritschard vs samuel arauzo martinez -- M25 Zaragoza R16

ITF (ITF) · Clay · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106310:213124:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| samuel arauzo martinez (`KXITFMATCH-26OCT01RITARA-ARA`) | 0.04 / 0.05 (104) | 4.5% | 4.6% | 16.8% | 4.6% [3.9%-5.4%] | -- | -- | -- | -- | PASS | +0.1 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Alexander Ritschard (`KXITFMATCH-26OCT01RITARA-RIT`) | 0.93 / 0.96 (4262) | 94.5% | 95.4% | 83.2% | 95.4% [94.6%-96.1%] | -- | -- | -- | -- | PASS | +0.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 3172.0, B 0.0; serve-point win A 66.5%, B 46.7%; Elo A 1773.1, B 1244.9; model uncertainty 0.0074
* Form inputs: days since last match A 24, B 787; matches on record A 681, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.008, surface_dev_loose -0.002, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Charlie Robertson vs Hoyoung Roh -- M15 Fayetteville AR R16

ITF (ITF) · Hard · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:212115:212127:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charlie Robertson (`KXITFMATCH-26OCT01ROBROH-ROB`) | 0.49 / 0.51 (964) | 50.0% | 52.7% | 56.8% | 54.7% [52.1%-56.8%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.7 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hoyoung Roh (`KXITFMATCH-26OCT01ROBROH-ROH`) | 0.48 / 0.51 (51) | 49.5% | 47.3% | 43.2% | 45.3% [43.2%-47.9%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.2 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1222.0, B 1129.0; serve-point win A 62.9%, B 37.7%; Elo A 1348.8, B 1325.4; model uncertainty 0.0236
* Form inputs: days since last match A 178, B 122; matches on record A 38, B 36; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aryan Shah vs Evan Bynoe -- M15 Fayetteville AR R16

ITF (ITF) · Hard · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208466:211325:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Evan Bynoe (`KXITFMATCH-26OCT01SHABYN-BYN`) | 0.24 / 0.27 (26) | 25.5% | 23.5% | 24.6% | 23.8% [22.1%-26.3%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.7 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aryan Shah (`KXITFMATCH-26OCT01SHABYN-SHA`) | 0.71 / 0.76 (3823) | 73.5% | 76.5% | 75.4% | 76.2% [73.7%-77.9%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.7 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2442.0, B 1889.0; serve-point win A 65.5%, B 40.3%; Elo A 1455.1, B 1243.8; model uncertainty 0.0206
* Form inputs: days since last match A 68, B 143; matches on record A 130, B 102; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.004, surface_dev_loose -0.008, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juliana Giaccio vs Mathilde Lollia -- W35 Baza R16

ITF (ITF) · Hard · scheduled 2026-10-01T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221443:269835:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juliana Giaccio (`KXITFWMATCH-26OCT01GIALOL-GIA`) | 0.46 / 0.49 (29) | 47.5% | 29.8% | 26.6% | 26.6% [22.8%-31.1%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mathilde Lollia (`KXITFWMATCH-26OCT01GIALOL-LOL`) | 0.51 / 0.54 (150) | 52.5% | 70.2% | 73.4% | 73.4% [68.8%-77.2%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 776.0, B 2163.0; serve-point win A 53.7%, B 42.3%; Elo A 1236.6, B 1409.2; model uncertainty 0.0419
* Form inputs: days since last match A 192, B 171; matches on record A 22, B 173; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01GIALOL-LOL  (YES = Mathilde Lollia)
Model: 73%
Kalshi: 52%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.034, surface_pool_high +0.045, surface_dev_loose -0.008, surface_dev_tight +0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Friedman / Sohns vs Bartel / Justine Hejtmanek -- W15 Nashville TN QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T22:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01FRISOHBARJUS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bartel / Justine Hejtmanek (`KXITFWDOUBLES-26OCT01FRISOHBARJUS-BARJUS`) | 0.07 / 0.90 (100) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Friedman / Sohns (`KXITFWDOUBLES-26OCT01FRISOHBARJUS-FRISOH`) | 0.06 / 0.94 (210) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Luciana Moyano vs Sofia Meabe -- W15 Trelew R16

ITF (ITF) · Hard · scheduled 2026-10-01T22:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:237454:266446:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Meabe (`KXITFWMATCH-26OCT01MOYMEA-MEA`) | 0.26 / 0.28 (1163) | 27.0% | 40.2% | 21.8% | 37.3% [34.3%-40.4%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.3 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luciana Moyano (`KXITFWMATCH-26OCT01MOYMEA-MOY`) | 0.72 / 0.73 (1722) | 72.5% | 59.8% | 78.2% | 62.7% [59.6%-65.7%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2452.0, B 235.0; serve-point win A 56.6%, B 45.2%; Elo A 1405.3, B 1336.4; model uncertainty 0.0305
* Form inputs: days since last match A 157, B 255; matches on record A 106, B 18; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.031, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emily Zornada vs Ana Victoria Gobbi Monllau -- W15 Trelew R16

ITF (ITF) · Hard · scheduled 2026-10-01T22:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211600:270329:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ana Victoria Gobbi Monllau (`KXITFWMATCH-26OCT01ZORGOB-GOB`) | 0.50 / 0.51 (727) | 50.5% | 42.5% | 32.4% | 42.0% [41.0%-42.6%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.5 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Emily Zornada (`KXITFWMATCH-26OCT01ZORGOB-ZOR`) | 0.46 / 0.49 (4277) | 47.5% | 57.5% | 67.6% | 58.0% [57.4%-59.0%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.5 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 106.0, B 761.0; serve-point win A 56.4%, B 45.0%; Elo A 1299.7, B 1247.0; model uncertainty 0.008
* Form inputs: days since last match A 185, B 192; matches on record A 2, B 108; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Boland / Smillie vs Lestir / Milosavljevic -- M15 Fayetteville AR QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01BOLSMILESMIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boland / Smillie (`KXITFDOUBLES-26OCT01BOLSMILESMIL-BOLSMI`) | 0.06 / 0.88 (583) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lestir / Milosavljevic (`KXITFDOUBLES-26OCT01BOLSMILESMIL-LESMIL`) | 0.13 / 0.86 (600) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Goity Zapico / Valletta vs Arcila / Rozin -- M15 Fayetteville AR QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01GOIVALARCROZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arcila / Rozin (`KXITFDOUBLES-26OCT01GOIVALARCROZ-ARCROZ`) | 0.09 / 0.69 (100) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Goity Zapico / Valletta (`KXITFDOUBLES-26OCT01GOIVALARCROZ-GOIVAL`) | 0.08 / 0.38 (1) | 23.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tatjana Maria vs Lea Ma -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-01T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:213583:221220:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tatjana Maria (`KXITFWMATCH-26OCT01MARMAX-MAR`) | 0.83 / 0.86 (5035) | 84.5% | 54.0% | 28.5% | 42.3% [33.5%-65.7%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -42.2 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lea Ma (`KXITFWMATCH-26OCT01MARMAX-MAX`) | 0.14 / 0.17 (1043) | 15.5% | 46.0% | 71.5% | 57.7% [34.3%-66.5%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +42.2 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4444.0, B 2727.0; serve-point win A 56.1%, B 44.7%; Elo A 1749.9, B 1608.9; model uncertainty 0.161
* Form inputs: days since last match A 17, B 19; matches on record A 1257, B 167; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01MARMAX-MAX  (YES = Lea Ma)
Model: 58%
Kalshi: 16%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.041, surface_pool_high -0.045, surface_dev_loose -0.015, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Whitney Osuigwe vs Ella McDonald -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-01T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215992:259591:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ella McDonald (`KXITFWMATCH-26OCT01OSUMCD-MCD`) | 0.47 / 0.48 (1358) | 47.5% | 44.2% | 56.9% | 47.9% [39.9%-52.7%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.4 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Whitney Osuigwe (`KXITFWMATCH-26OCT01OSUMCD-OSU`) | 0.51 / 0.53 (3953) | 52.0% | 55.8% | 43.1% | 52.1% [47.3%-60.1%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.1 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3327.0, B 1341.0; serve-point win A 56.2%, B 44.9%; Elo A 1644.5, B 1577.9; model uncertainty 0.0637
* Form inputs: days since last match A 18, B 100; matches on record A 411, B 146; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.021, surface_dev_loose -0.021, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Malaika Rapolu vs Akasha Urhobo -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-01T23:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222837:259857:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Malaika Rapolu (`KXITFWMATCH-26OCT01RAPURH-RAP`) | 0.54 / 0.55 (150) | 54.5% | 40.9% | 43.1% | 45.2% [40.0%-48.4%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Akasha Urhobo (`KXITFWMATCH-26OCT01RAPURH-URH`) | 0.44 / 0.45 (1080) | 44.5% | 59.1% | 56.9% | 54.8% [51.6%-60.0%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +10.3 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1761.0, B 3335.0; serve-point win A 54.8%, B 43.5%; Elo A 1612.4, B 1631.7; model uncertainty 0.0421
* Form inputs: days since last match A 14, B 38; matches on record A 133, B 177; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.042, surface_pool_high +0.032, surface_dev_loose +0.005, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Azar / Cairo vs Klimas / Mikovic -- M15 Ann Arbor MI QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01AZACAIKLIMIK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Azar / Cairo (`KXITFDOUBLES-26OCT01AZACAIKLIMIK-AZACAI`) | 0.06 / 0.92 (501) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Klimas / Mikovic (`KXITFDOUBLES-26OCT01AZACAIKLIMIK-KLIMIK`) | 0.07 / 0.80 (600) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Fradkin / Kuhar vs Albieri / Heng -- M15 Ann Arbor MI QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01FRAKUHALBHEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Albieri / Heng (`KXITFDOUBLES-26OCT01FRAKUHALBHEN-ALBHEN`) | 0.20 / 0.30 (35) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fradkin / Kuhar (`KXITFDOUBLES-26OCT01FRAKUHALBHEN-FRAKUH`) | 0.62 / 0.87 (1977) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Gogineni / Petrovic vs Burnett / Tomizawa -- M15 Ann Arbor MI QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01GOGPETBURTOM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Burnett / Tomizawa (`KXITFDOUBLES-26OCT01GOGPETBURTOM-BURTOM`) | 0.07 / 0.88 (581) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gogineni / Petrovic (`KXITFDOUBLES-26OCT01GOGPETBURTOM-GOGPET`) | 0.13 / 0.87 (1101) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Sheldon / Swenson vs Matta / Peck -- M15 Ann Arbor MI QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01SHESWEMATPEC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matta / Peck (`KXITFDOUBLES-26OCT01SHESWEMATPEC-MATPEC`) | 0.31 / 0.35 (38) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sheldon / Swenson (`KXITFDOUBLES-26OCT01SHESWEMATPEC-SHESWE`) | 0.07 / 0.70 (586) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Carrocera / Maria Maruca vs Ayala / Fiorella Britez Risso -- W15 Trelew QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01CARMARAYAFIO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayala / Fiorella Britez Risso (`KXITFWDOUBLES-26OCT01CARMARAYAFIO-AYAFIO`) | 0.09 / 0.88 (100) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Carrocera / Maria Maruca (`KXITFWDOUBLES-26OCT01CARMARAYAFIO-CARMAR`) | 0.06 / 0.93 (103) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Doldan / Celina Sosa vs Ailin Larraya Guidi / Sousa Salazar -- W15 Trelew QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-01T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01DOLCELAILSOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ailin Larraya Guidi / Sousa Salazar (`KXITFWDOUBLES-26OCT01DOLCELAILSOU-AILSOU`) | 0.09 / 0.92 (55) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Doldan / Celina Sosa (`KXITFWDOUBLES-26OCT01DOLCELAILSOU-DOLCEL`) | 0.06 / 0.93 (100) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Carolina Kuhl vs Kristina Penickova -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-02T00:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:230882:266381:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carolina Kuhl (`KXITFWMATCH-26OCT01KUHPEN-KUH`) | 0.34 / 0.36 (3) | 35.0% | -- | 28.5% | 36.1% [30.4%-45.8%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kristina Penickova (`KXITFWMATCH-26OCT01KUHPEN-PEN`) | 0.62 / 0.65 (672) | 63.5% | -- | 71.5% | 63.9% [54.2%-69.6%] | -- | -- | -- | -- | PASS | +0.4 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1139.0, B 1178.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0769
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.029, surface_dev_loose -0.004, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francesca Pace vs Amelie Van Impe -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-02T00:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:228909:256673:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesca Pace (`KXITFWMATCH-26OCT01PACVAN-PAC`) | 0.55 / 0.56 (47) | 55.5% | -- | 62.0% | 55.3% [50.5%-57.9%] | -- | -- | -- | -- | PASS | -0.2 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amelie Van Impe (`KXITFWMATCH-26OCT01PACVAN-VAN`) | 0.44 / 0.45 (5675) | 44.5% | -- | 38.0% | 44.7% [42.1%-49.5%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2585.0, B 1949.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0367
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.016, surface_dev_loose +0.026, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Julieta Pareja vs Mary Stoiana -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-02T00:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:223168:264075:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julieta Pareja (`KXITFWMATCH-26OCT01PARSTO-PAR`) | 0.43 / 0.46 (4107) | 44.5% | -- | 35.5% | 36.5% [36.0%-37.5%] | -- | -- | -- | -- | PASS | -8.0 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mary Stoiana (`KXITFWMATCH-26OCT01PARSTO-STO`) | 0.54 / 0.57 (25) | 55.5% | -- | 64.5% | 63.5% [62.5%-64.0%] | -- | -- | -- | -- | WATCH | +8.0 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1273.0, B 2840.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0074
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Henrique Pissetti Vialle / Leonardo Storck Franca vs Luis Guto Miguel / Eduardo Ribeiro -- ATP Challenger Curitiba QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-02T00:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01PISSTOMIGRIB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Guto Miguel / Eduardo Ribeiro (`KXATPCHALLENGERDOUBLES-26OCT01PISSTOMIGRIB-MIGRIB`) | 0.80 / 0.89 (105) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Henrique Pissetti Vialle / Leonardo Storck Franca (`KXATPCHALLENGERDOUBLES-26OCT01PISSTOMIGRIB-PISSTO`) | 0.14 / 0.19 (475) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Broadus / Zamarripa vs Chang / Hu -- W100 Templeton CA QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T01:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01BROZAMCHAHUX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Broadus / Zamarripa (`KXITFWDOUBLES-26OCT01BROZAMCHAHUX-BROZAM`) | 0.06 / 0.94 (168) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chang / Hu (`KXITFWDOUBLES-26OCT01BROZAMCHAHUX-CHAHUX`) | 0.07 / 0.22 (32) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Madison Brengle vs Arianna Zucchini -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-02T02:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:201483:222369:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madison Brengle (`KXITFWMATCH-26OCT01BREZUC-BRE`) | 0.76 / 0.79 (358) | 77.5% | -- | 48.9% | 63.2% [58.0%-75.3%] | -- | -- | -- | -- | PASS | -14.3 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arianna Zucchini (`KXITFWMATCH-26OCT01BREZUC-ZUC`) | 0.21 / 0.24 (3156) | 22.5% | -- | 51.1% | 36.8% [24.7%-42.0%] | -- | -- | -- | -- | WATCH | +14.3 pp | REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2464.0, B 2652.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0866
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.005, surface_dev_loose -0.015, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hewitt / Strakhova vs Frodin / Sahdiieva -- W100 Templeton CA QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T02:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01HEWSTRFROSAH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Frodin / Sahdiieva (`KXITFWDOUBLES-26OCT01HEWSTRFROSAH-FROSAH`) | 0.08 / 0.43 (43) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hewitt / Strakhova (`KXITFWDOUBLES-26OCT01HEWSTRFROSAH-HEWSTR`) | 0.06 / 0.73 (92) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Kawano Cho / Tarantola vs Meabe / Florencia Urrutia -- W15 Trelew QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T02:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01KAWTARMEAFLO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kawano Cho / Tarantola (`KXITFWDOUBLES-26OCT01KAWTARMEAFLO-KAWTAR`) | 0.06 / 0.94 (211) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Meabe / Florencia Urrutia (`KXITFWDOUBLES-26OCT01KAWTARMEAFLO-MEAFLO`) | 0.08 / 0.94 (111) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Moyano / Sofia Sanchez vs Bhatia / Belen Moron -- W15 Trelew QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T02:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01MOYSOFBHABEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bhatia / Belen Moron (`KXITFWDOUBLES-26OCT01MOYSOFBHABEL-BHABEL`) | 0.06 / 0.07 (26) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Moyano / Sofia Sanchez (`KXITFWDOUBLES-26OCT01MOYSOFBHABEL-MOYSOF`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Penickova / Penickova vs Osuigwe / Urhobo -- W100 Templeton CA QF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T03:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01PENPENOSUURH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Osuigwe / Urhobo (`KXITFWDOUBLES-26OCT01PENPENOSUURH-OSUURH`) | 0.07 / 0.44 (1) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Penickova / Penickova (`KXITFWDOUBLES-26OCT01PENPENOSUURH-PENPEN`) | 0.06 / 0.72 (89) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arthur Fils vs Frances Tiafoe -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126207:209950:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fils (`KXATPMATCH-26OCT01FILTIA-FIL`) | 0.70 / 0.71 (2677) | 70.5% | -- | 69.5% | 68.2% [65.2%-69.0%] | -- | -- | -- | -- | PASS | -2.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Frances Tiafoe (`KXATPMATCH-26OCT01FILTIA-TIA`) | 0.29 / 0.30 (7926) | 29.5% | -- | 30.5% | 31.8% [30.9%-34.8%] | -- | -- | -- | -- | PASS | +2.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5009.0, B 5884.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0193
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose +0.008, surface_dev_tight -0.013
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01FILTIA-24` Over 23.5 games: 0.42/0.44 mid 43.0%, model 52.8% (market_conditioned_v1 (model4_board_v1)) -- gap +9.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01FILTIA-FIL6` Will Arthur Fils win at least 5.5 more games than Frances Tiafoe?: 0.21/0.24 mid 22.5%, model 12.9% (market_conditioned_v1 (model4_board_v1)) -- gap -9.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01FILTIA-29` Over 28.5 games: 0.25/0.29 mid 27.0%, model 36.5% (market_conditioned_v1 (model4_board_v1)) -- gap +9.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01FILTIA-19` Over 18.5 games: 0.81/0.84 mid 82.5%, model 89.7% (market_conditioned_v1 (model4_board_v1)) -- gap +7.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01FILTIA-FIL21` Will Arthur Fils win the Arthur Fils vs Frances Tiafoe match by a set score of 2-1?: 0.22/0.25 mid 23.5%, model 29.5% (market_conditioned_v1 (model4_board_v1)) -- gap +6.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01FILTIA-FIL3` Will Arthur Fils win at least 2.5 more games than Frances Tiafoe?: 0.57/0.59 mid 58.0%, model 53.6% (market_conditioned_v1 (model4_board_v1)) -- gap -4.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01FILTIA-FIL20` Will Arthur Fils win the Arthur Fils vs Frances Tiafoe match by a set score of 2-0?: 0.43/0.46 mid 44.5%, model 40.8% (market_conditioned_v1 (model4_board_v1)) -- gap -3.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01FILTIA-TIA20` Will Frances Tiafoe win the Arthur Fils vs Frances Tiafoe match by a set score of 2-0?: 0.14/0.17 mid 15.5%, model 13.0% (market_conditioned_v1 (model4_board_v1)) -- gap -2.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01FILTIA-TIA21` Will Frances Tiafoe win the Arthur Fils vs Frances Tiafoe match by a set score of 2-1?: 0.13/0.16 mid 14.5%, model 16.7% (market_conditioned_v1 (model4_board_v1)) -- gap +2.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01FILTIA-TIA2` Will Frances Tiafoe win at least 1.5 more games than Arthur Fils?: 0.23/0.26 mid 24.5%, model 23.0% (market_conditioned_v1 (model4_board_v1)) -- gap -1.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Ugo Humbert vs Jiri Lehecka -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200005:208103:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ugo Humbert (`KXATPMATCH-26OCT01HUMLEH-HUM`) | 0.33 / 0.34 (1515) | 33.5% | -- | 45.3% | 45.8% [43.4%-47.2%] | -- | 38.4% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +12.3 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiri Lehecka (`KXATPMATCH-26OCT01HUMLEH-LEH`) | 0.63 / 0.64 (3432) | 63.5% | -- | 54.7% | 54.2% [52.8%-56.6%] | -- | 62.4% | -- | INSUFFICIENT_INPUTS | PASS | -9.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5799.0, B 5765.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0192
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.014, surface_dev_loose -0.004, surface_dev_tight -0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01HUMLEH-24` Over 23.5 games: 0.44/0.45 mid 44.5%, model 57.4% (market_conditioned_v1 (model4_board_v1)) -- gap +12.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01HUMLEH-19` Over 18.5 games: 0.65/0.99 mid 82.0%, model 94.1% (market_conditioned_v1 (model4_board_v1)) -- gap +12.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01HUMLEH-LEH6` Will Jiri Lehecka win at least 5.5 more games than Ugo Humbert?: 0.05/0.29 mid 17.0%, model 7.2% (market_conditioned_v1 (model4_board_v1)) -- gap -9.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01HUMLEH-29` Over 28.5 games: 0.16/0.49 mid 32.5%, model 41.4% (market_conditioned_v1 (model4_board_v1)) -- gap +8.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01HUMLEH-LEH20` Will Jiri Lehecka win the Ugo Humbert vs Jiri Lehecka match by a set score of 2-0?: 0.40/0.43 mid 41.5%, model 36.4% (market_conditioned_v1 (model4_board_v1)) -- gap -5.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01HUMLEH-LEH3` Will Jiri Lehecka win at least 2.5 more games than Ugo Humbert?: 0.50/0.51 mid 50.5%, model 45.4% (market_conditioned_v1 (model4_board_v1)) -- gap -5.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01HUMLEH-LEH21` Will Jiri Lehecka win the Ugo Humbert vs Jiri Lehecka match by a set score of 2-1?: 0.22/0.26 mid 24.0%, model 28.9% (market_conditioned_v1 (model4_board_v1)) -- gap +4.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01HUMLEH-HUM21` Will Ugo Humbert win the Ugo Humbert vs Jiri Lehecka match by a set score of 2-1?: 0.14/0.17 mid 15.5%, model 19.0% (market_conditioned_v1 (model4_board_v1)) -- gap +3.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01HUMLEH-HUM2` Will Ugo Humbert win at least 1.5 more games than Jiri Lehecka?: 0.27/0.31 mid 29.0%, model 26.7% (market_conditioned_v1 (model4_board_v1)) -- gap -2.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01HUMLEH-HUM20` Will Ugo Humbert win the Ugo Humbert vs Jiri Lehecka match by a set score of 2-0?: 0.17/0.19 mid 18.0%, model 15.7% (market_conditioned_v1 (model4_board_v1)) -- gap -2.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Kyrian Jacquet vs Luciano Darderi -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208021:209260:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciano Darderi (`KXATPMATCH-26OCT01JACDAR-DAR`) | 0.55 / 0.57 (19532) | 56.0% | -- | 39.2% | 41.6% [37.8%-49.5%] | -- | 56.4% | 56.4% | MODEL_LONE_OUTLIER | PASS | -14.4 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Kyrian Jacquet (`KXATPMATCH-26OCT01JACDAR-JAC`) | 0.43 / 0.45 (17044) | 44.0% | -- | 60.8% | 58.4% [50.5%-62.2%] | -- | 44.1% | 44.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +14.4 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4700.0, B 7374.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0584
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.029, surface_dev_loose +0.038, surface_dev_tight -0.039
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01JACDAR-24` Over 23.5 games: 0.45/0.46 mid 45.5%, model 54.9% (market_conditioned_v1 (model4_board_v1)) -- gap +9.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01JACDAR-29` Over 28.5 games: 0.27/0.30 mid 28.5%, model 36.6% (market_conditioned_v1 (model4_board_v1)) -- gap +8.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01JACDAR-19` Over 18.5 games: 0.82/0.85 mid 83.5%, model 88.9% (market_conditioned_v1 (model4_board_v1)) -- gap +5.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01JACDAR-DAR21` Will Luciano Darderi win the Kyrian Jacquet vs Luciano Darderi match by a set score of 2-1?: 0.20/0.23 mid 21.5%, model 26.8% (market_conditioned_v1 (model4_board_v1)) -- gap +5.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01JACDAR-JAC21` Will Kyrian Jacquet win the Kyrian Jacquet vs Luciano Darderi match by a set score of 2-1?: 0.17/0.21 mid 19.0%, model 22.9% (market_conditioned_v1 (model4_board_v1)) -- gap +3.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01JACDAR-DAR20` Will Luciano Darderi win the Kyrian Jacquet vs Luciano Darderi match by a set score of 2-0?: 0.31/0.34 mid 32.5%, model 29.1% (market_conditioned_v1 (model4_board_v1)) -- gap -3.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01JACDAR-JAC20` Will Kyrian Jacquet win the Kyrian Jacquet vs Luciano Darderi match by a set score of 2-0?: 0.23/0.26 mid 24.5%, model 21.2% (market_conditioned_v1 (model4_board_v1)) -- gap -3.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01JACDAR-DAR5` Will Luciano Darderi win at least 4.5 more games than Kyrian Jacquet?: 0.20/0.23 mid 21.5%, model 19.1% (market_conditioned_v1 (model4_board_v1)) -- gap -2.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01JACDAR-JAC2` Will Kyrian Jacquet win at least 1.5 more games than Luciano Darderi?: 0.37/0.41 mid 39.0%, model 36.7% (market_conditioned_v1 (model4_board_v1)) -- gap -2.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01JACDAR-DAR2` Will Luciano Darderi win at least 1.5 more games than Kyrian Jacquet?: 0.49/0.51 mid 50.0%, model 48.3% (market_conditioned_v1 (model4_board_v1)) -- gap -1.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; THIN_DISPLAYED_SIZE

## Jaume Munar vs Jaime Faria -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144719:210262:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jaime Faria (`KXATPMATCH-26OCT01MUNFAR-FAR`) | 0.37 / 0.38 (4612) | 37.5% | -- | 34.1% | 38.8% [35.9%-42.1%] | -- | 37.9% | 37.9% | MARKETS_AGREE | PASS | +1.3 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Jaume Munar (`KXATPMATCH-26OCT01MUNFAR-MUN`) | 0.61 / 0.62 (2021) | 61.5% | -- | 65.9% | 61.2% [57.9%-64.0%] | -- | 62.5% | 62.5% | MARKETS_AGREE | PASS | -0.3 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4944.0, B 5916.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0306
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.001, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01MUNFAR-23` Over 22.5 games: 0.49/0.51 mid 50.0%, model 60.8% (market_conditioned_v1 (model4_board_v1)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01MUNFAR-28` Over 27.5 games: 0.28/0.32 mid 30.0%, model 40.6% (market_conditioned_v1 (model4_board_v1)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01MUNFAR-MUN6` Will Jaume Munar win at least 5.5 more games than Jaime Faria?: 0.20/0.23 mid 21.5%, model 12.2% (market_conditioned_v1 (model4_board_v1)) -- gap -9.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MUNFAR-MUN21` Will Jaume Munar win the Jaume Munar vs Jaime Faria match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 28.3% (market_conditioned_v1 (model4_board_v1)) -- gap +5.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01MUNFAR-MUN3` Will Jaume Munar win at least 2.5 more games than Jaime Faria?: 0.51/0.52 mid 51.5%, model 46.5% (market_conditioned_v1 (model4_board_v1)) -- gap -5.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MUNFAR-MUN20` Will Jaume Munar win the Jaume Munar vs Jaime Faria match by a set score of 2-0?: 0.37/0.40 mid 38.5%, model 33.7% (market_conditioned_v1 (model4_board_v1)) -- gap -4.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MUNFAR-FAR21` Will Jaime Faria win the Jaume Munar vs Jaime Faria match by a set score of 2-1?: 0.15/0.18 mid 16.5%, model 20.4% (market_conditioned_v1 (model4_board_v1)) -- gap +3.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01MUNFAR-18` Over 17.5 games: 0.86/0.95 mid 90.5%, model 93.7% (market_conditioned_v1 (model4_board_v1)) -- gap +3.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MUNFAR-FAR20` Will Jaime Faria win the Jaume Munar vs Jaime Faria match by a set score of 2-0?: 0.18/0.22 mid 20.0%, model 17.6% (market_conditioned_v1 (model4_board_v1)) -- gap -2.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01MUNFAR-FAR2` Will Jaime Faria win at least 1.5 more games than Jaume Munar?: 0.30/0.33 mid 31.5%, model 30.9% (market_conditioned_v1 (model4_board_v1)) -- gap -0.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Denis Shapovalov vs Alejandro Tabilo -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126214:133430:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Denis Shapovalov (`KXATPMATCH-26OCT01SHATAB-SHA`) | 0.55 / 0.58 (77) | 56.5% | -- | 48.5% | 51.0% [49.5%-52.9%] | -- | -- | -- | -- | PASS | -5.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Tabilo (`KXATPMATCH-26OCT01SHATAB-TAB`) | 0.40 / 0.44 (1802) | 42.0% | -- | 51.5% | 49.0% [47.1%-50.5%] | -- | -- | -- | -- | SHADOW_BET | +7.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4723.0, B 7913.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0172
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.020, surface_dev_loose +0.010, surface_dev_tight -0.005
* Derivatives listed: 6 (GAME_SPREAD, MATCH_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXATPGTOTAL-26OCT01SHATAB-19` Over 18.5 games: 0.62/0.99 mid 80.5%, model 90.2% (market_conditioned_v1 (model4_board_v1)) -- gap +9.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01SHATAB-SHA6` Will Denis Shapovalov win at least 5.5 more games than Alejandro Tabilo?: 0.01/0.36 mid 18.5%, model 9.3% (market_conditioned_v1 (model4_board_v1)) -- gap -9.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01SHATAB-29` Over 28.5 games: 0.10/0.51 mid 30.5%, model 38.0% (market_conditioned_v1 (model4_board_v1)) -- gap +7.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01SHATAB-24` Over 23.5 games: 0.47/0.55 mid 51.0%, model 55.5% (market_conditioned_v1 (model4_board_v1)) -- gap +4.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01SHATAB-SHA3` Will Denis Shapovalov win at least 2.5 more games than Alejandro Tabilo?: 0.42/0.45 mid 43.5%, model 40.9% (market_conditioned_v1 (model4_board_v1)) -- gap -2.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01SHATAB-TAB2` Will Alejandro Tabilo win at least 1.5 more games than Denis Shapovalov?: 0.36/0.40 mid 38.0%, model 35.5% (market_conditioned_v1 (model4_board_v1)) -- gap -2.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Valentin Vacherot vs Stefanos Tsitsipas -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126774:200473:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefanos Tsitsipas (`KXATPMATCH-26OCT01VACTSI-TSI`) | 0.60 / 0.61 (22248) | 60.5% | -- | 48.1% | 49.1% [47.2%-56.1%] | -- | 59.6% | 59.6% | MARKETS_AGREE | PASS | -11.4 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Valentin Vacherot (`KXATPMATCH-26OCT01VACTSI-VAC`) | 0.39 / 0.40 (865) | 39.5% | -- | 51.9% | 50.9% [43.9%-52.8%] | -- | 40.7% | 40.7% | MARKETS_AGREE | SHADOW_BET | +11.4 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5393.0, B 5388.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0446
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.019, surface_dev_loose +0.009, surface_dev_tight -0.014
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01VACTSI-29` Over 28.5 games: 0.30/0.33 mid 31.5%, model 43.3% (market_conditioned_v1 (model4_board_v1)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01VACTSI-24` Over 23.5 games: 0.47/0.49 mid 48.0%, model 59.6% (market_conditioned_v1 (model4_board_v1)) -- gap +11.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01VACTSI-TSI6` Will Stefanos Tsitsipas win at least 5.5 more games than Valentin Vacherot?: 0.01/0.32 mid 16.5%, model 5.3% (market_conditioned_v1 (model4_board_v1)) -- gap -11.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01VACTSI-19` Over 18.5 games: 0.84/0.88 mid 86.0%, model 95.3% (market_conditioned_v1 (model4_board_v1)) -- gap +9.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01VACTSI-TSI21` Will Stefanos Tsitsipas win the Valentin Vacherot vs Stefanos Tsitsipas match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 27.9% (market_conditioned_v1 (model4_board_v1)) -- gap +4.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01VACTSI-TSI3` Will Stefanos Tsitsipas win at least 2.5 more games than Valentin Vacherot?: 0.43/0.45 mid 44.0%, model 39.8% (market_conditioned_v1 (model4_board_v1)) -- gap -4.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01VACTSI-VAC20` Will Valentin Vacherot win the Valentin Vacherot vs Stefanos Tsitsipas match by a set score of 2-0?: 0.21/0.23 mid 22.0%, model 18.5% (market_conditioned_v1 (model4_board_v1)) -- gap -3.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01VACTSI-VAC21` Will Valentin Vacherot win the Valentin Vacherot vs Stefanos Tsitsipas match by a set score of 2-1?: 0.16/0.20 mid 18.0%, model 21.1% (market_conditioned_v1 (model4_board_v1)) -- gap +3.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01VACTSI-TSI20` Will Stefanos Tsitsipas win the Valentin Vacherot vs Stefanos Tsitsipas match by a set score of 2-0?: 0.34/0.37 mid 35.5%, model 32.5% (market_conditioned_v1 (model4_board_v1)) -- gap -3.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01VACTSI-VAC2` Will Valentin Vacherot win at least 1.5 more games than Stefanos Tsitsipas?: 0.32/0.35 mid 33.5%, model 30.9% (market_conditioned_v1 (model4_board_v1)) -- gap -2.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alex de Minaur vs Quentin Halys -- ATP Beijing R16

ATP (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111460:200282:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex de Minaur (`KXATPMATCH-26OCT01DEHAL-DE`) | 0.73 / 0.75 (16634) | 74.0% | -- | 79.4% | 79.1% [77.8%-79.7%] | -- | -- | -- | -- | SHADOW_BET | +5.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Quentin Halys (`KXATPMATCH-26OCT01DEHAL-HAL`) | 0.25 / 0.27 (21527) | 26.0% | -- | 20.6% | 20.9% [20.3%-22.2%] | -- | -- | -- | -- | PASS | -5.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 7096.0, B 7371.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0097
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.004, surface_dev_loose -0.001, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01DEHAL-22` Over 21.5 games: 0.54/0.56 mid 55.0%, model 66.5% (market_conditioned_v1 (model4_board_v1)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01DEHAL-DE8` Will Alex de Minaur win at least 7.5 more games than Quentin Halys?: 0.02/0.24 mid 13.0%, model 2.9% (market_conditioned_v1 (model4_board_v1)) -- gap -10.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01DEHAL-27` Over 26.5 games: 0.30/0.34 mid 32.0%, model 40.8% (market_conditioned_v1 (model4_board_v1)) -- gap +8.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01DEHAL-DE21` Will Alex de Minaur win the Alex de Minaur vs Quentin Halys match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 29.6% (market_conditioned_v1 (model4_board_v1)) -- gap +6.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01DEHAL-DE20` Will Alex de Minaur win the Alex de Minaur vs Quentin Halys match by a set score of 2-0?: 0.49/0.52 mid 50.5%, model 43.9% (market_conditioned_v1 (model4_board_v1)) -- gap -6.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01DEHAL-DE5` Will Alex de Minaur win at least 4.5 more games than Quentin Halys?: 0.35/0.36 mid 35.5%, model 29.3% (market_conditioned_v1 (model4_board_v1)) -- gap -6.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01DEHAL-17` Over 16.5 games: 0.92/0.96 mid 94.0%, model 97.2% (market_conditioned_v1 (model4_board_v1)) -- gap +3.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01DEHAL-HAL21` Will Quentin Halys win the Alex de Minaur vs Quentin Halys match by a set score of 2-1?: 0.11/0.13 mid 12.0%, model 15.1% (market_conditioned_v1 (model4_board_v1)) -- gap +3.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01DEHAL-DE2` Will Alex de Minaur win at least 1.5 more games than Quentin Halys?: 0.54/0.75 mid 64.5%, model 66.7% (market_conditioned_v1 (model4_board_v1)) -- gap +2.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01DEHAL-HAL20` Will Quentin Halys win the Alex de Minaur vs Quentin Halys match by a set score of 2-0?: 0.11/0.14 mid 12.5%, model 11.4% (market_conditioned_v1 (model4_board_v1)) -- gap -1.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alex Molcan vs Karen Khachanov -- ATP Beijing R16

ATP (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111575:144684:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karen Khachanov (`KXATPMATCH-26OCT01MOLKHA-KHA`) | 0.79 / 0.80 (22611) | 79.5% | -- | 70.7% | 71.2% [67.3%-72.3%] | -- | 78.5% | 78.5% | MODEL_LONE_OUTLIER | PASS | -8.3 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Alex Molcan (`KXATPMATCH-26OCT01MOLKHA-MOL`) | 0.21 / 0.22 (8406) | 21.5% | -- | 29.3% | 28.8% [27.7%-32.6%] | -- | 22.0% | 22.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.3 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3805.0, B 5981.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0249
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.008, surface_dev_loose -0.012, surface_dev_tight +0.012
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01MOLKHA-22` Over 21.5 games: 0.48/0.50 mid 49.0%, model 61.6% (market_conditioned_v1 (model4_board_v1)) -- gap +12.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01MOLKHA-KHA8` Will Karen Khachanov win at least 7.5 more games than Alex Molcan?: 0.02/0.31 mid 16.5%, model 4.6% (market_conditioned_v1 (model4_board_v1)) -- gap -11.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01MOLKHA-KHA5` Will Karen Khachanov win at least 4.5 more games than Alex Molcan?: 0.46/0.48 mid 47.0%, model 36.1% (market_conditioned_v1 (model4_board_v1)) -- gap -10.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01MOLKHA-27` Over 26.5 games: 0.25/0.29 mid 27.0%, model 37.3% (market_conditioned_v1 (model4_board_v1)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MOLKHA-KHA20` Will Karen Khachanov win the Alex Molcan vs Karen Khachanov match by a set score of 2-0?: 0.55/0.58 mid 56.5%, model 49.0% (market_conditioned_v1 (model4_board_v1)) -- gap -7.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MOLKHA-KHA21` Will Karen Khachanov win the Alex Molcan vs Karen Khachanov match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 29.4% (market_conditioned_v1 (model4_board_v1)) -- gap +6.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01MOLKHA-17` Over 16.5 games: 0.88/0.92 mid 90.0%, model 95.7% (market_conditioned_v1 (model4_board_v1)) -- gap +5.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01MOLKHA-KHA2` Will Karen Khachanov win at least 1.5 more games than Alex Molcan?: 0.74/0.78 mid 76.0%, model 72.5% (market_conditioned_v1 (model4_board_v1)) -- gap -3.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MOLKHA-MOL21` Will Alex Molcan win the Alex Molcan vs Karen Khachanov match by a set score of 2-1?: 0.09/0.11 mid 10.0%, model 12.6% (market_conditioned_v1 (model4_board_v1)) -- gap +2.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MOLKHA-MOL20` Will Alex Molcan win the Alex Molcan vs Karen Khachanov match by a set score of 2-0?: 0.08/0.11 mid 9.5%, model 9.0% (market_conditioned_v1 (model4_board_v1)) -- gap -0.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yunchaokete Bu vs Novak Djokovic -- ATP Beijing R16

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT01YUNDJO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Novak Djokovic (`KXATPMATCH-26OCT01YUNDJO-DJO`) | 0.76 / 0.77 (37523) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yunchaokete Bu (`KXATPMATCH-26OCT01YUNDJO-YUN`) | 0.23 / 0.25 (8858) | 24.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexander Zverev vs Juncheng Shang -- ATP Beijing R16

ATP (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:100644:209992:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juncheng Shang (`KXATPMATCH-26OCT01ZVESHA-SHA`) | 0.08 / 0.11 (25) | 9.5% | -- | 11.4% | 12.8% [11.1%-14.7%] | -- | -- | -- | -- | WATCH | +3.4 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Zverev (`KXATPMATCH-26OCT01ZVESHA-ZVE`) | 0.88 / 0.91 (2221) | 89.5% | -- | 88.6% | 87.2% [85.3%-88.9%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 8165.0, B 3774.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0182
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.018, surface_dev_loose -0.001, surface_dev_tight +0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGSPREAD-26OCT01ZVESHA-ZVE6` Will Alexander Zverev win at least 5.5 more games than Juncheng Shang?: 0.28/0.65 mid 46.5%, model 24.3% (market_conditioned_v1 (model4_board_v1)) -- gap -22.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01ZVESHA-20` Over 19.5 games: 0.48/0.56 mid 52.0%, model 72.4% (market_conditioned_v1 (model4_board_v1)) -- gap +20.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01ZVESHA-ZVE9` Will Alexander Zverev win at least 8.5 more games than Juncheng Shang?: 0.01/0.29 mid 15.0%, model 1.8% (market_conditioned_v1 (model4_board_v1)) -- gap -13.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01ZVESHA-15` Over 14.5 games: 0.75/0.99 mid 87.0%, model 99.6% (market_conditioned_v1 (model4_board_v1)) -- gap +12.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01ZVESHA-25` Over 24.5 games: 0.08/0.47 mid 27.5%, model 37.9% (market_conditioned_v1 (model4_board_v1)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01ZVESHA-ZVE20` Will Alexander Zverev win the Alexander Zverev vs Juncheng Shang match by a set score of 2-0?: 0.69/0.72 mid 70.5%, model 63.4% (market_conditioned_v1 (model4_board_v1)) -- gap -7.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01ZVESHA-ZVE21` Will Alexander Zverev win the Alexander Zverev vs Juncheng Shang match by a set score of 2-1?: 0.17/0.21 mid 19.0%, model 25.9% (market_conditioned_v1 (model4_board_v1)) -- gap +6.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01ZVESHA-SHA21` Will Juncheng Shang win the Alexander Zverev vs Juncheng Shang match by a set score of 2-1?: 0.03/0.07 mid 5.0%, model 6.6% (market_conditioned_v1 (model4_board_v1)) -- gap +1.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01ZVESHA-ZVE3` Will Alexander Zverev win at least 2.5 more games than Juncheng Shang?: 0.69/0.87 mid 78.0%, model 76.5% (market_conditioned_v1 (model4_board_v1)) -- gap -1.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ekaterina Alexandrova vs Aliaksandra Sasnovich -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:205925:206420:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Alexandrova (`KXWTAMATCH-26OCT01ALESAS-ALE`) | 0.59 / 0.60 (13748) | 59.5% | -- | 60.4% | 61.4% [59.9%-64.9%] | 58.3% | 57.7% | 58.3% | MODEL_LONE_OUTLIER | PASS | +1.9 pp | NORMAL | STALE | A / LIMITED | ALL_AGREE | VERIFIED |
| Aliaksandra Sasnovich (`KXWTAMATCH-26OCT01ALESAS-SAS`) | 0.40 / 0.41 (340) | 40.5% | -- | 39.6% | 38.6% [35.1%-40.1%] | 41.7% | 42.5% | 42.1% | MODEL_LONE_OUTLIER | PASS | -1.9 pp | NORMAL | STALE | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4877.0, B 4822.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0251
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose -0.010, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01ALESAS-23` Over 22.5 games: 0.44/0.46 mid 45.0%, model 55.7% (market_conditioned_v1 (model4_board_v1)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01ALESAS-28` Over 27.5 games: 0.21/0.27 mid 24.0%, model 34.2% (market_conditioned_v1 (model4_board_v1)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01ALESAS-18` Over 17.5 games: 0.74/0.82 mid 78.0%, model 87.8% (market_conditioned_v1 (model4_board_v1)) -- gap +9.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Nikola Bartunkova vs Magdalena Frech -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211684:223360:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikola Bartunkova (`KXWTAMATCH-26OCT01BARFRE-BAR`) | 0.57 / 0.59 (10972) | 58.0% | -- | 57.8% | 56.3% [50.5%-58.9%] | 58.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Magdalena Frech (`KXWTAMATCH-26OCT01BARFRE-FRE`) | 0.41 / 0.42 (842) | 41.5% | -- | 42.2% | 43.7% [41.1%-49.5%] | 41.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3248.0, B 4552.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0416
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.021, surface_dev_loose +0.005, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01BARFRE-22` Over 21.5 games: 0.53/0.54 mid 53.5%, model 62.8% (market_conditioned_v1 (model4_board_v1)) -- gap +9.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01BARFRE-17` Over 16.5 games: 0.83/0.91 mid 87.0%, model 93.9% (market_conditioned_v1 (model4_board_v1)) -- gap +6.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01BARFRE-27` Over 26.5 games: 0.29/0.37 mid 33.0%, model 39.6% (market_conditioned_v1 (model4_board_v1)) -- gap +6.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Sara Bejlek vs Maddison Inglis -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213666:239383:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Bejlek (`KXWTAMATCH-26OCT01BEJING-BEJ`) | 0.74 / 0.75 (2024) | 74.5% | -- | 76.3% | 73.8% [69.7%-74.6%] | 73.4% | 73.4% | 73.4% | MARKETS_AGREE | PASS | -0.7 pp | NORMAL | STALE | A / LIMITED | ALL_AGREE | VERIFIED |
| Maddison Inglis (`KXWTAMATCH-26OCT01BEJING-ING`) | 0.25 / 0.26 (8170) | 25.5% | -- | 23.7% | 26.2% [25.4%-30.3%] | 26.7% | 26.2% | 26.4% | MARKETS_AGREE | PASS | +0.7 pp | NORMAL | STALE | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3433.0, B 3027.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0244
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.018, surface_dev_loose +0.009, surface_dev_tight -0.009
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01BEJING-21` Over 20.5 games: 0.47/0.49 mid 48.0%, model 61.5% (market_conditioned_v1 (model4_board_v1)) -- gap +13.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01BEJING-26` Over 25.5 games: 0.23/0.31 mid 27.0%, model 38.9% (market_conditioned_v1 (model4_board_v1)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01BEJING-16` Over 15.5 games: 0.85/0.93 mid 89.0%, model 95.5% (market_conditioned_v1 (model4_board_v1)) -- gap +6.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
* Warnings: STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Belinda Bencic vs Anastasia Zakharova -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202505:220435:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Belinda Bencic (`KXWTAMATCH-26OCT01BENZAK-BEN`) | 0.78 / 0.81 (3175) | 79.5% | -- | 77.8% | 79.3% [77.0%-82.6%] | -- | -- | -- | -- | PASS | -0.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Zakharova (`KXWTAMATCH-26OCT01BENZAK-ZAK`) | 0.18 / 0.21 (4) | 19.5% | -- | 22.2% | 20.7% [17.4%-23.0%] | -- | -- | -- | -- | PASS | +1.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3571.0, B 4628.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0279
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.023, surface_dev_loose +0.004, surface_dev_tight -0.000
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Marie Bouzkova vs Kimberly Birrell -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213631:214040:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kimberly Birrell (`KXWTAMATCH-26OCT01BOUBIR-BIR`) | 0.33 / 0.35 (4194) | 34.0% | -- | 45.8% | 43.6% [39.5%-45.2%] | -- | -- | -- | -- | SHADOW_BET | +9.7 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marie Bouzkova (`KXWTAMATCH-26OCT01BOUBIR-BOU`) | 0.62 / 0.66 (115) | 64.0% | -- | 54.2% | 56.4% [54.8%-60.5%] | -- | -- | -- | -- | PASS | -7.7 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4089.0, B 5020.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0286
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.016, surface_dev_loose -0.011, surface_dev_tight +0.005
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Linda Fruhvirtova vs Liudmila Samsonova -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214643:222258:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linda Fruhvirtova (`KXWTAMATCH-26OCT01FRUSAM-FRU`) | 0.18 / 0.19 (1234) | 18.5% | -- | 43.7% | 39.6% [28.0%-43.7%] | 20.2% | 18.7% | 19.4% | MODEL_LONE_OUTLIER | WATCH | +21.1 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Liudmila Samsonova (`KXWTAMATCH-26OCT01FRUSAM-SAM`) | 0.80 / 0.82 (15613) | 81.0% | -- | 56.3% | 60.4% [56.3%-72.0%] | 79.8% | 82.3% | 81.1% | MODEL_LONE_OUTLIER | PASS | -20.6 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

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
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.040, surface_pool_high +0.041, surface_dev_loose +0.021, surface_dev_tight -0.020
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01FRUSAM-21` Over 20.5 games: 0.44/0.46 mid 45.0%, model 56.9% (market_conditioned_v1 (model4_board_v1)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01FRUSAM-16` Over 15.5 games: 0.82/0.90 mid 86.0%, model 94.2% (market_conditioned_v1 (model4_board_v1)) -- gap +8.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01FRUSAM-26` Over 25.5 games: 0.22/0.32 mid 27.0%, model 34.9% (market_conditioned_v1 (model4_board_v1)) -- gap +7.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Viktorija Golubic vs Peyton Stearns -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:203530:220548:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viktorija Golubic (`KXWTAMATCH-26OCT01GOLSTE-GOL`) | 0.40 / 0.41 (125) | 40.5% | -- | 45.8% | 47.4% [46.8%-48.4%] | 40.6% | 41.8% | 41.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.9 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Peyton Stearns (`KXWTAMATCH-26OCT01GOLSTE-STE`) | 0.59 / 0.60 (8807) | 59.5% | -- | 54.2% | 52.6% [51.6%-53.2%] | 59.4% | 59.2% | 59.3% | MODEL_LONE_OUTLIER | PASS | -6.9 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4714.0, B 4027.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0079
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01GOLSTE-21` Over 20.5 games: 0.54/0.56 mid 55.0%, model 66.9% (market_conditioned_v1 (model4_board_v1)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01GOLSTE-26` Over 25.5 games: 0.28/0.36 mid 32.0%, model 43.7% (market_conditioned_v1 (model4_board_v1)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01GOLSTE-16` Over 15.5 games: 0.89/0.96 mid 92.5%, model 97.0% (market_conditioned_v1 (model4_board_v1)) -- gap +4.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Sonay Kartal vs Xinyu Wang -- WTA Beijing R64

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT01KARWAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sonay Kartal (`KXWTAMATCH-26OCT01KARWAN-KAR`) | 0.50 / 0.54 (4592) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xinyu Wang (`KXWTAMATCH-26OCT01KARWAN-WAN`) | 0.45 / 0.48 (1362) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ashlyn Krueger vs Ann Li -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215983:221909:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ann Li (`KXWTAMATCH-26OCT01KRUANN-ANN`) | 0.52 / 0.55 (148) | 53.5% | -- | 63.7% | 60.2% [55.7%-61.7%] | -- | -- | -- | -- | WATCH | +6.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ashlyn Krueger (`KXWTAMATCH-26OCT01KRUANN-KRU`) | 0.43 / 0.47 (43) | 45.0% | -- | 36.3% | 39.8% [38.3%-44.3%] | -- | -- | -- | -- | PASS | -5.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4211.0, B 4567.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0301
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose -0.010, surface_dev_tight +0.010
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Karolina Muchova vs Katie Boulter -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211107:214096:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katie Boulter (`KXWTAMATCH-26OCT01MUCBOU-BOU`) | 0.12 / 0.13 (2009) | 12.5% | -- | 24.1% | 22.9% [22.1%-23.7%] | 14.7% | 12.1% | 13.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.4 pp | REVIEW | STALE | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Karolina Muchova (`KXWTAMATCH-26OCT01MUCBOU-MUC`) | 0.87 / 0.88 (8647) | 87.5% | -- | 75.9% | 77.1% [76.3%-77.9%] | 85.3% | 87.4% | 86.4% | MODEL_LONE_OUTLIER | PASS | -10.4 pp | REVIEW | STALE | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3972.0, B 3928.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0078
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high +0.000, surface_dev_loose +0.008, surface_dev_tight -0.008
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT01MUCBOU-19` Over 18.5 games: 0.50/0.51 mid 50.5%, model 68.7% (market_conditioned_v1 (model4_board_v1)) -- gap +18.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01MUCBOU-24` Over 23.5 games: 0.20/0.26 mid 23.0%, model 36.5% (market_conditioned_v1 (model4_board_v1)) -- gap +13.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
* Warnings: STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mio Mushika vs Yuno Kitahara -- W35 Wagga Wagga QF

ITF (ITF) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222986:263881:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuno Kitahara (`KXITFWMATCH-26OCT01MUSKIT-KIT`) | 0.39 / 0.43 (128) | 41.0% | -- | 33.9% | 35.4% [34.4%-37.4%] | 41.9% | -- | 41.9% | MODEL_LONE_OUTLIER | PASS | -5.6 pp | NORMAL | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Mio Mushika (`KXITFWMATCH-26OCT01MUSKIT-MUS`) | 0.53 / 0.60 (29) | 56.5% | -- | 66.1% | 64.6% [62.6%-65.6%] | 58.1% | -- | 58.1% | MODEL_LONE_OUTLIER | PASS | +8.1 pp | NORMAL | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2224.0, B 2068.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.015
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Linda Noskova vs Elena-Gabriela Ruse -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211817:222328:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linda Noskova (`KXWTAMATCH-26OCT01NOSRUS-NOS`) | 0.77 / 0.79 (11497) | 78.0% | -- | 64.5% | 67.8% [66.9%-70.5%] | 76.2% | 78.5% | 78.5% | MODEL_LONE_OUTLIER | PASS | -10.2 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Elena-Gabriela Ruse (`KXWTAMATCH-26OCT01NOSRUS-RUS`) | 0.21 / 0.22 (1394) | 21.5% | -- | 35.5% | 32.2% [29.5%-33.1%] | 23.8% | 21.5% | 21.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.7 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4568.0, B 4254.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0182
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.018, surface_dev_loose +0.009, surface_dev_tight -0.004
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01NOSRUS-26` Over 25.5 games: 0.21/0.29 mid 25.0%, model 39.4% (market_conditioned_v1 (model4_board_v1)) -- gap +14.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01NOSRUS-21` Over 20.5 games: 0.49/0.51 mid 50.0%, model 62.6% (market_conditioned_v1 (model4_board_v1)) -- gap +12.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01NOSRUS-16` Over 15.5 games: 0.85/0.94 mid 89.5%, model 96.8% (market_conditioned_v1 (model4_board_v1)) -- gap +7.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jelena Ostapenko vs Paula Badosa -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211533:211651:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Paula Badosa (`KXWTAMATCH-26OCT01OSTBAD-BAD`) | 0.61 / 0.64 (4491) | 62.5% | -- | 63.5% | 62.0% [57.9%-63.0%] | -- | -- | -- | -- | PASS | -0.5 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jelena Ostapenko (`KXWTAMATCH-26OCT01OSTBAD-OST`) | 0.35 / 0.38 (1015) | 36.5% | -- | 36.5% | 38.0% [37.0%-42.1%] | -- | -- | -- | -- | PASS | +1.5 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3919.0, B 3479.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0255
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.010
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Jasmine Paolini vs Daria Snigur -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211148:220750:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jasmine Paolini (`KXWTAMATCH-26OCT01PAOSNI-PAO`) | 0.58 / 0.59 (3678) | 58.5% | -- | 23.2% | 33.5% [27.4%-53.7%] | 59.4% | 59.0% | 59.2% | MODEL_LONE_OUTLIER | PASS | -25.0 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Daria Snigur (`KXWTAMATCH-26OCT01PAOSNI-SNI`) | 0.40 / 0.41 (5) | 40.5% | -- | 76.8% | 66.5% [46.3%-72.6%] | 40.6% | 41.2% | 40.9% | MODEL_LONE_OUTLIER | WATCH | +26.0 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4852.0, B 4190.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1314
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01PAOSNI-SNI  (YES = Daria Snigur)
Model: 67%
Kalshi: 40%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.019, surface_dev_loose -0.024, surface_dev_tight +0.029
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01PAOSNI-22` Over 21.5 games: 0.48/0.49 mid 48.5%, model 61.5% (market_conditioned_v1 (model4_board_v1)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01PAOSNI-27` Over 26.5 games: 0.23/0.31 mid 27.0%, model 38.2% (market_conditioned_v1 (model4_board_v1)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01PAOSNI-17` Over 16.5 games: 0.82/0.90 mid 86.0%, model 92.8% (market_conditioned_v1 (model4_board_v1)) -- gap +6.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anastasia Potapova vs Sinja Kraus -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215713:221257:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sinja Kraus (`KXWTAMATCH-26OCT01POTKRA-KRA`) | 0.25 / 0.26 (1146) | 25.5% | -- | 54.2% | 45.8% [35.5%-49.5%] | 26.7% | 26.0% | 26.0% | MODEL_LONE_OUTLIER | WATCH | +20.3 pp | HIGH_REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Anastasia Potapova (`KXWTAMATCH-26OCT01POTKRA-POT`) | 0.74 / 0.75 (18300) | 74.5% | -- | 45.8% | 54.2% [50.5%-64.5%] | 73.4% | 73.8% | 73.8% | MODEL_LONE_OUTLIER | PASS | -20.3 pp | HIGH_REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4594.0, B 5054.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.07
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01POTKRA-KRA  (YES = Sinja Kraus)
Model: 46%
Kalshi: 26%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.016
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01POTKRA-15` Over 14.5 games: 0.02/0.99 mid 50.5%, model 98.2% (market_conditioned_v1 (model4_board_v1)) -- gap +47.7 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01POTKRA-20` Over 19.5 games: 0.55/0.57 mid 56.0%, model 67.8% (market_conditioned_v1 (model4_board_v1)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01POTKRA-25` Over 24.5 games: 0.29/0.35 mid 32.0%, model 42.9% (market_conditioned_v1 (model4_board_v1)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Taylah Preston vs Diane Parry -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220348:223194:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diane Parry (`KXWTAMATCH-26OCT01PREPAR-PAR`) | 0.55 / 0.56 (3804) | 55.5% | -- | 19.4% | 24.8% [19.7%-43.7%] | 55.6% | 53.9% | 53.9% | MODEL_LONE_OUTLIER | PASS | -30.7 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Taylah Preston (`KXWTAMATCH-26OCT01PREPAR-PRE`) | 0.43 / 0.44 (1785) | 43.5% | -- | 80.7% | 75.2% [56.3%-80.3%] | 44.4% | 45.1% | 45.1% | MODEL_LONE_OUTLIER | WATCH | +31.7 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5098.0, B 3742.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1199
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01PREPAR-PRE  (YES = Taylah Preston)
Model: 75%
Kalshi: 44%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.043, surface_pool_high +0.040, surface_dev_loose +0.012, surface_dev_tight -0.012
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01PREPAR-23` Over 22.5 games: 0.45/0.47 mid 46.0%, model 56.8% (market_conditioned_v1 (model4_board_v1)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01PREPAR-28` Over 27.5 games: 0.23/0.28 mid 25.5%, model 35.4% (market_conditioned_v1 (model4_board_v1)) -- gap +9.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01PREPAR-18` Over 17.5 games: 0.76/0.84 mid 80.0%, model 88.9% (market_conditioned_v1 (model4_board_v1)) -- gap +8.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Kamilla Rakhimova vs Leylah Fernandez -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215872:220367:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leylah Fernandez (`KXWTAMATCH-26OCT01RAKFER-FER`) | 0.72 / 0.75 (3149) | 73.5% | -- | 66.3% | 67.7% [66.8%-68.7%] | -- | -- | -- | -- | PASS | -5.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kamilla Rakhimova (`KXWTAMATCH-26OCT01RAKFER-RAK`) | 0.23 / 0.25 (1) | 24.0% | -- | 33.7% | 32.3% [31.3%-33.2%] | -- | -- | -- | -- | SHADOW_BET | +8.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5718.0, B 4828.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0094
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.009
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Elena Rybakina vs Alina Charaeva -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214981:221406:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Charaeva (`KXWTAMATCH-26OCT01RYBCHA-CHA`) | 0.09 / 0.10 (1275) | 9.5% | -- | 5.3% | 5.2% [4.9%-5.9%] | -- | -- | -- | -- | PASS | -4.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Rybakina (`KXWTAMATCH-26OCT01RYBCHA-RYB`) | 0.92 / 0.93 (823) | 92.5% | -- | 94.7% | 94.8% [94.1%-95.1%] | -- | -- | -- | -- | SHADOW_BET | +2.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6087.0, B 3668.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0048
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.003, surface_dev_loose -0.001, surface_dev_tight -0.003
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maria Sakkari vs Storm Hunter -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:204411:206289:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Storm Hunter (`KXWTAMATCH-26OCT01SAKHUN-HUN`) | 0.34 / 0.35 (77) | 34.5% | -- | 27.6% | 29.8% [28.0%-32.2%] | -- | -- | -- | -- | PASS | -4.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Sakkari (`KXWTAMATCH-26OCT01SAKHUN-SAK`) | 0.65 / 0.66 (4298) | 65.5% | -- | 72.4% | 70.2% [67.8%-72.0%] | -- | -- | -- | -- | WATCH | +4.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3640.0, B 2089.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0207
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.023, surface_dev_loose -0.009, surface_dev_tight +0.005
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Naho Sato vs Hikaru Sato -- W35 Wagga Wagga QF

ITF (ITF) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220997:221141:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naho Sato (`KXITFWMATCH-26OCT01SATSAT2-SAT`) | 0.54 / 0.58 (150) | 56.0% | -- | 46.8% | 48.9% [47.9%-50.5%] | 56.1% | -- | 56.1% | MODEL_LONE_OUTLIER | PASS | -7.1 pp | NORMAL | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Hikaru Sato (`KXITFWMATCH-26OCT01SATSAT2-SAT2`) | 0.26 / 0.46 (51) | 36.0% | -- | 53.2% | 51.1% [49.5%-52.1%] | 43.9% | -- | 43.9% | KALSHI_LONE_OUTLIER | PASS | +15.1 pp | HIGH_REVIEW | STALE | B / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 1522.0, B 1807.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0133
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01SATSAT2-SAT2  (YES = Hikaru Sato)
Model: 51%
Kalshi: 36%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: B (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kanon Sawashiro vs Nagi Hanatani -- W35 Wagga Wagga QF

ITF (ITF) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211544:263905:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nagi Hanatani (`KXITFWMATCH-26OCT01SAWHAN-HAN`) | 0.16 / 0.19 (24) | 17.5% | -- | 19.5% | 36.4% [28.2%-47.3%] | -- | -- | -- | -- | WATCH | +18.9 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kanon Sawashiro (`KXITFWMATCH-26OCT01SAWHAN-SAW`) | 0.79 / 0.84 (2) | 81.5% | -- | 80.5% | 63.6% [52.7%-71.8%] | -- | -- | -- | -- | PASS | -17.9 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 827.0, B 1219.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0958
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01SAWHAN-HAN  (YES = Nagi Hanatani)
Model: 36%
Kalshi: 18%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katerina Siniakova vs Elina Svitolina -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202494:211701:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katerina Siniakova (`KXWTAMATCH-26OCT01SINSVI-SIN`) | 0.23 / 0.24 (834) | 23.5% | -- | 29.9% | 29.0% [27.2%-29.9%] | -- | -- | -- | -- | SHADOW_BET | +5.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elina Svitolina (`KXWTAMATCH-26OCT01SINSVI-SVI`) | 0.73 / 0.76 (9) | 74.5% | -- | 70.1% | 71.0% [70.1%-72.8%] | -- | -- | -- | -- | PASS | -3.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4278.0, B 4144.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0137
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.009, surface_dev_tight +0.004
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Clara Tauson vs Polina Kudermetova -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220704:221236:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Kudermetova (`KXWTAMATCH-26OCT01TAUKUD-KUD`) | 0.34 / 0.35 (151) | 34.5% | -- | 32.9% | 34.3% [32.4%-40.2%] | 35.4% | 35.9% | 35.6% | MODEL_LONE_OUTLIER | PASS | -0.2 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Clara Tauson (`KXWTAMATCH-26OCT01TAUKUD-TAU`) | 0.64 / 0.66 (13112) | 65.0% | -- | 67.1% | 65.7% [59.8%-67.6%] | 64.6% | 64.3% | 64.5% | MODEL_LONE_OUTLIER | PASS | +0.7 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4452.0, B 4285.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0386
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.009, surface_dev_loose -0.000, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01TAUKUD-26` Over 25.5 games: 0.26/0.35 mid 30.5%, model 44.1% (market_conditioned_v1 (model4_board_v1)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TAUKUD-21` Over 20.5 games: 0.55/0.57 mid 56.0%, model 67.4% (market_conditioned_v1 (model4_board_v1)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TAUKUD-16` Over 15.5 games: 0.88/0.96 mid 92.0%, model 97.5% (market_conditioned_v1 (model4_board_v1)) -- gap +5.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Maria Timofeeva vs Naomi Osaka -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211768:221237:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naomi Osaka (`KXWTAMATCH-26OCT01TIMOSA-OSA`) | 0.77 / 0.78 (2032) | 77.5% | -- | 76.0% | 80.3% [78.0%-81.7%] | 76.2% | 76.7% | 76.7% | MODEL_LONE_OUTLIER | WATCH | +2.8 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Maria Timofeeva (`KXWTAMATCH-26OCT01TIMOSA-TIM`) | 0.21 / 0.22 (3808) | 21.5% | -- | 24.0% | 19.7% [18.3%-22.0%] | 23.8% | 23.0% | 23.0% | MARKETS_AGREE | PASS | -1.8 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3737.0, B 2986.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0182
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.004, surface_dev_loose -0.004, surface_dev_tight +0.004
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01TIMOSA-26` Over 25.5 games: 0.21/0.29 mid 25.0%, model 37.8% (market_conditioned_v1 (model4_board_v1)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TIMOSA-21` Over 20.5 games: 0.49/0.51 mid 50.0%, model 60.4% (market_conditioned_v1 (model4_board_v1)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TIMOSA-16` Over 15.5 games: 0.84/0.99 mid 91.5%, model 95.6% (market_conditioned_v1 (model4_board_v1)) -- gap +4.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Janice Tjen vs Diana Shnaider -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:222145:223670:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diana Shnaider (`KXWTAMATCH-26OCT01TJESHN-SHN`) | 0.73 / 0.74 (17844) | 73.5% | -- | 42.4% | 47.4% [42.4%-63.2%] | 70.6% | 72.5% | 72.5% | MODEL_LONE_OUTLIER | PASS | -26.1 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Janice Tjen (`KXWTAMATCH-26OCT01TJESHN-TJE`) | 0.26 / 0.27 (2321) | 26.5% | -- | 57.6% | 52.5% [36.8%-57.6%] | 29.4% | 27.4% | 27.4% | MODEL_LONE_OUTLIER | WATCH | +26.1 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3631.0, B 4846.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1039
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01TJESHN-TJE  (YES = Janice Tjen)
Model: 53%
Kalshi: 26%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.041, surface_pool_high +0.041, surface_dev_loose -0.000, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01TJESHN-21` Over 20.5 games: 0.51/0.53 mid 52.0%, model 66.0% (market_conditioned_v1 (model4_board_v1)) -- gap +14.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TJESHN-26` Over 25.5 games: 0.26/0.32 mid 29.0%, model 42.4% (market_conditioned_v1 (model4_board_v1)) -- gap +13.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TJESHN-16` Over 15.5 games: 0.85/0.94 mid 89.5%, model 97.5% (market_conditioned_v1 (model4_board_v1)) -- gap +8.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Mutsumi Uemura vs Ashleigh Simes -- W35 Wagga Wagga QF

ITF (ITF) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221929:260828:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashleigh Simes (`KXITFWMATCH-26OCT01UEMSIM-SIM`) | 0.28 / 0.32 (44) | 30.0% | -- | 74.3% | 70.7% [68.5%-74.2%] | -- | -- | -- | -- | PASS | +40.7 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mutsumi Uemura (`KXITFWMATCH-26OCT01UEMSIM-UEM`) | 0.67 / 0.71 (1) | 69.0% | -- | 25.7% | 29.3% [25.8%-31.6%] | -- | -- | -- | -- | PASS | -39.7 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

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
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
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
| Elise Mertens (`KXWTAMATCH-26OCT01VOLMER-MER`) | 0.51 / 0.52 (822) | 51.5% | -- | 76.4% | 73.0% [67.9%-75.1%] | -- | -- | -- | -- | WATCH | +21.5 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katie Volynets (`KXWTAMATCH-26OCT01VOLMER-VOL`) | 0.45 / 0.47 (0) | 46.0% | -- | 23.6% | 27.0% [24.9%-32.1%] | -- | -- | -- | -- | PASS | -19.0 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5386.0, B 3838.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0359
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01VOLMER-MER  (YES = Elise Mertens)
Model: 73%
Kalshi: 52%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.009, surface_dev_tight +0.009
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dayana Yastremska vs Maja Chwalinska -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215035:216081:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maja Chwalinska (`KXWTAMATCH-26OCT01YASCHW-CHW`) | 0.62 / 0.63 (242918) | 62.5% | -- | 81.1% | 72.6% [59.0%-77.3%] | 61.6% | 62.0% | 61.8% | MODEL_LONE_OUTLIER | WATCH | +10.1 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Dayana Yastremska (`KXWTAMATCH-26OCT01YASCHW-YAS`) | 0.37 / 0.38 (3659) | 37.5% | -- | 18.9% | 27.4% [22.7%-41.0%] | 38.4% | 37.8% | 38.1% | MODEL_LONE_OUTLIER | PASS | -10.1 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4632.0, B 3543.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0914
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.022, surface_dev_tight +0.027
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01YASCHW-22` Over 21.5 games: 0.48/0.49 mid 48.5%, model 60.6% (market_conditioned_v1 (model4_board_v1)) -- gap +12.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01YASCHW-27` Over 26.5 games: 0.23/0.29 mid 26.0%, model 37.5% (market_conditioned_v1 (model4_board_v1)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01YASCHW-17` Over 16.5 games: 0.79/0.92 mid 85.5%, model 92.3% (market_conditioned_v1 (model4_board_v1)) -- gap +6.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Yue Yuan vs Mirra Andreeva -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:206294:259799:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mirra Andreeva (`KXWTAMATCH-26OCT01YUAAND-AND`) | 0.92 / 0.93 (15187) | 92.5% | -- | 89.4% | 87.9% [85.1%-88.9%] | 90.5% | 92.2% | 92.2% | MODEL_LONE_OUTLIER | PASS | -4.6 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Yue Yuan (`KXWTAMATCH-26OCT01YUAAND-YUA`) | 0.08 / 0.09 (22040) | 8.5% | -- | 10.6% | 12.1% [11.1%-14.9%] | 9.6% | 7.1% | 7.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.6 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4806.0, B 4895.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0192
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.014, surface_dev_loose -0.005, surface_dev_tight +0.008
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT01YUAAND-19` Over 18.5 games: 0.41/0.44 mid 42.5%, model 61.0% (market_conditioned_v1 (model4_board_v1)) -- gap +18.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01YUAAND-24` Over 23.5 games: 0.10/0.25 mid 17.5%, model 30.6% (market_conditioned_v1 (model4_board_v1)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Renata Zarazua vs Aryna Sabalenka -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213887:214544:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aryna Sabalenka (`KXWTAMATCH-26OCT01ZARSAB-SAB`) | 0.96 / 0.97 (12718) | 96.5% | -- | 95.1% | 95.1% [94.4%-95.5%] | 94.7% | -- | 94.7% | MODEL_LONE_OUTLIER | PASS | -1.4 pp | NORMAL | STALE | A / LIMITED | ALL_AGREE | VERIFIED |
| Renata Zarazua (`KXWTAMATCH-26OCT01ZARSAB-ZAR`) | 0.03 / 0.04 (6967) | 3.5% | -- | 4.9% | 4.9% [4.5%-5.6%] | 5.3% | -- | 5.3% | MODEL_LONE_OUTLIER | PASS | +1.4 pp | NORMAL | STALE | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4923.0, B 5768.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0057
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.003, surface_dev_loose -0.002, surface_dev_tight +0.002
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT01ZARSAB-22` Over 21.5 games: 0.12/0.20 mid 16.0%, model 29.7% (market_conditioned_v1 (model4_board_v1)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01ZARSAB-17` Over 16.5 games: 0.62/0.63 mid 62.5%, model 75.5% (market_conditioned_v1 (model4_board_v1)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
* Warnings: STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Qinwen Zheng vs Anna Kalinskaya -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214939:221012:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Kalinskaya (`KXWTAMATCH-26OCT01ZHEKAL-KAL`) | 0.38 / 0.39 (3205) | 38.5% | -- | 35.8% | 37.8% [35.8%-40.2%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Qinwen Zheng (`KXWTAMATCH-26OCT01ZHEKAL-ZHE`) | 0.59 / 0.62 (1225) | 60.5% | -- | 64.2% | 62.2% [59.8%-64.2%] | -- | -- | -- | -- | PASS | +1.7 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3151.0, B 4015.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0217
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight +0.000
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arakawa / Tse vs Di Tommaso / Simes -- W35 Wagga Wagga SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01ARATSEDITSIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arakawa / Tse (`KXITFWDOUBLES-26OCT01ARATSEDITSIM-ARATSE`) | 0.06 / 0.94 (160) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Di Tommaso / Simes (`KXITFWDOUBLES-26OCT01ARATSEDITSIM-DITSIM`) | 0.06 / 0.94 (160) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Caroline Dolehide vs Kate Fakih -- W100 Templeton CA R16

ITF (ITF) · Hard · scheduled 2026-10-02T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214452:261278:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caroline Dolehide (`KXITFWMATCH-26OCT01DOLFAK-DOL`) | 0.84 / 0.86 (2) | 85.0% | -- | 88.0% | 87.5% [84.8%-89.7%] | -- | -- | -- | -- | PASS | +2.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kate Fakih (`KXITFWMATCH-26OCT01DOLFAK-FAK`) | 0.13 / 0.16 (3199) | 14.5% | -- | 12.0% | 12.5% [10.3%-15.2%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3771.0, B 215.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0244
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.026, surface_dev_loose +0.003, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## David Stevenson / Marcus Willis vs Hugo Nys / Edouard Roger-Vasselin -- ATP Tokyo R16

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-02T07:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02STEWILNYSROG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Nys / Edouard Roger-Vasselin (`KXATPDOUBLES-26OCT02STEWILNYSROG-NYSROG`) | 0.62 / 0.69 (77) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| David Stevenson / Marcus Willis (`KXATPDOUBLES-26OCT02STEWILNYSROG-STEWIL`) | 0.30 / 0.36 (80) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Nino Ehrenschneider vs Taisei Ichikawa -- M15 Luan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207383:209510:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nino Ehrenschneider (`KXITFMATCH-26OCT01EHRICH-EHR`) | 0.67 / 0.71 (3239) | 69.0% | -- | 59.1% | 57.6% [56.6%-58.6%] | -- | -- | -- | -- | PASS | -11.4 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Taisei Ichikawa (`KXITFMATCH-26OCT01EHRICH-ICH`) | 0.29 / 0.32 (29) | 30.5% | -- | 40.9% | 42.4% [41.4%-43.4%] | -- | -- | -- | -- | WATCH | +11.9 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3879.0, B 3136.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.01
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ryuki Matsuda vs Kosuke Ogura -- M15 Luan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202124:207987:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryuki Matsuda (`KXITFMATCH-26OCT01MATOGU-MAT`) | 0.61 / 0.65 (22) | 63.0% | -- | 41.7% | 46.9% [44.3%-52.1%] | -- | -- | -- | -- | PASS | -16.1 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kosuke Ogura (`KXITFMATCH-26OCT01MATOGU-OGU`) | 0.35 / 0.39 (42) | 37.0% | -- | 58.3% | 53.1% [47.9%-55.7%] | -- | -- | -- | -- | WATCH | +16.1 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3092.0, B 3515.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0389
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01MATOGU-OGU  (YES = Kosuke Ogura)
Model: 53%
Kalshi: 37%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.015, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kai-i Wang vs Isaac Becroft -- M15 Luan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208653:212459:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isaac Becroft (`KXITFMATCH-26OCT01WANBEC-BEC`) | 0.73 / 0.80 (110) | 76.5% | -- | 63.8% | 70.5% [69.1%-72.1%] | -- | -- | -- | -- | PASS | -6.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kai-i Wang (`KXITFMATCH-26OCT01WANBEC-WAN`) | 0.20 / 0.25 (35) | 22.5% | -- | 36.1% | 29.5% [27.9%-30.9%] | -- | -- | -- | -- | PASS | +7.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 553.0, B 1967.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0151
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Taiyo Yamanaka vs Max Purcell -- M15 Luan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:126845:208277:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Purcell (`KXITFMATCH-26OCT01YAMPUR-PUR`) | 0.71 / 0.94 (70) | 82.5% | -- | 79.1% | 87.7% [85.0%-89.9%] | -- | -- | -- | -- | PASS | +5.2 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Taiyo Yamanaka (`KXITFMATCH-26OCT01YAMPUR-YAM`) | 0.07 / 0.16 (59) | 11.5% | -- | 20.9% | 12.3% [10.1%-15.0%] | -- | -- | -- | -- | PASS | +0.8 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2646.0, B 1721.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0245
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.005, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eva Marie Desvignes vs Zijun Jiang -- W15 Maanshan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:223214:261082:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eva Marie Desvignes (`KXITFWMATCH-26OCT01DESJIA-DES`) | 0.54 / 0.58 (0) | 56.0% | -- | 22.1% | 31.6% [28.4%-33.5%] | -- | -- | -- | -- | PASS | -24.4 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zijun Jiang (`KXITFWMATCH-26OCT01DESJIA-JIA`) | 0.42 / 0.46 (46) | 44.0% | -- | 77.9% | 68.4% [66.5%-71.6%] | -- | -- | -- | -- | PASS | +24.4 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1379.0, B 178.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0252
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01DESJIA-JIA  (YES = Zijun Jiang)
Model: 68%
Kalshi: 44%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.019, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ha Eum Lee vs Ke Ren -- W15 Maanshan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:260621:270449:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ha Eum Lee (`KXITFWMATCH-26OCT01LEEREN-LEE`) | 0.86 / 0.90 (100) | 88.0% | -- | 73.0% | 69.4% [67.5%-72.1%] | -- | -- | -- | -- | PASS | -18.6 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ke Ren (`KXITFWMATCH-26OCT01LEEREN-REN`) | 0.11 / 0.14 (22) | 12.5% | -- | 27.0% | 30.6% [27.9%-32.5%] | -- | -- | -- | -- | PASS | +18.1 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

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
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xi Luo vs Ha Yoon Son -- W15 Maanshan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:260607:264069:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xi Luo (`KXITFWMATCH-26OCT01LUOSON-LUO`) | 0.71 / 0.75 (21) | 73.0% | -- | 80.8% | 77.3% [76.5%-79.7%] | -- | -- | -- | -- | PASS | +4.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ha Yoon Son (`KXITFWMATCH-26OCT01LUOSON-SON`) | 0.26 / 0.29 (37) | 27.5% | -- | 19.2% | 22.7% [20.3%-23.5%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 827.0, B 90.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.016
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.016, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stevens / Thompson vs Kitahara / Wen Wan -- W35 Wagga Wagga SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01STETHOKITWEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kitahara / Wen Wan (`KXITFWDOUBLES-26OCT01STETHOKITWEN-KITWEN`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stevens / Thompson (`KXITFWDOUBLES-26OCT01STETHOKITWEN-STETHO`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Yingqun Sun vs Jiayu Xu -- W15 Maanshan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222606:264029:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yingqun Sun (`KXITFWMATCH-26OCT01SUNXUX-SUN`) | 0.70 / 0.75 (196) | 72.5% | -- | 78.4% | 64.5% [58.5%-69.8%] | -- | -- | -- | -- | PASS | -8.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiayu Xu (`KXITFWMATCH-26OCT01SUNXUX-XUX`) | 0.25 / 0.30 (36) | 27.5% | -- | 21.6% | 35.5% [30.2%-41.5%] | -- | -- | -- | -- | PASS | +8.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1826.0, B 444.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0568
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose +0.015, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## HSUN LIN / Yang vs SUN / Wang -- M15 Luan SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T10:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02HSUYANSUNWAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HSUN LIN / Yang (`KXITFDOUBLES-26OCT02HSUYANSUNWAN-HSUYAN`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| SUN / Wang (`KXITFDOUBLES-26OCT02HSUYANSUNWAN-SUNWAN`) | 0.06 / 0.94 (110) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
