# ASSISTED SLATE -- 2026-10-03T01:16Z (`SL-20261003T011624Z-f4da71a1`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

110 open matches not seen started, 445 markets. Skipped: {"no_match_winner_listed": 1}. Sources: shadow board 2026-10-02T22:36:16.679747+00:00, Model 4 2026-10-02T22:36:37.419280+00:00, Gen-1 ledger 2026-10-02T13:30:06.576336+00:00, external 2026-10-03T00:56:12.574610+00:00, capture 20261003T005123Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-03 02:00Z**
* Recommended RUN TENNIS time: **2026-10-03 01:15Z**  (**OVERDUE -- run now**)
* Final price/status check time: **2026-10-03 01:50Z**
* Number of matches in window: 7 (Denis Shapovalov vs Alejandro Tabilo, Alex de Minaur vs Quentin Halys, Ashlyn Krueger vs Ann Li, Katie Volynets vs Elise Mertens, Coco Gauff vs Camila Osorio, Donna Vekic vs Lin Zhu ...)

Slate built 2026-10-03T01:16Z. Refresh due by: 2026-10-03 01:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 7, "HIGH_REVIEW": 21, "NORMAL": 164, "REVIEW": 48, "UNPRICED": 205}; match winners: {"EXTREME": 6, "HIGH_REVIEW": 17, "NORMAL": 76, "REVIEW": 15, "UNPRICED": 106}; quote freshness at build: {"AGING": 158, "STALE": 82}.

