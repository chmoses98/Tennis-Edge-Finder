# ASSISTED SLATE -- 2026-10-03T10:14Z (`SL-20261003T101435Z-95212bce`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

115 open matches not seen started, 402 markets. Skipped: {"scheduled_start_over_24h_past": 4, "first_ball_already_observed": 5}. Sources: shadow board 2026-10-03T05:44:10.695635+00:00, Model 4 2026-10-02T22:36:37.419280+00:00, Gen-1 ledger 2026-10-03T05:44:07.349269+00:00, external 2026-10-03T09:49:26.873643+00:00, capture 20261003T095817Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-10-03 11:00Z**
* Recommended RUN TENNIS time: **2026-10-03 10:15Z**
* Final price/status check time: **2026-10-03 10:50Z**
* Number of matches in window: 1 (Francisco Cerundolo vs Jakub Mensik)

* **5 main-tour match(es) have NO verified start status** (START_UNKNOWN, STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-10-03T10:14Z. Refresh due by: 2026-10-03 10:15Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 9, "HIGH_REVIEW": 17, "NORMAL": 53, "REVIEW": 20, "UNPRICED": 303}; match winners: {"EXTREME": 9, "HIGH_REVIEW": 16, "NORMAL": 33, "REVIEW": 18, "UNPRICED": 154}; quote freshness at build: {"AGING": 94, "STALE": 5}.

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
| Yujia Huang (`KXWTACHALLENGERMATCH-26OCT02HUAKHO-HUA`) | 0.50 / 0.51 (1260) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Darya Khomutsianskaya (`KXWTACHALLENGERMATCH-26OCT02HUAKHO-KHO`) | 0.49 / 0.50 (136) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Kanon Sawashiro vs Naho Sato -- W35 Wagga Wagga SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 09:15Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T09:15:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220997:263905:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naho Sato (`KXITFWMATCH-26OCT02SAWSAT-SAT`) | 0.81 / 0.82 (60) | 81.5% | 53.8% | 38.4% | 57.5% [51.6%-63.7%] | -- | -- | -- | -- | PASS | -24.0 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kanon Sawashiro (`KXITFWMATCH-26OCT02SAWSAT-SAW`) | 0.18 / 0.19 (1469) | 18.5% | 46.2% | 61.6% | 42.5% [36.3%-48.4%] | -- | -- | -- | -- | WATCH | +24.0 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 827.0, B 1522.0; serve-point win A 55.3%, B 44.0%; Elo A 1348.8, B 1476.0; model uncertainty 0.0603
* Form inputs: days since last match A 166, B 166; matches on record A 36, B 304; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT02SAWSAT-SAW  (YES = Kanon Sawashiro)
Model: 43%
Kalshi: 18%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
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
| Francisco Cabral / James Tracy (`KXATPDOUBLES-26OCT03CABTRACASERL-CABTRA`) | 0.51 / 0.52 (183) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Robert Cash / Alexander Erler (`KXATPDOUBLES-26OCT03CABTRACASERL-CASERL`) | 0.48 / 0.49 (908) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Xinran Sun vs Cristina Bucsa -- WTA Beijing R64

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: 2026-10-03 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-03 09:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+240_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213710:270082:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Bucsa (`KXWTAMATCH-26OCT02SUNBUC-BUC`) | 0.69 / 0.70 (25641) | 69.5% | -- | 41.5% | 66.6% [53.7%-81.0%] | 67.6% | 68.0% | 67.8% | MODEL_LONE_OUTLIER | PASS | -2.9 pp | NORMAL | AGING | C / LIMITED | ALL_AGREE | VERIFIED |
| Xinran Sun (`KXWTAMATCH-26OCT02SUNBUC-SUN`) | 0.30 / 0.31 (23) | 30.5% | -- | 58.5% | 33.4% [19.0%-46.3%] | 32.4% | 32.0% | 32.2% | MODEL_LONE_OUTLIER | PASS | +2.9 pp | NORMAL | AGING | C / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 1001.0, B 4493.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.1365
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.029, surface_pool_high +0.030, surface_dev_loose +0.015, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 3 carry a model probability
  * `KXWTAGTOTAL-26OCT02SUNBUC-22` Over 21.5 games: 0.41/0.42 mid 41.5%, model 58.2% (market_conditioned_v1 (model4_board_v1)) -- gap +16.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT02SUNBUC-27` Over 26.5 games: 0.22/0.26 mid 24.0%, model 35.5% (market_conditioned_v1 (model4_board_v1)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote STALE, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26OCT02SUNBUC-17` Over 16.5 games: 0.79/0.88 mid 83.5%, model 91.0% (market_conditioned_v1 (model4_board_v1)) -- gap +7.5 pp, NORMAL, OK, quote STALE, identity VERIFIED, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; MODEL_ROW_STALE; STATUS_AMBIGUOUS; STALE_QUOTE; WIDE_SPREAD

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
| Gonzalo Escobar / Niki Kaliyanda Poonacha (`KXATPCHALLENGERDOUBLES-26OCT03ESCKALREYSTA-ESCKAL`) | 0.99 / -- (0) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Miguel Angel Reyes-Varela / Reese Stalder (`KXATPCHALLENGERDOUBLES-26OCT03ESCKALREYSTA-REYSTA`) | -- / 0.01 (1627) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE

## Daniil Medvedev vs Jan-Lennard Struff -- ATP Beijing R16

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: 2026-10-03 10:05Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-03 09:20Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+245_MIN; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105526:106421:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniil Medvedev (`KXATPMATCH-26OCT02MEDSTR-MED`) | 0.85 / 0.86 (65354) | 85.5% | -- | 84.9% | 85.5% [81.8%-86.1%] | 82.7% | 85.2% | 83.9% | MODEL_LONE_OUTLIER | PASS | -0.0 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26OCT02MEDSTR-STR`) | 0.14 / 0.15 (27285) | 14.5% | -- | 15.1% | 14.5% [14.0%-18.2%] | 17.3% | 14.5% | 15.9% | MODEL_LONE_OUTLIER | PASS | +0.0 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 6997.0, B 5447.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.021
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.012, surface_pool_high +0.006, surface_dev_loose +0.006, surface_dev_tight -0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT02MEDSTR-16` Over 15.5 games: 0.74/0.99 mid 86.5%, model 96.8% (market_conditioned_v1 (model4_board_v1)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02MEDSTR-MED20` Will Daniil Medvedev win the Daniil Medvedev vs Jan-Lennard Struff match by a set score of 2-0?: 0.64/0.65 mid 64.5%, model 56.0% (market_conditioned_v1 (model4_board_v1)) -- gap -8.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02MEDSTR-26` Over 25.5 games: 0.28/0.31 mid 29.5%, model 36.2% (market_conditioned_v1 (model4_board_v1)) -- gap +6.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02MEDSTR-MED21` Will Daniil Medvedev win the Daniil Medvedev vs Jan-Lennard Struff match by a set score of 2-1?: 0.21/0.22 mid 21.5%, model 28.2% (market_conditioned_v1 (model4_board_v1)) -- gap +6.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02MEDSTR-21` Over 20.5 games: 0.55/0.56 mid 55.5%, model 59.9% (market_conditioned_v1 (model4_board_v1)) -- gap +4.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02MEDSTR-MED8` Will Daniil Medvedev win at least 7.5 more games than Jan-Lennard Struff?: 0.06/0.17 mid 11.5%, model 8.1% (market_conditioned_v1 (model4_board_v1)) -- gap -3.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02MEDSTR-STR21` Will Jan-Lennard Struff win the Daniil Medvedev vs Jan-Lennard Struff match by a set score of 2-1?: 0.06/0.09 mid 7.5%, model 9.5% (market_conditioned_v1 (model4_board_v1)) -- gap +2.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02MEDSTR-MED5` Will Daniil Medvedev win at least 4.5 more games than Jan-Lennard Struff?: 0.47/0.48 mid 47.5%, model 46.1% (market_conditioned_v1 (model4_board_v1)) -- gap -1.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02MEDSTR-MED2` Will Daniil Medvedev win at least 1.5 more games than Jan-Lennard Struff?: 0.80/0.81 mid 80.5%, model 79.4% (market_conditioned_v1 (model4_board_v1)) -- gap -1.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02MEDSTR-STR20` Will Jan-Lennard Struff win the Daniil Medvedev vs Jan-Lennard Struff match by a set score of 2-0?: 0.06/0.08 mid 7.0%, model 6.3% (market_conditioned_v1 (model4_board_v1)) -- gap -0.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; MODEL_ROW_STALE; STATUS_AMBIGUOUS; WIDE_SPREAD

## Francisco Cerundolo vs Jakub Mensik -- ATP Beijing R16

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: 2026-10-03 11:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-03 10:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+300_MIN

ATP (MASTERS_1000) · Hard · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:202103:210150:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cerundolo (`KXATPMATCH-26OCT02CERMEN-CER`) | 0.35 / 0.37 (55616) | 36.0% | -- | 49.5% | 45.0% [42.5%-47.5%] | -- | 36.2% | 36.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +9.0 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jakub Mensik (`KXATPMATCH-26OCT02CERMEN-MEN`) | 0.64 / 0.65 (55681) | 64.5% | -- | 50.5% | 55.0% [52.5%-57.5%] | -- | 63.5% | 63.5% | MODEL_LONE_OUTLIER | PASS | -9.5 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 6448.0, B 5037.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0249
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.020, surface_dev_loose -0.005, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 10 carry a model probability
  * `KXATPGTOTAL-26OCT02CERMEN-23` Over 22.5 games: 0.49/0.50 mid 49.5%, model 58.5% (market_conditioned_v1 (model4_board_v1)) -- gap +9.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02CERMEN-28` Over 27.5 games: 0.29/0.31 mid 30.0%, model 38.3% (market_conditioned_v1 (model4_board_v1)) -- gap +8.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26OCT02CERMEN-18` Over 17.5 games: 0.83/0.86 mid 84.5%, model 92.0% (market_conditioned_v1 (model4_board_v1)) -- gap +7.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02CERMEN-MEN21` Will Jakub Mensik win the Francisco Cerundolo vs Jakub Mensik match by a set score of 2-1?: 0.22/0.24 mid 23.0%, model 28.7% (market_conditioned_v1 (model4_board_v1)) -- gap +5.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02CERMEN-MEN20` Will Jakub Mensik win the Francisco Cerundolo vs Jakub Mensik match by a set score of 2-0?: 0.40/0.42 mid 41.0%, model 35.6% (market_conditioned_v1 (model4_board_v1)) -- gap -5.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02CERMEN-MEN6` Will Jakub Mensik win at least 5.5 more games than Francisco Cerundolo?: 0.18/0.21 mid 19.5%, model 15.4% (market_conditioned_v1 (model4_board_v1)) -- gap -4.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02CERMEN-CER21` Will Francisco Cerundolo win the Francisco Cerundolo vs Jakub Mensik match by a set score of 2-1?: 0.15/0.17 mid 16.0%, model 19.4% (market_conditioned_v1 (model4_board_v1)) -- gap +3.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26OCT02CERMEN-CER20` Will Francisco Cerundolo win the Francisco Cerundolo vs Jakub Mensik match by a set score of 2-0?: 0.18/0.21 mid 19.5%, model 16.2% (market_conditioned_v1 (model4_board_v1)) -- gap -3.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02CERMEN-CER2` Will Francisco Cerundolo win at least 1.5 more games than Jakub Mensik?: 0.23/0.30 mid 26.5%, model 28.9% (market_conditioned_v1 (model4_board_v1)) -- gap +2.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26OCT02CERMEN-MEN3` Will Jakub Mensik win at least 2.5 more games than Francisco Cerundolo?: 0.51/0.53 mid 52.0%, model 49.9% (market_conditioned_v1 (model4_board_v1)) -- gap -2.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: SCHEDULED_START_PASSED; MODEL_ROW_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Yi Chen / Luo (`KXITFWDOUBLES-26OCT03YILSUNYICLUO-YICLUO`) | 0.67 / 0.70 (757) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yi Liu / Sun (`KXITFWDOUBLES-26OCT03YILSUNYICLUO-YILSUN`) | 0.31 / 0.32 (323) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Stevens / Thompson vs Arakawa / Tse -- W35 Wagga Wagga F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 11:26Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T11:26:46Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03STETHOARATSE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arakawa / Tse (`KXITFWDOUBLES-26OCT03STETHOARATSE-ARATSE`) | 0.08 / 0.57 (51) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stevens / Thompson (`KXITFWDOUBLES-26OCT03STETHOARATSE-STETHO`) | 0.07 / 0.48 (47) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Erika Andreeva vs Lois Boisson -- WTA 125K Adana SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 15:00Z
* Current expected start: 2026-10-03 12:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-03 11:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T15:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03ANDBOI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Erika Andreeva (`KXWTACHALLENGERMATCH-26OCT03ANDBOI-AND`) | 0.29 / 0.30 (2128) | 29.5% | -- | -- | -- [-----] | 31.2% | 31.2% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lois Boisson (`KXWTACHALLENGERMATCH-26OCT03ANDBOI-BOI`) | 0.70 / 0.71 (15463) | 70.5% | -- | -- | -- [-----] | 68.8% | 69.2% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Luis Carlos Alvarez Valdes / Adrian Oetzbach (`KXATPCHALLENGERDOUBLES-26OCT03ALVAOETOVCWEH-ALVAOET`) | 0.16 / 0.24 (501) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oleksandr Ovcharenko / Kai Wehnelt (`KXATPCHALLENGERDOUBLES-26OCT03ALVAOETOVCWEH-OVCWEH`) | 0.76 / 0.84 (1) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Millen Hurrion (`KXITFMATCH-26OCT03HURYIL-HUR`) | 0.78 / 0.82 (78) | 80.0% | 77.2% | 76.4% | 78.4% [76.8%-79.5%] | -- | -- | -- | -- | PASS | -1.6 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kerem Yilmaz (`KXITFMATCH-26OCT03HURYIL-YIL`) | 0.18 / 0.20 (188) | 19.0% | 22.8% | 23.6% | 21.6% [20.5%-23.2%] | -- | -- | -- | -- | PASS | +2.6 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3153.0, B 1537.0; serve-point win A 67.0%, B 39.0%; Elo A 1476.4, B 1224.3; model uncertainty 0.0138
* Form inputs: days since last match A 61, B 61; matches on record A 183, B 45; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

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
| Digvijay Pratap Singh (`KXITFMATCH-26OCT03WALSIN-SIN`) | 0.68 / 0.69 (33) | 68.5% | 59.5% | 54.9% | 59.3% [57.3%-61.3%] | -- | -- | -- | -- | PASS | -9.2 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marcus Walters (`KXITFMATCH-26OCT03WALSIN-WAL`) | 0.29 / 0.32 (61) | 30.5% | 40.5% | 45.1% | 40.7% [38.7%-42.7%] | -- | -- | -- | -- | WATCH | +10.2 pp | REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2102.0, B 2204.0; serve-point win A 63.0%, B 35.0%; Elo A 1257.0, B 1360.6; model uncertainty 0.0197
* Form inputs: days since last match A 89, B 19; matches on record A 106, B 181; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

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
| Hayden Jones (`KXITFMATCH-26OCT03JONPHA-JON`) | 0.73 / 0.74 (3698) | 73.5% | 44.8% | 50.0% | 45.4% [44.9%-46.5%] | -- | -- | -- | -- | PASS | -28.1 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Derek Pham (`KXITFMATCH-26OCT03JONPHA-PHA`) | 0.26 / 0.27 (1465) | 26.5% | 55.2% | 50.0% | 54.6% [53.5%-55.1%] | -- | -- | -- | -- | PASS | +28.1 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1969.0, B 178.0; serve-point win A 62.1%, B 36.9%; Elo A 1276.0, B 1312.3; model uncertainty 0.0079
* Form inputs: days since last match A 313, B 320; matches on record A 71, B 71; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT03JONPHA-PHA  (YES = Derek Pham)
Model: 55%
Kalshi: 26%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Antonia Ruzic vs Leolia Jeanjean -- WTA 125K Adana SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 16:10Z
* Current expected start: 2026-10-03 13:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-03 12:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T16:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03RUZJEA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leolia Jeanjean (`KXWTACHALLENGERMATCH-26OCT03RUZJEA-JEA`) | 0.42 / 0.43 (3512) | 42.5% | -- | -- | -- [-----] | 42.8% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Antonia Ruzic (`KXWTACHALLENGERMATCH-26OCT03RUZJEA-RUZ`) | 0.57 / 0.58 (7530) | 57.5% | -- | -- | -- [-----] | 57.2% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Finn Bass / Scott Duncan (`KXATPCHALLENGERDOUBLES-26OCT03BASDUNPOLSHE-BASDUN`) | 0.34 / 0.49 (49) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karl Poling / Joshua Sheehy (`KXATPCHALLENGERDOUBLES-26OCT03BASDUNPOLSHE-POLSHE`) | 0.42 / 0.56 (228) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| David Jorda Sanchis (`KXATPCHALLENGERMATCH-26OCT03JORMON-JOR`) | 0.28 / 0.29 (351) | 28.5% | 32.2% | 26.1% | 27.0% [25.3%-30.9%] | 31.2% | -- | 31.2% | KALSHI_LONE_OUTLIER | PASS | -1.6 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Inaki Montes-de la Torre (`KXATPCHALLENGERMATCH-26OCT03JORMON-MON`) | 0.71 / 0.72 (21279) | 71.5% | 67.8% | 73.9% | 73.0% [69.1%-74.7%] | 68.8% | -- | 68.8% | KALSHI_LONE_OUTLIER | PASS | +1.6 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5646.0, B 4378.0; serve-point win A 60.8%, B 35.6%; Elo A 1499.8, B 1650.2; model uncertainty 0.0282
* Form inputs: days since last match A 12, B 19; matches on record A 495, B 245; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.008, surface_dev_loose -0.015, surface_dev_tight +0.021
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Vitaliy Sachko vs Samuele Pieri -- ATP Challenger Bari SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 13:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-03T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126964:210129:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Samuele Pieri (`KXATPCHALLENGERMATCH-26OCT03SACPIE-PIE`) | 0.24 / 0.25 (8365) | 24.5% | 35.3% | 42.8% | 38.2% [32.5%-41.7%] | 26.0% | 23.9% | 24.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +13.7 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Vitaliy Sachko (`KXATPCHALLENGERMATCH-26OCT03SACPIE-SAC`) | 0.75 / 0.76 (2718) | 75.5% | 64.7% | 57.2% | 61.8% [58.3%-67.5%] | 74.0% | 76.7% | 75.3% | MODEL_LONE_OUTLIER | PASS | -13.7 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5739.0, B 4011.0; serve-point win A 61.4%, B 41.6%; Elo A 1699.3, B 1518.3; model uncertainty 0.0464
* Form inputs: days since last match A 19, B 12; matches on record A 683, B 209; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

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
| Felitsata Dorofeeva-Rybas (`KXITFWMATCH-26OCT03DORZHE-DOR`) | 0.70 / 0.73 (1) | 71.5% | 60.2% | 65.2% | 60.6% [57.5%-63.7%] | -- | -- | -- | -- | PASS | -10.9 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sonja Zhenikhova (`KXITFWMATCH-26OCT03DORZHE-ZHE`) | 0.26 / 0.30 (260) | 28.0% | 39.8% | 34.8% | 39.4% [36.3%-42.5%] | -- | -- | -- | -- | PASS | +11.4 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 923.0, B 1212.0; serve-point win A 55.0%, B 47.0%; Elo A 1460.2, B 1407.0; model uncertainty 0.0311
* Form inputs: days since last match A 306, B 222; matches on record A 19, B 38; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.005, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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
| Giulia Safina Popa (`KXITFWMATCH-26OCT03POPSAK-POP`) | 0.99 / -- (0) | -- | 47.9% | 52.6% | 51.6% [47.4%-54.2%] | -- | -- | -- | -- | PASS | -- | UNPRICED | AGING | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Sapfo Sakellaridi (`KXITFWMATCH-26OCT03POPSAK-SAK`) | -- / 0.01 (188951) | -- | 52.1% | 47.4% | 48.4% [45.8%-52.6%] | -- | -- | -- | -- | PASS | -- | UNPRICED | AGING | D / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 1013.0, B 4165.0; serve-point win A 53.8%, B 45.8%; Elo A 1546.3, B 1539.3; model uncertainty 0.0343
* Form inputs: days since last match A 369, B 81; matches on record A 38, B 703; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.021, surface_dev_loose +0.016, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE
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
| Arzhankin / Kunitsyn (`KXITFDOUBLES-26OCT03ARZKUNLORSEN-ARZKUN`) | 0.05 / 0.08 (1) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lorusso / Senn (`KXITFDOUBLES-26OCT03ARZKUNLORSEN-LORSEN`) | 0.92 / 0.93 (5) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

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
| Connel / Walters (`KXITFDOUBLES-26OCT03CONWALDELSTA-CONWAL`) | 0.32 / 0.71 (1) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Delicata / Stamatopoulos (`KXITFDOUBLES-26OCT03CONWALDELSTA-DELSTA`) | 0.29 / 0.30 (1035) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-03T14:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208843:210012:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jerome Kym (`KXATPCHALLENGERMATCH-26OCT03ROCKYM-KYM`) | 0.40 / 0.41 (14611) | 40.5% | 52.6% | 61.7% | 57.4% [53.0%-59.8%] | 41.6% | 41.5% | 41.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +16.9 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Henrique Rocha (`KXATPCHALLENGERMATCH-26OCT03ROCKYM-ROC`) | 0.59 / 0.60 (14412) | 59.5% | 47.4% | 38.3% | 42.6% [40.2%-47.0%] | 58.4% | 58.9% | 58.6% | MODEL_LONE_OUTLIER | PASS | -16.9 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5037.0, B 3926.0; serve-point win A 62.3%, B 37.1%; Elo A 1721.6, B 1694.4; model uncertainty 0.0341
* Form inputs: days since last match A 26, B 32; matches on record A 353, B 311; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT03ROCKYM-KYM  (YES = Jerome Kym)
Model: 57%
Kalshi: 40%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

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
| Beale / Vujic (`KXITFDOUBLES-26OCT03HOEPADBEAVUJ-BEAVUJ`) | 0.36 / 0.47 (117) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hoeyeraal / Padgham (`KXITFDOUBLES-26OCT03HOEPADBEAVUJ-HOEPAD`) | 0.44 / 0.60 (49) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Ryan Nijboer (`KXITFMATCH-26OCT03NIJRIT-NIJ`) | 0.23 / 0.29 (5) | 26.0% | 22.8% | 24.2% | 21.1% [18.6%-22.7%] | 30.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Ritschard (`KXITFMATCH-26OCT03NIJRIT-RIT`) | 0.72 / 0.75 (2) | 73.5% | 77.2% | 75.8% | 78.9% [77.3%-81.4%] | 69.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +5.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4005.0, B 3172.0; serve-point win A 57.0%, B 37.2%; Elo A 1482.5, B 1773.1; model uncertainty 0.0205
* Form inputs: days since last match A 12, B 26; matches on record A 484, B 681; data quality A
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
| Biletic / Kajin (`KXITFDOUBLES-26OCT03BILKAJJERKUP-BILKAJ`) | 0.75 / 0.82 (523) | 78.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeran / Kupcic (`KXITFDOUBLES-26OCT03BILKAJJERKUP-JERKUP`) | 0.18 / 0.25 (1) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Emilien Demanet (`KXITFMATCH-26OCT03DEMDUR-DEM`) | 0.16 / 0.17 (2562) | 16.5% | 47.8% | 36.9% | 41.8% [38.4%-49.5%] | 47.1% | -- | 47.1% | KALSHI_LONE_OUTLIER | PASS | +25.3 pp | EXTREME (DATA_WARNING) | AGING | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Tuncay Duran (`KXITFMATCH-26OCT03DEMDUR-DUR`) | 0.82 / 0.83 (118) | 82.5% | 52.2% | 63.1% | 58.2% [50.5%-61.6%] | 52.9% | -- | 52.9% | KALSHI_LONE_OUTLIER | WATCH | -24.3 pp | HIGH_REVIEW | AGING | A / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 2543.0, B 2317.0; serve-point win A 62.4%, B 37.2%; Elo A 1429.3, B 1432.2; model uncertainty 0.0556
* Form inputs: days since last match A 61, B 61; matches on record A 142, B 116; data quality A

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT03DEMDUR-DEM  (YES = Emilien Demanet)
Model: 42%
Kalshi: 16%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose -0.020, surface_dev_tight +0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER
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
| Florent Bax (`KXITFMATCH-26OCT03HEMBAX-BAX`) | 0.15 / 0.16 (2769) | 15.5% | 42.8% | 62.6% | 54.9% [49.5%-58.3%] | 40.1% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +39.4 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Calvin Hemery (`KXITFMATCH-26OCT03HEMBAX-HEM`) | 0.84 / 0.85 (4521) | 84.5% | 57.2% | 37.4% | 45.1% [41.7%-50.5%] | 59.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -39.4 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5909.0, B 4639.0; serve-point win A 60.6%, B 40.8%; Elo A 1670.5, B 1549.8; model uncertainty 0.044
* Form inputs: days since last match A 12, B 19; matches on record A 938, B 354; data quality A

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT03HEMBAX-BAX  (YES = Florent Bax)
Model: 55%
Kalshi: 16%
Gap: +39 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose -0.019, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
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
| Noah Lopez (`KXITFMATCH-26OCT03LOPVAN-LOP`) | 0.17 / 0.18 (38) | 17.5% | 38.1% | 38.2% | 32.8% [29.2%-34.7%] | 31.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +15.3 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Martin VAN DER MEERSCHEN (`KXITFMATCH-26OCT03LOPVAN-VAN`) | 0.80 / 0.82 (2729) | 81.0% | 61.9% | 61.8% | 67.2% [65.3%-70.8%] | 68.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -13.8 pp | REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1139.0, B 2224.0; serve-point win A 58.7%, B 38.9%; Elo A 1204.7, B 1362.4; model uncertainty 0.0276
* Form inputs: days since last match A 138, B 138; matches on record A 116, B 107; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26OCT03LOPVAN-LOP  (YES = Noah Lopez)
Model: 33%
Kalshi: 18%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.009, surface_dev_loose -0.018, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
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
| Kris van Wyk (`KXITFMATCH-26OCT03VANVER-VAN`) | 0.32 / 0.33 (1554) | 32.5% | 47.7% | 17.1% | 44.2% [36.0%-53.7%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +11.7 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lars Goran Verwerft (`KXITFMATCH-26OCT03VANVER-VER`) | 0.67 / 0.68 (2255) | 67.5% | 52.3% | 82.9% | 55.8% [46.3%-63.9%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.7 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2787.0, B 832.0; serve-point win A 62.4%, B 37.2%; Elo A 1308.5, B 1225.4; model uncertainty 0.0881
* Form inputs: days since last match A 124, B 131; matches on record A 330, B 20; data quality C
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
| Ekaterina Dotsenko (`KXITFWMATCH-26OCT03MIXDOT-DOT`) | 0.95 / 0.96 (1096) | 95.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lan Mi (`KXITFWMATCH-26OCT03MIXDOT-MIX`) | 0.04 / 0.05 (3836) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
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
| Lisa Pigato (`KXITFWMATCH-26OCT03PIGSWA-PIG`) | 0.66 / 0.68 (1) | 67.0% | 46.2% | 47.3% | 44.7% [41.6%-50.5%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -22.3 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katie Swan (`KXITFWMATCH-26OCT03PIGSWA-SWA`) | 0.33 / 0.35 (6) | 34.0% | 53.8% | 52.6% | 55.3% [49.5%-58.4%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +21.3 pp | HIGH_REVIEW | STALE | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4114.0, B 2343.0; serve-point win A 55.3%, B 44.0%; Elo A 1654.6, B 1720.0; model uncertainty 0.0448
* Form inputs: days since last match A 14, B 8; matches on record A 353, B 385; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT03PIGSWA-SWA  (YES = Katie Swan)
Model: 55%
Kalshi: 34%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.037, surface_pool_high -0.031, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE
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
| Sophia Biolay (`KXITFWMATCH-26OCT03SORBIO-BIO`) | 0.78 / 0.80 (1) | 79.0% | 71.2% | 85.5% | 69.9% [62.6%-76.9%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.1 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marta Soriano Santiago (`KXITFWMATCH-26OCT03SORBIO-SOR`) | 0.18 / 0.20 (1) | 19.0% | 28.7% | 14.5% | 30.1% [23.1%-37.4%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.1 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1358.0, B 766.0; serve-point win A 53.6%, B 42.2%; Elo A 1390.2, B 1461.2; model uncertainty 0.0716
* Form inputs: days since last match A 159, B 229; matches on record A 98, B 133; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.019, surface_dev_loose -0.009, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hatouka / Zelinskaya vs Rabl / Marlies Rothensteiner -- W15 Sharm ElSheikh F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 15:08Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T15:08:46Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03HATZELRABMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hatouka / Zelinskaya (`KXITFWDOUBLES-26OCT03HATZELRABMAR-HATZEL`) | 0.91 / 0.94 (119) | 92.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rabl / Marlies Rothensteiner (`KXITFWDOUBLES-26OCT03HATZELRABMAR-RABMAR`) | 0.04 / 0.12 (10) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Gabi Adrian Boitan (`KXITFMATCH-26OCT03BOIZGO-BOI`) | 0.88 / 0.90 (1) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Borys Zgola (`KXITFMATCH-26OCT03BOIZGO-ZGO`) | 0.09 / 0.14 (16) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
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

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-03T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209849:212082:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sascha Gueymard Wayenburg (`KXATPCHALLENGERMATCH-26OCT03SCHGUE-GUE`) | 0.58 / 0.59 (20494) | 58.5% | 56.4% | 66.5% | 64.2% [61.5%-66.0%] | -- | -- | -- | -- | WATCH | +5.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Joel Schwaerzler (`KXATPCHALLENGERMATCH-26OCT03SCHGUE-SCH`) | 0.41 / 0.42 (3356) | 41.5% | 43.6% | 33.5% | 35.8% [34.1%-38.5%] | -- | -- | -- | -- | PASS | -5.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4727.0, B 4960.0; serve-point win A 62.0%, B 36.8%; Elo A 1601.4, B 1660.7; model uncertainty 0.0221
* Form inputs: days since last match A 12, B 19; matches on record A 191, B 357; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.009, surface_dev_loose -0.017, surface_dev_tight +0.022
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

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
| Branger / Dugardin (`KXITFDOUBLES-26OCT03BRADUGNAGPIA-BRADUG`) | 0.44 / 0.66 (99) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nagoudi / Piatti (`KXITFDOUBLES-26OCT03BRADUGNAGPIA-NAGPIA`) | 0.30 / 0.40 (501) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

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
| Max Houkes (`KXITFMATCH-26OCT03HOULOC-HOU`) | 0.86 / 0.87 (363) | 86.5% | 75.9% | 79.5% | 78.3% [71.4%-80.1%] | 85.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -8.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Benjamin Lock (`KXITFMATCH-26OCT03HOULOC-LOC`) | 0.13 / 0.14 (1805) | 13.5% | 24.1% | 20.5% | 21.6% [19.9%-28.6%] | 14.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +8.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5070.0, B 4430.0; serve-point win A 62.6%, B 42.8%; Elo A 1640.9, B 1445.6; model uncertainty 0.0439
* Form inputs: days since last match A 54, B 677; matches on record A 430, B 700; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose -0.000, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Juan Cruz Martin Manzano vs Matthew William Donald -- ATP Challenger Bari SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-03T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210054:212305:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew William Donald (`KXATPCHALLENGERMATCH-26OCT03MARDON-DON`) | 0.47 / 0.48 (13141) | 47.5% | 50.1% | 63.1% | 55.8% [52.1%-59.0%] | 48.0% | 48.1% | 48.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Juan Cruz Martin Manzano (`KXATPCHALLENGERMATCH-26OCT03MARDON-MAR`) | 0.52 / 0.53 (5522) | 52.5% | 49.9% | 36.9% | 44.2% [41.0%-47.9%] | 52.0% | 52.0% | 52.0% | MODEL_LONE_OUTLIER | PASS | -8.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3350.0, B 2929.0; serve-point win A 59.9%, B 40.1%; Elo A 1491.1, B 1435.7; model uncertainty 0.0343
* Form inputs: days since last match A 12, B 12; matches on record A 120, B 205; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.016, surface_dev_loose -0.011, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

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
| Sander Jong (`KXITFMATCH-26OCT03MORJON-JON`) | 0.33 / 0.35 (1480) | 34.0% | 36.1% | 38.9% | 34.1% [25.6%-38.9%] | 35.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +0.1 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Moro Canas (`KXITFMATCH-26OCT03MORJON-MOR`) | 0.66 / 0.67 (4598) | 66.5% | 63.9% | 61.1% | 65.9% [61.1%-74.4%] | 64.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.6 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6297.0, B 1938.0; serve-point win A 61.3%, B 41.5%; Elo A 1639.8, B 1478.4; model uncertainty 0.0668
* Form inputs: days since last match A 19, B 118; matches on record A 426, B 134; data quality B
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
| Margaux Rouvroy (`KXITFWMATCH-26OCT03VEDROU-ROU`) | 0.36 / 0.39 (345) | 37.5% | 54.3% | 60.4% | 58.9% [52.6%-60.9%] | 38.5% | -- | 38.5% | MODEL_LONE_OUTLIER | PASS | +21.4 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Eva Vedder (`KXITFWMATCH-26OCT03VEDROU-VED`) | 0.61 / 0.64 (372) | 62.5% | 45.7% | 39.6% | 41.1% [39.1%-47.4%] | 61.5% | -- | 61.5% | MODEL_LONE_OUTLIER | PASS | -21.4 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3271.0, B 3212.0; serve-point win A 55.3%, B 43.9%; Elo A 1586.1, B 1624.5; model uncertainty 0.0412
* Form inputs: days since last match A 18, B 20; matches on record A 432, B 337; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT03VEDROU-ROU  (YES = Margaux Rouvroy)
Model: 59%
Kalshi: 38%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.020, surface_dev_loose -0.010, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
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
| Charles Bertimon (`KXITFMATCH-26OCT03MASBER-BER`) | 0.21 / 0.23 (3666) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nikita Mashtakov (`KXITFMATCH-26OCT03MASBER-MAS`) | 0.77 / 0.79 (363) | 78.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
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
| Sebastian Gima (`KXITFMATCH-26OCT03TURGIM-GIM`) | 0.39 / 0.40 (42) | 39.5% | 44.4% | 42.2% | 42.2% [40.2%-45.9%] | 40.1% | -- | 40.1% | MODEL_LONE_OUTLIER | PASS | +2.7 pp | NORMAL | AGING | B / LIMITED | ALL_AGREE | VERIFIED |
| Radu David Turcanu (`KXITFMATCH-26OCT03TURGIM-TUR`) | 0.58 / 0.61 (4757) | 59.5% | 55.6% | 57.8% | 57.8% [54.1%-59.8%] | 59.9% | -- | 59.9% | MODEL_LONE_OUTLIER | PASS | -1.7 pp | NORMAL | AGING | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2393.0, B 3345.0; serve-point win A 60.4%, B 40.6%; Elo A 1462.2, B 1402.1; model uncertainty 0.0283
* Form inputs: days since last match A 124, B 12; matches on record A 70, B 386; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.020, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Clement Chidekh vs Henry Bernet -- ATP Challenger Mouilleron-Le-Captif SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 16:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-03T16:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:148679:206889:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Henry Bernet (`KXATPCHALLENGERMATCH-26OCT03CHIBER-BER`) | 0.37 / 0.38 (4363) | 37.5% | 29.5% | 18.5% | 22.1% [19.9%-27.6%] | 38.4% | 38.2% | 38.2% | MODEL_LONE_OUTLIER | PASS | -15.4 pp | HIGH_REVIEW | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Clement Chidekh (`KXATPCHALLENGERMATCH-26OCT03CHIBER-CHI`) | 0.62 / 0.63 (9486) | 62.5% | 70.5% | 81.5% | 78.0% [72.4%-80.1%] | 61.6% | 62.6% | 62.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +15.4 pp | HIGH_REVIEW | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5365.0, B 2182.0; serve-point win A 64.7%, B 39.5%; Elo A 1688.7, B 1526.8; model uncertainty 0.0386
* Form inputs: days since last match A 19, B 33; matches on record A 353, B 61; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26OCT03CHIBER-CHI  (YES = Clement Chidekh)
Model: 78%
Kalshi: 62%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: EXTERNAL_STALE
Data quality: A (ADEQUATE)
Reasons: NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.022, surface_dev_tight -0.024
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Stefan Latinovic / Mili Poljicak vs Alexander Donski / Filip Pieczonka -- ATP Challenger Porto 2 F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-03T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03LATPOLDONPIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Donski / Filip Pieczonka (`KXATPCHALLENGERDOUBLES-26OCT03LATPOLDONPIE-DONPIE`) | 0.51 / 0.58 (16) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stefan Latinovic / Mili Poljicak (`KXATPCHALLENGERDOUBLES-26OCT03LATPOLDONPIE-LATPOL`) | 0.42 / 0.50 (198) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Gatoto / Shalin Shah (`KXITFDOUBLES-26OCT03GATSHANEFSCH-GATSHA`) | 0.15 / 0.21 (31) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nefve / Schachter (`KXITFDOUBLES-26OCT03GATSHANEFSCH-NEFSCH`) | 0.08 / 0.87 (136) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Guido Ivan Justo vs Marcelo Tomas Barrios Vera -- ATP Challenger Curitiba SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-03T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03JUSBAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcelo Tomas Barrios Vera (`KXATPCHALLENGERMATCH-26OCT03JUSBAR-BAR`) | 0.65 / 0.66 (2446) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Guido Ivan Justo (`KXATPCHALLENGERMATCH-26OCT03JUSBAR-JUS`) | 0.33 / 0.35 (3526) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Daniel Milavsky / Braden Shick vs Brandon Carpico / Nikita Samuel Filin -- ATP Challenger Columbus F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-03T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03MILSHICARFIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brandon Carpico / Nikita Samuel Filin (`KXATPCHALLENGERDOUBLES-26OCT03MILSHICARFIL-CARFIL`) | 0.47 / 0.54 (55) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Milavsky / Braden Shick (`KXATPCHALLENGERDOUBLES-26OCT03MILSHICARFIL-MILSHI`) | 0.44 / 0.51 (216) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

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
| Sada Nahimana (`KXITFWMATCH-26OCT03NAHVAN-NAH`) | 0.44 / 0.45 (3806) | 44.5% | 40.7% | 27.0% | 34.4% [28.8%-46.3%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -10.1 pp | REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Isis Louise Van den Broek (`KXITFWMATCH-26OCT03NAHVAN-VAN`) | 0.53 / 0.55 (57) | 54.0% | 59.3% | 73.0% | 65.6% [53.7%-71.2%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +11.6 pp | REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2636.0, B 1856.0; serve-point win A 54.8%, B 43.4%; Elo A 1540.8, B 1579.5; model uncertainty 0.0876
* Form inputs: days since last match A 136, B 159; matches on record A 369, B 103; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.024, surface_dev_loose -0.034, surface_dev_tight +0.025
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
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
| Bertacchi / Dibenedetto (`KXITFWDOUBLES-26OCT03BERDIBBIOCIR-BERDIB`) | 0.10 / 0.55 (596) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Biolay / Cirotte (`KXITFWDOUBLES-26OCT03BERDIBBIOCIR-BIOCIR`) | 0.46 / 0.61 (510) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Dylan Dietrich vs Andres Andrade -- ATP Challenger Columbus SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-10-03T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200748:210157:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andres Andrade (`KXATPCHALLENGERMATCH-26OCT03DIEAND-AND`) | 0.29 / 0.30 (3080) | 29.5% | -- | 29.9% | 42.9% [34.5%-53.6%] | 30.3% | 30.7% | 30.5% | MODEL_LONE_OUTLIER | WATCH | +13.4 pp | REVIEW | AGING | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Dylan Dietrich (`KXATPCHALLENGERMATCH-26OCT03DIEAND-DIE`) | 0.70 / 0.71 (2554) | 70.5% | -- | 70.1% | 57.1% [46.4%-65.5%] | 69.7% | 70.2% | 69.9% | MODEL_LONE_OUTLIER | PASS | -13.4 pp | REVIEW | AGING | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1313.0, B 4672.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0953
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.020, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Gustavo Heide vs Pedro Boscardin Dias -- ATP Challenger Curitiba SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-10-03T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208046:208361:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Boscardin Dias (`KXATPCHALLENGERMATCH-26OCT03HEIBOS-BOS`) | 0.18 / 0.19 (3654) | 18.5% | -- | 12.6% | 14.8% [13.1%-17.6%] | 20.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gustavo Heide (`KXATPCHALLENGERMATCH-26OCT03HEIBOS-HEI`) | 0.81 / 0.82 (6129) | 81.5% | -- | 87.5% | 85.2% [82.3%-86.9%] | 79.2% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.7 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4906.0, B 4852.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0229
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.003, surface_pool_high -0.003, surface_dev_loose +0.006, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

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
| Ifi / Stanke (`KXITFDOUBLES-26OCT03LOPPALIFISTA-IFISTA`) | 0.60 / 0.68 (0) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lopez Martos / Palomar (`KXITFDOUBLES-26OCT03LOPPALIFISTA-LOPPAL`) | 0.30 / 0.38 (0) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

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
| Salma Djoubri (`KXITFWMATCH-26OCT03DJODUP-DJO`) | 0.19 / 0.20 (1110) | 19.5% | 34.3% | 12.7% | 31.4% [25.5%-38.4%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.9 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Britt Du Pree (`KXITFWMATCH-26OCT03DJODUP-DUP`) | 0.79 / 0.81 (447) | 80.0% | 65.7% | 87.3% | 68.6% [61.6%-74.5%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -11.4 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 169.0, B 2691.0; serve-point win A 54.2%, B 42.8%; Elo A 1467.4, B 1580.2; model uncertainty 0.0644
* Form inputs: days since last match A 320, B 159; matches on record A 168, B 85; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.039, surface_pool_high -0.028, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mariano Kestelboim / Marcelo Zormann vs Luis Guto Miguel / Eduardo Ribeiro -- ATP Challenger Curitiba F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 20:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-10-03T20:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03KESZORMIGRIB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariano Kestelboim / Marcelo Zormann (`KXATPCHALLENGERDOUBLES-26OCT03KESZORMIGRIB-KESZOR`) | 0.44 / 0.53 (52) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luis Guto Miguel / Eduardo Ribeiro (`KXATPCHALLENGERDOUBLES-26OCT03KESZORMIGRIB-MIGRIB`) | 0.46 / 0.54 (53) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Abdullah Shelbayh vs Mitchell Krueger -- ATP Challenger Columbus SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 20:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-10-03T20:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03SHEKRU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mitchell Krueger (`KXATPCHALLENGERMATCH-26OCT03SHEKRU-KRU`) | 0.43 / 0.45 (5688) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Abdullah Shelbayh (`KXATPCHALLENGERMATCH-26OCT03SHEKRU-SHE`) | 0.55 / 0.57 (4171) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Hugo Coquelin vs Oliver Bonding -- M15 Ann Arbor MI SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212839:213042:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oliver Bonding (`KXITFMATCH-26OCT03COQBON-BON`) | 0.80 / 0.82 (138) | 81.0% | 71.9% | 79.9% | 73.9% [71.2%-77.2%] | 81.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hugo Coquelin (`KXITFMATCH-26OCT03COQBON-COQ`) | 0.18 / 0.19 (62) | 18.5% | 28.1% | 20.1% | 26.1% [22.8%-28.8%] | 18.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +7.6 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 446.0, B 1207.0; serve-point win A 60.3%, B 35.1%; Elo A 1277.2, B 1440.2; model uncertainty 0.0304
* Form inputs: days since last match A 124, B 40; matches on record A 17, B 42; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.008, surface_dev_loose -0.013, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE
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
| Theo Papamalamis (`KXITFMATCH-26OCT03PAPROZ-PAP`) | 0.53 / 0.55 (28) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Rozin (`KXITFMATCH-26OCT03PAPROZ-ROZ`) | 0.45 / 0.48 (92) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
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

ITF (ITF) · Hard · scheduled 2026-10-03T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211609:214236:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Dahlin (`KXITFMATCH-26OCT03TOMDAH-DAH`) | 0.81 / 0.83 (1) | 82.0% | 71.6% | 81.3% | 72.1% [70.3%-73.8%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Naoto Tomizawa (`KXITFMATCH-26OCT03TOMDAH-TOM`) | 0.16 / 0.17 (646) | 16.5% | 28.4% | 18.7% | 27.9% [26.2%-29.7%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.4 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 62.0, B 583.0; serve-point win A 60.3%, B 35.1%; Elo A 1263.2, B 1424.0; model uncertainty 0.0175
* Form inputs: days since last match A 341, B 68; matches on record A 1, B 41; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.017, surface_dev_loose -0.009, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
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

ITF (ITF) · Hard · scheduled 2026-10-03T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:203281:264962:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charo Esquiva Banuls (`KXITFWMATCH-26OCT03HESESQ-ESQ`) | 0.75 / 0.76 (2587) | 75.5% | 40.4% | 35.9% | 34.9% [30.5%-38.9%] | 57.0% | -- | 57.0% | MODEL_LONE_OUTLIER | PASS | -40.6 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Amandine Hesse (`KXITFWMATCH-26OCT03HESESQ-HES`) | 0.24 / 0.25 (2435) | 24.5% | 59.6% | 64.1% | 65.1% [61.1%-69.5%] | 43.0% | -- | 43.0% | MODEL_LONE_OUTLIER | WATCH | +40.6 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 2021.0, B 1005.0; serve-point win A 56.6%, B 45.2%; Elo A 1578.2, B 1466.2; model uncertainty 0.0419
* Form inputs: days since last match A 83, B 18; matches on record A 777, B 35; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT03HESESQ-HES  (YES = Amandine Hesse)
Model: 65%
Kalshi: 24%
Gap: +41 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.040, surface_dev_loose +0.020, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
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

ITF (ITF) · Hard · scheduled 2026-10-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211738:213771:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jonah Braswell (`KXITFMATCH-26OCT03BRAMOS-BRA`) | 0.36 / 0.39 (3583) | 37.5% | 53.6% | 32.0% | 50.5% [45.3%-53.1%] | 37.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +13.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dominick Mosejczuk (`KXITFMATCH-26OCT03BRAMOS-MOS`) | 0.60 / 0.63 (66) | 61.5% | 46.4% | 68.0% | 49.5% [46.9%-54.7%] | 62.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -12.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 298.0, B 379.0; serve-point win A 62.9%, B 37.8%; Elo A 1291.2, B 1266.4; model uncertainty 0.0388
* Form inputs: days since last match A 320, B 369; matches on record A 17, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.010, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
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
| Fradkin / Kuhar (`KXITFDOUBLES-26OCT03FRAKUHSHESWE-FRAKUH`) | 0.07 / 0.52 (53) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sheldon / Swenson (`KXITFDOUBLES-26OCT03FRAKUHSHESWE-SHESWE`) | 0.39 / 0.56 (8) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Leyla Fiorella Britez Risso vs Maria Florencia Urrutia -- W15 Trelew SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220447:222513:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leyla Fiorella Britez Risso (`KXITFWMATCH-26OCT03BRIURR-BRI`) | 0.61 / 0.64 (27) | 62.5% | 38.9% | 9.4% | 32.9% [26.8%-38.4%] | -- | -- | -- | -- | PASS | -29.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maria Florencia Urrutia (`KXITFWMATCH-26OCT03BRIURR-URR`) | 0.37 / 0.38 (3121) | 37.5% | 61.1% | 90.5% | 67.1% [61.6%-73.2%] | -- | -- | -- | -- | PASS | +29.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 257.0, B 2454.0; serve-point win A 54.6%, B 43.3%; Elo A 1408.3, B 1486.5; model uncertainty 0.0579
* Form inputs: days since last match A 845, B 159; matches on record A 44, B 106; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT03BRIURR-URR  (YES = Maria Florencia Urrutia)
Model: 67%
Kalshi: 38%
Gap: +30 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Celia Cervino Ruiz vs Valentina Ivanov -- W35 Baza SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216078:221173:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Celia Cervino Ruiz (`KXITFWMATCH-26OCT03CERIVA-CER`) | 0.45 / 0.46 (688) | 45.5% | 40.1% | 31.9% | 36.9% [32.4%-45.7%] | 44.8% | -- | 44.8% | MARKETS_AGREE | PASS | -8.7 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Valentina Ivanov (`KXITFWMATCH-26OCT03CERIVA-IVA`) | 0.54 / 0.56 (5009) | 55.0% | 59.9% | 68.1% | 63.1% [54.3%-67.6%] | 55.2% | -- | 55.2% | MARKETS_AGREE | WATCH | +8.2 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1450.0, B 1892.0; serve-point win A 54.7%, B 43.4%; Elo A 1439.1, B 1496.4; model uncertainty 0.0667
* Form inputs: days since last match A 11, B 166; matches on record A 265, B 135; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.030, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Roddick / Tokac vs Arcila / Rozin -- M15 Fayetteville AR F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03RODTOKARCROZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arcila / Rozin (`KXITFDOUBLES-26OCT03RODTOKARCROZ-ARCROZ`) | 0.07 / 0.64 (69) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Roddick / Tokac (`KXITFDOUBLES-26OCT03RODTOKARCROZ-RODTOK`) | 0.07 / 0.53 (53) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Ana Sofia Sanchez vs Luciana Moyano -- W15 Trelew SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-03 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-10-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204419:237454:2026-10-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciana Moyano (`KXITFWMATCH-26OCT03SANMOY-MOY`) | 0.16 / 0.18 (3946) | 17.0% | 40.2% | 45.7% | 37.9% [32.9%-41.0%] | -- | -- | -- | -- | WATCH | +20.9 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ana Sofia Sanchez (`KXITFWMATCH-26OCT03SANMOY-SAN`) | 0.81 / 0.84 (1583) | 82.5% | 59.8% | 54.3% | 62.1% [59.0%-67.1%] | -- | -- | -- | -- | PASS | -20.4 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3191.0, B 2452.0; serve-point win A 56.6%, B 45.2%; Elo A 1573.4, B 1405.3; model uncertainty 0.0406
* Form inputs: days since last match A 21, B 159; matches on record A 856, B 106; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT03SANMOY-MOY  (YES = Luciana Moyano)
Model: 38%
Kalshi: 17%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ashton Bowers vs Astra Sharma -- W15 Nashville TN SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206292:248665:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashton Bowers (`KXITFWMATCH-26OCT03BOWSHA-BOW`) | 0.16 / 0.17 (3278) | 16.5% | 16.8% | 36.5% | 16.4% [16.3%-16.4%] | -- | -- | -- | -- | PASS | -0.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Astra Sharma (`KXITFWMATCH-26OCT03BOWSHA-SHA`) | 0.82 / 0.84 (186) | 83.0% | 83.2% | 63.5% | 83.6% [83.6%-83.7%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 2800.0; serve-point win A 53.3%, B 39.3%; Elo A 1419.7, B 1698.2; model uncertainty 0.0006
* Form inputs: days since last match A 712, B 17; matches on record A 46, B 423; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Broadus / Zamarripa vs Osuigwe / Urhobo -- W100 Templeton CA F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-04T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03BROZAMOSUURH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Broadus / Zamarripa (`KXITFWDOUBLES-26OCT03BROZAMOSUURH-BROZAM`) | 0.06 / 0.79 (119) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Osuigwe / Urhobo (`KXITFWDOUBLES-26OCT03BROZAMOSUURH-OSUURH`) | 0.06 / 0.37 (39) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Merna Refaat vs Rose Marie Nijkamp -- W15 Nashville TN SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221473:260225:2026-10-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rose Marie Nijkamp (`KXITFWMATCH-26OCT03REFNIJ-NIJ`) | 0.41 / 0.42 (43) | 41.5% | 63.0% | 62.1% | 63.7% [63.1%-64.7%] | -- | -- | -- | -- | PASS | +22.2 pp | HIGH_REVIEW | STALE | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Merna Refaat (`KXITFWMATCH-26OCT03REFNIJ-REF`) | 0.58 / 0.60 (3120) | 59.0% | 37.0% | 37.9% | 36.3% [35.3%-36.9%] | -- | -- | -- | -- | PASS | -22.7 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 556.0, B 1080.0; serve-point win A 55.7%, B 41.7%; Elo A 1376.3, B 1482.4; model uncertainty 0.0076
* Form inputs: days since last match A 355, B 166; matches on record A 201, B 54; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26OCT03REFNIJ-NIJ  (YES = Rose Marie Nijkamp)
Model: 64%
Kalshi: 42%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: STALE
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: STALE_KALSHI_QUOTE, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; STALE_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pearce / Yamakita vs Kamper / Kruger -- W15 Nashville TN F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-04T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03PEAYAMKAMKRU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kamper / Kruger (`KXITFWDOUBLES-26OCT03PEAYAMKAMKRU-KAMKRU`) | 0.06 / 0.75 (100) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pearce / Yamakita (`KXITFWDOUBLES-26OCT03PEAYAMKAMKRU-PEAYAM`) | 0.06 / 0.43 (43) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Ayala / Fiorella Britez Risso vs Meabe / Florencia Urrutia -- W15 Trelew F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-10-04T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03AYAFIOMEAFLO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayala / Fiorella Britez Risso (`KXITFWDOUBLES-26OCT03AYAFIOMEAFLO-AYAFIO`) | 0.06 / 0.54 (54) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Meabe / Florencia Urrutia (`KXITFWDOUBLES-26OCT03AYAFIOMEAFLO-MEAFLO`) | 0.06 / 0.65 (71) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Jaume Munar vs Kyrian Jacquet -- ATP Tokyo QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 05:00Z
* Current expected start: 2026-10-04 02:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 01:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-04T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT03MUNJAC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kyrian Jacquet (`KXATPMATCH-26OCT03MUNJAC-JAC`) | 0.41 / 0.42 (17485) | 41.5% | -- | -- | -- [-----] | 41.7% | 41.2% | 41.4% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jaume Munar (`KXATPMATCH-26OCT03MUNJAC-MUN`) | 0.59 / 0.60 (25017) | 59.5% | -- | -- | -- [-----] | 58.3% | 58.8% | 58.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jia-Jing Lu vs Zongyu Li -- WTA 125K Suzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 08:00Z
* Current expected start: 2026-10-04 02:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 01:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03JIAZON:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jia-Jing Lu (`KXWTACHALLENGERMATCH-26OCT03JIAZON-JIA`) | 0.63 / 0.65 (363) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Zongyu Li (`KXWTACHALLENGERMATCH-26OCT03JIAZON-ZON`) | 0.36 / 0.38 (4399) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Wushuang Zheng vs Yihan Qu -- WTA 125K Suzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 11:50Z
* Current expected start: 2026-10-04 02:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 01:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T11:50:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03ZHEYIH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yihan Qu (`KXWTACHALLENGERMATCH-26OCT03ZHEYIH-YIH`) | 0.26 / 0.27 (1296) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Wushuang Zheng (`KXWTACHALLENGERMATCH-26OCT03ZHEYIH-ZHE`) | 0.73 / 0.74 (1325) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Nikola Bartunkova vs Aryna Sabalenka -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 03:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03BARSAB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikola Bartunkova (`KXWTAMATCH-26OCT03BARSAB-BAR`) | 0.14 / 0.15 (20749) | 14.5% | -- | -- | -- [-----] | 15.9% | 14.4% | 15.1% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aryna Sabalenka (`KXWTAMATCH-26OCT03BARSAB-SAB`) | 0.85 / 0.86 (2318) | 85.5% | -- | -- | -- [-----] | 84.1% | 86.3% | 85.2% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mariia Alexandrovna Kozyreva / Vera Zvonareva vs Lyudmyla Kichenok / Asia Muhammad -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 03:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03KOZZVOKICMUH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lyudmyla Kichenok / Asia Muhammad (`KXWTADOUBLES-26OCT03KOZZVOKICMUH-KICMUH`) | 0.39 / 0.46 (46) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mariia Alexandrovna Kozyreva / Vera Zvonareva (`KXWTADOUBLES-26OCT03KOZZVOKICMUH-KOZZVO`) | 0.51 / 0.59 (46) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Sinja Kraus vs Dayana Yastremska -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 03:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03KRAYAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sinja Kraus (`KXWTAMATCH-26OCT03KRAYAS-KRA`) | 0.28 / 0.29 (14174) | 28.5% | -- | -- | -- [-----] | 28.2% | 29.0% | 28.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dayana Yastremska (`KXWTAMATCH-26OCT03KRAYAS-YAS`) | 0.71 / 0.72 (1023) | 71.5% | -- | -- | -- [-----] | 71.8% | 71.0% | 71.4% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; WIDE_SPREAD

## Qianhui Tang / Yifan Xu vs Gabriela Dabrowski / Luisa Stefani -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 03:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 02:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03TANYIFDABSTE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriela Dabrowski / Luisa Stefani (`KXWTADOUBLES-26OCT03TANYIFDABSTE-DABSTE`) | 0.70 / 0.76 (770) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Qianhui Tang / Yifan Xu (`KXWTADOUBLES-26OCT03TANYIFDABSTE-TANYIF`) | 0.24 / 0.28 (27) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Han Shi vs Chengyiyi Yuan -- WTA 125K Suzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: 2026-10-04 03:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 02:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02SHIYUA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Han Shi (`KXWTACHALLENGERMATCH-26OCT02SHIYUA-SHI`) | 0.87 / 0.88 (535) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chengyiyi Yuan (`KXWTACHALLENGERMATCH-26OCT02SHIYUA-YUA`) | 0.12 / 0.13 (5856) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Yidi Yang vs Rina Saigo -- WTA 125K Suzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: 2026-10-04 03:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 02:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT02YANSAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rina Saigo (`KXWTACHALLENGERMATCH-26OCT02YANSAI-SAI`) | 0.49 / 0.50 (1085) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yidi Yang (`KXWTACHALLENGERMATCH-26OCT02YANSAI-YAN`) | 0.50 / 0.52 (8739) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Katarina Zavatska vs Kristiana Sidorova -- WTA 125K Suzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 08:00Z
* Current expected start: 2026-10-04 03:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 02:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03ZAVSID:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kristiana Sidorova (`KXWTACHALLENGERMATCH-26OCT03ZAVSID-SID`) | 0.64 / 0.65 (73) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katarina Zavatska (`KXWTACHALLENGERMATCH-26OCT03ZAVSID-ZAV`) | 0.34 / 0.38 (4802) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Carlos Alcaraz vs Denis Shapovalov -- ATP Tokyo QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 05:00Z
* Current expected start: 2026-10-04 04:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 03:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-60_MIN

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-04T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT03ALCSHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlos Alcaraz (`KXATPMATCH-26OCT03ALCSHA-ALC`) | 0.88 / 0.89 (5130) | 88.5% | -- | -- | -- [-----] | -- | 88.6% | 88.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Denis Shapovalov (`KXATPMATCH-26OCT03ALCSHA-SHA`) | 0.11 / 0.12 (17887) | 11.5% | -- | -- | -- [-----] | -- | 11.8% | 11.8% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ekaterina Alexandrova vs Diana Shnaider -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 04:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03ALESHN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Alexandrova (`KXWTAMATCH-26OCT03ALESHN-ALE`) | 0.31 / 0.32 (150) | 31.5% | -- | -- | -- [-----] | 32.4% | 33.3% | 32.9% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Diana Shnaider (`KXWTAMATCH-26OCT03ALESHN-SHN`) | 0.66 / 0.68 (382) | 67.0% | -- | -- | -- [-----] | 67.6% | 66.9% | 67.2% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD

## Paula Badosa / Maria Sakkari vs Ellen Perez / Demi Schuurs -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 04:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 03:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03BADSAKPERSCH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Paula Badosa / Maria Sakkari (`KXWTADOUBLES-26OCT03BADSAKPERSCH-BADSAK`) | 0.32 / 0.37 (380) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ellen Perez / Demi Schuurs (`KXWTADOUBLES-26OCT03BADSAKPERSCH-PERSCH`) | 0.62 / 0.68 (1176) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Hubert Hurkacz vs Karen Khachanov -- ATP Beijing QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z
* Current expected start: 2026-10-04 05:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 04:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-60_MIN

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT03HURKHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hubert Hurkacz (`KXATPMATCH-26OCT03HURKHA-HUR`) | 0.42 / 0.43 (2626) | 42.5% | -- | -- | -- [-----] | 43.4% | 41.9% | 41.9% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karen Khachanov (`KXATPMATCH-26OCT03HURKHA-KHA`) | 0.57 / 0.58 (29898) | 57.5% | -- | -- | -- [-----] | 56.6% | 58.3% | 58.3% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Polina Kudermetova vs Mirra Andreeva -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 05:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 04:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03KUDAND:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mirra Andreeva (`KXWTAMATCH-26OCT03KUDAND-AND`) | 0.91 / 0.92 (14255) | 91.5% | -- | -- | -- [-----] | 89.9% | 91.8% | 91.8% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Polina Kudermetova (`KXWTAMATCH-26OCT03KUDAND-KUD`) | 0.09 / 0.10 (20514) | 9.5% | -- | -- | -- [-----] | 10.1% | 8.8% | 8.8% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rinko Matsuda vs Sijia Wei -- WTA 125K Suzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 11:50Z
* Current expected start: 2026-10-04 05:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 04:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T11:50:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03MATWEI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rinko Matsuda (`KXWTACHALLENGERMATCH-26OCT03MATWEI-MAT`) | 0.24 / 0.25 (270) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sijia Wei (`KXWTACHALLENGERMATCH-26OCT03MATWEI-WEI`) | 0.75 / 0.76 (1268) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Priska Madelyn Nugroho vs Kyoka Okamura -- WTA 125K Suzhou Q1

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 08:00Z
* Current expected start: 2026-10-04 05:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 04:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

WTA125 (WTA_125) · surface ? · scheduled 2026-10-03T08:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26OCT03NUGOKA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Priska Madelyn Nugroho (`KXWTACHALLENGERMATCH-26OCT03NUGOKA-NUG`) | 0.43 / 0.45 (3363) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kyoka Okamura (`KXWTACHALLENGERMATCH-26OCT03NUGOKA-OKA`) | 0.55 / 0.56 (884) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Rinky Hijikata / Kaito Uesugi vs Theo Arribage / Albano Olivetti -- ATP Tokyo SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 05:00Z
* Current expected start: 2026-10-04 05:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 04:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-10-04T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03HIJUESARROLI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26OCT03HIJUESARROLI-ARROLI`) | 0.62 / 0.70 (34) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rinky Hijikata / Kaito Uesugi (`KXATPDOUBLES-26OCT03HIJUESARROLI-HIJUES`) | 0.29 / 0.35 (30) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Marie Bouzkova / Ann Li vs Storm Hunter / Kristina Mladenovic -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 06:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03BOUANNHUNMLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marie Bouzkova / Ann Li (`KXWTADOUBLES-26OCT03BOUANNHUNMLA-BOUANN`) | 0.35 / 0.40 (122) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Storm Hunter / Kristina Mladenovic (`KXWTADOUBLES-26OCT03BOUANNHUNMLA-HUNMLA`) | 0.58 / 0.64 (36) | 61.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Daria Snigur vs Taylah Preston -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 06:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 05:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03SNIPRE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Taylah Preston (`KXWTAMATCH-26OCT03SNIPRE-PRE`) | 0.38 / 0.39 (1024) | 38.5% | -- | -- | -- [-----] | 39.1% | 39.1% | 39.1% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daria Snigur (`KXWTAMATCH-26OCT03SNIPRE-SNI`) | 0.60 / 0.62 (1136) | 61.0% | -- | -- | -- [-----] | 60.9% | 61.0% | 61.0% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; STALE_QUOTE; WIDE_SPREAD

## Ekaterina Alexandrova / Fanny Stollar vs Cristina Bucsa / Nicole Melichar-Martinez -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03ALESTOBUCMEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Alexandrova / Fanny Stollar (`KXWTADOUBLES-26OCT03ALESTOBUCMEL-ALESTO`) | 0.31 / 0.39 (42) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cristina Bucsa / Nicole Melichar-Martinez (`KXWTADOUBLES-26OCT03ALESTOBUCMEL-BUCMEL`) | 0.58 / 0.66 (51) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Shuko Aoyama / En-Shuo Liang vs Anna Danilina / Desirae Krawczyk -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03AOYLIADANKRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shuko Aoyama / En-Shuo Liang (`KXWTADOUBLES-26OCT03AOYLIADANKRA-AOYLIA`) | 0.06 / 0.46 (93) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Anna Danilina / Desirae Krawczyk (`KXWTADOUBLES-26OCT03AOYLIADANKRA-DANKRA`) | 0.13 / 0.59 (97) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Madison Brengle vs Julieta Pareja -- W100 Templeton CA SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03BREPAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madison Brengle (`KXITFWMATCH-26OCT03BREPAR-BRE`) | 0.27 / 0.29 (0) | 28.0% | -- | -- | -- [-----] | 28.9% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Julieta Pareja (`KXITFWMATCH-26OCT03BREPAR-PAR`) | 0.69 / 0.73 (100) | 71.0% | -- | -- | -- [-----] | 71.1% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hao-Ching Chan / Miyu (1994) Kato vs Tereza Mihalikova / Olivia Nicholls -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03CHAKATMIHNIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hao-Ching Chan / Miyu (1994) Kato (`KXWTADOUBLES-26OCT03CHAKATMIHNIC-CHAKAT`) | 0.20 / 0.47 (24) | 33.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tereza Mihalikova / Olivia Nicholls (`KXWTADOUBLES-26OCT03CHAKATMIHNIC-MIHNIC`) | 0.23 / 0.57 (96) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sara Errani / Jasmine Paolini vs Anastasia Detiuc / Fang-Hsien Wu -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03ERRPAODETFAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anastasia Detiuc / Fang-Hsien Wu (`KXWTADOUBLES-26OCT03ERRPAODETFAN-DETFAN`) | 0.17 / 0.26 (34) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sara Errani / Jasmine Paolini (`KXWTADOUBLES-26OCT03ERRPAODETFAN-ERRPAO`) | 0.52 / 0.75 (30) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Su-Wei Hsieh / Jelena Ostapenko vs Xinyu Jiang / Xiyu Wang -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03HSIOSTJIAWAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Su-Wei Hsieh / Jelena Ostapenko (`KXWTADOUBLES-26OCT03HSIOSTJIAWAN-HSIOST`) | 0.62 / 0.70 (151) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xinyu Jiang / Xiyu Wang (`KXWTADOUBLES-26OCT03HSIOSTJIAWAN-JIAWAN`) | 0.17 / 0.34 (29) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Irina Khromacheva / Liudmila Samsonova vs Jesika Maleckova / Miriam Skoch -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03KHRSAMMALSKO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Irina Khromacheva / Liudmila Samsonova (`KXWTADOUBLES-26OCT03KHRSAMMALSKO-KHRSAM`) | 0.55 / 0.62 (400) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jesika Maleckova / Miriam Skoch (`KXWTADOUBLES-26OCT03KHRSAMMALSKO-MALSKO`) | 0.36 / 0.43 (88) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Tatjana Maria vs Ella McDonald -- W100 Templeton CA SF

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03MARMCD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tatjana Maria (`KXITFWMATCH-26OCT03MARMCD-MAR`) | 0.80 / 0.81 (3504) | 80.5% | -- | -- | -- [-----] | 78.6% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ella McDonald (`KXITFWMATCH-26OCT03MARMCD-MCD`) | 0.19 / 0.20 (83) | 19.5% | -- | -- | -- [-----] | 21.4% | -- | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Caty McNally / Janice Tjen vs Nikola Bartunkova / Maja Chwalinska -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03MCCTJEBARCHW:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikola Bartunkova / Maja Chwalinska (`KXWTADOUBLES-26OCT03MCCTJEBARCHW-BARCHW`) | 0.27 / 0.31 (37) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Caty McNally / Janice Tjen (`KXWTADOUBLES-26OCT03MCCTJEBARCHW-MCCTJE`) | 0.66 / 0.73 (1013) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Linda Noskova / Clara Tauson vs Ulrikke Eikeri / Quinn Gleason -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03NOSTAUEIKGLE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ulrikke Eikeri / Quinn Gleason (`KXWTADOUBLES-26OCT03NOSTAUEIKGLE-EIKGLE`) | 0.42 / 0.48 (474) | 45.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Linda Noskova / Clara Tauson (`KXWTADOUBLES-26OCT03NOSTAUEIKGLE-NOSTAU`) | 0.51 / 0.57 (104) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Jelena Ostapenko vs Elise Mertens -- WTA Beijing R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03OSTMER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elise Mertens (`KXWTAMATCH-26OCT03OSTMER-MER`) | 0.59 / 0.62 (73) | 60.5% | -- | -- | -- [-----] | -- | 57.6% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jelena Ostapenko (`KXWTAMATCH-26OCT03OSTMER-OST`) | 0.38 / 0.39 (11) | 38.5% | -- | -- | -- [-----] | -- | 42.5% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Erin Routliffe / Aldila Sutjiadi vs Ingrid Neel / Giuliana Olmos -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03ROUSUTNEEOLM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ingrid Neel / Giuliana Olmos (`KXWTADOUBLES-26OCT03ROUSUTNEEOLM-NEEOLM`) | 0.34 / 0.41 (43) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Erin Routliffe / Aldila Sutjiadi (`KXWTADOUBLES-26OCT03ROUSUTNEEOLM-ROUSUT`) | 0.51 / 0.63 (30) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Maria Sakkari vs Elina Svitolina -- WTA Beijing R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03SAKSVI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Sakkari (`KXWTAMATCH-26OCT03SAKSVI-SAK`) | 0.17 / 0.87 (1) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elina Svitolina (`KXWTAMATCH-26OCT03SAKSVI-SVI`) | 0.16 / 0.84 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Katerina Siniakova / Shuai Zhang vs Shuo Feng / Yue Yuan -- WTA Beijing R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03SINZHAFENYUA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shuo Feng / Yue Yuan (`KXWTADOUBLES-26OCT03SINZHAFENYUA-FENYUA`) | 0.12 / 0.17 (106) | 14.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Katerina Siniakova / Shuai Zhang (`KXWTADOUBLES-26OCT03SINZHAFENYUA-SINZHA`) | 0.83 / 0.85 (6) | 84.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Donna Vekic vs Iga Swiatek -- WTA Beijing R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-10-05T04:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03VEKSWI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iga Swiatek (`KXWTAMATCH-26OCT03VEKSWI-SWI`) | 0.88 / 0.89 (723) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Donna Vekic (`KXWTAMATCH-26OCT03VEKSWI-VEK`) | 0.11 / 0.12 (266) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; STALE_QUOTE; WIDE_SPREAD

## Alex de Minaur vs Andrey Rublev -- ATP Beijing QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z
* Current expected start: 2026-10-04 06:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 05:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+30_MIN

ATP (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT03DERUB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex de Minaur (`KXATPMATCH-26OCT03DERUB-DE`) | 0.55 / 0.57 (3082) | 56.0% | -- | -- | -- [-----] | 55.6% | -- | 55.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Andrey Rublev (`KXATPMATCH-26OCT03DERUB-RUB`) | 0.40 / 0.45 (538) | 42.5% | -- | -- | -- [-----] | 44.4% | -- | 44.4% | MARKETS_AGREE | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Linda Noskova vs Viktorija Golubic -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 06:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 05:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03NOSGOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viktorija Golubic (`KXWTAMATCH-26OCT03NOSGOL-GOL`) | 0.14 / 0.15 (16588) | 14.5% | -- | -- | -- [-----] | 15.9% | 13.5% | 14.7% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Linda Noskova (`KXWTAMATCH-26OCT03NOSGOL-NOS`) | 0.85 / 0.86 (3783) | 85.5% | -- | -- | -- [-----] | 84.1% | 86.3% | 85.2% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Valentin Vacherot vs Arthur Fils -- ATP Tokyo QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 05:00Z
* Current expected start: 2026-10-04 07:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 06:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+120_MIN

ATP (TOUR_500_250) · surface ? · scheduled 2026-10-04T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26OCT03VACFIL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fils (`KXATPMATCH-26OCT03VACFIL-FIL`) | 0.78 / 0.80 (36877) | 79.0% | -- | -- | -- [-----] | 77.5% | 78.5% | 78.0% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Valentin Vacherot (`KXATPMATCH-26OCT03VACFIL-VAC`) | 0.21 / 0.22 (28080) | 21.5% | -- | -- | -- [-----] | 22.5% | 22.0% | 22.3% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sander Arends / David Pel vs Alexander Bublik / Juncheng Shang -- ATP Beijing SF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z
* Current expected start: 2026-10-04 07:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 06:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT03AREPELBUBSHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sander Arends / David Pel (`KXATPDOUBLES-26OCT03AREPELBUBSHA-AREPEL`) | 0.27 / 0.66 (3) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Bublik / Juncheng Shang (`KXATPDOUBLES-26OCT03AREPELBUBSHA-BUBSHA`) | 0.26 / 0.70 (3) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mirra Andreeva / Anna Kalinskaya vs Maya Joint / Andreja Klepac -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 07:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 06:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03ANDKALJOIKLE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mirra Andreeva / Anna Kalinskaya (`KXWTADOUBLES-26OCT03ANDKALJOIKLE-ANDKAL`) | 0.54 / 0.58 (1) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maya Joint / Andreja Klepac (`KXWTADOUBLES-26OCT03ANDKALJOIKLE-JOIKLE`) | 0.40 / 0.44 (45) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Elise Mertens / Diana Shnaider vs Maia Lumsden / Alexandra Panova -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 07:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 06:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26OCT03MERSHNLUMPAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maia Lumsden / Alexandra Panova (`KXWTADOUBLES-26OCT03MERSHNLUMPAN-LUMPAN`) | 0.29 / 0.33 (37) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Elise Mertens / Diana Shnaider (`KXWTADOUBLES-26OCT03MERSHNLUMPAN-MERSHN`) | 0.65 / 0.71 (450) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Sara Bejlek vs Naomi Osaka -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 11:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 10:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03BEJOSA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Bejlek (`KXWTAMATCH-26OCT03BEJOSA-BEJ`) | 0.26 / 0.28 (11642) | 27.0% | -- | -- | -- [-----] | 27.4% | 27.8% | 27.6% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Naomi Osaka (`KXWTAMATCH-26OCT03BEJOSA-OSA`) | 0.72 / 0.73 (170) | 72.5% | -- | -- | -- [-----] | 72.6% | 72.8% | 72.7% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Marcelo Melo / Alexander Zverev vs Julian Cash / Lloyd Glasspool -- ATP Beijing QF

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-03 06:00Z
* Current expected start: 2026-10-04 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 11:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-10-03T06:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26OCT02MELZVECASGLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julian Cash / Lloyd Glasspool (`KXATPDOUBLES-26OCT02MELZVECASGLA-CASGLA`) | 0.66 / 0.67 (43) | 66.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marcelo Melo / Alexander Zverev (`KXATPDOUBLES-26OCT02MELZVECASGLA-MELZVE`) | 0.31 / 0.33 (460) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Karolina Muchova vs Liudmila Samsonova -- WTA Beijing R32

**START STATUS: VERIFIED_UPCOMING**
* Nominal schedule: 2026-10-04 06:00Z (day placeholder, not a start time)
* Current expected start: 2026-10-04 12:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence HIGH
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-10-03 10:01Z
* Recommended handicap-by time: 2026-10-04 11:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

WTA (MASTERS_1000) · surface ? · scheduled 2026-10-04T06:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26OCT03MUCSAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karolina Muchova (`KXWTAMATCH-26OCT03MUCSAM-MUC`) | 0.76 / 0.77 (330) | 76.5% | -- | -- | -- [-----] | 75.5% | 77.3% | 76.4% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | STALE | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liudmila Samsonova (`KXWTAMATCH-26OCT03MUCSAM-SAM`) | 0.23 / 0.24 (13167) | 23.5% | -- | -- | -- [-----] | 24.5% | 23.1% | 23.8% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: NO_MODEL_FOR_MATCH; NOMINAL_START_IS_DAY_PLACEHOLDER; STALE_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
