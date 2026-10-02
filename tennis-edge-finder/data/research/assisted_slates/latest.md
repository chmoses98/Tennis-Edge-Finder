# ASSISTED SLATE -- 2026-10-02T06:12Z (`SL-20261002T061255Z-456d5bef`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

207 open matches not seen started, 790 markets. Skipped: {"first_ball_already_observed": 8, "scheduled_start_over_24h_past": 1, "no_match_winner_listed": 1}. Sources: shadow board 2026-10-02T06:09:12.133291+00:00, Model 4 2026-10-02T06:09:27.714667+00:00, Gen-1 ledger 2026-10-02T06:09:09.086637+00:00, external 2026-10-02T05:23:53.643371+00:00, capture 20261002T053857Z.quotes.jsonl.gz.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 35, "HIGH_REVIEW": 50, "NORMAL": 292, "REVIEW": 96, "UNPRICED": 317}; match winners: {"EXTREME": 30, "HIGH_REVIEW": 43, "NORMAL": 163, "REVIEW": 44, "UNPRICED": 134}; quote freshness at build: {"STALE": 473}.

## Elias Ymer vs Federico Cina -- ATP Challenger Jingshan R16

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-01T07:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:111200:210748:2026-10-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Cina (`KXATPCHALLENGERMATCH-26OCT01YMECIN-CIN`) | 0.99 / -- (0) | -- | 58.0% | 60.4% | 60.9% [59.4%-62.3%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | A / ADEQUATE | INSUFFICIENT_INPUTS | VERIFIED |
| Elias Ymer (`KXATPCHALLENGERMATCH-26OCT01YMECIN-YME`) | -- / 0.01 (44788) | -- | 42.0% | 39.6% | 39.1% [37.8%-40.6%] | -- | -- | -- | -- | SHADOW_BET | -- | UNPRICED | STALE | A / ADEQUATE | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 5409.0, B 3635.0; serve-point win A 61.8%, B 36.6%; Elo A 1618.1, B 1702.2; model uncertainty 0.0141
* Form inputs: days since last match A 9, B 5; matches on record A 1064, B 187; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.014, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

## Lloyd Harris / Cheng-Peng Hsieh vs Nathaniel Lammons / Jackson Withrow -- ATP Challenger Jingshan QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T08:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HARHSILAMWIT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lloyd Harris / Cheng-Peng Hsieh (`KXATPCHALLENGERDOUBLES-26OCT01HARHSILAMWIT-HARHSI`) | 0.23 / 0.27 (26) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nathaniel Lammons / Jackson Withrow (`KXATPCHALLENGERDOUBLES-26OCT01HARHSILAMWIT-LAMWIT`) | 0.68 / 0.77 (500) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Ryan Seggerman / Bart Stevens vs Alex Bolt / Adam Walton -- ATP Challenger Jingshan QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T08:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01SEGSTEBOLWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Bolt / Adam Walton (`KXATPCHALLENGERDOUBLES-26OCT01SEGSTEBOLWAL-BOLWAL`) | 0.24 / 0.29 (14) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ryan Seggerman / Bart Stevens (`KXATPCHALLENGERDOUBLES-26OCT01SEGSTEBOLWAL-SEGSTE`) | 0.67 / 0.74 (90) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Gonzalo Escobar / Niki Kaliyanda Poonacha vs Mitsuki Wei Kang Leong / Stefanos Sakellaridis -- ATP Challenger Jingshan QF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-01T09:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01ESCKALLEOSAK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gonzalo Escobar / Niki Kaliyanda Poonacha (`KXATPCHALLENGERDOUBLES-26OCT01ESCKALLEOSAK-ESCKAL`) | 0.73 / 0.80 (9) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mitsuki Wei Kang Leong / Stefanos Sakellaridis (`KXATPCHALLENGERDOUBLES-26OCT01ESCKALLEOSAK-LEOSAK`) | 0.18 / 0.21 (14) | 19.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arthur Fils vs Frances Tiafoe -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126207:209950:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fils (`KXATPMATCH-26OCT01FILTIA-FIL`) | 0.69 / 0.70 (34855) | 69.5% | -- | 69.5% | 67.8% [64.3%-69.0%] | 69.1% | 69.7% | 69.7% | MODEL_LONE_OUTLIER | PASS | -1.7 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Frances Tiafoe (`KXATPMATCH-26OCT01FILTIA-TIA`) | 0.31 / 0.32 (50970) | 31.5% | -- | 30.5% | 32.2% [31.0%-35.7%] | 30.9% | 30.1% | 30.1% | MODEL_LONE_OUTLIER | PASS | +0.7 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5009.0, B 5884.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0235
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.000, surface_dev_loose +0.012, surface_dev_tight -0.013
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01FILTIA-24` Over 23.5 games: 0.43/0.44 mid 43.5%, model 53.5% (market_conditioned_v1 (model4_board_v1)) -- gap +10.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01FILTIA-29` Over 28.5 games: 0.27/0.28 mid 27.5%, model 37.1% (market_conditioned_v1 (model4_board_v1)) -- gap +9.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01FILTIA-FIL6` Will Arthur Fils win at least 5.5 more games than Frances Tiafoe?: 0.21/0.22 mid 21.5%, model 12.2% (market_conditioned_v1 (model4_board_v1)) -- gap -9.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01FILTIA-19` Over 18.5 games: 0.80/0.85 mid 82.5%, model 90.1% (market_conditioned_v1 (model4_board_v1)) -- gap +7.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01FILTIA-FIL3` Will Arthur Fils win at least 2.5 more games than Frances Tiafoe?: 0.58/0.59 mid 58.5%, model 51.8% (market_conditioned_v1 (model4_board_v1)) -- gap -6.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01FILTIA-FIL21` Will Arthur Fils win the Arthur Fils vs Frances Tiafoe match by a set score of 2-1?: 0.23/0.25 mid 24.0%, model 29.3% (market_conditioned_v1 (model4_board_v1)) -- gap +5.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01FILTIA-FIL20` Will Arthur Fils win the Arthur Fils vs Frances Tiafoe match by a set score of 2-0?: 0.43/0.45 mid 44.0%, model 39.3% (market_conditioned_v1 (model4_board_v1)) -- gap -4.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01FILTIA-TIA21` Will Frances Tiafoe win the Arthur Fils vs Frances Tiafoe match by a set score of 2-1?: 0.14/0.16 mid 15.0%, model 17.4% (market_conditioned_v1 (model4_board_v1)) -- gap +2.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01FILTIA-TIA20` Will Frances Tiafoe win the Arthur Fils vs Frances Tiafoe match by a set score of 2-0?: 0.15/0.16 mid 15.5%, model 13.9% (market_conditioned_v1 (model4_board_v1)) -- gap -1.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01FILTIA-TIA2` Will Frances Tiafoe win at least 1.5 more games than Arthur Fils?: 0.23/0.25 mid 24.0%, model 24.4% (market_conditioned_v1 (model4_board_v1)) -- gap +0.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Ugo Humbert vs Jiri Lehecka -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200005:208103:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ugo Humbert (`KXATPMATCH-26OCT01HUMLEH-HUM`) | 0.36 / 0.37 (5273) | 36.5% | -- | 45.3% | 45.8% [43.4%-47.2%] | -- | -- | -- | -- | SHADOW_BET | +9.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiri Lehecka (`KXATPMATCH-26OCT01HUMLEH-LEH`) | 0.63 / 0.64 (19660) | 63.5% | -- | 54.7% | 54.2% [52.8%-56.6%] | -- | -- | -- | -- | PASS | -9.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5799.0, B 5765.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0192
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.014, surface_dev_loose -0.004, surface_dev_tight -0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01HUMLEH-24` Over 23.5 games: 0.43/0.44 mid 43.5%, model 58.0% (market_conditioned_v1 (model4_board_v1)) -- gap +14.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01HUMLEH-LEH6` Will Jiri Lehecka win at least 5.5 more games than Ugo Humbert?: 0.11/0.31 mid 21.0%, model 6.7% (market_conditioned_v1 (model4_board_v1)) -- gap -14.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01HUMLEH-29` Over 28.5 games: 0.28/0.31 mid 29.5%, model 41.9% (market_conditioned_v1 (model4_board_v1)) -- gap +12.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01HUMLEH-19` Over 18.5 games: 0.82/0.87 mid 84.5%, model 94.3% (market_conditioned_v1 (model4_board_v1)) -- gap +9.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01HUMLEH-LEH3` Will Jiri Lehecka win at least 2.5 more games than Ugo Humbert?: 0.49/0.51 mid 50.0%, model 43.5% (market_conditioned_v1 (model4_board_v1)) -- gap -6.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01HUMLEH-LEH21` Will Jiri Lehecka win the Ugo Humbert vs Jiri Lehecka match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 28.5% (market_conditioned_v1 (model4_board_v1)) -- gap +5.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01HUMLEH-LEH20` Will Jiri Lehecka win the Ugo Humbert vs Jiri Lehecka match by a set score of 2-0?: 0.35/0.42 mid 38.5%, model 34.8% (market_conditioned_v1 (model4_board_v1)) -- gap -3.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01HUMLEH-HUM21` Will Ugo Humbert win the Ugo Humbert vs Jiri Lehecka match by a set score of 2-1?: 0.15/0.19 mid 17.0%, model 19.8% (market_conditioned_v1 (model4_board_v1)) -- gap +2.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01HUMLEH-HUM20` Will Ugo Humbert win the Ugo Humbert vs Jiri Lehecka match by a set score of 2-0?: 0.18/0.21 mid 19.5%, model 16.8% (market_conditioned_v1 (model4_board_v1)) -- gap -2.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01HUMLEH-HUM2` Will Ugo Humbert win at least 1.5 more games than Jiri Lehecka?: 0.29/0.33 mid 31.0%, model 28.4% (market_conditioned_v1 (model4_board_v1)) -- gap -2.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kyrian Jacquet vs Luciano Darderi -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208021:209260:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciano Darderi (`KXATPMATCH-26OCT01JACDAR-DAR`) | 0.56 / 0.57 (47644) | 56.5% | -- | 39.2% | 41.6% [37.8%-49.5%] | 55.6% | 58.1% | 58.1% | MODEL_LONE_OUTLIER | PASS | -14.9 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Kyrian Jacquet (`KXATPMATCH-26OCT01JACDAR-JAC`) | 0.43 / 0.44 (14582) | 43.5% | -- | 60.8% | 58.4% [50.5%-62.2%] | 44.4% | 43.6% | 43.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +14.9 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4700.0, B 7374.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0584
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.029, surface_dev_loose +0.038, surface_dev_tight -0.039
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01JACDAR-24` Over 23.5 games: 0.44/0.45 mid 44.5%, model 54.8% (market_conditioned_v1 (model4_board_v1)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01JACDAR-29` Over 28.5 games: 0.25/0.30 mid 27.5%, model 36.6% (market_conditioned_v1 (model4_board_v1)) -- gap +9.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01JACDAR-19` Over 18.5 games: 0.81/0.85 mid 83.0%, model 88.8% (market_conditioned_v1 (model4_board_v1)) -- gap +5.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01JACDAR-DAR21` Will Luciano Darderi win the Kyrian Jacquet vs Luciano Darderi match by a set score of 2-1?: 0.22/0.23 mid 22.5%, model 27.0% (market_conditioned_v1 (model4_board_v1)) -- gap +4.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01JACDAR-JAC21` Will Kyrian Jacquet win the Kyrian Jacquet vs Luciano Darderi match by a set score of 2-1?: 0.18/0.19 mid 18.5%, model 22.7% (market_conditioned_v1 (model4_board_v1)) -- gap +4.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01JACDAR-DAR20` Will Luciano Darderi win the Kyrian Jacquet vs Luciano Darderi match by a set score of 2-0?: 0.33/0.34 mid 33.5%, model 29.5% (market_conditioned_v1 (model4_board_v1)) -- gap -4.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01JACDAR-JAC20` Will Kyrian Jacquet win the Kyrian Jacquet vs Luciano Darderi match by a set score of 2-0?: 0.24/0.25 mid 24.5%, model 20.9% (market_conditioned_v1 (model4_board_v1)) -- gap -3.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01JACDAR-DAR5` Will Luciano Darderi win at least 4.5 more games than Kyrian Jacquet?: 0.22/0.23 mid 22.5%, model 19.4% (market_conditioned_v1 (model4_board_v1)) -- gap -3.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01JACDAR-JAC2` Will Kyrian Jacquet win at least 1.5 more games than Luciano Darderi?: 0.37/0.39 mid 38.0%, model 36.1% (market_conditioned_v1 (model4_board_v1)) -- gap -1.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01JACDAR-DAR2` Will Luciano Darderi win at least 1.5 more games than Kyrian Jacquet?: 0.49/0.50 mid 49.5%, model 48.8% (market_conditioned_v1 (model4_board_v1)) -- gap -0.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Denis Shapovalov vs Alejandro Tabilo -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126214:133430:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Denis Shapovalov (`KXATPMATCH-26OCT01SHATAB-SHA`) | 0.57 / 0.59 (24628) | 58.0% | -- | 48.5% | 52.0% [49.5%-53.4%] | -- | -- | -- | -- | PASS | -6.0 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Tabilo (`KXATPMATCH-26OCT01SHATAB-TAB`) | 0.42 / 0.43 (18757) | 42.5% | -- | 51.5% | 48.0% [46.6%-50.5%] | -- | -- | -- | -- | SHADOW_BET | +5.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4723.0, B 7913.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0196
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.015
* Derivatives listed: 6 (GAME_SPREAD, MATCH_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXATPGTOTAL-26OCT01SHATAB-24` Over 23.5 games: 0.44/0.45 mid 44.5%, model 55.4% (market_conditioned_v1 (model4_board_v1)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01SHATAB-29` Over 28.5 games: 0.27/0.30 mid 28.5%, model 37.9% (market_conditioned_v1 (model4_board_v1)) -- gap +9.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01SHATAB-19` Over 18.5 games: 0.81/0.84 mid 82.5%, model 90.1% (market_conditioned_v1 (model4_board_v1)) -- gap +7.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01SHATAB-SHA6` Will Denis Shapovalov win at least 5.5 more games than Alejandro Tabilo?: 0.01/0.32 mid 16.5%, model 9.6% (market_conditioned_v1 (model4_board_v1)) -- gap -6.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01SHATAB-SHA3` Will Denis Shapovalov win at least 2.5 more games than Alejandro Tabilo?: 0.45/0.46 mid 45.5%, model 41.9% (market_conditioned_v1 (model4_board_v1)) -- gap -3.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01SHATAB-TAB2` Will Alejandro Tabilo win at least 1.5 more games than Denis Shapovalov?: 0.35/0.38 mid 36.5%, model 34.6% (market_conditioned_v1 (model4_board_v1)) -- gap -1.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Valentin Vacherot vs Stefanos Tsitsipas -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126774:200473:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefanos Tsitsipas (`KXATPMATCH-26OCT01VACTSI-TSI`) | 0.06 / 0.07 (51823) | 6.5% | -- | 48.1% | 49.1% [47.2%-56.1%] | -- | -- | -- | -- | WATCH | +42.6 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentin Vacherot (`KXATPMATCH-26OCT01VACTSI-VAC`) | 0.93 / 0.94 (133021) | 93.5% | -- | 51.9% | 50.9% [43.9%-52.8%] | -- | -- | -- | -- | PASS | -42.6 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5393.0, B 5388.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0446
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26OCT01VACTSI-TSI  (YES = Stefanos Tsitsipas)
Model: 49%
Kalshi: 6%
Gap: +43 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.019, surface_dev_loose +0.009, surface_dev_tight -0.019
* Derivatives listed: 12 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGSPREAD-26OCT01VACTSI-VAC2` Will Valentin Vacherot win at least 1.5 more games than Stefanos Tsitsipas?: 0.09/0.24 mid 16.5%, model 89.3% (market_conditioned_v1 (model4_board_v1)) -- gap +72.8 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01VACTSI-VAC21` Will Valentin Vacherot win the Valentin Vacherot vs Stefanos Tsitsipas match by a set score of 2-1?: 0.93/0.94 mid 93.5%, model 22.7% (market_conditioned_v1 (model4_board_v1)) -- gap -70.8 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01VACTSI-TSI3` Will Stefanos Tsitsipas win at least 2.5 more games than Valentin Vacherot?: 0.05/0.07 mid 6.0%, model 2.8% (market_conditioned_v1 (model4_board_v1)) -- gap -3.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01VACTSI-TSI21` Will Stefanos Tsitsipas win the Valentin Vacherot vs Stefanos Tsitsipas match by a set score of 2-1?: 0.05/0.07 mid 6.0%, model 4.3% (market_conditioned_v1 (model4_board_v1)) -- gap -1.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alex de Minaur vs Quentin Halys -- ATP Beijing R16

ATP (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111460:200282:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex de Minaur (`KXATPMATCH-26OCT01DEHAL-DE`) | 0.72 / 0.73 (43752) | 72.5% | -- | 79.4% | 78.7% [77.7%-79.4%] | -- | -- | -- | -- | SHADOW_BET | +6.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Quentin Halys (`KXATPMATCH-26OCT01DEHAL-HAL`) | 0.27 / 0.28 (14915) | 27.5% | -- | 20.6% | 21.3% [20.6%-22.3%] | -- | -- | -- | -- | PASS | -6.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 7096.0, B 7371.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0086
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.000, surface_dev_loose +0.003, surface_dev_tight +0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01DEHAL-22` Over 21.5 games: 0.54/0.56 mid 55.0%, model 67.2% (market_conditioned_v1 (model4_board_v1)) -- gap +12.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01DEHAL-27` Over 26.5 games: 0.27/0.35 mid 31.0%, model 41.4% (market_conditioned_v1 (model4_board_v1)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01DEHAL-DE21` Will Alex de Minaur win the Alex de Minaur vs Quentin Halys match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 29.6% (market_conditioned_v1 (model4_board_v1)) -- gap +7.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01DEHAL-DE20` Will Alex de Minaur win the Alex de Minaur vs Quentin Halys match by a set score of 2-0?: 0.48/0.50 mid 49.0%, model 42.7% (market_conditioned_v1 (model4_board_v1)) -- gap -6.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01DEHAL-DE5` Will Alex de Minaur win at least 4.5 more games than Quentin Halys?: 0.33/0.34 mid 33.5%, model 28.2% (market_conditioned_v1 (model4_board_v1)) -- gap -5.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01DEHAL-DE8` Will Alex de Minaur win at least 7.5 more games than Quentin Halys?: 0.05/0.11 mid 8.0%, model 2.8% (market_conditioned_v1 (model4_board_v1)) -- gap -5.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01DEHAL-17` Over 16.5 games: 0.91/0.97 mid 94.0%, model 97.4% (market_conditioned_v1 (model4_board_v1)) -- gap +3.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01DEHAL-HAL21` Will Quentin Halys win the Alex de Minaur vs Quentin Halys match by a set score of 2-1?: 0.13/0.15 mid 14.0%, model 15.7% (market_conditioned_v1 (model4_board_v1)) -- gap +1.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01DEHAL-DE2` Will Alex de Minaur win at least 1.5 more games than Quentin Halys?: 0.62/0.71 mid 66.5%, model 65.3% (market_conditioned_v1 (model4_board_v1)) -- gap -1.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01DEHAL-HAL20` Will Quentin Halys win the Alex de Minaur vs Quentin Halys match by a set score of 2-0?: 0.11/0.15 mid 13.0%, model 12.0% (market_conditioned_v1 (model4_board_v1)) -- gap -1.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Alex Molcan vs Karen Khachanov -- ATP Beijing R16

ATP (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111575:144684:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karen Khachanov (`KXATPMATCH-26OCT01MOLKHA-KHA`) | 0.78 / 0.79 (19750) | 78.5% | -- | 70.7% | 71.2% [66.9%-72.3%] | 77.5% | 78.1% | 78.1% | MODEL_LONE_OUTLIER | PASS | -7.3 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Alex Molcan (`KXATPMATCH-26OCT01MOLKHA-MOL`) | 0.21 / 0.22 (26062) | 21.5% | -- | 29.3% | 28.8% [27.7%-33.1%] | 22.5% | 22.5% | 22.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.3 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3805.0, B 5981.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0271
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.008, surface_dev_loose -0.012, surface_dev_tight +0.016
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT01MOLKHA-22` Over 21.5 games: 0.70/0.72 mid 71.0%, model 61.8% (market_conditioned_v1 (model4_board_v1)) -- gap -9.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01MOLKHA-KHA8` Will Karen Khachanov win at least 7.5 more games than Alex Molcan?: 0.06/0.21 mid 13.5%, model 4.5% (market_conditioned_v1 (model4_board_v1)) -- gap -8.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01MOLKHA-KHA5` Will Karen Khachanov win at least 4.5 more games than Alex Molcan?: 0.29/0.35 mid 32.0%, model 35.9% (market_conditioned_v1 (model4_board_v1)) -- gap +3.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01MOLKHA-17` Over 16.5 games: 0.90/0.96 mid 93.0%, model 95.8% (market_conditioned_v1 (model4_board_v1)) -- gap +2.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MOLKHA-MOL21` Will Alex Molcan win the Alex Molcan vs Karen Khachanov match by a set score of 2-1?: 0.09/0.13 mid 11.0%, model 12.7% (market_conditioned_v1 (model4_board_v1)) -- gap +1.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MOLKHA-MOL20` Will Alex Molcan win the Alex Molcan vs Karen Khachanov match by a set score of 2-0?: 0.08/0.13 mid 10.5%, model 9.1% (market_conditioned_v1 (model4_board_v1)) -- gap -1.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MOLKHA-KHA21` Will Karen Khachanov win the Alex Molcan vs Karen Khachanov match by a set score of 2-1?: 0.27/0.30 mid 28.5%, model 29.4% (market_conditioned_v1 (model4_board_v1)) -- gap +0.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01MOLKHA-KHA2` Will Karen Khachanov win at least 1.5 more games than Alex Molcan?: 0.70/0.76 mid 73.0%, model 72.2% (market_conditioned_v1 (model4_board_v1)) -- gap -0.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01MOLKHA-KHA20` Will Karen Khachanov win the Alex Molcan vs Karen Khachanov match by a set score of 2-0?: 0.46/0.52 mid 49.0%, model 48.8% (market_conditioned_v1 (model4_board_v1)) -- gap -0.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01MOLKHA-27` Over 26.5 games: 0.34/0.41 mid 37.5%, model 37.5% (market_conditioned_v1 (model4_board_v1)) -- gap -0.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yunchaokete Bu vs Novak Djokovic -- ATP Beijing R16

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT01YUNDJO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Novak Djokovic (`KXATPMATCH-26OCT01YUNDJO-DJO`) | 0.76 / 0.77 (23146) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yunchaokete Bu (`KXATPMATCH-26OCT01YUNDJO-YUN`) | 0.24 / 0.25 (65999) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexander Zverev vs Juncheng Shang -- ATP Beijing R16

ATP (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:100644:209992:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juncheng Shang (`KXATPMATCH-26OCT01ZVESHA-SHA`) | 0.07 / 0.08 (10442) | 7.5% | -- | 11.4% | 12.8% [11.1%-14.7%] | -- | -- | -- | -- | SHADOW_BET | +5.3 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Zverev (`KXATPMATCH-26OCT01ZVESHA-ZVE`) | 0.92 / 0.93 (36792) | 92.5% | -- | 88.6% | 87.2% [85.3%-88.9%] | -- | -- | -- | -- | PASS | -5.3 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 8165.0, B 3774.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0182
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.018, surface_dev_loose -0.001, surface_dev_tight +0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGSPREAD-26OCT01ZVESHA-ZVE9` Will Alexander Zverev win at least 8.5 more games than Juncheng Shang?: 0.02/0.26 mid 14.0%, model 2.3% (market_conditioned_v1 (model4_board_v1)) -- gap -11.7 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01ZVESHA-15` Over 14.5 games: 0.78/0.99 mid 88.5%, model 99.5% (market_conditioned_v1 (model4_board_v1)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01ZVESHA-ZVE6` Will Alexander Zverev win at least 5.5 more games than Juncheng Shang?: 0.38/0.39 mid 38.5%, model 28.4% (market_conditioned_v1 (model4_board_v1)) -- gap -10.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01ZVESHA-20` Over 19.5 games: 0.58/0.59 mid 58.5%, model 68.3% (market_conditioned_v1 (model4_board_v1)) -- gap +9.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT01ZVESHA-25` Over 24.5 games: 0.22/0.30 mid 26.0%, model 33.5% (market_conditioned_v1 (model4_board_v1)) -- gap +7.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01ZVESHA-ZVE21` Will Alexander Zverev win the Alexander Zverev vs Juncheng Shang match by a set score of 2-1?: 0.17/0.20 mid 18.5%, model 23.6% (market_conditioned_v1 (model4_board_v1)) -- gap +5.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01ZVESHA-SHA20` Will Juncheng Shang win the Alexander Zverev vs Juncheng Shang match by a set score of 2-0?: 0.02/0.05 mid 3.5%, model 3.0% (market_conditioned_v1 (model4_board_v1)) -- gap -0.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT01ZVESHA-ZVE3` Will Alexander Zverev win at least 2.5 more games than Juncheng Shang?: 0.77/0.85 mid 81.0%, model 81.2% (market_conditioned_v1 (model4_board_v1)) -- gap +0.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01ZVESHA-SHA21` Will Juncheng Shang win the Alexander Zverev vs Juncheng Shang match by a set score of 2-1?: 0.04/0.06 mid 5.0%, model 4.9% (market_conditioned_v1 (model4_board_v1)) -- gap -0.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT01ZVESHA-ZVE20` Will Alexander Zverev win the Alexander Zverev vs Juncheng Shang match by a set score of 2-0?: 0.68/0.69 mid 68.5%, model 68.4% (market_conditioned_v1 (model4_board_v1)) -- gap -0.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ekaterina Alexandrova vs Aliaksandra Sasnovich -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:205925:206420:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Alexandrova (`KXWTAMATCH-26OCT01ALESAS-ALE`) | 0.58 / 0.59 (9520) | 58.5% | -- | 60.4% | 61.4% [59.9%-64.9%] | 58.3% | 58.7% | 58.5% | MODEL_LONE_OUTLIER | WATCH | +2.9 pp | NORMAL | STALE | A / LIMITED | ALL_AGREE | VERIFIED |
| Aliaksandra Sasnovich (`KXWTAMATCH-26OCT01ALESAS-SAS`) | 0.40 / 0.42 (44396) | 41.0% | -- | 39.6% | 38.6% [35.1%-40.1%] | 41.7% | 41.3% | 41.5% | MODEL_LONE_OUTLIER | PASS | -2.4 pp | NORMAL | STALE | A / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4877.0, B 4822.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0251
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.015, surface_dev_loose -0.010, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01ALESAS-23` Over 22.5 games: 0.43/0.46 mid 44.5%, model 55.9% (market_conditioned_v1 (model4_board_v1)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01ALESAS-28` Over 27.5 games: 0.20/0.26 mid 23.0%, model 34.4% (market_conditioned_v1 (model4_board_v1)) -- gap +11.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01ALESAS-18` Over 17.5 games: 0.72/0.87 mid 79.5%, model 87.9% (market_conditioned_v1 (model4_board_v1)) -- gap +8.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
* Warnings: SCHEDULED_START_PASSED; STALE_QUOTE; WIDE_SPREAD

## Nikola Bartunkova vs Magdalena Frech -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211684:223360:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikola Bartunkova (`KXWTAMATCH-26OCT01BARFRE-BAR`) | 0.58 / 0.59 (22044) | 58.5% | -- | 57.8% | 56.3% [50.5%-58.9%] | 58.3% | 59.0% | 58.7% | MODEL_LONE_OUTLIER | PASS | -2.2 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Magdalena Frech (`KXWTAMATCH-26OCT01BARFRE-FRE`) | 0.41 / 0.42 (3463) | 41.5% | -- | 42.2% | 43.7% [41.1%-49.5%] | 41.7% | 41.0% | 41.4% | MODEL_LONE_OUTLIER | PASS | +2.2 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3248.0, B 4552.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0416
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.021, surface_dev_loose +0.005, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01BARFRE-27` Over 26.5 games: 0.26/0.32 mid 29.0%, model 39.6% (market_conditioned_v1 (model4_board_v1)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01BARFRE-22` Over 21.5 games: 0.53/0.54 mid 53.5%, model 62.8% (market_conditioned_v1 (model4_board_v1)) -- gap +9.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01BARFRE-17` Over 16.5 games: 0.87/0.90 mid 88.5%, model 93.9% (market_conditioned_v1 (model4_board_v1)) -- gap +5.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; STALE_QUOTE; THIN_DISPLAYED_SIZE

## Sara Bejlek vs Maddison Inglis -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213666:239383:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Bejlek (`KXWTAMATCH-26OCT01BEJING-BEJ`) | 0.74 / 0.75 (44757) | 74.5% | -- | 76.3% | 73.8% [69.7%-74.6%] | 73.4% | 73.3% | 73.3% | MARKETS_AGREE | PASS | -0.7 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Maddison Inglis (`KXWTAMATCH-26OCT01BEJING-ING`) | 0.25 / 0.26 (5791) | 25.5% | -- | 23.7% | 26.2% [25.4%-30.3%] | 26.7% | 26.3% | 26.3% | MARKETS_AGREE | PASS | +0.7 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3433.0, B 3027.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0244
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.018, surface_dev_loose +0.009, surface_dev_tight -0.009
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01BEJING-21` Over 20.5 games: 0.47/0.49 mid 48.0%, model 61.5% (market_conditioned_v1 (model4_board_v1)) -- gap +13.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01BEJING-26` Over 25.5 games: 0.23/0.29 mid 26.0%, model 38.9% (market_conditioned_v1 (model4_board_v1)) -- gap +12.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01BEJING-16` Over 15.5 games: 0.88/0.96 mid 92.0%, model 95.5% (market_conditioned_v1 (model4_board_v1)) -- gap +3.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
* Warnings: SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Belinda Bencic vs Anastasia Zakharova -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202505:220435:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Belinda Bencic (`KXWTAMATCH-26OCT01BENZAK-BEN`) | 0.79 / 0.80 (3613) | 79.5% | -- | 77.8% | 79.3% [77.0%-82.6%] | -- | -- | -- | -- | PASS | -0.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Zakharova (`KXWTAMATCH-26OCT01BENZAK-ZAK`) | 0.20 / 0.21 (7792) | 20.5% | -- | 22.2% | 20.7% [17.4%-23.0%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3571.0, B 4628.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0279
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.023, surface_dev_loose +0.004, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01BENZAK-21` Over 20.5 games: 0.44/0.46 mid 45.0%, model 58.7% (market_conditioned_v1 (model4_board_v1)) -- gap +13.7 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01BENZAK-26` Over 25.5 games: 0.21/0.31 mid 26.0%, model 36.4% (market_conditioned_v1 (model4_board_v1)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01BENZAK-16` Over 15.5 games: 0.81/0.93 mid 87.0%, model 94.9% (market_conditioned_v1 (model4_board_v1)) -- gap +7.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Marie Bouzkova vs Kimberly Birrell -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213631:214040:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kimberly Birrell (`KXWTAMATCH-26OCT01BOUBIR-BIR`) | 0.32 / 0.33 (1289) | 32.5% | -- | 45.8% | 43.6% [39.5%-45.8%] | -- | -- | -- | -- | SHADOW_BET | +11.2 pp | REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marie Bouzkova (`KXWTAMATCH-26OCT01BOUBIR-BOU`) | 0.67 / 0.68 (19711) | 67.5% | -- | 54.2% | 56.4% [54.2%-60.5%] | -- | -- | -- | -- | PASS | -11.2 pp | REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4089.0, B 5020.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0313
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.021, surface_dev_loose -0.011, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01BOUBIR-22` Over 21.5 games: 0.47/0.48 mid 47.5%, model 59.2% (market_conditioned_v1 (model4_board_v1)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01BOUBIR-27` Over 26.5 games: 0.22/0.31 mid 26.5%, model 36.4% (market_conditioned_v1 (model4_board_v1)) -- gap +9.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01BOUBIR-17` Over 16.5 games: 0.80/0.92 mid 86.0%, model 91.7% (market_conditioned_v1 (model4_board_v1)) -- gap +5.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Linda Fruhvirtova vs Liudmila Samsonova -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214643:222258:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linda Fruhvirtova (`KXWTAMATCH-26OCT01FRUSAM-FRU`) | 0.31 / 0.34 (76) | 32.5% | -- | 43.7% | 39.6% [28.0%-43.7%] | -- | -- | -- | -- | WATCH | +7.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Liudmila Samsonova (`KXWTAMATCH-26OCT01FRUSAM-SAM`) | 0.66 / 0.71 (141) | 68.5% | -- | 56.3% | 60.4% [56.3%-72.0%] | -- | -- | -- | -- | PASS | -8.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4353.0, B 3968.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0785
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.040, surface_pool_high +0.041, surface_dev_loose +0.021, surface_dev_tight -0.020
* Derivatives listed: 3 (MATCH_WINNER, TOTAL_GAMES); 3 carry a model probability
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

## Viktorija Golubic vs Peyton Stearns -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:203530:220548:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viktorija Golubic (`KXWTAMATCH-26OCT01GOLSTE-GOL`) | 0.76 / 0.78 (12) | 77.0% | -- | 45.8% | 47.4% [46.8%-48.4%] | -- | -- | -- | -- | PASS | -29.6 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Peyton Stearns (`KXWTAMATCH-26OCT01GOLSTE-STE`) | 0.22 / 0.25 (64) | 23.5% | -- | 54.2% | 52.6% [51.6%-53.2%] | -- | -- | -- | -- | WATCH | +29.1 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4714.0, B 4027.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0079
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01GOLSTE-STE  (YES = Peyton Stearns)
Model: 53%
Kalshi: 24%
Gap: +29 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, NO_EXTERNAL_REFERENCE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight -0.000
* Derivatives listed: 3 (MATCH_WINNER, TOTAL_GAMES); 3 carry a model probability
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

## Sonay Kartal vs Xinyu Wang -- WTA Beijing R64

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT01KARWAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sonay Kartal (`KXWTAMATCH-26OCT01KARWAN-KAR`) | 0.51 / 0.52 (150) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xinyu Wang (`KXWTAMATCH-26OCT01KARWAN-WAN`) | 0.49 / 0.50 (24463) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ashlyn Krueger vs Ann Li -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215983:221909:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ann Li (`KXWTAMATCH-26OCT01KRUANN-ANN`) | 0.56 / 0.57 (20709) | 56.5% | -- | 63.7% | 59.7% [55.7%-61.7%] | -- | -- | -- | -- | WATCH | +3.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ashlyn Krueger (`KXWTAMATCH-26OCT01KRUANN-KRU`) | 0.43 / 0.44 (1693) | 43.5% | -- | 36.3% | 40.3% [38.3%-44.3%] | -- | -- | -- | -- | PASS | -3.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4211.0, B 4567.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0301
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01KRUANN-28` Over 27.5 games: 0.22/0.28 mid 25.0%, model 36.6% (market_conditioned_v1 (model4_board_v1)) -- gap +11.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01KRUANN-23` Over 22.5 games: 0.45/0.47 mid 46.0%, model 57.6% (market_conditioned_v1 (model4_board_v1)) -- gap +11.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01KRUANN-18` Over 17.5 games: 0.75/0.87 mid 81.0%, model 90.0% (market_conditioned_v1 (model4_board_v1)) -- gap +9.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Karolina Muchova vs Katie Boulter -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211107:214096:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katie Boulter (`KXWTAMATCH-26OCT01MUCBOU-BOU`) | 0.15 / 0.16 (7512) | 15.5% | -- | 24.1% | 22.9% [22.1%-23.7%] | 17.3% | 15.6% | 15.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +7.4 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Karolina Muchova (`KXWTAMATCH-26OCT01MUCBOU-MUC`) | 0.84 / 0.85 (45963) | 84.5% | -- | 75.9% | 77.1% [76.3%-77.9%] | 82.7% | 84.4% | 84.4% | MODEL_LONE_OUTLIER | PASS | -7.4 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3972.0, B 3928.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0078
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high +0.000, surface_dev_loose +0.008, surface_dev_tight -0.008
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT01MUCBOU-19` Over 18.5 games: 0.53/0.54 mid 53.5%, model 71.8% (market_conditioned_v1 (model4_board_v1)) -- gap +18.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01MUCBOU-24` Over 23.5 games: 0.22/0.27 mid 24.5%, model 39.6% (market_conditioned_v1 (model4_board_v1)) -- gap +15.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data LIMITED
* Warnings: SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Mio Mushika vs Yuno Kitahara -- W35 Wagga Wagga QF

ITF (ITF) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222986:263881:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuno Kitahara (`KXITFWMATCH-26OCT01MUSKIT-KIT`) | 0.33 / 0.34 (5290) | 33.5% | -- | 33.9% | 35.4% [34.4%-37.4%] | -- | -- | -- | -- | PASS | +1.9 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mio Mushika (`KXITFWMATCH-26OCT01MUSKIT-MUS`) | 0.66 / 0.67 (2668) | 66.5% | -- | 66.1% | 64.6% [62.6%-65.6%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2224.0, B 2068.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.015
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Linda Noskova vs Elena-Gabriela Ruse -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211817:222328:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Linda Noskova (`KXWTAMATCH-26OCT01NOSRUS-NOS`) | 0.87 / 0.88 (15210) | 87.5% | -- | 64.5% | 67.8% [66.9%-70.5%] | 74.5% | 78.2% | 76.3% | MODEL_LONE_OUTLIER | PASS | -19.7 pp | HIGH_REVIEW | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Elena-Gabriela Ruse (`KXWTAMATCH-26OCT01NOSRUS-RUS`) | 0.12 / 0.13 (5927) | 12.5% | -- | 35.5% | 32.2% [29.5%-33.1%] | 25.5% | 22.0% | 23.8% | MODEL_LONE_OUTLIER | WATCH | +19.7 pp | HIGH_REVIEW | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 4568.0, B 4254.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0182
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01NOSRUS-RUS  (YES = Elena-Gabriela Ruse)
Model: 32%
Kalshi: 12%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, EXTERNAL_MARKET_CONFIRMATION, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.018, surface_dev_loose +0.009, surface_dev_tight -0.004
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01NOSRUS-21` Over 20.5 games: 0.29/0.40 mid 34.5%, model 54.2% (market_conditioned_v1 (model4_board_v1)) -- gap +19.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01NOSRUS-16` Over 15.5 games: 0.76/0.79 mid 77.5%, model 94.8% (market_conditioned_v1 (model4_board_v1)) -- gap +17.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01NOSRUS-26` Over 25.5 games: 0.16/0.26 mid 21.0%, model 31.9% (market_conditioned_v1 (model4_board_v1)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; STALE_QUOTE; WIDE_SPREAD

## Kyoka Okamura vs Emerson Jones -- WTA 125K Jingshan QF

WTA125 (WTA_125) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211846:263644:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emerson Jones (`KXWTACHALLENGERMATCH-26OCT01OKAJON-JON`) | 0.85 / 0.86 (23704) | 85.5% | -- | 80.4% | 77.7% [73.3%-80.0%] | -- | -- | -- | -- | PASS | -7.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kyoka Okamura (`KXWTACHALLENGERMATCH-26OCT01OKAJON-OKA`) | 0.14 / 0.15 (17024) | 14.5% | -- | 19.6% | 22.3% [20.0%-26.7%] | -- | -- | -- | -- | PASS | +7.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2971.0, B 3547.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0335
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE

## Jelena Ostapenko vs Paula Badosa -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211533:211651:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Paula Badosa (`KXWTAMATCH-26OCT01OSTBAD-BAD`) | 0.63 / 0.64 (7743) | 63.5% | -- | 63.5% | 62.0% [57.9%-63.0%] | -- | -- | -- | -- | PASS | -1.5 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jelena Ostapenko (`KXWTAMATCH-26OCT01OSTBAD-OST`) | 0.36 / 0.37 (5100) | 36.5% | -- | 36.5% | 38.0% [37.0%-42.1%] | -- | -- | -- | -- | PASS | +1.5 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3919.0, B 3479.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0255
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01OSTBAD-18` Over 17.5 games: 0.71/0.80 mid 75.5%, model 86.8% (market_conditioned_v1 (model4_board_v1)) -- gap +11.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01OSTBAD-23` Over 22.5 games: 0.43/0.45 mid 44.0%, model 54.5% (market_conditioned_v1 (model4_board_v1)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01OSTBAD-28` Over 27.5 games: 0.21/0.29 mid 25.0%, model 33.1% (market_conditioned_v1 (model4_board_v1)) -- gap +8.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jasmine Paolini vs Daria Snigur -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211148:220750:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jasmine Paolini (`KXWTAMATCH-26OCT01PAOSNI-PAO`) | 0.53 / 0.54 (32661) | 53.5% | -- | 23.2% | 33.5% [27.4%-53.7%] | 55.6% | 55.6% | 55.6% | MODEL_LONE_OUTLIER | PASS | -20.0 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Daria Snigur (`KXWTAMATCH-26OCT01PAOSNI-SNI`) | 0.46 / 0.47 (9068) | 46.5% | -- | 76.8% | 66.5% [46.3%-72.6%] | 44.4% | 44.7% | 44.5% | MODEL_LONE_OUTLIER | WATCH | +20.0 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4852.0, B 4190.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1314
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01PAOSNI-SNI  (YES = Daria Snigur)
Model: 67%
Kalshi: 46%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.019, surface_dev_loose -0.024, surface_dev_tight +0.029
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01PAOSNI-22` Over 21.5 games: 0.46/0.50 mid 48.0%, model 62.2% (market_conditioned_v1 (model4_board_v1)) -- gap +14.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01PAOSNI-27` Over 26.5 games: 0.23/0.30 mid 26.5%, model 38.8% (market_conditioned_v1 (model4_board_v1)) -- gap +12.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01PAOSNI-17` Over 16.5 games: 0.81/0.92 mid 86.5%, model 93.1% (market_conditioned_v1 (model4_board_v1)) -- gap +6.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Taylah Preston vs Diane Parry -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220348:223194:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diane Parry (`KXWTAMATCH-26OCT01PREPAR-PAR`) | 0.55 / 0.56 (39031) | 55.5% | -- | 19.4% | 24.8% [19.7%-43.7%] | 56.6% | 56.9% | 56.7% | MODEL_LONE_OUTLIER | PASS | -30.7 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Taylah Preston (`KXWTAMATCH-26OCT01PREPAR-PRE`) | 0.44 / 0.45 (14302) | 44.5% | -- | 80.7% | 75.2% [56.3%-80.3%] | 43.4% | 43.1% | 43.3% | MODEL_LONE_OUTLIER | WATCH | +30.7 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5098.0, B 3742.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1199
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01PREPAR-PRE  (YES = Taylah Preston)
Model: 75%
Kalshi: 44%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.043, surface_pool_high +0.040, surface_dev_loose +0.012, surface_dev_tight -0.012
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01PREPAR-23` Over 22.5 games: 0.39/0.55 mid 47.0%, model 56.8% (market_conditioned_v1 (model4_board_v1)) -- gap +9.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01PREPAR-18` Over 17.5 games: 0.72/0.89 mid 80.5%, model 88.9% (market_conditioned_v1 (model4_board_v1)) -- gap +8.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01PREPAR-28` Over 27.5 games: 0.20/0.36 mid 28.0%, model 35.4% (market_conditioned_v1 (model4_board_v1)) -- gap +7.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; STALE_QUOTE; WIDE_SPREAD

## Kamilla Rakhimova vs Leylah Fernandez -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215872:220367:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leylah Fernandez (`KXWTAMATCH-26OCT01RAKFER-FER`) | 0.74 / 0.75 (100) | 74.5% | -- | 66.3% | 67.7% [65.8%-68.7%] | -- | -- | -- | -- | PASS | -6.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kamilla Rakhimova (`KXWTAMATCH-26OCT01RAKFER-RAK`) | 0.25 / 0.26 (18834) | 25.5% | -- | 33.7% | 32.3% [31.4%-34.2%] | -- | -- | -- | -- | SHADOW_BET | +6.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5718.0, B 4828.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0142
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01RAKFER-21` Over 20.5 games: 0.49/0.51 mid 50.0%, model 62.5% (market_conditioned_v1 (model4_board_v1)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01RAKFER-26` Over 25.5 games: 0.26/0.34 mid 30.0%, model 39.7% (market_conditioned_v1 (model4_board_v1)) -- gap +9.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01RAKFER-16` Over 15.5 games: 0.84/0.96 mid 90.0%, model 96.1% (market_conditioned_v1 (model4_board_v1)) -- gap +6.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Elena Rybakina vs Alina Charaeva -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214981:221406:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Charaeva (`KXWTAMATCH-26OCT01RYBCHA-CHA`) | 0.04 / 0.05 (2763) | 4.5% | -- | 5.3% | 5.2% [4.9%-5.9%] | -- | -- | -- | -- | PASS | +0.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Rybakina (`KXWTAMATCH-26OCT01RYBCHA-RYB`) | 0.95 / 0.96 (19366) | 95.5% | -- | 94.7% | 94.8% [94.1%-95.1%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6087.0, B 3668.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0048
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.003, surface_dev_loose -0.001, surface_dev_tight -0.003
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT01RYBCHA-18` Over 17.5 games: 0.52/0.54 mid 53.0%, model 71.3% (market_conditioned_v1 (model4_board_v1)) -- gap +18.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01RYBCHA-23` Over 22.5 games: 0.17/0.27 mid 22.0%, model 28.9% (market_conditioned_v1 (model4_board_v1)) -- gap +6.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maria Sakkari vs Storm Hunter -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:204411:206289:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Storm Hunter (`KXWTAMATCH-26OCT01SAKHUN-HUN`) | 0.28 / 0.29 (471) | 28.5% | -- | 27.6% | 30.3% [28.0%-32.2%] | -- | -- | -- | -- | PASS | +1.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Sakkari (`KXWTAMATCH-26OCT01SAKHUN-SAK`) | 0.71 / 0.72 (29651) | 71.5% | -- | 72.4% | 69.7% [67.8%-72.0%] | -- | -- | -- | -- | PASS | -1.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3640.0, B 2089.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0207
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.019, surface_dev_loose -0.005, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01SAKHUN-22` Over 21.5 games: 0.46/0.48 mid 47.0%, model 58.2% (market_conditioned_v1 (model4_board_v1)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01SAKHUN-27` Over 26.5 games: 0.19/0.32 mid 25.5%, model 35.7% (market_conditioned_v1 (model4_board_v1)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01SAKHUN-17` Over 16.5 games: 0.79/0.93 mid 86.0%, model 91.6% (market_conditioned_v1 (model4_board_v1)) -- gap +5.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Naho Sato vs Hikaru Sato -- W35 Wagga Wagga QF

ITF (ITF) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220997:221141:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naho Sato (`KXITFWMATCH-26OCT01SATSAT2-SAT`) | 0.67 / 0.68 (94) | 67.5% | -- | 46.8% | 48.9% [47.9%-50.5%] | 53.8% | -- | 53.8% | MODEL_LONE_OUTLIER | PASS | -18.6 pp | HIGH_REVIEW | STALE | B / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Hikaru Sato (`KXITFWMATCH-26OCT01SATSAT2-SAT2`) | 0.31 / 0.32 (3650) | 31.5% | -- | 53.2% | 51.1% [49.5%-52.1%] | 46.2% | -- | 46.2% | MODEL_LONE_OUTLIER | WATCH | +19.6 pp | HIGH_REVIEW | STALE | B / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 1522.0, B 1807.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0133
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01SATSAT2-SAT2  (YES = Hikaru Sato)
Model: 51%
Kalshi: 32%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_MODEL
Data quality: B (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kanon Sawashiro vs Nagi Hanatani -- W35 Wagga Wagga QF

ITF (ITF) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211544:263905:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nagi Hanatani (`KXITFWMATCH-26OCT01SAWHAN-HAN`) | 0.27 / 0.28 (16646) | 27.5% | -- | 19.5% | 36.4% [28.2%-47.3%] | 23.2% | -- | 23.2% | MODEL_LONE_OUTLIER | WATCH | +8.8 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Kanon Sawashiro (`KXITFWMATCH-26OCT01SAWHAN-SAW`) | 0.72 / 0.73 (6068) | 72.5% | -- | 80.5% | 63.6% [52.7%-71.8%] | 76.8% | -- | 76.8% | MODEL_LONE_OUTLIER | PASS | -8.8 pp | NORMAL | STALE | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 827.0, B 1219.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0958
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katerina Siniakova vs Elina Svitolina -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202494:211701:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katerina Siniakova (`KXWTAMATCH-26OCT01SINSVI-SIN`) | 0.23 / 0.24 (10002) | 23.5% | -- | 29.9% | 29.0% [27.2%-29.9%] | -- | -- | -- | -- | SHADOW_BET | +5.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elina Svitolina (`KXWTAMATCH-26OCT01SINSVI-SVI`) | 0.77 / 0.78 (32041) | 77.5% | -- | 70.1% | 71.0% [70.1%-72.8%] | -- | -- | -- | -- | PASS | -6.5 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4278.0, B 4144.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0137
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.009, surface_dev_tight +0.004
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01SINSVI-21` Over 20.5 games: 0.47/0.49 mid 48.0%, model 60.7% (market_conditioned_v1 (model4_board_v1)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01SINSVI-26` Over 25.5 games: 0.24/0.33 mid 28.5%, model 38.2% (market_conditioned_v1 (model4_board_v1)) -- gap +9.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01SINSVI-16` Over 15.5 games: 0.84/0.95 mid 89.5%, model 95.5% (market_conditioned_v1 (model4_board_v1)) -- gap +6.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Clara Tauson vs Polina Kudermetova -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220704:221236:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Kudermetova (`KXWTAMATCH-26OCT01TAUKUD-KUD`) | 0.37 / 0.38 (20766) | 37.5% | -- | 32.9% | 34.3% [32.4%-40.2%] | 38.4% | 37.2% | 37.8% | MARKETS_AGREE | PASS | -3.2 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Clara Tauson (`KXWTAMATCH-26OCT01TAUKUD-TAU`) | 0.62 / 0.63 (19739) | 62.5% | -- | 67.1% | 65.7% [59.8%-67.6%] | 61.6% | 62.7% | 62.2% | MARKETS_AGREE | WATCH | +3.2 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4452.0, B 4285.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0386
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.009, surface_dev_loose -0.000, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01TAUKUD-26` Over 25.5 games: 0.28/0.36 mid 32.0%, model 44.9% (market_conditioned_v1 (model4_board_v1)) -- gap +12.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TAUKUD-21` Over 20.5 games: 0.56/0.57 mid 56.5%, model 68.2% (market_conditioned_v1 (model4_board_v1)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TAUKUD-16` Over 15.5 games: 0.92/0.97 mid 94.5%, model 97.7% (market_conditioned_v1 (model4_board_v1)) -- gap +3.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; STALE_QUOTE; WIDE_SPREAD

## Maria Timofeeva vs Naomi Osaka -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211768:221237:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naomi Osaka (`KXWTAMATCH-26OCT01TIMOSA-OSA`) | 0.77 / 0.78 (8818) | 77.5% | -- | 76.0% | 80.3% [78.0%-81.7%] | 77.5% | 78.5% | 78.0% | MODEL_LONE_OUTLIER | WATCH | +2.8 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Maria Timofeeva (`KXWTAMATCH-26OCT01TIMOSA-TIM`) | 0.22 / 0.23 (49156) | 22.5% | -- | 24.0% | 19.7% [18.3%-22.0%] | 22.5% | 22.0% | 22.3% | MODEL_LONE_OUTLIER | PASS | -2.8 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3737.0, B 2986.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0182
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.004, surface_dev_loose -0.004, surface_dev_tight +0.004
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01TIMOSA-26` Over 25.5 games: 0.21/0.29 mid 25.0%, model 38.3% (market_conditioned_v1 (model4_board_v1)) -- gap +13.3 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TIMOSA-21` Over 20.5 games: 0.47/0.49 mid 48.0%, model 60.9% (market_conditioned_v1 (model4_board_v1)) -- gap +12.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01TIMOSA-16` Over 15.5 games: 0.89/0.96 mid 92.5%, model 95.8% (market_conditioned_v1 (model4_board_v1)) -- gap +3.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; STALE_QUOTE; WIDE_SPREAD

## Mutsumi Uemura vs Ashleigh Simes -- W35 Wagga Wagga QF

ITF (ITF) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221929:260828:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashleigh Simes (`KXITFWMATCH-26OCT01UEMSIM-SIM`) | 0.04 / 0.05 (14684) | 4.5% | -- | 74.3% | 70.7% [68.5%-74.2%] | -- | -- | -- | -- | PASS | +66.2 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mutsumi Uemura (`KXITFWMATCH-26OCT01UEMSIM-UEM`) | 0.95 / 0.96 (32963) | 95.5% | -- | 25.7% | 29.3% [25.8%-31.6%] | -- | -- | -- | -- | PASS | -66.2 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 824.0, B 942.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.029
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01UEMSIM-SIM  (YES = Ashleigh Simes)
Model: 71%
Kalshi: 4%
Gap: +66 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katie Volynets vs Elise Mertens -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:210722:220465:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elise Mertens (`KXWTAMATCH-26OCT01VOLMER-MER`) | 0.53 / 0.54 (7744) | 53.5% | -- | 76.4% | 73.0% [67.9%-75.1%] | -- | -- | -- | -- | WATCH | +19.5 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katie Volynets (`KXWTAMATCH-26OCT01VOLMER-VOL`) | 0.45 / 0.46 (1798) | 45.5% | -- | 23.6% | 27.0% [24.9%-32.1%] | -- | -- | -- | -- | PASS | -18.5 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5386.0, B 3838.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0359
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01VOLMER-MER  (YES = Elise Mertens)
Model: 73%
Kalshi: 54%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.009, surface_dev_loose -0.009, surface_dev_tight +0.009
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01VOLMER-23` Over 22.5 games: 0.44/0.46 mid 45.0%, model 55.9% (market_conditioned_v1 (model4_board_v1)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01VOLMER-18` Over 17.5 games: 0.73/0.83 mid 78.0%, model 87.5% (market_conditioned_v1 (model4_board_v1)) -- gap +9.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01VOLMER-28` Over 27.5 games: 0.21/0.29 mid 25.0%, model 34.0% (market_conditioned_v1 (model4_board_v1)) -- gap +8.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dayana Yastremska vs Maja Chwalinska -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215035:216081:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maja Chwalinska (`KXWTAMATCH-26OCT01YASCHW-CHW`) | 0.02 / 0.03 (32430) | 2.5% | -- | 81.1% | 72.6% [59.0%-77.3%] | 60.2% | -- | 60.2% | MODEL_LONE_OUTLIER | WATCH | +70.1 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Dayana Yastremska (`KXWTAMATCH-26OCT01YASCHW-YAS`) | 0.96 / 0.97 (5178) | 96.5% | -- | 18.9% | 27.4% [22.7%-41.0%] | 39.8% | -- | 39.8% | MODEL_LONE_OUTLIER | PASS | -69.1 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 4632.0, B 3543.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0914
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT01YASCHW-CHW  (YES = Maja Chwalinska)
Model: 73%
Kalshi: 2%
Gap: +70 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose -0.022, surface_dev_tight +0.027
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01YASCHW-22` Over 21.5 games: 0.06/0.07 mid 6.5%, model 24.4% (market_conditioned_v1 (model4_board_v1)) -- gap +17.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01YASCHW-17` Over 16.5 games: 0.63/0.65 mid 64.0%, model 66.5% (market_conditioned_v1 (model4_board_v1)) -- gap +2.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01YASCHW-27` Over 26.5 games: 0.05/0.13 mid 9.0%, model 11.5% (market_conditioned_v1 (model4_board_v1)) -- gap +2.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yue Yuan vs Mirra Andreeva -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:206294:259799:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mirra Andreeva (`KXWTAMATCH-26OCT01YUAAND-AND`) | 0.99 / -- (0) | -- | -- | 89.4% | 87.9% [85.1%-88.9%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | A / ADEQUATE | INSUFFICIENT_INPUTS | VERIFIED |
| Yue Yuan (`KXWTAMATCH-26OCT01YUAAND-YUA`) | -- / 0.01 (160250) | -- | -- | 10.6% | 12.1% [11.1%-14.9%] | -- | -- | -- | -- | SHADOW_BET | -- | UNPRICED | STALE | A / ADEQUATE | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 4806.0, B 4895.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0192
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.014, surface_dev_loose -0.005, surface_dev_tight +0.008
* Derivatives listed: 2 (MATCH_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE

## Renata Zarazua vs Aryna Sabalenka -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213887:214544:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aryna Sabalenka (`KXWTAMATCH-26OCT01ZARSAB-SAB`) | 0.96 / 0.97 (31872) | 96.5% | -- | 95.1% | 95.1% [94.2%-95.5%] | 94.7% | 96.2% | 96.2% | MODEL_LONE_OUTLIER | PASS | -1.4 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Renata Zarazua (`KXWTAMATCH-26OCT01ZARSAB-ZAR`) | 0.03 / 0.04 (26539) | 3.5% | -- | 4.9% | 4.9% [4.5%-5.8%] | 5.3% | 3.6% | 3.6% | MODEL_LONE_OUTLIER | PASS | +1.4 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4923.0, B 5768.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0064
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.003, surface_dev_loose -0.002, surface_dev_tight +0.004
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT01ZARSAB-17` Over 16.5 games: 0.62/0.63 mid 62.5%, model 75.5% (market_conditioned_v1 (model4_board_v1)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT01ZARSAB-22` Over 21.5 games: 0.12/0.26 mid 19.0%, model 29.7% (market_conditioned_v1 (model4_board_v1)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
* Warnings: SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Qinwen Zheng vs Anna Kalinskaya -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-02T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214939:221012:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Kalinskaya (`KXWTAMATCH-26OCT01ZHEKAL-KAL`) | 0.38 / 0.39 (15923) | 38.5% | -- | 35.8% | 37.8% [35.8%-40.2%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Qinwen Zheng (`KXWTAMATCH-26OCT01ZHEKAL-ZHE`) | 0.62 / 0.63 (15284) | 62.5% | -- | 64.2% | 62.2% [59.8%-64.2%] | -- | -- | -- | -- | PASS | -0.3 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3151.0, B 4015.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0217
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT01ZHEKAL-23` Over 22.5 games: 0.44/0.46 mid 45.0%, model 56.5% (market_conditioned_v1 (model4_board_v1)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01ZHEKAL-18` Over 17.5 games: 0.74/0.83 mid 78.5%, model 89.3% (market_conditioned_v1 (model4_board_v1)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT01ZHEKAL-28` Over 27.5 games: 0.21/0.29 mid 25.0%, model 35.6% (market_conditioned_v1 (model4_board_v1)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arakawa / Tse vs Di Tommaso / Simes -- W35 Wagga Wagga SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01ARATSEDITSIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arakawa / Tse (`KXITFWDOUBLES-26OCT01ARATSEDITSIM-ARATSE`) | 0.36 / 0.77 (40) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Di Tommaso / Simes (`KXITFWDOUBLES-26OCT01ARATSEDITSIM-DITSIM`) | 0.21 / 0.60 (92) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Aliona Falei vs Sara Sorribes Tormo -- WTA 125K Jingshan QF

WTA125 (WTA_125) · Hard · scheduled 2026-10-02T07:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:204427:221434:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aliona Falei (`KXWTACHALLENGERMATCH-26OCT02FALSOR-FAL`) | 0.90 / 0.91 (164035) | 90.5% | 55.8% | 80.8% | 71.4% [54.8%-77.0%] | 42.8% | 43.3% | 43.1% | MODEL_LONE_OUTLIER | PASS | -19.1 pp | HIGH_REVIEW | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Sara Sorribes Tormo (`KXWTACHALLENGERMATCH-26OCT02FALSOR-SOR`) | 0.09 / 0.10 (6093) | 9.5% | 44.2% | 19.2% | 28.6% [23.0%-45.2%] | 57.2% | 56.5% | 56.9% | MODEL_LONE_OUTLIER | WATCH | +19.1 pp | HIGH_REVIEW | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 3528.0, B 3334.0; serve-point win A 56.2%, B 44.9%; Elo A 1742.7, B 1774.0; model uncertainty 0.1109
* Form inputs: days since last match A 1, B 3; matches on record A 280, B 706; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT02FALSOR-SOR  (YES = Sara Sorribes Tormo)
Model: 29%
Kalshi: 10%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.013, surface_dev_loose +0.022, surface_dev_tight -0.028
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## David Stevenson / Marcus Willis vs Hugo Nys / Edouard Roger-Vasselin -- ATP Tokyo R16

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-02T07:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02STEWILNYSROG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Nys / Edouard Roger-Vasselin (`KXATPDOUBLES-26OCT02STEWILNYSROG-NYSROG`) | 0.66 / 0.69 (1812) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| David Stevenson / Marcus Willis (`KXATPDOUBLES-26OCT02STEWILNYSROG-STEWIL`) | 0.31 / 0.34 (1057) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Ryuki Matsuda vs Kosuke Ogura -- M15 Luan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202124:207987:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryuki Matsuda (`KXITFMATCH-26OCT01MATOGU-MAT`) | 0.91 / 0.92 (9478) | 91.5% | 53.1% | 41.7% | 46.9% [44.3%-52.1%] | -- | -- | -- | -- | PASS | -44.6 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kosuke Ogura (`KXITFMATCH-26OCT01MATOGU-OGU`) | 0.08 / 0.09 (14546) | 8.5% | 46.9% | 58.3% | 53.1% [47.9%-55.7%] | -- | -- | -- | -- | PASS | +44.6 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3092.0, B 3515.0; serve-point win A 62.9%, B 37.7%; Elo A 1307.8, B 1257.4; model uncertainty 0.0389
* Form inputs: days since last match A 18, B 123; matches on record A 275, B 256; data quality A

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT01MATOGU-OGU  (YES = Kosuke Ogura)
Model: 53%
Kalshi: 8%
Gap: +45 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.015, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alex Bolt vs Dane Sweeny -- ATP Challenger Jingshan QF

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106109:208013:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex Bolt (`KXATPCHALLENGERMATCH-26OCT02BOLSWE-BOL`) | 0.56 / 0.59 (272) | 57.5% | 50.6% | 46.5% | 48.0% [44.5%-54.0%] | -- | 41.5% | 41.5% | MODEL_LONE_OUTLIER | PASS | -9.5 pp | NORMAL | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Dane Sweeny (`KXATPCHALLENGERMATCH-26OCT02BOLSWE-SWE`) | 0.41 / 0.44 (283) | 42.5% | 49.4% | 53.5% | 52.0% [46.0%-55.5%] | -- | 58.0% | 58.0% | MODEL_LONE_OUTLIER | WATCH | +9.5 pp | NORMAL | STALE | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 5430.0, B 5839.0; serve-point win A 62.7%, B 37.5%; Elo A 1660.4, B 1655.7; model uncertainty 0.0476
* Form inputs: days since last match A 8, B 8; matches on record A 932, B 481; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.035, surface_dev_loose -0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Lloyd Harris vs Andre Ilagan -- ATP Challenger Jingshan QF

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:144750:210318:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lloyd Harris (`KXATPCHALLENGERMATCH-26OCT02HARILA-HAR`) | 0.82 / 0.83 (26714) | 82.5% | 72.7% | 66.3% | 70.3% [68.5%-72.9%] | -- | 81.0% | 81.0% | MODEL_LONE_OUTLIER | PASS | -12.2 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Andre Ilagan (`KXATPCHALLENGERMATCH-26OCT02HARILA-ILA`) | 0.17 / 0.18 (21296) | 17.5% | 27.3% | 33.7% | 29.7% [27.2%-31.4%] | -- | 17.2% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +12.2 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4129.0, B 5539.0; serve-point win A 65.0%, B 39.8%; Elo A 1841.8, B 1608.9; model uncertainty 0.0215
* Form inputs: days since last match A 5, B 10; matches on record A 809, B 236; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Ha Eum Lee vs Ke Ren -- W15 Maanshan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:260621:270449:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ha Eum Lee (`KXITFWMATCH-26OCT01LEEREN-LEE`) | 0.99 / -- (0) | -- | 68.8% | 73.0% | 69.4% [67.5%-72.1%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Ke Ren (`KXITFWMATCH-26OCT01LEEREN-REN`) | -- / 0.01 (55383) | -- | 31.2% | 27.0% | 30.6% [27.9%-32.5%] | -- | -- | -- | -- | PASS | -- | UNPRICED | STALE | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 1048.0, B 366.0; serve-point win A 57.5%, B 46.2%; Elo A 1390.4, B 1253.1; model uncertainty 0.0232
* Form inputs: days since last match A 158, B 158; matches on record A 15, B 72; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.014, surface_pool_high -0.009, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xi Luo vs Ha Yoon Son -- W15 Maanshan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:260607:264069:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xi Luo (`KXITFWMATCH-26OCT01LUOSON-LUO`) | 0.91 / 0.92 (805) | 91.5% | 77.4% | 80.8% | 77.3% [76.5%-79.7%] | -- | -- | -- | -- | PASS | -14.2 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ha Yoon Son (`KXITFWMATCH-26OCT01LUOSON-SON`) | 0.08 / 0.09 (6134) | 8.5% | 22.6% | 19.2% | 22.7% [20.3%-23.5%] | -- | -- | -- | -- | PASS | +14.2 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 827.0, B 90.0; serve-point win A 58.5%, B 47.1%; Elo A 1415.7, B 1202.0; model uncertainty 0.016
* Form inputs: days since last match A 158, B 172; matches on record A 43, B 11; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.016, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stevens / Thompson vs Kitahara / Wen Wan -- W35 Wagga Wagga SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT01STETHOKITWEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kitahara / Wen Wan (`KXITFWDOUBLES-26OCT01STETHOKITWEN-KITWEN`) | 0.41 / 0.70 (154) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stevens / Thompson (`KXITFWDOUBLES-26OCT01STETHOKITWEN-STETHO`) | 0.22 / 0.64 (61) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Yingqun Sun vs Jiayu Xu -- W15 Maanshan QF

ITF (ITF) · Hard · scheduled 2026-10-02T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222606:264029:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yingqun Sun (`KXITFWMATCH-26OCT01SUNXUX-SUN`) | 0.41 / 0.45 (10) | 43.0% | 59.1% | 78.4% | 64.5% [58.5%-69.8%] | -- | -- | -- | -- | WATCH | +21.5 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiayu Xu (`KXITFWMATCH-26OCT01SUNXUX-XUX`) | 0.56 / 0.59 (5) | 57.5% | 40.9% | 21.6% | 35.5% [30.2%-41.5%] | -- | -- | -- | -- | PASS | -22.0 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1826.0, B 444.0; serve-point win A 56.5%, B 45.2%; Elo A 1387.9, B 1324.1; model uncertainty 0.0568
* Form inputs: days since last match A 158, B 158; matches on record A 99, B 86; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT01SUNXUX-SUN  (YES = Yingqun Sun)
Model: 65%
Kalshi: 43%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose +0.015, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jessica Bouzas Maneiro vs Sofya Lansere -- WTA 125K Jingshan QF

WTA125 (WTA_125) · Hard · scheduled 2026-10-02T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216139:222601:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jessica Bouzas Maneiro (`KXWTACHALLENGERMATCH-26OCT02BOULAN-BOU`) | 0.84 / 0.85 (45435) | 84.5% | 58.1% | 37.3% | 48.4% [41.0%-68.1%] | -- | 84.4% | 84.4% | MODEL_LONE_OUTLIER | PASS | -36.1 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Sofya Lansere (`KXWTACHALLENGERMATCH-26OCT02BOULAN-LAN`) | 0.16 / 0.17 (18978) | 16.5% | 41.9% | 62.7% | 51.6% [31.9%-59.0%] | -- | 16.1% | 16.1% | MODEL_LONE_OUTLIER | WATCH | +35.1 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3457.0, B 3253.0; serve-point win A 56.5%, B 45.1%; Elo A 1802.7, B 1649.3; model uncertainty 0.1356
* Form inputs: days since last match A 16, B 1; matches on record A 434, B 351; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26OCT02BOULAN-LAN  (YES = Sofya Lansere)
Model: 52%
Kalshi: 16%
Gap: +35 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.037, surface_pool_high -0.048, surface_dev_loose -0.016, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Han / Zhang vs Ichikawa / Jeong -- M15 Luan SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T09:09:06Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT01HANZHAICHJEO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Han / Zhang (`KXITFDOUBLES-26OCT01HANZHAICHJEO-HANZHA`) | 0.05 / 0.69 (1) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ichikawa / Jeong (`KXITFDOUBLES-26OCT01HANZHAICHJEO-ICHJEO`) | 0.26 / 0.67 (1) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexandra Shubladze vs Sijia Wei -- WTA 125K Jingshan QF

WTA125 (WTA_125) · Hard · scheduled 2026-10-02T09:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221096:260168:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Shubladze (`KXWTACHALLENGERMATCH-26OCT02SHUWEI-SHU`) | 0.77 / 0.78 (18085) | 77.5% | 69.4% | 88.0% | 75.7% [66.6%-81.1%] | 75.7% | 78.2% | 76.9% | MODEL_LONE_OUTLIER | PASS | -1.8 pp | NORMAL | STALE | B / LIMITED | ALL_AGREE | VERIFIED |
| Sijia Wei (`KXWTACHALLENGERMATCH-26OCT02SHUWEI-WEI`) | 0.22 / 0.23 (15195) | 22.5% | 30.6% | 12.0% | 24.3% [18.9%-33.4%] | 24.3% | 22.0% | 23.2% | MODEL_LONE_OUTLIER | PASS | +1.8 pp | NORMAL | STALE | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3247.0, B 2150.0; serve-point win A 57.6%, B 46.2%; Elo A 1728.3, B 1721.8; model uncertainty 0.0728
* Form inputs: days since last match A 3, B 158; matches on record A 201, B 301; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.024, surface_pool_high -0.026, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## HSUN LIN / Yang vs SUN / Wang -- M15 Luan SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T10:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02HSUYANSUNWAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HSUN LIN / Yang (`KXITFDOUBLES-26OCT02HSUYANSUNWAN-HSUYAN`) | 0.86 / 0.88 (660) | 87.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| SUN / Wang (`KXITFDOUBLES-26OCT02HSUYANSUNWAN-SUNWAN`) | 0.11 / 0.13 (212) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Maximo Gonzalez / Andres Molteni vs Alexander Bublik / Juncheng Shang -- ATP Beijing QF

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-02T10:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02GONMOLBUBSHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Bublik / Juncheng Shang (`KXATPDOUBLES-26OCT02GONMOLBUBSHA-BUBSHA`) | 0.31 / 0.33 (2595) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maximo Gonzalez / Andres Molteni (`KXATPDOUBLES-26OCT02GONMOLBUBSHA-GONMOL`) | 0.67 / 0.68 (174) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Yi Chen / Luo vs Choi / Suvirdjonkova -- W15 Maanshan SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02YICLUOCHOSUV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Choi / Suvirdjonkova (`KXITFWDOUBLES-26OCT02YICLUOCHOSUV-CHOSUV`) | 0.21 / 0.34 (27) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yi Chen / Luo (`KXITFWDOUBLES-26OCT02YICLUOCHOSUV-YICLUO`) | 0.23 / 0.76 (1) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yi Liu / Sun vs Chen / Tang -- W15 Maanshan SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T11:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02YILSUNCHETAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chen / Tang (`KXITFWDOUBLES-26OCT02YILSUNCHETAN-CHETAN`) | 0.44 / 0.48 (12) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yi Liu / Sun (`KXITFWDOUBLES-26OCT02YILSUNCHETAN-YILSUN`) | 0.41 / 0.63 (14) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Finn Bass / Scott Duncan vs Constantin Bittoun Kouzmine / Niels Visker -- ATP Challenger Mouilleron-Le-Captif SF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-02T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02BASDUNBITVIS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Finn Bass / Scott Duncan (`KXATPCHALLENGERDOUBLES-26OCT02BASDUNBITVIS-BASDUN`) | 0.44 / 0.49 (49) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Constantin Bittoun Kouzmine / Niels Visker (`KXATPCHALLENGERDOUBLES-26OCT02BASDUNBITVIS-BITVIS`) | 0.49 / 0.56 (155) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Casey Hoole vs Colin Sinclair -- M25 Darwin QF

ITF (ITF) · Hard · scheduled 2026-10-02T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:124040:211315:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Casey Hoole (`KXITFMATCH-26OCT02HOOSIN-HOO`) | 0.54 / 0.56 (1211) | 55.0% | 42.7% | 46.6% | 43.2% [36.4%-49.0%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.8 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Colin Sinclair (`KXITFMATCH-26OCT02HOOSIN-SIN`) | 0.44 / 0.45 (208) | 44.5% | 57.3% | 53.4% | 56.8% [51.0%-63.6%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +12.3 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 187.0, B 4093.0; serve-point win A 61.9%, B 36.7%; Elo A 1372.4, B 1423.3; model uncertainty 0.0631
* Form inputs: days since last match A 641, B 18; matches on record A 18, B 427; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.057, surface_pool_high +0.058, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Philip Sekulic vs Herman Hoeyeraal -- M25 Darwin QF

ITF (ITF) · Hard · scheduled 2026-10-02T11:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208382:210340:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Herman Hoeyeraal (`KXITFMATCH-26OCT02SEKHOE-HOE`) | 0.17 / 0.20 (1194) | 18.5% | 27.4% | 31.7% | 26.2% [24.4%-28.6%] | -- | -- | -- | -- | WATCH | +7.7 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Philip Sekulic (`KXITFMATCH-26OCT02SEKHOE-SEK`) | 0.78 / 0.82 (129) | 80.0% | 72.6% | 68.3% | 73.9% [71.4%-75.6%] | -- | -- | -- | -- | PASS | -6.2 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4539.0, B 1869.0; serve-point win A 65.0%, B 39.8%; Elo A 1562.7, B 1322.1; model uncertainty 0.021
* Form inputs: days since last match A 10, B 88; matches on record A 316, B 42; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.008, surface_dev_loose -0.008, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arda Azkara vs Digvijay Pratap Singh -- M15 Baku QF

ITF (ITF) · surface ? · scheduled 2026-10-02T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200014:207907:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arda Azkara (`KXITFMATCH-26OCT02AZKSIN-AZK`) | 0.49 / 0.50 (3687) | 49.5% | 57.6% | 55.4% | 57.8% [56.8%-58.4%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +8.3 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Digvijay Pratap Singh (`KXITFMATCH-26OCT02AZKSIN-SIN`) | 0.50 / 0.51 (3615) | 50.5% | 42.4% | 44.6% | 42.2% [41.6%-43.2%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.3 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1821.0, B 2204.0; serve-point win A 64.8%, B 36.8%; Elo A 1438.0, B 1360.6; model uncertainty 0.0076
* Form inputs: days since last match A 60, B 18; matches on record A 94, B 181; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matic Dimic vs Dmitry Popko -- M15 Telavi SF

ITF (ITF) · Clay · scheduled 2026-10-02T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:122078:210174:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matic Dimic (`KXITFMATCH-26OCT02DIMPOP-DIM`) | 0.09 / 0.10 (843) | 9.5% | 5.6% | 17.0% | 7.4% [4.9%-9.6%] | 10.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.1 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dmitry Popko (`KXITFMATCH-26OCT02DIMPOP-POP`) | 0.91 / 0.93 (1938) | 92.0% | 94.4% | 83.0% | 92.6% [90.4%-95.2%] | 89.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 459.0, B 4384.0; serve-point win A 53.7%, B 33.9%; Elo A 1085.9, B 1577.9; model uncertainty 0.0239
* Form inputs: days since last match A 123, B 88; matches on record A 57, B 1042; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.022, surface_dev_loose -0.004, surface_dev_tight +0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Millen Hurrion vs Louis Larue -- M15 Baku QF

ITF (ITF) · surface ? · scheduled 2026-10-02T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209140:211646:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Millen Hurrion (`KXITFMATCH-26OCT02HURLAR-HUR`) | 0.89 / 0.90 (2297) | 89.5% | 79.4% | 82.2% | 80.1% [76.4%-82.9%] | 88.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.4 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Louis Larue (`KXITFMATCH-26OCT02HURLAR-LAR`) | 0.10 / 0.12 (5194) | 11.0% | 20.6% | 17.8% | 19.9% [17.1%-23.5%] | 11.7% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +8.9 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3153.0, B 1681.0; serve-point win A 67.3%, B 39.3%; Elo A 1476.4, B 1260.9; model uncertainty 0.0323
* Form inputs: days since last match A 60, B 137; matches on record A 183, B 48; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dragos Nicolae Madaras vs Stijn Paardekooper -- M15 Telavi SF

ITF (ITF) · Clay · scheduled 2026-10-02T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200096:212311:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dragos Nicolae Madaras (`KXITFMATCH-26OCT02MADPAA-MAD`) | 0.76 / 0.78 (1126) | 77.0% | 85.9% | 93.2% | 89.5% [85.3%-92.1%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +12.5 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stijn Paardekooper (`KXITFMATCH-26OCT02MADPAA-PAA`) | 0.21 / 0.24 (3603) | 22.5% | 14.1% | 6.8% | 10.5% [7.9%-14.7%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.0 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1481.0, B 1300.0; serve-point win A 64.1%, B 44.3%; Elo A 1646.0, B 1340.4; model uncertainty 0.0339
* Form inputs: days since last match A 186, B 207; matches on record A 475, B 45; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nannelli / Seleznev vs Mishkin / Shvets -- M15 Telavi F

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02NANSELMISSHV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mishkin / Shvets (`KXITFDOUBLES-26OCT02NANSELMISSHV-MISSHV`) | 0.14 / 0.59 (2100) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nannelli / Seleznev (`KXITFDOUBLES-26OCT02NANSELMISSHV-NANSEL`) | 0.07 / 0.50 (2) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Marcus Walters vs James Connel -- M15 Baku QF

ITF (ITF) · surface ? · scheduled 2026-10-02T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:126971:212250:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Connel (`KXITFMATCH-26OCT02WALCON-CON`) | 0.63 / 0.66 (5363) | 64.5% | 62.7% | 62.6% | 63.5% [62.6%-64.5%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marcus Walters (`KXITFMATCH-26OCT02WALCON-WAL`) | 0.36 / 0.37 (6228) | 36.5% | 37.3% | 37.4% | 36.5% [35.5%-37.4%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.0 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2102.0, B 868.0; serve-point win A 62.7%, B 34.7%; Elo A 1257.0, B 1362.6; model uncertainty 0.0096
* Form inputs: days since last match A 88, B 144; matches on record A 106, B 27; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gianluca Cadenasso vs Vitaliy Sachko -- ATP Challenger Bari QF

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:126964:211533:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gianluca Cadenasso (`KXATPCHALLENGERMATCH-26OCT02CADSAC-CAD`) | 0.41 / 0.42 (11935) | 41.5% | 50.4% | 59.4% | 54.2% [46.9%-58.9%] | 42.8% | 41.7% | 41.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +12.7 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Vitaliy Sachko (`KXATPCHALLENGERMATCH-26OCT02CADSAC-SAC`) | 0.58 / 0.59 (5311) | 58.5% | 49.6% | 40.6% | 45.8% [41.1%-53.1%] | 57.2% | 58.7% | 58.7% | MODEL_LONE_OUTLIER | PASS | -12.7 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2989.0, B 5739.0; serve-point win A 59.9%, B 40.1%; Elo A 1656.1, B 1699.3; model uncertainty 0.0603
* Form inputs: days since last match A 11, B 18; matches on record A 175, B 683; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.021, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Scott Jones vs Hayden Jones -- M25 Darwin QF

ITF (ITF) · Hard · scheduled 2026-10-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:206921:210436:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Scott Jones (`KXITFMATCH-26OCT02JONJON2-JON`) | 0.44 / 0.45 (64) | 44.5% | 64.5% | 72.8% | 66.5% [60.2%-69.3%] | 46.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +22.0 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hayden Jones (`KXITFMATCH-26OCT02JONJON2-JON2`) | 0.55 / 0.56 (3573) | 55.5% | 35.5% | 27.2% | 33.5% [30.7%-39.8%] | 53.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -22.0 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1787.0, B 1969.0; serve-point win A 64.1%, B 38.9%; Elo A 1333.5, B 1276.0; model uncertainty 0.0455
* Form inputs: days since last match A 193, B 312; matches on record A 62, B 71; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02JONJON2-JON  (YES = Scott Jones)
Model: 67%
Kalshi: 44%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.009, surface_dev_loose +0.001, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Derek Pham vs Jake Delaney -- M25 Darwin QF

ITF (ITF) · Hard · scheduled 2026-10-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:117359:210613:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jake Delaney (`KXITFMATCH-26OCT02PHADEL-DEL`) | 0.65 / 0.66 (1778) | 65.5% | 69.5% | 72.7% | 69.7% [69.0%-71.3%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Derek Pham (`KXITFMATCH-26OCT02PHADEL-PHA`) | 0.33 / 0.34 (836) | 33.5% | 30.5% | 27.3% | 30.3% [28.7%-31.0%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.2 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 178.0, B 4278.0; serve-point win A 60.6%, B 35.4%; Elo A 1312.3, B 1455.6; model uncertainty 0.0113
* Form inputs: days since last match A 319, B 10; matches on record A 71, B 364; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.004, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Samuele Pieri vs Carlos Taberner -- ATP Challenger Bari QF

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:126535:210129:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samuele Pieri (`KXATPCHALLENGERMATCH-26OCT02PIETAB-PIE`) | 0.23 / 0.24 (8558) | 23.5% | 32.3% | 43.3% | 36.2% [32.4%-39.2%] | 24.7% | 22.8% | 22.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +12.7 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Carlos Taberner (`KXATPCHALLENGERMATCH-26OCT02PIETAB-TAB`) | 0.76 / 0.77 (6013) | 76.5% | 67.7% | 56.7% | 63.8% [60.8%-67.6%] | 75.3% | 77.8% | 77.8% | MODEL_LONE_OUTLIER | PASS | -12.7 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4011.0, B 4908.0; serve-point win A 58.1%, B 38.3%; Elo A 1518.3, B 1745.9; model uncertainty 0.0338
* Form inputs: days since last match A 11, B 11; matches on record A 209, B 923; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.005, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Karl Poling / Joshua Sheehy vs Liam Broady / Emile Hudd -- ATP Challenger Mouilleron-Le-Captif SF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-02T12:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02POLSHEBROHUD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liam Broady / Emile Hudd (`KXATPCHALLENGERDOUBLES-26OCT02POLSHEBROHUD-BROHUD`) | 0.37 / 0.45 (2577) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karl Poling / Joshua Sheehy (`KXATPCHALLENGERDOUBLES-26OCT02POLSHEBROHUD-POLSHE`) | 0.55 / 0.63 (19) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Anton Arzhankin vs Karan Singh -- M15 Sharm ElSheikh QF

ITF (ITF) · Hard · scheduled 2026-10-02T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210000:213996:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anton Arzhankin (`KXITFMATCH-26OCT02ARZSIN-ARZ`) | 0.44 / 0.48 (11) | 46.0% | 59.5% | 75.6% | 67.7% [57.5%-72.3%] | -- | -- | -- | -- | WATCH | +21.7 pp | HIGH_REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Karan Singh (`KXITFMATCH-26OCT02ARZSIN-SIN`) | 0.50 / 0.57 (3818) | 53.5% | 40.5% | 24.4% | 32.3% [27.7%-42.5%] | -- | -- | -- | -- | PASS | -21.2 pp | HIGH_REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1841.0, B 3601.0; serve-point win A 63.5%, B 38.4%; Elo A 1441.2, B 1400.5; model uncertainty 0.0743
* Form inputs: days since last match A 123, B 67; matches on record A 34, B 257; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02ARZSIN-ARZ  (YES = Anton Arzhankin)
Model: 68%
Kalshi: 46%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.004, surface_dev_loose +0.021, surface_dev_tight -0.027
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hugo Grenier vs Inaki Montes-de la Torre -- ATP Challenger Porto 2 QF

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-02T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:126409:208540:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Grenier (`KXATPCHALLENGERMATCH-26OCT02GREMON-GRE`) | 0.42 / 0.43 (24607) | 42.5% | 41.0% | 34.9% | 38.3% [36.3%-41.3%] | 42.8% | 42.8% | 42.8% | MODEL_LONE_OUTLIER | PASS | -4.2 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Inaki Montes-de la Torre (`KXATPCHALLENGERMATCH-26OCT02GREMON-MON`) | 0.57 / 0.58 (6560) | 57.5% | 59.0% | 65.1% | 61.7% [58.7%-63.7%] | 57.2% | 57.5% | 57.5% | MODEL_LONE_OUTLIER | WATCH | +4.2 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4799.0, B 4378.0; serve-point win A 61.7%, B 36.5%; Elo A 1658.2, B 1650.2; model uncertainty 0.0249
* Form inputs: days since last match A 11, B 18; matches on record A 946, B 245; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Volodymyr Iakubenko vs Kerem Yilmaz -- M15 Baku QF

ITF (ITF) · surface ? · scheduled 2026-10-02T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:212030:212246:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Volodymyr Iakubenko (`KXITFMATCH-26OCT02IAKYIL-IAK`) | 0.47 / 0.50 (4652) | 48.5% | 58.4% | 60.2% | 59.2% [58.7%-60.7%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +10.7 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kerem Yilmaz (`KXITFMATCH-26OCT02IAKYIL-YIL`) | 0.51 / 0.54 (93) | 52.5% | 41.6% | 39.8% | 40.8% [39.3%-41.3%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.7 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1553.0, B 1537.0; serve-point win A 64.8%, B 36.9%; Elo A 1285.6, B 1224.3; model uncertainty 0.0099
* Form inputs: days since last match A 137, B 60; matches on record A 50, B 45; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Paul Jubb vs Amr Elsayed -- M15 Sharm ElSheikh QF

ITF (ITF) · surface ? · scheduled 2026-10-02T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02JUBELS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amr Elsayed (`KXITFMATCH-26OCT02JUBELS-ELS`) | 0.11 / 0.13 (4020) | 12.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Paul Jubb (`KXITFMATCH-26OCT02JUBELS-JUB`) | 0.85 / 0.89 (2722) | 87.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniel Rincon vs David Jorda Sanchis -- ATP Challenger Porto 2 QF

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-02T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:122554:209405:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Jorda Sanchis (`KXATPCHALLENGERMATCH-26OCT02RINJOR-JOR`) | 0.27 / 0.28 (15) | 27.5% | 41.2% | 41.4% | 39.5% [37.6%-40.9%] | 29.4% | 29.5% | 29.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +12.0 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Daniel Rincon (`KXATPCHALLENGERMATCH-26OCT02RINJOR-RIN`) | 0.71 / 0.73 (8632) | 72.0% | 58.8% | 58.6% | 60.5% [59.1%-62.4%] | 70.6% | 71.5% | 71.0% | MODEL_LONE_OUTLIER | PASS | -11.5 pp | REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5943.0, B 5646.0; serve-point win A 63.5%, B 38.3%; Elo A 1617.2, B 1499.8; model uncertainty 0.0167
* Form inputs: days since last match A 11, B 11; matches on record A 422, B 495; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.019, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Robert Strombachs vs Michal Krajci -- M15 Sharm ElSheikh QF

ITF (ITF) · Hard · scheduled 2026-10-02T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207669:211756:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michal Krajci (`KXITFMATCH-26OCT02STRKRA-KRA`) | 0.31 / 0.35 (137) | 33.0% | 35.1% | 30.3% | 31.2% [29.9%-32.1%] | -- | -- | -- | -- | PASS | -1.8 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Robert Strombachs (`KXITFMATCH-26OCT02STRKRA-STR`) | 0.65 / 0.69 (4969) | 67.0% | 64.9% | 69.7% | 68.8% [67.9%-70.1%] | -- | -- | -- | -- | PASS | +1.8 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3812.0, B 3305.0; serve-point win A 64.1%, B 38.9%; Elo A 1528.0, B 1399.3; model uncertainty 0.011
* Form inputs: days since last match A 18, B 123; matches on record A 483, B 123; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.009, surface_dev_loose +0.009, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jade Groen vs Ksenia Meshcheryakova -- W15 Sharm ElSheikh QF

ITF (ITF) · Hard · scheduled 2026-10-02T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222554:267722:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jade Groen (`KXITFWMATCH-26OCT02GROMES-GRO`) | 0.72 / 0.77 (11) | 74.5% | 86.2% | 79.0% | 85.2% [83.9%-86.1%] | -- | -- | -- | -- | PASS | +10.7 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ksenia Meshcheryakova (`KXITFWMATCH-26OCT02GROMES-MES`) | 0.23 / 0.28 (230) | 25.5% | 13.8% | 21.0% | 14.8% [13.9%-16.1%] | -- | -- | -- | -- | PASS | -10.7 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 470.0, B 335.0; serve-point win A 59.8%, B 48.4%; Elo A 1298.8, B 980.4; model uncertainty 0.0111
* Form inputs: days since last match A 326, B 158; matches on record A 9, B 75; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.006, surface_dev_loose +0.003, surface_dev_tight -0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuliya Hatouka vs Ksenia Smirnova -- W15 Sharm ElSheikh QF

ITF (ITF) · Hard · scheduled 2026-10-02T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216013:269968:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuliya Hatouka (`KXITFWMATCH-26OCT02HATSMI-HAT`) | 0.82 / 0.86 (4295) | 84.0% | 65.0% | 58.5% | 68.1% [64.2%-73.2%] | -- | -- | -- | -- | PASS | -15.9 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ksenia Smirnova (`KXITFWMATCH-26OCT02HATSMI-SMI`) | 0.14 / 0.17 (1046) | 15.5% | 34.9% | 41.5% | 31.9% [26.9%-35.8%] | -- | -- | -- | -- | PASS | +16.4 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2126.0, B 692.0; serve-point win A 57.1%, B 45.8%; Elo A 1626.6, B 1461.8; model uncertainty 0.0449
* Form inputs: days since last match A 179, B 165; matches on record A 378, B 17; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02HATSMI-SMI  (YES = Ksenia Smirnova)
Model: 32%
Kalshi: 16%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.015, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Antonina Sushkova vs Esther Adeshina -- W15 Sharm ElSheikh QF

ITF (ITF) · Hard · scheduled 2026-10-02T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221959:266849:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Esther Adeshina (`KXITFWMATCH-26OCT02SUSADE-ADE`) | 0.47 / 0.49 (335) | 48.0% | 76.0% | 67.6% | 74.0% [72.7%-74.9%] | -- | -- | -- | -- | PASS | +26.0 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Antonina Sushkova (`KXITFWMATCH-26OCT02SUSADE-SUS`) | 0.50 / 0.52 (1944) | 51.0% | 24.0% | 32.4% | 26.0% [25.1%-27.3%] | -- | -- | -- | -- | PASS | -25.0 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 527.0, B 3059.0; serve-point win A 53.0%, B 41.6%; Elo A 1288.5, B 1488.7; model uncertainty 0.0109
* Form inputs: days since last match A 228, B 100; matches on record A 11, B 115; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02SUSADE-ADE  (YES = Esther Adeshina)
Model: 74%
Kalshi: 48%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Charlotte Van Zonneveld vs Daria Zelinskaya -- W15 Sharm ElSheikh QF

ITF (ITF) · Hard · scheduled 2026-10-02T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:239158:264252:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charlotte Van Zonneveld (`KXITFWMATCH-26OCT02VANZEL-VAN`) | 0.36 / 0.40 (56) | 38.0% | 22.9% | 12.7% | 22.0% [17.0%-27.2%] | -- | -- | -- | -- | PASS | -16.0 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daria Zelinskaya (`KXITFWMATCH-26OCT02VANZEL-ZEL`) | 0.60 / 0.63 (4510) | 61.5% | 77.1% | 87.3% | 78.0% [72.8%-83.0%] | -- | -- | -- | -- | PASS | +16.5 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 578.0, B 2491.0; serve-point win A 52.9%, B 41.5%; Elo A 1320.6, B 1503.3; model uncertainty 0.0506
* Form inputs: days since last match A 221, B 82; matches on record A 32, B 171; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02VANZEL-ZEL  (YES = Daria Zelinskaya)
Model: 78%
Kalshi: 62%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.011, surface_dev_loose -0.007, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aleshchev / Dolzhenkov vs Delicata / Stamatopoulos -- M15 Baku SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02ALEDOLDELSTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleshchev / Dolzhenkov (`KXITFDOUBLES-26OCT02ALEDOLDELSTA-ALEDOL`) | 0.35 / 0.52 (0) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Delicata / Stamatopoulos (`KXITFDOUBLES-26OCT02ALEDOLDELSTA-DELSTA`) | 0.49 / 0.63 (1000) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Astrid Wanja Brune Olsen vs Felitsata Dorofeeva-Rybas -- W15 Varna QF

ITF (ITF) · Clay · scheduled 2026-10-02T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214934:267022:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Astrid Wanja Brune Olsen (`KXITFWMATCH-26OCT02BRUDOR-BRU`) | 0.13 / 0.14 (7290) | 13.5% | 38.3% | 37.9% | 38.9% [37.9%-39.9%] | -- | -- | -- | -- | PASS | +25.4 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Felitsata Dorofeeva-Rybas (`KXITFWMATCH-26OCT02BRUDOR-DOR`) | 0.86 / 0.87 (0) | 86.5% | 61.7% | 62.2% | 61.1% [60.1%-62.1%] | -- | -- | -- | -- | PASS | -25.4 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1262.0, B 923.0; serve-point win A 52.9%, B 44.9%; Elo A 1387.2, B 1460.2; model uncertainty 0.0103
* Form inputs: days since last match A 158, B 305; matches on record A 171, B 19; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02BRUDOR-BRU  (YES = Astrid Wanja Brune Olsen)
Model: 39%
Kalshi: 14%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valeria Garnevska vs Sapfo Sakellaridi -- W15 Varna QF

ITF (ITF) · Clay · scheduled 2026-10-02T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220364:270109:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valeria Garnevska (`KXITFWMATCH-26OCT02GARSAK-GAR`) | 0.21 / 0.23 (62) | 22.0% | 16.8% | 10.1% | 16.2% [14.9%-17.2%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -5.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sapfo Sakellaridi (`KXITFWMATCH-26OCT02GARSAK-SAK`) | 0.77 / 0.79 (3352) | 78.0% | 83.2% | 89.9% | 83.8% [82.8%-85.1%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.8 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 149.0, B 4165.0; serve-point win A 50.4%, B 42.4%; Elo A 1261.3, B 1539.3; model uncertainty 0.0112
* Form inputs: days since last match A 368, B 80; matches on record A 5, B 703; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.010, surface_dev_loose -0.003, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fabrizio Andaloro / Volodoymyr Uzhylovskyi vs Luis Carlos Alvarez Valdes / Adrian Oetzbach -- ATP Challenger Bari SF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-02T13:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02ANDUZVALVAOET:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Carlos Alvarez Valdes / Adrian Oetzbach (`KXATPCHALLENGERDOUBLES-26OCT02ANDUZVALVAOET-ALVAOET`) | 0.06 / 0.60 (14) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fabrizio Andaloro / Volodoymyr Uzhylovskyi (`KXATPCHALLENGERDOUBLES-26OCT02ANDUZVALVAOET-ANDUZV`) | 0.40 / 0.80 (15) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Enrico Dalla Valle vs Juan Cruz Martin Manzano -- ATP Challenger Bari QF

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-02T13:40:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:133872:212305:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enrico Dalla Valle (`KXATPCHALLENGERMATCH-26OCT02DALMAR-DAL`) | 0.72 / 0.73 (2635) | 72.5% | 67.3% | 76.2% | 73.7% [72.0%-74.6%] | 71.1% | 72.5% | 71.8% | MODEL_LONE_OUTLIER | PASS | +1.2 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Juan Cruz Martin Manzano (`KXATPCHALLENGERMATCH-26OCT02DALMAR-MAR`) | 0.27 / 0.28 (3814) | 27.5% | 32.7% | 23.8% | 26.3% [25.4%-28.0%] | 28.9% | 27.8% | 28.4% | MODEL_LONE_OUTLIER | PASS | -1.2 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5437.0, B 3350.0; serve-point win A 61.6%, B 41.8%; Elo A 1615.7, B 1491.1; model uncertainty 0.0129
* Form inputs: days since last match A 11, B 11; matches on record A 547, B 120; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.009, surface_dev_loose +0.004, surface_dev_tight -0.017
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Lucas Poullain vs Joel Schwaerzler -- ATP Challenger Mouilleron-Le-Captif QF

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-02T13:50:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:131911:212082:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Poullain (`KXATPCHALLENGERMATCH-26OCT02POUSCH-POU`) | 0.39 / 0.40 (43297) | 39.5% | 53.1% | 62.9% | 59.5% [53.5%-62.4%] | -- | 39.7% | 39.7% | MODEL_LONE_OUTLIER | WATCH | +20.0 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Joel Schwaerzler (`KXATPCHALLENGERMATCH-26OCT02POUSCH-SCH`) | 0.60 / 0.62 (15148) | 61.0% | 46.9% | 37.1% | 40.5% [37.6%-46.5%] | -- | 60.5% | 60.5% | MODEL_LONE_OUTLIER | PASS | -20.5 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4684.0, B 4727.0; serve-point win A 62.9%, B 37.7%; Elo A 1604.0, B 1601.4; model uncertainty 0.0444
* Form inputs: days since last match A 18, B 11; matches on record A 416, B 191; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT02POUSCH-POU  (YES = Lucas Poullain)
Model: 60%
Kalshi: 40%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.029, surface_dev_loose +0.009, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Gabi Adrian Boitan vs Florian Broska -- M25 Slobozia QF

ITF (ITF) · surface ? · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02BOIBRO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabi Adrian Boitan (`KXITFMATCH-26OCT02BOIBRO-BOI`) | 0.50 / 0.51 (1660) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Florian Broska (`KXITFMATCH-26OCT02BOIBRO-BRO`) | 0.49 / 0.50 (1791) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Castagnola / Orlando Fellin vs Lorusso / Senn -- M15 Sharm ElSheikh SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02CASORLLORSEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Castagnola / Orlando Fellin (`KXITFDOUBLES-26OCT02CASORLLORSEN-CASORL`) | 0.47 / 0.72 (1) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lorusso / Senn (`KXITFDOUBLES-26OCT02CASORLLORSEN-LORSEN`) | 0.26 / 0.40 (100) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sebastian Gima vs Jannik Opitz -- M25 Slobozia QF

ITF (ITF) · Clay · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200457:209142:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sebastian Gima (`KXITFMATCH-26OCT02GIMOPI-GIM`) | 0.64 / 0.67 (4964) | 65.5% | 65.2% | 60.5% | 69.4% [67.1%-72.2%] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.9 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jannik Opitz (`KXITFMATCH-26OCT02GIMOPI-OPI`) | 0.33 / 0.35 (977) | 34.0% | 34.8% | 39.5% | 30.6% [27.8%-32.9%] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.4 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3345.0, B 858.0; serve-point win A 61.4%, B 41.6%; Elo A 1402.1, B 1217.8; model uncertainty 0.0256
* Form inputs: days since last match A 11, B 165; matches on record A 386, B 50; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.004, surface_dev_loose +0.012, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Houkes vs Alec Beckley -- M25 Kigali QF

ITF (ITF) · Clay · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208069:209278:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alec Beckley (`KXITFMATCH-26OCT02HOUBEC-BEC`) | 0.10 / 0.11 (938) | 10.5% | 30.4% | 30.7% | 28.4% [26.7%-29.3%] | 14.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +17.9 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Max Houkes (`KXITFMATCH-26OCT02HOUBEC-HOU`) | 0.88 / 0.90 (7858) | 89.0% | 69.6% | 69.3% | 71.6% [70.7%-73.3%] | 85.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -17.4 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5070.0, B 3000.0; serve-point win A 61.9%, B 42.1%; Elo A 1640.9, B 1426.2; model uncertainty 0.0131
* Form inputs: days since last match A 53, B 123; matches on record A 430, B 232; data quality A

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02HOUBEC-BEC  (YES = Alec Beckley)
Model: 28%
Kalshi: 10%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.017, surface_dev_loose +0.013, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hrazdil / Lanik vs Arzhankin / Kunitsyn -- M15 Sharm ElSheikh SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02HRALANARZKUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arzhankin / Kunitsyn (`KXITFDOUBLES-26OCT02HRALANARZKUN-ARZKUN`) | 0.42 / 0.53 (1012) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hrazdil / Lanik (`KXITFDOUBLES-26OCT02HRALANARZKUN-HRALAN`) | 0.29 / 0.60 (0) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hubert Hurkacz vs Arthur Gea -- ATP Beijing R16

ATP (MASTERS_1000) · Hard · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:128034:210338:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Gea (`KXATPMATCH-26OCT02HURGEA-GEA`) | 0.41 / 0.42 (300) | 41.5% | 30.6% | 47.1% | 41.7% [34.6%-45.1%] | 43.4% | 42.4% | 42.9% | MODEL_LONE_OUTLIER | PASS | +0.2 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Hubert Hurkacz (`KXATPMATCH-26OCT02HURGEA-HUR`) | 0.57 / 0.58 (3514) | 57.5% | 69.4% | 52.9% | 58.3% [54.9%-65.3%] | 56.6% | 57.8% | 57.2% | MODEL_LONE_OUTLIER | PASS | +0.8 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4552.0, B 5606.0; serve-point win A 64.6%, B 39.4%; Elo A 1978.2, B 1815.5; model uncertainty 0.0524
* Form inputs: days since last match A 3, B 3; matches on record A 813, B 294; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.024, surface_dev_loose -0.034, surface_dev_tight +0.038
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26OCT02HURGEA-28` Over 27.5 games: 0.29/0.35 mid 32.0%, model 42.4% (market_conditioned_v1 (model4_board_v1)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02HURGEA-23` Over 22.5 games: 0.52/0.54 mid 53.0%, model 63.0% (market_conditioned_v1 (model4_board_v1)) -- gap +10.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26OCT02HURGEA-2-GEA` Will Arthur Gea win set 2 in the Hubert Hurkacz vs Arthur Gea match: 0.43/0.46 mid 44.5%, model 36.8% (Gen-1 ELO_DP_FAIR (prediction ledger)) -- gap -7.7 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT02HURGEA-2-HUR` Will Hubert Hurkacz win set 2 in the Hubert Hurkacz vs Arthur Gea match: 0.54/0.57 mid 55.5%, model 63.2% (Gen-1 ELO_DP_FAIR (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT02HURGEA-1-GEA` Will Arthur Gea win set 1 in the Hubert Hurkacz vs Arthur Gea match: 0.42/0.45 mid 43.5%, model 36.8% (Gen-1 ELO_DP_FAIR (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26OCT02HURGEA-1-HUR` Will Hubert Hurkacz win set 1 in the Hubert Hurkacz vs Arthur Gea match: 0.55/0.58 mid 56.5%, model 63.2% (Gen-1 ELO_DP_FAIR (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote STALE, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02HURGEA-HUR21` Will Hubert Hurkacz win the Hubert Hurkacz vs Arthur Gea match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 27.4% (market_conditioned_v1 (model4_board_v1)) -- gap +4.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02HURGEA-GEA20` Will Arthur Gea win the Hubert Hurkacz vs Arthur Gea match by a set score of 2-0?: 0.23/0.25 mid 24.0%, model 19.9% (market_conditioned_v1 (model4_board_v1)) -- gap -4.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02HURGEA-GEA21` Will Arthur Gea win the Hubert Hurkacz vs Arthur Gea match by a set score of 2-1?: 0.17/0.19 mid 18.0%, model 22.1% (market_conditioned_v1 (model4_board_v1)) -- gap +4.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02HURGEA-HUR20` Will Hubert Hurkacz win the Hubert Hurkacz vs Arthur Gea match by a set score of 2-0?: 0.34/0.35 mid 34.5%, model 30.6% (market_conditioned_v1 (model4_board_v1)) -- gap -3.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02HURGEA-HUR3` Will Hubert Hurkacz win at least 2.5 more games than Arthur Gea?: 0.45/0.46 mid 45.5%, model 41.8% (market_conditioned_v1 (model4_board_v1)) -- gap -3.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02HURGEA-18` Over 17.5 games: 0.89/0.94 mid 91.5%, model 95.0% (market_conditioned_v1 (model4_board_v1)) -- gap +3.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02HURGEA-HUR6` Will Hubert Hurkacz win at least 5.5 more games than Arthur Gea?: 0.04/0.21 mid 12.5%, model 9.3% (market_conditioned_v1 (model4_board_v1)) -- gap -3.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02HURGEA-GEA2` Will Arthur Gea win at least 1.5 more games than Hubert Hurkacz?: 0.35/0.38 mid 36.5%, model 34.4% (market_conditioned_v1 (model4_board_v1)) -- gap -2.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Filip Cristian Jianu vs Radu David Turcanu -- M25 Slobozia QF

ITF (ITF) · Clay · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202262:212886:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Cristian Jianu (`KXITFMATCH-26OCT02JIATUR-JIA`) | 0.62 / 0.64 (29) | 63.0% | 67.3% | 70.0% | 69.6% [69.1%-70.5%] | 61.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +6.6 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Radu David Turcanu (`KXITFMATCH-26OCT02JIATUR-TUR`) | 0.37 / 0.38 (3272) | 37.5% | 32.7% | 30.0% | 30.4% [29.5%-30.9%] | 38.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.1 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5523.0, B 2393.0; serve-point win A 61.6%, B 41.8%; Elo A 1599.3, B 1462.2; model uncertainty 0.0068
* Form inputs: days since last match A 11, B 123; matches on record A 710, B 70; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.005, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Filip Krolo vs Noah Lopez -- M15 Sibenik QF

ITF (ITF) · Clay · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210055:212593:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Krolo (`KXITFMATCH-26OCT02KROLOP-KRO`) | 0.43 / 0.44 (204) | 43.5% | 38.2% | 33.8% | 36.7% [33.3%-40.3%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Noah Lopez (`KXITFMATCH-26OCT02KROLOP-LOP`) | 0.55 / 0.57 (4055) | 56.0% | 61.8% | 66.2% | 63.3% [59.7%-66.7%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.3 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 442.0, B 1139.0; serve-point win A 58.7%, B 38.9%; Elo A 1120.9, B 1204.7; model uncertainty 0.0347
* Form inputs: days since last match A 235, B 137; matches on record A 26, B 116; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikita Mashtakov vs Jeffrey Von Der Schulenburg -- M15 Sibenik QF

ITF (ITF) · surface ? · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02MASVON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikita Mashtakov (`KXITFMATCH-26OCT02MASVON-MAS`) | 0.59 / 0.61 (4875) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeffrey Von Der Schulenburg (`KXITFMATCH-26OCT02MASVON-VON`) | 0.38 / 0.40 (89) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jakub Nicod vs Charles Bertimon -- M15 Sibenik QF

ITF (ITF) · Clay · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202293:210556:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charles Bertimon (`KXITFMATCH-26OCT02NICBER-BER`) | 0.16 / 0.18 (3753) | 17.0% | 12.3% | 5.3% | 8.3% [6.7%-11.0%] | -- | -- | -- | -- | PASS | -8.7 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jakub Nicod (`KXITFMATCH-26OCT02NICBER-NIC`) | 0.83 / 0.84 (2031) | 83.5% | 87.6% | 94.7% | 91.7% [89.0%-93.3%] | -- | -- | -- | -- | WATCH | +8.2 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1919.0, B 976.0; serve-point win A 64.4%, B 44.6%; Elo A 1548.3, B 1194.1; model uncertainty 0.0219
* Form inputs: days since last match A 123, B 165; matches on record A 152, B 38; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.017, surface_dev_loose +0.006, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Manuel Plunger vs Benjamin Lock -- M25 Kigali QF

ITF (ITF) · Clay · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:111761:211708:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Lock (`KXITFMATCH-26OCT02PLULOC-LOC`) | 0.47 / 0.49 (1) | 48.0% | 77.1% | 77.9% | 77.5% [73.5%-81.2%] | 48.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +29.5 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manuel Plunger (`KXITFMATCH-26OCT02PLULOC-PLU`) | 0.51 / 0.52 (5355) | 51.5% | 22.9% | 22.1% | 22.5% [18.9%-26.5%] | 51.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -29.0 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 330.0, B 4430.0; serve-point win A 57.0%, B 37.2%; Elo A 1234.2, B 1445.6; model uncertainty 0.0383
* Form inputs: days since last match A 130, B 676; matches on record A 42, B 700; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02PLULOC-LOC  (YES = Benjamin Lock)
Model: 78%
Kalshi: 48%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.036, surface_pool_high +0.040, surface_dev_loose -0.004, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Fares Zakaria vs Romain Faucon -- M15 Sharm ElSheikh QF

ITF (ITF) · surface ? · scheduled 2026-10-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02ZAKFAU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Romain Faucon (`KXITFMATCH-26OCT02ZAKFAU-FAU`) | 0.53 / 0.57 (4368) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fares Zakaria (`KXITFMATCH-26OCT02ZAKFAU-ZAK`) | 0.44 / 0.47 (1154) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexander Donski / Filip Pieczonka vs Daniel Cukierman / Fernando Romboli -- ATP Challenger Porto 2 SF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-02T14:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02DONPIECUKROM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Cukierman / Fernando Romboli (`KXATPCHALLENGERDOUBLES-26OCT02DONPIECUKROM-CUKROM`) | 0.40 / 0.50 (500) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Donski / Filip Pieczonka (`KXATPCHALLENGERDOUBLES-26OCT02DONPIECUKROM-DONPIE`) | 0.50 / 0.60 (500) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Cadence Brace vs Amandine Hesse -- W35 Baza QF

ITF (ITF) · Hard · scheduled 2026-10-02T14:15:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:203281:223335:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cadence Brace (`KXITFWMATCH-26OCT02BRAHES-BRA`) | 0.66 / 0.68 (4849) | 67.0% | 65.2% | 70.0% | 65.6% [56.4%-70.4%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.4 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amandine Hesse (`KXITFWMATCH-26OCT02BRAHES-HES`) | 0.32 / 0.35 (357) | 33.5% | 34.8% | 30.0% | 34.4% [29.6%-43.6%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.8 pp | NORMAL | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2165.0, B 2021.0; serve-point win A 57.2%, B 45.8%; Elo A 1646.6, B 1578.2; model uncertainty 0.0702
* Form inputs: days since last match A 16, B 82; matches on record A 222, B 777; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.024, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentina Ryser vs Charo Esquiva Banuls -- W35 Baza QF

ITF (ITF) · Hard · scheduled 2026-10-02T14:15:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220489:264962:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charo Esquiva Banuls (`KXITFWMATCH-26OCT02RYSESQ-ESQ`) | 0.57 / 0.60 (37) | 58.5% | 34.1% | 33.5% | 31.6% [27.9%-34.5%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -26.9 pp | EXTREME (DATA_WARNING) | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentina Ryser (`KXITFWMATCH-26OCT02RYSESQ-RYS`) | 0.40 / 0.43 (149) | 41.5% | 66.0% | 66.5% | 68.4% [65.5%-72.1%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +26.9 pp | EXTREME (DATA_WARNING) | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3017.0, B 1005.0; serve-point win A 57.2%, B 45.9%; Elo A 1607.9, B 1466.2; model uncertainty 0.033
* Form inputs: days since last match A 24, B 17; matches on record A 391, B 35; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02RYSESQ-RYS  (YES = Valentina Ryser)
Model: 68%
Kalshi: 42%
Gap: +27 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.028, surface_pool_high -0.029, surface_dev_loose +0.005, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bulte / Talic vs Beale / Vujic -- M25 Darwin SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02BULTALBEAVUJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beale / Vujic (`KXITFDOUBLES-26OCT02BULTALBEAVUJ-BEAVUJ`) | 0.36 / 0.42 (43) | 39.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bulte / Talic (`KXITFDOUBLES-26OCT02BULTALBEAVUJ-BULTAL`) | 0.56 / 0.63 (190) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Connel / Walters vs Bessonov / Gretskiy -- M15 Baku SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02CONWALBESGRE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bessonov / Gretskiy (`KXITFDOUBLES-26OCT02CONWALBESGRE-BESGRE`) | 0.07 / 0.67 (100) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Connel / Walters (`KXITFDOUBLES-26OCT02CONWALBESGRE-CONWAL`) | 0.07 / 0.78 (117) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Cook / Leonard Sach vs Hoeyeraal / Padgham -- M25 Darwin SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02COOLEOHOEPAD:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cook / Leonard Sach (`KXITFDOUBLES-26OCT02COOLEOHOEPAD-COOLEO`) | 0.07 / 0.78 (113) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hoeyeraal / Padgham (`KXITFDOUBLES-26OCT02COOLEOHOEPAD-HOEPAD`) | 0.18 / 0.40 (42) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Tuncay Duran vs Jack Loge -- M15 Monastir QF

ITF (ITF) · Hard · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210513:211504:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tuncay Duran (`KXITFMATCH-26OCT02DURLOG-DUR`) | 0.50 / 0.52 (4706) | 51.0% | 52.2% | 61.1% | 56.1% [46.9%-61.1%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +5.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jack Loge (`KXITFMATCH-26OCT02DURLOG-LOG`) | 0.48 / 0.49 (1626) | 48.5% | 47.8% | 38.9% | 43.9% [38.9%-53.1%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2317.0, B 3866.0; serve-point win A 62.8%, B 37.6%; Elo A 1432.2, B 1436.0; model uncertainty 0.0706
* Form inputs: days since last match A 60, B 60; matches on record A 116, B 191; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.040, surface_dev_loose +0.015, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kris van Wyk vs Liam Branger -- M15 Monastir QF

ITF (ITF) · Hard · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:144748:210605:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liam Branger (`KXITFMATCH-26OCT02VANBRA-BRA`) | 0.72 / 0.74 (100) | 73.0% | 58.1% | 77.3% | 62.7% [56.7%-67.5%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.3 pp | REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kris van Wyk (`KXITFMATCH-26OCT02VANBRA-VAN`) | 0.26 / 0.29 (3302) | 27.5% | 41.9% | 22.7% | 37.3% [32.5%-43.3%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +9.8 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2787.0, B 1201.0; serve-point win A 61.8%, B 36.6%; Elo A 1308.5, B 1301.4; model uncertainty 0.0538
* Form inputs: days since last match A 123, B 172; matches on record A 330, B 32; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.030, surface_dev_loose -0.010, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Polina Berezina vs Sophia Biolay -- W15 Monastir QF

ITF (ITF) · Hard · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221192:269754:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Berezina (`KXITFWMATCH-26OCT02BERBIO-BER`) | 0.27 / 0.28 (3647) | 27.5% | 38.1% | 7.7% | 36.4% [33.4%-38.4%] | 31.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sophia Biolay (`KXITFWMATCH-26OCT02BERBIO-BIO`) | 0.71 / 0.72 (1105) | 71.5% | 61.9% | 92.3% | 63.6% [61.6%-66.6%] | 68.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.9 pp | NORMAL | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 71.0, B 766.0; serve-point win A 54.5%, B 43.2%; Elo A 1376.6, B 1461.2; model uncertainty 0.025
* Form inputs: days since last match A 221, B 228; matches on record A 8, B 133; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.020, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lan Mi vs Jessica Hinojosa Gomez -- W15 Monastir QF

ITF (ITF) · Hard · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:213739:260141:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jessica Hinojosa Gomez (`KXITFWMATCH-26OCT02MIXHIN-HIN`) | 0.30 / 0.31 (4131) | 30.5% | 34.8% | 34.8% | 34.4% [32.4%-36.8%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.9 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lan Mi (`KXITFWMATCH-26OCT02MIXHIN-MIX`) | 0.68 / 0.70 (48) | 69.0% | 65.2% | 65.2% | 65.6% [63.2%-67.6%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.4 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2699.0, B 1620.0; serve-point win A 57.2%, B 45.8%; Elo A 1444.9, B 1322.6; model uncertainty 0.0222
* Form inputs: days since last match A 158, B 12; matches on record A 89, B 175; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.019, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giulia Safina Popa vs Oana Georgeta Simion -- W15 Varna QF

ITF (ITF) · Clay · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211646:267428:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giulia Safina Popa (`KXITFWMATCH-26OCT02POPSIM-POP`) | 0.64 / 0.67 (454) | 65.5% | 57.7% | 67.1% | 59.0% [53.7%-62.6%] | 63.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oana Georgeta Simion (`KXITFWMATCH-26OCT02POPSIM-SIM`) | 0.33 / 0.35 (3363) | 34.0% | 42.3% | 32.9% | 41.0% [37.4%-46.3%] | 36.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.0 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1013.0, B 1762.0; serve-point win A 54.7%, B 46.7%; Elo A 1546.3, B 1520.4; model uncertainty 0.0444
* Form inputs: days since last match A 368, B 179; matches on record A 38, B 543; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.000, surface_dev_loose +0.016, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marta Soriano Santiago vs Astrid Cirotte -- W15 Monastir QF

ITF (ITF) · Hard · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:236980:259105:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Astrid Cirotte (`KXITFWMATCH-26OCT02SORCIR-CIR`) | 0.43 / 0.46 (3120) | 44.5% | 47.9% | 43.1% | 45.2% [43.6%-46.8%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.7 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marta Soriano Santiago (`KXITFWMATCH-26OCT02SORCIR-SOR`) | 0.55 / 0.58 (1956) | 56.5% | 52.1% | 56.9% | 54.8% [53.2%-56.4%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.7 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1358.0, B 2379.0; serve-point win A 55.9%, B 44.5%; Elo A 1390.2, B 1366.7; model uncertainty 0.0158
* Form inputs: days since last match A 158, B 172; matches on record A 98, B 227; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.005, surface_dev_loose +0.016, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tara Wuerth vs Sonja Zhenikhova -- W15 Varna QF

ITF (ITF) · surface ? · scheduled 2026-10-02T14:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02WUEZHE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tara Wuerth (`KXITFWMATCH-26OCT02WUEZHE-WUE`) | 0.81 / 0.83 (1527) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sonja Zhenikhova (`KXITFWMATCH-26OCT02WUEZHE-ZHE`) | 0.17 / 0.19 (4179) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oleksandr Ovcharenko / Kai Wehnelt vs Gianluca Cadenasso / Massimo Giunta -- ATP Challenger Bari SF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-02T14:50:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02OVCWEHCADGIU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gianluca Cadenasso / Massimo Giunta (`KXATPCHALLENGERDOUBLES-26OCT02OVCWEHCADGIU-CADGIU`) | 0.06 / 0.80 (15) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oleksandr Ovcharenko / Kai Wehnelt (`KXATPCHALLENGERDOUBLES-26OCT02OVCWEHCADGIU-OVCWEH`) | 0.06 / 0.80 (15) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## August Holmgren vs Henrique Rocha -- ATP Challenger Porto 2 QF

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-02T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200416:210012:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| August Holmgren (`KXATPCHALLENGERMATCH-26OCT02HOLROC-HOL`) | 0.31 / 0.32 (8482) | 31.5% | 39.0% | 44.2% | 42.2% [40.3%-43.2%] | 32.3% | 31.3% | 31.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.8 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Henrique Rocha (`KXATPCHALLENGERMATCH-26OCT02HOLROC-ROC`) | 0.68 / 0.69 (200) | 68.5% | 61.0% | 55.8% | 57.8% [56.8%-59.7%] | 67.7% | 68.8% | 68.8% | MODEL_LONE_OUTLIER | PASS | -10.8 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5043.0, B 5037.0; serve-point win A 61.5%, B 36.3%; Elo A 1614.1, B 1721.6; model uncertainty 0.0145
* Form inputs: days since last match A 25, B 25; matches on record A 350, B 353; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose -0.009, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Dev Javia vs Calvin Hemery -- M25 Kigali QF

ITF (ITF) · Clay · scheduled 2026-10-02T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:123921:209956:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Calvin Hemery (`KXITFMATCH-26OCT02JAVHEM-HEM`) | 0.78 / 0.84 (216) | 81.0% | 78.1% | 67.5% | 76.4% [73.2%-83.6%] | -- | -- | -- | -- | PASS | -4.6 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dev Javia (`KXITFMATCH-26OCT02JAVHEM-JAV`) | 0.16 / 0.20 (380) | 18.0% | 21.9% | 32.5% | 23.6% [16.4%-26.8%] | -- | -- | -- | -- | WATCH | +5.6 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2032.0, B 5909.0; serve-point win A 56.9%, B 37.1%; Elo A 1359.7, B 1670.5; model uncertainty 0.052
* Form inputs: days since last match A 137, B 11; matches on record A 147, B 938; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.016, surface_dev_loose +0.012, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yshai Oliel vs Florent Bax -- M25 Kigali QF

ITF (ITF) · Clay · scheduled 2026-10-02T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200075:202147:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Florent Bax (`KXITFMATCH-26OCT02OLIBAX-BAX`) | 0.68 / 0.71 (819) | 69.5% | 77.2% | 93.6% | 79.2% [68.3%-85.8%] | 68.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.7 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yshai Oliel (`KXITFMATCH-26OCT02OLIBAX-OLI`) | 0.29 / 0.32 (416) | 30.5% | 22.8% | 6.4% | 20.8% [14.2%-31.7%] | 31.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.7 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 932.0, B 4639.0; serve-point win A 57.0%, B 37.2%; Elo A 1440.0, B 1549.8; model uncertainty 0.0875
* Form inputs: days since last match A 326, B 18; matches on record A 457, B 354; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.007, surface_dev_loose -0.014, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Borys Zgola vs Radu Mihai Papoe -- M25 Slobozia QF

ITF (ITF) · Clay · scheduled 2026-10-02T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208457:210169:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Radu Mihai Papoe (`KXITFMATCH-26OCT02ZGOPAP-PAP`) | 0.94 / 0.95 (2128) | 94.5% | 93.5% | 92.8% | 93.7% [91.9%-94.7%] | 92.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Borys Zgola (`KXITFMATCH-26OCT02ZGOPAP-ZGO`) | 0.05 / 0.06 (619) | 5.5% | 6.6% | 7.1% | 6.3% [5.3%-8.1%] | 7.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.8 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 63.0, B 3052.0; serve-point win A 54.0%, B 34.2%; Elo A 1118.3, B 1580.1; model uncertainty 0.0143
* Form inputs: days since last match A 193, B 46; matches on record A 14, B 190; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.018, surface_dev_loose -0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alicia Dudeney vs Katie Swan -- W75 Quinta do Lago QF

ITF (ITF) · Hard · scheduled 2026-10-02T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215042:260206:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alicia Dudeney (`KXITFWMATCH-26OCT02DUDSWA-DUD`) | 0.30 / 0.31 (3302) | 30.5% | 47.3% | 57.8% | 51.6% [43.2%-54.7%] | 33.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +21.1 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katie Swan (`KXITFWMATCH-26OCT02DUDSWA-SWA`) | 0.68 / 0.69 (114) | 68.5% | 52.6% | 42.2% | 48.4% [45.3%-56.8%] | 66.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.1 pp | HIGH_REVIEW | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3238.0, B 2343.0; serve-point win A 55.4%, B 44.1%; Elo A 1659.9, B 1720.0; model uncertainty 0.0577
* Form inputs: days since last match A 95, B 7; matches on record A 92, B 385; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02DUDSWA-DUD  (YES = Alicia Dudeney)
Model: 52%
Kalshi: 30%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose +0.011, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leolia Jeanjean vs Lucrezia Stefanini -- WTA 125K Adana QF

WTA125 (WTA_125) · surface ? · scheduled 2026-10-02T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:206417:214593:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leolia Jeanjean (`KXWTACHALLENGERMATCH-26OCT02JEASTE-JEA`) | 0.47 / 0.48 (7499) | 47.5% | 57.1% | 55.3% | 56.4% [55.9%-56.4%] | 48.0% | 47.4% | 47.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.9 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Lucrezia Stefanini (`KXWTACHALLENGERMATCH-26OCT02JEASTE-STE`) | 0.52 / 0.53 (4230) | 52.5% | 42.9% | 44.7% | 43.6% [43.6%-44.1%] | 52.0% | 52.7% | 52.7% | MODEL_LONE_OUTLIER | PASS | -8.9 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4130.0, B 4432.0; serve-point win A 57.7%, B 43.7%; Elo A 1916.9, B 1863.6; model uncertainty 0.0027
* Form inputs: days since last match A 2, B 2; matches on record A 438, B 605; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Sada Nahimana vs Diana Martynov -- W35 Reims QF

ITF (ITF) · Hard · scheduled 2026-10-02T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216367:221157:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diana Martynov (`KXITFWMATCH-26OCT02NAHMAR-MAR`) | 0.56 / 0.57 (8044) | 56.5% | 39.2% | 48.9% | 44.7% [40.5%-47.9%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.8 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sada Nahimana (`KXITFWMATCH-26OCT02NAHMAR-NAH`) | 0.44 / 0.45 (183) | 44.5% | 60.8% | 51.1% | 55.3% [52.1%-59.5%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.8 pp | REVIEW | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2636.0, B 1861.0; serve-point win A 56.7%, B 45.4%; Elo A 1540.8, B 1461.8; model uncertainty 0.0368
* Form inputs: days since last match A 135, B 26; matches on record A 369, B 331; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.005, surface_dev_loose -0.032, surface_dev_tight +0.032
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Margaux Rouvroy vs Susan Bandecchi -- W75 Quinta do Lago QF

ITF (ITF) · Hard · scheduled 2026-10-02T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214826:221191:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Susan Bandecchi (`KXITFWMATCH-26OCT02ROUBAN-BAN`) | 0.81 / 0.82 (1833) | 81.5% | 56.9% | 49.5% | 53.7% [50.5%-62.5%] | 81.4% | -- | 81.4% | MODEL_LONE_OUTLIER | PASS | -27.8 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Margaux Rouvroy (`KXITFWMATCH-26OCT02ROUBAN-ROU`) | 0.17 / 0.19 (5375) | 18.0% | 43.1% | 50.5% | 46.3% [37.5%-49.5%] | 18.6% | -- | 18.6% | MODEL_LONE_OUTLIER | WATCH | +28.3 pp | EXTREME (DATA_WARNING) | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3212.0, B 3884.0; serve-point win A 55.0%, B 43.7%; Elo A 1624.5, B 1714.3; model uncertainty 0.0599
* Form inputs: days since last match A 19, B 11; matches on record A 337, B 523; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02ROUBAN-ROU  (YES = Margaux Rouvroy)
Model: 46%
Kalshi: 18%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefan Latinovic / Mili Poljicak vs Alexandru Jecan / Szymon Kielan -- ATP Challenger Porto 2 SF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-02T15:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02LATPOLJECKIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandru Jecan / Szymon Kielan (`KXATPCHALLENGERDOUBLES-26OCT02LATPOLJECKIE-JECKIE`) | 0.30 / 0.40 (500) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stefan Latinovic / Mili Poljicak (`KXATPCHALLENGERDOUBLES-26OCT02LATPOLJECKIE-LATPOL`) | 0.60 / 0.70 (500) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Emilien Demanet vs Aziz Ouakaa -- M15 Monastir QF

ITF (ITF) · Hard · scheduled 2026-10-02T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200297:212598:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emilien Demanet (`KXITFMATCH-26OCT02DEMOUA-DEM`) | 0.64 / 0.66 (11) | 65.0% | 66.7% | 70.6% | 67.3% [62.4%-70.1%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aziz Ouakaa (`KXITFMATCH-26OCT02DEMOUA-OUA`) | 0.32 / 0.36 (76) | 34.0% | 33.3% | 29.4% | 32.7% [29.9%-37.6%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2543.0, B 3759.0; serve-point win A 64.3%, B 39.1%; Elo A 1429.3, B 1355.5; model uncertainty 0.0387
* Form inputs: days since last match A 60, B 53; matches on record A 142, B 450; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jeran / Kupcic vs Mavracic / Zuberbuehler -- M15 Sibenik SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02JERKUPMAVZUB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jeran / Kupcic (`KXITFDOUBLES-26OCT02JERKUPMAVZUB-JERKUP`) | 0.06 / 0.94 (2210) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mavracic / Zuberbuehler (`KXITFDOUBLES-26OCT02JERKUPMAVZUB-MAVZUB`) | 0.06 / 0.89 (600) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Lumsden / Nortey vs Nagoudi / Piatti -- M15 Monastir SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02LUMNORNAGPIA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lumsden / Nortey (`KXITFDOUBLES-26OCT02LUMNORNAGPIA-LUMNOR`) | 0.07 / 0.82 (1501) | 44.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nagoudi / Piatti (`KXITFDOUBLES-26OCT02LUMNORNAGPIA-NAGPIA`) | 0.13 / 0.63 (1600) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Mak Mikovic vs Martin VAN DER MEERSCHEN -- M15 Sibenik QF

ITF (ITF) · Clay · scheduled 2026-10-02T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207592:212951:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mak Mikovic (`KXITFMATCH-26OCT02MIKVAN-MIK`) | 0.15 / 0.17 (15) | 16.0% | 31.7% | 26.1% | 27.3% [25.1%-28.3%] | 17.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.3 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Martin VAN DER MEERSCHEN (`KXITFMATCH-26OCT02MIKVAN-VAN`) | 0.83 / 0.85 (3117) | 84.0% | 68.3% | 74.0% | 72.7% [71.7%-74.9%] | 82.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.3 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 608.0, B 2224.0; serve-point win A 58.1%, B 38.3%; Elo A 1195.3, B 1362.4; model uncertainty 0.016
* Form inputs: days since last match A 123, B 137; matches on record A 16, B 107; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.013, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lars Goran Verwerft vs Carles Hernandez -- M15 Monastir QF

ITF (ITF) · Hard · scheduled 2026-10-02T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208264:213121:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carles Hernandez (`KXITFMATCH-26OCT02VERHER-HER`) | 0.65 / 0.67 (0) | 66.0% | 48.4% | 28.8% | 44.3% [38.2%-53.1%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -21.7 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lars Goran Verwerft (`KXITFMATCH-26OCT02VERHER-VER`) | 0.32 / 0.34 (48) | 33.0% | 51.5% | 71.2% | 55.7% [46.9%-61.8%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +22.7 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 832.0, B 2103.0; serve-point win A 62.7%, B 37.6%; Elo A 1225.4, B 1251.7; model uncertainty 0.0746
* Form inputs: days since last match A 130, B 137; matches on record A 20, B 85; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02VERHER-VER  (YES = Lars Goran Verwerft)
Model: 56%
Kalshi: 33%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.015, surface_dev_loose +0.021, surface_dev_tight -0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bertacchi / Dibenedetto vs Bosman / Maloney -- W15 Monastir SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02BERDIBBOSMAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bertacchi / Dibenedetto (`KXITFWDOUBLES-26OCT02BERDIBBOSMAL-BERDIB`) | 0.10 / 0.74 (1531) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bosman / Maloney (`KXITFWDOUBLES-26OCT02BERDIBBOSMAL-BOSMAL`) | 0.22 / 0.82 (600) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Celia Cervino Ruiz vs Nahia Berecoechea -- W35 Baza QF

ITF (ITF) · Hard · scheduled 2026-10-02T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216078:222171:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nahia Berecoechea (`KXITFWMATCH-26OCT02CERBER-BER`) | 0.64 / 0.68 (1111) | 66.0% | 63.9% | 68.1% | 66.6% [63.6%-68.1%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.6 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Celia Cervino Ruiz (`KXITFWMATCH-26OCT02CERBER-CER`) | 0.32 / 0.35 (80) | 33.5% | 36.1% | 31.9% | 33.4% [31.9%-36.4%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.1 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1450.0, B 1894.0; serve-point win A 54.3%, B 43.0%; Elo A 1439.1, B 1547.8; model uncertainty 0.0223
* Form inputs: days since last match A 10, B 172; matches on record A 265, B 250; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Valentina Losciale vs Ekaterina Dotsenko -- W15 Monastir QF

ITF (ITF) · surface ? · scheduled 2026-10-02T15:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02LOSDOT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Dotsenko (`KXITFWMATCH-26OCT02LOSDOT-DOT`) | 0.83 / 0.86 (58) | 84.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Valentina Losciale (`KXITFWMATCH-26OCT02LOSDOT-LOS`) | 0.13 / 0.17 (4059) | 15.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Adrian Andreescu / Claudiu Schinteie vs Florin Breazu / Cristian Breazu -- M25 Slobozia SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02ADRCLAFLOCRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Andreescu / Claudiu Schinteie (`KXITFDOUBLES-26OCT02ADRCLAFLOCRI-ADRCLA`) | 0.07 / 0.68 (1) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Florin Breazu / Cristian Breazu (`KXITFDOUBLES-26OCT02ADRCLAFLOCRI-FLOCRI`) | 0.06 / 0.65 (2) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Francisca Jorge vs Eva Vedder -- W75 Quinta do Lago QF

ITF (ITF) · Hard · scheduled 2026-10-02T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216055:220770:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisca Jorge (`KXITFWMATCH-26OCT02JORVED-JOR`) | 0.54 / 0.55 (622) | 54.5% | 56.5% | 64.4% | 62.9% [57.4%-64.8%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +8.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eva Vedder (`KXITFWMATCH-26OCT02JORVED-VED`) | 0.46 / 0.47 (3150) | 46.5% | 43.5% | 35.6% | 37.1% [35.1%-42.6%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3145.0, B 3271.0; serve-point win A 56.3%, B 44.9%; Elo A 1652.2, B 1586.1; model uncertainty 0.0375
* Form inputs: days since last match A 10, B 17; matches on record A 457, B 432; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Manon Leonard vs Isis Louise Van den Broek -- W35 Reims QF

ITF (ITF) · Hard · scheduled 2026-10-02T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215807:264227:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manon Leonard (`KXITFWMATCH-26OCT02LEOVAN-LEO`) | 0.64 / 0.66 (37) | 65.0% | 53.4% | 56.9% | 57.4% [52.7%-60.0%] | 65.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.6 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Isis Louise Van den Broek (`KXITFWMATCH-26OCT02LEOVAN-VAN`) | 0.34 / 0.35 (840) | 34.5% | 46.6% | 43.1% | 42.6% [40.0%-47.3%] | 34.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +8.1 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3201.0, B 1856.0; serve-point win A 56.0%, B 44.6%; Elo A 1629.8, B 1579.5; model uncertainty 0.0369
* Form inputs: days since last match A 109, B 158; matches on record A 347, B 103; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.032, surface_pool_high +0.026, surface_dev_loose +0.000, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lisa Pigato vs Polona Hercog -- W75 Quinta do Lago QF

ITF (ITF) · Hard · scheduled 2026-10-02T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:201555:221354:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polona Hercog (`KXITFWMATCH-26OCT02PIGHER-HER`) | 0.29 / 0.30 (85) | 29.5% | 44.5% | 39.6% | 42.7% [41.1%-44.2%] | 32.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.2 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lisa Pigato (`KXITFWMATCH-26OCT02PIGHER-PIG`) | 0.69 / 0.71 (2072) | 70.0% | 55.5% | 60.4% | 57.3% [55.8%-58.9%] | 67.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.7 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4114.0, B 2590.0; serve-point win A 56.2%, B 44.8%; Elo A 1654.6, B 1647.9; model uncertainty 0.0156
* Form inputs: days since last match A 13, B 11; matches on record A 353, B 863; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.016, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isabella Maria Serban vs Britt Du Pree -- W35 Reims QF

ITF (ITF) · Hard · scheduled 2026-10-02T16:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:264228:265197:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Britt Du Pree (`KXITFWMATCH-26OCT02SERDUP-DUP`) | 0.73 / 0.76 (876) | 74.5% | 68.5% | 81.2% | 75.7% [66.1%-79.0%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.2 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Isabella Maria Serban (`KXITFWMATCH-26OCT02SERDUP-SER`) | 0.24 / 0.27 (67) | 25.5% | 31.5% | 18.8% | 24.3% [21.1%-33.9%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.2 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2134.0, B 2691.0; serve-point win A 53.9%, B 42.5%; Elo A 1459.0, B 1580.2; model uncertainty 0.0642
* Form inputs: days since last match A 9, B 158; matches on record A 114, B 85; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.008, surface_dev_loose -0.020, surface_dev_tight +0.026
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jerome Kym vs Edas Butvilas -- ATP Challenger Porto 2 QF

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-02T16:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208843:210220:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edas Butvilas (`KXATPCHALLENGERMATCH-26OCT02KYMBUT-BUT`) | 0.45 / 0.47 (5133) | 46.0% | 46.0% | 46.6% | 47.5% [46.5%-49.0%] | -- | 46.8% | 46.8% | MODEL_LONE_OUTLIER | PASS | +1.5 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Jerome Kym (`KXATPCHALLENGERMATCH-26OCT02KYMBUT-KYM`) | 0.53 / 0.54 (1630) | 53.5% | 54.0% | 53.4% | 52.5% [51.0%-53.5%] | -- | 53.6% | 53.6% | MODEL_LONE_OUTLIER | PASS | -1.0 pp | NORMAL | STALE | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3926.0, B 5196.0; serve-point win A 63.0%, B 37.8%; Elo A 1694.4, B 1695.1; model uncertainty 0.0123
* Form inputs: days since last match A 31, B 11; matches on record A 311, B 293; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Antonia Ruzic vs Teodora Kostovic -- WTA 125K Adana QF

WTA125 (WTA_125) · surface ? · scheduled 2026-10-02T16:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222045:267439:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Teodora Kostovic (`KXWTACHALLENGERMATCH-26OCT02RUZKOS-KOS`) | 0.46 / 0.47 (12010) | 46.5% | 40.0% | 50.0% | 43.7% [37.0%-46.8%] | 45.9% | 47.2% | 47.2% | MODEL_LONE_OUTLIER | PASS | -2.8 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Antonia Ruzic (`KXWTACHALLENGERMATCH-26OCT02RUZKOS-RUZ`) | 0.53 / 0.54 (3705) | 53.5% | 60.0% | 50.0% | 56.3% [53.2%-63.0%] | 54.1% | 53.1% | 53.1% | MODEL_LONE_OUTLIER | WATCH | +2.8 pp | NORMAL | STALE | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4066.0, B 3286.0; serve-point win A 58.0%, B 44.0%; Elo A 1883.9, B 1738.1; model uncertainty 0.0492
* Form inputs: days since last match A 2, B 2; matches on record A 358, B 110; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Beckley / Sahtali vs Nefve / Schachter -- M25 Kigali SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02BECSAHNEFSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beckley / Sahtali (`KXITFDOUBLES-26OCT02BECSAHNEFSCH-BECSAH`) | 0.17 / 0.50 (3) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nefve / Schachter (`KXITFDOUBLES-26OCT02BECSAHNEFSCH-NEFSCH`) | 0.16 / 0.67 (100) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Denolly / Plunger vs Gatoto / Shalin Shah -- M25 Kigali SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02DENPLUGATSHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Denolly / Plunger (`KXITFDOUBLES-26OCT02DENPLUGATSHA-DENPLU`) | 0.12 / 0.87 (2) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gatoto / Shalin Shah (`KXITFDOUBLES-26OCT02DENPLUGATSHA-GATSHA`) | 0.15 / 0.68 (100) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Clement Tabur vs Sascha Gueymard Wayenburg -- ATP Challenger Mouilleron-Le-Captif QF

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-02T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:202127:209849:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sascha Gueymard Wayenburg (`KXATPCHALLENGERMATCH-26OCT02TABGUE-GUE`) | 0.58 / 0.59 (11441) | 58.5% | -- | 44.1% | 46.1% [44.1%-48.0%] | 58.4% | 59.2% | 59.2% | MODEL_LONE_OUTLIER | PASS | -12.4 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Clement Tabur (`KXATPCHALLENGERMATCH-26OCT02TABGUE-TAB`) | 0.41 / 0.42 (3900) | 41.5% | -- | 55.9% | 53.9% [52.0%-55.9%] | 41.6% | 41.0% | 41.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +12.4 pp | REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5131.0, B 4960.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0196
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Mair / Peer vs Elena Barbulescu / Wanja Brune Olsen -- W15 Varna SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02MAIPEEELEWAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elena Barbulescu / Wanja Brune Olsen (`KXITFWDOUBLES-26OCT02MAIPEEELEWAN-ELEWAN`) | 0.07 / 0.77 (100) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mair / Peer (`KXITFWDOUBLES-26OCT02MAIPEEELEWAN-MAIPEE`) | 0.07 / 0.55 (2) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sakellaridi / Vilar vs Andrienko / Georgiana Goina -- W15 Varna SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T16:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02SAKVILANDGEO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrienko / Georgiana Goina (`KXITFWDOUBLES-26OCT02SAKVILANDGEO-ANDGEO`) | 0.41 / 0.88 (43) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sakellaridi / Vilar (`KXITFWDOUBLES-26OCT02SAKVILANDGEO-SAKVIL`) | 0.21 / 0.59 (1) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nicolas Ifi vs Ryan Nijboer -- M25 Zaragoza QF

ITF (ITF) · Clay · scheduled 2026-10-02T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:207764:212552:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Ifi (`KXITFMATCH-26OCT02IFINIJ-IFI`) | 0.18 / 0.19 (4912) | 18.5% | 23.3% | 23.4% | 21.5% [20.7%-23.3%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.0 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ryan Nijboer (`KXITFMATCH-26OCT02IFINIJ-NIJ`) | 0.81 / 0.83 (1772) | 82.0% | 76.7% | 76.6% | 78.5% [76.7%-79.3%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.5 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1923.0, B 4005.0; serve-point win A 57.1%, B 37.3%; Elo A 1239.5, B 1482.5; model uncertainty 0.013
* Form inputs: days since last match A 130, B 11; matches on record A 78, B 484; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose +0.001, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mariano Kestelboim / Marcelo Zormann vs Samuel Heredia / Miguel Tobon -- ATP Challenger Curitiba SF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-02T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02KESZORHERTOB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samuel Heredia / Miguel Tobon (`KXATPCHALLENGERDOUBLES-26OCT02KESZORHERTOB-HERTOB`) | 0.06 / 0.80 (15) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mariano Kestelboim / Marcelo Zormann (`KXATPCHALLENGERDOUBLES-26OCT02KESZORHERTOB-KESZOR`) | 0.06 / 0.80 (15) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Lopez Martos / Palomar vs Garcia Mestre / Naharro -- M25 Zaragoza SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02LOPPALGARNAH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Garcia Mestre / Naharro (`KXITFDOUBLES-26OCT02LOPPALGARNAH-GARNAH`) | 0.08 / 0.93 (100) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lopez Martos / Palomar (`KXITFDOUBLES-26OCT02LOPPALGARNAH-LOPPAL`) | 0.06 / 0.94 (209) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Matheus Pucinelli de Almeida vs Marcelo Tomas Barrios Vera -- ATP Challenger Curitiba QF

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-02T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02PDABAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcelo Tomas Barrios Vera (`KXATPCHALLENGERMATCH-26OCT02PDABAR-BAR`) | 0.52 / 0.53 (7199) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matheus Pucinelli de Almeida (`KXATPCHALLENGERMATCH-26OCT02PDABAR-PDA`) | 0.47 / 0.48 (16010) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Valentina Ivanov vs Juliana Giaccio -- W35 Baza QF

ITF (ITF) · Hard · scheduled 2026-10-02T17:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221173:269835:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juliana Giaccio (`KXITFWMATCH-26OCT02IVAGIA-GIA`) | 0.39 / 0.42 (3104) | 40.5% | 19.4% | 8.5% | 14.2% [10.2%-20.7%] | 40.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -26.3 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentina Ivanov (`KXITFWMATCH-26OCT02IVAGIA-IVA`) | 0.59 / 0.61 (168) | 60.0% | 80.5% | 91.5% | 85.8% [79.3%-89.8%] | 59.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +25.8 pp | EXTREME (DATA_WARNING) | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1892.0, B 776.0; serve-point win A 58.9%, B 47.6%; Elo A 1496.4, B 1236.6; model uncertainty 0.0524
* Form inputs: days since last match A 165, B 193; matches on record A 135, B 22; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02IVAGIA-IVA  (YES = Valentina Ivanov)
Model: 86%
Kalshi: 60%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.012, surface_pool_high +0.009, surface_dev_loose +0.020, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Biletic / Kajin vs Mashtakov / Savano -- M15 Sibenik SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02BILKAJMASSAV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Biletic / Kajin (`KXITFDOUBLES-26OCT02BILKAJMASSAV-BILKAJ`) | 0.47 / 0.93 (1113) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mashtakov / Savano (`KXITFDOUBLES-26OCT02BILKAJMASSAV-MASSAV`) | 0.08 / 0.53 (600) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Matthew William Donald vs Martin Krumich -- ATP Challenger Bari QF

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-02T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:209322:210054:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew William Donald (`KXATPCHALLENGERMATCH-26OCT02DONKRU-DON`) | 0.33 / 0.34 (304) | 33.5% | -- | 39.1% | 35.1% [33.2%-36.6%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.6 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Martin Krumich (`KXATPCHALLENGERMATCH-26OCT02DONKRU-KRU`) | 0.65 / 0.67 (8375) | 66.0% | -- | 60.9% | 64.9% [63.4%-66.8%] | 65.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.1 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2929.0, B 5732.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.017
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Mitchell Krueger vs Keegan Smith -- ATP Challenger Columbus QF

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-02T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106283:202333:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mitchell Krueger (`KXATPCHALLENGERMATCH-26OCT02KRUSMI-KRU`) | 0.44 / 0.45 (3303) | 44.5% | -- | 32.5% | 37.0% [33.4%-44.6%] | 45.9% | -- | 45.9% | MODEL_LONE_OUTLIER | PASS | -7.5 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Keegan Smith (`KXATPCHALLENGERMATCH-26OCT02KRUSMI-SMI`) | 0.54 / 0.56 (3651) | 55.0% | -- | 67.5% | 63.0% [55.4%-66.6%] | 54.1% | -- | 54.1% | MODEL_LONE_OUTLIER | WATCH | +8.0 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5011.0, B 5491.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.056
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.027, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Opitz / Wessels vs Adrian Boitan / Andrei Golescu -- M25 Slobozia SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02OPIWESADRAND:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Boitan / Andrei Golescu (`KXITFDOUBLES-26OCT02OPIWESADRAND-ADRAND`) | 0.08 / 0.55 (8) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Opitz / Wessels (`KXITFDOUBLES-26OCT02OPIWESADRAND-OPIWES`) | 0.33 / 0.90 (0) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mees Rottgering vs Andres Andrade -- ATP Challenger Columbus QF

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-02T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:200748:212219:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andres Andrade (`KXATPCHALLENGERMATCH-26OCT02ROTAND-AND`) | 0.39 / 0.41 (5941) | 40.0% | -- | 46.4% | 48.4% [45.8%-52.6%] | 40.8% | 41.3% | 41.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.4 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Mees Rottgering (`KXATPCHALLENGERMATCH-26OCT02ROTAND-ROT`) | 0.59 / 0.60 (381) | 59.5% | -- | 53.6% | 51.6% [47.4%-54.2%] | 59.2% | 60.3% | 60.3% | MODEL_LONE_OUTLIER | PASS | -7.9 pp | NORMAL | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2398.0, B 4672.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0338
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.010, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Akli / Brantmeier vs Collins / Tanguilig -- W75 Quinta do Lago F

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T18:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02AKLBRACOLTAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Akli / Brantmeier (`KXITFWDOUBLES-26OCT02AKLBRACOLTAN-AKLBRA`) | 0.07 / 0.76 (108) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Collins / Tanguilig (`KXITFWDOUBLES-26OCT02AKLBRACOLTAN-COLTAN`) | 0.09 / 0.73 (8) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Duran / Ouakaa vs Branger / Dugardin -- M15 Monastir SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02DUROUABRADUG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Branger / Dugardin (`KXITFDOUBLES-26OCT02DUROUABRADUG-BRADUG`) | 0.06 / 0.79 (1) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Duran / Ouakaa (`KXITFDOUBLES-26OCT02DUROUABRADUG-DUROUA`) | 0.06 / 0.73 (3) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kroitor / Mi vs Biolay / Cirotte -- W15 Monastir SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02KROMIXBIOCIR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Biolay / Cirotte (`KXITFWDOUBLES-26OCT02KROMIXBIOCIR-BIOCIR`) | 0.08 / 0.52 (2) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kroitor / Mi (`KXITFWDOUBLES-26OCT02KROMIXBIOCIR-KROMIX`) | 0.06 / 0.64 (2) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lorenzo Carboni vs Sander Jong -- M25 Zaragoza QF

ITF (ITF) · Clay · scheduled 2026-10-02T19:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210093:212077:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Carboni (`KXITFMATCH-26OCT02CARJON-CAR`) | 0.36 / 0.39 (4998) | 37.5% | 46.7% | 36.4% | 44.3% [40.3%-50.0%] | 38.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +6.8 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sander Jong (`KXITFMATCH-26OCT02CARJON-JON`) | 0.61 / 0.64 (27) | 62.5% | 53.3% | 63.6% | 55.7% [50.0%-59.7%] | 61.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.8 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3666.0, B 1938.0; serve-point win A 59.6%, B 39.8%; Elo A 1505.1, B 1478.4; model uncertainty 0.0485
* Form inputs: days since last match A 32, B 117; matches on record A 186, B 134; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexander Ritschard vs Miguel Damas -- M25 Zaragoza QF

ITF (ITF) · Clay · scheduled 2026-10-02T19:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106310:207732:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miguel Damas (`KXITFMATCH-26OCT02RITDAM-DAM`) | 0.26 / 0.30 (28) | 28.0% | 30.9% | 31.1% | 29.3% [27.9%-30.2%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.3 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Ritschard (`KXITFMATCH-26OCT02RITDAM-RIT`) | 0.69 / 0.72 (3) | 70.5% | 69.2% | 68.9% | 70.7% [69.8%-72.1%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3172.0, B 5726.0; serve-point win A 61.8%, B 42.0%; Elo A 1773.1, B 1584.0; model uncertainty 0.0117
* Form inputs: days since last match A 25, B 25; matches on record A 681, B 410; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose +0.014, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Darwin Blanch vs Dylan Dietrich -- ATP Challenger Columbus QF

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-02T19:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210157:210464:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Darwin Blanch (`KXATPCHALLENGERMATCH-26OCT02BLADIE-BLA`) | 0.41 / 0.42 (2587) | 41.5% | -- | 39.8% | 52.4% [46.6%-59.8%] | 42.8% | 44.4% | 43.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.9 pp | REVIEW | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Dylan Dietrich (`KXATPCHALLENGERMATCH-26OCT02BLADIE-DIE`) | 0.58 / 0.59 (5569) | 58.5% | -- | 60.2% | 47.5% [40.2%-53.4%] | 57.2% | 58.5% | 57.9% | MODEL_LONE_OUTLIER | PASS | -10.9 pp | REVIEW | STALE | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3993.0, B 1313.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0661
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; STALE_QUOTE

## Abdullah Shelbayh vs Aidan Mayo -- ATP Challenger Columbus QF

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-02T19:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02SHEMAY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aidan Mayo (`KXATPCHALLENGERMATCH-26OCT02SHEMAY-MAY`) | 0.45 / 0.46 (2494) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Abdullah Shelbayh (`KXATPCHALLENGERMATCH-26OCT02SHEMAY-SHE`) | 0.54 / 0.55 (2981) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Pedro Boscardin Dias vs Luis Guto Miguel -- ATP Challenger Curitiba QF

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-02T19:15:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208046:213036:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Boscardin Dias (`KXATPCHALLENGERMATCH-26OCT02BOSMIG-BOS`) | 0.46 / 0.47 (6280) | 46.5% | -- | 28.5% | 54.1% [44.4%-66.9%] | -- | -- | -- | -- | WATCH | +7.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luis Guto Miguel (`KXATPCHALLENGERMATCH-26OCT02BOSMIG-MIG`) | 0.53 / 0.54 (70) | 53.5% | -- | 71.5% | 45.9% [33.1%-55.6%] | -- | -- | -- | -- | PASS | -7.6 pp | NORMAL | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4852.0, B 1185.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1128
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose -0.021, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE

## Guido Ivan Justo vs Gonzalo Villanueva -- ATP Challenger Curitiba QF

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-02T19:15:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:106380:207815:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guido Ivan Justo (`KXATPCHALLENGERMATCH-26OCT02JUSVIL-JUS`) | 0.61 / 0.62 (73) | 61.5% | -- | 68.7% | 66.3% [64.4%-67.8%] | -- | -- | -- | -- | SHADOW_BET | +4.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gonzalo Villanueva (`KXATPCHALLENGERMATCH-26OCT02JUSVIL-VIL`) | 0.38 / 0.39 (3460) | 38.5% | -- | 31.3% | 33.7% [32.2%-35.6%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4964.0, B 5724.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.017
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.010, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE

## Henry Bernet vs Felix Balshaw -- ATP Challenger Mouilleron-Le-Captif QF

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-02T19:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:148679:213149:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felix Balshaw (`KXATPCHALLENGERMATCH-26OCT02BERBAL-BAL`) | 0.47 / 0.48 (3845) | 47.5% | -- | 78.8% | 71.7% [69.1%-75.0%] | 46.9% | 47.0% | 47.0% | MODEL_LONE_OUTLIER | WATCH | +24.2 pp | HIGH_REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Henry Bernet (`KXATPCHALLENGERMATCH-26OCT02BERBAL-BER`) | 0.52 / 0.53 (1356) | 52.5% | -- | 21.2% | 28.3% [25.0%-30.9%] | 53.1% | 53.4% | 53.4% | MODEL_LONE_OUTLIER | PASS | -24.2 pp | HIGH_REVIEW | STALE | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2182.0, B 4079.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0293
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT02BERBAL-BAL  (YES = Felix Balshaw)
Model: 72%
Kalshi: 48%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.017, surface_dev_loose -0.029, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE

## Tessa Johanna Brockmann vs Salma Djoubri -- W35 Reims QF

ITF (ITF) · Hard · scheduled 2026-10-02T19:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220305:260598:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tessa Johanna Brockmann (`KXITFWMATCH-26OCT02BRODJO-BRO`) | 0.74 / 0.75 (1) | 74.5% | 67.4% | 72.6% | 68.0% [64.6%-71.3%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Salma Djoubri (`KXITFWMATCH-26OCT02BRODJO-DJO`) | 0.24 / 0.25 (3120) | 24.5% | 32.6% | 27.4% | 32.0% [28.7%-35.4%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.5 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3426.0, B 169.0; serve-point win A 57.4%, B 46.0%; Elo A 1593.9, B 1467.4; model uncertainty 0.0334
* Form inputs: days since last match A 23, B 319; matches on record A 171, B 168; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.033, surface_pool_high -0.034, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Dahlin vs Damir Zhalgasbay -- M15 Ann Arbor MI QF

ITF (ITF) · Hard · scheduled 2026-10-02T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:211609:212846:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Dahlin (`KXITFMATCH-26OCT02DAHZHA-DAH`) | 0.70 / 0.72 (4345) | 71.0% | 82.3% | 78.5% | 82.1% [80.4%-83.2%] | 70.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.1 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Damir Zhalgasbay (`KXITFMATCH-26OCT02DAHZHA-ZHA`) | 0.28 / 0.31 (57) | 29.5% | 17.7% | 21.5% | 17.9% [16.9%-19.6%] | 29.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.6 pp | REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 583.0, B 222.0; serve-point win A 66.3%, B 41.1%; Elo A 1424.0, B 1156.7; model uncertainty 0.014
* Form inputs: days since last match A 67, B 158; matches on record A 41, B 6; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.017, surface_dev_loose +0.002, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## John Hallquist Lithen vs Naoto Tomizawa -- M15 Ann Arbor MI QF

ITF (ITF) · Hard · scheduled 2026-10-02T20:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:208925:214236:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| John Hallquist Lithen (`KXITFMATCH-26OCT02HALTOM-HAL`) | 0.72 / 0.75 (1226) | 73.5% | 62.8% | 78.1% | 63.4% [61.3%-65.9%] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.1 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Naoto Tomizawa (`KXITFMATCH-26OCT02HALTOM-TOM`) | 0.25 / 0.27 (4832) | 26.0% | 37.2% | 21.9% | 36.6% [34.1%-38.7%] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +10.6 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2695.0, B 62.0; serve-point win A 63.9%, B 38.7%; Elo A 1354.3, B 1263.2; model uncertainty 0.0227
* Form inputs: days since last match A 130, B 340; matches on record A 94, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Brandon Carpico / Nikita Samuel Filin vs Alexander Ikenna Okonkwo / Preston Stearns -- ATP Challenger Columbus SF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-02T20:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02CARFILOKOSTE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brandon Carpico / Nikita Samuel Filin (`KXATPCHALLENGERDOUBLES-26OCT02CARFILOKOSTE-CARFIL`) | 0.06 / 0.80 (15) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Ikenna Okonkwo / Preston Stearns (`KXATPCHALLENGERDOUBLES-26OCT02CARFILOKOSTE-OKOSTE`) | 0.06 / 0.80 (15) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Daniel Milavsky / Braden Shick vs Alex Rybakov / Keegan Smith -- ATP Challenger Columbus SF

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-02T20:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02MILSHIRYBSMI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Milavsky / Braden Shick (`KXATPCHALLENGERDOUBLES-26OCT02MILSHIRYBSMI-MILSHI`) | 0.06 / 0.80 (15) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alex Rybakov / Keegan Smith (`KXATPCHALLENGERDOUBLES-26OCT02MILSHIRYBSMI-RYBSMI`) | 0.06 / 0.80 (15) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Oliver Bonding vs Nikola Djosic -- M15 Ann Arbor MI QF

ITF (ITF) · Hard · scheduled 2026-10-02T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:212149:212839:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oliver Bonding (`KXITFMATCH-26OCT02BONDJO-BON`) | 0.87 / 0.91 (2) | 89.0% | 66.4% | 70.8% | 70.4% [68.5%-72.2%] | 88.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -18.6 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nikola Djosic (`KXITFMATCH-26OCT02BONDJO-DJO`) | 0.08 / 0.11 (37) | 9.5% | 33.6% | 29.2% | 29.6% [27.8%-31.6%] | 11.7% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +20.1 pp | HIGH_REVIEW | STALE | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1207.0, B 1313.0; serve-point win A 64.3%, B 39.1%; Elo A 1440.2, B 1289.1; model uncertainty 0.0186
* Form inputs: days since last match A 39, B 130; matches on record A 42, B 39; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02BONDJO-DJO  (YES = Nikola Djosic)
Model: 30%
Kalshi: 10%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.013, surface_dev_loose +0.014, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hugo Coquelin vs Olaf Pieczkowski -- M15 Ann Arbor MI QF

ITF (ITF) · Hard · scheduled 2026-10-02T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210142:213042:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Coquelin (`KXITFMATCH-26OCT02COQPIE-COQ`) | 0.28 / 0.31 (44) | 29.5% | 28.7% | 16.1% | 25.9% [21.8%-28.5%] | 30.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Olaf Pieczkowski (`KXITFMATCH-26OCT02COQPIE-PIE`) | 0.66 / 0.73 (151) | 69.5% | 71.3% | 83.9% | 74.1% [71.5%-78.2%] | 69.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.6 pp | NORMAL | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 446.0, B 2433.0; serve-point win A 60.4%, B 35.2%; Elo A 1277.2, B 1435.1; model uncertainty 0.0335
* Form inputs: days since last match A 123, B 60; matches on record A 17, B 234; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.041, surface_pool_high +0.026, surface_dev_loose -0.009, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Johan Alexander Rodriguez vs Jonah Braswell -- M15 Fayetteville AR QF

ITF (ITF) · surface ? · scheduled 2026-10-02T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02RODBRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonah Braswell (`KXITFMATCH-26OCT02RODBRA-BRA`) | 0.30 / 0.34 (34) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Johan Alexander Rodriguez (`KXITFMATCH-26OCT02RODBRA-ROD`) | 0.66 / 0.70 (4) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexander Rozin vs Hoyoung Roh -- M15 Fayetteville AR QF

ITF (ITF) · surface ? · scheduled 2026-10-02T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02ROZROH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hoyoung Roh (`KXITFMATCH-26OCT02ROZROH-ROH`) | 0.49 / 0.53 (3348) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Rozin (`KXITFMATCH-26OCT02ROZROH-ROZ`) | 0.49 / 0.51 (20) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alvin Nicholas Tudorica vs Dominick Mosejczuk -- M15 Fayetteville AR QF

ITF (ITF) · Hard · scheduled 2026-10-02T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:212202:213771:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dominick Mosejczuk (`KXITFMATCH-26OCT02TUDMOS-MOS`) | 0.64 / 0.69 (4751) | 66.5% | -- | 53.1% | 34.8% [32.0%-37.7%] | -- | -- | -- | -- | PASS | -31.7 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alvin Nicholas Tudorica (`KXITFMATCH-26OCT02TUDMOS-TUD`) | 0.31 / 0.34 (17) | 32.5% | -- | 46.9% | 65.2% [62.3%-68.0%] | -- | -- | -- | -- | PASS | +32.7 pp | EXTREME (DATA_WARNING) | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1789.0, B 379.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0288
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT02TUDMOS-TUD  (YES = Alvin Nicholas Tudorica)
Model: 65%
Kalshi: 32%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.024, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Leyla Fiorella Britez Risso vs Liv Zingg -- W15 Trelew QF

ITF (ITF) · surface ? · scheduled 2026-10-02T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02BRIZIN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leyla Fiorella Britez Risso (`KXITFWMATCH-26OCT02BRIZIN-BRI`) | 0.85 / 0.86 (0) | 85.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liv Zingg (`KXITFWMATCH-26OCT02BRIZIN-ZIN`) | 0.13 / 0.15 (5) | 14.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luciana Moyano vs Pilar Da Silva -- W15 Trelew QF

ITF (ITF) · surface ? · scheduled 2026-10-02T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02MOYDAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pilar Da Silva (`KXITFWMATCH-26OCT02MOYDAS-DAS`) | 0.05 / 0.95 (164) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luciana Moyano (`KXITFWMATCH-26OCT02MOYDAS-MOY`) | 0.05 / 0.95 (242) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Meneses Perny / Perez socas vs Ifi / Stanke -- M25 Zaragoza SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T21:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02MENPERIFISTA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ifi / Stanke (`KXITFDOUBLES-26OCT02MENPERIFISTA-IFISTA`) | 0.06 / 0.94 (210) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Meneses Perny / Perez socas (`KXITFDOUBLES-26OCT02MENPERIFISTA-MENPER`) | 0.06 / 0.94 (210) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Arcila / Rozin vs Boland / Smillie -- M15 Fayetteville AR SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02ARCROZBOLSMI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arcila / Rozin (`KXITFDOUBLES-26OCT02ARCROZBOLSMI-ARCROZ`) | 0.06 / 0.94 (210) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Boland / Smillie (`KXITFDOUBLES-26OCT02ARCROZBOLSMI-BOLSMI`) | 0.06 / 0.94 (210) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Alejandro Moro Canas vs Pedro Vives Marcos -- M25 Zaragoza QF

ITF (ITF) · Clay · scheduled 2026-10-02T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:206325:208279:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alejandro Moro Canas (`KXITFMATCH-26OCT02MORVIV-MOR`) | 0.68 / 0.71 (7340) | 69.5% | 55.8% | 53.1% | 56.7% [52.1%-63.3%] | 68.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.8 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Pedro Vives Marcos (`KXITFMATCH-26OCT02MORVIV-VIV`) | 0.29 / 0.31 (227) | 30.0% | 44.2% | 46.9% | 43.3% [36.7%-47.9%] | 31.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +13.3 pp | REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6297.0, B 1642.0; serve-point win A 60.5%, B 40.7%; Elo A 1639.8, B 1566.4; model uncertainty 0.0559
* Form inputs: days since last match A 18, B 32; matches on record A 426, B 212; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.031, surface_dev_loose -0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Theo Papamalamis vs Aryan Shah -- M15 Fayetteville AR QF

ITF (ITF) · Hard · scheduled 2026-10-02T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:210494:211325:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Papamalamis (`KXITFMATCH-26OCT02PAPSHA-PAP`) | 0.55 / 0.59 (174) | 57.0% | -- | 59.3% | 53.1% [48.4%-55.7%] | -- | -- | -- | -- | PASS | -3.9 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aryan Shah (`KXITFMATCH-26OCT02PAPSHA-SHA`) | 0.41 / 0.45 (69) | 43.0% | -- | 40.7% | 46.9% [44.3%-51.6%] | -- | -- | -- | -- | PASS | +3.9 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1643.0, B 2442.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0364
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.016, surface_dev_tight -0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Roddick / Tokac vs Chavez / Melero Kretzer -- M15 Fayetteville AR SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02RODTOKCHAMEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chavez / Melero Kretzer (`KXITFDOUBLES-26OCT02RODTOKCHAMEL-CHAMEL`) | 0.06 / 0.94 (210) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Roddick / Tokac (`KXITFDOUBLES-26OCT02RODTOKCHAMEL-RODTOK`) | 0.06 / 0.94 (210) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Coppez / Tran vs Im / Kim -- W35 Reims F

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02COPTRAIMXKIM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coppez / Tran (`KXITFWDOUBLES-26OCT02COPTRAIMXKIM-COPTRA`) | 0.06 / 0.90 (50) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Im / Kim (`KXITFWDOUBLES-26OCT02COPTRAIMXKIM-IMXKIM`) | 0.06 / 0.90 (50) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Meabe / Florencia Urrutia vs Ailin Larraya Guidi / Sousa Salazar -- W15 Trelew SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02MEAFLOAILSOU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ailin Larraya Guidi / Sousa Salazar (`KXITFWDOUBLES-26OCT02MEAFLOAILSOU-AILSOU`) | 0.06 / 0.90 (50) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Meabe / Florencia Urrutia (`KXITFWDOUBLES-26OCT02MEAFLOAILSOU-MEAFLO`) | 0.06 / 0.90 (50) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Milovanovic / Novak vs Hietaranta / Zelnickova -- W35 Baza F

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02MILNOVHIEZEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hietaranta / Zelnickova (`KXITFWDOUBLES-26OCT02MILNOVHIEZEL-HIEZEL`) | 0.06 / 0.76 (1) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Milovanovic / Novak (`KXITFWDOUBLES-26OCT02MILNOVHIEZEL-MILNOV`) | 0.06 / 0.71 (3) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ana Sofia Sanchez vs Lourdes Ayala -- W15 Trelew QF

ITF (ITF) · Hard · scheduled 2026-10-02T22:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:204419:236968:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lourdes Ayala (`KXITFWMATCH-26OCT02SANAYA-AYA`) | 0.07 / 0.09 (29) | 8.0% | 12.4% | 6.9% | 9.3% [7.9%-11.6%] | 9.3% | -- | 9.3% | MARKETS_AGREE | PASS | +1.3 pp | NORMAL | STALE | C / LIMITED | ALL_AGREE | VERIFIED |
| Ana Sofia Sanchez (`KXITFWMATCH-26OCT02SANAYA-SAN`) | 0.91 / 0.93 (281) | 92.0% | 87.6% | 93.1% | 90.7% [88.4%-92.1%] | 90.7% | -- | 90.7% | MARKETS_AGREE | PASS | -1.3 pp | NORMAL | STALE | C / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3191.0, B 813.0; serve-point win A 60.0%, B 48.7%; Elo A 1573.4, B 1215.8; model uncertainty 0.0188
* Form inputs: days since last match A 20, B 186; matches on record A 856, B 105; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high -0.014, surface_dev_loose +0.004, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Azar / Cairo vs Sheldon / Swenson -- M15 Ann Arbor MI SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02AZACAISHESWE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Azar / Cairo (`KXITFDOUBLES-26OCT02AZACAISHESWE-AZACAI`) | 0.06 / 0.94 (210) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sheldon / Swenson (`KXITFDOUBLES-26OCT02AZACAISHESWE-SHESWE`) | 0.06 / 0.94 (210) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Fradkin / Kuhar vs Burnett / Tomizawa -- M15 Ann Arbor MI SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-02T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `ATP:26OCT02FRAKUHBURTOM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Burnett / Tomizawa (`KXITFDOUBLES-26OCT02FRAKUHBURTOM-BURTOM`) | 0.06 / 0.92 (100) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fradkin / Kuhar (`KXITFDOUBLES-26OCT02FRAKUHBURTOM-FRAKUH`) | 0.06 / 0.94 (210) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Emily Zornada vs Maria Florencia Urrutia -- W15 Trelew QF

ITF (ITF) · Hard · scheduled 2026-10-02T23:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220447:270329:2026-10-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Florencia Urrutia (`KXITFWMATCH-26OCT02ZORURR-URR`) | 0.05 / 0.95 (164) | 50.0% | -- | 73.2% | 74.9% [74.0%-75.7%] | -- | -- | -- | -- | PASS | +24.9 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Emily Zornada (`KXITFWMATCH-26OCT02ZORURR-ZOR`) | 0.05 / 0.95 (242) | 50.0% | -- | 26.8% | 25.1% [24.3%-26.0%] | -- | -- | -- | -- | PASS | -24.9 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 106.0, B 2454.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0084
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02ZORURR-URR  (YES = Maria Florencia Urrutia)
Model: 75%
Kalshi: 50%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.009, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tatjana Maria vs Malaika Rapolu -- W100 Templeton CA QF

ITF (ITF) · Hard · scheduled 2026-10-03T00:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:213583:222837:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tatjana Maria (`KXITFWMATCH-26OCT02MARRAP-MAR`) | 0.72 / 0.74 (4134) | 73.0% | -- | 15.3% | 37.0% [23.2%-68.9%] | -- | -- | -- | -- | PASS | -36.0 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Malaika Rapolu (`KXITFWMATCH-26OCT02MARRAP-RAP`) | 0.26 / 0.28 (36) | 27.0% | -- | 84.7% | 63.0% [31.1%-76.8%] | -- | -- | -- | -- | PASS | +36.0 pp | EXTREME (DATA_WARNING) | STALE | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4444.0, B 1761.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.2284
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02MARRAP-RAP  (YES = Malaika Rapolu)
Model: 63%
Kalshi: 27%
Gap: +36 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: STALE_KALSHI_QUOTE, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.062, surface_pool_high -0.059, surface_dev_loose -0.030, surface_dev_tight +0.036
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ella McDonald vs Kristina Penickova -- W100 Templeton CA QF

ITF (ITF) · Hard · scheduled 2026-10-03T00:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:259591:266381:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ella McDonald (`KXITFWMATCH-26OCT02MCDPEN-MCD`) | 0.58 / 0.60 (201) | 59.0% | -- | 58.4% | 60.5% [59.5%-61.5%] | -- | -- | -- | -- | PASS | +1.5 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kristina Penickova (`KXITFWMATCH-26OCT02MCDPEN-PEN`) | 0.39 / 0.42 (63) | 40.5% | -- | 41.6% | 39.5% [38.5%-40.6%] | -- | -- | -- | -- | PASS | -1.0 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1341.0, B 1178.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0105
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Moyano / Sofia Sanchez vs Ayala / Fiorella Britez Risso -- W15 Trelew SF

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T00:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02MOYSOFAYAFIO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayala / Fiorella Britez Risso (`KXITFWDOUBLES-26OCT02MOYSOFAYAFIO-AYAFIO`) | 0.06 / 0.90 (50) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Moyano / Sofia Sanchez (`KXITFWDOUBLES-26OCT02MOYSOFAYAFIO-MOYSOF`) | 0.06 / 0.90 (50) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Madison Brengle vs Amelie Van Impe -- W100 Templeton CA QF

ITF (ITF) · Hard · scheduled 2026-10-03T01:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:201483:228909:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madison Brengle (`KXITFWMATCH-26OCT02BREVAN-BRE`) | 0.68 / 0.69 (1) | 68.5% | -- | 67.6% | 75.3% [72.3%-78.5%] | -- | -- | -- | -- | WATCH | +6.8 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amelie Van Impe (`KXITFWMATCH-26OCT02BREVAN-VAN`) | 0.28 / 0.31 (13) | 29.5% | -- | 32.4% | 24.7% [21.4%-27.7%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2464.0, B 1949.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0314
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose +0.021, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ashton Bowers vs Chiara Di Genova -- W15 Nashville TN QF

ITF (ITF) · surface ? · scheduled 2026-10-03T02:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221414:248665:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashton Bowers (`KXITFWMATCH-26OCT02BOWDIG-BOW`) | 0.75 / 0.79 (4) | 77.0% | -- | 49.5% | 64.6% [64.6%-64.6%] | -- | -- | -- | -- | PASS | -12.4 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chiara Di Genova (`KXITFWMATCH-26OCT02BOWDIG-DIG`) | 0.19 / 0.23 (25) | 21.0% | -- | 50.5% | 35.4% [35.4%-35.4%] | -- | -- | -- | -- | PASS | +14.4 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 146.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Caroline Dolehide vs Julieta Pareja -- W100 Templeton CA QF

ITF (ITF) · Hard · scheduled 2026-10-03T02:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214452:264075:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caroline Dolehide (`KXITFWMATCH-26OCT02DOLPAR-DOL`) | 0.05 / 0.95 (164) | 50.0% | -- | 61.0% | 59.4% [57.4%-62.5%] | -- | -- | -- | -- | PASS | +9.4 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julieta Pareja (`KXITFWMATCH-26OCT02DOLPAR-PAR`) | 0.05 / 0.95 (142) | 50.0% | -- | 39.1% | 40.6% [37.5%-42.6%] | -- | -- | -- | -- | PASS | -9.4 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3771.0, B 1273.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0258
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.021, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rose Marie Nijkamp vs Emma Kamper -- W15 Nashville TN QF

ITF (ITF) · surface ? · scheduled 2026-10-03T02:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:241715:260225:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emma Kamper (`KXITFWMATCH-26OCT02NIJKAM-KAM`) | 0.61 / 0.66 (155) | 63.5% | -- | 64.2% | 40.4% [33.4%-47.3%] | -- | -- | -- | -- | PASS | -23.1 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rose Marie Nijkamp (`KXITFWMATCH-26OCT02NIJKAM-NIJ`) | 0.34 / 0.39 (42) | 36.5% | -- | 35.8% | 59.6% [52.7%-66.6%] | -- | -- | -- | -- | PASS | +23.1 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1080.0, B 510.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0697
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02NIJKAM-NIJ  (YES = Rose Marie Nijkamp)
Model: 60%
Kalshi: 36%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Merna Refaat vs Carlota Moreno -- W15 Nashville TN QF

ITF (ITF) · surface ? · scheduled 2026-10-03T02:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221473:270436:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlota Moreno (`KXITFWMATCH-26OCT02REFMOR-MOR`) | 0.41 / 0.45 (1323) | 43.0% | -- | 66.6% | 59.0% [57.4%-62.1%] | -- | -- | -- | -- | PASS | +16.0 pp | HIGH_REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Merna Refaat (`KXITFWMATCH-26OCT02REFMOR-REF`) | 0.53 / 0.58 (3267) | 55.5% | -- | 33.4% | 41.0% [37.9%-42.6%] | -- | -- | -- | -- | PASS | -14.5 pp | REVIEW | STALE | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 556.0, B 350.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0235
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02REFMOR-MOR  (YES = Carlota Moreno)
Model: 59%
Kalshi: 43%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Astra Sharma vs Ashley Lahey -- W15 Nashville TN QF

ITF (ITF) · surface ? · scheduled 2026-10-03T03:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:206292:216076:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashley Lahey (`KXITFWMATCH-26OCT02SHALAH-LAH`) | 0.29 / 0.32 (37) | 30.5% | -- | 57.8% | 49.5% [40.6%-53.1%] | -- | -- | -- | -- | PASS | +19.0 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Astra Sharma (`KXITFWMATCH-26OCT02SHALAH-SHA`) | 0.67 / 0.71 (3) | 69.0% | -- | 42.2% | 50.5% [46.9%-59.4%] | -- | -- | -- | -- | PASS | -18.5 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2800.0, B 1883.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0627
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02SHALAH-LAH  (YES = Ashley Lahey)
Model: 49%
Kalshi: 30%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carlos Alcaraz vs Matteo Arnaldi -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-03T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207989:208286:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlos Alcaraz (`KXATPMATCH-26OCT02ALCARN-ALC`) | 0.94 / 0.95 (29827) | 94.5% | -- | 97.4% | 96.7% [94.2%-97.2%] | 92.7% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +2.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matteo Arnaldi (`KXATPMATCH-26OCT02ALCARN-ARN`) | 0.05 / 0.06 (8897) | 5.5% | -- | 2.6% | 3.3% [2.8%-5.8%] | 7.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.2 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 7542.0, B 6406.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0148
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.001, surface_pool_high -0.001, surface_dev_loose +0.003, surface_dev_tight -0.004
* Derivatives listed: 13 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 9 carry a model probability
  * `KXATPGSPREAD-26OCT02ALCARN-ALC10` Will Carlos Alcaraz win at least 9.5 more games than Matteo Arnaldi?: 0.01/0.99 mid 50.0%, model 2.6% (market_conditioned_v1 (model4_board_v1)) -- gap -47.4 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02ALCARN-19` Over 18.5 games: 0.49/0.50 mid 49.5%, model 62.7% (market_conditioned_v1 (model4_board_v1)) -- gap +13.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02ALCARN-ALC7` Will Carlos Alcaraz win at least 6.5 more games than Matteo Arnaldi?: 0.40/0.41 mid 40.5%, model 30.7% (market_conditioned_v1 (model4_board_v1)) -- gap -9.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02ALCARN-ALC21` Will Carlos Alcaraz win the Carlos Alcaraz vs Matteo Arnaldi match by a set score of 2-1?: 0.13/0.15 mid 14.0%, model 21.5% (market_conditioned_v1 (model4_board_v1)) -- gap +7.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02ALCARN-ALC20` Will Carlos Alcaraz win the Carlos Alcaraz vs Matteo Arnaldi match by a set score of 2-0?: 0.77/0.79 mid 78.0%, model 72.5% (market_conditioned_v1 (model4_board_v1)) -- gap -5.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02ALCARN-24` Over 23.5 games: 0.18/0.26 mid 22.0%, model 27.3% (market_conditioned_v1 (model4_board_v1)) -- gap +5.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02ALCARN-ALC4` Will Carlos Alcaraz win at least 3.5 more games than Matteo Arnaldi?: 0.82/0.87 mid 84.5%, model 79.5% (market_conditioned_v1 (model4_board_v1)) -- gap -5.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Matteo Berrettini vs Adolfo Daniel Vallejo -- ATP Tokyo R16

ATP (TOUR_500_250) · Hard · scheduled 2026-10-03T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126610:209226:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Berrettini (`KXATPMATCH-26OCT02BERVAL-BER`) | 0.60 / 0.61 (15360) | 60.5% | -- | 63.2% | 68.2% [66.0%-73.0%] | 59.4% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +7.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Adolfo Daniel Vallejo (`KXATPMATCH-26OCT02BERVAL-VAL`) | 0.40 / 0.41 (20635) | 40.5% | -- | 36.8% | 31.8% [27.0%-34.1%] | 40.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.7 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4565.0, B 5913.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0354
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.018, surface_dev_loose -0.000, surface_dev_tight -0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGSPREAD-26OCT02BERVAL-BER6` Will Matteo Berrettini win at least 5.5 more games than Adolfo Daniel Vallejo?: 0.01/0.99 mid 50.0%, model 11.8% (market_conditioned_v1 (model4_board_v1)) -- gap -38.2 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02BERVAL-28` Over 27.5 games: 0.26/0.33 mid 29.5%, model 40.6% (market_conditioned_v1 (model4_board_v1)) -- gap +11.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02BERVAL-23` Over 22.5 games: 0.49/0.51 mid 50.0%, model 60.9% (market_conditioned_v1 (model4_board_v1)) -- gap +10.8 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02BERVAL-BER21` Will Matteo Berrettini win the Matteo Berrettini vs Adolfo Daniel Vallejo match by a set score of 2-1?: 0.21/0.24 mid 22.5%, model 27.8% (market_conditioned_v1 (model4_board_v1)) -- gap +5.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02BERVAL-18` Over 17.5 games: 0.83/0.95 mid 89.0%, model 93.6% (market_conditioned_v1 (model4_board_v1)) -- gap +4.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02BERVAL-VAL21` Will Adolfo Daniel Vallejo win the Matteo Berrettini vs Adolfo Daniel Vallejo match by a set score of 2-1?: 0.16/0.19 mid 17.5%, model 21.3% (market_conditioned_v1 (model4_board_v1)) -- gap +3.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02BERVAL-BER20` Will Matteo Berrettini win the Matteo Berrettini vs Adolfo Daniel Vallejo match by a set score of 2-0?: 0.33/0.38 mid 35.5%, model 32.0% (market_conditioned_v1 (model4_board_v1)) -- gap -3.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02BERVAL-VAL20` Will Adolfo Daniel Vallejo win the Matteo Berrettini vs Adolfo Daniel Vallejo match by a set score of 2-0?: 0.20/0.24 mid 22.0%, model 18.9% (market_conditioned_v1 (model4_board_v1)) -- gap -3.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02BERVAL-BER3` Will Matteo Berrettini win at least 2.5 more games than Adolfo Daniel Vallejo?: 0.46/0.48 mid 47.0%, model 44.6% (market_conditioned_v1 (model4_board_v1)) -- gap -2.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02BERVAL-VAL2` Will Adolfo Daniel Vallejo win at least 1.5 more games than Matteo Berrettini?: 0.33/0.37 mid 35.0%, model 33.0% (market_conditioned_v1 (model4_board_v1)) -- gap -2.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Francisco Cerundolo vs Jakub Mensik -- ATP Beijing R16

ATP (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:202103:210150:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cerundolo (`KXATPMATCH-26OCT02CERMEN-CER`) | 0.34 / 0.36 (2179) | 35.0% | -- | 49.5% | 45.0% [42.5%-47.5%] | 36.8% | -- | 36.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +10.0 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jakub Mensik (`KXATPMATCH-26OCT02CERMEN-MEN`) | 0.64 / 0.66 (28056) | 65.0% | -- | 50.5% | 55.0% [52.5%-57.5%] | 63.2% | -- | 63.2% | MODEL_LONE_OUTLIER | PASS | -10.0 pp | NORMAL | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 6448.0, B 5037.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0249
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.020, surface_dev_loose -0.005, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT02CERMEN-23` Over 22.5 games: 0.48/0.50 mid 49.0%, model 58.4% (market_conditioned_v1 (model4_board_v1)) -- gap +9.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02CERMEN-28` Over 27.5 games: 0.26/0.34 mid 30.0%, model 38.2% (market_conditioned_v1 (model4_board_v1)) -- gap +8.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02CERMEN-MEN21` Will Jakub Mensik win the Francisco Cerundolo vs Jakub Mensik match by a set score of 2-1?: 0.20/0.25 mid 22.5%, model 28.8% (market_conditioned_v1 (model4_board_v1)) -- gap +6.3 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02CERMEN-MEN6` Will Jakub Mensik win at least 5.5 more games than Francisco Cerundolo?: 0.16/0.23 mid 19.5%, model 15.6% (market_conditioned_v1 (model4_board_v1)) -- gap -3.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02CERMEN-18` Over 17.5 games: 0.82/0.94 mid 88.0%, model 91.9% (market_conditioned_v1 (model4_board_v1)) -- gap +3.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02CERMEN-CER21` Will Francisco Cerundolo win the Francisco Cerundolo vs Jakub Mensik match by a set score of 2-1?: 0.13/0.19 mid 16.0%, model 19.2% (market_conditioned_v1 (model4_board_v1)) -- gap +3.2 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02CERMEN-MEN20` Will Jakub Mensik win the Francisco Cerundolo vs Jakub Mensik match by a set score of 2-0?: 0.36/0.42 mid 39.0%, model 35.9% (market_conditioned_v1 (model4_board_v1)) -- gap -3.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02CERMEN-CER20` Will Francisco Cerundolo win the Francisco Cerundolo vs Jakub Mensik match by a set score of 2-0?: 0.17/0.21 mid 19.0%, model 16.1% (market_conditioned_v1 (model4_board_v1)) -- gap -3.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02CERMEN-MEN3` Will Jakub Mensik win at least 2.5 more games than Francisco Cerundolo?: 0.52/0.54 mid 53.0%, model 50.3% (market_conditioned_v1 (model4_board_v1)) -- gap -2.7 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02CERMEN-CER2` Will Francisco Cerundolo win at least 1.5 more games than Jakub Mensik?: 0.23/0.32 mid 27.5%, model 28.6% (market_conditioned_v1 (model4_board_v1)) -- gap +1.1 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Andrey Rublev vs Roman Safiullin -- ATP Beijing R16

ATP (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126094:126128:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrey Rublev (`KXATPMATCH-26OCT02RUBSAF-RUB`) | 0.55 / 0.57 (20895) | 56.0% | -- | 66.8% | 65.4% [63.6%-67.2%] | 55.6% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +9.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Roman Safiullin (`KXATPMATCH-26OCT02RUBSAF-SAF`) | 0.43 / 0.45 (30021) | 44.0% | -- | 33.2% | 34.6% [32.8%-36.4%] | 44.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6741.0, B 4566.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0183
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.018, surface_dev_loose -0.005, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT02RUBSAF-20` Over 19.5 games: 0.70/0.77 mid 73.5%, model 82.3% (market_conditioned_v1 (model4_board_v1)) -- gap +8.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02RUBSAF-25` Over 24.5 games: 0.45/0.47 mid 46.0%, model 54.0% (market_conditioned_v1 (model4_board_v1)) -- gap +8.0 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02RUBSAF-30` Over 29.5 games: 0.21/0.29 mid 25.0%, model 32.4% (market_conditioned_v1 (model4_board_v1)) -- gap +7.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02RUBSAF-RUB21` Will Andrey Rublev win the Andrey Rublev vs Roman Safiullin match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 26.8% (market_conditioned_v1 (model4_board_v1)) -- gap +4.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02RUBSAF-RUB5` Will Andrey Rublev win at least 4.5 more games than Roman Safiullin?: 0.21/0.25 mid 23.0%, model 18.6% (market_conditioned_v1 (model4_board_v1)) -- gap -4.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02RUBSAF-SAF21` Will Roman Safiullin win the Andrey Rublev vs Roman Safiullin match by a set score of 2-1?: 0.17/0.20 mid 18.5%, model 22.9% (market_conditioned_v1 (model4_board_v1)) -- gap +4.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02RUBSAF-RUB20` Will Andrey Rublev win the Andrey Rublev vs Roman Safiullin match by a set score of 2-0?: 0.30/0.35 mid 32.5%, model 29.1% (market_conditioned_v1 (model4_board_v1)) -- gap -3.4 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02RUBSAF-SAF20` Will Roman Safiullin win the Andrey Rublev vs Roman Safiullin match by a set score of 2-0?: 0.22/0.26 mid 24.0%, model 21.2% (market_conditioned_v1 (model4_board_v1)) -- gap -2.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02RUBSAF-RUB2` Will Andrey Rublev win at least 1.5 more games than Roman Safiullin?: 0.49/0.51 mid 50.0%, model 48.2% (market_conditioned_v1 (model4_board_v1)) -- gap -1.8 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02RUBSAF-SAF2` Will Roman Safiullin win at least 1.5 more games than Andrey Rublev?: 0.33/0.39 mid 36.0%, model 36.6% (market_conditioned_v1 (model4_board_v1)) -- gap +0.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Xinyu Gao vs Iga Swiatek -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214386:216347:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xinyu Gao (`KXWTAMATCH-26OCT02GAOSWI-GAO`) | 0.05 / 0.06 (3249) | 5.5% | -- | 8.1% | 7.5% [6.6%-8.7%] | 5.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +2.0 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Iga Swiatek (`KXWTAMATCH-26OCT02GAOSWI-SWI`) | 0.93 / 0.95 (625) | 94.0% | -- | 91.9% | 92.5% [91.3%-93.4%] | 94.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.5 pp | NORMAL | STALE | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3203.0, B 4863.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0105
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.010, surface_dev_loose +0.006, surface_dev_tight -0.005
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT02GAOSWI-17` Over 16.5 games: 0.44/0.50 mid 47.0%, model 76.4% (market_conditioned_v1 (model4_board_v1)) -- gap +29.4 pp, EXTREME, DATA_WARNING, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT02GAOSWI-22` Over 21.5 games: 0.07/0.21 mid 14.0%, model 33.6% (market_conditioned_v1 (model4_board_v1)) -- gap +19.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote STALE, identity VERIFIED, data LIMITED
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Coco Gauff vs Camila Osorio -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215785:221103:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coco Gauff (`KXWTAMATCH-26OCT02GAUOSO-GAU`) | 0.90 / 0.91 (3824) | 90.5% | -- | 78.1% | 81.1% [79.7%-84.2%] | -- | -- | -- | -- | PASS | -9.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Camila Osorio (`KXWTAMATCH-26OCT02GAUOSO-OSO`) | 0.09 / 0.10 (9749) | 9.5% | -- | 21.9% | 18.9% [15.8%-20.3%] | -- | -- | -- | -- | SHADOW_BET | +9.4 pp | NORMAL | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5157.0, B 4356.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0227
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.007, surface_dev_loose -0.007, surface_dev_tight +0.007
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT02GAUOSO-19` Over 18.5 games: 0.48/0.50 mid 49.0%, model 60.1% (market_conditioned_v1 (model4_board_v1)) -- gap +11.1 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT02GAUOSO-24` Over 23.5 games: 0.20/0.29 mid 24.5%, model 31.4% (market_conditioned_v1 (model4_board_v1)) -- gap +6.9 pp, NORMAL, OK, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: NO_EXTERNAL_PRICE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Iva Jovic vs Harriet Dart -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211279:260300:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Harriet Dart (`KXWTAMATCH-26OCT02JOVDAR-DAR`) | 0.10 / 0.11 (8688) | 10.5% | -- | 34.0% | 30.7% [28.0%-32.1%] | 12.3% | -- | 12.3% | MODEL_LONE_OUTLIER | WATCH | +20.2 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Iva Jovic (`KXWTAMATCH-26OCT02JOVDAR-JOV`) | 0.89 / 0.90 (209) | 89.5% | -- | 66.0% | 69.3% [67.9%-72.0%] | 87.7% | -- | 87.7% | MODEL_LONE_OUTLIER | PASS | -20.2 pp | HIGH_REVIEW | STALE | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3602.0, B 4244.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0208
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT02JOVDAR-DAR  (YES = Harriet Dart)
Model: 31%
Kalshi: 10%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, EXTERNAL_MARKET_REJECTION
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.004, surface_dev_tight +0.000
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 2 carry a model probability
  * `KXWTAGTOTAL-26OCT02JOVDAR-19` Over 18.5 games: 0.47/0.49 mid 48.0%, model 63.0% (market_conditioned_v1 (model4_board_v1)) -- gap +15.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT02JOVDAR-24` Over 23.5 games: 0.16/0.30 mid 23.0%, model 33.2% (market_conditioned_v1 (model4_board_v1)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: STALE_QUOTE; WIDE_SPREAD

## Xinran Sun vs Cristina Bucsa -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213710:270082:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Bucsa (`KXWTAMATCH-26OCT02SUNBUC-BUC`) | 0.65 / 0.66 (3579) | 65.5% | -- | 41.5% | 66.6% [53.7%-81.0%] | 61.6% | -- | 61.6% | ALL_THREE_DISAGREE | PASS | +1.1 pp | NORMAL | STALE | C / LIMITED | ALL_AGREE | VERIFIED |
| Xinran Sun (`KXWTAMATCH-26OCT02SUNBUC-SUN`) | 0.34 / 0.35 (65) | 34.5% | -- | 58.5% | 33.4% [19.0%-46.3%] | 38.4% | -- | 38.4% | ALL_THREE_DISAGREE | PASS | -1.1 pp | NORMAL | STALE | C / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1001.0, B 4493.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1365
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.030, surface_dev_loose +0.015, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT02SUNBUC-22` Over 21.5 games: 0.42/0.54 mid 48.0%, model 59.5% (market_conditioned_v1 (model4_board_v1)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT02SUNBUC-27` Over 26.5 games: 0.20/0.33 mid 26.5%, model 36.5% (market_conditioned_v1 (model4_board_v1)) -- gap +10.0 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT02SUNBUC-17` Over 16.5 games: 0.79/0.91 mid 85.0%, model 91.6% (market_conditioned_v1 (model4_board_v1)) -- gap +6.6 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
* Warnings: LOW_DATA_QUALITY; STALE_QUOTE; WIDE_SPREAD

## Donna Vekic vs Lin Zhu -- WTA Beijing R64

WTA (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202499:202684:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Donna Vekic (`KXWTAMATCH-26OCT02VEKZHU-VEK`) | 0.60 / 0.62 (7727) | 61.0% | -- | 32.3% | 40.2% [34.2%-57.8%] | 60.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.8 pp | HIGH_REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lin Zhu (`KXWTAMATCH-26OCT02VEKZHU-ZHU`) | 0.38 / 0.39 (3450) | 38.5% | -- | 67.7% | 59.8% [42.2%-65.8%] | 39.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +21.3 pp | HIGH_REVIEW | STALE | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4044.0, B 3182.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1179
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26OCT02VEKZHU-ZHU  (YES = Lin Zhu)
Model: 60%
Kalshi: 38%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.036, surface_pool_high -0.035, surface_dev_loose -0.020, surface_dev_tight +0.025
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT02VEKZHU-23` Over 22.5 games: 0.43/0.44 mid 43.5%, model 55.9% (market_conditioned_v1 (model4_board_v1)) -- gap +12.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT02VEKZHU-28` Over 27.5 games: 0.17/0.30 mid 23.5%, model 34.7% (market_conditioned_v1 (model4_board_v1)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26OCT02VEKZHU-18` Over 17.5 games: 0.73/0.83 mid 78.0%, model 88.4% (market_conditioned_v1 (model4_board_v1)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data ADEQUATE
* Warnings: EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