## Kanon Sawashiro vs Nagi Hanatani -- W35 Wagga Wagga QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-02 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:211544:263905:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nagi Hanatani (`KXITFWMATCH-26OCT01SAWHAN-HAN`) | 0.34 / 0.36 (78) | 35.0% | -- | 19.5% | 36.4% [28.2%-47.3%] | -- | -- | -- | -- | PASS | +1.4 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kanon Sawashiro (`KXITFWMATCH-26OCT01SAWHAN-SAW`) | 0.65 / 0.67 (174) | 66.0% | -- | 80.5% | 63.6% [52.7%-71.8%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 827.0, B 1219.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0958
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stevens / Thompson vs Kitahara / Wen Wan -- W35 Wagga Wagga SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-02 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT01STETHOKITWEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kitahara / Wen Wan (`KXITFWDOUBLES-26OCT01STETHOKITWEN-KITWEN`) | 0.31 / 0.76 (187) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stevens / Thompson (`KXITFWDOUBLES-26OCT01STETHOKITWEN-STETHO`) | 0.26 / 0.67 (14) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Meabe / Florencia Urrutia vs Ailin Larraya Guidi / Sousa Salazar -- W15 Trelew SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-02 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT02MEAFLOAILSOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ailin Larraya Guidi / Sousa Salazar (`KXITFWDOUBLES-26OCT02MEAFLOAILSOU-AILSOU`) | 0.68 / 0.69 (210) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Meabe / Florencia Urrutia (`KXITFWDOUBLES-26OCT02MEAFLOAILSOU-MEAFLO`) | 0.29 / 0.30 (8) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Denis Shapovalov vs Alejandro Tabilo -- ATP Tokyo R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-02 05:00Z
* Current expected start: 2026-10-03 02:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 01:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1260_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126214:133430:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Denis Shapovalov (`KXATPMATCH-26OCT01SHATAB-SHA`) | 0.56 / 0.57 (22548) | 56.5% | -- | 48.5% | 52.0% [49.5%-53.4%] | -- | -- | -- | -- | PASS | -4.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Tabilo (`KXATPMATCH-26OCT01SHATAB-TAB`) | 0.43 / 0.44 (35228) | 43.5% | -- | 51.5% | 48.0% [46.6%-50.5%] | -- | -- | -- | -- | SHADOW_BET | +4.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4723.0, B 7913.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0196
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.015
* Derivatives listed: 6 (GAME_SPREAD, MATCH_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXATPGTOTAL-26OCT01SHATAB-29` Over 28.5 games: 0.26/0.27 mid 26.5%, model 37.9% (market_conditioned_v1 (model4_board_v1)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01SHATAB-24` Over 23.5 games: 0.44/0.45 mid 44.5%, model 55.4% (market_conditioned_v1 (model4_board_v1)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01SHATAB-19` Over 18.5 games: 0.79/0.81 mid 80.0%, model 90.1% (market_conditioned_v1 (model4_board_v1)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01SHATAB-SHA6` Will Denis Shapovalov win at least 5.5 more games than Alejandro Tabilo?: 0.09/0.18 mid 13.5%, model 9.6% (market_conditioned_v1 (model4_board_v1)) -- gap -3.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01SHATAB-SHA3` Will Denis Shapovalov win at least 2.5 more games than Alejandro Tabilo?: 0.44/0.45 mid 44.5%, model 41.9% (market_conditioned_v1 (model4_board_v1)) -- gap -2.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01SHATAB-TAB2` Will Alejandro Tabilo win at least 1.5 more games than Denis Shapovalov?: 0.36/0.38 mid 37.0%, model 34.6% (market_conditioned_v1 (model4_board_v1)) -- gap -2.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; MODEL_ROW_STALE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lucas Miedler / Neil Oberleitner vs Theo Arribage / Albano Olivetti -- ATP Tokyo QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: 2026-10-03 02:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 01:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-03T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT02MIEOBEARROLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26OCT02MIEOBEARROLI-ARROLI`) | 0.53 / 0.56 (1705) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26OCT02MIEOBEARROLI-MIEOBE`) | 0.44 / 0.46 (102) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Caroline Dolehide vs Julieta Pareja -- W100 Templeton CA QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214452:264075:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caroline Dolehide (`KXITFWMATCH-26OCT02DOLPAR-DOL`) | 0.57 / 0.58 (42569) | 57.5% | -- | 61.0% | 59.4% [57.4%-62.5%] | -- | -- | -- | -- | PASS | +1.9 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julieta Pareja (`KXITFWMATCH-26OCT02DOLPAR-PAR`) | 0.42 / 0.43 (19448) | 42.5% | -- | 39.1% | 40.6% [37.5%-42.6%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3771.0, B 1273.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0258
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.021, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alex de Minaur vs Quentin Halys -- ATP Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-02 06:00Z
* Current expected start: 2026-10-03 03:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 02:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1260_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111460:200282:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex de Minaur (`KXATPMATCH-26OCT01DEHAL-DE`) | 0.72 / 0.73 (577) | 72.5% | -- | 79.4% | 78.7% [77.7%-79.4%] | -- | -- | -- | -- | SHADOW_BET | +6.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Quentin Halys (`KXATPMATCH-26OCT01DEHAL-HAL`) | 0.27 / 0.28 (112568) | 27.5% | -- | 20.6% | 21.3% [20.6%-22.3%] | -- | -- | -- | -- | PASS | -6.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 7096.0, B 7371.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0086
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.000, surface_dev_loose +0.003, surface_dev_tight +0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01DEHAL-22` Over 21.5 games: 0.55/0.57 mid 56.0%, model 67.2% (market_conditioned_v1 (model4_board_v1)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01DEHAL-27` Over 26.5 games: 0.31/0.32 mid 31.5%, model 41.4% (market_conditioned_v1 (model4_board_v1)) -- gap +9.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01DEHAL-DE20` Will Alex de Minaur win the Alex de Minaur vs Quentin Halys match by a set score of 2-0?: 0.49/0.52 mid 50.5%, model 42.7% (market_conditioned_v1 (model4_board_v1)) -- gap -7.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01DEHAL-DE21` Will Alex de Minaur win the Alex de Minaur vs Quentin Halys match by a set score of 2-1?: 0.23/0.25 mid 24.0%, model 29.6% (market_conditioned_v1 (model4_board_v1)) -- gap +5.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01DEHAL-DE5` Will Alex de Minaur win at least 4.5 more games than Quentin Halys?: 0.33/0.34 mid 33.5%, model 28.2% (market_conditioned_v1 (model4_board_v1)) -- gap -5.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01DEHAL-17` Over 16.5 games: 0.91/0.94 mid 92.5%, model 97.4% (market_conditioned_v1 (model4_board_v1)) -- gap +4.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01DEHAL-DE8` Will Alex de Minaur win at least 7.5 more games than Quentin Halys?: 0.05/0.08 mid 6.5%, model 2.8% (market_conditioned_v1 (model4_board_v1)) -- gap -3.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01DEHAL-HAL21` Will Quentin Halys win the Alex de Minaur vs Quentin Halys match by a set score of 2-1?: 0.12/0.14 mid 13.0%, model 15.7% (market_conditioned_v1 (model4_board_v1)) -- gap +2.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01DEHAL-HAL20` Will Quentin Halys win the Alex de Minaur vs Quentin Halys match by a set score of 2-0?: 0.13/0.15 mid 14.0%, model 12.0% (market_conditioned_v1 (model4_board_v1)) -- gap -2.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01DEHAL-DE2` Will Alex de Minaur win at least 1.5 more games than Quentin Halys?: 0.63/0.69 mid 66.0%, model 65.3% (market_conditioned_v1 (model4_board_v1)) -- gap -0.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; MODEL_ROW_STALE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Rinky Hijikata / Kaito Uesugi vs Hugo Nys / Edouard Roger-Vasselin -- ATP Tokyo QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 06:10Z
* Current expected start: 2026-10-03 03:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 02:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-03T06:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT02HIJUESNYSROG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rinky Hijikata / Kaito Uesugi (`KXATPDOUBLES-26OCT02HIJUESNYSROG-HIJUES`) | 0.28 / 0.30 (1662) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hugo Nys / Edouard Roger-Vasselin (`KXATPDOUBLES-26OCT02HIJUESNYSROG-NYSROG`) | 0.70 / 0.72 (4429) | 71.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Ashlyn Krueger vs Ann Li -- WTA Beijing R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-02 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-03 03:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215983:221909:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ann Li (`KXWTAMATCH-26OCT01KRUANN-ANN`) | 0.55 / 0.56 (35439) | 55.5% | -- | 63.7% | 59.7% [55.7%-61.7%] | -- | -- | -- | -- | WATCH | +4.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ashlyn Krueger (`KXWTAMATCH-26OCT01KRUANN-KRU`) | 0.44 / 0.45 (4787) | 44.5% | -- | 36.3% | 40.3% [38.3%-44.3%] | -- | -- | -- | -- | PASS | -4.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4211.0, B 4567.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0301
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01KRUANN-18` Over 17.5 games: 0.62/0.89 mid 75.5%, model 90.0% (market_conditioned_v1 (model4_board_v1)) -- gap +14.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01KRUANN-23` Over 22.5 games: 0.45/0.47 mid 46.0%, model 57.6% (market_conditioned_v1 (model4_board_v1)) -- gap +11.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01KRUANN-28` Over 27.5 games: 0.24/0.28 mid 26.0%, model 36.6% (market_conditioned_v1 (model4_board_v1)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; MODEL_ROW_STALE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Katie Volynets vs Elise Mertens -- WTA Beijing R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-02 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-03 03:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:210722:220465:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elise Mertens (`KXWTAMATCH-26OCT01VOLMER-MER`) | 0.53 / 0.54 (18311) | 53.5% | -- | 76.4% | 73.0% [67.9%-75.1%] | -- | -- | -- | -- | WATCH | +19.5 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katie Volynets (`KXWTAMATCH-26OCT01VOLMER-VOL`) | 0.46 / 0.48 (28752) | 47.0% | -- | 23.6% | 27.0% [24.9%-32.1%] | -- | -- | -- | -- | PASS | -20.0 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

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
Reasons: NO_EXTERNAL_REFERENCE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.009, surface_dev_loose -0.009, surface_dev_tight +0.009
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01VOLMER-18` Over 17.5 games: 0.58/0.89 mid 73.5%, model 87.5% (market_conditioned_v1 (model4_board_v1)) -- gap +14.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01VOLMER-23` Over 22.5 games: 0.44/0.45 mid 44.5%, model 55.9% (market_conditioned_v1 (model4_board_v1)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01VOLMER-28` Over 27.5 games: 0.23/0.26 mid 24.5%, model 34.0% (market_conditioned_v1 (model4_board_v1)) -- gap +9.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; MODEL_ROW_STALE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Coco Gauff vs Camila Osorio -- WTA Beijing R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-03 03:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215785:221103:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coco Gauff (`KXWTAMATCH-26OCT02GAUOSO-GAU`) | 0.90 / 0.91 (12490) | 90.5% | -- | 78.1% | 80.8% [79.7%-83.9%] | -- | 91.3% | 91.3% | MODEL_LONE_OUTLIER | PASS | -9.7 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Camila Osorio (`KXWTAMATCH-26OCT02GAUOSO-OSO`) | 0.09 / 0.10 (31542) | 9.5% | -- | 21.9% | 19.2% [16.1%-20.3%] | -- | 9.3% | 9.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +9.7 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5157.0, B 4356.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0211
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.004, surface_dev_loose -0.007, surface_dev_tight +0.011
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT02GAUOSO-19` Over 18.5 games: 0.50/0.51 mid 50.5%, model 60.1% (market_conditioned_v1 (model4_board_v1)) -- gap +9.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT02GAUOSO-24` Over 23.5 games: 0.20/0.24 mid 22.0%, model 31.4% (market_conditioned_v1 (model4_board_v1)) -- gap +9.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Han Shi vs Chengyiyi Yuan -- WTA 125K Suzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: 2026-10-03 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 02:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02SHIYUA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Han Shi (`KXWTACHALLENGERMATCH-26OCT02SHIYUA-SHI`) | 0.86 / 0.87 (2464) | 86.5% | -- | -- | -- [-----] | -- | 87.9% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chengyiyi Yuan (`KXWTACHALLENGERMATCH-26OCT02SHIYUA-YUA`) | 0.12 / 0.13 (1972) | 12.5% | -- | -- | -- [-----] | -- | 13.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Donna Vekic vs Lin Zhu -- WTA Beijing R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-03 03:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202499:202684:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Donna Vekic (`KXWTAMATCH-26OCT02VEKZHU-VEK`) | 0.62 / 0.63 (3128) | 62.5% | -- | 32.3% | 40.2% [34.2%-57.8%] | 63.2% | 63.1% | 63.2% | MODEL_LONE_OUTLIER | PASS | -22.3 pp | HIGH_REVIEW | AGING | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Lin Zhu (`KXWTAMATCH-26OCT02VEKZHU-ZHU`) | 0.36 / 0.37 (2066) | 36.5% | -- | 67.7% | 59.8% [42.2%-65.8%] | 36.8% | 37.2% | 37.0% | MODEL_LONE_OUTLIER | WATCH | +23.3 pp | HIGH_REVIEW | AGING | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4044.0, B 3182.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1179
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT02VEKZHU-ZHU  (YES = Lin Zhu)
Model: 60%
Kalshi: 36%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: B (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.036, surface_pool_high -0.035, surface_dev_loose -0.020, surface_dev_tight +0.025
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT02VEKZHU-18` Over 17.5 games: 0.60/0.89 mid 74.5%, model 87.9% (market_conditioned_v1 (model4_board_v1)) -- gap +13.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT02VEKZHU-23` Over 22.5 games: 0.41/0.43 mid 42.0%, model 55.2% (market_conditioned_v1 (model4_board_v1)) -- gap +13.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT02VEKZHU-28` Over 27.5 games: 0.22/0.26 mid 24.0%, model 34.2% (market_conditioned_v1 (model4_board_v1)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; WIDE_SPREAD

## Yidi Yang vs Rina Saigo -- WTA 125K Suzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: 2026-10-03 03:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 02:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02YANSAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rina Saigo (`KXWTACHALLENGERMATCH-26OCT02YANSAI-SAI`) | 0.49 / 0.50 (1903) | 49.5% | -- | -- | -- [-----] | 49.0% | 48.5% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yidi Yang (`KXWTACHALLENGERMATCH-26OCT02YANSAI-YAN`) | 0.49 / 0.50 (1956) | 49.5% | -- | -- | -- [-----] | 51.0% | 51.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Astra Sharma vs Ashley Lahey -- W15 Nashville TN QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-03T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206292:216076:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashley Lahey (`KXITFWMATCH-26OCT02SHALAH-LAH`) | 0.03 / 0.04 (38303) | 3.5% | -- | 57.8% | 49.5% [40.6%-53.1%] | -- | -- | -- | -- | PASS | +46.0 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Astra Sharma (`KXITFWMATCH-26OCT02SHALAH-SHA`) | 0.96 / 0.97 (41898) | 96.5% | -- | 42.2% | 50.5% [46.9%-59.4%] | -- | -- | -- | -- | PASS | -46.0 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2800.0, B 1883.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0627
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02SHALAH-LAH  (YES = Ashley Lahey)
Model: 49%
Kalshi: 4%
Gap: +46 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carlos Alcaraz vs Matteo Arnaldi -- ATP Tokyo R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 05:00Z
* Current expected start: 2026-10-03 03:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 02:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-90_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-03T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207989:208286:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlos Alcaraz (`KXATPMATCH-26OCT02ALCARN-ALC`) | 0.92 / 0.93 (54982) | 92.5% | -- | 97.4% | 96.7% [94.2%-97.2%] | 91.3% | 92.2% | 91.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +4.2 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Matteo Arnaldi (`KXATPMATCH-26OCT02ALCARN-ARN`) | 0.07 / 0.08 (27908) | 7.5% | -- | 2.6% | 3.3% [2.8%-5.8%] | 8.7% | 7.0% | 7.9% | MODEL_LONE_OUTLIER | PASS | -4.2 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 7542.0, B 6406.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0148
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.001, surface_pool_high -0.001, surface_dev_loose +0.003, surface_dev_tight -0.004
* Derivatives listed: 13 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 9 carry a model probability
  * `KXATPGTOTAL-26OCT02ALCARN-19` Over 18.5 games: 0.51/0.52 mid 51.5%, model 68.3% (market_conditioned_v1 (model4_board_v1)) -- gap +16.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02ALCARN-ALC7` Will Carlos Alcaraz win at least 6.5 more games than Matteo Arnaldi?: 0.41/0.42 mid 41.5%, model 25.6% (market_conditioned_v1 (model4_board_v1)) -- gap -15.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02ALCARN-24` Over 23.5 games: 0.20/0.23 mid 21.5%, model 32.4% (market_conditioned_v1 (model4_board_v1)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02ALCARN-ALC20` Will Carlos Alcaraz win the Carlos Alcaraz vs Matteo Arnaldi match by a set score of 2-0?: 0.76/0.77 mid 76.5%, model 66.7% (market_conditioned_v1 (model4_board_v1)) -- gap -9.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02ALCARN-ALC4` Will Carlos Alcaraz win at least 3.5 more games than Matteo Arnaldi?: 0.82/0.83 mid 82.5%, model 73.7% (market_conditioned_v1 (model4_board_v1)) -- gap -8.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02ALCARN-ALC21` Will Carlos Alcaraz win the Carlos Alcaraz vs Matteo Arnaldi match by a set score of 2-1?: 0.16/0.17 mid 16.5%, model 24.4% (market_conditioned_v1 (model4_board_v1)) -- gap +7.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02ALCARN-ALC10` Will Carlos Alcaraz win at least 9.5 more games than Matteo Arnaldi?: 0.02/0.08 mid 5.0%, model 1.9% (market_conditioned_v1 (model4_board_v1)) -- gap -3.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02ALCARN-ARN21` Will Matteo Arnaldi win the Carlos Alcaraz vs Matteo Arnaldi match by a set score of 2-1?: 0.03/0.04 mid 3.5%, model 5.5% (market_conditioned_v1 (model4_board_v1)) -- gap +2.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02ALCARN-ARN20` Will Matteo Arnaldi win the Carlos Alcaraz vs Matteo Arnaldi match by a set score of 2-0?: 0.02/0.03 mid 2.5%, model 3.4% (market_conditioned_v1 (model4_board_v1)) -- gap +0.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE

## Pearce / Yamakita vs Mattioli / Webb -- W15 Nashville TN SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT02PEAYAMMATWEB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mattioli / Webb (`KXITFWDOUBLES-26OCT02PEAYAMMATWEB-MATWEB`) | 0.47 / 0.48 (267) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pearce / Yamakita (`KXITFWDOUBLES-26OCT02PEAYAMMATWEB-PEAYAM`) | 0.51 / 0.53 (784) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Austin Krajicek / Nikola Mektic vs Alejandro Tabilo / Luca Van Assche -- ATP Tokyo QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 05:00Z
* Current expected start: 2026-10-03 04:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 03:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-03T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT02KRAMEKTABVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Austin Krajicek / Nikola Mektic (`KXATPDOUBLES-26OCT02KRAMEKTABVAN-KRAMEK`) | 0.74 / 0.76 (138) | 75.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alejandro Tabilo / Luca Van Assche (`KXATPDOUBLES-26OCT02KRAMEKTABVAN-TABVAN`) | 0.23 / 0.25 (477) | 24.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Jelena Ostapenko vs Paula Badosa -- WTA Beijing R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-02 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-03 04:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211533:211651:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Paula Badosa (`KXWTAMATCH-26OCT01OSTBAD-BAD`) | 0.60 / 0.61 (53693) | 60.5% | -- | 63.5% | 62.0% [57.9%-63.0%] | -- | -- | -- | -- | PASS | +1.5 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jelena Ostapenko (`KXWTAMATCH-26OCT01OSTBAD-OST`) | 0.40 / 0.41 (401) | 40.5% | -- | 36.5% | 38.0% [37.0%-42.1%] | -- | -- | -- | -- | PASS | -2.5 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3919.0, B 3479.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0255
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01OSTBAD-18` Over 17.5 games: 0.60/0.89 mid 74.5%, model 86.8% (market_conditioned_v1 (model4_board_v1)) -- gap +12.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01OSTBAD-23` Over 22.5 games: 0.43/0.45 mid 44.0%, model 54.5% (market_conditioned_v1 (model4_board_v1)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01OSTBAD-28` Over 27.5 games: 0.23/0.27 mid 25.0%, model 33.1% (market_conditioned_v1 (model4_board_v1)) -- gap +8.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
* Warnings: SCHEDULED_START_PASSED; MODEL_ROW_STALE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Maria Sakkari vs Storm Hunter -- WTA Beijing R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-02 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-03 04:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:204411:206289:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Storm Hunter (`KXWTAMATCH-26OCT01SAKHUN-HUN`) | 0.30 / 0.31 (49141) | 30.5% | -- | 27.6% | 30.3% [28.0%-32.2%] | -- | -- | -- | -- | PASS | -0.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Sakkari (`KXWTAMATCH-26OCT01SAKHUN-SAK`) | 0.69 / 0.70 (8811) | 69.5% | -- | 72.4% | 69.7% [67.8%-72.0%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3640.0, B 2089.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0207
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.019, surface_dev_loose -0.005, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01SAKHUN-22` Over 21.5 games: 0.45/0.46 mid 45.5%, model 58.2% (market_conditioned_v1 (model4_board_v1)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01SAKHUN-27` Over 26.5 games: 0.24/0.28 mid 26.0%, model 35.7% (market_conditioned_v1 (model4_board_v1)) -- gap +9.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01SAKHUN-17` Over 16.5 games: 0.78/0.89 mid 83.5%, model 91.6% (market_conditioned_v1 (model4_board_v1)) -- gap +8.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; MODEL_ROW_STALE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Katerina Siniakova vs Elina Svitolina -- WTA Beijing R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-02 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-03 04:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202494:211701:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katerina Siniakova (`KXWTAMATCH-26OCT01SINSVI-SIN`) | 0.24 / 0.25 (28331) | 24.5% | -- | 29.9% | 29.0% [27.2%-29.9%] | -- | -- | -- | -- | SHADOW_BET | +4.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elina Svitolina (`KXWTAMATCH-26OCT01SINSVI-SVI`) | 0.76 / 0.77 (125223) | 76.5% | -- | 70.1% | 71.0% [70.1%-72.8%] | -- | -- | -- | -- | PASS | -5.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4278.0, B 4144.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0137
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.009, surface_dev_tight +0.004
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01SINSVI-21` Over 20.5 games: 0.48/0.49 mid 48.5%, model 60.7% (market_conditioned_v1 (model4_board_v1)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01SINSVI-26` Over 25.5 games: 0.26/0.28 mid 27.0%, model 38.2% (market_conditioned_v1 (model4_board_v1)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01SINSVI-16` Over 15.5 games: 0.85/0.94 mid 89.5%, model 95.5% (market_conditioned_v1 (model4_board_v1)) -- gap +6.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; MODEL_ROW_STALE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Emerson Jones vs Alexandra Shubladze -- WTA 125K Jingshan SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 07:10Z
* Current expected start: 2026-10-03 04:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 03:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T07:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03JONSHU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emerson Jones (`KXWTACHALLENGERMATCH-26OCT03JONSHU-JON`) | 0.41 / 0.42 (8327) | 41.5% | -- | -- | -- [-----] | 41.6% | 41.5% | 41.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexandra Shubladze (`KXWTACHALLENGERMATCH-26OCT03JONSHU-SHU`) | 0.59 / 0.60 (24323) | 59.5% | -- | -- | -- [-----] | 58.4% | 58.3% | 58.3% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Andrey Rublev vs Roman Safiullin -- ATP Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: 2026-10-03 05:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 04:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-60_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126094:126128:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrey Rublev (`KXATPMATCH-26OCT02RUBSAF-RUB`) | 0.57 / 0.58 (11914) | 57.5% | -- | 66.8% | 65.4% [63.6%-67.2%] | 56.6% | 57.7% | 57.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.9 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Roman Safiullin (`KXATPMATCH-26OCT02RUBSAF-SAF`) | 0.42 / 0.43 (13244) | 42.5% | -- | 33.2% | 34.6% [32.8%-36.4%] | 43.4% | 42.6% | 43.0% | MODEL_LONE_OUTLIER | PASS | -7.9 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 6741.0, B 4566.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0183
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.018, surface_dev_loose -0.005, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT02RUBSAF-25` Over 24.5 games: 0.46/0.47 mid 46.5%, model 54.0% (market_conditioned_v1 (model4_board_v1)) -- gap +7.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02RUBSAF-30` Over 29.5 games: 0.24/0.28 mid 26.0%, model 32.3% (market_conditioned_v1 (model4_board_v1)) -- gap +6.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02RUBSAF-RUB20` Will Andrey Rublev win the Andrey Rublev vs Roman Safiullin match by a set score of 2-0?: 0.33/0.35 mid 34.0%, model 29.5% (market_conditioned_v1 (model4_board_v1)) -- gap -4.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02RUBSAF-20` Over 19.5 games: 0.77/0.79 mid 78.0%, model 82.2% (market_conditioned_v1 (model4_board_v1)) -- gap +4.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02RUBSAF-RUB21` Will Andrey Rublev win the Andrey Rublev vs Roman Safiullin match by a set score of 2-1?: 0.22/0.24 mid 23.0%, model 27.0% (market_conditioned_v1 (model4_board_v1)) -- gap +4.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02RUBSAF-SAF21` Will Roman Safiullin win the Andrey Rublev vs Roman Safiullin match by a set score of 2-1?: 0.18/0.20 mid 19.0%, model 22.7% (market_conditioned_v1 (model4_board_v1)) -- gap +3.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02RUBSAF-SAF20` Will Roman Safiullin win the Andrey Rublev vs Roman Safiullin match by a set score of 2-0?: 0.22/0.25 mid 23.5%, model 20.9% (market_conditioned_v1 (model4_board_v1)) -- gap -2.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02RUBSAF-RUB5` Will Andrey Rublev win at least 4.5 more games than Roman Safiullin?: 0.21/0.22 mid 21.5%, model 18.9% (market_conditioned_v1 (model4_board_v1)) -- gap -2.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02RUBSAF-RUB2` Will Andrey Rublev win at least 1.5 more games than Roman Safiullin?: 0.50/0.51 mid 50.5%, model 48.8% (market_conditioned_v1 (model4_board_v1)) -- gap -1.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02RUBSAF-SAF2` Will Roman Safiullin win at least 1.5 more games than Andrey Rublev?: 0.35/0.37 mid 36.0%, model 36.1% (market_conditioned_v1 (model4_board_v1)) -- gap +0.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE

## Xinyu Gao vs Iga Swiatek -- WTA Beijing R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-03 05:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 04:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214386:216347:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xinyu Gao (`KXWTAMATCH-26OCT02GAOSWI-GAO`) | 0.02 / 0.03 (25275) | 2.5% | -- | 8.1% | 7.5% [6.6%-8.7%] | -- | 2.1% | 2.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +5.0 pp | NORMAL | AGING | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Iga Swiatek (`KXWTAMATCH-26OCT02GAOSWI-SWI`) | 0.97 / 0.98 (44018) | 97.5% | -- | 91.9% | 92.5% [91.3%-93.4%] | -- | 97.6% | 97.6% | MODEL_LONE_OUTLIER | PASS | -5.0 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3203.0, B 4863.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0105
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.010, surface_dev_loose +0.006, surface_dev_tight -0.005
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT02GAOSWI-17` Over 16.5 games: 0.43/0.44 mid 43.5%, model 71.8% (market_conditioned_v1 (model4_board_v1)) -- gap +28.3 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT02GAOSWI-22` Over 21.5 games: 0.11/0.15 mid 13.0%, model 28.3% (market_conditioned_v1 (model4_board_v1)) -- gap +15.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data LIMITED
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Jia-Jing Lu vs Zongyu Li -- WTA 125K Suzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 08:00Z
* Current expected start: 2026-10-03 05:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 04:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03JIAZON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jia-Jing Lu (`KXWTACHALLENGERMATCH-26OCT03JIAZON-JIA`) | 0.62 / 0.65 (5482) | 63.5% | -- | -- | -- [-----] | 63.1% | 63.5% | 63.5% | MARKETS_AGREE | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zongyu Li (`KXWTACHALLENGERMATCH-26OCT03JIAZON-ZON`) | 0.35 / 0.38 (7703) | 36.5% | -- | -- | -- [-----] | 36.9% | 36.3% | 36.3% | MARKETS_AGREE | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Katarina Zavatska vs Kristiana Sidorova -- WTA 125K Suzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 08:00Z
* Current expected start: 2026-10-03 05:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 04:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03ZAVSID:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristiana Sidorova (`KXWTACHALLENGERMATCH-26OCT03ZAVSID-SID`) | 0.64 / 0.65 (2790) | 64.5% | -- | -- | -- [-----] | 65.1% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katarina Zavatska (`KXWTACHALLENGERMATCH-26OCT03ZAVSID-ZAV`) | 0.34 / 0.35 (1538) | 34.5% | -- | -- | -- [-----] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Jessica Bouzas Maneiro vs Aliona Falei -- WTA 125K Jingshan SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 08:30Z
* Current expected start: 2026-10-03 05:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 04:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T08:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03BOUFAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jessica Bouzas Maneiro (`KXWTACHALLENGERMATCH-26OCT03BOUFAL-BOU`) | 0.76 / 0.77 (4221) | 76.5% | -- | -- | -- [-----] | 76.0% | 76.1% | 76.1% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aliona Falei (`KXWTACHALLENGERMATCH-26OCT03BOUFAL-FAL`) | 0.23 / 0.24 (6161) | 23.5% | -- | -- | -- [-----] | 24.0% | 24.1% | 24.1% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Simone Bolelli / Andrea Vavassori vs Marc Polmans / Jan Zielinski -- ATP Tokyo QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 08:30Z
* Current expected start: 2026-10-03 06:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 05:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-03T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03BOLVAVPOLZIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Simone Bolelli / Andrea Vavassori (`KXATPDOUBLES-26OCT03BOLVAVPOLZIE-BOLVAV`) | 0.60 / 0.62 (1889) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marc Polmans / Jan Zielinski (`KXATPDOUBLES-26OCT03BOLVAVPOLZIE-POLZIE`) | 0.38 / 0.39 (65) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Kamilla Rakhimova vs Leylah Fernandez -- WTA Beijing R64

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-10-02 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-03 06:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-02 11:13Z
* Recommended handicap-by time: 2026-10-03 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215872:220367:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leylah Fernandez (`KXWTAMATCH-26OCT01RAKFER-FER`) | 0.74 / 0.75 (350) | 74.5% | -- | 66.3% | 67.7% [65.8%-68.7%] | -- | -- | -- | -- | PASS | -6.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kamilla Rakhimova (`KXWTAMATCH-26OCT01RAKFER-RAK`) | 0.25 / 0.26 (31786) | 25.5% | -- | 33.7% | 32.3% [31.4%-34.2%] | -- | -- | -- | -- | SHADOW_BET | +6.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5718.0, B 4828.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0142
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01RAKFER-21` Over 20.5 games: 0.49/0.50 mid 49.5%, model 62.5% (market_conditioned_v1 (model4_board_v1)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01RAKFER-26` Over 25.5 games: 0.28/0.31 mid 29.5%, model 39.7% (market_conditioned_v1 (model4_board_v1)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01RAKFER-16` Over 15.5 games: 0.88/0.95 mid 91.5%, model 96.1% (market_conditioned_v1 (model4_board_v1)) -- gap +4.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; MODEL_ROW_STALE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Iva Jovic vs Harriet Dart -- WTA Beijing R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-03 06:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211279:260300:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harriet Dart (`KXWTAMATCH-26OCT02JOVDAR-DAR`) | 0.10 / 0.11 (45804) | 10.5% | -- | 34.0% | 30.7% [28.0%-32.1%] | 11.9% | 9.3% | 10.6% | MODEL_LONE_OUTLIER | WATCH | +20.2 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Iva Jovic (`KXWTAMATCH-26OCT02JOVDAR-JOV`) | 0.89 / 0.90 (13681) | 89.5% | -- | 66.0% | 69.3% [67.9%-72.0%] | 88.1% | 90.1% | 89.1% | MODEL_LONE_OUTLIER | PASS | -20.2 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3602.0, B 4244.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0208
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT02JOVDAR-DAR  (YES = Harriet Dart)
Model: 31%
Kalshi: 10%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_REJECTION, UNKNOWN
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.004, surface_dev_tight +0.000
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT02JOVDAR-19` Over 18.5 games: 0.48/0.49 mid 48.5%, model 62.8% (market_conditioned_v1 (model4_board_v1)) -- gap +14.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT02JOVDAR-24` Over 23.5 games: 0.20/0.23 mid 21.5%, model 33.0% (market_conditioned_v1 (model4_board_v1)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE

## Priska Madelyn Nugroho vs Kyoka Okamura -- WTA 125K Suzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 08:00Z
* Current expected start: 2026-10-03 06:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 05:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03NUGOKA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Priska Madelyn Nugroho (`KXWTACHALLENGERMATCH-26OCT03NUGOKA-NUG`) | 0.43 / 0.45 (474) | 44.0% | -- | -- | -- [-----] | 44.6% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kyoka Okamura (`KXWTACHALLENGERMATCH-26OCT03NUGOKA-OKA`) | 0.55 / 0.57 (8124) | 56.0% | -- | -- | -- [-----] | 55.4% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Lloyd Harris vs Alex Bolt -- ATP Challenger Jingshan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106109:144750:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Bolt (`KXATPCHALLENGERMATCH-26OCT02HARBOL-BOL`) | 0.16 / 0.17 (4312) | 16.5% | -- | 34.2% | 32.0% [29.9%-34.9%] | 18.8% | 16.4% | 17.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +15.5 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Lloyd Harris (`KXATPCHALLENGERMATCH-26OCT02HARBOL-HAR`) | 0.83 / 0.84 (10653) | 83.5% | -- | 65.8% | 68.0% [65.1%-70.1%] | 81.2% | 84.1% | 82.7% | MODEL_LONE_OUTLIER | PASS | -15.5 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4129.0, B 5430.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0254
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT02HARBOL-BOL  (YES = Alex Bolt)
Model: 32%
Kalshi: 16%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.022, surface_pool_high +0.021, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Marcelo Melo / Alexander Zverev vs Julian Cash / Lloyd Glasspool -- ATP Beijing QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-04T04:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-03T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT02MELZVECASGLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julian Cash / Lloyd Glasspool (`KXATPDOUBLES-26OCT02MELZVECASGLA-CASGLA`) | 0.64 / 0.71 (305) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marcelo Melo / Alexander Zverev (`KXATPDOUBLES-26OCT02MELZVECASGLA-MELZVE`) | 0.28 / 0.33 (164) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Frodin / Sahdiieva vs Broadus / Zamarripa -- W100 Templeton CA SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT02FROSAHBROZAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Broadus / Zamarripa (`KXITFWDOUBLES-26OCT02FROSAHBROZAM-BROZAM`) | 0.77 / 0.80 (41) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Frodin / Sahdiieva (`KXITFWDOUBLES-26OCT02FROSAHBROZAM-FROSAH`) | 0.19 / 0.21 (113) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Yujia Huang vs Darya Khomutsianskaya -- WTA 125K Suzhou Q1

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02HUAKHO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yujia Huang (`KXWTACHALLENGERMATCH-26OCT02HUAKHO-HUA`) | 0.51 / 0.52 (6982) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Darya Khomutsianskaya (`KXWTACHALLENGERMATCH-26OCT02HUAKHO-KHO`) | 0.49 / 0.50 (3402) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Kamper / Kruger vs Bartel / Justine Hejtmanek -- W15 Nashville TN SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT02KAMKRUBARJUS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bartel / Justine Hejtmanek (`KXITFWDOUBLES-26OCT02KAMKRUBARJUS-BARJUS`) | 0.39 / 0.43 (9) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kamper / Kruger (`KXITFWDOUBLES-26OCT02KAMKRUBARJUS-KAMKRU`) | 0.57 / 0.66 (15) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Belinda Bencic vs Anastasia Zakharova -- WTA Beijing R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-02 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-03 06:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 05:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202505:220435:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Belinda Bencic (`KXWTAMATCH-26OCT01BENZAK-BEN`) | 0.79 / 0.80 (14135) | 79.5% | -- | 77.8% | 79.3% [77.0%-82.6%] | -- | -- | -- | -- | PASS | -0.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Zakharova (`KXWTAMATCH-26OCT01BENZAK-ZAK`) | 0.20 / 0.21 (2083) | 20.5% | -- | 22.2% | 20.7% [17.4%-23.0%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3571.0, B 4628.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0279
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.023, surface_dev_loose +0.004, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01BENZAK-21` Over 20.5 games: 0.44/0.46 mid 45.0%, model 58.7% (market_conditioned_v1 (model4_board_v1)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01BENZAK-26` Over 25.5 games: 0.23/0.27 mid 25.0%, model 36.4% (market_conditioned_v1 (model4_board_v1)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01BENZAK-16` Over 15.5 games: 0.85/0.94 mid 89.5%, model 94.9% (market_conditioned_v1 (model4_board_v1)) -- gap +5.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; MODEL_ROW_STALE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Qinwen Zheng vs Anna Kalinskaya -- WTA Beijing R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-02 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-03 06:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 05:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214939:221012:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Kalinskaya (`KXWTAMATCH-26OCT01ZHEKAL-KAL`) | 0.38 / 0.39 (1802) | 38.5% | -- | 35.8% | 37.8% [35.8%-40.2%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Qinwen Zheng (`KXWTAMATCH-26OCT01ZHEKAL-ZHE`) | 0.61 / 0.62 (8851) | 61.5% | -- | 64.2% | 62.2% [59.8%-64.2%] | -- | -- | -- | -- | PASS | +0.7 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3151.0, B 4015.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0217
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01ZHEKAL-23` Over 22.5 games: 0.45/0.46 mid 45.5%, model 56.5% (market_conditioned_v1 (model4_board_v1)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01ZHEKAL-28` Over 27.5 games: 0.24/0.30 mid 27.0%, model 35.6% (market_conditioned_v1 (model4_board_v1)) -- gap +8.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01ZHEKAL-18` Over 17.5 games: 0.79/0.85 mid 82.0%, model 89.3% (market_conditioned_v1 (model4_board_v1)) -- gap +7.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; MODEL_ROW_STALE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Matteo Berrettini vs Adolfo Daniel Vallejo -- ATP Tokyo R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 05:00Z
* Current expected start: 2026-10-03 07:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 06:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+120_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-03T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126610:209226:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Berrettini (`KXATPMATCH-26OCT02BERVAL-BER`) | 0.60 / 0.61 (21762) | 60.5% | -- | 63.2% | 68.2% [66.0%-73.0%] | 60.2% | 61.2% | 61.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.7 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Adolfo Daniel Vallejo (`KXATPMATCH-26OCT02BERVAL-VAL`) | 0.40 / 0.41 (50745) | 40.5% | -- | 36.8% | 31.8% [27.0%-34.1%] | 39.8% | 39.4% | 39.4% | MODEL_LONE_OUTLIER | PASS | -8.7 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4565.0, B 5913.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0354
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.018, surface_dev_loose -0.000, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT02BERVAL-23` Over 22.5 games: 0.50/0.51 mid 50.5%, model 60.7% (market_conditioned_v1 (model4_board_v1)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02BERVAL-28` Over 27.5 games: 0.29/0.33 mid 31.0%, model 40.5% (market_conditioned_v1 (model4_board_v1)) -- gap +9.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02BERVAL-BER20` Will Matteo Berrettini win the Matteo Berrettini vs Adolfo Daniel Vallejo match by a set score of 2-0?: 0.37/0.39 mid 38.0%, model 32.5% (market_conditioned_v1 (model4_board_v1)) -- gap -5.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02BERVAL-BER21` Will Matteo Berrettini win the Matteo Berrettini vs Adolfo Daniel Vallejo match by a set score of 2-1?: 0.22/0.23 mid 22.5%, model 27.9% (market_conditioned_v1 (model4_board_v1)) -- gap +5.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02BERVAL-18` Over 17.5 games: 0.88/0.91 mid 89.5%, model 93.5% (market_conditioned_v1 (model4_board_v1)) -- gap +4.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02BERVAL-VAL21` Will Adolfo Daniel Vallejo win the Matteo Berrettini vs Adolfo Daniel Vallejo match by a set score of 2-1?: 0.16/0.19 mid 17.5%, model 21.1% (market_conditioned_v1 (model4_board_v1)) -- gap +3.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02BERVAL-VAL20` Will Adolfo Daniel Vallejo win the Matteo Berrettini vs Adolfo Daniel Vallejo match by a set score of 2-0?: 0.20/0.23 mid 21.5%, model 18.5% (market_conditioned_v1 (model4_board_v1)) -- gap -3.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02BERVAL-BER6` Will Matteo Berrettini win at least 5.5 more games than Adolfo Daniel Vallejo?: 0.10/0.19 mid 14.5%, model 12.0% (market_conditioned_v1 (model4_board_v1)) -- gap -2.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02BERVAL-BER3` Will Matteo Berrettini win at least 2.5 more games than Adolfo Daniel Vallejo?: 0.47/0.48 mid 47.5%, model 45.2% (market_conditioned_v1 (model4_board_v1)) -- gap -2.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02BERVAL-VAL2` Will Adolfo Daniel Vallejo win at least 1.5 more games than Matteo Berrettini?: 0.32/0.36 mid 34.0%, model 32.4% (market_conditioned_v1 (model4_board_v1)) -- gap -1.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Sander Arends / David Pel vs Zhizhen Zhang / Yi Zhou -- ATP Beijing QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 08:20Z
* Current expected start: 2026-10-03 07:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 06:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-03T08:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03AREPELZHAZHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sander Arends / David Pel (`KXATPDOUBLES-26OCT03AREPELZHAZHO-AREPEL`) | 0.54 / 0.60 (100) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zhizhen Zhang / Yi Zhou (`KXATPDOUBLES-26OCT03AREPELZHAZHO-ZHAZHO`) | 0.40 / 0.44 (45) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Pace / Zucchini vs Osuigwe / Urhobo -- W100 Templeton CA SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT02PACZUCOSUURH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Osuigwe / Urhobo (`KXITFWDOUBLES-26OCT02PACZUCOSUURH-OSUURH`) | 0.58 / 0.64 (322) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pace / Zucchini (`KXITFWDOUBLES-26OCT02PACZUCOSUURH-PACZUC`) | 0.33 / 0.40 (842) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Mutsumi Uemura vs Mio Mushika -- W35 Wagga Wagga SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 07:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222986:260828:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mio Mushika (`KXITFWMATCH-26OCT02UEMMUS-MUS`) | 0.48 / 0.50 (1087) | 49.0% | -- | 87.5% | 80.8% [75.6%-84.8%] | 49.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +31.8 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mutsumi Uemura (`KXITFWMATCH-26OCT02UEMMUS-UEM`) | 0.51 / 0.52 (3005) | 51.5% | -- | 12.6% | 19.2% [15.2%-24.4%] | 50.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -32.2 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 824.0, B 2224.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0459
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02UEMMUS-MUS  (YES = Mio Mushika)
Model: 81%
Kalshi: 49%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.007, surface_dev_loose -0.011, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marie Bouzkova vs Kimberly Birrell -- WTA Beijing R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-02 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-03 07:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 06:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213631:214040:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kimberly Birrell (`KXWTAMATCH-26OCT01BOUBIR-BIR`) | 0.33 / 0.34 (21294) | 33.5% | -- | 45.8% | 43.6% [39.5%-45.8%] | -- | -- | -- | -- | SHADOW_BET | +10.2 pp | REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marie Bouzkova (`KXWTAMATCH-26OCT01BOUBIR-BOU`) | 0.66 / 0.68 (27400) | 67.0% | -- | 54.2% | 56.4% [54.2%-60.5%] | -- | -- | -- | -- | PASS | -10.7 pp | REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4089.0, B 5020.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0313
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.021, surface_dev_loose -0.011, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01BOUBIR-22` Over 21.5 games: 0.48/0.49 mid 48.5%, model 59.2% (market_conditioned_v1 (model4_board_v1)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01BOUBIR-27` Over 26.5 games: 0.25/0.31 mid 28.0%, model 36.4% (market_conditioned_v1 (model4_board_v1)) -- gap +8.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01BOUBIR-17` Over 16.5 games: 0.83/0.89 mid 86.0%, model 91.7% (market_conditioned_v1 (model4_board_v1)) -- gap +5.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
* Warnings: SCHEDULED_START_PASSED; MODEL_ROW_STALE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Xinran Sun vs Cristina Bucsa -- WTA Beijing R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-03 07:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 06:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213710:270082:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Bucsa (`KXWTAMATCH-26OCT02SUNBUC-BUC`) | 0.68 / 0.69 (24437) | 68.5% | -- | 41.5% | 66.6% [53.7%-81.0%] | 67.6% | 68.5% | 68.0% | MODEL_LONE_OUTLIER | PASS | -1.9 pp | NORMAL | AGING | C / LIMITED | ALL_AGREE | VERIFIED |
| Xinran Sun (`KXWTAMATCH-26OCT02SUNBUC-SUN`) | 0.31 / 0.32 (3788) | 31.5% | -- | 58.5% | 33.4% [19.0%-46.3%] | 32.4% | 31.8% | 32.1% | MODEL_LONE_OUTLIER | PASS | +1.9 pp | NORMAL | AGING | C / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1001.0, B 4493.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1365
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.030, surface_dev_loose +0.015, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT02SUNBUC-22` Over 21.5 games: 0.43/0.44 mid 43.5%, model 58.2% (market_conditioned_v1 (model4_board_v1)) -- gap +14.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT02SUNBUC-27` Over 26.5 games: 0.22/0.31 mid 26.5%, model 35.5% (market_conditioned_v1 (model4_board_v1)) -- gap +9.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT02SUNBUC-17` Over 16.5 games: 0.81/0.86 mid 83.5%, model 91.0% (market_conditioned_v1 (model4_board_v1)) -- gap +7.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data LIMITED
* Warnings: LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Darya Astakhova vs Sijia Wei -- WTA 125K Suzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 11:00Z
* Current expected start: 2026-10-03 08:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 07:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03ASTWEI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Darya Astakhova (`KXWTACHALLENGERMATCH-26OCT03ASTWEI-AST`) | 0.57 / 0.58 (61) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sijia Wei (`KXWTACHALLENGERMATCH-26OCT03ASTWEI-WEI`) | 0.38 / 0.41 (43) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Sofya Lansere vs Yihan Qu -- WTA 125K Suzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 11:00Z
* Current expected start: 2026-10-03 08:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 07:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03LANYIH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofya Lansere (`KXWTACHALLENGERMATCH-26OCT03LANYIH-LAN`) | 0.70 / 0.74 (325) | 72.0% | -- | -- | -- [-----] | 70.6% | -- | 70.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yihan Qu (`KXWTACHALLENGERMATCH-26OCT03LANYIH-YIH`) | 0.28 / 0.30 (715) | 29.0% | -- | -- | -- [-----] | 29.4% | -- | 29.4% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Nino Ehrenschneider vs Ryuki Matsuda -- M15 Luan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207987:209510:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nino Ehrenschneider (`KXITFMATCH-26OCT02EHRMAT-EHR`) | 0.64 / 0.65 (1394) | 64.5% | -- | 71.9% | 68.4% [66.5%-69.7%] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ryuki Matsuda (`KXITFMATCH-26OCT02EHRMAT-MAT`) | 0.35 / 0.36 (5791) | 35.5% | -- | 28.1% | 31.6% [30.3%-33.5%] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3879.0, B 3092.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0161
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.014, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ugo Humbert vs Jiri Lehecka -- ATP Tokyo R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-02 05:00Z
* Current expected start: 2026-10-03 08:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 07:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1650_MIN

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200005:208103:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ugo Humbert (`KXATPMATCH-26OCT01HUMLEH-HUM`) | 0.39 / 0.40 (9105) | 39.5% | -- | 45.3% | 45.8% [43.4%-47.2%] | -- | -- | -- | -- | SHADOW_BET | +6.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiri Lehecka (`KXATPMATCH-26OCT01HUMLEH-LEH`) | 0.60 / 0.61 (3769) | 60.5% | -- | 54.7% | 54.2% [52.8%-56.6%] | -- | -- | -- | -- | PASS | -6.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5799.0, B 5765.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0192
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.014, surface_dev_loose -0.004, surface_dev_tight -0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01HUMLEH-24` Over 23.5 games: 0.44/0.45 mid 44.5%, model 58.0% (market_conditioned_v1 (model4_board_v1)) -- gap +13.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01HUMLEH-29` Over 28.5 games: 0.29/0.32 mid 30.5%, model 41.9% (market_conditioned_v1 (model4_board_v1)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01HUMLEH-19` Over 18.5 games: 0.83/0.87 mid 85.0%, model 94.3% (market_conditioned_v1 (model4_board_v1)) -- gap +9.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01HUMLEH-LEH6` Will Jiri Lehecka win at least 5.5 more games than Ugo Humbert?: 0.12/0.17 mid 14.5%, model 6.7% (market_conditioned_v1 (model4_board_v1)) -- gap -7.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01HUMLEH-LEH21` Will Jiri Lehecka win the Ugo Humbert vs Jiri Lehecka match by a set score of 2-1?: 0.21/0.23 mid 22.0%, model 28.5% (market_conditioned_v1 (model4_board_v1)) -- gap +6.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01HUMLEH-HUM20` Will Ugo Humbert win the Ugo Humbert vs Jiri Lehecka match by a set score of 2-0?: 0.20/0.23 mid 21.5%, model 16.8% (market_conditioned_v1 (model4_board_v1)) -- gap -4.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01HUMLEH-HUM2` Will Ugo Humbert win at least 1.5 more games than Jiri Lehecka?: 0.31/0.35 mid 33.0%, model 28.4% (market_conditioned_v1 (model4_board_v1)) -- gap -4.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01HUMLEH-LEH20` Will Jiri Lehecka win the Ugo Humbert vs Jiri Lehecka match by a set score of 2-0?: 0.38/0.40 mid 39.0%, model 34.8% (market_conditioned_v1 (model4_board_v1)) -- gap -4.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01HUMLEH-LEH3` Will Jiri Lehecka win at least 2.5 more games than Ugo Humbert?: 0.47/0.48 mid 47.5%, model 43.5% (market_conditioned_v1 (model4_board_v1)) -- gap -4.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01HUMLEH-HUM21` Will Ugo Humbert win the Ugo Humbert vs Jiri Lehecka match by a set score of 2-1?: 0.16/0.19 mid 17.5%, model 19.8% (market_conditioned_v1 (model4_board_v1)) -- gap +2.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; MODEL_ROW_STALE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Yanki Erel vs Mattia Bellucci -- ATP Challenger Jingshan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 08:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-03T08:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207129:208233:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mattia Bellucci (`KXATPCHALLENGERMATCH-26OCT03EREBEL-BEL`) | 0.77 / 0.79 (14595) | 78.0% | -- | 42.0% | 53.5% [47.0%-62.8%] | 75.7% | 78.2% | 78.2% | MODEL_LONE_OUTLIER | PASS | -24.5 pp | HIGH_REVIEW | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Yanki Erel (`KXATPCHALLENGERMATCH-26OCT03EREBEL-ERE`) | 0.22 / 0.23 (9123) | 22.5% | -- | 58.0% | 46.5% [37.2%-53.0%] | 24.3% | 22.0% | 22.0% | MODEL_LONE_OUTLIER | WATCH | +24.0 pp | HIGH_REVIEW | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4118.0, B 7020.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0791
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT03EREBEL-ERE  (YES = Yanki Erel)
Model: 46%
Kalshi: 22%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Francisco Cerundolo vs Jakub Mensik -- ATP Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: 2026-10-03 09:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 08:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+180_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:202103:210150:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cerundolo (`KXATPMATCH-26OCT02CERMEN-CER`) | 0.35 / 0.36 (15323) | 35.5% | -- | 49.5% | 45.0% [42.5%-47.5%] | 35.4% | 36.0% | 35.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +9.5 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jakub Mensik (`KXATPMATCH-26OCT02CERMEN-MEN`) | 0.64 / 0.65 (375) | 64.5% | -- | 50.5% | 55.0% [52.5%-57.5%] | 64.6% | 64.1% | 64.4% | MODEL_LONE_OUTLIER | PASS | -9.5 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 6448.0, B 5037.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0249
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.020, surface_dev_loose -0.005, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT02CERMEN-23` Over 22.5 games: 0.48/0.49 mid 48.5%, model 58.5% (market_conditioned_v1 (model4_board_v1)) -- gap +10.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02CERMEN-28` Over 27.5 games: 0.28/0.30 mid 29.0%, model 38.3% (market_conditioned_v1 (model4_board_v1)) -- gap +9.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02CERMEN-MEN6` Will Jakub Mensik win at least 5.5 more games than Francisco Cerundolo?: 0.20/0.24 mid 22.0%, model 15.4% (market_conditioned_v1 (model4_board_v1)) -- gap -6.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02CERMEN-MEN21` Will Jakub Mensik win the Francisco Cerundolo vs Jakub Mensik match by a set score of 2-1?: 0.22/0.24 mid 23.0%, model 28.7% (market_conditioned_v1 (model4_board_v1)) -- gap +5.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02CERMEN-MEN20` Will Jakub Mensik win the Francisco Cerundolo vs Jakub Mensik match by a set score of 2-0?: 0.40/0.41 mid 40.5%, model 35.6% (market_conditioned_v1 (model4_board_v1)) -- gap -4.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02CERMEN-CER21` Will Francisco Cerundolo win the Francisco Cerundolo vs Jakub Mensik match by a set score of 2-1?: 0.14/0.17 mid 15.5%, model 19.4% (market_conditioned_v1 (model4_board_v1)) -- gap +3.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02CERMEN-18` Over 17.5 games: 0.87/0.90 mid 88.5%, model 92.0% (market_conditioned_v1 (model4_board_v1)) -- gap +3.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02CERMEN-CER20` Will Francisco Cerundolo win the Francisco Cerundolo vs Jakub Mensik match by a set score of 2-0?: 0.18/0.20 mid 19.0%, model 16.2% (market_conditioned_v1 (model4_board_v1)) -- gap -2.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02CERMEN-MEN3` Will Jakub Mensik win at least 2.5 more games than Francisco Cerundolo?: 0.52/0.53 mid 52.5%, model 49.9% (market_conditioned_v1 (model4_board_v1)) -- gap -2.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02CERMEN-CER2` Will Francisco Cerundolo win at least 1.5 more games than Jakub Mensik?: 0.28/0.32 mid 30.0%, model 28.9% (market_conditioned_v1 (model4_board_v1)) -- gap -1.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; THIN_DISPLAYED_SIZE

## Daniil Medvedev vs Jan-Lennard Struff -- ATP Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: 2026-10-03 09:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 08:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+180_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105526:106421:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniil Medvedev (`KXATPMATCH-26OCT02MEDSTR-MED`) | 0.85 / 0.86 (113850) | 85.5% | -- | 84.9% | 85.5% [81.8%-86.1%] | 82.7% | 83.7% | 83.7% | MODEL_LONE_OUTLIER | PASS | -0.0 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26OCT02MEDSTR-STR`) | 0.15 / 0.16 (7361) | 15.5% | -- | 15.1% | 14.5% [14.0%-18.2%] | 17.3% | 16.3% | 16.3% | MODEL_LONE_OUTLIER | PASS | -1.0 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 6997.0, B 5447.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.021
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.012, surface_pool_high +0.006, surface_dev_loose +0.006, surface_dev_tight -0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT02MEDSTR-16` Over 15.5 games: 0.75/0.99 mid 87.0%, model 96.8% (market_conditioned_v1 (model4_board_v1)) -- gap +9.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02MEDSTR-26` Over 25.5 games: 0.28/0.31 mid 29.5%, model 36.2% (market_conditioned_v1 (model4_board_v1)) -- gap +6.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02MEDSTR-MED20` Will Daniil Medvedev win the Daniil Medvedev vs Jan-Lennard Struff match by a set score of 2-0?: 0.61/0.62 mid 61.5%, model 56.0% (market_conditioned_v1 (model4_board_v1)) -- gap -5.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02MEDSTR-21` Over 20.5 games: 0.54/0.55 mid 54.5%, model 59.9% (market_conditioned_v1 (model4_board_v1)) -- gap +5.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02MEDSTR-MED21` Will Daniil Medvedev win the Daniil Medvedev vs Jan-Lennard Struff match by a set score of 2-1?: 0.23/0.24 mid 23.5%, model 28.2% (market_conditioned_v1 (model4_board_v1)) -- gap +4.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02MEDSTR-STR21` Will Jan-Lennard Struff win the Daniil Medvedev vs Jan-Lennard Struff match by a set score of 2-1?: 0.07/0.09 mid 8.0%, model 9.5% (market_conditioned_v1 (model4_board_v1)) -- gap +1.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02MEDSTR-MED2` Will Daniil Medvedev win at least 1.5 more games than Jan-Lennard Struff?: 0.75/0.81 mid 78.0%, model 79.4% (market_conditioned_v1 (model4_board_v1)) -- gap +1.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02MEDSTR-MED5` Will Daniil Medvedev win at least 4.5 more games than Jan-Lennard Struff?: 0.47/0.48 mid 47.5%, model 46.1% (market_conditioned_v1 (model4_board_v1)) -- gap -1.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02MEDSTR-MED8` Will Daniil Medvedev win at least 7.5 more games than Jan-Lennard Struff?: 0.06/0.12 mid 9.0%, model 8.1% (market_conditioned_v1 (model4_board_v1)) -- gap -0.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02MEDSTR-STR20` Will Jan-Lennard Struff win the Daniil Medvedev vs Jan-Lennard Struff match by a set score of 2-0?: 0.06/0.07 mid 6.5%, model 6.3% (market_conditioned_v1 (model4_board_v1)) -- gap -0.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Ha Eum Lee vs Yingqun Sun -- W15 Maanshan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264029:270449:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ha Eum Lee (`KXITFWMATCH-26OCT02LEESUN-LEE`) | 0.63 / 0.64 (11) | 63.5% | -- | 44.7% | 47.9% [45.8%-50.5%] | 63.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.6 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yingqun Sun (`KXITFWMATCH-26OCT02LEESUN-SUN`) | 0.36 / 0.37 (4175) | 36.5% | -- | 55.3% | 52.1% [49.5%-54.2%] | 36.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +15.6 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1048.0, B 1826.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0237
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02LEESUN-SUN  (YES = Yingqun Sun)
Model: 52%
Kalshi: 36%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.000, surface_dev_loose -0.021, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xi Luo vs Zijun Jiang -- W15 Maanshan SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223214:264069:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zijun Jiang (`KXITFWMATCH-26OCT02LUOJIA-JIA`) | 0.34 / 0.35 (1491) | 34.5% | -- | 39.0% | 42.6% [41.5%-42.6%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xi Luo (`KXITFWMATCH-26OCT02LUOJIA-LUO`) | 0.64 / 0.65 (1372) | 64.5% | -- | 61.1% | 57.4% [57.4%-58.5%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 827.0, B 178.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0052
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Francisco Cabral / James Tracy vs Robert Cash / Alexander Erler -- ATP Beijing QF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 09:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-03T09:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03CABTRACASERL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cabral / James Tracy (`KXATPDOUBLES-26OCT03CABTRACASERL-CABTRA`) | 0.54 / 0.58 (654) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Robert Cash / Alexander Erler (`KXATPDOUBLES-26OCT03CABTRACASERL-CASERL`) | 0.42 / 0.45 (292) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Gonzalo Escobar / Niki Kaliyanda Poonacha vs Miguel Angel Reyes-Varela / Reese Stalder -- ATP Challenger Jingshan F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-03T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03ESCKALREYSTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gonzalo Escobar / Niki Kaliyanda Poonacha (`KXATPCHALLENGERDOUBLES-26OCT03ESCKALREYSTA-ESCKAL`) | 0.25 / 0.75 (10) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Miguel Angel Reyes-Varela / Reese Stalder (`KXATPCHALLENGERDOUBLES-26OCT03ESCKALREYSTA-REYSTA`) | 0.06 / 0.80 (15) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Alexander Zverev vs Juncheng Shang -- ATP Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-02 06:00Z
* Current expected start: 2026-10-03 11:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 10:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+1740_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:100644:209992:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juncheng Shang (`KXATPMATCH-26OCT01ZVESHA-SHA`) | 0.08 / 0.09 (12733) | 8.5% | -- | 11.4% | 12.8% [11.1%-14.7%] | -- | -- | -- | -- | SHADOW_BET | +4.3 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Zverev (`KXATPMATCH-26OCT01ZVESHA-ZVE`) | 0.91 / 0.92 (29163) | 91.5% | -- | 88.6% | 87.2% [85.3%-88.9%] | -- | -- | -- | -- | PASS | -4.3 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 8165.0, B 3774.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0182
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.018, surface_dev_loose -0.001, surface_dev_tight +0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01ZVESHA-20` Over 19.5 games: 0.56/0.57 mid 56.5%, model 68.3% (market_conditioned_v1 (model4_board_v1)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01ZVESHA-ZVE6` Will Alexander Zverev win at least 5.5 more games than Juncheng Shang?: 0.39/0.40 mid 39.5%, model 28.4% (market_conditioned_v1 (model4_board_v1)) -- gap -11.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01ZVESHA-15` Over 14.5 games: 0.78/0.99 mid 88.5%, model 99.5% (market_conditioned_v1 (model4_board_v1)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01ZVESHA-ZVE21` Will Alexander Zverev win the Alexander Zverev vs Juncheng Shang match by a set score of 2-1?: 0.17/0.20 mid 18.5%, model 23.6% (market_conditioned_v1 (model4_board_v1)) -- gap +5.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01ZVESHA-25` Over 24.5 games: 0.29/0.30 mid 29.5%, model 33.5% (market_conditioned_v1 (model4_board_v1)) -- gap +4.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01ZVESHA-ZVE20` Will Alexander Zverev win the Alexander Zverev vs Juncheng Shang match by a set score of 2-0?: 0.70/0.73 mid 71.5%, model 68.4% (market_conditioned_v1 (model4_board_v1)) -- gap -3.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01ZVESHA-ZVE3` Will Alexander Zverev win at least 2.5 more games than Juncheng Shang?: 0.83/0.84 mid 83.5%, model 81.2% (market_conditioned_v1 (model4_board_v1)) -- gap -2.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01ZVESHA-ZVE9` Will Alexander Zverev win at least 8.5 more games than Juncheng Shang?: 0.02/0.06 mid 4.0%, model 2.3% (market_conditioned_v1 (model4_board_v1)) -- gap -1.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01ZVESHA-SHA20` Will Juncheng Shang win the Alexander Zverev vs Juncheng Shang match by a set score of 2-0?: 0.02/0.05 mid 3.5%, model 3.0% (market_conditioned_v1 (model4_board_v1)) -- gap -0.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01ZVESHA-SHA21` Will Juncheng Shang win the Alexander Zverev vs Juncheng Shang match by a set score of 2-1?: 0.04/0.06 mid 5.0%, model 4.9% (market_conditioned_v1 (model4_board_v1)) -- gap -0.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; MODEL_ROW_STALE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Sonay Kartal vs Xinyu Wang -- WTA Beijing R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-02 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-03 11:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 10:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT01KARWAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sonay Kartal (`KXWTAMATCH-26OCT01KARWAN-KAR`) | 0.50 / 0.51 (12206) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xinyu Wang (`KXWTAMATCH-26OCT01KARWAN-WAN`) | 0.49 / 0.50 (448) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Yi Liu / Sun vs Yi Chen / Luo -- W15 Maanshan F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03YILSUNYICLUO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yi Chen / Luo (`KXITFWDOUBLES-26OCT03YILSUNYICLUO-YICLUO`) | 0.49 / 0.75 (3) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yi Liu / Sun (`KXITFWDOUBLES-26OCT03YILSUNYICLUO-YILSUN`) | 0.21 / 0.51 (0) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Herman Hoeyeraal vs Casey Hoole -- M25 Darwin SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208382:211315:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Herman Hoeyeraal (`KXITFMATCH-26OCT03HOEHOO-HOE`) | 0.38 / 0.39 (368) | 38.5% | -- | 56.9% | 44.6% [42.2%-47.0%] | -- | -- | -- | -- | PASS | +6.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Casey Hoole (`KXITFMATCH-26OCT03HOEHOO-HOO`) | 0.62 / 0.63 (4810) | 62.5% | -- | 43.1% | 55.4% [52.9%-57.8%] | -- | -- | -- | -- | PASS | -7.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1869.0, B 187.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0244
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.024, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Erika Andreeva vs Lois Boisson -- WTA 125K Adana SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 15:00Z
* Current expected start: 2026-10-03 12:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 11:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03ANDBOI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Erika Andreeva (`KXWTACHALLENGERMATCH-26OCT03ANDBOI-AND`) | 0.29 / 0.30 (743) | 29.5% | -- | -- | -- [-----] | 31.2% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lois Boisson (`KXWTACHALLENGERMATCH-26OCT03ANDBOI-BOI`) | 0.70 / 0.72 (13070) | 71.0% | -- | -- | -- [-----] | 68.8% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Luis Carlos Alvarez Valdes / Adrian Oetzbach vs Oleksandr Ovcharenko / Kai Wehnelt -- ATP Challenger Bari F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-03T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03ALVAOETOVCWEH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Carlos Alvarez Valdes / Adrian Oetzbach (`KXATPCHALLENGERDOUBLES-26OCT03ALVAOETOVCWEH-ALVAOET`) | 0.39 / 0.49 (500) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oleksandr Ovcharenko / Kai Wehnelt (`KXATPCHALLENGERDOUBLES-26OCT03ALVAOETOVCWEH-OVCWEH`) | 0.51 / 0.61 (500) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Millen Hurrion vs Kerem Yilmaz -- M15 Baku SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-03T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209140:212030:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Millen Hurrion (`KXITFMATCH-26OCT03HURYIL-HUR`) | 0.79 / 0.80 (2) | 79.5% | -- | 76.4% | 78.4% [76.8%-79.5%] | 76.8% | -- | 76.8% | KALSHI_LONE_OUTLIER | PASS | -1.1 pp | NORMAL | STALE | B / ADEQUATE | ALL_AGREE | VERIFIED |
| Kerem Yilmaz (`KXITFMATCH-26OCT03HURYIL-YIL`) | 0.19 / 0.21 (6568) | 20.0% | -- | 23.6% | 21.6% [20.5%-23.2%] | 23.2% | -- | 23.2% | KALSHI_LONE_OUTLIER | PASS | +1.6 pp | NORMAL | AGING | B / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3153.0, B 1537.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0138
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ichikawa / Jeong vs HSUN LIN / Yang -- M15 Luan F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03ICHJEOHSUYAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HSUN LIN / Yang (`KXITFDOUBLES-26OCT03ICHJEOHSUYAN-HSUYAN`) | 0.08 / 0.48 (48) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ichikawa / Jeong (`KXITFDOUBLES-26OCT03ICHJEOHSUYAN-ICHJEO`) | 0.07 / 0.67 (78) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Marcus Walters vs Digvijay Pratap Singh -- M15 Baku SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-03T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126971:200014:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Digvijay Pratap Singh (`KXITFMATCH-26OCT03WALSIN-SIN`) | 0.69 / 0.70 (2816) | 69.5% | -- | 54.9% | 59.3% [57.3%-61.3%] | 68.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.2 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marcus Walters (`KXITFMATCH-26OCT03WALSIN-WAL`) | 0.29 / 0.30 (1209) | 29.5% | -- | 45.1% | 40.7% [38.7%-42.7%] | 31.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +11.2 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2102.0, B 2204.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0197
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elena Rybakina vs Alina Charaeva -- WTA Beijing R64

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-02 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-03 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 01:04Z
* Recommended handicap-by time: 2026-10-03 11:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214981:221406:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Charaeva (`KXWTAMATCH-26OCT01RYBCHA-CHA`) | 0.06 / 0.07 (21747) | 6.5% | -- | 5.3% | 5.2% [4.9%-5.9%] | -- | -- | -- | -- | PASS | -1.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Rybakina (`KXWTAMATCH-26OCT01RYBCHA-RYB`) | 0.93 / 0.94 (8947) | 93.5% | -- | 94.7% | 94.8% [94.1%-95.1%] | -- | -- | -- | -- | PASS | +1.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6087.0, B 3668.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0048
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.003, surface_dev_loose -0.001, surface_dev_tight -0.003
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT01RYBCHA-18` Over 17.5 games: 0.54/0.55 mid 54.5%, model 71.3% (market_conditioned_v1 (model4_board_v1)) -- gap +16.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01RYBCHA-23` Over 22.5 games: 0.16/0.46 mid 31.0%, model 28.9% (market_conditioned_v1 (model4_board_v1)) -- gap -2.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; MODEL_ROW_STALE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hayden Jones vs Derek Pham -- M25 Darwin SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210436:210613:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hayden Jones (`KXITFMATCH-26OCT03JONPHA-JON`) | 0.56 / 0.57 (150) | 56.5% | -- | 50.0% | 45.4% [44.9%-46.5%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.1 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Derek Pham (`KXITFMATCH-26OCT03JONPHA-PHA`) | 0.41 / 0.42 (3) | 41.5% | -- | 50.0% | 54.6% [53.5%-55.1%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.1 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1969.0, B 178.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0079
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Finn Bass / Scott Duncan vs Karl Poling / Joshua Sheehy -- ATP Challenger Mouilleron-Le-Captif F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-03T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03BASDUNPOLSHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Finn Bass / Scott Duncan (`KXATPCHALLENGERDOUBLES-26OCT03BASDUNPOLSHE-BASDUN`) | 0.41 / 0.51 (500) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karl Poling / Joshua Sheehy (`KXATPCHALLENGERDOUBLES-26OCT03BASDUNPOLSHE-POLSHE`) | 0.49 / 0.59 (500) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## David Jorda Sanchis vs Inaki Montes-de la Torre -- ATP Challenger Porto 2 SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-03T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122554:208540:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Jorda Sanchis (`KXATPCHALLENGERMATCH-26OCT03JORMON-JOR`) | 0.29 / 0.30 (6815) | 29.5% | -- | 26.1% | 27.0% [25.3%-30.9%] | 30.3% | -- | 30.3% | MODEL_LONE_OUTLIER | PASS | -2.5 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Inaki Montes-de la Torre (`KXATPCHALLENGERMATCH-26OCT03JORMON-MON`) | 0.70 / 0.72 (3434) | 71.0% | -- | 73.9% | 73.0% [69.1%-74.7%] | 69.7% | -- | 69.7% | MODEL_LONE_OUTLIER | PASS | +2.0 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5646.0, B 4378.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0282
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.008, surface_dev_loose -0.015, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Stijn Paardekooper vs Dmitry Popko -- M15 Telavi F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-03T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122078:212311:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stijn Paardekooper (`KXITFMATCH-26OCT03PAAPOP-PAA`) | 0.25 / 0.28 (4241) | 26.5% | -- | 50.0% | 32.6% [18.3%-41.3%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +6.0 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dmitry Popko (`KXITFMATCH-26OCT03PAAPOP-POP`) | 0.72 / 0.74 (73) | 73.0% | -- | 50.0% | 67.5% [58.7%-81.7%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.5 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1300.0, B 4384.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.115
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.041, surface_pool_high +0.048, surface_dev_loose +0.014, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Robert Strombachs vs Paul Jubb -- M15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206703:207669:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Paul Jubb (`KXITFMATCH-26OCT03STRJUB-JUB`) | 0.64 / 0.66 (1066) | 65.0% | -- | 59.1% | 59.6% [58.6%-61.1%] | -- | -- | -- | -- | PASS | -5.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Robert Strombachs (`KXITFMATCH-26OCT03STRJUB-STR`) | 0.33 / 0.35 (4353) | 34.0% | -- | 40.9% | 40.4% [38.9%-41.4%] | -- | -- | -- | -- | WATCH | +6.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3812.0, B 4251.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0124
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fares Zakaria vs Karan Singh -- M15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-03T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03ZAKSIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karan Singh (`KXITFMATCH-26OCT03ZAKSIN-SIN`) | 0.73 / 0.74 (99) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fares Zakaria (`KXITFMATCH-26OCT03ZAKSIN-ZAK`) | 0.24 / 0.27 (0) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jade Groen vs Yuliya Hatouka -- W15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216013:267722:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jade Groen (`KXITFWMATCH-26OCT03GROHAT-GRO`) | 0.29 / 0.30 (35) | 29.5% | -- | 25.1% | 15.7% [12.7%-17.4%] | -- | -- | -- | -- | PASS | -13.8 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuliya Hatouka (`KXITFWMATCH-26OCT03GROHAT-HAT`) | 0.69 / 0.70 (2) | 69.5% | -- | 74.9% | 84.3% [82.6%-87.3%] | -- | -- | -- | -- | PASS | +14.8 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 470.0, B 2126.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0232
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.006, surface_pool_high +0.006, surface_dev_loose +0.000, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria Zelinskaya vs Antonina Sushkova -- W15 Sharm ElSheikh SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:239158:266849:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Antonina Sushkova (`KXITFWMATCH-26OCT03ZELSUS-SUS`) | 0.65 / 0.66 (75) | 65.5% | -- | 26.7% | 23.8% [23.4%-24.6%] | -- | -- | -- | -- | PASS | -41.7 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daria Zelinskaya (`KXITFWMATCH-26OCT03ZELSUS-ZEL`) | 0.33 / 0.36 (1) | 34.5% | -- | 73.3% | 76.2% [75.4%-76.6%] | -- | -- | -- | -- | PASS | +41.7 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2491.0, B 527.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0061
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT03ZELSUS-ZEL  (YES = Daria Zelinskaya)
Model: 76%
Kalshi: 34%
Gap: +42 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.004, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vitaliy Sachko vs Samuele Pieri -- ATP Challenger Bari SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-03T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03SACPIE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samuele Pieri (`KXATPCHALLENGERMATCH-26OCT03SACPIE-PIE`) | 0.24 / 0.25 (2426) | 24.5% | -- | -- | -- [-----] | 26.0% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vitaliy Sachko (`KXATPCHALLENGERMATCH-26OCT03SACPIE-SAC`) | 0.75 / 0.76 (426) | 75.5% | -- | -- | -- [-----] | 74.0% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Felitsata Dorofeeva-Rybas vs Sonja Zhenikhova -- W15 Varna SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-03T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264961:267022:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felitsata Dorofeeva-Rybas (`KXITFWMATCH-26OCT03DORZHE-DOR`) | 0.79 / 0.82 (40) | 80.5% | -- | 65.2% | 60.6% [57.5%-63.7%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -19.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sonja Zhenikhova (`KXITFWMATCH-26OCT03DORZHE-ZHE`) | 0.18 / 0.21 (3148) | 19.5% | -- | 34.8% | 39.4% [36.3%-42.5%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +19.9 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 923.0, B 1212.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0311
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT03DORZHE-ZHE  (YES = Sonja Zhenikhova)
Model: 39%
Kalshi: 20%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.005, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giulia Safina Popa vs Sapfo Sakellaridi -- W15 Varna SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-03T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220364:267428:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giulia Safina Popa (`KXITFWMATCH-26OCT03POPSAK-POP`) | 0.63 / 0.65 (67) | 64.0% | -- | 52.6% | 51.6% [47.4%-54.2%] | 63.8% | -- | 63.8% | MODEL_LONE_OUTLIER | PASS | -12.4 pp | REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Sapfo Sakellaridi (`KXITFWMATCH-26OCT03POPSAK-SAK`) | 0.33 / 0.36 (4879) | 34.5% | -- | 47.4% | 48.4% [45.8%-52.6%] | 36.2% | -- | 36.2% | MODEL_LONE_OUTLIER | PASS | +13.9 pp | REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1013.0, B 4165.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0343
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.021, surface_dev_loose +0.016, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arzhankin / Kunitsyn vs Lorusso / Senn -- M15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03ARZKUNLORSEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arzhankin / Kunitsyn (`KXITFDOUBLES-26OCT03ARZKUNLORSEN-ARZKUN`) | 0.12 / 0.61 (66) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lorusso / Senn (`KXITFDOUBLES-26OCT03ARZKUNLORSEN-LORSEN`) | 0.12 / 0.56 (58) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Connel / Walters vs Delicata / Stamatopoulos -- M15 Baku F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03CONWALDELSTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Connel / Walters (`KXITFDOUBLES-26OCT03CONWALDELSTA-CONWAL`) | 0.07 / 0.86 (185) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Delicata / Stamatopoulos (`KXITFDOUBLES-26OCT03CONWALDELSTA-DELSTA`) | 0.06 / 0.27 (34) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Opitz / Wessels vs Adrian Andreescu / Claudiu Schinteie -- M25 Slobozia F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03OPIWESADRCLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Andreescu / Claudiu Schinteie (`KXITFDOUBLES-26OCT03OPIWESADRCLA-ADRCLA`) | 0.07 / 0.14 (0) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Opitz / Wessels (`KXITFDOUBLES-26OCT03OPIWESADRCLA-OPIWES`) | 0.07 / 0.93 (45) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Henrique Rocha vs Jerome Kym -- ATP Challenger Porto 2 SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 14:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-03T14:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03ROCKYM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jerome Kym (`KXATPCHALLENGERMATCH-26OCT03ROCKYM-KYM`) | 0.42 / 0.44 (6957) | 43.0% | -- | -- | -- [-----] | 43.7% | -- | 43.7% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Henrique Rocha (`KXATPCHALLENGERMATCH-26OCT03ROCKYM-ROC`) | 0.57 / 0.58 (1951) | 57.5% | -- | -- | -- [-----] | 56.3% | -- | 56.3% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Hoeyeraal / Padgham vs Beale / Vujic -- M25 Darwin F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03HOEPADBEAVUJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beale / Vujic (`KXITFDOUBLES-26OCT03HOEPADBEAVUJ-BEAVUJ`) | 0.12 / 0.60 (40) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hoeyeraal / Padgham (`KXITFDOUBLES-26OCT03HOEPADBEAVUJ-HOEPAD`) | 0.40 / 0.43 (12) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ryan Nijboer vs Alexander Ritschard -- M25 Zaragoza SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 14:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-03T14:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106310:207764:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryan Nijboer (`KXITFMATCH-26OCT03NIJRIT-NIJ`) | 0.28 / 0.32 (3438) | 30.0% | -- | 24.2% | 21.1% [18.6%-22.7%] | 30.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Ritschard (`KXITFMATCH-26OCT03NIJRIT-RIT`) | 0.68 / 0.72 (3) | 70.0% | -- | 75.8% | 78.9% [77.3%-81.4%] | 69.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4005.0, B 3172.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0205
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose -0.011, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Biletic / Kajin vs Jeran / Kupcic -- M15 Sibenik F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03BILKAJJERKUP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Biletic / Kajin (`KXITFDOUBLES-26OCT03BILKAJJERKUP-BILKAJ`) | 0.14 / 0.56 (1) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeran / Kupcic (`KXITFDOUBLES-26OCT03BILKAJJERKUP-JERKUP`) | 0.12 / 0.59 (60) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Emilien Demanet vs Tuncay Duran -- M15 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210513:212598:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emilien Demanet (`KXITFMATCH-26OCT03DEMDUR-DEM`) | 0.43 / 0.45 (342) | 44.0% | -- | 36.9% | 41.8% [38.4%-49.5%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tuncay Duran (`KXITFMATCH-26OCT03DEMDUR-DUR`) | 0.54 / 0.56 (4133) | 55.0% | -- | 63.1% | 58.2% [50.5%-61.6%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2543.0, B 2317.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0556
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose -0.020, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Calvin Hemery vs Florent Bax -- M25 Kigali SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-03T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:123921:202147:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florent Bax (`KXITFMATCH-26OCT03HEMBAX-BAX`) | 0.38 / 0.42 (60) | 40.0% | -- | 62.6% | 54.9% [49.5%-58.3%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +14.9 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Calvin Hemery (`KXITFMATCH-26OCT03HEMBAX-HEM`) | 0.59 / 0.62 (176) | 60.5% | -- | 37.4% | 45.1% [41.7%-50.5%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -15.4 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5909.0, B 4639.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.044
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose -0.019, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Noah Lopez vs Martin VAN DER MEERSCHEN -- M15 Sibenik SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-03T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207592:210055:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noah Lopez (`KXITFMATCH-26OCT03LOPVAN-LOP`) | 0.27 / 0.30 (15) | 28.5% | -- | 38.2% | 32.8% [29.2%-34.7%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +4.3 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Martin VAN DER MEERSCHEN (`KXITFMATCH-26OCT03LOPVAN-VAN`) | 0.70 / 0.73 (1298) | 71.5% | -- | 61.8% | 67.2% [65.3%-70.8%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.3 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1139.0, B 2224.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0276
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.009, surface_dev_loose -0.018, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kris van Wyk vs Lars Goran Verwerft -- M15 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144748:213121:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kris van Wyk (`KXITFMATCH-26OCT03VANVER-VAN`) | 0.33 / 0.34 (925) | 33.5% | -- | 17.1% | 44.2% [36.0%-53.7%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +10.7 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lars Goran Verwerft (`KXITFMATCH-26OCT03VANVER-VER`) | 0.65 / 0.67 (4512) | 66.0% | -- | 82.9% | 55.8% [46.3%-63.9%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.2 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2787.0, B 832.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0881
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose -0.021, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lan Mi vs Ekaterina Dotsenko -- W15 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-03T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03MIXDOT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Dotsenko (`KXITFWMATCH-26OCT03MIXDOT-DOT`) | 0.52 / 0.56 (3252) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lan Mi (`KXITFWMATCH-26OCT03MIXDOT-MIX`) | 0.44 / 0.48 (48) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lisa Pigato vs Katie Swan -- W75 Quinta do Lago SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215042:221354:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lisa Pigato (`KXITFWMATCH-26OCT03PIGSWA-PIG`) | 0.37 / 0.39 (3890) | 38.0% | -- | 47.3% | 44.7% [41.6%-50.5%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +6.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katie Swan (`KXITFWMATCH-26OCT03PIGSWA-SWA`) | 0.60 / 0.61 (225) | 60.5% | -- | 52.6% | 55.3% [49.5%-58.4%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4114.0, B 2343.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0448
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.037, surface_pool_high -0.031, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marta Soriano Santiago vs Sophia Biolay -- W15 Monastir SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221192:259105:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sophia Biolay (`KXITFWMATCH-26OCT03SORBIO-BIO`) | 0.64 / 0.68 (3380) | 66.0% | -- | 85.5% | 69.9% [62.6%-76.9%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.9 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marta Soriano Santiago (`KXITFWMATCH-26OCT03SORBIO-SOR`) | 0.32 / 0.35 (3330) | 33.5% | -- | 14.5% | 30.1% [23.1%-37.4%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.4 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1358.0, B 766.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0716
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.019, surface_dev_loose -0.009, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabi Adrian Boitan vs Borys Zgola -- M25 Slobozia SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-03T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03BOIZGO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabi Adrian Boitan (`KXITFMATCH-26OCT03BOIZGO-BOI`) | 0.89 / 0.91 (2801) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Borys Zgola (`KXITFMATCH-26OCT03BOIZGO-ZGO`) | 0.09 / 0.11 (8) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joel Schwaerzler vs Sascha Gueymard Wayenburg -- ATP Challenger Mouilleron-Le-Captif SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-03T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03SCHGUE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sascha Gueymard Wayenburg (`KXATPCHALLENGERMATCH-26OCT03SCHGUE-GUE`) | 0.59 / 0.61 (2746) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Joel Schwaerzler (`KXATPCHALLENGERMATCH-26OCT03SCHGUE-SCH`) | 0.39 / 0.41 (2419) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Branger / Dugardin vs Nagoudi / Piatti -- M15 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03BRADUGNAGPIA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Branger / Dugardin (`KXITFDOUBLES-26OCT03BRADUGNAGPIA-BRADUG`) | 0.12 / 0.70 (86) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nagoudi / Piatti (`KXITFDOUBLES-26OCT03BRADUGNAGPIA-NAGPIA`) | 0.12 / 0.49 (49) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Max Houkes vs Benjamin Lock -- M25 Kigali SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-03T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111761:208069:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Houkes (`KXITFMATCH-26OCT03HOULOC-HOU`) | 0.84 / 0.88 (4029) | 86.0% | -- | 79.5% | 78.3% [71.4%-80.1%] | 86.7% | -- | 86.7% | MODEL_LONE_OUTLIER | PASS | -7.7 pp | NORMAL | STALE | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Benjamin Lock (`KXITFMATCH-26OCT03HOULOC-LOC`) | 0.11 / 0.13 (21) | 12.0% | -- | 20.5% | 21.6% [19.9%-28.6%] | 13.3% | -- | 13.3% | MODEL_LONE_OUTLIER | PASS | +9.7 pp | NORMAL | STALE | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5070.0, B 4430.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0439
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose -0.000, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alejandro Moro Canas vs Sander Jong -- M25 Zaragoza SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-03T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208279:210093:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sander Jong (`KXITFMATCH-26OCT03MORJON-JON`) | 0.33 / 0.35 (995) | 34.0% | -- | 38.9% | 34.1% [25.6%-38.9%] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.1 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Moro Canas (`KXITFMATCH-26OCT03MORJON-MOR`) | 0.64 / 0.67 (27) | 65.5% | -- | 61.1% | 65.9% [61.1%-74.4%] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.4 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6297.0, B 1938.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0668
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.028, surface_pool_high -0.029, surface_dev_loose +0.001, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eva Vedder vs Margaux Rouvroy -- W75 Quinta do Lago SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220770:221191:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Margaux Rouvroy (`KXITFWMATCH-26OCT03VEDROU-ROU`) | 0.37 / 0.38 (1) | 37.5% | -- | 60.4% | 58.9% [52.6%-60.9%] | 38.5% | -- | 38.5% | MODEL_LONE_OUTLIER | WATCH | +21.4 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Eva Vedder (`KXITFWMATCH-26OCT03VEDROU-VED`) | 0.61 / 0.63 (3452) | 62.0% | -- | 39.6% | 41.1% [39.1%-47.4%] | 61.5% | -- | 61.5% | MODEL_LONE_OUTLIER | PASS | -20.9 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3271.0, B 3212.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0412
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT03VEDROU-ROU  (YES = Margaux Rouvroy)
Model: 59%
Kalshi: 38%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.020, surface_dev_loose -0.010, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikita Mashtakov vs Charles Bertimon -- M15 Sibenik SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-03T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03MASBER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charles Bertimon (`KXITFMATCH-26OCT03MASBER-BER`) | 0.16 / 0.17 (4508) | 16.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nikita Mashtakov (`KXITFMATCH-26OCT03MASBER-MAS`) | 0.83 / 0.84 (162) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Radu David Turcanu vs Sebastian Gima -- M25 Slobozia SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-10-03T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209142:212886:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Gima (`KXITFMATCH-26OCT03TURGIM-GIM`) | 0.40 / 0.43 (17) | 41.5% | -- | 42.2% | 42.2% [40.2%-45.9%] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.7 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Radu David Turcanu (`KXITFMATCH-26OCT03TURGIM-TUR`) | 0.56 / 0.60 (4469) | 58.0% | -- | 57.8% | 57.8% [54.1%-59.8%] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.2 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2393.0, B 3345.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0283
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.020, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gatoto / Shalin Shah vs Nefve / Schachter -- M25 Kigali F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03GATSHANEFSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gatoto / Shalin Shah (`KXITFDOUBLES-26OCT03GATSHANEFSCH-GATSHA`) | 0.06 / 0.25 (33) | 15.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nefve / Schachter (`KXITFDOUBLES-26OCT03GATSHANEFSCH-NEFSCH`) | 0.06 / 0.94 (147) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Sada Nahimana vs Isis Louise Van den Broek -- W35 Reims SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216367:264227:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sada Nahimana (`KXITFWMATCH-26OCT03NAHVAN-NAH`) | 0.43 / 0.45 (20) | 44.0% | -- | 27.0% | 34.4% [28.8%-46.3%] | 43.9% | -- | 43.9% | MARKETS_AGREE | PASS | -9.6 pp | NORMAL | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Isis Louise Van den Broek (`KXITFWMATCH-26OCT03NAHVAN-VAN`) | 0.54 / 0.57 (397) | 55.5% | -- | 73.0% | 65.6% [53.7%-71.2%] | 56.1% | -- | 56.1% | MARKETS_AGREE | WATCH | +10.1 pp | REVIEW | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2636.0, B 1856.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0876
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.024, surface_dev_loose -0.034, surface_dev_tight +0.025
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bertacchi / Dibenedetto vs Biolay / Cirotte -- W15 Monastir F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03BERDIBBIOCIR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bertacchi / Dibenedetto (`KXITFWDOUBLES-26OCT03BERDIBBIOCIR-BERDIB`) | 0.06 / 0.50 (52) | 28.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Biolay / Cirotte (`KXITFWDOUBLES-26OCT03BERDIBBIOCIR-BIOCIR`) | 0.06 / 0.72 (92) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Lopez Martos / Palomar vs Ifi / Stanke -- M25 Zaragoza F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03LOPPALIFISTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ifi / Stanke (`KXITFDOUBLES-26OCT03LOPPALIFISTA-IFISTA`) | 0.07 / 0.94 (147) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lopez Martos / Palomar (`KXITFDOUBLES-26OCT03LOPPALIFISTA-LOPPAL`) | 0.06 / 0.94 (147) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Salma Djoubri vs Britt Du Pree -- W35 Reims SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220305:264228:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Salma Djoubri (`KXITFWMATCH-26OCT03DJODUP-DJO`) | 0.20 / 0.21 (101) | 20.5% | -- | 12.7% | 31.4% [25.5%-38.4%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.9 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Britt Du Pree (`KXITFWMATCH-26OCT03DJODUP-DUP`) | 0.76 / 0.81 (4344) | 78.5% | -- | 87.3% | 68.6% [61.6%-74.5%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.9 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 169.0, B 2691.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0644
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.039, surface_pool_high -0.028, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hugo Coquelin vs Oliver Bonding -- M15 Ann Arbor MI SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-03T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03COQBON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oliver Bonding (`KXITFMATCH-26OCT03COQBON-BON`) | 0.79 / 0.84 (3) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hugo Coquelin (`KXITFMATCH-26OCT03COQBON-COQ`) | 0.16 / 0.22 (34) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Theo Papamalamis vs Alexander Rozin -- M15 Fayetteville AR SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-03T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03PAPROZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Papamalamis (`KXITFMATCH-26OCT03PAPROZ-PAP`) | 0.05 / 0.90 (5) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Rozin (`KXITFMATCH-26OCT03PAPROZ-ROZ`) | 0.05 / 0.90 (5) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Naoto Tomizawa vs Max Dahlin -- M15 Ann Arbor MI SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-03T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03TOMDAH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Dahlin (`KXITFMATCH-26OCT03TOMDAH-DAH`) | 0.35 / 0.89 (62) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Naoto Tomizawa (`KXITFMATCH-26OCT03TOMDAH-TOM`) | 0.05 / 0.19 (30) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amandine Hesse vs Charo Esquiva Banuls -- W35 Baza SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-03T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03HESESQ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charo Esquiva Banuls (`KXITFWMATCH-26OCT03HESESQ-ESQ`) | 0.57 / 0.60 (3517) | 58.5% | -- | -- | -- [-----] | 58.1% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Amandine Hesse (`KXITFWMATCH-26OCT03HESESQ-HES`) | 0.40 / 0.44 (3344) | 42.0% | -- | -- | -- [-----] | 41.9% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jonah Braswell vs Dominick Mosejczuk -- M15 Fayetteville AR SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03BRAMOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonah Braswell (`KXITFMATCH-26OCT03BRAMOS-BRA`) | 0.37 / 0.41 (460) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dominick Mosejczuk (`KXITFMATCH-26OCT03BRAMOS-MOS`) | 0.57 / 0.62 (104) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fradkin / Kuhar vs Sheldon / Swenson -- M15 Ann Arbor MI F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03FRAKUHSHESWE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fradkin / Kuhar (`KXITFDOUBLES-26OCT03FRAKUHSHESWE-FRAKUH`) | 0.06 / 0.94 (147) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sheldon / Swenson (`KXITFDOUBLES-26OCT03FRAKUHSHESWE-SHESWE`) | 0.06 / 0.94 (147) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Celia Cervino Ruiz vs Valentina Ivanov -- W35 Baza SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-03T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03CERIVA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Celia Cervino Ruiz (`KXITFWMATCH-26OCT03CERIVA-CER`) | 0.46 / 0.49 (0) | 47.5% | -- | -- | -- [-----] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Valentina Ivanov (`KXITFWMATCH-26OCT03CERIVA-IVA`) | 0.51 / 0.54 (150) | 52.5% | -- | -- | -- [-----] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
