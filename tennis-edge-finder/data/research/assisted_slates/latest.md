# ASSISTED SLATE -- 2026-11-02T07:43Z (`SL-20261102T074318Z-9a690c73`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

238 open matches not seen started, 1001 markets. Skipped: {"scheduled_start_over_24h_past": 1, "no_match_winner_listed": 2, "first_ball_already_observed": 1}. Sources: shadow board 2026-11-02T05:19:51.612143+00:00, Model 4 2026-11-02T05:20:12.009609+00:00, Gen-1 ledger 2026-11-02T05:19:47.473579+00:00, external 2026-11-02T07:20:21.609107+00:00, capture 20261102T071805Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-11-02 09:30Z**
* Recommended RUN TENNIS time: **2026-11-02 08:45Z**
* Final price/status check time: **2026-11-02 09:20Z**
* Number of matches in window: 10 (Aliona Falei vs Magda Linette, Mananchaya Sawangkaew vs Mai Hontama, Jeline Vandromme vs Kyoka Okamura, Ignacio Buse vs Zizou Bergs, Lorenzo Musetti vs Hubert Hurkacz, Luciano Darderi vs Rinky Hijikata ...)

* **31 main-tour match(es) have NO verified start status** (START_UNKNOWN, STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-11-02T07:43Z. Refresh due by: 2026-11-02 08:45Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 43, "HIGH_REVIEW": 94, "NORMAL": 514, "REVIEW": 131, "UNPRICED": 219}; match winners: {"EXTREME": 28, "HIGH_REVIEW": 50, "NORMAL": 154, "REVIEW": 58, "UNPRICED": 186}; quote freshness at build: {"FRESH": 782}.

## Leonardo Rossi vs Alessio Balestrieri -- ATP Challenger Taranto Q1

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-01T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01ROSBAL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessio Balestrieri (`KXATPCHALLENGERMATCH-26NOV01ROSBAL-BAL`) | 0.16 / 0.20 (928) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leonardo Rossi (`KXATPCHALLENGERMATCH-26NOV01ROSBAL-ROS`) | 0.81 / 0.82 (150) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Guido Andreozzi / Manuel Guinard vs Adam Pavlasek / Patrik Rikl -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 16:44Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01ANDGUIPAVRIK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guido Andreozzi / Manuel Guinard (`KXATPDOUBLES-26NOV01ANDGUIPAVRIK-ANDGUI`) | 0.29 / 0.58 (5) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Adam Pavlasek / Patrik Rikl (`KXATPDOUBLES-26NOV01ANDGUIPAVRIK-PAVRIK`) | 0.36 / 0.68 (1) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Theo Arribage / Albano Olivetti vs Julian Cash / Lloyd Glasspool -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 16:44Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01ARROLICASGLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theo Arribage / Albano Olivetti (`KXATPDOUBLES-26NOV01ARROLICASGLA-ARROLI`) | 0.05 / 0.69 (1) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Julian Cash / Lloyd Glasspool (`KXATPDOUBLES-26NOV01ARROLICASGLA-CASGLA`) | 0.17 / 0.69 (1) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Simone Bolelli / Andrea Vavassori vs Jakob Schnaitter / Mark Wallner -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 16:44Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01BOLVAVSCHWAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Simone Bolelli / Andrea Vavassori (`KXATPDOUBLES-26NOV01BOLVAVSCHWAL-BOLVAV`) | 0.36 / 0.79 (6) | 57.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jakob Schnaitter / Mark Wallner (`KXATPDOUBLES-26NOV01BOLVAVSCHWAL-SCHWAL`) | 0.13 / 0.59 (5) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Robert Cash / Brandon Nakashima vs Valentin Vacherot / Luca Van Assche -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 16:44Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01CASNAKVACVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robert Cash / Brandon Nakashima (`KXATPDOUBLES-26NOV01CASNAKVACVAN-CASNAK`) | 0.24 / 0.94 (5) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Valentin Vacherot / Luca Van Assche (`KXATPDOUBLES-26NOV01CASNAKVACVAN-VACVAN`) | 0.06 / 0.69 (33) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alejandro Davidovich Fokina vs Moise Kouame -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200221:213608:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alejandro Davidovich Fokina (`KXATPMATCH-26NOV01DAVKOU-DAV`) | 0.72 / 0.73 (97960) | 72.5% | 84.1% | 77.7% | 82.0% [79.6%-86.5%] | -- | -- | -- | -- | SHADOW_BET | +11.6 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Moise Kouame (`KXATPMATCH-26NOV01DAVKOU-KOU`) | 0.27 / 0.28 (2353) | 27.5% | 15.9% | 22.3% | 18.0% [13.5%-20.4%] | -- | -- | -- | -- | PASS | -11.6 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5501.0, B 3247.0; serve-point win A 65.8%, B 42.0%; Elo A 1995.3, B 1625.1; model uncertainty 0.0348
* Form inputs: days since last match A 14, B 11; matches on record A 568, B 83; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.022, surface_pool_high -0.021, surface_dev_loose -0.000, surface_dev_tight +0.003
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26NOV01DAVKOU-2-DAV` Will Alejandro Davidovich Fokina win set 2 in the Alejandro Davidovich Fokina vs Moise Kouame match: 0.03/0.80 mid 41.5%, model 74.7% (projection_v2.0 (prediction ledger)) -- gap +33.2 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DAVKOU-2-KOU` Will Moise Kouame win set 2 in the Alejandro Davidovich Fokina vs Moise Kouame match: 0.08/0.80 mid 44.0%, model 25.3% (projection_v2.0 (prediction ledger)) -- gap -18.7 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01DAVKOU-KOU20` Will Moise Kouame win the Alejandro Davidovich Fokina vs Moise Kouame match by a set score of 2-0?: 0.11/0.38 mid 24.5%, model 6.4% (projection_v2.0 (prediction ledger)) -- gap -18.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01DAVKOU-DAV20` Will Alejandro Davidovich Fokina win the Alejandro Davidovich Fokina vs Moise Kouame match by a set score of 2-0?: 0.24/0.54 mid 39.0%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +16.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01DAVKOU-KOU21` Will Moise Kouame win the Alejandro Davidovich Fokina vs Moise Kouame match by a set score of 2-1?: 0.08/0.38 mid 23.0%, model 9.6% (projection_v2.0 (prediction ledger)) -- gap -13.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01DAVKOU-KOU2` Will Moise Kouame win at least 1.5 more games than Alejandro Davidovich Fokina?: 0.21/0.29 mid 25.0%, model 11.8% (projection_v2.0 (prediction ledger)) -- gap -13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01DAVKOU-DAV4` Will Alejandro Davidovich Fokina win at least 3.5 more games than Moise Kouame?: 0.50/0.53 mid 51.5%, model 62.9% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DAVKOU-1-DAV` Will Alejandro Davidovich Fokina win set 1 in the Alejandro Davidovich Fokina vs Moise Kouame match: 0.64/0.68 mid 66.0%, model 74.7% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DAVKOU-1-KOU` Will Moise Kouame win set 1 in the Alejandro Davidovich Fokina vs Moise Kouame match: 0.33/0.35 mid 34.0%, model 25.3% (projection_v2.0 (prediction ledger)) -- gap -8.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01DAVKOU-DAV21` Will Alejandro Davidovich Fokina win the Alejandro Davidovich Fokina vs Moise Kouame match by a set score of 2-1?: 0.02/0.38 mid 20.0%, model 28.2% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01DAVKOU-18` Over 17.5 games: 0.72/0.83 mid 77.5%, model 84.1% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01DAVKOU-DAV7` Will Alejandro Davidovich Fokina win at least 6.5 more games than Moise Kouame?: 0.15/0.30 mid 22.5%, model 18.9% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01DAVKOU-23` Over 22.5 games: 0.47/0.48 mid 47.5%, model 45.7% (projection_v2.0 (prediction ledger)) -- gap -1.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01DAVKOU-28` Over 27.5 games: 0.21/0.35 mid 28.0%, model 27.9% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Novak Djokovic vs Valentin Vacherot -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:104925:200473:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Novak Djokovic (`KXATPMATCH-26NOV01DJOVAC-DJO`) | 0.67 / 0.69 (60316) | 68.0% | 73.9% | 71.6% | 76.6% [74.3%-82.2%] | -- | -- | -- | -- | SHADOW_BET | +5.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Valentin Vacherot (`KXATPMATCH-26NOV01DJOVAC-VAC`) | 0.32 / 0.33 (79428) | 32.5% | 26.1% | 28.4% | 23.4% [17.8%-25.7%] | -- | -- | -- | -- | PASS | -6.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4375.0, B 4676.0; serve-point win A 70.9%, B 34.5%; Elo A 2250.1, B 1896.6; model uncertainty 0.0393
* Form inputs: days since last match A 3, B 2; matches on record A 1505, B 425; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.022, surface_dev_loose -0.008, surface_dev_tight +0.016
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV01DJOVAC-DJO20` Will Novak Djokovic win the Novak Djokovic vs Valentin Vacherot match by a set score of 2-0?: 0.01/0.48 mid 24.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +19.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DJOVAC-2-DJO` Will Novak Djokovic win set 2 in the Novak Djokovic vs Valentin Vacherot match: 0.04/0.90 mid 47.0%, model 66.5% (projection_v2.0 (prediction ledger)) -- gap +19.5 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DJOVAC-2-VAC` Will Valentin Vacherot win set 2 in the Novak Djokovic vs Valentin Vacherot match: 0.14/0.79 mid 46.5%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap -13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01DJOVAC-VAC2` Will Valentin Vacherot win at least 1.5 more games than Novak Djokovic?: 0.23/0.33 mid 28.0%, model 21.3% (projection_v2.0 (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01DJOVAC-DJO21` Will Novak Djokovic win the Novak Djokovic vs Valentin Vacherot match by a set score of 2-1?: 0.16/0.31 mid 23.5%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01DJOVAC-VAC20` Will Valentin Vacherot win the Novak Djokovic vs Valentin Vacherot match by a set score of 2-0?: 0.10/0.23 mid 16.5%, model 11.2% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01DJOVAC-25` Over 24.5 games: 0.47/0.49 mid 48.0%, model 52.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DJOVAC-1-DJO` Will Novak Djokovic win set 1 in the Novak Djokovic vs Valentin Vacherot match: 0.60/0.64 mid 62.0%, model 66.5% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01DJOVAC-1-VAC` Will Valentin Vacherot win set 1 in the Novak Djokovic vs Valentin Vacherot match: 0.37/0.39 mid 38.0%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01DJOVAC-VAC21` Will Valentin Vacherot win the Novak Djokovic vs Valentin Vacherot match by a set score of 2-1?: 0.09/0.28 mid 18.5%, model 14.9% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01DJOVAC-DJO6` Will Novak Djokovic win at least 5.5 more games than Valentin Vacherot?: 0.10/0.19 mid 14.5%, model 11.1% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01DJOVAC-30` Over 29.5 games: 0.27/0.37 mid 32.0%, model 34.4% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01DJOVAC-20` Over 19.5 games: 0.80/0.85 mid 82.5%, model 84.2% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01DJOVAC-DJO3` Will Novak Djokovic win at least 2.5 more games than Valentin Vacherot?: 0.52/0.53 mid 52.5%, model 53.7% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexander Erler / Daniil Medvedev vs Kevin Krawietz / Tim Putz -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01ERLMEDKRAPUT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Erler / Daniil Medvedev (`KXATPDOUBLES-26NOV01ERLMEDKRAPUT-ERLMED`) | 0.15 / 0.94 (5) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kevin Krawietz / Tim Putz (`KXATPDOUBLES-26NOV01ERLMEDKRAPUT-KRAPUT`) | 0.06 / 0.82 (105) | 44.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Quentin Halys vs Arthur Fery -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 16:44Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111460:209259:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fery (`KXATPMATCH-26NOV01HALFER-FER`) | 0.41 / 0.42 (1256) | 41.5% | 48.2% | 52.4% | 51.9% [50.5%-52.4%] | -- | -- | -- | -- | SHADOW_BET | +6.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Quentin Halys (`KXATPMATCH-26NOV01HALFER-HAL`) | 0.58 / 0.59 (12) | 58.5% | 51.8% | 47.6% | 48.1% [47.6%-49.5%] | -- | -- | -- | -- | PASS | -6.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6422.0, B 4544.0; serve-point win A 66.5%, B 33.9%; Elo A 1834.0, B 1831.9; model uncertainty 0.0097
* Form inputs: days since last match A 6, B 2; matches on record A 840, B 267; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV01HALFER-18` Over 17.5 games: 0.64/0.94 mid 79.0%, model 95.7% (projection_v2.0 (prediction ledger)) -- gap +16.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01HALFER-HAL6` Will Quentin Halys win at least 5.5 more games than Arthur Fery?: 0.01/0.39 mid 20.0%, model 6.8% (projection_v2.0 (prediction ledger)) -- gap -13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01HALFER-HAL3` Will Quentin Halys win at least 2.5 more games than Arthur Fery?: 0.44/0.46 mid 45.0%, model 35.6% (projection_v2.0 (prediction ledger)) -- gap -9.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HALFER-2-HAL` Will Quentin Halys win set 2 in the Quentin Halys vs Arthur Fery match: 0.05/0.80 mid 42.5%, model 51.2% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HALFER-2-FER` Will Arthur Fery win set 2 in the Quentin Halys vs Arthur Fery match: 0.01/0.80 mid 40.5%, model 48.8% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01HALFER-FER2` Will Arthur Fery win at least 1.5 more games than Quentin Halys?: 0.28/0.37 mid 32.5%, model 40.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HALFER-1-HAL` Will Quentin Halys win set 1 in the Quentin Halys vs Arthur Fery match: 0.56/0.59 mid 57.5%, model 51.2% (projection_v2.0 (prediction ledger)) -- gap -6.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HALFER-HAL20` Will Quentin Halys win the Quentin Halys vs Arthur Fery match by a set score of 2-0?: 0.02/0.63 mid 32.5%, model 26.2% (projection_v2.0 (prediction ledger)) -- gap -6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01HALFER-28` Over 27.5 games: 0.13/0.62 mid 37.5%, model 43.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01HALFER-23` Over 22.5 games: 0.58/0.59 mid 58.5%, model 64.4% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HALFER-HAL21` Will Quentin Halys win the Quentin Halys vs Arthur Fery match by a set score of 2-1?: 0.01/0.39 mid 20.0%, model 25.6% (projection_v2.0 (prediction ledger)) -- gap +5.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HALFER-1-FER` Will Arthur Fery win set 1 in the Quentin Halys vs Arthur Fery match: 0.41/0.46 mid 43.5%, model 48.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HALFER-FER20` Will Arthur Fery win the Quentin Halys vs Arthur Fery match by a set score of 2-0?: 0.01/0.39 mid 20.0%, model 23.8% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HALFER-FER21` Will Arthur Fery win the Quentin Halys vs Arthur Fery match by a set score of 2-1?: 0.05/0.39 mid 22.0%, model 24.4% (projection_v2.0 (prediction ledger)) -- gap +2.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Orlando Luz / Rafael Matos vs Matteo Berrettini / Flavio Cobolli -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 13:47Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01LUZMATBERCOB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Berrettini / Flavio Cobolli (`KXATPDOUBLES-26NOV01LUZMATBERCOB-BERCOB`) | 0.06 / 0.70 (1) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Orlando Luz / Rafael Matos (`KXATPDOUBLES-26NOV01LUZMATBERCOB-LUZMAT`) | 0.38 / 0.90 (11) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alex Michelsen vs Jiri Lehecka -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208103:210506:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jiri Lehecka (`KXATPMATCH-26NOV01MICLEH-LEH`) | 0.57 / 0.58 (2080) | 57.5% | 54.2% | 55.3% | 55.3% [52.9%-59.2%] | -- | -- | -- | -- | PASS | -3.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alex Michelsen (`KXATPMATCH-26NOV01MICLEH-MIC`) | 0.42 / 0.43 (1155) | 42.5% | 45.8% | 44.7% | 44.7% [40.8%-47.1%] | -- | -- | -- | -- | PASS | +3.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5733.0, B 5638.0; serve-point win A 65.8%, B 33.3%; Elo A 1959.7, B 1984.9; model uncertainty 0.0313
* Form inputs: days since last match A 3, B 2; matches on record A 318, B 462; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.024, surface_dev_loose +0.000, surface_dev_tight -0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV01MICLEH-LEH21` Will Jiri Lehecka win the Alex Michelsen vs Jiri Lehecka match by a set score of 2-1?: 0.02/0.25 mid 13.5%, model 26.3% (projection_v2.0 (prediction ledger)) -- gap +12.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01MICLEH-23` Over 22.5 games: 0.51/0.52 mid 51.5%, model 64.2% (projection_v2.0 (prediction ledger)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01MICLEH-LEH6` Will Jiri Lehecka win at least 5.5 more games than Alex Michelsen?: 0.01/0.39 mid 20.0%, model 7.7% (projection_v2.0 (prediction ledger)) -- gap -12.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MICLEH-2-LEH` Will Jiri Lehecka win set 2 in the Alex Michelsen vs Jiri Lehecka match: 0.05/0.80 mid 42.5%, model 52.8% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MICLEH-MIC20` Will Alex Michelsen win the Alex Michelsen vs Jiri Lehecka match by a set score of 2-0?: 0.21/0.39 mid 30.0%, model 22.3% (projection_v2.0 (prediction ledger)) -- gap -7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01MICLEH-28` Over 27.5 games: 0.31/0.43 mid 37.0%, model 43.4% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01MICLEH-18` Over 17.5 games: 0.86/0.93 mid 89.5%, model 95.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01MICLEH-LEH3` Will Jiri Lehecka win at least 2.5 more games than Alex Michelsen?: 0.43/0.44 mid 43.5%, model 38.3% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MICLEH-2-MIC` Will Alex Michelsen win set 2 in the Alex Michelsen vs Jiri Lehecka match: 0.08/0.80 mid 44.0%, model 47.2% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MICLEH-1-LEH` Will Jiri Lehecka win set 1 in the Alex Michelsen vs Jiri Lehecka match: 0.54/0.57 mid 55.5%, model 52.8% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MICLEH-1-MIC` Will Alex Michelsen win set 1 in the Alex Michelsen vs Jiri Lehecka match: 0.43/0.47 mid 45.0%, model 47.2% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MICLEH-MIC21` Will Alex Michelsen win the Alex Michelsen vs Jiri Lehecka match by a set score of 2-1?: 0.12/0.39 mid 25.5%, model 23.5% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01MICLEH-MIC2` Will Alex Michelsen win at least 1.5 more games than Jiri Lehecka?: 0.31/0.41 mid 36.0%, model 37.3% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MICLEH-LEH20` Will Jiri Lehecka win the Alex Michelsen vs Jiri Lehecka match by a set score of 2-0?: 0.17/0.40 mid 28.5%, model 27.9% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lucas Miedler / Neil Oberleitner vs Marcelo Melo / Alexander Zverev -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 16:44Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01MIEOBEMELZVE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcelo Melo / Alexander Zverev (`KXATPDOUBLES-26NOV01MIEOBEMELZVE-MELZVE`) | 0.09 / 0.56 (1) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26NOV01MIEOBEMELZVE-MIEOBE`) | 0.52 / 0.92 (1) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Brandon Nakashima vs Matteo Berrettini -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 16:44Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126610:206909:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Berrettini (`KXATPMATCH-26NOV01NAKBER-BER`) | 0.41 / 0.43 (33911) | 42.0% | 40.6% | 44.0% | 44.5% [39.1%-51.9%] | -- | -- | -- | -- | PASS | -1.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Brandon Nakashima (`KXATPMATCH-26NOV01NAKBER-NAK`) | 0.57 / 0.59 (25074) | 58.0% | 59.4% | 56.0% | 55.5% [48.1%-60.9%] | -- | -- | -- | -- | PASS | +1.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6149.0, B 4151.0; serve-point win A 71.9%, B 30.1%; Elo A 1944.6, B 1907.9; model uncertainty 0.0638
* Form inputs: days since last match A 4, B 2; matches on record A 472, B 565; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.046, surface_pool_high +0.054, surface_dev_loose +0.009, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26NOV01NAKBER-2-NAK` Will Brandon Nakashima win set 2 in the Brandon Nakashima vs Matteo Berrettini match: 0.01/0.80 mid 40.5%, model 56.3% (projection_v2.0 (prediction ledger)) -- gap +15.8 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01NAKBER-NAK20` Will Brandon Nakashima win the Brandon Nakashima vs Matteo Berrettini match by a set score of 2-0?: 0.01/0.44 mid 22.5%, model 31.7% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01NAKBER-26` Over 25.5 games: 0.48/0.50 mid 49.0%, model 57.2% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01NAKBER-NAK21` Will Brandon Nakashima win the Brandon Nakashima vs Matteo Berrettini match by a set score of 2-1?: 0.01/0.39 mid 20.0%, model 27.7% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01NAKBER-21` Over 20.5 games: 0.73/0.85 mid 79.0%, model 85.2% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01NAKBER-NAK3` Will Brandon Nakashima win at least 2.5 more games than Matteo Berrettini?: 0.42/0.44 mid 43.0%, model 37.7% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01NAKBER-31` Over 30.5 games: 0.27/0.43 mid 35.0%, model 39.1% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01NAKBER-2-BER` Will Matteo Berrettini win set 2 in the Brandon Nakashima vs Matteo Berrettini match: 0.01/0.80 mid 40.5%, model 43.7% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01NAKBER-BER2` Will Matteo Berrettini win at least 1.5 more games than Brandon Nakashima?: 0.26/0.40 mid 33.0%, model 31.5% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01NAKBER-BER21` Will Matteo Berrettini win the Brandon Nakashima vs Matteo Berrettini match by a set score of 2-1?: 0.01/0.39 mid 20.0%, model 21.5% (projection_v2.0 (prediction ledger)) -- gap +1.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01NAKBER-1-NAK` Will Brandon Nakashima win set 1 in the Brandon Nakashima vs Matteo Berrettini match: 0.56/0.59 mid 57.5%, model 56.3% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01NAKBER-BER20` Will Matteo Berrettini win the Brandon Nakashima vs Matteo Berrettini match by a set score of 2-0?: 0.01/0.39 mid 20.0%, model 19.1% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01NAKBER-1-BER` Will Matteo Berrettini win set 1 in the Brandon Nakashima vs Matteo Berrettini match: 0.41/0.45 mid 43.0%, model 43.7% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Petr Nouza / Michael Venus vs Francisco Cabral / James Tracy -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01NOUVENCABTRA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cabral / James Tracy (`KXATPDOUBLES-26NOV01NOUVENCABTRA-CABTRA`) | 0.35 / 0.92 (1) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Petr Nouza / Michael Venus (`KXATPDOUBLES-26NOV01NOUVENCABTRA-NOUVEN`) | 0.05 / 0.69 (1) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Hugo Nys / Edouard Roger-Vasselin vs Sadio Doumbia / David Pel -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-01 16:44Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01NYSROGDOUPEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sadio Doumbia / David Pel (`KXATPDOUBLES-26NOV01NYSROGDOUPEL-DOUPEL`) | 0.06 / 0.68 (1) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hugo Nys / Edouard Roger-Vasselin (`KXATPDOUBLES-26NOV01NYSROGDOUPEL-NYSROG`) | 0.42 / 0.94 (6) | 68.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tommy Paul vs Holger Rune -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 16:44Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126205:208029:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tommy Paul (`KXATPMATCH-26NOV01PAURUN-PAU`) | 0.65 / 0.66 (12492) | 65.5% | 65.5% | 64.5% | 63.6% [61.7%-64.6%] | -- | -- | -- | -- | PASS | +0.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Holger Rune (`KXATPMATCH-26NOV01PAURUN-RUN`) | 0.34 / 0.35 (2188) | 34.5% | 34.4% | 35.5% | 36.4% [35.4%-38.3%] | -- | -- | -- | -- | PASS | -0.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6095.0, B 3079.0; serve-point win A 66.1%, B 37.1%; Elo A 2033.3, B 1965.0; model uncertainty 0.0143
* Form inputs: days since last match A 2, B 2; matches on record A 732, B 448; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.019, surface_dev_loose -0.009, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26NOV01PAURUN-2-PAU` Will Tommy Paul win set 2 in the Tommy Paul vs Holger Rune match: 0.01/0.80 mid 40.5%, model 60.5% (projection_v2.0 (prediction ledger)) -- gap +20.0 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01PAURUN-PAU7` Will Tommy Paul win at least 6.5 more games than Holger Rune?: 0.01/0.39 mid 20.0%, model 6.8% (projection_v2.0 (prediction ledger)) -- gap -13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01PAURUN-23` Over 22.5 games: 0.49/0.51 mid 50.0%, model 59.7% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01PAURUN-18` Over 17.5 games: 0.82/0.91 mid 86.5%, model 93.2% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01PAURUN-RUN2` Will Holger Rune win at least 1.5 more games than Tommy Paul?: 0.13/0.53 mid 33.0%, model 27.6% (projection_v2.0 (prediction ledger)) -- gap -5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01PAURUN-PAU4` Will Tommy Paul win at least 3.5 more games than Holger Rune?: 0.43/0.44 mid 43.5%, model 38.6% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01PAURUN-28` Over 27.5 games: 0.28/0.42 mid 35.0%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01PAURUN-RUN20` Will Holger Rune win the Tommy Paul vs Holger Rune match by a set score of 2-0?: 0.01/0.39 mid 20.0%, model 15.6% (projection_v2.0 (prediction ledger)) -- gap -4.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01PAURUN-1-PAU` Will Tommy Paul win set 1 in the Tommy Paul vs Holger Rune match: 0.61/0.65 mid 63.0%, model 60.5% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01PAURUN-PAU20` Will Tommy Paul win the Tommy Paul vs Holger Rune match by a set score of 2-0?: 0.01/0.69 mid 35.0%, model 36.6% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01PAURUN-2-RUN` Will Holger Rune win set 2 in the Tommy Paul vs Holger Rune match: 0.02/0.80 mid 41.0%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01PAURUN-1-RUN` Will Holger Rune win set 1 in the Tommy Paul vs Holger Rune match: 0.36/0.40 mid 38.0%, model 39.5% (projection_v2.0 (prediction ledger)) -- gap +1.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01PAURUN-RUN21` Will Holger Rune win the Tommy Paul vs Holger Rune match by a set score of 2-1?: 0.01/0.39 mid 20.0%, model 18.9% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01PAURUN-PAU21` Will Tommy Paul win the Tommy Paul vs Holger Rune match by a set score of 2-1?: 0.17/0.39 mid 28.0%, model 28.9% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arthur Rinderknech vs Francisco Cerundolo -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 16:44Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126239:202103:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cerundolo (`KXATPMATCH-26NOV01RINCER-CER`) | 0.65 / 0.66 (12870) | 65.5% | 63.9% | 62.5% | 61.1% [59.2%-63.5%] | -- | -- | -- | -- | PASS | -1.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arthur Rinderknech (`KXATPMATCH-26NOV01RINCER-RIN`) | 0.34 / 0.35 (56054) | 34.5% | 36.1% | 37.5% | 38.9% [36.5%-40.8%] | -- | -- | -- | -- | WATCH | +1.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5909.0, B 5818.0; serve-point win A 64.2%, B 32.9%; Elo A 1826.0, B 1868.6; model uncertainty 0.0213
* Form inputs: days since last match A 5, B 5; matches on record A 569, B 564; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.019, surface_dev_loose -0.004, surface_dev_tight -0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26NOV01RINCER-2-CER` Will Francisco Cerundolo win set 2 in the Arthur Rinderknech vs Francisco Cerundolo match: 0.11/0.80 mid 45.5%, model 59.4% (projection_v2.0 (prediction ledger)) -- gap +13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01RINCER-CER7` Will Francisco Cerundolo win at least 6.5 more games than Arthur Rinderknech?: 0.01/0.33 mid 17.0%, model 5.4% (projection_v2.0 (prediction ledger)) -- gap -11.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01RINCER-23` Over 22.5 games: 0.52/0.54 mid 53.0%, model 61.7% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01RINCER-CER21` Will Francisco Cerundolo win the Arthur Rinderknech vs Francisco Cerundolo match by a set score of 2-1?: 0.01/0.39 mid 20.0%, model 28.6% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01RINCER-CER4` Will Francisco Cerundolo win at least 3.5 more games than Arthur Rinderknech?: 0.42/0.43 mid 42.5%, model 35.6% (projection_v2.0 (prediction ledger)) -- gap -6.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01RINCER-28` Over 27.5 games: 0.29/0.43 mid 36.0%, model 41.3% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01RINCER-18` Over 17.5 games: 0.86/0.93 mid 89.5%, model 94.5% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01RINCER-RIN20` Will Arthur Rinderknech win the Arthur Rinderknech vs Francisco Cerundolo match by a set score of 2-0?: 0.01/0.26 mid 13.5%, model 16.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01RINCER-1-CER` Will Francisco Cerundolo win set 1 in the Arthur Rinderknech vs Francisco Cerundolo match: 0.60/0.64 mid 62.0%, model 59.4% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01RINCER-2-RIN` Will Arthur Rinderknech win set 2 in the Arthur Rinderknech vs Francisco Cerundolo match: 0.06/0.80 mid 43.0%, model 40.6% (projection_v2.0 (prediction ledger)) -- gap -2.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01RINCER-1-RIN` Will Arthur Rinderknech win set 1 in the Arthur Rinderknech vs Francisco Cerundolo match: 0.37/0.40 mid 38.5%, model 40.6% (projection_v2.0 (prediction ledger)) -- gap +2.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01RINCER-RIN2` Will Arthur Rinderknech win at least 1.5 more games than Francisco Cerundolo?: 0.21/0.35 mid 28.0%, model 28.9% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01RINCER-RIN21` Will Arthur Rinderknech win the Arthur Rinderknech vs Francisco Cerundolo match by a set score of 2-1?: 0.01/0.39 mid 20.0%, model 19.6% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01RINCER-CER20` Will Francisco Cerundolo win the Arthur Rinderknech vs Francisco Cerundolo match by a set score of 2-0?: 0.01/0.69 mid 35.0%, model 35.3% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Andrey Rublev vs Tomas Martin Etcheverry -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 16:44Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126094:144869:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tomas Martin Etcheverry (`KXATPMATCH-26NOV01RUBETC-ETC`) | 0.30 / 0.31 (36653) | 30.5% | 31.0% | 35.9% | 33.7% [31.4%-34.6%] | -- | -- | -- | -- | WATCH | +0.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andrey Rublev (`KXATPMATCH-26NOV01RUBETC-RUB`) | 0.69 / 0.71 (29952) | 70.0% | 69.0% | 64.1% | 66.3% [65.4%-68.5%] | -- | -- | -- | -- | PASS | -1.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5940.0, B 5595.0; serve-point win A 69.4%, B 34.7%; Elo A 1947.6, B 1768.9; model uncertainty 0.0157
* Form inputs: days since last match A 5, B 6; matches on record A 836, B 649; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.004, surface_dev_loose -0.001, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26NOV01RUBETC-2-RUB` Will Andrey Rublev win set 2 in the Andrey Rublev vs Tomas Martin Etcheverry match: 0.02/0.79 mid 40.5%, model 62.9% (projection_v2.0 (prediction ledger)) -- gap +22.4 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV01RUBETC-18` Over 17.5 games: 0.64/0.94 mid 79.0%, model 95.2% (projection_v2.0 (prediction ledger)) -- gap +16.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01RUBETC-RUB7` Will Andrey Rublev win at least 6.5 more games than Tomas Martin Etcheverry?: 0.01/0.37 mid 19.0%, model 5.1% (projection_v2.0 (prediction ledger)) -- gap -13.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01RUBETC-23` Over 22.5 games: 0.50/0.52 mid 51.0%, model 62.2% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01RUBETC-RUB21` Will Andrey Rublev win the Andrey Rublev vs Tomas Martin Etcheverry match by a set score of 2-1?: 0.01/0.39 mid 20.0%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +9.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01RUBETC-RUB4` Will Andrey Rublev win at least 3.5 more games than Tomas Martin Etcheverry?: 0.45/0.46 mid 45.5%, model 37.8% (projection_v2.0 (prediction ledger)) -- gap -7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01RUBETC-2-ETC` Will Tomas Martin Etcheverry win set 2 in the Andrey Rublev vs Tomas Martin Etcheverry match: 0.09/0.79 mid 44.0%, model 37.1% (projection_v2.0 (prediction ledger)) -- gap -6.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01RUBETC-ETC20` Will Tomas Martin Etcheverry win the Andrey Rublev vs Tomas Martin Etcheverry match by a set score of 2-0?: 0.02/0.38 mid 20.0%, model 13.7% (projection_v2.0 (prediction ledger)) -- gap -6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01RUBETC-RUB20` Will Andrey Rublev win the Andrey Rublev vs Tomas Martin Etcheverry match by a set score of 2-0?: 0.01/0.69 mid 35.0%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01RUBETC-ETC2` Will Tomas Martin Etcheverry win at least 1.5 more games than Andrey Rublev?: 0.02/0.54 mid 28.0%, model 24.0% (projection_v2.0 (prediction ledger)) -- gap -4.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01RUBETC-1-RUB` Will Andrey Rublev win set 1 in the Andrey Rublev vs Tomas Martin Etcheverry match: 0.65/0.68 mid 66.5%, model 62.9% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV01RUBETC-28` Over 27.5 games: 0.23/0.54 mid 38.5%, model 41.3% (projection_v2.0 (prediction ledger)) -- gap +2.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01RUBETC-ETC21` Will Tomas Martin Etcheverry win the Andrey Rublev vs Tomas Martin Etcheverry match by a set score of 2-1?: 0.02/0.38 mid 20.0%, model 17.3% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01RUBETC-1-ETC` Will Tomas Martin Etcheverry win set 1 in the Andrey Rublev vs Tomas Martin Etcheverry match: 0.32/0.37 mid 34.5%, model 37.1% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jan-Lennard Struff vs Arthur Gea -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 16:44Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:105526:210338:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Gea (`KXATPMATCH-26NOV01STRGEA-GEA`) | 0.54 / 0.57 (205) | 55.5% | 68.6% | 69.1% | 66.8% [58.4%-69.9%] | -- | -- | -- | -- | WATCH | +13.1 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jan-Lennard Struff (`KXATPMATCH-26NOV01STRGEA-STR`) | 0.43 / 0.45 (24) | 44.0% | 31.4% | 30.9% | 33.2% [30.1%-41.6%] | -- | -- | -- | -- | PASS | -12.6 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5412.0, B 5382.0; serve-point win A 62.4%, B 33.7%; Elo A 1827.8, B 1875.7; model uncertainty 0.0576
* Form inputs: days since last match A 2, B 17; matches on record A 1074, B 269; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.037, surface_pool_high -0.031, surface_dev_loose -0.026, surface_dev_tight +0.036
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26NOV01STRGEA-1-GEA` Will Arthur Gea win set 1 in the Jan-Lennard Struff vs Arthur Gea match: 0.01/0.80 mid 40.5%, model 62.7% (projection_v2.0 (prediction ledger)) -- gap +22.2 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01STRGEA-2-GEA` Will Arthur Gea win set 2 in the Jan-Lennard Struff vs Arthur Gea match: 0.01/0.80 mid 40.5%, model 62.7% (projection_v2.0 (prediction ledger)) -- gap +22.2 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01STRGEA-STR20` Will Jan-Lennard Struff win the Jan-Lennard Struff vs Arthur Gea match by a set score of 2-0?: 0.01/0.69 mid 35.0%, model 13.9% (projection_v2.0 (prediction ledger)) -- gap -21.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01STRGEA-GEA2` Will Arthur Gea win at least 1.5 more games than Jan-Lennard Struff?: 0.40/0.54 mid 47.0%, model 61.7% (projection_v2.0 (prediction ledger)) -- gap +14.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01STRGEA-STR2` Will Jan-Lennard Struff win at least 1.5 more games than Arthur Gea?: 0.35/0.41 mid 38.0%, model 24.7% (projection_v2.0 (prediction ledger)) -- gap -13.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01STRGEA-GEA5` Will Arthur Gea win at least 4.5 more games than Jan-Lennard Struff?: 0.12/0.27 mid 19.5%, model 27.6% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01STRGEA-23` Over 22.5 games: 0.47/0.57 mid 52.0%, model 58.3% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01STRGEA-GEA21` Will Arthur Gea win the Jan-Lennard Struff vs Arthur Gea match by a set score of 2-1?: 0.01/0.69 mid 35.0%, model 29.3% (projection_v2.0 (prediction ledger)) -- gap -5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01STRGEA-18` Over 17.5 games: 0.83/0.92 mid 87.5%, model 92.6% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01STRGEA-GEA20` Will Arthur Gea win the Jan-Lennard Struff vs Arthur Gea match by a set score of 2-0?: 0.01/0.69 mid 35.0%, model 39.3% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01STRGEA-28` Over 27.5 games: 0.28/0.42 mid 35.0%, model 38.5% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01STRGEA-1-STR` Will Jan-Lennard Struff win set 1 in the Jan-Lennard Struff vs Arthur Gea match: 0.01/0.80 mid 40.5%, model 37.3% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01STRGEA-2-STR` Will Jan-Lennard Struff win set 2 in the Jan-Lennard Struff vs Arthur Gea match: 0.01/0.80 mid 40.5%, model 37.3% (projection_v2.0 (prediction ledger)) -- gap -3.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01STRGEA-STR21` Will Jan-Lennard Struff win the Jan-Lennard Struff vs Arthur Gea match by a set score of 2-1?: 0.01/0.39 mid 20.0%, model 17.4% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Stefanos Tsitsipas vs Learner Tien -- ATP Paris R64

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-01 16:44Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-02T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126774:210530:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Learner Tien (`KXATPMATCH-26NOV01TSITIE-TIE`) | 0.54 / 0.56 (28242) | 55.0% | 48.6% | 50.5% | 52.0% [45.6%-55.9%] | -- | -- | -- | -- | PASS | -6.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefanos Tsitsipas (`KXATPMATCH-26NOV01TSITIE-TSI`) | 0.45 / 0.46 (38426) | 45.5% | 51.4% | 49.5% | 48.0% [44.1%-54.4%] | -- | -- | -- | -- | WATCH | +5.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5658.0, B 5484.0; serve-point win A 65.7%, B 34.6%; Elo A 1938.2, B 1985.8; model uncertainty 0.0513
* Form inputs: days since last match A 8, B 4; matches on record A 812, B 251; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.044, surface_pool_high -0.039, surface_dev_loose -0.010, surface_dev_tight +0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV01TSITIE-TSI21` Will Stefanos Tsitsipas win the Stefanos Tsitsipas vs Learner Tien match by a set score of 2-1?: 0.01/0.25 mid 13.0%, model 25.5% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TSITIE-2-TSI` Will Stefanos Tsitsipas win set 2 in the Stefanos Tsitsipas vs Learner Tien match: 0.01/0.80 mid 40.5%, model 50.9% (projection_v2.0 (prediction ledger)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV01TSITIE-24` Over 23.5 games: 0.46/0.48 mid 47.0%, model 56.1% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TSITIE-2-TIE` Will Learner Tien win set 2 in the Stefanos Tsitsipas vs Learner Tien match: 0.01/0.80 mid 40.5%, model 49.0% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01TSITIE-TIE2` Will Learner Tien win at least 1.5 more games than Stefanos Tsitsipas?: 0.48/0.50 mid 49.0%, model 40.7% (projection_v2.0 (prediction ledger)) -- gap -8.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01TSITIE-TSI20` Will Stefanos Tsitsipas win the Stefanos Tsitsipas vs Learner Tien match by a set score of 2-0?: 0.01/0.39 mid 20.0%, model 26.0% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01TSITIE-19` Over 18.5 games: 0.79/0.93 mid 86.0%, model 90.7% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01TSITIE-29` Over 28.5 games: 0.27/0.41 mid 34.0%, model 38.6% (projection_v2.0 (prediction ledger)) -- gap +4.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01TSITIE-TIE21` Will Learner Tien win the Stefanos Tsitsipas vs Learner Tien match by a set score of 2-1?: 0.01/0.39 mid 20.0%, model 24.5% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TSITIE-1-TSI` Will Stefanos Tsitsipas win set 1 in the Stefanos Tsitsipas vs Learner Tien match: 0.45/0.48 mid 46.5%, model 50.9% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01TSITIE-TIE5` Will Learner Tien win at least 4.5 more games than Stefanos Tsitsipas?: 0.11/0.25 mid 18.0%, model 13.7% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01TSITIE-TSI2` Will Stefanos Tsitsipas win at least 1.5 more games than Learner Tien?: 0.33/0.47 mid 40.0%, model 43.5% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TSITIE-1-TIE` Will Learner Tien win set 1 in the Stefanos Tsitsipas vs Learner Tien match: 0.49/0.56 mid 52.5%, model 49.0% (projection_v2.0 (prediction ledger)) -- gap -3.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01TSITIE-TIE20` Will Learner Tien win the Stefanos Tsitsipas vs Learner Tien match by a set score of 2-0?: 0.01/0.44 mid 22.5%, model 24.1% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Joaquin Aguilar Cardozo vs Hugo Dellien -- ATP Challenger Guayaquil F

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-01 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-01T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106198:212051:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joaquin Aguilar Cardozo (`KXATPCHALLENGERMATCH-26NOV01AGUDEL-AGU`) | 0.43 / 0.45 (366) | 44.0% | 26.3% | 36.1% | 27.7% [18.4%-31.3%] | -- | -- | -- | -- | PASS | -17.7 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Hugo Dellien (`KXATPCHALLENGERMATCH-26NOV01AGUDEL-DEL`) | 0.54 / 0.56 (219) | 55.0% | 73.7% | 63.9% | 72.3% [68.7%-81.6%] | -- | -- | -- | -- | WATCH | +18.7 pp | HIGH_REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2869.0, B 5486.0; serve-point win A 54.7%, B 40.5%; Elo A 1478.1, B 1778.7; model uncertainty 0.0644
* Form inputs: days since last match A 216, B 13; matches on record A 113, B 920; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV01AGUDEL-DEL  (YES = Hugo Dellien)
Model: 74%
Kalshi: 55%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.004, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NO_EXTERNAL_PRICE

## Sorana Cirstea vs Maria Timofeeva -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:201514:221237:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sorana Cirstea (`KXWTAMATCH-26NOV01CIRTIM-CIR`) | 0.67 / 0.69 (3363) | 68.0% | 66.4% | 78.9% | 78.2% [74.1%-79.3%] | -- | -- | -- | -- | SHADOW_BET | -1.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Timofeeva (`KXWTAMATCH-26NOV01CIRTIM-TIM`) | 0.31 / 0.32 (1363) | 31.5% | 33.6% | 21.1% | 21.8% [20.7%-25.9%] | -- | -- | -- | -- | PASS | +2.1 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4410.0, B 3737.0; serve-point win A 58.6%, B 44.6%; Elo A 2007.0, B 1813.9; model uncertainty 0.0258
* Form inputs: days since last match A 5, B 3; matches on record A 1064, B 362; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.008
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV01CIRTIM-21` Over 20.5 games: 0.52/0.54 mid 53.0%, model 65.6% (projection_v2.0 (prediction ledger)) -- gap +12.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01CIRTIM-26` Over 25.5 games: 0.25/0.39 mid 32.0%, model 42.6% (projection_v2.0 (prediction ledger)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV01CIRTIM-2-TIM` Will Maria Timofeeva win set 2 in the Sorana Cirstea vs Maria Timofeeva match: 0.09/0.51 mid 30.0%, model 38.9% (projection_v2.0 (prediction ledger)) -- gap +8.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01CIRTIM-16` Over 15.5 games: 0.84/0.92 mid 88.0%, model 96.8% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV01CIRTIM-1-CIR` Will Sorana Cirstea win set 1 in the Sorana Cirstea vs Maria Timofeeva match: 0.64/0.67 mid 65.5%, model 61.1% (projection_v2.0 (prediction ledger)) -- gap -4.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01CIRTIM-1-TIM` Will Maria Timofeeva win set 1 in the Sorana Cirstea vs Maria Timofeeva match: 0.33/0.37 mid 35.0%, model 38.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01CIRTIM-2-CIR` Will Sorana Cirstea win set 2 in the Sorana Cirstea vs Maria Timofeeva match: 0.39/0.91 mid 65.0%, model 61.1% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Leylah Fernandez vs Sofia Kenin -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213550:220367:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leylah Fernandez (`KXWTAMATCH-26NOV01FERKEN-FER`) | 0.69 / 0.71 (2724) | 70.0% | 81.0% | 78.7% | 77.9% [72.9%-79.0%] | -- | -- | -- | -- | WATCH | +11.0 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofia Kenin (`KXWTAMATCH-26NOV01FERKEN-KEN`) | 0.27 / 0.30 (212) | 28.5% | 19.0% | 21.3% | 22.1% [21.0%-27.1%] | -- | -- | -- | -- | PASS | -9.5 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4828.0, B 3897.0; serve-point win A 64.4%, B 42.4%; Elo A 1984.0, B 1798.5; model uncertainty 0.0305
* Form inputs: days since last match A 0, B 5; matches on record A 409, B 528; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.004, surface_dev_loose +0.011, surface_dev_tight -0.015
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTASETWINNER-26NOV01FERKEN-2-FER` Will Leylah Annie Fernandez win set 2 in the Leylah Annie Fernandez vs Sofia Kenin match: 0.27/0.94 mid 60.5%, model 73.5% (projection_v2.0 (prediction ledger)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV01FERKEN-1-FER` Will Leylah Annie Fernandez win set 1 in the Leylah Annie Fernandez vs Sofia Kenin match: 0.28/0.94 mid 61.0%, model 73.5% (projection_v2.0 (prediction ledger)) -- gap +12.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26NOV01FERKEN-22` Over 21.5 games: 0.42/0.56 mid 49.0%, model 55.1% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26NOV01FERKEN-17` Over 16.5 games: 0.79/0.93 mid 86.0%, model 92.0% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26NOV01FERKEN-27` Over 26.5 games: 0.24/0.37 mid 30.5%, model 33.1% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Talia Gibson vs Oleksandra Oliynykova -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220716:221883:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Talia Gibson (`KXWTAMATCH-26NOV01GIBOLI-GIB`) | 0.79 / 0.80 (10055) | 79.5% | 75.0% | 70.3% | 72.5% [67.7%-75.4%] | -- | -- | -- | -- | PASS | -4.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oleksandra Oliynykova (`KXWTAMATCH-26NOV01GIBOLI-OLI`) | 0.20 / 0.21 (2389) | 20.5% | 25.0% | 29.7% | 27.5% [24.6%-32.3%] | -- | -- | -- | -- | SHADOW_BET | +4.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4414.0, B 4041.0; serve-point win A 61.7%, B 43.5%; Elo A 1880.9, B 1646.2; model uncertainty 0.0386
* Form inputs: days since last match A 4, B 8; matches on record A 355, B 440; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.025, surface_dev_loose +0.029, surface_dev_tight -0.031
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV01GIBOLI-20` Over 19.5 games: 0.48/0.49 mid 48.5%, model 70.3% (projection_v2.0 (prediction ledger)) -- gap +21.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV01GIBOLI-2-GIB` Will Talia Gibson win set 2 in the Talia Gibson vs Oleksandra Oliynykova match: 0.21/0.93 mid 57.0%, model 67.4% (projection_v2.0 (prediction ledger)) -- gap +10.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01GIBOLI-25` Over 24.5 games: 0.28/0.41 mid 34.5%, model 44.2% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01GIBOLI-15` Over 14.5 games: 0.89/0.93 mid 91.0%, model 98.9% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV01GIBOLI-1-GIB` Will Talia Gibson win set 1 in the Talia Gibson vs Oleksandra Oliynykova match: 0.73/0.76 mid 74.5%, model 67.4% (projection_v2.0 (prediction ledger)) -- gap -7.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01GIBOLI-1-OLI` Will Oleksandra Oliynykova win set 1 in the Talia Gibson vs Oleksandra Oliynykova match: 0.24/0.28 mid 26.0%, model 32.6% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01GIBOLI-2-OLI` Will Oleksandra Oliynykova win set 2 in the Talia Gibson vs Oleksandra Oliynykova match: 0.20/0.51 mid 35.5%, model 32.6% (projection_v2.0 (prediction ledger)) -- gap -2.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maddison Inglis vs Maya Joint -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213666:233741:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maddison Inglis (`KXWTAMATCH-26NOV01INGJOI-ING`) | 0.26 / 0.27 (26928) | 26.5% | 35.4% | 43.2% | 41.2% [37.1%-43.2%] | -- | -- | -- | -- | SHADOW_BET | +8.9 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maya Joint (`KXWTAMATCH-26NOV01INGJOI-JOI`) | 0.74 / 0.75 (199) | 74.5% | 64.6% | 56.8% | 58.8% [56.8%-62.9%] | -- | -- | -- | -- | PASS | -9.9 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3027.0, B 3855.0; serve-point win A 56.5%, B 40.6%; Elo A 1764.9, B 1843.9; model uncertainty 0.0306
* Form inputs: days since last match A 8, B 2; matches on record A 484, B 244; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.021, surface_dev_loose +0.005, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV01INGJOI-21` Over 20.5 games: 0.51/0.52 mid 51.5%, model 66.8% (projection_v2.0 (prediction ledger)) -- gap +15.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26NOV01INGJOI-1-JOI` Will Maya Joint win set 1 in the Maddison Inglis vs Maya Joint match: 0.69/0.73 mid 71.0%, model 59.9% (projection_v2.0 (prediction ledger)) -- gap -11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV01INGJOI-1-ING` Will Maddison Inglis win set 1 in the Maddison Inglis vs Maya Joint match: 0.28/0.32 mid 30.0%, model 40.2% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26NOV01INGJOI-26` Over 25.5 games: 0.29/0.40 mid 34.5%, model 43.6% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26NOV01INGJOI-16` Over 15.5 games: 0.86/0.91 mid 88.5%, model 97.2% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alycia Parks vs Alexandra Eala -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:219917:223253:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Eala (`KXWTAMATCH-26NOV01PAREAL-EAL`) | 0.82 / 0.83 (1172) | 82.5% | 73.5% | 60.8% | 64.3% [62.8%-68.7%] | -- | -- | -- | -- | PASS | -9.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alycia Parks (`KXWTAMATCH-26NOV01PAREAL-PAR`) | 0.17 / 0.18 (5249) | 17.5% | 26.5% | 39.2% | 35.7% [31.3%-37.2%] | -- | -- | -- | -- | WATCH | +9.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5263.0, B 4541.0; serve-point win A 55.7%, B 39.5%; Elo A 1782.2, B 1956.5; model uncertainty 0.0291
* Form inputs: days since last match A 2, B 2; matches on record A 444, B 370; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose +0.000, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV01PAREAL-20` Over 19.5 games: 0.52/0.54 mid 53.0%, model 70.2% (projection_v2.0 (prediction ledger)) -- gap +17.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV01PAREAL-1-EAL` Will Alexandra Eala win set 1 in the Alycia Parks vs Alexandra Eala match: 0.75/0.79 mid 77.0%, model 66.3% (projection_v2.0 (prediction ledger)) -- gap -10.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01PAREAL-1-PAR` Will Alycia Parks win set 1 in the Alycia Parks vs Alexandra Eala match: 0.21/0.25 mid 23.0%, model 33.7% (projection_v2.0 (prediction ledger)) -- gap +10.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01PAREAL-25` Over 24.5 games: 0.29/0.39 mid 34.0%, model 44.6% (projection_v2.0 (prediction ledger)) -- gap +10.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01PAREAL-15` Over 14.5 games: 0.88/0.93 mid 90.5%, model 98.8% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV01PAREAL-2-EAL` Will Alexandra Eala win set 2 in the Alycia Parks vs Alexandra Eala match: 0.27/0.90 mid 58.5%, model 66.3% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01PAREAL-2-PAR` Will Alycia Parks win set 2 in the Alycia Parks vs Alexandra Eala match: 0.09/0.58 mid 33.5%, model 33.7% (projection_v2.0 (prediction ledger)) -- gap +0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Elena Pridankina vs Paula Badosa -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211651:239389:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Paula Badosa (`KXWTAMATCH-26NOV01PRIBAD-BAD`) | 0.74 / 0.75 (1844) | 74.5% | 72.2% | 66.4% | 71.1% [69.2%-76.7%] | -- | -- | -- | -- | PASS | -2.4 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Elena Pridankina (`KXWTAMATCH-26NOV01PRIBAD-PRI`) | 0.25 / 0.26 (1371) | 25.5% | 27.9% | 33.6% | 28.9% [23.3%-30.8%] | -- | -- | -- | -- | WATCH | +2.4 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3685.0, B 3479.0; serve-point win A 54.2%, B 41.4%; Elo A 1718.7, B 1952.1; model uncertainty 0.0372
* Form inputs: days since last match A 0, B 2; matches on record A 291, B 616; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.018, surface_dev_loose +0.014, surface_dev_tight -0.014
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTASETWINNER-26NOV01PRIBAD-2-BAD` Will Paula Badosa win set 2 in the Elena Pridankina vs Paula Badosa match: 0.02/0.93 mid 47.5%, model 65.2% (projection_v2.0 (prediction ledger)) -- gap +17.7 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV01PRIBAD-2-PRI` Will Elena Pridankina win set 2 in the Elena Pridankina vs Paula Badosa match: 0.03/0.93 mid 48.0%, model 34.8% (projection_v2.0 (prediction ledger)) -- gap -13.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26NOV01PRIBAD-21` Over 20.5 games: 0.49/0.51 mid 50.0%, model 61.7% (market_conditioned_v1 (model4_board_v1)) -- gap +11.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26NOV01PRIBAD-16` Over 15.5 games: 0.84/0.93 mid 88.5%, model 95.7% (market_conditioned_v1 (model4_board_v1)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26NOV01PRIBAD-26` Over 25.5 games: 0.29/0.37 mid 33.0%, model 39.1% (market_conditioned_v1 (model4_board_v1)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26NOV01PRIBAD-1-BAD` Will Paula Badosa win set 1 in the Elena Pridankina vs Paula Badosa match: 0.68/0.71 mid 69.5%, model 65.2% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV01PRIBAD-1-PRI` Will Elena Pridankina win set 1 in the Elena Pridankina vs Paula Badosa match: 0.29/0.33 mid 31.0%, model 34.8% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Antonia Ruzic vs Alina Charaeva -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221406:222045:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alina Charaeva (`KXWTAMATCH-26NOV01RUZCHA-CHA`) | 0.50 / 0.51 (2174) | 50.5% | 48.5% | 40.2% | 40.2% [38.2%-45.3%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Antonia Ruzic (`KXWTAMATCH-26NOV01RUZCHA-RUZ`) | 0.48 / 0.49 (103) | 48.5% | 51.5% | 59.8% | 59.8% [54.7%-61.8%] | -- | -- | -- | -- | SHADOW_BET | +3.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4066.0, B 3668.0; serve-point win A 58.7%, B 41.6%; Elo A 1841.4, B 1767.5; model uncertainty 0.0355
* Form inputs: days since last match A 5, B 1; matches on record A 363, B 333; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.020, surface_dev_loose +0.005, surface_dev_tight -0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV01RUZCHA-22` Over 21.5 games: 0.50/0.52 mid 51.0%, model 64.3% (projection_v2.0 (prediction ledger)) -- gap +13.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01RUZCHA-27` Over 26.5 games: 0.27/0.39 mid 33.0%, model 40.9% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01RUZCHA-17` Over 16.5 games: 0.81/0.93 mid 87.0%, model 94.8% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV01RUZCHA-2-CHA` Will Alina Charaeva win set 2 in the Antonia Ruzic vs Alina Charaeva match: 0.27/0.76 mid 51.5%, model 49.0% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01RUZCHA-1-CHA` Will Alina Charaeva win set 1 in the Antonia Ruzic vs Alina Charaeva match: 0.49/0.53 mid 51.0%, model 49.0% (projection_v2.0 (prediction ledger)) -- gap -2.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01RUZCHA-2-RUZ` Will Antonia Ruzic win set 2 in the Antonia Ruzic vs Alina Charaeva match: 0.27/0.78 mid 52.5%, model 51.0% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01RUZCHA-1-RUZ` Will Antonia Ruzic win set 1 in the Antonia Ruzic vs Alina Charaeva match: 0.48/0.52 mid 50.0%, model 51.0% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Himeno Sakatsume vs Tereza Valentova -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221124:238184:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Himeno Sakatsume (`KXWTAMATCH-26NOV01SAKVAL-SAK`) | 0.20 / 0.21 (2816) | 20.5% | 33.0% | 39.6% | 37.5% [32.2%-39.6%] | -- | -- | -- | -- | SHADOW_BET | +12.5 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tereza Valentova (`KXWTAMATCH-26NOV01SAKVAL-VAL`) | 0.79 / 0.80 (42) | 79.5% | 67.0% | 60.4% | 62.5% [60.4%-67.8%] | -- | -- | -- | -- | PASS | -12.5 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3693.0, B 3231.0; serve-point win A 54.8%, B 41.9%; Elo A 1766.2, B 1894.2; model uncertainty 0.037
* Form inputs: days since last match A 0, B 5; matches on record A 420, B 171; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.020, surface_dev_loose +0.000, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV01SAKVAL-21` Over 20.5 games: 0.42/0.44 mid 43.0%, model 58.5% (market_conditioned_v1 (model4_board_v1)) -- gap +15.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV01SAKVAL-2-VAL` Will Tereza Valentova win set 2 in the Himeno Sakatsume vs Tereza Valentova match: 0.02/0.93 mid 47.5%, model 61.6% (projection_v2.0 (prediction ledger)) -- gap +14.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01SAKVAL-1-VAL` Will Tereza Valentova win set 1 in the Himeno Sakatsume vs Tereza Valentova match: 0.71/0.75 mid 73.0%, model 61.6% (projection_v2.0 (prediction ledger)) -- gap -11.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01SAKVAL-1-SAK` Will Himeno Sakatsume win set 1 in the Himeno Sakatsume vs Tereza Valentova match: 0.26/0.29 mid 27.5%, model 38.5% (projection_v2.0 (prediction ledger)) -- gap +10.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01SAKVAL-2-SAK` Will Himeno Sakatsume win set 2 in the Himeno Sakatsume vs Tereza Valentova match: 0.03/0.93 mid 48.0%, model 38.5% (projection_v2.0 (prediction ledger)) -- gap -9.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01SAKVAL-16` Over 15.5 games: 0.83/0.91 mid 87.0%, model 94.7% (market_conditioned_v1 (model4_board_v1)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01SAKVAL-26` Over 25.5 games: 0.26/0.37 mid 31.5%, model 36.2% (market_conditioned_v1 (model4_board_v1)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexandra Shubladze vs Liudmila Samsonova -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214643:260168:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Liudmila Samsonova (`KXWTAMATCH-26NOV01SHUSAM-SAM`) | 0.55 / 0.57 (1064) | 56.0% | 56.9% | 24.1% | 37.0% [29.3%-61.0%] | -- | -- | -- | -- | PASS | +0.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexandra Shubladze (`KXWTAMATCH-26NOV01SHUSAM-SHU`) | 0.42 / 0.45 (68) | 43.5% | 43.1% | 75.9% | 63.0% [39.0%-70.7%] | -- | -- | -- | -- | WATCH | -0.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3247.0, B 3968.0; serve-point win A 54.8%, B 43.9%; Elo A 1759.0, B 1903.3; model uncertainty 0.1585
* Form inputs: days since last match A 0, B 8; matches on record A 209, B 541; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.015, surface_dev_loose +0.025, surface_dev_tight -0.030
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV01SHUSAM-17` Over 16.5 games: 0.03/0.93 mid 48.0%, model 93.3% (market_conditioned_v1 (model4_board_v1)) -- gap +45.3 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01SHUSAM-22` Over 21.5 games: 0.07/0.93 mid 50.0%, model 62.3% (market_conditioned_v1 (model4_board_v1)) -- gap +12.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01SHUSAM-27` Over 26.5 games: 0.03/0.93 mid 48.0%, model 39.0% (market_conditioned_v1 (model4_board_v1)) -- gap -9.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV01SHUSAM-2-SAM` Will Liudmila Samsonova win set 2 in the Alexandra Shubladze vs Liudmila Samsonova match: 0.02/0.93 mid 47.5%, model 54.6% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01SHUSAM-2-SHU` Will Alexandra Shubladze win set 2 in the Alexandra Shubladze vs Liudmila Samsonova match: 0.03/0.93 mid 48.0%, model 45.4% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01SHUSAM-1-SAM` Will Liudmila Samsonova win set 1 in the Alexandra Shubladze vs Liudmila Samsonova match: 0.36/0.69 mid 52.5%, model 54.6% (projection_v2.0 (prediction ledger)) -- gap +2.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01SHUSAM-1-SHU` Will Alexandra Shubladze win set 1 in the Alexandra Shubladze vs Liudmila Samsonova match: 0.32/0.57 mid 44.5%, model 45.4% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dayana Yastremska vs Zeynep Sonmez -- WTA Hong Kong R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215035:220309:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zeynep Sonmez (`KXWTAMATCH-26NOV01YASSON-SON`) | 0.49 / 0.50 (2212) | 49.5% | 52.9% | 64.0% | 59.5% [51.1%-61.5%] | -- | -- | -- | -- | WATCH | +3.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dayana Yastremska (`KXWTAMATCH-26NOV01YASSON-YAS`) | 0.50 / 0.51 (1855) | 50.5% | 47.1% | 36.0% | 40.5% [38.5%-48.9%] | -- | -- | -- | -- | PASS | -3.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4632.0, B 4355.0; serve-point win A 54.9%, B 44.6%; Elo A 1850.1, B 1829.1; model uncertainty 0.0523
* Form inputs: days since last match A 5, B 3; matches on record A 483, B 431; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.015, surface_dev_tight +0.021
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV01YASSON-23` Over 22.5 games: 0.43/0.45 mid 44.0%, model 55.9% (projection_v2.0 (prediction ledger)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01YASSON-18` Over 17.5 games: 0.77/0.83 mid 80.0%, model 87.5% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01YASSON-28` Over 27.5 games: 0.24/0.32 mid 28.0%, model 34.0% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV01YASSON-1-YAS` Will Dayana Yastremska win set 1 in the Dayana Yastremska vs Zeynep Sonmez match: 0.51/0.54 mid 52.5%, model 48.1% (projection_v2.0 (prediction ledger)) -- gap -4.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01YASSON-1-SON` Will Zeynep Sonmez win set 1 in the Dayana Yastremska vs Zeynep Sonmez match: 0.46/0.50 mid 48.0%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Carol Young Suh Lee vs Maria Sakkari -- WTA Hong Kong R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 07:14Z
* Source: COURT_PROGRESSION: preceding match on Centre Court in progress (set 2 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 06:29Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:206289:221803:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carol Young Suh Lee (`KXWTAMATCH-26NOV01LEESAK-LEE`) | 0.19 / 0.20 (21140) | 19.5% | 34.1% | 59.7% | 50.5% [32.4%-56.7%] | -- | 19.4% | 19.4% | MODEL_LONE_OUTLIER | WATCH | +14.6 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Maria Sakkari (`KXWTAMATCH-26NOV01LEESAK-SAK`) | 0.80 / 0.81 (3919) | 80.5% | 65.9% | 40.3% | 49.5% [43.3%-67.6%] | -- | 80.7% | 80.7% | MODEL_LONE_OUTLIER | PASS | -14.6 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4047.0, B 3640.0; serve-point win A 58.1%, B 38.8%; Elo A 1776.3, B 1936.8; model uncertainty 0.1215
* Form inputs: days since last match A 0, B 5; matches on record A 159, B 862; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.036, surface_pool_high +0.036, surface_dev_loose -0.000, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV01LEESAK-21` Over 20.5 games: 0.43/0.44 mid 43.5%, model 67.7% (projection_v2.0 (prediction ledger)) -- gap +24.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV01LEESAK-2-LEE` Will Carol Young Suh Lee win set 2 in the Carol Young Suh Lee vs Maria Sakkari match: 0.22/0.26 mid 24.0%, model 39.2% (projection_v2.0 (prediction ledger)) -- gap +15.2 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01LEESAK-2-SAK` Will Maria Sakkari win set 2 in the Carol Young Suh Lee vs Maria Sakkari match: 0.74/0.78 mid 76.0%, model 60.8% (projection_v2.0 (prediction ledger)) -- gap -15.2 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01LEESAK-1-LEE` Will Carol Young Suh Lee win set 1 in the Carol Young Suh Lee vs Maria Sakkari match: 0.24/0.25 mid 24.5%, model 39.2% (projection_v2.0 (prediction ledger)) -- gap +14.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV01LEESAK-1-SAK` Will Maria Sakkari win set 1 in the Carol Young Suh Lee vs Maria Sakkari match: 0.74/0.75 mid 74.5%, model 60.8% (projection_v2.0 (prediction ledger)) -- gap -13.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01LEESAK-26` Over 25.5 games: 0.26/0.38 mid 32.0%, model 44.3% (projection_v2.0 (prediction ledger)) -- gap +12.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV01LEESAK-16` Over 15.5 games: 0.85/0.88 mid 86.5%, model 97.6% (projection_v2.0 (prediction ledger)) -- gap +11.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Katie Volynets vs Aliaksandra Sasnovich -- WTA Hong Kong R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 07:14Z
* Source: COURT_PROGRESSION: preceding match on Court 1 in progress (set 2 of best-of-3); confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 06:29Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:205925:220465:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aliaksandra Sasnovich (`KXWTAMATCH-26NOV01VOLSAS-SAS`) | 0.58 / 0.59 (18664) | 58.5% | 44.1% | 51.1% | 50.0% [48.9%-50.5%] | -- | 56.9% | 56.9% | MODEL_LONE_OUTLIER | PASS | -14.4 pp | REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Katie Volynets (`KXWTAMATCH-26NOV01VOLSAS-VOL`) | 0.41 / 0.43 (20579) | 42.0% | 55.9% | 48.9% | 50.0% [49.5%-51.1%] | -- | 43.3% | 43.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +13.9 pp | REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5386.0, B 4822.0; serve-point win A 54.4%, B 46.7%; Elo A 1875.5, B 1851.4; model uncertainty 0.008
* Form inputs: days since last match A 5, B 0; matches on record A 454, B 798; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTASETWINNER-26NOV01VOLSAS-1-VOL` Will Katie Volynets win set 1 in the Katie Volynets vs Aliaksandra Sasnovich match: 0.43/0.44 mid 43.5%, model 54.0% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV01VOLSAS-2-VOL` Will Katie Volynets win set 2 in the Katie Volynets vs Aliaksandra Sasnovich match: 0.42/0.45 mid 43.5%, model 54.0% (projection_v2.0 (prediction ledger)) -- gap +10.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26NOV01VOLSAS-23` Over 22.5 games: 0.44/0.46 mid 45.0%, model 55.3% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26NOV01VOLSAS-2-SAS` Will Aliaksandra Sasnovich win set 2 in the Katie Volynets vs Aliaksandra Sasnovich match: 0.53/0.57 mid 55.0%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap -9.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV01VOLSAS-1-SAS` Will Aliaksandra Sasnovich win set 1 in the Katie Volynets vs Aliaksandra Sasnovich match: 0.54/0.55 mid 54.5%, model 46.0% (projection_v2.0 (prediction ledger)) -- gap -8.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26NOV01VOLSAS-28` Over 27.5 games: 0.27/0.28 mid 27.5%, model 33.2% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26NOV01VOLSAS-18` Over 17.5 games: 0.79/0.86 mid 82.5%, model 86.9% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jesika Maleckova / Miriam Skoch vs Nicole Fossa Huergo / Elena Pridankina -- WTA Hong Kong R16

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-02 09:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 09:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 08:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-02T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02MALSKOFOSPRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicole Fossa Huergo / Elena Pridankina (`KXWTADOUBLES-26NOV02MALSKOFOSPRI-FOSPRI`) | 0.48 / 0.51 (42) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jesika Maleckova / Miriam Skoch (`KXWTADOUBLES-26NOV02MALSKOFOSPRI-MALSKO`) | 0.48 / 0.50 (1528) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Ana Sofia Sanchez vs Abigayel Vosloo -- WTA 125K Luanda Q3

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 12:00Z
* Current expected start: 2026-11-02 09:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 08:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Hard · scheduled 2026-11-02T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:204419:266714:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ana Sofia Sanchez (`KXWTACHALLENGERMATCH-26NOV02SANVOS-SAN`) | 0.97 / 0.98 (2985) | 97.5% | -- | 94.1% | 88.6% [86.1%-91.0%] | -- | 94.6% | -- | INSUFFICIENT_INPUTS | PASS | -8.9 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Abigayel Vosloo (`KXWTACHALLENGERMATCH-26NOV02SANVOS-VOS`) | 0.02 / 0.03 (32431) | 2.5% | -- | 5.9% | 11.4% [9.0%-13.9%] | -- | 6.1% | 6.1% | KALSHI_LONE_OUTLIER | PASS | +8.9 pp | NORMAL | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3191.0, B 499.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0243
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.011, surface_dev_loose +0.010, surface_dev_tight -0.008
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Franziska Sziedat vs Madhurima Sawant -- WTA 125K Luanda Q2

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 12:00Z
* Current expected start: 2026-11-02 09:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 08:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Hard · scheduled 2026-11-02T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220645:261129:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Madhurima Sawant (`KXWTACHALLENGERMATCH-26NOV02SZISAW-SAW`) | 0.06 / 0.07 (44) | 6.5% | -- | 7.1% | 17.2% [11.8%-23.6%] | -- | 6.2% | 6.2% | MODEL_LONE_OUTLIER | WATCH | +10.7 pp | REVIEW | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Franziska Sziedat (`KXWTACHALLENGERMATCH-26NOV02SZISAW-SZI`) | 0.93 / 0.94 (2139) | 93.5% | -- | 92.9% | 82.8% [76.4%-88.2%] | -- | 90.8% | -- | INSUFFICIENT_INPUTS | PASS | -10.7 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2098.0, B 1045.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0591
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.018, surface_dev_loose +0.013, surface_dev_tight -0.010
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Daniel Michalski vs August Holmgren -- ATP Challenger Taipei R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-02T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200416:207415:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| August Holmgren (`KXATPCHALLENGERMATCH-26NOV02MICHOL-HOL`) | 0.72 / 0.73 (8495) | 72.5% | 62.3% | 49.5% | 53.5% [51.5%-58.4%] | -- | 59.7% | 59.7% | MODEL_LONE_OUTLIER | PASS | -10.2 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Daniel Michalski (`KXATPCHALLENGERMATCH-26NOV02MICHOL-MIC`) | 0.26 / 0.27 (1013) | 26.5% | 37.7% | 50.5% | 46.5% [41.6%-48.5%] | -- | 40.5% | 40.5% | MODEL_LONE_OUTLIER | WATCH | +11.2 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 3736.0, B 4556.0; serve-point win A 63.2%, B 34.3%; Elo A 1517.2, B 1612.6; model uncertainty 0.0346
* Form inputs: days since last match A 48, B 20; matches on record A 489, B 318; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Ekaterine Gorgodze / Maria Timofeeva vs I-Hsuan Cho / Yi Tsen Cho -- WTA Hong Kong R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-02T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02GORTIMCHOCHO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I-Hsuan Cho / Yi Tsen Cho (`KXWTADOUBLES-26NOV02GORTIMCHOCHO-CHOCHO`) | 0.18 / 0.94 (115) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ekaterine Gorgodze / Maria Timofeeva (`KXWTADOUBLES-26NOV02GORTIMCHOCHO-GORTIM`) | 0.05 / 0.80 (10) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Catherine Harrison / Dalayna Hewitt vs Hao-Ching Chan / Miyu (1994) Kato -- WTA Hong Kong R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-02T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02HARHEWCHAKAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hao-Ching Chan / Miyu (1994) Kato (`KXWTADOUBLES-26NOV02HARHEWCHAKAT-CHAKAT`) | 0.51 / 0.73 (3) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Catherine Harrison / Dalayna Hewitt (`KXWTADOUBLES-26NOV02HARHEWCHAKAT-HARHEW`) | 0.26 / 0.47 (3) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Xinyu Jiang / Hong Yi Cody Wong vs Ingrid Neel / Giuliana Olmos -- WTA Hong Kong R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-02T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02JIAWONNEEOLM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xinyu Jiang / Hong Yi Cody Wong (`KXWTADOUBLES-26NOV02JIAWONNEEOLM-JIAWON`) | 0.31 / 0.43 (47) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ingrid Neel / Giuliana Olmos (`KXWTADOUBLES-26NOV02JIAWONNEEOLM-NEEOLM`) | 0.50 / 0.62 (61) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Maria Kozyreva / Maia Lumsden vs Talia Gibson / Maddison Inglis -- WTA Hong Kong R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-02T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02KOZLUMGIBING:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Talia Gibson / Maddison Inglis (`KXWTADOUBLES-26NOV02KOZLUMGIBING-GIBING`) | 0.46 / 0.47 (1342) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Kozyreva / Maia Lumsden (`KXWTADOUBLES-26NOV02KOZLUMGIBING-KOZLUM`) | 0.53 / 0.54 (9854) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Ya-Hsuan Lee / Fang-Hsien Wu vs Venus Williams / Yifan Xu -- WTA Hong Kong R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-02T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02LEEFANWILYIF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ya-Hsuan Lee / Fang-Hsien Wu (`KXWTADOUBLES-26NOV02LEEFANWILYIF-LEEFAN`) | 0.14 / 0.92 (91) | 53.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Venus Williams / Yifan Xu (`KXWTADOUBLES-26NOV02LEEFANWILYIF-WILYIF`) | 0.08 / 0.85 (1) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Makoto Ninomiya / Ying (1998) Zhang vs Eri Hozumi / Andreja Klepac -- WTA Hong Kong R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-02T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02NINZHAHOZKLE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eri Hozumi / Andreja Klepac (`KXWTADOUBLES-26NOV02NINZHAHOZKLE-HOZKLE`) | 0.28 / 0.89 (90) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Makoto Ninomiya / Ying (1998) Zhang (`KXWTADOUBLES-26NOV02NINZHAHOZKLE-NINZHA`) | 0.11 / 0.68 (50) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Qianhui Tang / Qiu Yu Ye vs Adithya Karunaratne / Cheuk Ying Shek -- WTA Hong Kong R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-02T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02TANQIUKARSHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adithya Karunaratne / Cheuk Ying Shek (`KXWTADOUBLES-26NOV02TANQIUKARSHE-KARSHE`) | 0.16 / 0.24 (25) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Qianhui Tang / Qiu Yu Ye (`KXWTADOUBLES-26NOV02TANQIUKARSHE-TANQIU`) | 0.72 / 0.80 (1) | 76.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aliona Falei vs Magda Linette -- WTA Chennai R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 09:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 08:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:202663:221434:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aliona Falei (`KXWTAMATCH-26NOV02FALLIN-FAL`) | 0.33 / 0.35 (9835) | 34.0% | 46.6% | 77.6% | 65.3% [45.3%-71.8%] | -- | 34.3% | 34.3% | MODEL_LONE_OUTLIER | WATCH | +12.6 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Magda Linette (`KXWTAMATCH-26NOV02FALLIN-LIN`) | 0.65 / 0.66 (700) | 65.5% | 53.4% | 22.4% | 34.7% [28.2%-54.7%] | -- | 65.8% | 65.8% | MODEL_LONE_OUTLIER | PASS | -12.1 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3528.0, B 4278.0; serve-point win A 57.7%, B 41.6%; Elo A 1750.2, B 1876.0; model uncertainty 0.1325
* Form inputs: days since last match A 0, B 3; matches on record A 290, B 913; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.019, surface_dev_tight -0.025
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 4 carry a model probability
  * `KXWTASETWINNER-26NOV02FALLIN-2-FAL` Will Aliona Falei win set 2 in the Aliona Falei vs Magda Linette match: 0.35/0.38 mid 36.5%, model 47.7% (projection_v2.0 (prediction ledger)) -- gap +11.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02FALLIN-1-FAL` Will Aliona Falei win set 1 in the Aliona Falei vs Magda Linette match: 0.36/0.39 mid 37.5%, model 47.7% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02FALLIN-1-LIN` Will Magda Linette win set 1 in the Aliona Falei vs Magda Linette match: 0.61/0.63 mid 62.0%, model 52.3% (projection_v2.0 (prediction ledger)) -- gap -9.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02FALLIN-2-LIN` Will Magda Linette win set 2 in the Aliona Falei vs Magda Linette match: 0.61/0.63 mid 62.0%, model 52.3% (projection_v2.0 (prediction ledger)) -- gap -9.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER

## Mananchaya Sawangkaew vs Mai Hontama -- WTA Chennai R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 09:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 08:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215988:216566:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mai Hontama (`KXWTAMATCH-26NOV02SAWHON-HON`) | 0.38 / 0.39 (2881) | 38.5% | 30.0% | 21.3% | 23.7% [20.9%-28.8%] | -- | 38.5% | 38.5% | MODEL_LONE_OUTLIER | PASS | -8.5 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Mananchaya Sawangkaew (`KXWTAMATCH-26NOV02SAWHON-SAW`) | 0.61 / 0.62 (39) | 61.5% | 70.0% | 78.7% | 76.3% [71.2%-79.1%] | -- | 61.8% | 61.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.5 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2947.0, B 4001.0; serve-point win A 57.5%, B 46.5%; Elo A 1848.2, B 1674.7; model uncertainty 0.0397
* Form inputs: days since last match A 5, B 7; matches on record A 346, B 492; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.012, surface_dev_loose +0.012, surface_dev_tight -0.008
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV02SAWHON-21` Over 20.5 games: 0.51/0.53 mid 52.0%, model 63.4% (projection_v2.0 (prediction ledger)) -- gap +11.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV02SAWHON-26` Over 25.5 games: 0.30/0.34 mid 32.0%, model 40.6% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV02SAWHON-16` Over 15.5 games: 0.87/0.93 mid 90.0%, model 96.0% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV02SAWHON-1-SAW` Will Mananchaya Sawangkaew win set 1 in the Mananchaya Sawangkaew vs Mai Hontama match: 0.57/0.59 mid 58.0%, model 63.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02SAWHON-2-SAW` Will Mananchaya Sawangkaew win set 2 in the Mananchaya Sawangkaew vs Mai Hontama match: 0.57/0.60 mid 58.5%, model 63.7% (projection_v2.0 (prediction ledger)) -- gap +5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02SAWHON-1-HON` Will Mai Hontama win set 1 in the Mananchaya Sawangkaew vs Mai Hontama match: 0.40/0.42 mid 41.0%, model 36.3% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02SAWHON-2-HON` Will Mai Hontama win set 2 in the Mananchaya Sawangkaew vs Mai Hontama match: 0.39/0.43 mid 41.0%, model 36.3% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; WIDE_SPREAD

## Jeline Vandromme vs Kyoka Okamura -- WTA Chennai R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 09:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 08:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211846:259871:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kyoka Okamura (`KXWTAMATCH-26NOV02VANOKA-OKA`) | 0.26 / 0.27 (4342) | 26.5% | 20.8% | 8.0% | 13.7% [9.8%-26.4%] | -- | 26.7% | 26.7% | MODEL_LONE_OUTLIER | PASS | -5.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jeline Vandromme (`KXWTAMATCH-26NOV02VANOKA-VAN`) | 0.73 / 0.74 (2885) | 73.5% | 79.2% | 92.0% | 86.4% [73.6%-90.2%] | -- | 73.3% | 73.3% | MODEL_LONE_OUTLIER | WATCH | +5.8 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3468.0, B 2971.0; serve-point win A 61.4%, B 44.8%; Elo A 1787.1, B 1651.6; model uncertainty 0.0828
* Form inputs: days since last match A 8, B 0; matches on record A 131, B 630; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.003, surface_dev_loose +0.006, surface_dev_tight -0.008
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 4 carry a model probability
  * `KXWTASETWINNER-26NOV02VANOKA-1-VAN` Will Jeline Vandromme win set 1 in the Jeline Vandromme vs Kyoka Okamura match: 0.67/0.69 mid 68.0%, model 70.7% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02VANOKA-1-OKA` Will Kyoka Okamura win set 1 in the Jeline Vandromme vs Kyoka Okamura match: 0.30/0.33 mid 31.5%, model 29.3% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02VANOKA-2-VAN` Will Jeline Vandromme win set 2 in the Jeline Vandromme vs Kyoka Okamura match: 0.68/0.72 mid 70.0%, model 70.7% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02VANOKA-2-OKA` Will Kyoka Okamura win set 2 in the Jeline Vandromme vs Kyoka Okamura match: 0.28/0.31 mid 29.5%, model 29.3% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER

## Ignacio Buse vs Zizou Bergs -- ATP Paris R64

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 09:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:200267:209860:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zizou Bergs (`KXATPMATCH-26NOV01BUSBER-BER`) | 0.71 / 0.72 (1663) | 71.5% | 68.0% | 67.6% | 66.2% [64.8%-67.6%] | -- | -- | -- | -- | PASS | -3.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ignacio Buse (`KXATPMATCH-26NOV01BUSBER-BUS`) | 0.28 / 0.29 (46054) | 28.5% | 32.0% | 32.4% | 33.8% [32.4%-35.2%] | -- | -- | -- | -- | SHADOW_BET | +3.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5678.0, B 5846.0; serve-point win A 60.3%, B 36.0%; Elo A 1755.2, B 1841.6; model uncertainty 0.0138
* Form inputs: days since last match A 5, B 5; matches on record A 287, B 572; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose -0.014, surface_dev_tight +0.009
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV01BUSBER-23` Over 22.5 games: 0.45/0.46 mid 45.5%, model 56.5% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BUSBER-BER20` Will Zizou Bergs win the Ignacio Buse vs Zizou Bergs match by a set score of 2-0?: 0.49/0.50 mid 49.5%, model 38.7% (projection_v2.0 (prediction ledger)) -- gap -10.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01BUSBER-BER4` Will Zizou Bergs win at least 3.5 more games than Ignacio Buse?: 0.51/0.52 mid 51.5%, model 43.5% (projection_v2.0 (prediction ledger)) -- gap -8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01BUSBER-18` Over 17.5 games: 0.81/0.86 mid 83.5%, model 90.6% (projection_v2.0 (prediction ledger)) -- gap +7.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01BUSBER-BER7` Will Zizou Bergs win at least 6.5 more games than Ignacio Buse?: 0.13/0.20 mid 16.5%, model 9.8% (projection_v2.0 (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BUSBER-BER21` Will Zizou Bergs win the Ignacio Buse vs Zizou Bergs match by a set score of 2-1?: 0.22/0.24 mid 23.0%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01BUSBER-28` Over 27.5 games: 0.30/0.31 mid 30.5%, model 36.5% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01BUSBER-2-BUS` Will Ignacio Buse win set 2 in the Ignacio Buse vs Zizou Bergs match: 0.30/0.34 mid 32.0%, model 37.8% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BUSBER-BUS21` Will Ignacio Buse win the Ignacio Buse vs Zizou Bergs match by a set score of 2-1?: 0.11/0.14 mid 12.5%, model 17.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01BUSBER-1-BUS` Will Ignacio Buse win set 1 in the Ignacio Buse vs Zizou Bergs match: 0.32/0.34 mid 33.0%, model 37.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01BUSBER-2-BER` Will Zizou Bergs win set 2 in the Ignacio Buse vs Zizou Bergs match: 0.64/0.70 mid 67.0%, model 62.2% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01BUSBER-1-BER` Will Zizou Bergs win set 1 in the Ignacio Buse vs Zizou Bergs match: 0.65/0.68 mid 66.5%, model 62.2% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01BUSBER-BUS2` Will Ignacio Buse win at least 1.5 more games than Zizou Bergs?: 0.22/0.24 mid 23.0%, model 25.7% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01BUSBER-BUS20` Will Ignacio Buse win the Ignacio Buse vs Zizou Bergs match by a set score of 2-0?: 0.14/0.15 mid 14.5%, model 14.3% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lorenzo Musetti vs Hubert Hurkacz -- ATP Paris R64

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 09:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:128034:207518:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hubert Hurkacz (`KXATPMATCH-26NOV01MUSHUR-HUR`) | 0.50 / 0.51 (56101) | 50.5% | 48.6% | 49.0% | 51.0% [48.5%-52.4%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorenzo Musetti (`KXATPMATCH-26NOV01MUSHUR-MUS`) | 0.49 / 0.50 (32277) | 49.5% | 51.4% | 51.0% | 49.0% [47.6%-51.4%] | -- | -- | -- | -- | PASS | +1.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5110.0, B 5432.0; serve-point win A 67.3%, B 33.0%; Elo A 1949.1, B 1990.4; model uncertainty 0.0193
* Form inputs: days since last match A 3, B 4; matches on record A 490, B 691; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.014, surface_dev_loose +0.005, surface_dev_tight -0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV01MUSHUR-20` Over 19.5 games: 0.78/0.79 mid 78.5%, model 86.0% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01MUSHUR-25` Over 24.5 games: 0.50/0.51 mid 50.5%, model 56.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MUSHUR-MUS21` Will Lorenzo Musetti win the Lorenzo Musetti vs Hubert Hurkacz match by a set score of 2-1?: 0.17/0.22 mid 19.5%, model 25.4% (projection_v2.0 (prediction ledger)) -- gap +6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01MUSHUR-30` Over 29.5 games: 0.29/0.34 mid 31.5%, model 36.6% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01MUSHUR-HUR5` Will Hubert Hurkacz win at least 4.5 more games than Lorenzo Musetti?: 0.16/0.18 mid 17.0%, model 12.0% (projection_v2.0 (prediction ledger)) -- gap -5.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MUSHUR-HUR20` Will Hubert Hurkacz win the Lorenzo Musetti vs Hubert Hurkacz match by a set score of 2-0?: 0.27/0.29 mid 28.0%, model 24.1% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MUSHUR-HUR21` Will Hubert Hurkacz win the Lorenzo Musetti vs Hubert Hurkacz match by a set score of 2-1?: 0.20/0.22 mid 21.0%, model 24.5% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01MUSHUR-HUR2` Will Hubert Hurkacz win at least 1.5 more games than Lorenzo Musetti?: 0.42/0.44 mid 43.0%, model 40.3% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MUSHUR-MUS20` Will Lorenzo Musetti win the Lorenzo Musetti vs Hubert Hurkacz match by a set score of 2-0?: 0.27/0.30 mid 28.5%, model 25.9% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MUSHUR-1-HUR` Will Hubert Hurkacz win set 1 in the Lorenzo Musetti vs Hubert Hurkacz match: 0.49/0.52 mid 50.5%, model 49.1% (projection_v2.0 (prediction ledger)) -- gap -1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MUSHUR-1-MUS` Will Lorenzo Musetti win set 1 in the Lorenzo Musetti vs Hubert Hurkacz match: 0.49/0.50 mid 49.5%, model 50.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MUSHUR-2-MUS` Will Lorenzo Musetti win set 2 in the Lorenzo Musetti vs Hubert Hurkacz match: 0.47/0.52 mid 49.5%, model 50.9% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MUSHUR-2-HUR` Will Hubert Hurkacz win set 2 in the Lorenzo Musetti vs Hubert Hurkacz match: 0.47/0.50 mid 48.5%, model 49.1% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01MUSHUR-MUS2` Will Lorenzo Musetti win at least 1.5 more games than Hubert Hurkacz?: 0.42/0.44 mid 43.0%, model 43.0% (projection_v2.0 (prediction ledger)) -- gap +0.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Luciano Darderi vs Rinky Hijikata -- ATP Paris R64

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 13:00Z
* Current expected start: 2026-11-02 10:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 09:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-02T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208014:209260:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciano Darderi (`KXATPMATCH-26NOV02DARHIJ-DAR`) | 0.44 / 0.45 (1760) | 44.5% | 49.6% | 53.5% | 51.0% [49.0%-53.5%] | -- | 45.3% | 45.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +5.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Rinky Hijikata (`KXATPMATCH-26NOV02DARHIJ-HIJ`) | 0.56 / 0.57 (135885) | 56.5% | 50.4% | 46.5% | 49.0% [46.5%-51.0%] | -- | 54.7% | 54.7% | MODEL_LONE_OUTLIER | PASS | -6.1 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 6361.0, B 6001.0; serve-point win A 62.6%, B 37.3%; Elo A 1754.6, B 1817.9; model uncertainty 0.0227
* Form inputs: days since last match A 4, B 1; matches on record A 439, B 468; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose -0.020, surface_dev_tight +0.025
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV02DARHIJ-28` Over 27.5 games: 0.29/0.30 mid 29.5%, model 39.9% (projection_v2.0 (prediction ledger)) -- gap +10.3 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02DARHIJ-HIJ20` Will Rinky Hijikata win the Luciano Darderi vs Rinky Hijikata match by a set score of 2-0?: 0.31/0.34 mid 32.5%, model 25.3% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV02DARHIJ-1-DAR` Will Luciano Darderi win set 1 in the Luciano Darderi vs Rinky Hijikata match: 0.43/0.44 mid 43.5%, model 49.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV02DARHIJ-23` Over 22.5 games: 0.54/0.55 mid 54.5%, model 60.4% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV02DARHIJ-HIJ2` Will Rinky Hijikata win at least 1.5 more games than Luciano Darderi?: 0.48/0.49 mid 48.5%, model 43.1% (projection_v2.0 (prediction ledger)) -- gap -5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV02DARHIJ-1-HIJ` Will Rinky Hijikata win set 1 in the Luciano Darderi vs Rinky Hijikata match: 0.54/0.57 mid 55.5%, model 50.3% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02DARHIJ-DAR21` Will Luciano Darderi win the Luciano Darderi vs Rinky Hijikata match by a set score of 2-1?: 0.19/0.21 mid 20.0%, model 24.9% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV02DARHIJ-18` Over 17.5 games: 0.87/0.91 mid 89.0%, model 92.8% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV02DARHIJ-2-DAR` Will Luciano Darderi win set 2 in the Luciano Darderi vs Rinky Hijikata match: 0.44/0.48 mid 46.0%, model 49.7% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02DARHIJ-HIJ21` Will Rinky Hijikata win the Luciano Darderi vs Rinky Hijikata match by a set score of 2-1?: 0.20/0.23 mid 21.5%, model 25.1% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV02DARHIJ-2-HIJ` Will Rinky Hijikata win set 2 in the Luciano Darderi vs Rinky Hijikata match: 0.52/0.54 mid 53.0%, model 50.3% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV02DARHIJ-DAR2` Will Luciano Darderi win at least 1.5 more games than Rinky Hijikata?: 0.38/0.42 mid 40.0%, model 42.3% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02DARHIJ-DAR20` Will Luciano Darderi win the Luciano Darderi vs Rinky Hijikata match by a set score of 2-0?: 0.23/0.24 mid 23.5%, model 24.7% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV02DARHIJ-DAR5` Will Luciano Darderi win at least 4.5 more games than Rinky Hijikata?: 0.15/0.20 mid 17.5%, model 17.2% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE

## Joel Schwaerzler vs Jan Kumstat -- ATP Challenger Taipei R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 10:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-02T10:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211618:212082:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jan Kumstat (`KXATPCHALLENGERMATCH-26NOV02SCHKUM-KUM`) | 0.47 / 0.48 (10881) | 47.5% | 61.5% | 64.5% | 60.0% [57.6%-62.7%] | -- | 46.8% | 46.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +14.0 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Joel Schwaerzler (`KXATPCHALLENGERMATCH-26NOV02SCHKUM-SCH`) | 0.52 / 0.53 (6995) | 52.5% | 38.5% | 35.5% | 40.1% [37.3%-42.4%] | -- | 53.0% | 53.0% | MODEL_LONE_OUTLIER | PASS | -14.0 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4824.0, B 2715.0; serve-point win A 66.3%, B 31.2%; Elo A 1597.8, B 1604.4; model uncertainty 0.0252
* Form inputs: days since last match A 27, B 14; matches on record A 178, B 83; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.014, surface_dev_loose +0.001, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Venus Williams vs Mary Stoiana -- WTA Hong Kong R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 10:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 09:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:200748:223168:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mary Stoiana (`KXWTAMATCH-26NOV01WILSTO-STO`) | 0.84 / 0.85 (10628) | 84.5% | 70.4% | 87.1% | 64.9% [50.0%-74.5%] | -- | 85.9% | 85.9% | MODEL_LONE_OUTLIER | PASS | -14.1 pp | REVIEW | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Venus Williams (`KXWTAMATCH-26NOV01WILSTO-WIL`) | 0.15 / 0.16 (40871) | 15.5% | 29.6% | 12.9% | 35.1% [25.6%-50.0%] | -- | 14.8% | 14.8% | MODEL_LONE_OUTLIER | WATCH | +14.1 pp | REVIEW | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 762.0, B 2840.0; serve-point win A 55.3%, B 40.7%; Elo A 1819.2, B 1817.0; model uncertainty 0.1222
* Form inputs: days since last match A 5, B 9; matches on record A 1115, B 145; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.010, surface_dev_loose -0.010, surface_dev_tight +0.014
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV01WILSTO-20` Over 19.5 games: 0.42/0.43 mid 42.5%, model 71.1% (projection_v2.0 (prediction ledger)) -- gap +28.6 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26NOV01WILSTO-25` Over 24.5 games: 0.23/0.27 mid 25.0%, model 45.6% (projection_v2.0 (prediction ledger)) -- gap +20.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26NOV01WILSTO-2-WIL` Will Venus Williams win set 2 in the Venus Williams vs Mary Stoiana match: 0.16/0.23 mid 19.5%, model 36.0% (projection_v2.0 (prediction ledger)) -- gap +16.6 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV01WILSTO-1-STO` Will Mary Stoiana win set 1 in the Venus Williams vs Mary Stoiana match: 0.78/0.80 mid 79.0%, model 63.9% (projection_v2.0 (prediction ledger)) -- gap -15.1 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV01WILSTO-1-WIL` Will Venus Williams win set 1 in the Venus Williams vs Mary Stoiana match: 0.20/0.22 mid 21.0%, model 36.0% (projection_v2.0 (prediction ledger)) -- gap +15.1 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26NOV01WILSTO-15` Over 14.5 games: 0.87/0.91 mid 89.0%, model 98.8% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26NOV01WILSTO-2-STO` Will Mary Stoiana win set 2 in the Venus Williams vs Mary Stoiana match: 0.64/0.81 mid 72.5%, model 63.9% (projection_v2.0 (prediction ledger)) -- gap -8.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mei Yamaguchi vs Zhibek Kulambayeva -- WTA Chennai R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 13:40Z
* Current expected start: 2026-11-02 10:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 09:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-190_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T13:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214992:215614:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zhibek Kulambayeva (`KXWTAMATCH-26NOV02YAMKUL-KUL`) | 0.37 / 0.38 (664) | 37.5% | 40.0% | 60.5% | 48.4% [42.6%-53.2%] | -- | 40.4% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +2.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mei Yamaguchi (`KXWTAMATCH-26NOV02YAMKUL-YAM`) | 0.61 / 0.63 (714) | 62.0% | 60.0% | 39.5% | 51.6% [46.8%-57.4%] | -- | 60.3% | -- | INSUFFICIENT_INPUTS | PASS | -2.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3409.0, B 2176.0; serve-point win A 56.0%, B 46.0%; Elo A 1582.1, B 1450.8; model uncertainty 0.0529
* Form inputs: days since last match A 1, B 1; matches on record A 353, B 436; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.021, surface_dev_loose +0.026, surface_dev_tight -0.016
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 4 carry a model probability
  * `KXWTASETWINNER-26NOV02YAMKUL-2-YAM` Will Mei Yamaguchi win set 2 in the Mei Yamaguchi vs Zhibek Kulambayeva match: 0.03/0.93 mid 48.0%, model 56.7% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02YAMKUL-2-KUL` Will Zhibek Kulambayeva win set 2 in the Mei Yamaguchi vs Zhibek Kulambayeva match: 0.03/0.93 mid 48.0%, model 43.3% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02YAMKUL-1-KUL` Will Zhibek Kulambayeva win set 1 in the Mei Yamaguchi vs Zhibek Kulambayeva match: 0.35/0.43 mid 39.0%, model 43.3% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02YAMKUL-1-YAM` Will Mei Yamaguchi win set 1 in the Mei Yamaguchi vs Zhibek Kulambayeva match: 0.54/0.60 mid 57.0%, model 56.7% (projection_v2.0 (prediction ledger)) -- gap -0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Linda Fruhvirtova vs Weronika Falkowska -- WTA Chennai R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 13:40Z
* Current expected start: 2026-11-02 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 10:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T13:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:216579:222258:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weronika Falkowska (`KXWTAMATCH-26NOV02FRUFAL-FAL`) | 0.34 / 0.35 (113) | 34.5% | 30.8% | 53.7% | 41.6% [34.1%-46.3%] | -- | -- | -- | -- | WATCH | -3.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Linda Fruhvirtova (`KXWTAMATCH-26NOV02FRUFAL-FRU`) | 0.64 / 0.65 (608) | 64.5% | 69.2% | 46.3% | 58.4% [53.7%-66.0%] | -- | -- | -- | -- | PASS | +4.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4353.0, B 2031.0; serve-point win A 58.3%, B 45.5%; Elo A 1758.5, B 1582.4; model uncertainty 0.0613
* Form inputs: days since last match A 8, B 0; matches on record A 299, B 374; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.015, surface_dev_loose -0.016, surface_dev_tight +0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 4 carry a model probability
  * `KXWTASETWINNER-26NOV02FRUFAL-2-FRU` Will Linda Fruhvirtova win set 2 in the Linda Fruhvirtova vs Weronika Falkowska match: 0.56/0.64 mid 60.0%, model 63.1% (projection_v2.0 (prediction ledger)) -- gap +3.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02FRUFAL-1-FAL` Will Weronika Falkowska win set 1 in the Linda Fruhvirtova vs Weronika Falkowska match: 0.37/0.40 mid 38.5%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap -1.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02FRUFAL-1-FRU` Will Linda Fruhvirtova win set 1 in the Linda Fruhvirtova vs Weronika Falkowska match: 0.60/0.63 mid 61.5%, model 63.1% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02FRUFAL-2-FAL` Will Weronika Falkowska win set 2 in the Linda Fruhvirtova vs Weronika Falkowska match: 0.32/0.40 mid 36.0%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Isabella Shinikova vs Dune Vaissaud -- WTA 125K Luanda R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 14:00Z
* Current expected start: 2026-11-02 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 10:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Hard · scheduled 2026-11-02T14:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:202688:266642:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isabella Shinikova (`KXWTACHALLENGERMATCH-26NOV02SHIVAI-SHI`) | 0.53 / 0.54 (372) | 53.5% | -- | 53.7% | 59.9% [56.8%-65.0%] | -- | 54.7% | -- | INSUFFICIENT_INPUTS | WATCH | +6.4 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Dune Vaissaud (`KXWTACHALLENGERMATCH-26NOV02SHIVAI-VAI`) | 0.46 / 0.47 (1215) | 46.5% | -- | 46.3% | 40.1% [35.0%-43.2%] | -- | 45.4% | -- | INSUFFICIENT_INPUTS | PASS | -6.4 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3553.0, B 2429.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0407
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE

## Moyuka Uchijima vs Rebecca Sramkova -- WTA Chennai R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 10:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211685:220416:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rebecca Sramkova (`KXWTAMATCH-26NOV02UCHSRA-SRA`) | 0.59 / 0.60 (8) | 59.5% | 51.3% | 46.3% | 48.9% [46.8%-55.3%] | -- | 60.3% | 60.3% | MODEL_LONE_OUTLIER | PASS | -8.2 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Moyuka Uchijima (`KXWTAMATCH-26NOV02UCHSRA-UCH`) | 0.40 / 0.41 (9216) | 40.5% | 48.6% | 53.7% | 51.0% [44.7%-53.2%] | -- | 40.2% | 40.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.2 pp | NORMAL | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4591.0, B 4339.0; serve-point win A 56.7%, B 43.0%; Elo A 1740.3, B 1774.5; model uncertainty 0.0421
* Form inputs: days since last match A 6, B 21; matches on record A 476, B 638; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.021, surface_dev_loose +0.005, surface_dev_tight +0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV02UCHSRA-22` Over 21.5 games: 0.51/0.52 mid 51.5%, model 63.3% (projection_v2.0 (prediction ledger)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26NOV02UCHSRA-1-UCH` Will Moyuka Uchijima win set 1 in the Moyuka Uchijima vs Rebecca Sramkova match: 0.40/0.42 mid 41.0%, model 49.1% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV02UCHSRA-2-UCH` Will Moyuka Uchijima win set 2 in the Moyuka Uchijima vs Rebecca Sramkova match: 0.38/0.44 mid 41.0%, model 49.1% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTAGTOTAL-26NOV02UCHSRA-17` Over 16.5 games: 0.84/0.88 mid 86.0%, model 94.0% (projection_v2.0 (prediction ledger)) -- gap +8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26NOV02UCHSRA-27` Over 26.5 games: 0.31/0.33 mid 32.0%, model 39.9% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26NOV02UCHSRA-1-SRA` Will Rebecca Sramkova win set 1 in the Moyuka Uchijima vs Rebecca Sramkova match: 0.57/0.58 mid 57.5%, model 50.9% (projection_v2.0 (prediction ledger)) -- gap -6.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV02UCHSRA-2-SRA` Will Rebecca Sramkova win set 2 in the Moyuka Uchijima vs Rebecca Sramkova match: 0.55/0.58 mid 56.5%, model 50.9% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Austin Krajicek / Nikola Mektic vs Quentin Halys / Pierre-Hugues Herbert -- ATP Paris R32

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 10:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01KRAMEKHALHER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Quentin Halys / Pierre-Hugues Herbert (`KXATPDOUBLES-26NOV01KRAMEKHALHER-HALHER`) | 0.48 / 0.51 (1330) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Austin Krajicek / Nikola Mektic (`KXATPDOUBLES-26NOV01KRAMEKHALHER-KRAMEK`) | 0.48 / 0.51 (1000) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Alejandro Tabilo vs Rafael Jodar -- ATP Paris R64

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 10:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126214:212588:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael Jodar (`KXATPMATCH-26NOV01TABJOD-JOD`) | 0.79 / 0.80 (1364) | 79.5% | 72.6% | 70.9% | 71.8% [70.1%-72.2%] | -- | -- | -- | -- | PASS | -6.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alejandro Tabilo (`KXATPMATCH-26NOV01TABJOD-TAB`) | 0.20 / 0.21 (63534) | 20.5% | 27.4% | 29.1% | 28.2% [27.8%-29.9%] | -- | -- | -- | -- | SHADOW_BET | +6.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6132.0, B 5268.0; serve-point win A 61.3%, B 33.9%; Elo A 1836.1, B 2015.9; model uncertainty 0.0105
* Form inputs: days since last match A 5, B 3; matches on record A 655, B 142; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.004, surface_dev_loose -0.004, surface_dev_tight +0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV01TABJOD-JOD20` Will Rafael Jodar win the Alejandro Tabilo vs Rafael Jodar match by a set score of 2-0?: 0.58/0.59 mid 58.5%, model 43.0% (projection_v2.0 (prediction ledger)) -- gap -15.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01TABJOD-JOD5` Will Rafael Jodar win at least 4.5 more games than Alejandro Tabilo?: 0.46/0.47 mid 46.5%, model 32.0% (projection_v2.0 (prediction ledger)) -- gap -14.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01TABJOD-22` Over 21.5 games: 0.49/0.50 mid 49.5%, model 64.0% (projection_v2.0 (prediction ledger)) -- gap +14.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01TABJOD-27` Over 26.5 games: 0.29/0.31 mid 30.0%, model 39.8% (projection_v2.0 (prediction ledger)) -- gap +9.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TABJOD-2-TAB` Will Alejandro Tabilo win set 2 in the Alejandro Tabilo vs Rafael Jodar match: 0.23/0.29 mid 26.0%, model 34.5% (projection_v2.0 (prediction ledger)) -- gap +8.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01TABJOD-JOD8` Will Rafael Jodar win at least 7.5 more games than Alejandro Tabilo?: 0.09/0.15 mid 12.0%, model 4.0% (projection_v2.0 (prediction ledger)) -- gap -8.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TABJOD-2-JOD` Will Rafael Jodar win set 2 in the Alejandro Tabilo vs Rafael Jodar match: 0.71/0.76 mid 73.5%, model 65.5% (projection_v2.0 (prediction ledger)) -- gap -8.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01TABJOD-JOD21` Will Rafael Jodar win the Alejandro Tabilo vs Rafael Jodar match by a set score of 2-1?: 0.20/0.24 mid 22.0%, model 29.6% (projection_v2.0 (prediction ledger)) -- gap +7.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01TABJOD-JOD2` Will Rafael Jodar win at least 1.5 more games than Alejandro Tabilo?: 0.72/0.75 mid 73.5%, model 66.0% (projection_v2.0 (prediction ledger)) -- gap -7.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01TABJOD-17` Over 16.5 games: 0.87/0.92 mid 89.5%, model 96.1% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TABJOD-1-TAB` Will Alejandro Tabilo win set 1 in the Alejandro Tabilo vs Rafael Jodar match: 0.27/0.29 mid 28.0%, model 34.5% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01TABJOD-TAB21` Will Alejandro Tabilo win the Alejandro Tabilo vs Rafael Jodar match by a set score of 2-1?: 0.08/0.11 mid 9.5%, model 15.6% (projection_v2.0 (prediction ledger)) -- gap +6.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01TABJOD-1-JOD` Will Rafael Jodar win set 1 in the Alejandro Tabilo vs Rafael Jodar match: 0.70/0.73 mid 71.5%, model 65.5% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01TABJOD-TAB20` Will Alejandro Tabilo win the Alejandro Tabilo vs Rafael Jodar match by a set score of 2-0?: 0.09/0.11 mid 10.0%, model 11.9% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Luca Van Assche vs Mariano Navone -- ATP Paris R64

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 11:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 10:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:208363:209414:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mariano Navone (`KXATPMATCH-26NOV01VANNAV-NAV`) | 0.42 / 0.43 (45164) | 42.5% | 44.4% | 46.9% | 45.4% [43.3%-47.4%] | -- | -- | -- | -- | WATCH | +1.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luca Van Assche (`KXATPMATCH-26NOV01VANNAV-VAN`) | 0.57 / 0.58 (2475) | 57.5% | 55.6% | 53.1% | 54.6% [52.6%-56.7%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6040.0, B 5714.0; serve-point win A 60.0%, B 41.1%; Elo A 1801.5, B 1721.0; model uncertainty 0.0204
* Form inputs: days since last match A 6, B 6; matches on record A 394, B 433; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.020, surface_dev_tight -0.021
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV01VANNAV-VAN20` Will Luca Van Assche win the Luca Van Assche vs Mariano Navone match by a set score of 2-0?: 0.33/0.36 mid 34.5%, model 28.9% (projection_v2.0 (prediction ledger)) -- gap -5.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01VANNAV-NAV21` Will Mariano Navone win the Luca Van Assche vs Mariano Navone match by a set score of 2-1?: 0.16/0.19 mid 17.5%, model 23.0% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01VANNAV-24` Over 23.5 games: 0.47/0.48 mid 47.5%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01VANNAV-VAN2` Will Luca Van Assche win at least 1.5 more games than Mariano Navone?: 0.52/0.54 mid 53.0%, model 48.8% (projection_v2.0 (prediction ledger)) -- gap -4.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01VANNAV-VAN5` Will Luca Van Assche win at least 4.5 more games than Mariano Navone?: 0.26/0.29 mid 27.5%, model 23.7% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01VANNAV-VAN21` Will Luca Van Assche win the Luca Van Assche vs Mariano Navone match by a set score of 2-1?: 0.21/0.25 mid 23.0%, model 26.7% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01VANNAV-29` Over 28.5 games: 0.27/0.29 mid 28.0%, model 31.4% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01VANNAV-19` Over 18.5 games: 0.79/0.82 mid 80.5%, model 83.7% (projection_v2.0 (prediction ledger)) -- gap +3.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01VANNAV-2-NAV` Will Mariano Navone win set 2 in the Luca Van Assche vs Mariano Navone match: 0.41/0.47 mid 44.0%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap +2.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01VANNAV-2-VAN` Will Luca Van Assche win set 2 in the Luca Van Assche vs Mariano Navone match: 0.53/0.59 mid 56.0%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01VANNAV-NAV20` Will Mariano Navone win the Luca Van Assche vs Mariano Navone match by a set score of 2-0?: 0.22/0.25 mid 23.5%, model 21.4% (projection_v2.0 (prediction ledger)) -- gap -2.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01VANNAV-1-NAV` Will Mariano Navone win set 1 in the Luca Van Assche vs Mariano Navone match: 0.44/0.46 mid 45.0%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01VANNAV-1-VAN` Will Luca Van Assche win set 1 in the Luca Van Assche vs Mariano Navone match: 0.53/0.56 mid 54.5%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01VANNAV-NAV2` Will Mariano Navone win at least 1.5 more games than Luca Van Assche?: 0.36/0.38 mid 37.0%, model 37.6% (projection_v2.0 (prediction ledger)) -- gap +0.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Francisco Cerundolo / Tomas Martin Etcheverry vs Marc Polmans / Jan Zielinski -- ATP Paris R32

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 12:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 11:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01CERETCPOLZIE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cerundolo / Tomas Martin Etcheverry (`KXATPDOUBLES-26NOV01CERETCPOLZIE-CERETC`) | 0.30 / 0.33 (25) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marc Polmans / Jan Zielinski (`KXATPDOUBLES-26NOV01CERETCPOLZIE-POLZIE`) | 0.65 / 0.69 (723) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Xinyu Wang vs Adithya Karunaratne -- WTA Hong Kong R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 05:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 12:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 11:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · surface ? · scheduled 2026-11-02T05:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:26NOV01WANKAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adithya Karunaratne (`KXWTAMATCH-26NOV01WANKAR-KAR`) | 0.08 / 0.09 (6109) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xinyu Wang (`KXWTAMATCH-26NOV01WANKAR-WAN`) | 0.91 / 0.92 (3436) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Isabelle Haverlag / Panna Udvardy vs Mana Ayukawa / Emily Webley-Smith -- WTA Chennai R16

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 12:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 11:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-02T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02HAVUDVAYUWEB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mana Ayukawa / Emily Webley-Smith (`KXWTADOUBLES-26NOV02HAVUDVAYUWEB-AYUWEB`) | 0.22 / 0.25 (27) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Isabelle Haverlag / Panna Udvardy (`KXWTADOUBLES-26NOV02HAVUDVAYUWEB-HAVUDV`) | 0.74 / 0.77 (1070) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Warona Mdlulwa vs Kristina Novak -- WTA 125K Luanda R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 14:20Z
* Current expected start: 2026-11-02 12:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 11:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Hard · scheduled 2026-11-02T14:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214503:216038:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Warona Mdlulwa (`KXWTACHALLENGERMATCH-26NOV02MDLNOV-MDL`) | 0.04 / 0.05 (300) | 4.5% | -- | 33.9% | 20.3% [17.5%-22.2%] | -- | 3.5% | 3.5% | MODEL_LONE_OUTLIER | PASS | +15.8 pp | HIGH_REVIEW | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Kristina Novak (`KXWTACHALLENGERMATCH-26NOV02MDLNOV-NOV`) | 0.95 / 0.96 (493) | 95.5% | -- | 66.1% | 79.7% [77.8%-82.5%] | -- | 96.2% | 96.2% | MODEL_LONE_OUTLIER | PASS | -15.8 pp | HIGH_REVIEW | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 302.0, B 994.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0236
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26NOV02MDLNOV-MDL  (YES = Warona Mdlulwa)
Model: 20%
Kalshi: 4%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose -0.004, surface_dev_tight +0.008
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Massimo Giunta vs Adrian Andreev -- ATP Challenger Taranto Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202090:210668:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Adrian Andreev (`KXATPCHALLENGERMATCH-26NOV02GIUAND-AND`) | 0.42 / 0.43 (4245) | 42.5% | 57.9% | 45.5% | 56.5% [52.5%-62.9%] | -- | 44.6% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +15.4 pp | HIGH_REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Massimo Giunta (`KXATPCHALLENGERMATCH-26NOV02GIUAND-GIU`) | 0.56 / 0.57 (107) | 56.5% | 42.1% | 54.5% | 43.5% [37.1%-47.5%] | -- | 57.5% | 57.5% | MODEL_LONE_OUTLIER | PASS | -14.4 pp | REVIEW | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3654.0, B 2392.0; serve-point win A 61.6%, B 36.8%; Elo A 1469.9, B 1645.1; model uncertainty 0.0519
* Form inputs: days since last match A 13, B 41; matches on record A 179, B 361; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV02GIUAND-AND  (YES = Adrian Andreev)
Model: 58%
Kalshi: 42%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Loann Massard vs Ziga Sesko -- ATP Challenger Taranto Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210604:212949:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Loann Massard (`KXATPCHALLENGERMATCH-26NOV02MASSES-MAS`) | 0.32 / 0.33 (312) | 32.5% | 62.7% | 63.0% | 58.6% [56.6%-60.1%] | -- | 32.3% | 32.3% | MODEL_LONE_OUTLIER | PASS | +30.2 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Ziga Sesko (`KXATPCHALLENGERMATCH-26NOV02MASSES-SES`) | 0.66 / 0.67 (4000) | 66.5% | 37.3% | 37.0% | 41.4% [39.9%-43.4%] | -- | 68.3% | 68.3% | MODEL_LONE_OUTLIER | PASS | -29.2 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3485.0, B 731.0; serve-point win A 63.1%, B 39.5%; Elo A 1372.0, B 1333.9; model uncertainty 0.0175
* Form inputs: days since last match A 223, B 61; matches on record A 152, B 28; data quality D

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV02MASSES-MAS  (YES = Loann Massard)
Model: 63%
Kalshi: 32%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER

## Tiago Pereira vs Peter Makk -- ATP Challenger Taranto Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207407:211500:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Peter Makk (`KXATPCHALLENGERMATCH-26NOV02PERMAK-MAK`) | 0.32 / 0.33 (233) | 32.5% | 50.2% | 67.2% | 56.1% [49.0%-62.0%] | -- | 33.5% | 33.5% | MODEL_LONE_OUTLIER | WATCH | +17.7 pp | HIGH_REVIEW | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Tiago Pereira (`KXATPCHALLENGERMATCH-26NOV02PERMAK-PER`) | 0.65 / 0.66 (265) | 65.5% | 49.8% | 32.8% | 43.9% [38.0%-51.0%] | -- | 66.5% | 66.5% | MODEL_LONE_OUTLIER | PASS | -15.7 pp | HIGH_REVIEW | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4590.0, B 2061.0; serve-point win A 62.0%, B 38.0%; Elo A 1550.4, B 1480.1; model uncertainty 0.065
* Form inputs: days since last match A 103, B 43; matches on record A 266, B 82; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV02PERMAK-MAK  (YES = Peter Makk)
Model: 50%
Kalshi: 32%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Leonardo Rossi vs Nico Hipfl -- ATP Challenger Taranto Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 12:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210223:211503:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nico Hipfl (`KXATPCHALLENGERMATCH-26NOV02ROSHIP-HIP`) | 0.41 / 0.42 (1913) | 41.5% | 44.2% | 50.5% | 43.5% [41.5%-45.5%] | -- | 44.9% | 44.9% | MARKETS_AGREE | PASS | +2.7 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |
| Leonardo Rossi (`KXATPCHALLENGERMATCH-26NOV02ROSHIP-ROS`) | 0.57 / 0.59 (2020) | 58.0% | 55.8% | 49.5% | 56.5% [54.5%-58.5%] | -- | 58.3% | -- | INSUFFICIENT_INPUTS | PASS | -2.2 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2379.0, B 866.0; serve-point win A 63.3%, B 37.9%; Elo A 1347.0, B 1272.9; model uncertainty 0.02
* Form inputs: days since last match A 69, B 55; matches on record A 203, B 45; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Jodie Burrage / Robin Montgomery vs Teodora Kostovic / Jeline Vandromme -- WTA Chennai R16

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 12:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 11:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-02T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02BURMONKOSVAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jodie Burrage / Robin Montgomery (`KXWTADOUBLES-26NOV02BURMONKOSVAN-BURMON`) | 0.81 / 0.83 (25) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Teodora Kostovic / Jeline Vandromme (`KXWTADOUBLES-26NOV02BURMONKOSVAN-KOSVAN`) | 0.14 / 0.18 (377) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Jahnie van Zyl vs Yasmine Kabbaj -- WTA 125K Luanda R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 15:10Z
* Current expected start: 2026-11-02 12:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 11:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Hard · scheduled 2026-11-02T15:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:236956:267180:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yasmine Kabbaj (`KXWTACHALLENGERMATCH-26NOV02VANKAB-KAB`) | 0.71 / 0.72 (1862) | 71.5% | -- | 60.0% | 60.0% [52.7%-68.5%] | -- | 72.5% | 72.5% | MARKETS_AGREE | PASS | -11.5 pp | REVIEW | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Jahnie van Zyl (`KXWTACHALLENGERMATCH-26NOV02VANKAB-VAN`) | 0.28 / 0.29 (145) | 28.5% | -- | 40.0% | 40.0% [31.5%-47.3%] | -- | 28.4% | 28.4% | MARKETS_AGREE | PASS | +11.5 pp | REVIEW | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 643.0, B 2651.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.079
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.065, surface_pool_high +0.074, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Sahaja Yamalapalli vs Simona Waltert -- WTA Chennai R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 12:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 11:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215899:246481:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Simona Waltert (`KXWTAMATCH-26NOV02YAMWAL-WAL`) | 0.87 / 0.88 (6829) | 87.5% | 71.9% | 74.3% | 73.0% [69.8%-76.0%] | -- | 87.4% | 87.4% | MODEL_LONE_OUTLIER | PASS | -15.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Sahaja Yamalapalli (`KXWTAMATCH-26NOV02YAMWAL-YAM`) | 0.12 / 0.14 (9569) | 13.0% | 28.1% | 25.7% | 27.0% [24.0%-30.2%] | -- | 12.7% | 12.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +15.1 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2258.0, B 4747.0; serve-point win A 52.8%, B 42.8%; Elo A 1570.3, B 1723.9; model uncertainty 0.0307
* Form inputs: days since last match A 40, B 5; matches on record A 233, B 521; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26NOV02YAMWAL-YAM  (YES = Sahaja Yamalapalli)
Model: 28%
Kalshi: 13%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_REJECTION, UNKNOWN
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.032, surface_dev_loose +0.000, surface_dev_tight -0.000
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXWTAGTOTAL-26NOV02YAMWAL-19` Over 18.5 games: 0.49/0.50 mid 49.5%, model 76.5% (projection_v2.0 (prediction ledger)) -- gap +27.0 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV02YAMWAL-24` Over 23.5 games: 0.25/0.29 mid 27.0%, model 46.7% (projection_v2.0 (prediction ledger)) -- gap +19.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV02YAMWAL-2-YAM` Will Sahaja Yamalapalli win set 2 in the Sahaja Yamalapalli vs Simona Waltert match: 0.12/0.20 mid 16.0%, model 34.9% (projection_v2.0 (prediction ledger)) -- gap +18.9 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02YAMWAL-1-YAM` Will Sahaja Yamalapalli win set 1 in the Sahaja Yamalapalli vs Simona Waltert match: 0.18/0.20 mid 19.0%, model 34.9% (projection_v2.0 (prediction ledger)) -- gap +15.9 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02YAMWAL-1-WAL` Will Simona Waltert win set 1 in the Sahaja Yamalapalli vs Simona Waltert match: 0.79/0.82 mid 80.5%, model 65.0% (projection_v2.0 (prediction ledger)) -- gap -15.4 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02YAMWAL-2-WAL` Will Simona Waltert win set 2 in the Sahaja Yamalapalli vs Simona Waltert match: 0.76/0.84 mid 80.0%, model 65.0% (projection_v2.0 (prediction ledger)) -- gap -14.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Vaishnavi Adkar / Rutuja Bhosale vs Madeleine Brooks / Amelia Rajecki -- WTA Chennai R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-02T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02ADKBHOBRORAJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vaishnavi Adkar / Rutuja Bhosale (`KXWTADOUBLES-26NOV02ADKBHOBRORAJ-ADKBHO`) | 0.19 / 0.49 (50) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Madeleine Brooks / Amelia Rajecki (`KXWTADOUBLES-26NOV02ADKBHOBRORAJ-BRORAJ`) | 0.50 / 0.81 (90) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Jodie Burrage vs Vaishnavi Adkar -- WTA Chennai R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214839:261038:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vaishnavi Adkar (`KXWTAMATCH-26NOV02BURADK-ADK`) | 0.23 / 0.25 (368) | 24.0% | 34.8% | 69.6% | 53.7% [31.7%-61.4%] | -- | -- | -- | -- | WATCH | +10.8 pp | REVIEW | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jodie Burrage (`KXWTAMATCH-26NOV02BURADK-BUR`) | 0.74 / 0.75 (12) | 74.5% | 65.2% | 30.4% | 46.3% [38.6%-68.3%] | -- | -- | -- | -- | PASS | -9.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2529.0, B 2186.0; serve-point win A 58.7%, B 44.2%; Elo A 1689.6, B 1540.6; model uncertainty 0.1487
* Form inputs: days since last match A 33, B 188; matches on record A 427, B 143; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.011, surface_dev_loose -0.010, surface_dev_tight +0.021
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV02BURADK-15` Over 14.5 games: 0.05/0.94 mid 49.5%, model 99.0% (projection_v2.0 (prediction ledger)) -- gap +49.5 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26NOV02BURADK-20` Over 19.5 games: 0.49/0.52 mid 50.5%, model 72.9% (projection_v2.0 (prediction ledger)) -- gap +22.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTAGTOTAL-26NOV02BURADK-25` Over 24.5 games: 0.25/0.34 mid 29.5%, model 47.5% (projection_v2.0 (prediction ledger)) -- gap +18.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data LIMITED
  * `KXWTASETWINNER-26NOV02BURADK-1-ADK` Will Vaishnavi Adkar win set 1 in the Jodie Burrage vs Vaishnavi Adkar match: 0.29/0.32 mid 30.5%, model 39.7% (projection_v2.0 (prediction ledger)) -- gap +9.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV02BURADK-1-BUR` Will Jodie Burrage win set 1 in the Jodie Burrage vs Vaishnavi Adkar match: 0.68/0.71 mid 69.5%, model 60.3% (projection_v2.0 (prediction ledger)) -- gap -9.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV02BURADK-2-ADK` Will Vaishnavi Adkar win set 2 in the Jodie Burrage vs Vaishnavi Adkar match: 0.08/0.59 mid 33.5%, model 39.7% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV02BURADK-2-BUR` Will Jodie Burrage win set 2 in the Jodie Burrage vs Vaishnavi Adkar match: 0.33/0.87 mid 60.0%, model 60.3% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gabriella Da Silva Fick / Zhibek Kulambayeva vs Hiroko Kuwata / Ankita Raina -- WTA Chennai R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-02T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02DAKULKUWRAI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gabriella Da Silva Fick / Zhibek Kulambayeva (`KXWTADOUBLES-26NOV02DAKULKUWRAI-DAKUL`) | 0.50 / 0.79 (90) | 64.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hiroko Kuwata / Ankita Raina (`KXWTADOUBLES-26NOV02DAKULKUWRAI-KUWRAI`) | 0.21 / 0.50 (90) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Mai Hontama / Moyuka Uchijima vs Weronika Falkowska / Alana Smith -- WTA Chennai R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-02T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02HONUCHFALSMI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weronika Falkowska / Alana Smith (`KXWTADOUBLES-26NOV02HONUCHFALSMI-FALSMI`) | 0.51 / 0.75 (1) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mai Hontama / Moyuka Uchijima (`KXWTADOUBLES-26NOV02HONUCHFALSMI-HONUCH`) | 0.23 / 0.47 (11) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Elsa Jacquemot vs Lucrezia Stefanini -- WTA Chennai R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:214593:221039:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elsa Jacquemot (`KXWTAMATCH-26NOV02JACSTE-JAC`) | 0.46 / 0.47 (1198) | 46.5% | 42.3% | 45.7% | 45.2% [44.1%-46.8%] | -- | -- | -- | -- | PASS | -4.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lucrezia Stefanini (`KXWTAMATCH-26NOV02JACSTE-STE`) | 0.53 / 0.54 (2359) | 53.5% | 57.7% | 54.3% | 54.8% [53.2%-55.9%] | -- | -- | -- | -- | PASS | +4.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4592.0, B 4432.0; serve-point win A 52.7%, B 45.9%; Elo A 1712.2, B 1748.4; model uncertainty 0.0132
* Form inputs: days since last match A 1, B 3; matches on record A 406, B 615; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.011, surface_dev_loose -0.005, surface_dev_tight +0.016
* Derivatives listed: 3 (MATCH_WINNER, TOTAL_GAMES); 0 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Naima Karamoko / Simona Waltert vs Diya Ramesh Ramesh / Deepshika Vinayagamurthy -- WTA Chennai R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-02T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02KARWALRAMVIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naima Karamoko / Simona Waltert (`KXWTADOUBLES-26NOV02KARWALRAMVIN-KARWAL`) | 0.53 / 0.96 (10) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Diya Ramesh Ramesh / Deepshika Vinayagamurthy (`KXWTADOUBLES-26NOV02KARWALRAMVIN-RAMVIN`) | 0.05 / 0.49 (5) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Momoko Kobori / Peangtarn Plipuech vs Freya Christie / Eden Silva -- WTA Chennai R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-02T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02KOBPLICHRSIL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Freya Christie / Eden Silva (`KXWTADOUBLES-26NOV02KOBPLICHRSIL-CHRSIL`) | 0.36 / 0.62 (90) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Momoko Kobori / Peangtarn Plipuech (`KXWTADOUBLES-26NOV02KOBPLICHRSIL-KOBPLI`) | 0.38 / 0.64 (90) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Viktoria Morvayova vs Polina Kudermetova -- WTA Chennai R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215077:221236:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Kudermetova (`KXWTAMATCH-26NOV02MORKUD-KUD`) | 0.81 / 0.84 (12679) | 82.5% | 82.0% | 55.8% | 64.4% [59.9%-76.2%] | -- | -- | -- | -- | PASS | -0.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Viktoria Morvayova (`KXWTAMATCH-26NOV02MORKUD-MOR`) | 0.16 / 0.18 (526) | 17.0% | 18.0% | 44.2% | 35.6% [23.8%-40.1%] | -- | -- | -- | -- | WATCH | +1.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3267.0, B 4285.0; serve-point win A 54.1%, B 38.9%; Elo A 1552.2, B 1809.2; model uncertainty 0.0815
* Form inputs: days since last match A 0, B 5; matches on record A 466, B 392; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.010, surface_dev_loose -0.009, surface_dev_tight -0.000
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 4 carry a model probability
  * `KXWTASETWINNER-26NOV02MORKUD-2-KUD` Will Polina Kudermetova win set 2 in the Viktoria Morvayova vs Polina Kudermetova match: 0.09/0.97 mid 53.0%, model 73.0% (projection_v2.0 (prediction ledger)) -- gap +20.0 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02MORKUD-1-KUD` Will Polina Kudermetova win set 1 in the Viktoria Morvayova vs Polina Kudermetova match: 0.73/0.76 mid 74.5%, model 73.0% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02MORKUD-1-MOR` Will Viktoria Morvayova win set 1 in the Viktoria Morvayova vs Polina Kudermetova match: 0.24/0.28 mid 26.0%, model 27.0% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maaya Rajeshwaran Revathi vs Katarzyna Kawa -- WTA Chennai R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:203514:266722:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katarzyna Kawa (`KXWTAMATCH-26NOV02RAJKAW-KAW`) | 0.76 / 0.77 (1690) | 76.5% | 75.2% | 73.0% | 72.5% [63.0%-81.7%] | -- | -- | -- | -- | PASS | -1.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maaya Rajeshwaran Revathi (`KXWTAMATCH-26NOV02RAJKAW-RAJ`) | 0.23 / 0.24 (683) | 23.5% | 24.8% | 27.1% | 27.5% [18.3%-37.0%] | -- | -- | -- | -- | PASS | +1.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 796.0, B 4311.0; serve-point win A 52.8%, B 42.0%; Elo A 1456.1, B 1620.1; model uncertainty 0.0935
* Form inputs: days since last match A 258, B 9; matches on record A 23, B 706; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.073, surface_pool_high +0.095, surface_dev_loose +0.000, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV02RAJKAW-15` Over 14.5 games: 0.03/0.94 mid 48.5%, model 98.2% (projection_v2.0 (prediction ledger)) -- gap +49.7 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data POOR
  * `KXWTAGTOTAL-26NOV02RAJKAW-25` Over 24.5 games: 0.30/0.92 mid 61.0%, model 42.5% (projection_v2.0 (prediction ledger)) -- gap -18.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data POOR
  * `KXWTAGTOTAL-26NOV02RAJKAW-20` Over 19.5 games: 0.53/0.55 mid 54.0%, model 67.4% (projection_v2.0 (prediction ledger)) -- gap +13.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data POOR
  * `KXWTASETWINNER-26NOV02RAJKAW-2-KAW` Will Katarzyna Kawa win set 2 in the Maaya Rajeshwaran Revathi vs Katarzyna Kawa match: 0.33/0.91 mid 62.0%, model 67.5% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26NOV02RAJKAW-1-RAJ` Will Maaya Rajeshwaran Revathi win set 1 in the Maaya Rajeshwaran Revathi vs Katarzyna Kawa match: 0.23/0.31 mid 27.0%, model 32.5% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26NOV02RAJKAW-1-KAW` Will Katarzyna Kawa win set 1 in the Maaya Rajeshwaran Revathi vs Katarzyna Kawa match: 0.68/0.72 mid 70.0%, model 67.5% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26NOV02RAJKAW-2-RAJ` Will Maaya Rajeshwaran Revathi win set 2 in the Maaya Rajeshwaran Revathi vs Katarzyna Kawa match: 0.08/0.59 mid 33.5%, model 32.5% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data POOR
* Warnings: BET_BLOCKED_START_STATUS; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Oksana Selekhmeteva vs Teodora Kostovic -- WTA Chennai R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221407:267439:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Teodora Kostovic (`KXWTAMATCH-26NOV02SELKOS-KOS`) | 0.54 / 0.55 (1571) | 54.5% | 56.1% | 40.6% | 42.6% [41.1%-44.7%] | -- | -- | -- | -- | PASS | +1.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oksana Selekhmeteva (`KXWTAMATCH-26NOV02SELKOS-SEL`) | 0.45 / 0.46 (1539) | 45.5% | 43.9% | 59.4% | 57.4% [55.3%-58.9%] | -- | -- | -- | -- | SHADOW_BET | -1.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4338.0, B 3286.0; serve-point win A 55.7%, B 43.1%; Elo A 1740.7, B 1719.5; model uncertainty 0.0181
* Form inputs: days since last match A 4, B 6; matches on record A 355, B 117; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.016, surface_dev_loose +0.005, surface_dev_tight -0.010
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV02SELKOS-18` Over 17.5 games: 0.05/0.84 mid 44.5%, model 87.9% (projection_v2.0 (prediction ledger)) -- gap +43.4 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV02SELKOS-28` Over 27.5 games: 0.05/0.33 mid 19.0%, model 34.4% (projection_v2.0 (prediction ledger)) -- gap +15.3 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV02SELKOS-23` Over 22.5 games: 0.43/0.45 mid 44.0%, model 56.0% (projection_v2.0 (prediction ledger)) -- gap +12.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV02SELKOS-1-SEL` Will Oksana Selekhmeteva win set 1 in the Oksana Selekhmeteva vs Teodora Kostovic match: 0.43/0.48 mid 45.5%, model 45.9% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02SELKOS-1-KOS` Will Teodora Kostovic win set 1 in the Oksana Selekhmeteva vs Teodora Kostovic match: 0.52/0.56 mid 54.0%, model 54.1% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02SELKOS-2-KOS` Will Teodora Kostovic win set 2 in the Oksana Selekhmeteva vs Teodora Kostovic match: 0.10/0.98 mid 54.0%, model 54.1% (projection_v2.0 (prediction ledger)) -- gap +0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jil Teichmann vs Joanna Garland -- WTA Chennai R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:213525:220466:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joanna Garland (`KXWTAMATCH-26NOV02TEIGAR-GAR`) | 0.46 / 0.47 (202) | 46.5% | 53.7% | 58.2% | 55.6% [49.5%-58.1%] | -- | -- | -- | -- | SHADOW_BET | +7.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jil Teichmann (`KXWTAMATCH-26NOV02TEIGAR-TEI`) | 0.52 / 0.53 (111) | 52.5% | 46.3% | 41.8% | 44.4% [41.9%-50.5%] | -- | -- | -- | -- | PASS | -6.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2567.0, B 2480.0; serve-point win A 60.2%, B 39.1%; Elo A 1768.1, B 1771.4; model uncertainty 0.0433
* Form inputs: days since last match A 2, B 7; matches on record A 585, B 395; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose +0.015, surface_dev_tight -0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV02TEIGAR-18` Over 17.5 games: 0.44/0.85 mid 64.5%, model 91.0% (projection_v2.0 (prediction ledger)) -- gap +26.5 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV02TEIGAR-28` Over 27.5 games: 0.09/0.33 mid 21.0%, model 37.8% (projection_v2.0 (prediction ledger)) -- gap +16.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV02TEIGAR-23` Over 22.5 games: 0.43/0.44 mid 43.5%, model 58.6% (projection_v2.0 (prediction ledger)) -- gap +15.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV02TEIGAR-1-GAR` Will Joanna Garland win set 1 in the Jil Teichmann vs Joanna Garland match: 0.45/0.50 mid 47.5%, model 52.5% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02TEIGAR-1-TEI` Will Jil Teichmann win set 1 in the Jil Teichmann vs Joanna Garland match: 0.50/0.54 mid 52.0%, model 47.5% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02TEIGAR-2-GAR` Will Joanna Garland win set 2 in the Jil Teichmann vs Joanna Garland match: 0.14/0.84 mid 49.0%, model 52.5% (projection_v2.0 (prediction ledger)) -- gap +3.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02TEIGAR-2-TEI` Will Jil Teichmann win set 2 in the Jil Teichmann vs Joanna Garland match: 0.14/0.84 mid 49.0%, model 47.5% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Janice Tjen vs Katherine Hui -- WTA Chennai R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:222145:222866:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katherine Hui (`KXWTAMATCH-26NOV02TJEHUI-HUI`) | 0.04 / 0.05 (601) | 4.5% | 5.4% | 10.2% | 6.4% [6.3%-6.9%] | -- | -- | -- | -- | WATCH | +0.9 pp | NORMAL | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Janice Tjen (`KXWTAMATCH-26NOV02TJEHUI-TJE`) | 0.96 / 0.97 (2191) | 96.5% | 94.6% | 89.8% | 93.6% [93.1%-93.7%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | FRESH | C / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3631.0, B 270.0; serve-point win A 67.1%, B 45.4%; Elo A 1889.0, B 1407.2; model uncertainty 0.0032
* Form inputs: days since last match A 4, B 5; matches on record A 186, B 66; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.002, surface_dev_loose -0.000, surface_dev_tight -0.001
* Derivatives listed: 6 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 6 carry a model probability
  * `KXWTASETWINNER-26NOV02TJEHUI-1-TJE` Will Janice Tjen win set 1 in the Janice Tjen vs Katherine Hui match: 0.03/0.91 mid 47.0%, model 85.9% (projection_v2.0 (prediction ledger)) -- gap +38.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26NOV02TJEHUI-2-TJE` Will Janice Tjen win set 2 in the Janice Tjen vs Katherine Hui match: 0.05/0.91 mid 48.0%, model 85.9% (projection_v2.0 (prediction ledger)) -- gap +37.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXWTASETWINNER-26NOV02TJEHUI-1-HUI` Will Katherine Hui win set 1 in the Janice Tjen vs Katherine Hui match: 0.05/0.93 mid 49.0%, model 14.1% (projection_v2.0 (prediction ledger)) -- gap -34.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXWTAGTOTAL-26NOV02TJEHUI-17` Over 16.5 games: 0.03/0.93 mid 48.0%, model 81.4% (projection_v2.0 (prediction ledger)) -- gap +33.4 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data POOR
  * `KXWTASETWINNER-26NOV02TJEHUI-2-HUI` Will Katherine Hui win set 2 in the Janice Tjen vs Katherine Hui match: 0.04/0.90 mid 47.0%, model 14.1% (projection_v2.0 (prediction ledger)) -- gap -32.9 pp, EXTREME, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data POOR
  * `KXWTAGTOTAL-26NOV02TJEHUI-22` Over 21.5 games: 0.03/0.93 mid 48.0%, model 35.1% (projection_v2.0 (prediction ledger)) -- gap -12.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data POOR
* Warnings: BET_BLOCKED_START_STATUS; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Panna Udvardy vs Robin Montgomery -- WTA Chennai R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:215910:221905:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robin Montgomery (`KXWTAMATCH-26NOV02UDVMON-MON`) | 0.70 / 0.71 (1487) | 70.5% | 66.5% | 39.3% | 54.6% [49.5%-61.8%] | -- | -- | -- | -- | PASS | -4.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Panna Udvardy (`KXWTAMATCH-26NOV02UDVMON-UDV`) | 0.28 / 0.29 (27) | 28.5% | 33.5% | 60.7% | 45.4% [38.2%-50.5%] | -- | -- | -- | -- | SHADOW_BET | +5.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5090.0, B 2060.0; serve-point win A 58.4%, B 38.3%; Elo A 1653.8, B 1836.7; model uncertainty 0.0617
* Form inputs: days since last match A 6, B 4; matches on record A 583, B 250; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.025, surface_dev_loose -0.005, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV02UDVMON-16` Over 15.5 games: 0.03/0.93 mid 48.0%, model 97.7% (projection_v2.0 (prediction ledger)) -- gap +49.7 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV02UDVMON-21` Over 20.5 games: 0.50/0.52 mid 51.0%, model 67.8% (projection_v2.0 (prediction ledger)) -- gap +16.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV02UDVMON-1-UDV` Will Panna Udvardy win set 1 in the Panna Udvardy vs Robin Montgomery match: 0.28/0.36 mid 32.0%, model 38.8% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02UDVMON-2-UDV` Will Panna Udvardy win set 2 in the Panna Udvardy vs Robin Montgomery match: 0.08/0.59 mid 33.5%, model 38.8% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV02UDVMON-26` Over 25.5 games: 0.03/0.93 mid 48.0%, model 44.4% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV02UDVMON-1-MON` Will Robin Montgomery win set 1 in the Panna Udvardy vs Robin Montgomery match: 0.57/0.68 mid 62.5%, model 61.2% (projection_v2.0 (prediction ledger)) -- gap -1.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02UDVMON-2-MON` Will Robin Montgomery win set 2 in the Panna Udvardy vs Robin Montgomery match: 0.33/0.91 mid 62.0%, model 61.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anastasia Zakharova vs Polina Iatcenko -- WTA Chennai R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-02T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220435:223325:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Iatcenko (`KXWTAMATCH-26NOV02ZAKIAT-IAT`) | 0.37 / 0.39 (6673) | 38.0% | 44.6% | 51.1% | 48.4% [42.1%-51.6%] | -- | -- | -- | -- | SHADOW_BET | +6.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Zakharova (`KXWTAMATCH-26NOV02ZAKIAT-ZAK`) | 0.61 / 0.62 (124) | 61.5% | 55.4% | 48.9% | 51.6% [48.4%-57.9%] | -- | -- | -- | -- | PASS | -6.2 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4628.0, B 2951.0; serve-point win A 56.9%, B 44.1%; Elo A 1804.6, B 1763.1; model uncertainty 0.0473
* Form inputs: days since last match A 5, B 7; matches on record A 484, B 301; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.021, surface_dev_loose +0.005, surface_dev_tight -0.011
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV02ZAKIAT-16` Over 15.5 games: 0.03/0.93 mid 48.0%, model 97.2% (projection_v2.0 (prediction ledger)) -- gap +49.2 pp, EXTREME, DATA_WARNING, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV02ZAKIAT-21` Over 20.5 games: 0.50/0.52 mid 51.0%, model 67.8% (projection_v2.0 (prediction ledger)) -- gap +16.8 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV02ZAKIAT-26` Over 25.5 games: 0.25/0.93 mid 59.0%, model 44.5% (projection_v2.0 (prediction ledger)) -- gap -14.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV02ZAKIAT-1-ZAK` Will Anastasia Zakharova win set 1 in the Anastasia Zakharova vs Polina Iatcenko match: 0.58/0.61 mid 59.5%, model 53.6% (projection_v2.0 (prediction ledger)) -- gap -5.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02ZAKIAT-1-IAT` Will Polina Iatcenko win set 1 in the Anastasia Zakharova vs Polina Iatcenko match: 0.39/0.43 mid 41.0%, model 46.4% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02ZAKIAT-2-ZAK` Will Anastasia Zakharova win set 2 in the Anastasia Zakharova vs Polina Iatcenko match: 0.26/0.82 mid 54.0%, model 53.6% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV02ZAKIAT-2-IAT` Will Polina Iatcenko win set 2 in the Anastasia Zakharova vs Polina Iatcenko match: 0.14/0.79 mid 46.5%, model 46.4% (projection_v2.0 (prediction ledger)) -- gap -0.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Daniel Merida vs Alexander Blockx -- ATP Paris R64

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 12:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:210017:210696:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Blockx (`KXATPMATCH-26NOV01MERBLO-BLO`) | 0.58 / 0.59 (1357) | 58.5% | 63.1% | 74.2% | 71.8% [67.8%-73.9%] | -- | -- | -- | -- | SHADOW_BET | +4.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Daniel Merida (`KXATPMATCH-26NOV01MERBLO-MER`) | 0.41 / 0.42 (36707) | 41.5% | 36.9% | 25.8% | 28.2% [26.2%-32.1%] | -- | -- | -- | -- | PASS | -4.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 5577.0, B 5354.0; serve-point win A 62.3%, B 35.1%; Elo A 1772.9, B 1873.8; model uncertainty 0.03
* Form inputs: days since last match A 4, B 23; matches on record A 356, B 247; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.008, surface_dev_loose -0.004, surface_dev_tight +0.008
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26NOV01MERBLO-2-BLO` Will Alexander Blockx win set 2 in the Daniel Merida vs Alexander Blockx match: 0.23/0.60 mid 41.5%, model 58.8% (projection_v2.0 (prediction ledger)) -- gap +17.3 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MERBLO-BLO21` Will Alexander Blockx win the Daniel Merida vs Alexander Blockx match by a set score of 2-1?: 0.14/0.24 mid 19.0%, model 28.5% (projection_v2.0 (prediction ledger)) -- gap +9.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV01MERBLO-25` Over 24.5 games: 0.41/0.44 mid 42.5%, model 51.9% (projection_v2.0 (prediction ledger)) -- gap +9.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV01MERBLO-20` Over 19.5 games: 0.70/0.72 mid 71.0%, model 79.8% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MERBLO-2-MER` Will Daniel Merida win set 2 in the Daniel Merida vs Alexander Blockx match: 0.21/0.46 mid 33.5%, model 41.2% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01MERBLO-MER2` Will Daniel Merida win at least 1.5 more games than Alexander Blockx?: 0.36/0.38 mid 37.0%, model 30.0% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MERBLO-MER20` Will Daniel Merida win the Daniel Merida vs Alexander Blockx match by a set score of 2-0?: 0.21/0.25 mid 23.0%, model 17.0% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV01MERBLO-30` Over 29.5 games: 0.22/0.26 mid 24.0%, model 29.9% (projection_v2.0 (prediction ledger)) -- gap +5.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01MERBLO-BLO5` Will Alexander Blockx win at least 4.5 more games than Daniel Merida?: 0.29/0.31 mid 30.0%, model 24.5% (projection_v2.0 (prediction ledger)) -- gap -5.5 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MERBLO-MER21` Will Daniel Merida win the Daniel Merida vs Alexander Blockx match by a set score of 2-1?: 0.10/0.20 mid 15.0%, model 20.0% (projection_v2.0 (prediction ledger)) -- gap +5.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01MERBLO-BLO20` Will Alexander Blockx win the Daniel Merida vs Alexander Blockx match by a set score of 2-0?: 0.36/0.40 mid 38.0%, model 34.6% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01MERBLO-BLO2` Will Alexander Blockx win at least 1.5 more games than Daniel Merida?: 0.52/0.53 mid 52.5%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MERBLO-1-BLO` Will Alexander Blockx win set 1 in the Daniel Merida vs Alexander Blockx match: 0.55/0.58 mid 56.5%, model 58.8% (projection_v2.0 (prediction ledger)) -- gap +2.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01MERBLO-1-MER` Will Daniel Merida win set 1 in the Daniel Merida vs Alexander Blockx match: 0.42/0.44 mid 43.0%, model 41.2% (projection_v2.0 (prediction ledger)) -- gap -1.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cameron Norrie vs Matteo Arnaldi -- ATP Paris R64

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 12:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111815:208286:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Arnaldi (`KXATPMATCH-26NOV01NORARN-ARN`) | 0.33 / 0.34 (11654) | 33.5% | 37.5% | 38.0% | 38.0% [37.1%-39.5%] | -- | -- | -- | -- | SHADOW_BET | +4.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cameron Norrie (`KXATPMATCH-26NOV01NORARN-NOR`) | 0.66 / 0.67 (17643) | 66.5% | 62.5% | 62.0% | 62.0% [60.5%-62.9%] | -- | -- | -- | -- | PASS | -4.0 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5400.0, B 4906.0; serve-point win A 63.7%, B 38.8%; Elo A 1888.0, B 1790.2; model uncertainty 0.0121
* Form inputs: days since last match A 3, B 6; matches on record A 679, B 400; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26NOV01NORARN-2-ARN` Will Matteo Arnaldi win set 2 in the Cameron Norrie vs Matteo Arnaldi match: 0.13/0.40 mid 26.5%, model 41.6% (projection_v2.0 (prediction ledger)) -- gap +15.1 pp, HIGH_REVIEW, DATA_WARNING, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01NORARN-2-NOR` Will Cameron Norrie win set 2 in the Cameron Norrie vs Matteo Arnaldi match: 0.21/0.66 mid 43.5%, model 58.4% (projection_v2.0 (prediction ledger)) -- gap +14.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01NORARN-NOR20` Will Cameron Norrie win the Cameron Norrie vs Matteo Arnaldi match by a set score of 2-0?: 0.43/0.46 mid 44.5%, model 34.1% (projection_v2.0 (prediction ledger)) -- gap -10.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01NORARN-24` Over 23.5 games: 0.42/0.43 mid 42.5%, model 52.7% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01NORARN-NOR5` Will Cameron Norrie win at least 4.5 more games than Matteo Arnaldi?: 0.34/0.35 mid 34.5%, model 25.6% (projection_v2.0 (prediction ledger)) -- gap -8.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01NORARN-19` Over 18.5 games: 0.76/0.79 mid 77.5%, model 85.9% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01NORARN-ARN21` Will Matteo Arnaldi win the Cameron Norrie vs Matteo Arnaldi match by a set score of 2-1?: 0.07/0.17 mid 12.0%, model 20.2% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01NORARN-NOR21` Will Cameron Norrie win the Cameron Norrie vs Matteo Arnaldi match by a set score of 2-1?: 0.16/0.25 mid 20.5%, model 28.4% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01NORARN-29` Over 28.5 games: 0.25/0.29 mid 27.0%, model 33.5% (projection_v2.0 (prediction ledger)) -- gap +6.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01NORARN-NOR2` Will Cameron Norrie win at least 1.5 more games than Matteo Arnaldi?: 0.60/0.62 mid 61.0%, model 55.5% (projection_v2.0 (prediction ledger)) -- gap -5.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01NORARN-1-ARN` Will Matteo Arnaldi win set 1 in the Cameron Norrie vs Matteo Arnaldi match: 0.35/0.38 mid 36.5%, model 41.6% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01NORARN-1-NOR` Will Cameron Norrie win set 1 in the Cameron Norrie vs Matteo Arnaldi match: 0.62/0.64 mid 63.0%, model 58.4% (projection_v2.0 (prediction ledger)) -- gap -4.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01NORARN-ARN2` Will Matteo Arnaldi win at least 1.5 more games than Cameron Norrie?: 0.27/0.29 mid 28.0%, model 30.7% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01NORARN-ARN20` Will Matteo Arnaldi win the Cameron Norrie vs Matteo Arnaldi match by a set score of 2-0?: 0.15/0.19 mid 17.0%, model 17.3% (projection_v2.0 (prediction ledger)) -- gap +0.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Casper Ruud vs Juan Manuel Cerundolo -- ATP Paris R64

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 15:20Z
* Current expected start: 2026-11-02 13:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 12:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-02T15:20:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:134770:207678:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Manuel Cerundolo (`KXATPMATCH-26NOV02RUUCER-CER`) | 0.28 / 0.29 (14337) | 28.5% | 31.1% | 25.4% | 25.4% [23.1%-27.8%] | -- | -- | -- | -- | PASS | +2.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Casper Ruud (`KXATPMATCH-26NOV02RUUCER-RUU`) | 0.71 / 0.72 (39124) | 71.5% | 68.9% | 74.6% | 74.6% [72.2%-77.0%] | -- | -- | -- | -- | WATCH | -2.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5162.0, B 6168.0; serve-point win A 67.5%, B 36.5%; Elo A 1941.2, B 1748.5; model uncertainty 0.0237
* Form inputs: days since last match A 5, B 2; matches on record A 719, B 546; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.024, surface_dev_loose +0.002, surface_dev_tight -0.003
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV02RUUCER-23` Over 22.5 games: 0.49/0.50 mid 49.5%, model 59.7% (projection_v2.0 (prediction ledger)) -- gap +10.2 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV02RUUCER-28` Over 27.5 games: 0.29/0.33 mid 31.0%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV02RUUCER-RUU7` Will Casper Ruud win at least 6.5 more games than Juan Manuel Cerundolo?: 0.13/0.17 mid 15.0%, model 6.8% (projection_v2.0 (prediction ledger)) -- gap -8.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02RUUCER-RUU21` Will Casper Ruud win the Casper Ruud vs Juan Manuel Cerundolo match by a set score of 2-1?: 0.17/0.26 mid 21.5%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV02RUUCER-18` Over 17.5 games: 0.84/0.88 mid 86.0%, model 93.7% (projection_v2.0 (prediction ledger)) -- gap +7.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV02RUUCER-RUU4` Will Casper Ruud win at least 3.5 more games than Juan Manuel Cerundolo?: 0.47/0.48 mid 47.5%, model 40.5% (projection_v2.0 (prediction ledger)) -- gap -7.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02RUUCER-CER21` Will Juan Manuel Cerundolo win the Casper Ruud vs Juan Manuel Cerundolo match by a set score of 2-1?: 0.08/0.14 mid 11.0%, model 17.3% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02RUUCER-RUU20` Will Casper Ruud win the Casper Ruud vs Juan Manuel Cerundolo match by a set score of 2-0?: 0.44/0.47 mid 45.5%, model 39.6% (projection_v2.0 (prediction ledger)) -- gap -6.0 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV02RUUCER-2-CER` Will Juan Manuel Cerundolo win set 2 in the Casper Ruud vs Juan Manuel Cerundolo match: 0.29/0.35 mid 32.0%, model 37.1% (projection_v2.0 (prediction ledger)) -- gap +5.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV02RUUCER-1-CER` Will Juan Manuel Cerundolo win set 1 in the Casper Ruud vs Juan Manuel Cerundolo match: 0.32/0.35 mid 33.5%, model 37.1% (projection_v2.0 (prediction ledger)) -- gap +3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV02RUUCER-1-RUU` Will Casper Ruud win set 1 in the Casper Ruud vs Juan Manuel Cerundolo match: 0.65/0.68 mid 66.5%, model 62.9% (projection_v2.0 (prediction ledger)) -- gap -3.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV02RUUCER-2-RUU` Will Casper Ruud win set 2 in the Casper Ruud vs Juan Manuel Cerundolo match: 0.62/0.69 mid 65.5%, model 62.9% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV02RUUCER-CER2` Will Juan Manuel Cerundolo win at least 1.5 more games than Casper Ruud?: 0.22/0.26 mid 24.0%, model 24.4% (projection_v2.0 (prediction ledger)) -- gap +0.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02RUUCER-CER20` Will Juan Manuel Cerundolo win the Casper Ruud vs Juan Manuel Cerundolo match by a set score of 2-0?: 0.12/0.16 mid 14.0%, model 13.8% (projection_v2.0 (prediction ledger)) -- gap -0.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Michal Krajci vs Niels Visker -- ATP Challenger Bratislava II Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-02T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208253:211756:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michal Krajci (`KXATPCHALLENGERMATCH-26NOV02KRAVIS-KRA`) | 0.24 / 0.25 (878) | 24.5% | 40.8% | 49.0% | 43.8% [35.9%-46.7%] | -- | 24.6% | 24.6% | MODEL_LONE_OUTLIER | WATCH | +16.3 pp | HIGH_REVIEW | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Niels Visker (`KXATPCHALLENGERMATCH-26NOV02KRAVIS-VIS`) | 0.75 / 0.76 (2119) | 75.5% | 59.2% | 50.9% | 56.2% [53.3%-64.1%] | -- | 75.5% | 75.5% | MODEL_LONE_OUTLIER | PASS | -16.3 pp | HIGH_REVIEW | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3159.0, B 3283.0; serve-point win A 67.0%, B 31.1%; Elo A 1320.8, B 1445.7; model uncertainty 0.0541
* Form inputs: days since last match A 160, B 20; matches on record A 120, B 252; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV02KRAVIS-KRA  (YES = Michal Krajci)
Model: 41%
Kalshi: 24%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.009, surface_dev_loose -0.023, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Lucas Poullain vs Yannik Kelm -- ATP Challenger Bratislava II Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-02T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:131911:212025:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yannik Kelm (`KXATPCHALLENGERMATCH-26NOV02POUKEL-KEL`) | 0.24 / 0.25 (770) | 24.5% | 24.2% | 18.6% | 19.7% [18.9%-21.6%] | -- | 25.9% | 25.9% | MODEL_LONE_OUTLIER | PASS | -0.3 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |
| Lucas Poullain (`KXATPCHALLENGERMATCH-26NOV02POUKEL-POU`) | 0.73 / 0.74 (177) | 73.5% | 75.8% | 81.4% | 80.3% [78.4%-81.0%] | -- | 74.4% | 74.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +2.3 pp | NORMAL | FRESH | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4417.0, B 2489.0; serve-point win A 60.3%, B 45.1%; Elo A 1461.4, B 1239.4; model uncertainty 0.0133
* Form inputs: days since last match A 34, B 188; matches on record A 394, B 83; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.015, surface_dev_loose +0.001, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Ryan Peniston vs Marcus Walters -- ATP Challenger Taranto Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 13:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126106:126971:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryan Peniston (`KXATPCHALLENGERMATCH-26NOV02PENWAL-PEN`) | 0.70 / 0.71 (5) | 70.5% | 87.1% | 76.4% | 84.7% [82.2%-88.3%] | -- | 70.0% | 70.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +16.6 pp | HIGH_REVIEW | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Marcus Walters (`KXATPCHALLENGERMATCH-26NOV02PENWAL-WAL`) | 0.28 / 0.30 (1919) | 29.0% | 12.9% | 23.6% | 15.3% [11.7%-17.8%] | -- | 29.8% | 29.8% | MODEL_LONE_OUTLIER | PASS | -16.1 pp | HIGH_REVIEW | FRESH | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2785.0, B 2017.0; serve-point win A 65.3%, B 43.5%; Elo A 1698.5, B 1256.2; model uncertainty 0.0305
* Form inputs: days since last match A 55, B 118; matches on record A 500, B 104; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV02PENWAL-PEN  (YES = Ryan Peniston)
Model: 87%
Kalshi: 70%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE

## Jacopo Vasami vs Matteo Sciahbasi -- ATP Challenger Taranto Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 13:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T13:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213635:214126:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Sciahbasi (`KXATPCHALLENGERMATCH-26NOV02VASSCI-SCI`) | 0.27 / 0.28 (506) | 27.5% | 5.7% | 24.4% | 11.5% [10.8%-12.8%] | -- | 24.8% | 24.8% | MODEL_LONE_OUTLIER | PASS | -21.9 pp | HIGH_REVIEW | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Jacopo Vasami (`KXATPCHALLENGERMATCH-26NOV02VASSCI-VAS`) | 0.72 / 0.73 (58) | 72.5% | 94.3% | 75.6% | 88.5% [87.2%-89.2%] | -- | 76.7% | 76.7% | KALSHI_LONE_OUTLIER | PASS | +21.9 pp | HIGH_REVIEW | FRESH | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2284.0, B 272.0; serve-point win A 68.9%, B 43.6%; Elo A 1599.0, B 1209.9; model uncertainty 0.0099
* Form inputs: days since last match A 13, B 34; matches on record A 65, B 7; data quality D

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV02VASSCI-VAS  (YES = Jacopo Vasami)
Model: 94%
Kalshi: 72%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, LEVEL_TRANSFER_RISK, MODEL_CALIBRATION_OUTLIER, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Laura Boehner vs Prathyusha Rachapudi -- WTA 125K Luanda Q3

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-02 13:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

WTA125 (WTA_125) · Hard · scheduled 2026-11-02T13:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:221258:222161:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laura Boehner (`KXWTACHALLENGERMATCH-26NOV02BOERAC-BOE`) | 0.78 / 0.79 (2555) | 78.5% | -- | 62.1% | 63.1% [59.5%-67.5%] | -- | 79.1% | 79.1% | MODEL_LONE_OUTLIER | PASS | -15.4 pp | HIGH_REVIEW | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Prathyusha Rachapudi (`KXWTACHALLENGERMATCH-26NOV02BOERAC-RAC`) | 0.21 / 0.22 (593) | 21.5% | -- | 37.9% | 36.9% [32.5%-40.5%] | -- | 22.0% | 22.0% | MODEL_LONE_OUTLIER | WATCH | +15.4 pp | HIGH_REVIEW | FRESH | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 824.0, B 668.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0399
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26NOV02BOERAC-RAC  (YES = Prathyusha Rachapudi)
Model: 37%
Kalshi: 22%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.035, surface_pool_high -0.036, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Ignacio Buse / Luciano Darderi vs Benjamin Bonzi / Arthur Rinderknech -- ATP Paris R32

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 13:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 12:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-01T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV01BUSDARBONRIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Bonzi / Arthur Rinderknech (`KXATPDOUBLES-26NOV01BUSDARBONRIN-BONRIN`) | 0.76 / 0.77 (124) | 76.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ignacio Buse / Luciano Darderi (`KXATPDOUBLES-26NOV01BUSDARBONRIN-BUSDAR`) | 0.21 / 0.24 (83) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Aneta Kucmova / Aneta Laboutkova vs Shrivalli Rashmikaa Bhamidipaty / Maaya Rajeshwaran Revathi -- WTA Chennai R16

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-02 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 14:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 13:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-02T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02KUCLABBHARAJ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shrivalli Rashmikaa Bhamidipaty / Maaya Rajeshwaran Revathi (`KXWTADOUBLES-26NOV02KUCLABBHARAJ-BHARAJ`) | 0.05 / 0.80 (100) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aneta Kucmova / Aneta Laboutkova (`KXWTADOUBLES-26NOV02KUCLABBHARAJ-KUCLAB`) | 0.18 / 0.94 (10) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Sara Cakarevic vs Teodora Miron -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214319:270171:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sara Cakarevic (`KXITFWMATCH-26NOV02CAKMIR-CAK`) | 0.62 / 0.66 (21) | 64.0% | 85.9% | 36.5% | 67.0% [57.9%-75.5%] | -- | -- | -- | -- | PASS | +21.9 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Teodora Miron (`KXITFWMATCH-26NOV02CAKMIR-MIR`) | 0.31 / 0.34 (138) | 32.5% | 14.1% | 63.5% | 33.1% [24.4%-42.1%] | -- | -- | -- | -- | PASS | -18.4 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1791.0, B 136.0; serve-point win A 59.4%, B 48.8%; Elo A 1460.0, B 1320.1; model uncertainty 0.0882
* Form inputs: days since last match A 21, B 469; matches on record A 475, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV02CAKMIR-CAK  (YES = Sara Cakarevic)
Model: 86%
Kalshi: 64%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.060, surface_pool_high -0.075, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Felitsata Dorofeeva-Rybas vs Valeriia Artemeva -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:267022:267841:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valeriia Artemeva (`KXITFWMATCH-26NOV02DORART-ART`) | 0.14 / 0.15 (3) | 14.5% | 29.6% | 34.8% | 36.3% [34.8%-37.9%] | -- | -- | -- | -- | PASS | +15.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Felitsata Dorofeeva-Rybas (`KXITFWMATCH-26NOV02DORART-DOR`) | 0.85 / 0.86 (269) | 85.5% | 70.4% | 65.2% | 63.7% [62.1%-65.2%] | -- | -- | -- | -- | PASS | -15.1 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 923.0, B 1430.0; serve-point win A 53.5%, B 50.4%; Elo A 1447.6, B 1357.5; model uncertainty 0.0152
* Form inputs: days since last match A 336, B 203; matches on record A 19, B 41; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV02DORART-ART  (YES = Valeriia Artemeva)
Model: 30%
Kalshi: 14%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Antonia Stoyanov vs Cristina Diaz Adrover -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:232881:267422:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cristina Diaz Adrover (`KXITFWMATCH-26NOV02STODIA-DIA`) | 0.08 / 0.13 (61) | 10.5% | 36.5% | 45.7% | 50.5% [45.2%-55.3%] | -- | -- | -- | -- | PASS | +26.0 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Antonia Stoyanov (`KXITFWMATCH-26NOV02STODIA-STO`) | 0.87 / 0.89 (1) | 88.0% | 63.5% | 54.3% | 49.5% [44.7%-54.8%] | -- | -- | -- | -- | PASS | -24.5 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 608.0, B 3491.0; serve-point win A 53.6%, B 48.9%; Elo A 1451.4, B 1462.3; model uncertainty 0.0507
* Form inputs: days since last match A 203, B 21; matches on record A 24, B 204; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV02STODIA-DIA  (YES = Cristina Diaz Adrover)
Model: 37%
Kalshi: 10%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.032, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eliska Tichackova vs Beatris Spasova -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221315:254748:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beatris Spasova (`KXITFWMATCH-26NOV02TICSPA-SPA`) | 0.03 / 0.06 (578) | 4.5% | 1.4% | 0.8% | 4.1% [2.1%-6.7%] | -- | -- | -- | -- | PASS | -3.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eliska Tichackova (`KXITFWMATCH-26NOV02TICSPA-TIC`) | 0.91 / 0.98 (117) | 94.5% | 98.6% | 99.2% | 95.9% [93.3%-97.9%] | -- | -- | -- | -- | PASS | +4.1 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1647.0, B 520.0; serve-point win A 59.9%, B 56.7%; Elo A 1623.6, B 1166.2; model uncertainty 0.0234
* Form inputs: days since last match A 252, B 245; matches on record A 46, B 195; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.002, surface_pool_high -0.004, surface_dev_loose +0.002, surface_dev_tight -0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Houkes vs Michael Vrbensky -- ATP Challenger Bratislava II Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 14:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-02T14:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202398:208069:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Houkes (`KXATPCHALLENGERMATCH-26NOV02HOUVRB-HOU`) | 0.65 / 0.66 (1000) | 65.5% | -- | 81.7% | 76.9% [72.8%-80.3%] | -- | 65.8% | 65.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +11.4 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Michael Vrbensky (`KXATPCHALLENGERMATCH-26NOV02HOUVRB-VRB`) | 0.33 / 0.34 (61) | 33.5% | -- | 18.3% | 23.1% [19.7%-27.3%] | -- | 35.2% | 35.2% | MODEL_LONE_OUTLIER | PASS | -10.4 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4345.0, B 2640.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0378
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.004, surface_dev_loose +0.008, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Giovanni Mpetshi Perricard vs Sebastian Sorger -- ATP Challenger Bratislava II Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 14:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-02T14:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208659:210285:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giovanni Mpetshi Perricard (`KXATPCHALLENGERMATCH-26NOV02MPESOR-MPE`) | 0.78 / 0.81 (1745) | 79.5% | -- | 48.5% | 62.9% [55.3%-74.1%] | -- | 80.3% | 80.3% | MODEL_LONE_OUTLIER | PASS | -16.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Sebastian Sorger (`KXATPCHALLENGERMATCH-26NOV02MPESOR-SOR`) | 0.19 / 0.20 (791) | 19.5% | -- | 51.5% | 37.1% [25.9%-44.7%] | -- | 20.1% | 20.1% | MODEL_LONE_OUTLIER | WATCH | +17.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4345.0, B 2759.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.094
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV02MPESOR-SOR  (YES = Sebastian Sorger)
Model: 37%
Kalshi: 20%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.023, surface_dev_loose +0.001, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Mattia Bellucci vs Lorenzo Sonego -- ATP Paris R64

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 16:50Z
* Current expected start: 2026-11-02 14:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 13:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-140_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-02T16:50:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:132283:208233:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mattia Bellucci (`KXATPMATCH-26NOV02BELSON-BEL`) | 0.57 / 0.58 (14066) | 57.5% | 63.2% | 56.3% | 56.3% [55.3%-56.8%] | -- | -- | -- | -- | PASS | +5.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorenzo Sonego (`KXATPMATCH-26NOV02BELSON-SON`) | 0.41 / 0.42 (14) | 41.5% | 36.8% | 43.7% | 43.7% [43.2%-44.7%] | -- | -- | -- | -- | PASS | -4.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5542.0, B 4676.0; serve-point win A 67.6%, B 35.1%; Elo A 1825.7, B 1776.9; model uncertainty 0.0073
* Form inputs: days since last match A 1, B 2; matches on record A 433, B 702; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV02BELSON-BEL20` Will Mattia Bellucci win the Mattia Bellucci vs Lorenzo Sonego match by a set score of 2-0?: 0.02/0.37 mid 19.5%, model 34.7% (projection_v2.0 (prediction ledger)) -- gap +15.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02BELSON-BEL21` Will Mattia Bellucci win the Mattia Bellucci vs Lorenzo Sonego match by a set score of 2-1?: 0.02/0.28 mid 15.0%, model 28.5% (projection_v2.0 (prediction ledger)) -- gap +13.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV02BELSON-SON2` Will Lorenzo Sonego win at least 1.5 more games than Mattia Bellucci?: 0.33/0.52 mid 42.5%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap -13.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV02BELSON-19` Over 18.5 games: 0.64/0.92 mid 78.0%, model 90.6% (projection_v2.0 (prediction ledger)) -- gap +12.6 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV02BELSON-2-BEL` Will Mattia Bellucci win set 2 in the Mattia Bellucci vs Lorenzo Sonego match: 0.15/0.79 mid 47.0%, model 58.9% (projection_v2.0 (prediction ledger)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV02BELSON-2-SON` Will Lorenzo Sonego win set 2 in the Mattia Bellucci vs Lorenzo Sonego match: 0.15/0.79 mid 47.0%, model 41.1% (projection_v2.0 (prediction ledger)) -- gap -5.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV02BELSON-29` Over 28.5 games: 0.35/0.52 mid 43.5%, model 38.1% (projection_v2.0 (prediction ledger)) -- gap -5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV02BELSON-BEL2` Will Mattia Bellucci win at least 1.5 more games than Lorenzo Sonego?: 0.50/0.51 mid 50.5%, model 55.3% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV02BELSON-24` Over 23.5 games: 0.51/0.52 mid 51.5%, model 54.9% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV02BELSON-1-BEL` Will Mattia Bellucci win set 1 in the Mattia Bellucci vs Lorenzo Sonego match: 0.54/0.57 mid 55.5%, model 58.9% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV02BELSON-1-SON` Will Lorenzo Sonego win set 1 in the Mattia Bellucci vs Lorenzo Sonego match: 0.43/0.46 mid 44.5%, model 41.1% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02BELSON-SON21` Will Lorenzo Sonego win the Mattia Bellucci vs Lorenzo Sonego match by a set score of 2-1?: 0.12/0.22 mid 17.0%, model 19.9% (projection_v2.0 (prediction ledger)) -- gap +2.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02BELSON-SON20` Will Lorenzo Sonego win the Mattia Bellucci vs Lorenzo Sonego match by a set score of 2-0?: 0.11/0.25 mid 18.0%, model 16.9% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV02BELSON-BEL5` Will Mattia Bellucci win at least 4.5 more games than Lorenzo Sonego?: 0.17/0.23 mid 20.0%, model 20.7% (projection_v2.0 (prediction ledger)) -- gap +0.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kyrian Jacquet vs Tomas Machac -- ATP Paris R64

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 17:30Z
* Current expected start: 2026-11-02 14:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 13:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-02T17:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207830:208021:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kyrian Jacquet (`KXATPMATCH-26NOV02JACMAC-JAC`) | 0.36 / 0.37 (4502) | 36.5% | 40.0% | 54.5% | 48.0% [43.5%-51.0%] | -- | -- | -- | -- | SHADOW_BET | +3.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tomas Machac (`KXATPMATCH-26NOV02JACMAC-MAC`) | 0.63 / 0.64 (6512) | 63.5% | 60.0% | 45.5% | 52.0% [49.0%-56.5%] | -- | -- | -- | -- | PASS | -3.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4419.0, B 4045.0; serve-point win A 62.7%, B 35.3%; Elo A 1779.5, B 1912.3; model uncertainty 0.0374
* Form inputs: days since last match A 11, B 7; matches on record A 415, B 458; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.015, surface_dev_tight -0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV02JACMAC-24` Over 23.5 games: 0.41/0.42 mid 41.5%, model 53.9% (projection_v2.0 (prediction ledger)) -- gap +12.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV02JACMAC-MAC5` Will Tomas Machac win at least 4.5 more games than Kyrian Jacquet?: 0.30/0.34 mid 32.0%, model 22.3% (projection_v2.0 (prediction ledger)) -- gap -9.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV02JACMAC-2-MAC` Will Tomas Machac win set 2 in the Kyrian Jacquet vs Tomas Machac match: 0.17/0.79 mid 48.0%, model 56.7% (projection_v2.0 (prediction ledger)) -- gap +8.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV02JACMAC-29` Over 28.5 games: 0.25/0.31 mid 28.0%, model 35.4% (projection_v2.0 (prediction ledger)) -- gap +7.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02JACMAC-MAC21` Will Tomas Machac win the Kyrian Jacquet vs Tomas Machac match by a set score of 2-1?: 0.16/0.26 mid 21.0%, model 27.9% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02JACMAC-MAC20` Will Tomas Machac win the Kyrian Jacquet vs Tomas Machac match by a set score of 2-0?: 0.08/0.44 mid 26.0%, model 32.2% (projection_v2.0 (prediction ledger)) -- gap +6.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV02JACMAC-MAC2` Will Tomas Machac win at least 1.5 more games than Kyrian Jacquet?: 0.57/0.58 mid 57.5%, model 52.6% (projection_v2.0 (prediction ledger)) -- gap -4.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV02JACMAC-19` Over 18.5 games: 0.80/0.86 mid 83.0%, model 87.8% (projection_v2.0 (prediction ledger)) -- gap +4.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV02JACMAC-2-JAC` Will Kyrian Jacquet win set 2 in the Kyrian Jacquet vs Tomas Machac match: 0.17/0.79 mid 48.0%, model 43.3% (projection_v2.0 (prediction ledger)) -- gap -4.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02JACMAC-JAC20` Will Kyrian Jacquet win the Kyrian Jacquet vs Tomas Machac match by a set score of 2-0?: 0.18/0.26 mid 22.0%, model 18.7% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV02JACMAC-1-JAC` Will Kyrian Jacquet win set 1 in the Kyrian Jacquet vs Tomas Machac match: 0.41/0.42 mid 41.5%, model 43.3% (projection_v2.0 (prediction ledger)) -- gap +1.8 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02JACMAC-JAC21` Will Kyrian Jacquet win the Kyrian Jacquet vs Tomas Machac match by a set score of 2-1?: 0.07/0.39 mid 23.0%, model 21.2% (projection_v2.0 (prediction ledger)) -- gap -1.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV02JACMAC-JAC2` Will Kyrian Jacquet win at least 1.5 more games than Tomas Machac?: 0.07/0.56 mid 31.5%, model 32.8% (projection_v2.0 (prediction ledger)) -- gap +1.3 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV02JACMAC-1-MAC` Will Tomas Machac win set 1 in the Kyrian Jacquet vs Tomas Machac match: 0.57/0.59 mid 58.0%, model 56.7% (projection_v2.0 (prediction ledger)) -- gap -1.3 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Carlo Alberto Caniato vs Lorenzo Giustino -- ATP Challenger Taranto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105841:212241:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlo Alberto Caniato (`KXATPCHALLENGERMATCH-26NOV02CANGIU-CAN`) | 0.61 / 0.62 (1317) | 61.5% | -- | 62.2% | 53.5% [46.5%-57.9%] | -- | 62.0% | 62.0% | MODEL_LONE_OUTLIER | PASS | -8.0 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Lorenzo Giustino (`KXATPCHALLENGERMATCH-26NOV02CANGIU-GIU`) | 0.38 / 0.39 (44) | 38.5% | -- | 37.8% | 46.5% [42.1%-53.5%] | -- | 38.2% | 38.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.0 pp | NORMAL | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3539.0, B 5720.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0568
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Hugo Grenier vs Marvin Moeller -- ATP Challenger Taranto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:126409:202359:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hugo Grenier (`KXATPCHALLENGERMATCH-26NOV02GREMOE-GRE`) | 0.59 / 0.60 (1641) | 59.5% | -- | 41.9% | 43.9% [42.9%-44.9%] | -- | 59.4% | 59.4% | MODEL_LONE_OUTLIER | PASS | -15.6 pp | HIGH_REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Marvin Moeller (`KXATPCHALLENGERMATCH-26NOV02GREMOE-MOE`) | 0.41 / 0.42 (2767) | 41.5% | -- | 58.1% | 56.1% [55.1%-57.1%] | -- | 41.0% | 41.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +14.6 pp | REVIEW | FRESH | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4380.0, B 5348.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0101
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Philip Henning vs Calvin Hemery -- ATP Challenger Taranto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 15:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:123921:202475:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Calvin Hemery (`KXATPCHALLENGERMATCH-26NOV02HENHEM-HEM`) | 0.43 / 0.46 (46) | 44.5% | -- | 34.4% | 42.0% [38.1%-49.0%] | -- | 45.8% | -- | INSUFFICIENT_INPUTS | PASS | -2.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Philip Henning (`KXATPCHALLENGERMATCH-26NOV02HENHEM-HEN`) | 0.55 / 0.56 (1077) | 55.5% | -- | 65.6% | 58.0% [51.0%-61.9%] | -- | 54.1% | -- | INSUFFICIENT_INPUTS | PASS | +2.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3868.0, B 4976.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0543
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Sofia Alekseeva vs Lisa Gruber -- W15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260050:270215:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Alekseeva (`KXITFWMATCH-26NOV02ALEGRU-ALE`) | 0.89 / 0.90 (100) | 89.5% | 92.3% | 26.9% | 74.0% [72.2%-74.8%] | -- | -- | -- | -- | PASS | +2.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lisa Gruber (`KXITFWMATCH-26NOV02ALEGRU-GRU`) | 0.09 / 0.10 (32) | 9.5% | 7.6% | 73.1% | 26.0% [25.2%-27.8%] | -- | -- | -- | -- | PASS | -1.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 339.0, B 41.0; serve-point win A 58.3%, B 52.4%; Elo A 1252.5, B 1062.9; model uncertainty 0.013
* Form inputs: days since last match A 231, B 371; matches on record A 8, B 19; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.009, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ilinca Dalina Amariei vs Angelica Raggi -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216051:221168:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ilinca Dalina Amariei (`KXITFWMATCH-26NOV02AMARAG-AMA`) | 0.62 / 0.65 (81) | 63.5% | 58.0% | 60.1% | 57.5% [55.3%-59.0%] | -- | -- | -- | -- | PASS | -5.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Angelica Raggi (`KXITFWMATCH-26NOV02AMARAG-RAG`) | 0.34 / 0.35 (268) | 34.5% | 42.0% | 39.9% | 42.5% [41.0%-44.7%] | -- | -- | -- | -- | WATCH | +7.5 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2360.0, B 2349.0; serve-point win A 51.9%, B 49.6%; Elo A 1534.4, B 1503.9; model uncertainty 0.0185
* Form inputs: days since last match A 329, B 196; matches on record A 325, B 320; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.005, surface_dev_loose -0.016, surface_dev_tight +0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Barhacova vs Lujza Zimenova -- W15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02BARZIM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Barhacova (`KXITFWMATCH-26NOV02BARZIM-BAR`) | 0.56 / 0.58 (3) | 57.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lujza Zimenova (`KXITFWMATCH-26NOV02BARZIM-ZIM`) | 0.39 / 0.40 (41) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alessandra Crump vs Laura Svatikova -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215505:221067:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessandra Crump (`KXITFWMATCH-26NOV02CRUSVA-CRU`) | 0.04 / 0.06 (1129) | 5.0% | 7.4% | 64.6% | 17.5% [15.5%-19.7%] | -- | -- | -- | -- | PASS | +2.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Laura Svatikova (`KXITFWMATCH-26NOV02CRUSVA-SVA`) | 0.94 / 0.97 (462) | 95.5% | 92.6% | 35.4% | 82.5% [80.3%-84.5%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 1657.0; serve-point win A 49.0%, B 40.1%; Elo A 1036.9, B 1303.4; model uncertainty 0.0208
* Form inputs: days since last match A 714, B 350; matches on record A 99, B 244; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.021, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lola Giza vs Jade Groen -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-02T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260503:267722:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lola Giza (`KXITFWMATCH-26NOV02GIZGRO-GIZ`) | 0.62 / 0.64 (5) | 63.0% | 34.6% | 24.3% | 37.9% [32.9%-42.6%] | -- | -- | -- | -- | PASS | -28.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jade Groen (`KXITFWMATCH-26NOV02GIZGRO-GRO`) | 0.36 / 0.39 (146) | 37.5% | 65.4% | 75.7% | 62.1% [57.4%-67.1%] | -- | -- | -- | -- | PASS | +27.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 432.0, B 470.0; serve-point win A 51.2%, B 45.9%; Elo A 1241.0, B 1292.1; model uncertainty 0.0483
* Form inputs: days since last match A 455, B 357; matches on record A 14, B 9; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV02GIZGRO-GRO  (YES = Jade Groen)
Model: 65%
Kalshi: 38%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amelie Justine Hejtmanek vs Anika Jaskova -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-02T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222637:260323:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amelie Justine Hejtmanek (`KXITFWMATCH-26NOV02HEJJAS-HEJ`) | 0.62 / 0.65 (120) | 63.5% | 44.3% | 55.4% | 45.7% [43.6%-48.9%] | -- | -- | -- | -- | PASS | -19.2 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anika Jaskova (`KXITFWMATCH-26NOV02HEJJAS-JAS`) | 0.34 / 0.37 (141) | 35.5% | 55.7% | 44.6% | 54.3% [51.1%-56.4%] | -- | -- | -- | -- | PASS | +20.2 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1296.0, B 199.0; serve-point win A 50.8%, B 48.1%; Elo A 1350.9, B 1389.6; model uncertainty 0.0265
* Form inputs: days since last match A 196, B 455; matches on record A 54, B 182; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV02HEJJAS-JAS  (YES = Anika Jaskova)
Model: 56%
Kalshi: 36%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Iakukhina vs Anna Boron -- W15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:270160:270379:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Boron (`KXITFWMATCH-26NOV02IAKBOR-BOR`) | 0.37 / 0.39 (51) | 38.0% | 35.4% | 34.8% | 44.1% [43.1%-44.7%] | -- | -- | -- | -- | PASS | -2.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofia Iakukhina (`KXITFWMATCH-26NOV02IAKBOR-IAK`) | 0.59 / 0.64 (76) | 61.5% | 64.6% | 65.2% | 55.9% [55.3%-56.9%] | -- | -- | -- | -- | PASS | +3.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 94.0, B 173.0; serve-point win A 52.9%, B 49.9%; Elo A 1255.9, B 1215.6; model uncertainty 0.0081
* Form inputs: days since last match A 343, B 427; matches on record A 1, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Astrid Lew Yan Foon vs Mirjana Jovanovic -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:235159:260993:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mirjana Jovanovic (`KXITFWMATCH-26NOV02LEWJOV-JOV`) | 0.07 / 0.09 (32) | 8.0% | 8.4% | 19.9% | 19.5% [17.4%-21.7%] | -- | -- | -- | -- | WATCH | +0.4 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Astrid Lew Yan Foon (`KXITFWMATCH-26NOV02LEWJOV-LEW`) | 0.90 / 0.92 (167) | 91.0% | 91.6% | 80.1% | 80.5% [78.3%-82.6%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1722.0, B 871.0; serve-point win A 61.4%, B 49.0%; Elo A 1525.8, B 1277.7; model uncertainty 0.0216
* Form inputs: days since last match A 119, B 210; matches on record A 180, B 117; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.023, surface_dev_loose +0.003, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kira Pavlova vs Tilwith Di Girolami -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223302:228910:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tilwith Di Girolami (`KXITFWMATCH-26NOV02PAVDIG-DIG`) | 0.30 / 0.31 (79) | 30.5% | 32.2% | 35.4% | 32.4% [29.6%-35.4%] | -- | -- | -- | -- | PASS | +1.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kira Pavlova (`KXITFWMATCH-26NOV02PAVDIG-PAV`) | 0.66 / 0.68 (141) | 67.0% | 67.8% | 64.6% | 67.6% [64.6%-70.4%] | -- | -- | -- | -- | PASS | +0.8 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2405.0, B 1533.0; serve-point win A 54.6%, B 48.9%; Elo A 1588.9, B 1440.2; model uncertainty 0.0287
* Form inputs: days since last match A 210, B 189; matches on record A 230, B 202; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.019, surface_dev_loose +0.028, surface_dev_tight -0.029
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gloria Pop vs Timea Gross -- W15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:268802:270491:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Timea Gross (`KXITFWMATCH-26NOV02POPGRO-GRO`) | 0.27 / 0.30 (78) | 28.5% | 53.9% | 67.0% | 60.5% [59.5%-61.5%] | -- | -- | -- | -- | PASS | +25.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gloria Pop (`KXITFWMATCH-26NOV02POPGRO-POP`) | 0.71 / 0.72 (114) | 71.5% | 46.1% | 33.0% | 39.5% [38.5%-40.5%] | -- | -- | -- | -- | PASS | -25.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 292.0, B 149.0; serve-point win A 54.5%, B 44.8%; Elo A 1242.6, B 1309.2; model uncertainty 0.0101
* Form inputs: days since last match A 308, B 189; matches on record A 7, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV02POPGRO-GRO  (YES = Timea Gross)
Model: 54%
Kalshi: 28%
Gap: +25 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cristiana Nicoleta Todoni vs Jessica Bertoldo -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216075:261104:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jessica Bertoldo (`KXITFWMATCH-26NOV02TODBER-BER`) | 0.39 / 0.46 (111) | 42.5% | 64.2% | 55.3% | 63.6% [61.6%-67.6%] | -- | -- | -- | -- | WATCH | +21.7 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Cristiana Nicoleta Todoni (`KXITFWMATCH-26NOV02TODBER-TOD`) | 0.54 / 0.57 (100) | 55.5% | 35.8% | 44.7% | 36.4% [32.4%-38.4%] | -- | -- | -- | -- | PASS | -19.7 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 865.0, B 1651.0; serve-point win A 50.4%, B 46.9%; Elo A 1304.5, B 1439.6; model uncertainty 0.0298
* Form inputs: days since last match A 113, B 203; matches on record A 57, B 169; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV02TODBER-BER  (YES = Jessica Bertoldo)
Model: 64%
Kalshi: 42%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.005, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stephanie Judith Visscher vs Clervie Ngounoue -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 15:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T15:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220613:238064:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clervie Ngounoue (`KXITFWMATCH-26NOV02VISNGO-NGO`) | 0.71 / 0.72 (100) | 71.5% | 62.7% | 29.9% | 44.4% [37.4%-66.3%] | -- | -- | -- | -- | PASS | -8.8 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stephanie Judith Visscher (`KXITFWMATCH-26NOV02VISNGO-VIS`) | 0.26 / 0.28 (53) | 27.0% | 37.2% | 70.1% | 55.6% [33.7%-62.6%] | -- | -- | -- | -- | WATCH | +10.2 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3377.0, B 2509.0; serve-point win A 59.4%, B 38.1%; Elo A 1566.0, B 1704.5; model uncertainty 0.1442
* Form inputs: days since last match A 50, B 70; matches on record A 453, B 153; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.015, surface_dev_tight -0.025
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jonas Forejtek vs Matthew William Donald -- ATP Challenger Bratislava II Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 15:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-02T15:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207797:210054:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matthew William Donald (`KXATPCHALLENGERMATCH-26NOV02FORDON-DON`) | 0.36 / 0.37 (1176) | 36.5% | -- | 43.8% | 40.2% [37.7%-42.2%] | -- | -- | -- | -- | WATCH | +3.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jonas Forejtek (`KXATPCHALLENGERMATCH-26NOV02FORDON-FOR`) | 0.62 / 0.63 (6) | 62.5% | -- | 56.2% | 59.8% [57.8%-62.3%] | -- | -- | -- | -- | PASS | -2.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4481.0, B 3065.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0226
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Eero Vasa vs Vadym Ursu -- ATP Challenger Bratislava II Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 15:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-02T15:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:134068:144814:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vadym Ursu (`KXATPCHALLENGERMATCH-26NOV02VASURS-URS`) | 0.47 / 0.49 (43) | 48.0% | -- | 39.3% | 36.8% [33.9%-41.3%] | -- | -- | -- | -- | PASS | -11.2 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eero Vasa (`KXATPCHALLENGERMATCH-26NOV02VASURS-VAS`) | 0.52 / 0.53 (110) | 52.5% | -- | 60.7% | 63.2% [58.7%-66.1%] | -- | -- | -- | -- | SHADOW_BET | +10.7 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3099.0, B 3850.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0369
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.019, surface_dev_loose +0.029, surface_dev_tight -0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Diana Martynov vs Sandra Samir -- WTA 125K Luanda R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 18:30Z
* Current expected start: 2026-11-02 15:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 14:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Hard · scheduled 2026-11-02T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211529:221157:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Diana Martynov (`KXWTACHALLENGERMATCH-26NOV02MARSAM-MAR`) | 0.61 / 0.62 (1577) | 61.5% | -- | 16.1% | 24.3% [19.6%-33.4%] | -- | 62.0% | 62.0% | MODEL_LONE_OUTLIER | PASS | -37.2 pp | EXTREME (DATA_WARNING) | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Sandra Samir (`KXWTACHALLENGERMATCH-26NOV02MARSAM-SAM`) | 0.38 / 0.39 (348) | 38.5% | -- | 83.9% | 75.7% [66.6%-80.4%] | -- | 38.4% | 38.4% | MODEL_LONE_OUTLIER | WATCH | +37.2 pp | EXTREME (DATA_WARNING) | FRESH | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1861.0, B 4604.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0692
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXWTACHALLENGERMATCH-26NOV02MARSAM-SAM  (YES = Sandra Samir)
Model: 76%
Kalshi: 38%
Gap: +37 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: AGREES_WITH_KALSHI
Data quality: A (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.004, surface_dev_tight -0.000
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE

## Alex Molcan vs Titouan Droguet -- ATP Paris R64

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 18:40Z
* Current expected start: 2026-11-02 16:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 15:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-160_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-02T18:40:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144684:208169:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Titouan Droguet (`KXATPMATCH-26NOV02MOLDRO-DRO`) | 0.45 / 0.46 (1212) | 45.5% | 55.6% | 56.9% | 56.5% [54.5%-58.4%] | -- | -- | -- | -- | SHADOW_BET | +10.1 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alex Molcan (`KXATPMATCH-26NOV02MOLDRO-MOL`) | 0.54 / 0.55 (2658) | 54.5% | 44.4% | 43.1% | 43.5% [41.6%-45.5%] | -- | -- | -- | -- | PASS | -10.1 pp | REVIEW | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4355.0, B 6214.0; serve-point win A 63.4%, B 35.5%; Elo A 1756.0, B 1794.6; model uncertainty 0.0193
* Form inputs: days since last match A 2, B 8; matches on record A 555, B 430; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.019, surface_dev_tight +0.019
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26NOV02MOLDRO-MOL5` Will Alex Molcan win at least 4.5 more games than Titouan Droguet?: 0.04/0.69 mid 36.5%, model 13.4% (projection_v2.0 (prediction ledger)) -- gap -23.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV02MOLDRO-19` Over 18.5 games: 0.53/0.92 mid 72.5%, model 88.6% (projection_v2.0 (prediction ledger)) -- gap +16.1 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV02MOLDRO-DRO2` Will Titouan Droguet win at least 1.5 more games than Alex Molcan?: 0.14/0.56 mid 35.0%, model 48.0% (projection_v2.0 (prediction ledger)) -- gap +13.0 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02MOLDRO-DRO21` Will Titouan Droguet win the Alex Molcan vs Titouan Droguet match by a set score of 2-1?: 0.01/0.27 mid 14.0%, model 26.7% (projection_v2.0 (prediction ledger)) -- gap +12.7 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02MOLDRO-DRO20` Will Titouan Droguet win the Alex Molcan vs Titouan Droguet match by a set score of 2-0?: 0.01/0.32 mid 16.5%, model 28.9% (projection_v2.0 (prediction ledger)) -- gap +12.4 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02MOLDRO-MOL21` Will Alex Molcan win the Alex Molcan vs Titouan Droguet match by a set score of 2-1?: 0.02/0.27 mid 14.5%, model 23.0% (projection_v2.0 (prediction ledger)) -- gap +8.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV02MOLDRO-24` Over 23.5 games: 0.47/0.48 mid 47.5%, model 54.7% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV02MOLDRO-29` Over 28.5 games: 0.09/0.50 mid 29.5%, model 36.3% (projection_v2.0 (prediction ledger)) -- gap +6.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV02MOLDRO-1-DRO` Will Titouan Droguet win set 1 in the Alex Molcan vs Titouan Droguet match: 0.45/0.49 mid 47.0%, model 53.7% (projection_v2.0 (prediction ledger)) -- gap +6.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV02MOLDRO-1-MOL` Will Alex Molcan win set 1 in the Alex Molcan vs Titouan Droguet match: 0.50/0.55 mid 52.5%, model 46.3% (projection_v2.0 (prediction ledger)) -- gap -6.2 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV02MOLDRO-2-DRO` Will Titouan Droguet win set 2 in the Alex Molcan vs Titouan Droguet match: 0.03/0.93 mid 48.0%, model 53.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV02MOLDRO-MOL20` Will Alex Molcan win the Alex Molcan vs Titouan Droguet match by a set score of 2-0?: 0.02/0.37 mid 19.5%, model 21.4% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV02MOLDRO-2-MOL` Will Alex Molcan win set 2 in the Alex Molcan vs Titouan Droguet match: 0.03/0.93 mid 48.0%, model 46.3% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV02MOLDRO-MOL2` Will Alex Molcan win at least 1.5 more games than Titouan Droguet?: 0.13/0.62 mid 37.5%, model 37.0% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Leolia Jeanjean vs Lucia Bronzetti -- WTA 125K Cali R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 19:00Z
* Current expected start: 2026-11-02 16:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 15:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-11-02T19:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:206417:214459:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucia Bronzetti (`KXWTACHALLENGERMATCH-26NOV02JEABRO-BRO`) | 0.42 / 0.45 (24) | 43.5% | -- | 33.0% | 35.0% [33.5%-38.5%] | -- | -- | -- | -- | PASS | -8.5 pp | NORMAL | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Leolia Jeanjean (`KXWTACHALLENGERMATCH-26NOV02JEABRO-JEA`) | 0.54 / 0.55 (55) | 54.5% | -- | 67.0% | 65.0% [61.5%-66.5%] | -- | -- | -- | -- | PASS | +10.5 pp | REVIEW | FRESH | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4130.0, B 4550.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.025
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.015, surface_dev_tight -0.020
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Maria Camila Torres Murcia vs Luisina Giovannini -- WTA 125K Cali R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 19:00Z
* Current expected start: 2026-11-02 16:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 15:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-11-02T19:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:222000:236972:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luisina Giovannini (`KXWTACHALLENGERMATCH-26NOV02TORGIO-GIO`) | 0.96 / 0.97 (787) | 96.5% | -- | 98.6% | 96.2% [92.7%-97.8%] | -- | -- | -- | -- | WATCH | -0.3 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Camila Torres Murcia (`KXWTACHALLENGERMATCH-26NOV02TORGIO-TOR`) | 0.04 / 0.05 (412) | 4.5% | -- | 1.4% | 3.8% [2.2%-7.3%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1147.0, B 3057.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0254
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.007, surface_dev_tight +0.006
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Santiago De la Fuente vs Ryo Tabata -- ATP Challenger Villa Maria Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-02T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208099:212944:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Santiago De la Fuente (`KXATPCHALLENGERMATCH-26NOV02DLFTAB-DLF`) | 0.52 / 0.53 (405) | 52.5% | -- | 46.4% | 49.5% [46.4%-52.1%] | -- | -- | -- | -- | PASS | -3.0 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ryo Tabata (`KXATPCHALLENGERMATCH-26NOV02DLFTAB-TAB`) | 0.47 / 0.49 (1116) | 48.0% | -- | 53.6% | 50.5% [47.9%-53.6%] | -- | -- | -- | -- | PASS | +2.5 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2660.0, B 1648.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0286
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.011, surface_dev_loose -0.031, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Tomas Farjat vs Federico Aguilar Cardozo -- ATP Challenger Villa Maria Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-02T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208078:212481:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Aguilar Cardozo (`KXATPCHALLENGERMATCH-26NOV02FARAGU-AGU`) | 0.58 / 0.60 (1025) | 59.0% | -- | 47.4% | 42.8% [41.3%-43.8%] | -- | -- | -- | -- | PASS | -16.2 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tomas Farjat (`KXATPCHALLENGERMATCH-26NOV02FARAGU-FAR`) | 0.40 / 0.41 (1154) | 40.5% | -- | 52.6% | 57.2% [56.2%-58.7%] | -- | -- | -- | -- | PASS | +16.7 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2227.0, B 884.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0127
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV02FARAGU-FAR  (YES = Tomas Farjat)
Model: 57%
Kalshi: 40%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE

## Lorenzo Gagliardo vs Ian Luca Vertberger -- ATP Challenger Villa Maria Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02GAGVER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Gagliardo (`KXATPCHALLENGERMATCH-26NOV02GAGVER-GAG`) | 0.88 / 0.89 (1445) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ian Luca Vertberger (`KXATPCHALLENGERMATCH-26NOV02GAGVER-VER`) | 0.11 / 0.12 (15) | 11.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Nahia Berecoechea vs Anastasiya Kuparev -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222171:223398:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nahia Berecoechea (`KXITFWMATCH-26NOV02BERKUP-BER`) | 0.91 / 0.94 (397) | 92.5% | 95.1% | 91.6% | 90.3% [88.0%-92.0%] | -- | -- | -- | -- | PASS | +2.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasiya Kuparev (`KXITFWMATCH-26NOV02BERKUP-KUP`) | 0.06 / 0.08 (135) | 7.0% | 4.9% | 8.4% | 9.7% [8.0%-12.0%] | -- | -- | -- | -- | WATCH | -2.1 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1894.0, B 723.0; serve-point win A 59.1%, B 53.2%; Elo A 1547.8, B 1178.2; model uncertainty 0.0197
* Form inputs: days since last match A 203, B 217; matches on record A 250, B 121; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.013, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tessa Johanna Brockmann vs Georgina Garcia-Perez -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:202916:260598:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tessa Johanna Brockmann (`KXITFWMATCH-26NOV02BROGAR-BRO`) | 0.76 / 0.78 (2) | 77.0% | 74.2% | 81.7% | 60.3% [55.3%-65.3%] | -- | -- | -- | -- | PASS | -2.8 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Georgina Garcia-Perez (`KXITFWMATCH-26NOV02BROGAR-GAR`) | 0.22 / 0.23 (248) | 22.5% | 25.8% | 18.3% | 39.7% [34.7%-44.7%] | -- | -- | -- | -- | WATCH | +3.3 pp | NORMAL | FRESH | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3426.0, B 507.0; serve-point win A 60.4%, B 44.5%; Elo A 1598.4, B 1586.6; model uncertainty 0.0502
* Form inputs: days since last match A 20, B 50; matches on record A 169, B 484; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.031, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anna Hsu vs Oriana Gniewkowska -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-02T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264215:266749:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oriana Gniewkowska (`KXITFWMATCH-26NOV02HSUGNI-GNI`) | 0.96 / 0.97 (625) | 96.5% | 91.9% | 53.2% | 68.6% [67.6%-69.5%] | -- | -- | -- | -- | PASS | -4.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Hsu (`KXITFWMATCH-26NOV02HSUGNI-HSU`) | 0.04 / 0.05 (411) | 4.5% | 8.1% | 46.8% | 31.4% [30.5%-32.4%] | -- | -- | -- | -- | PASS | +3.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 34.0, B 810.0; serve-point win A 45.5%, B 44.1%; Elo A 1172.9, B 1310.9; model uncertainty 0.0093
* Form inputs: days since last match A 238, B 385; matches on record A 3, B 34; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Urszula Radwanska vs Lenka Munzarova -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 16:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-02T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:201524:222982:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lenka Munzarova (`KXITFWMATCH-26NOV02RADMUN-MUN`) | 0.21 / 0.24 (131) | 22.5% | 22.7% | 65.1% | 36.4% [26.1%-44.7%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Urszula Radwanska (`KXITFWMATCH-26NOV02RADMUN-RAD`) | 0.73 / 0.79 (240) | 76.0% | 77.3% | 34.9% | 63.6% [55.3%-73.9%] | -- | -- | -- | -- | PASS | +1.3 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1581.0, B 269.0; serve-point win A 57.2%, B 48.4%; Elo A 1457.3, B 1320.6; model uncertainty 0.0931
* Form inputs: days since last match A 91, B 189; matches on record A 840, B 13; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.058, surface_pool_high -0.051, surface_dev_loose -0.015, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victoria Allen vs Sofia Kryvoruchko -- W50 Heraklion R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216253:269993:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victoria Allen (`KXITFWMATCH-26NOV02ALLKRY-ALL`) | 0.88 / 0.91 (324) | 89.5% | 82.2% | 74.1% | 70.1% [69.2%-71.5%] | -- | -- | -- | -- | PASS | -7.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sofia Kryvoruchko (`KXITFWMATCH-26NOV02ALLKRY-KRY`) | 0.08 / 0.11 (130) | 9.5% | 17.8% | 25.9% | 29.9% [28.5%-30.8%] | -- | -- | -- | -- | PASS | +8.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1893.0, B 335.0; serve-point win A 60.4%, B 46.6%; Elo A 1480.5, B 1341.9; model uncertainty 0.0116
* Form inputs: days since last match A 156, B 427; matches on record A 83, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.009, surface_dev_loose +0.004, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lucie Petruzelova vs Marta Lombardini -- W50 Heraklion R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221219:267409:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marta Lombardini (`KXITFWMATCH-26NOV02PETLOM-LOM`) | 0.65 / 0.66 (2) | 65.5% | 78.6% | 76.5% | 74.0% [69.4%-77.3%] | -- | -- | -- | -- | WATCH | +13.1 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lucie Petruzelova (`KXITFWMATCH-26NOV02PETLOM-PET`) | 0.33 / 0.34 (42) | 33.5% | 21.4% | 23.5% | 26.0% [22.7%-30.6%] | -- | -- | -- | -- | PASS | -12.1 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1518.0, B 984.0; serve-point win A 50.5%, B 43.6%; Elo A 1281.7, B 1447.1; model uncertainty 0.0394
* Form inputs: days since last match A 203, B 40; matches on record A 141, B 25; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.017, surface_dev_loose -0.008, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Styliani Roussopoulou vs Matilde Paoletti -- W50 Heraklion R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222396:257893:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matilde Paoletti (`KXITFWMATCH-26NOV02ROUPAO-PAO`) | 0.95 / 0.97 (385) | 96.0% | 98.5% | 67.1% | 89.1% [87.0%-92.1%] | -- | -- | -- | -- | PASS | +2.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Styliani Roussopoulou (`KXITFWMATCH-26NOV02ROUPAO-ROU`) | 0.03 / 0.05 (739) | 4.0% | 1.5% | 32.9% | 10.9% [7.9%-13.0%] | -- | -- | -- | -- | PASS | -2.5 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 185.0, B 466.0; serve-point win A 44.2%, B 39.6%; Elo A 1182.7, B 1577.0; model uncertainty 0.0256
* Form inputs: days since last match A 343, B 210; matches on record A 35, B 103; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.018, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sarah Van Emst vs Thea Marcu -- W50 Heraklion R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 16:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02VANMAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thea Marcu (`KXITFWMATCH-26NOV02VANMAR-MAR`) | 0.03 / 0.06 (147) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sarah Van Emst (`KXITFWMATCH-26NOV02VANMAR-VAN`) | 0.94 / 0.95 (100) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexandra Biot vs Alexandra Bayuschenko -- W15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02BIOBAY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandra Bayuschenko (`KXITFWMATCH-26NOV02BIOBAY-BAY`) | 0.21 / 0.26 (4) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexandra Biot (`KXITFWMATCH-26NOV02BIOBAY-BIO`) | 0.72 / 0.75 (100) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lea Fojcik vs Lena Ramharter -- W15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260047:264106:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lea Fojcik (`KXITFWMATCH-26NOV02FOJRAM-FOJ`) | 0.67 / 0.72 (16) | 69.5% | 83.3% | 50.0% | 75.6% [75.6%-75.6%] | -- | -- | -- | -- | PASS | +13.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Lena Ramharter (`KXITFWMATCH-26NOV02FOJRAM-RAM`) | 0.28 / 0.31 (8) | 29.5% | 16.7% | 50.0% | 24.4% [24.4%-24.4%] | -- | -- | -- | -- | PASS | -12.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 57.5%, B 49.7%; Elo A 1285.8, B 1088.5; model uncertainty 0.0
* Form inputs: days since last match A 1155, B 714; matches on record A 3, B 36; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexia-Shara Iancu vs Lora Kardos -- W15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260262:267641:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexia-Shara Iancu (`KXITFWMATCH-26NOV02IANKAR-IAN`) | 0.40 / 0.47 (156) | 43.5% | 57.2% | 32.9% | 54.3% [53.2%-55.3%] | -- | -- | -- | -- | PASS | +13.7 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lora Kardos (`KXITFWMATCH-26NOV02IANKAR-KAR`) | 0.54 / 0.56 (6) | 55.0% | 42.8% | 67.1% | 45.7% [44.7%-46.8%] | -- | -- | -- | -- | PASS | -12.2 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 74.0, B 126.0; serve-point win A 52.9%, B 48.4%; Elo A 1259.2, B 1218.5; model uncertainty 0.0106
* Form inputs: days since last match A 308, B 364; matches on record A 57, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vanesa Salaiova vs Viktoria Varga -- W15 Szabolcsveresmart R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 17:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:249669:270261:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vanesa Salaiova (`KXITFWMATCH-26NOV02SALVAR-SAL`) | 0.16 / 0.17 (13) | 16.5% | 51.1% | 60.0% | 51.1% [51.0%-53.1%] | -- | -- | -- | -- | PASS | +34.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Viktoria Varga (`KXITFWMATCH-26NOV02SALVAR-VAR`) | 0.81 / 0.82 (5) | 81.5% | 48.9% | 40.1% | 48.9% [46.9%-48.9%] | -- | -- | -- | -- | PASS | -32.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 53.0, B 139.0; serve-point win A 56.0%, B 44.2%; Elo A 1261.7, B 1251.1; model uncertainty 0.0105
* Form inputs: days since last match A 238, B 364; matches on record A 1, B 14; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV02SALVAR-SAL  (YES = Vanesa Salaiova)
Model: 51%
Kalshi: 16%
Gap: +35 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.011, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mateo Del Pino vs Joao Victor Couto Loureiro -- ATP Challenger Villa Maria Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-02T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208533:210182:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Victor Couto Loureiro (`KXATPCHALLENGERMATCH-26NOV02DELCOU-COU`) | 0.71 / 0.72 (1037) | 71.5% | -- | 49.5% | 51.0% [49.0%-52.1%] | -- | -- | -- | -- | PASS | -20.5 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mateo Del Pino (`KXATPCHALLENGERMATCH-26NOV02DELCOU-DEL`) | 0.28 / 0.29 (27) | 28.5% | -- | 50.5% | 49.0% [47.9%-51.0%] | -- | -- | -- | -- | WATCH | +20.5 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1424.0, B 2307.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0155
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV02DELCOU-DEL  (YES = Mateo Del Pino)
Model: 49%
Kalshi: 28%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.010, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE

## Victor Hugo Remondy Pagotto vs Ivan Dreycopp -- ATP Challenger Villa Maria Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-02T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210403:212762:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ivan Dreycopp (`KXATPCHALLENGERMATCH-26NOV02REMDRE-DRE`) | 0.44 / 0.45 (37) | 44.5% | -- | 45.8% | 57.2% [55.7%-59.2%] | -- | -- | -- | -- | PASS | +12.7 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Victor Hugo Remondy Pagotto (`KXATPCHALLENGERMATCH-26NOV02REMDRE-REM`) | 0.55 / 0.57 (92) | 56.0% | -- | 54.2% | 42.8% [40.8%-44.3%] | -- | -- | -- | -- | PASS | -13.2 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1016.0, B 293.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0177
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.015, surface_dev_loose +0.010, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE

## Franco Ribero vs Nicolas Bruna -- ATP Challenger Villa Maria Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 17:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-02T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202220:202305:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Bruna (`KXATPCHALLENGERMATCH-26NOV02RIBBRU-BRU`) | 0.42 / 0.43 (44) | 42.5% | -- | 30.4% | 32.2% [28.6%-40.4%] | -- | -- | -- | -- | PASS | -10.3 pp | REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Franco Ribero (`KXATPCHALLENGERMATCH-26NOV02RIBBRU-RIB`) | 0.57 / 0.58 (1591) | 57.5% | -- | 69.6% | 67.8% [59.6%-71.4%] | -- | -- | -- | -- | WATCH | +10.3 pp | REVIEW | FRESH | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2261.0, B 1663.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.059
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.028, surface_pool_high +0.027, surface_dev_loose +0.014, surface_dev_tight -0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Carolina Alves vs Maria Paulina Perez Garcia -- WTA 125K Cali R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 20:10Z
* Current expected start: 2026-11-02 17:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 16:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · surface ? · scheduled 2026-11-02T20:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV02ALVPER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carolina Alves (`KXWTACHALLENGERMATCH-26NOV02ALVPER-ALV`) | 0.94 / 0.95 (333) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maria Paulina Perez Garcia (`KXWTACHALLENGERMATCH-26NOV02ALVPER-PER`) | 0.05 / 0.07 (1250) | 6.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Selena Janicijevic vs Solana Sierra -- WTA 125K Cali R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 20:10Z
* Current expected start: 2026-11-02 17:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 16:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · surface ? · scheduled 2026-11-02T20:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV02JANSIE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Selena Janicijevic (`KXWTACHALLENGERMATCH-26NOV02JANSIE-JAN`) | 0.19 / 0.25 (64) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Solana Sierra (`KXWTACHALLENGERMATCH-26NOV02JANSIE-SIE`) | 0.74 / 0.80 (109) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Emma Slavikova vs Daria Gorska -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-02T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:239126:239484:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daria Gorska (`KXITFWMATCH-26NOV02SLAGOR-GOR`) | 0.49 / 0.53 (161) | 51.0% | 31.5% | 35.4% | 40.5% [37.9%-42.6%] | -- | -- | -- | -- | PASS | -19.5 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Emma Slavikova (`KXITFWMATCH-26NOV02SLAGOR-SLA`) | 0.46 / 0.48 (78) | 47.0% | 68.5% | 64.6% | 59.5% [57.4%-62.1%] | -- | -- | -- | -- | WATCH | +21.5 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1128.0, B 685.0; serve-point win A 54.3%, B 49.3%; Elo A 1326.8, B 1271.3; model uncertainty 0.0234
* Form inputs: days since last match A 189, B 92; matches on record A 137, B 63; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV02SLAGOR-SLA  (YES = Emma Slavikova)
Model: 69%
Kalshi: 47%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.016, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amy Sucha vs Danka Kovinic -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 17:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-02T17:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:203575:266407:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Danka Kovinic (`KXITFWMATCH-26NOV02SUCKOV-KOV`) | 0.61 / 0.62 (267) | 61.5% | 93.6% | 60.6% | 86.9% [82.6%-92.1%] | -- | -- | -- | -- | PASS | +32.1 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amy Sucha (`KXITFWMATCH-26NOV02SUCKOV-SUC`) | 0.39 / 0.40 (221) | 39.5% | 6.4% | 39.4% | 13.1% [7.9%-17.4%] | -- | -- | -- | -- | PASS | -33.1 pp | EXTREME (DATA_WARNING) | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 650.0, B 1093.0; serve-point win A 47.3%, B 41.3%; Elo A 1357.5, B 1815.8; model uncertainty 0.0479
* Form inputs: days since last match A 196, B 6; matches on record A 18, B 671; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV02SUCKOV-KOV  (YES = Danka Kovinic)
Model: 94%
Kalshi: 62%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.012, surface_pool_high -0.016, surface_dev_loose -0.003, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Denis Shapovalov vs Karen Khachanov -- ATP Paris R64

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 18:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 17:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111575:133430:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karen Khachanov (`KXATPMATCH-26NOV01SHAKHA-KHA`) | 0.60 / 0.61 (6182) | 60.5% | 59.8% | 61.2% | 58.8% [56.9%-59.7%] | -- | -- | -- | -- | PASS | -0.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Denis Shapovalov (`KXATPMATCH-26NOV01SHAKHA-SHA`) | 0.38 / 0.39 (10072) | 38.5% | 40.2% | 38.8% | 41.2% [40.3%-43.1%] | -- | -- | -- | -- | WATCH | +1.7 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4653.0, B 5835.0; serve-point win A 64.1%, B 33.9%; Elo A 1932.3, B 1936.1; model uncertainty 0.0144
* Form inputs: days since last match A 3, B 5; matches on record A 582, B 765; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.014, surface_dev_loose +0.005, surface_dev_tight -0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPSETWINNER-26NOV01SHAKHA-2-KHA` Will Karen Khachanov win set 2 in the Denis Shapovalov vs Karen Khachanov match: 0.07/0.80 mid 43.5%, model 56.5% (projection_v2.0 (prediction ledger)) -- gap +13.1 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV01SHAKHA-18` Over 17.5 games: 0.71/0.94 mid 82.5%, model 94.4% (projection_v2.0 (prediction ledger)) -- gap +11.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01SHAKHA-KHA6` Will Karen Khachanov win at least 5.5 more games than Denis Shapovalov?: 0.03/0.40 mid 21.5%, model 10.6% (projection_v2.0 (prediction ledger)) -- gap -10.9 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01SHAKHA-KHA20` Will Karen Khachanov win the Denis Shapovalov vs Karen Khachanov match by a set score of 2-0?: 0.02/0.45 mid 23.5%, model 32.0% (projection_v2.0 (prediction ledger)) -- gap +8.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01SHAKHA-KHA21` Will Karen Khachanov win the Denis Shapovalov vs Karen Khachanov match by a set score of 2-1?: 0.02/0.38 mid 20.0%, model 27.8% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01SHAKHA-SHA2` Will Denis Shapovalov win at least 1.5 more games than Karen Khachanov?: 0.23/0.56 mid 39.5%, model 32.8% (projection_v2.0 (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01SHAKHA-23` Over 22.5 games: 0.56/0.57 mid 56.5%, model 62.0% (projection_v2.0 (prediction ledger)) -- gap +5.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01SHAKHA-2-SHA` Will Denis Shapovalov win set 2 in the Denis Shapovalov vs Karen Khachanov match: 0.01/0.80 mid 40.5%, model 43.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01SHAKHA-KHA3` Will Karen Khachanov win at least 2.5 more games than Denis Shapovalov?: 0.46/0.47 mid 46.5%, model 43.9% (projection_v2.0 (prediction ledger)) -- gap -2.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01SHAKHA-28` Over 27.5 games: 0.29/0.58 mid 43.5%, model 41.6% (projection_v2.0 (prediction ledger)) -- gap -1.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01SHAKHA-SHA21` Will Denis Shapovalov win the Denis Shapovalov vs Karen Khachanov match by a set score of 2-1?: 0.01/0.39 mid 20.0%, model 21.3% (projection_v2.0 (prediction ledger)) -- gap +1.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01SHAKHA-SHA20` Will Denis Shapovalov win the Denis Shapovalov vs Karen Khachanov match by a set score of 2-0?: 0.01/0.39 mid 20.0%, model 18.9% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01SHAKHA-1-KHA` Will Karen Khachanov win set 1 in the Denis Shapovalov vs Karen Khachanov match: 0.56/0.59 mid 57.5%, model 56.5% (projection_v2.0 (prediction ledger)) -- gap -0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01SHAKHA-1-SHA` Will Denis Shapovalov win set 1 in the Denis Shapovalov vs Karen Khachanov match: 0.41/0.44 mid 42.5%, model 43.5% (projection_v2.0 (prediction ledger)) -- gap +0.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Nishesh Basavareddy vs Milos Karol -- ATP Challenger Bratislava II R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-02T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209984:210460:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nishesh Basavareddy (`KXATPCHALLENGERMATCH-26NOV02BASKAR-BAS`) | 0.73 / 0.74 (1626) | 73.5% | -- | 69.2% | 70.0% [68.7%-72.2%] | -- | -- | -- | -- | PASS | -3.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Milos Karol (`KXATPCHALLENGERMATCH-26NOV02BASKAR-KAR`) | 0.26 / 0.27 (1098) | 26.5% | -- | 30.8% | 29.9% [27.8%-31.3%] | -- | -- | -- | -- | WATCH | +3.5 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3957.0, B 3195.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0175
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.013, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Daniel Milavsky vs Shunsuke Mitsui -- ATP Challenger Charlottesville Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-02T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210034:212251:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Milavsky (`KXATPCHALLENGERMATCH-26NOV02MILMIT-MIL`) | 0.64 / 0.66 (1035) | 65.0% | -- | 46.0% | 48.5% [47.0%-54.0%] | -- | -- | -- | -- | PASS | -16.5 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Shunsuke Mitsui (`KXATPCHALLENGERMATCH-26NOV02MILMIT-MIT`) | 0.34 / 0.35 (83) | 34.5% | -- | 54.0% | 51.5% [46.0%-53.0%] | -- | -- | -- | -- | WATCH | +17.0 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3740.0, B 2112.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0351
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality C

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV02MILMIT-MIT  (YES = Shunsuke Mitsui)
Model: 52%
Kalshi: 34%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.005, surface_dev_loose +0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Luka Pavlovic vs Aleksandr Shevchenko -- ATP Challenger Bratislava II R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-02T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202146:207686:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luka Pavlovic (`KXATPCHALLENGERMATCH-26NOV02PAVSHE-PAV`) | 0.36 / 0.37 (132) | 36.5% | -- | 30.5% | 32.2% [30.9%-34.1%] | -- | 36.7% | 36.7% | MARKETS_AGREE | PASS | -4.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | AMBIGUOUS |
| Aleksandr Shevchenko (`KXATPCHALLENGERMATCH-26NOV02PAVSHE-SHE`) | 0.63 / 0.64 (1325) | 63.5% | -- | 69.5% | 67.8% [66.0%-69.1%] | -- | 63.9% | 63.9% | MARKETS_AGREE | PASS | +4.3 pp | NORMAL | FRESH | A / ADEQUATE | ALL_AGREE | AMBIGUOUS |

* Serve evidence (points): A 3728.0, B 5512.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0158
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.014, surface_dev_loose -0.013, surface_dev_tight +0.018
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## James Kent Trotter vs Ozan Baris -- ATP Challenger Charlottesville Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-02T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208801:210028:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ozan Baris (`KXATPCHALLENGERMATCH-26NOV02TROBAR-BAR`) | 0.46 / 0.47 (1036) | 46.5% | -- | 32.0% | 36.1% [34.8%-37.5%] | -- | -- | -- | -- | PASS | -10.3 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| James Kent Trotter (`KXATPCHALLENGERMATCH-26NOV02TROBAR-TRO`) | 0.52 / 0.54 (1036) | 53.0% | -- | 68.0% | 63.8% [62.5%-65.2%] | -- | -- | -- | -- | PASS | +10.8 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 223.0, B 1211.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0134
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.009, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Andronicou / Sara vs Dorofeeva-Rybas / Golovina -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-02T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02ANDSARDORGOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andronicou / Sara (`KXITFWDOUBLES-26NOV02ANDSARDORGOL-ANDSAR`) | 0.05 / 0.10 (27) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Dorofeeva-Rybas / Golovina (`KXITFWDOUBLES-26NOV02ANDSARDORGOL-DORGOL`) | 0.85 / 0.90 (1) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Gavrila / Sakellaridi vs Kusy / Spasova -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-02T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02GAVSAKKUSSPA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gavrila / Sakellaridi (`KXITFWDOUBLES-26NOV02GAVSAKKUSSPA-GAVSAK`) | 0.80 / 0.94 (10) | 87.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kusy / Spasova (`KXITFWDOUBLES-26NOV02GAVSAKKUSSPA-KUSSPA`) | 0.03 / 0.06 (195) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Gaia Maduzzi vs Gina Marie Dittmann -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222273:266431:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gina Marie Dittmann (`KXITFWMATCH-26NOV02MADDIT-DIT`) | 0.21 / 0.25 (5) | 23.0% | 23.9% | 31.9% | 34.4% [31.5%-37.9%] | -- | -- | -- | -- | WATCH | +0.9 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gaia Maduzzi (`KXITFWMATCH-26NOV02MADDIT-MAD`) | 0.71 / 0.78 (111) | 74.5% | 76.1% | 68.1% | 65.6% [62.1%-68.5%] | -- | -- | -- | -- | PASS | +1.6 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1969.0, B 1885.0; serve-point win A 55.3%, B 50.0%; Elo A 1508.7, B 1412.4; model uncertainty 0.0322
* Form inputs: days since last match A 6, B 210; matches on record A 62, B 115; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isabella Maria Serban vs Selina Dal -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223399:265197:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Selina Dal (`KXITFWMATCH-26NOV02SERDAL-DAL`) | 0.46 / 0.47 (10) | 46.5% | 70.2% | 77.7% | 70.9% [66.1%-74.9%] | -- | -- | -- | -- | PASS | +23.8 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Isabella Maria Serban (`KXITFWMATCH-26NOV02SERDAL-SER`) | 0.52 / 0.53 (4) | 52.5% | 29.8% | 22.3% | 29.1% [25.1%-33.9%] | -- | -- | -- | -- | PASS | -22.8 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2134.0, B 867.0; serve-point win A 50.9%, B 45.1%; Elo A 1448.9, B 1571.0; model uncertainty 0.0439
* Form inputs: days since last match A 6, B 189; matches on record A 116, B 186; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV02SERDAL-DAL  (YES = Selina Dal)
Model: 70%
Kalshi: 46%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.005, surface_dev_loose -0.027, surface_dev_tight +0.023
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stoyanov / Yesypchuk vs Seraphidou / Georgiana Serban -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-02T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02STOYESSERGEO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Seraphidou / Georgiana Serban (`KXITFWDOUBLES-26NOV02STOYESSERGEO-SERGEO`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stoyanov / Yesypchuk (`KXITFWDOUBLES-26NOV02STOYESSERGEO-STOYES`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Polona Hercog vs Leyre Romero Gormaz -- WTA 125K Cali R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 21:20Z
* Current expected start: 2026-11-02 19:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 18:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · surface ? · scheduled 2026-11-02T21:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV02HERROM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polona Hercog (`KXWTACHALLENGERMATCH-26NOV02HERROM-HER`) | 0.38 / 0.45 (63) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Leyre Romero Gormaz (`KXWTACHALLENGERMATCH-26NOV02HERROM-ROM`) | 0.53 / 0.59 (2) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Laura Samson vs Yuliana Lizarazo -- WTA 125K Cali R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-02 21:20Z
* Current expected start: 2026-11-02 19:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 18:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · surface ? · scheduled 2026-11-02T21:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV02SAMLIZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuliana Lizarazo (`KXWTACHALLENGERMATCH-26NOV02SAMLIZ-LIZ`) | 0.05 / 0.06 (26) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Laura Samson (`KXWTACHALLENGERMATCH-26NOV02SAMLIZ-SAM`) | 0.90 / 0.94 (183) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Vitor Machado De Melo Cunha vs Filipe Bullamah -- M15 Salvador R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02CUNBUL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filipe Bullamah (`KXITFMATCH-26NOV02CUNBUL-BUL`) | 0.31 / 0.35 (166) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vitor Machado De Melo Cunha (`KXITFMATCH-26NOV02CUNBUL-CUN`) | 0.63 / 0.67 (100) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Guilherme Barbieri Renner vs Agustin Eduardo Cuellar Lorberg -- M15 Salvador R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-02T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208273:214225:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agustin Eduardo Cuellar Lorberg (`KXITFMATCH-26NOV02RENCUE-CUE`) | 0.48 / 0.51 (64) | 49.5% | 25.7% | 55.8% | 29.8% [29.2%-31.6%] | -- | -- | -- | -- | PASS | -23.8 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Guilherme Barbieri Renner (`KXITFMATCH-26NOV02RENCUE-REN`) | 0.47 / 0.50 (1) | 48.5% | 74.3% | 44.2% | 70.2% [68.5%-70.8%] | -- | -- | -- | -- | PASS | +25.8 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 50.0, B 169.0; serve-point win A 58.8%, B 46.1%; Elo A 1248.8, B 1097.6; model uncertainty 0.0117
* Form inputs: days since last match A 370, B 342; matches on record A 1, B 8; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV02RENCUE-REN  (YES = Guilherme Barbieri Renner)
Model: 74%
Kalshi: 48%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.000, surface_dev_loose -0.008, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pedro Rodrigues Longobardi vs Laelson Rodrigues -- M15 Salvador R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-02T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:109946:207832:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Rodrigues Longobardi (`KXITFMATCH-26NOV02RODROD2-ROD`) | 0.45 / 0.49 (62) | 47.0% | -- | 96.0% | 90.4% [88.6%-93.2%] | -- | -- | -- | -- | PASS | +43.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Laelson Rodrigues (`KXITFMATCH-26NOV02RODROD2-ROD2`) | 0.51 / 0.55 (105) | 53.0% | -- | 4.0% | 9.6% [6.8%-11.4%] | -- | -- | -- | -- | PASS | -43.4 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 1514.0, B 238.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.023
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV02RODROD2-ROD  (YES = Pedro Rodrigues Longobardi)
Model: 90%
Kalshi: 47%
Gap: +43 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.000, surface_dev_loose +0.007, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ebeling Koning / Tsygourova vs Grammatikopoulou / Yardley -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-02T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02EBETSYGRAYAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ebeling Koning / Tsygourova (`KXITFWDOUBLES-26NOV02EBETSYGRAYAR-EBETSY`) | 0.85 / 0.90 (1) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Grammatikopoulou / Yardley (`KXITFWDOUBLES-26NOV02EBETSYGRAYAR-GRAYAR`) | 0.05 / 0.09 (27) | 7.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Amandine Hesse vs Tamila Gadamauri -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:203281:260446:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tamila Gadamauri (`KXITFWMATCH-26NOV02HESGAD-GAD`) | 0.27 / 0.30 (146) | 28.5% | 46.0% | 65.6% | 54.3% [41.5%-60.0%] | -- | -- | -- | -- | PASS | +17.5 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amandine Hesse (`KXITFWMATCH-26NOV02HESGAD-HES`) | 0.69 / 0.73 (5) | 71.0% | 54.0% | 34.4% | 45.7% [40.0%-58.5%] | -- | -- | -- | -- | PASS | -17.0 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2021.0, B 2577.0; serve-point win A 54.6%, B 46.2%; Elo A 1575.8, B 1491.0; model uncertainty 0.0924
* Form inputs: days since last match A 22, B 252; matches on record A 777, B 57; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV02HESGAD-GAD  (YES = Tamila Gadamauri)
Model: 46%
Kalshi: 28%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.011, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luna Morini vs Abril Pajello -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-02T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221064:266726:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luna Morini (`KXITFWMATCH-26NOV02MORPAJ-MOR`) | 0.92 / 0.94 (229) | 93.0% | 79.4% | 50.0% | 57.4% [57.4%-57.4%] | -- | -- | -- | -- | PASS | -13.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Abril Pajello (`KXITFWMATCH-26NOV02MORPAJ-PAJ`) | 0.05 / 0.07 (105) | 6.0% | 20.6% | 50.0% | 42.6% [42.6%-42.6%] | -- | -- | -- | -- | PASS | +14.6 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 57.0%, B 49.2%; Elo A 1263.9, B 1210.5; model uncertainty 0.0
* Form inputs: days since last match A 3122, B 973; matches on record A 1, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Agustina Tarantola vs Jazmin Baier -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02TARBAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jazmin Baier (`KXITFWMATCH-26NOV02TARBAI-BAI`) | 0.03 / 0.08 (16) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Agustina Tarantola (`KXITFWMATCH-26NOV02TARBAI-TAR`) | 0.92 / 0.95 (132) | 93.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Aiken Tejada vs Luciana Agudelo -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-02T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266453:270250:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luciana Agudelo (`KXITFWMATCH-26NOV02TEJAGU-AGU`) | 0.90 / 0.92 (398) | 91.0% | 92.3% | 24.7% | 74.0% [71.3%-75.7%] | -- | -- | -- | -- | PASS | +1.3 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aiken Tejada (`KXITFWMATCH-26NOV02TEJAGU-TEJ`) | 0.07 / 0.10 (369) | 8.5% | 7.7% | 75.3% | 26.0% [24.3%-28.7%] | -- | -- | -- | -- | PASS | -0.8 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 55.0, B 79.0; serve-point win A 47.6%, B 41.7%; Elo A 1065.7, B 1262.7; model uncertainty 0.0216
* Form inputs: days since last match A 364, B 371; matches on record A 19, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isis Louise Van den Broek vs Jana Otzipka -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260445:264227:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jana Otzipka (`KXITFWMATCH-26NOV02VANOTZ-OTZ`) | 0.40 / 0.43 (5) | 41.5% | 27.3% | 29.5% | 30.0% [27.7%-33.4%] | -- | -- | -- | -- | PASS | -14.2 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Isis Louise Van den Broek (`KXITFWMATCH-26NOV02VANOTZ-VAN`) | 0.57 / 0.60 (8) | 58.5% | 72.7% | 70.5% | 70.0% [66.6%-72.3%] | -- | -- | -- | -- | WATCH | +14.2 pp | REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1856.0, B 908.0; serve-point win A 53.4%, B 51.1%; Elo A 1579.5, B 1434.0; model uncertainty 0.0284
* Form inputs: days since last match A 189, B 189; matches on record A 103, B 98; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.018, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Samuel Heredia vs Justin Boulais -- ATP Challenger Charlottesville Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-02T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207993:212831:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justin Boulais (`KXATPCHALLENGERMATCH-26NOV02HERBOU-BOU`) | 0.76 / 0.77 (410) | 76.5% | -- | 81.4% | 81.1% [78.2%-82.7%] | -- | -- | -- | -- | WATCH | +4.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Samuel Heredia (`KXATPCHALLENGERMATCH-26NOV02HERBOU-HER`) | 0.23 / 0.24 (72) | 23.5% | -- | 18.6% | 18.9% [17.3%-21.8%] | -- | -- | -- | -- | PASS | -4.6 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2713.0, B 3260.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0227
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.007, surface_dev_loose -0.017, surface_dev_tight +0.018
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Mitchell Krueger vs Andrew Fenty -- ATP Challenger Charlottesville Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-02T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106283:208649:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrew Fenty (`KXATPCHALLENGERMATCH-26NOV02KRUFEN-FEN`) | 0.31 / 0.34 (690) | 32.5% | -- | 40.6% | 35.8% [30.3%-38.6%] | -- | -- | -- | -- | PASS | +3.3 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mitchell Krueger (`KXATPCHALLENGERMATCH-26NOV02KRUFEN-KRU`) | 0.66 / 0.68 (25) | 67.0% | -- | 59.4% | 64.2% [61.4%-69.7%] | -- | -- | -- | -- | PASS | -2.8 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4228.0, B 3101.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0417
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.019, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Ugo Humbert vs Botic Van de Zandschulp -- ATP Paris R64

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-01 13:00Z (day placeholder, not a start time)
* Current expected start: 2026-11-02 19:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: 2026-11-02 18:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-01T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:122298:200005:2026-11-01`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ugo Humbert (`KXATPMATCH-26NOV01HUMVAN-HUM`) | 0.59 / 0.60 (7549) | 59.5% | 56.1% | 54.9% | 55.9% [54.9%-56.4%] | -- | -- | -- | -- | PASS | -3.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Botic Van de Zandschulp (`KXATPMATCH-26NOV01HUMVAN-VAN`) | 0.40 / 0.41 (4515) | 40.5% | 43.9% | 45.1% | 44.1% [43.6%-45.1%] | -- | -- | -- | -- | SHADOW_BET | +3.4 pp | NORMAL | FRESH | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4892.0, B 5999.0; serve-point win A 65.9%, B 35.3%; Elo A 1938.3, B 1883.9; model uncertainty 0.0072
* Form inputs: days since last match A 4, B 5; matches on record A 625, B 651; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose -0.000, surface_dev_tight +0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV01HUMVAN-24` Over 23.5 games: 0.43/0.45 mid 44.0%, model 55.5% (projection_v2.0 (prediction ledger)) -- gap +11.5 pp, REVIEW, REVIEW_CONTEXT, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01HUMVAN-HUM3` Will Ugo Humbert win at least 2.5 more games than Botic Van de Zandschulp?: 0.48/0.50 mid 49.0%, model 40.3% (projection_v2.0 (prediction ledger)) -- gap -8.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HUMVAN-2-HUM` Will Ugo Humbert win set 2 in the Ugo Humbert vs Botic Van de Zandschulp match: 0.12/0.80 mid 46.0%, model 54.1% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HUMVAN-VAN21` Will Botic Van de Zandschulp win the Ugo Humbert vs Botic Van de Zandschulp match by a set score of 2-1?: 0.07/0.23 mid 15.0%, model 22.8% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HUMVAN-HUM21` Will Ugo Humbert win the Ugo Humbert vs Botic Van de Zandschulp match by a set score of 2-1?: 0.01/0.39 mid 20.0%, model 26.9% (projection_v2.0 (prediction ledger)) -- gap +6.9 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HUMVAN-VAN20` Will Botic Van de Zandschulp win the Ugo Humbert vs Botic Van de Zandschulp match by a set score of 2-0?: 0.01/0.28 mid 14.5%, model 21.1% (projection_v2.0 (prediction ledger)) -- gap +6.6 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV01HUMVAN-HUM20` Will Ugo Humbert win the Ugo Humbert vs Botic Van de Zandschulp match by a set score of 2-0?: 0.02/0.45 mid 23.5%, model 29.2% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV01HUMVAN-HUM6` Will Ugo Humbert win at least 5.5 more games than Botic Van de Zandschulp?: 0.09/0.20 mid 14.5%, model 9.1% (projection_v2.0 (prediction ledger)) -- gap -5.4 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01HUMVAN-19` Over 18.5 games: 0.79/0.92 mid 85.5%, model 90.2% (projection_v2.0 (prediction ledger)) -- gap +4.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV01HUMVAN-29` Over 28.5 games: 0.27/0.40 mid 33.5%, model 38.0% (projection_v2.0 (prediction ledger)) -- gap +4.5 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HUMVAN-1-HUM` Will Ugo Humbert win set 1 in the Ugo Humbert vs Botic Van de Zandschulp match: 0.57/0.59 mid 58.0%, model 54.1% (projection_v2.0 (prediction ledger)) -- gap -3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HUMVAN-1-VAN` Will Botic Van de Zandschulp win set 1 in the Ugo Humbert vs Botic Van de Zandschulp match: 0.40/0.44 mid 42.0%, model 45.9% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV01HUMVAN-VAN2` Will Botic Van de Zandschulp win at least 1.5 more games than Ugo Humbert?: 0.36/0.42 mid 39.0%, model 36.3% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote FRESH, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV01HUMVAN-2-VAN` Will Botic Van de Zandschulp win set 2 in the Ugo Humbert vs Botic Van de Zandschulp match: 0.08/0.80 mid 44.0%, model 45.9% (projection_v2.0 (prediction ledger)) -- gap +1.9 pp, NORMAL, OK, quote FRESH, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anna Kmiecik vs Barbora Michalkova -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-02T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259981:267734:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Kmiecik (`KXITFWMATCH-26NOV02KMIMIC-KMI`) | 0.61 / 0.63 (67) | 62.0% | 56.8% | 74.5% | 62.1% [56.4%-67.6%] | -- | -- | -- | -- | PASS | -5.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Barbora Michalkova (`KXITFWMATCH-26NOV02KMIMIC-MIC`) | 0.33 / 0.36 (3) | 34.5% | 43.2% | 25.5% | 37.9% [32.4%-43.6%] | -- | -- | -- | -- | PASS | +8.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 758.0, B 1187.0; serve-point win A 52.5%, B 48.8%; Elo A 1370.4, B 1330.8; model uncertainty 0.0561
* Form inputs: days since last match A 203, B 196; matches on record A 22, B 86; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jialin Tian vs Klara Blazkova -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02TIABLA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Klara Blazkova (`KXITFWMATCH-26NOV02TIABLA-BLA`) | 0.21 / 0.22 (251) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jialin Tian (`KXITFWMATCH-26NOV02TIABLA-TIA`) | 0.77 / 0.78 (131) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mitchell Dobek vs Danny Al Barbour -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02DOBALB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Danny Al Barbour (`KXITFMATCH-26NOV02DOBALB-ALB`) | 0.30 / 0.38 (5) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mitchell Dobek (`KXITFMATCH-26NOV02DOBALB-DOB`) | 0.60 / 0.64 (6) | 62.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bruno Fernandez vs Nicolas Kicker -- ATP Challenger Villa Maria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02FERKIC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bruno Fernandez (`KXATPCHALLENGERMATCH-26NOV02FERKIC-FER`) | 0.16 / 0.20 (56) | 18.0% | -- | -- | -- [-----] | -- | 17.0% | 17.0% | MODEL_LONE_OUTLIER | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nicolas Kicker (`KXATPCHALLENGERMATCH-26NOV02FERKIC-KIC`) | 0.78 / 0.83 (59) | 80.5% | -- | -- | -- [-----] | -- | 79.9% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE

## Matt Kuhar vs Tareq Alani -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02KUHALA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tareq Alani (`KXITFMATCH-26NOV02KUHALA-ALA`) | 0.30 / 0.34 (5) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matt Kuhar (`KXITFMATCH-26NOV02KUHALA-KUH`) | 0.63 / 0.69 (1) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eric Von Marton Martins vs Joao Cunha Cunha -- M15 Salvador R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02MARCUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Cunha Cunha (`KXITFMATCH-26NOV02MARCUN-CUN`) | 0.61 / 0.65 (0) | 63.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eric Von Marton Martins (`KXITFMATCH-26NOV02MARCUN-MAR`) | 0.32 / 0.34 (42) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thomas Enrique Menzel Piccioli vs Mateus Napoli da Silveira -- M15 Salvador R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02MENNAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thomas Enrique Menzel Piccioli (`KXITFMATCH-26NOV02MENNAP-MEN`) | 0.72 / 0.78 (214) | 75.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mateus Napoli da Silveira (`KXITFMATCH-26NOV02MENNAP-NAP`) | 0.22 / 0.25 (47) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tyler Mercier vs Nicholas Adesalu -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202108:213807:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicholas Adesalu (`KXITFMATCH-26NOV02MERADE-ADE`) | 0.12 / 0.16 (7) | 14.0% | 60.3% | 42.8% | 61.3% [60.3%-62.2%] | -- | -- | -- | -- | PASS | +46.3 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tyler Mercier (`KXITFMATCH-26NOV02MERADE-MER`) | 0.83 / 0.84 (144) | 83.5% | 39.7% | 57.2% | 38.7% [37.8%-39.7%] | -- | -- | -- | -- | PASS | -43.8 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 54.0, B 248.0; serve-point win A 58.2%, B 39.8%; Elo A 1118.2, B 1204.8; model uncertainty 0.0095
* Form inputs: days since last match A 441, B 567; matches on record A 102, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV02MERADE-ADE  (YES = Nicholas Adesalu)
Model: 60%
Kalshi: 14%
Gap: +46 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ignacio Monzon / Lorenzo Joaquin Rodriguez vs Ryan Nijboer / Oriol Roca Batalla -- ATP Challenger Villa Maria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-02T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02MONRODNIJROC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ignacio Monzon / Lorenzo Joaquin Rodriguez (`KXATPCHALLENGERDOUBLES-26NOV02MONRODNIJROC-MONROD`) | 0.05 / 0.94 (25) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ryan Nijboer / Oriol Roca Batalla (`KXATPCHALLENGERDOUBLES-26NOV02MONRODNIJROC-NIJROC`) | 0.05 / 0.94 (25) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Glauco Pinheiro da Cruz Junior vs Miguel Daiha -- M15 Salvador R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02PINDAI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miguel Daiha (`KXITFMATCH-26NOV02PINDAI-DAI`) | 0.10 / 0.15 (6) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Glauco Pinheiro da Cruz Junior (`KXITFMATCH-26NOV02PINDAI-PIN`) | 0.79 / 0.88 (130) | 83.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rohan Sachdev vs Leon Achurra Correa -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02SACACH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leon Achurra Correa (`KXITFMATCH-26NOV02SACACH-ACH`) | 0.21 / 0.23 (5) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rohan Sachdev (`KXITFMATCH-26NOV02SACACH-SAC`) | 0.76 / 0.79 (0) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pilar Da Silva vs Felicitas Simon Padros -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02DASSIM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pilar Da Silva (`KXITFWMATCH-26NOV02DASSIM-DAS`) | 0.63 / 0.75 (3) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Felicitas Simon Padros (`KXITFWMATCH-26NOV02DASSIM-SIM`) | 0.24 / 0.33 (10) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zoe Doldan vs Angela Portoman -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-02T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266456:269847:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zoe Doldan (`KXITFWMATCH-26NOV02DOLPOR-DOL`) | 0.82 / 0.88 (8) | 85.0% | 63.1% | 50.0% | 57.4% [57.4%-57.4%] | -- | -- | -- | -- | PASS | -21.9 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Angela Portoman (`KXITFWMATCH-26NOV02DOLPOR-POR`) | 0.12 / 0.18 (14) | 15.0% | 36.9% | 50.0% | 42.6% [42.6%-42.6%] | -- | -- | -- | -- | PASS | +21.9 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 55.1%, B 47.3%; Elo A 1244.4, B 1191.4; model uncertainty 0.0
* Form inputs: days since last match A 742, B 791; matches on record A 1, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV02DOLPOR-POR  (YES = Angela Portoman)
Model: 37%
Kalshi: 15%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Gabriela Kawano Cho vs Camila Bertolini -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02KAWBER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Camila Bertolini (`KXITFWMATCH-26NOV02KAWBER-BER`) | 0.03 / 0.05 (1640) | 4.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gabriela Kawano Cho (`KXITFWMATCH-26NOV02KAWBER-KAW`) | 0.92 / 0.98 (899) | 95.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andres Martin vs Stiles Brockett -- ATP Challenger Charlottesville Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 20:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T20:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02MARBRO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stiles Brockett (`KXATPCHALLENGERMATCH-26NOV02MARBRO-BRO`) | 0.18 / 0.19 (7) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Andres Martin (`KXATPCHALLENGERMATCH-26NOV02MARBRO-MAR`) | 0.80 / 0.82 (1623) | 81.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Aidan Mayo vs Kenta Miyoshi (b. 2004) -- ATP Challenger Charlottesville Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 20:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T20:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02MAYMIY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aidan Mayo (`KXATPCHALLENGERMATCH-26NOV02MAYMIY-MAY`) | 0.63 / 0.65 (57) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kenta Miyoshi (b. 2004) (`KXATPCHALLENGERMATCH-26NOV02MAYMIY-MIY`) | 0.35 / 0.36 (23) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Matthew Michibata vs Lucas Hammond -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02MICHAM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Hammond (`KXITFMATCH-26NOV02MICHAM-HAM`) | 0.71 / 0.75 (151) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matthew Michibata (`KXITFMATCH-26NOV02MICHAM-MIC`) | 0.23 / 0.28 (0) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kim Johannes Niethammer vs Steven McCartney -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02NIEMCC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Steven McCartney (`KXITFMATCH-26NOV02NIEMCC-MCC`) | 0.07 / 0.11 (134) | 9.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kim Johannes Niethammer (`KXITFMATCH-26NOV02NIEMCC-NIE`) | 0.86 / 0.91 (116) | 88.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hernan Casanova / Franco Ribero vs Franco Agamenone / Juan Estevez -- ATP Challenger Villa Maria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-02T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02CASRIBAGAEST:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Franco Agamenone / Juan Estevez (`KXATPCHALLENGERDOUBLES-26NOV02CASRIBAGAEST-AGAEST`) | 0.05 / 0.77 (5) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hernan Casanova / Franco Ribero (`KXATPCHALLENGERDOUBLES-26NOV02CASRIBAGAEST-CASRIB`) | 0.36 / 0.94 (25) | 65.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ben Chetewy Ungar vs Jonny Degroot -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02CHEDEG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ben Chetewy Ungar (`KXITFMATCH-26NOV02CHEDEG-CHE`) | 0.50 / 0.90 (3) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jonny Degroot (`KXITFMATCH-26NOV02CHEDEG-DEG`) | 0.07 / 0.50 (5) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniel Elahi Galan vs Joao Eduardo Schiessl -- ATP Challenger Costa do Sauipe Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02GALSCH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Elahi Galan (`KXATPCHALLENGERMATCH-26NOV02GALSCH-GAL`) | 0.74 / 0.75 (2101) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Joao Eduardo Schiessl (`KXATPCHALLENGERMATCH-26NOV02GALSCH-SCH`) | 0.25 / 0.26 (12) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Aydan Gomez Osorio vs Alexander Bravo -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149127:207966:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexander Bravo (`KXITFMATCH-26NOV02GOMBRA-BRA`) | 0.34 / 0.44 (4) | 39.0% | 40.1% | 25.4% | 44.8% [44.8%-44.9%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Aydan Gomez Osorio (`KXITFMATCH-26NOV02GOMBRA-GOM`) | 0.57 / 0.68 (4) | 62.5% | 60.0% | 74.6% | 55.2% [55.1%-55.2%] | -- | -- | -- | -- | PASS | -2.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 138.0; serve-point win A 60.7%, B 41.3%; Elo A 1217.7, B 1186.1; model uncertainty 0.0001
* Form inputs: days since last match A 805, B 371; matches on record A 7, B 12; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pedro Petroski Rocha vs Alexander Wriedt -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02PETWRI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Petroski Rocha (`KXITFMATCH-26NOV02PETWRI-PET`) | 0.50 / 0.89 (4) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Wriedt (`KXITFMATCH-26NOV02PETWRI-WRI`) | 0.14 / 0.55 (4) | 34.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Santiago Rodriguez Taverna vs Wilson Leite -- ATP Challenger Costa do Sauipe Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02RODLEI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wilson Leite (`KXATPCHALLENGERMATCH-26NOV02RODLEI-LEI`) | 0.16 / 0.18 (1063) | 17.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Santiago Rodriguez Taverna (`KXATPCHALLENGERMATCH-26NOV02RODLEI-ROD`) | 0.82 / 0.83 (1424) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Miguel Tobon vs Leonardo Storck Franca -- ATP Challenger Costa do Sauipe Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02TOBSTO:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Leonardo Storck Franca (`KXATPCHALLENGERMATCH-26NOV02TOBSTO-STO`) | 0.16 / 0.19 (1340) | 17.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Miguel Tobon (`KXATPCHALLENGERMATCH-26NOV02TOBSTO-TOB`) | 0.81 / 0.83 (30) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Tadeo Meneo / Fermin Tenti vs Murkel Dellien / Arklon Huertas Del Pino Cordova -- ATP Challenger Villa Maria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 21:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-02T21:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02MENTENDEVHUE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Murkel Dellien / Arklon Huertas Del Pino Cordova (`KXATPCHALLENGERDOUBLES-26NOV02MENTENDEVHUE-DEVHUE`) | 0.41 / 0.94 (25) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tadeo Meneo / Fermin Tenti (`KXATPCHALLENGERDOUBLES-26NOV02MENTENDEVHUE-MENTEN`) | 0.05 / 0.70 (1) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lucio Ratti vs Maximo Zeitune -- ATP Challenger Villa Maria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 21:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T21:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02RATZEI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucio Ratti (`KXATPCHALLENGERMATCH-26NOV02RATZEI-RAT`) | 0.35 / 0.40 (65) | 37.5% | -- | -- | -- [-----] | -- | 35.2% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maximo Zeitune (`KXATPCHALLENGERMATCH-26NOV02RATZEI-ZEI`) | 0.60 / 0.63 (0) | 61.5% | -- | -- | -- [-----] | -- | 64.9% | -- | INSUFFICIENT_INPUTS | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE

## Romain Gales vs Caden Colburne -- M15 Trois-Rivières R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02GALCOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caden Colburne (`KXITFMATCH-26NOV02GALCOL-COL`) | 0.07 / 0.09 (6) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Romain Gales (`KXITFMATCH-26NOV02GALCOL-GAL`) | 0.87 / 0.94 (27) | 90.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefano Lacroce vs Eric David Verdes -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02LACVER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefano Lacroce (`KXITFMATCH-26NOV02LACVER-LAC`) | 0.05 / 0.06 (147) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eric David Verdes (`KXITFMATCH-26NOV02LACVER-VER`) | 0.94 / 0.97 (504) | 95.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ana Julieta Lopez Ocampos vs Daphne Belen Marquez -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-02T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264200:269888:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ana Julieta Lopez Ocampos (`KXITFWMATCH-26NOV02LOPMAR-LOP`) | 0.06 / 0.92 (2) | 49.0% | 49.5% | 50.0% | 56.4% [53.2%-59.5%] | -- | -- | -- | -- | PASS | +0.5 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daphne Belen Marquez (`KXITFWMATCH-26NOV02LOPMAR-MAR`) | 0.05 / 0.92 (2) | 48.5% | 50.5% | 50.0% | 43.6% [40.5%-46.8%] | -- | -- | -- | -- | PASS | +2.0 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 53.8%, B 46.1%; Elo A 1218.6, B 1174.9; model uncertainty 0.0315
* Form inputs: days since last match A 728, B 714; matches on record A 2, B 39; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.031, surface_pool_high -0.032, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Simon Padros vs Sofia Nahiara Nappi -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV02SIMNAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Nahiara Nappi (`KXITFWMATCH-26NOV02SIMNAP-NAP`) | 0.09 / 0.93 (5) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofia Simon Padros (`KXITFWMATCH-26NOV02SIMNAP-SIM`) | 0.05 / 0.92 (5) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marcelo Tomas Barrios Vera vs Henrique Rocha -- ATP Challenger Costa do Sauipe R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02BARROC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcelo Tomas Barrios Vera (`KXATPCHALLENGERMATCH-26NOV02BARROC-BAR`) | 0.33 / 0.38 (41) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Henrique Rocha (`KXATPCHALLENGERMATCH-26NOV02BARROC-ROC`) | 0.61 / 0.64 (30) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Hernando Jose Escurra Isnardi vs Yuki Ikeda -- M15 Salvador R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-02T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200622:214366:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hernando Jose Escurra Isnardi (`KXITFMATCH-26NOV02ESCIKE-ESC`) | 0.91 / 0.95 (621) | 93.0% | 41.7% | 44.9% | 35.1% [35.0%-36.0%] | -- | -- | -- | -- | PASS | -51.3 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuki Ikeda (`KXITFMATCH-26NOV02ESCIKE-IKE`) | 0.05 / 0.06 (26) | 5.5% | 58.3% | 55.1% | 64.9% [64.0%-65.0%] | -- | -- | -- | -- | PASS | +52.8 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 505.0, B 41.0; serve-point win A 60.6%, B 37.8%; Elo A 1174.9, B 1280.3; model uncertainty 0.0051
* Form inputs: days since last match A 44, B 308; matches on record A 61, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV02ESCIKE-IKE  (YES = Yuki Ikeda)
Model: 58%
Kalshi: 6%
Gap: +53 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jack Kennedy vs Hynek Barton -- ATP Challenger Charlottesville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02KENBAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hynek Barton (`KXATPCHALLENGERMATCH-26NOV02KENBAR-BAR`) | 0.65 / 0.67 (9) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jack Kennedy (`KXATPCHALLENGERMATCH-26NOV02KENBAR-KEN`) | 0.31 / 0.35 (14) | 33.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Nicolas Mejia vs Murphy Cassone -- ATP Challenger Charlottesville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02MEJCAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Murphy Cassone (`KXATPCHALLENGERMATCH-26NOV02MEJCAS-CAS`) | 0.52 / 0.55 (44) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nicolas Mejia (`KXATPCHALLENGERMATCH-26NOV02MEJCAS-MEJ`) | 0.40 / 0.47 (27) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kaue Noatto vs Vitor Leal -- M15 Salvador R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-02T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211508:213613:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vitor Leal (`KXITFMATCH-26NOV02NOALEA-LEA`) | 0.25 / 0.32 (28) | 28.5% | 60.5% | 74.8% | 46.9% [45.9%-49.0%] | -- | -- | -- | -- | PASS | +32.0 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kaue Noatto (`KXITFMATCH-26NOV02NOALEA-NOA`) | 0.63 / 0.73 (160) | 68.0% | 39.5% | 25.2% | 53.1% [51.0%-54.1%] | -- | -- | -- | -- | PASS | -28.5 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 89.0, B 0.0; serve-point win A 59.8%, B 38.2%; Elo A 1194.2, B 1173.4; model uncertainty 0.0154
* Form inputs: days since last match A 287, B 854; matches on record A 3, B 27; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV02NOALEA-LEA  (YES = Vitor Leal)
Model: 60%
Kalshi: 28%
Gap: +32 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.020, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Midori Castillo Meza vs Judith Hernandez Miranda -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221915:222665:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Midori Castillo Meza (`KXITFWMATCH-26NOV02CASHER-CAS`) | 0.72 / 0.80 (51) | 76.0% | 64.3% | 70.8% | 53.2% [47.9%-60.0%] | -- | -- | -- | -- | PASS | -11.7 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Judith Hernandez Miranda (`KXITFWMATCH-26NOV02CASHER-HER`) | 0.19 / 0.25 (59) | 22.0% | 35.7% | 29.2% | 46.8% [40.0%-52.1%] | -- | -- | -- | -- | PASS | +13.7 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 835.0, B 185.0; serve-point win A 55.8%, B 47.0%; Elo A 1272.9, B 1268.5; model uncertainty 0.0607
* Form inputs: days since last match A 203, B 189; matches on record A 65, B 110; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.021, surface_dev_loose +0.011, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maddalena Giordano vs Ana Carmen Zamburek -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220642:221979:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maddalena Giordano (`KXITFWMATCH-26NOV02GIOZAM-GIO`) | 0.10 / 0.11 (16) | 10.5% | 25.2% | 15.2% | 25.2% [23.5%-27.8%] | -- | -- | -- | -- | PASS | +14.8 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ana Carmen Zamburek (`KXITFWMATCH-26NOV02GIOZAM-ZAM`) | 0.86 / 0.92 (23) | 89.0% | 74.8% | 84.8% | 74.8% [72.2%-76.5%] | -- | -- | -- | -- | PASS | -14.2 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1760.0, B 216.0; serve-point win A 51.0%, B 44.0%; Elo A 1179.5, B 1347.5; model uncertainty 0.0215
* Form inputs: days since last match A 189, B 364; matches on record A 144, B 27; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.026, surface_dev_loose -0.000, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Misa Malkin vs Fernanda Guadalupe Regalado Macias -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221923:222509:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Misa Malkin (`KXITFWMATCH-26NOV02MALREG-MAL`) | 0.89 / 0.91 (289) | 90.0% | 97.7% | 87.0% | 89.6% [88.9%-91.4%] | -- | -- | -- | -- | PASS | +7.7 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Fernanda Guadalupe Regalado Macias (`KXITFWMATCH-26NOV02MALREG-REG`) | 0.06 / 0.11 (12) | 8.5% | 2.3% | 13.0% | 10.4% [8.6%-11.1%] | -- | -- | -- | -- | PASS | -6.2 pp | NORMAL | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 892.0, B 168.0; serve-point win A 57.7%, B 57.3%; Elo A 1364.5, B 982.1; model uncertainty 0.0127
* Form inputs: days since last match A 238, B 245; matches on record A 39, B 26; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mateus Alves vs Filip Misolic -- ATP Challenger Costa do Sauipe Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 22:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T22:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02ALVMIS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateus Alves (`KXATPCHALLENGERMATCH-26NOV02ALVMIS-ALV`) | 0.26 / 0.29 (33) | 27.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Filip Misolic (`KXATPCHALLENGERMATCH-26NOV02ALVMIS-MIS`) | 0.71 / 0.73 (27) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Eduardo Ribeiro vs Luis Felipe Miguel -- ATP Challenger Costa do Sauipe Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 22:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T22:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02RIBMIG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Felipe Miguel (`KXATPCHALLENGERMATCH-26NOV02RIBMIG-MIG`) | 0.36 / 0.37 (216) | 36.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Eduardo Ribeiro (`KXATPCHALLENGERMATCH-26NOV02RIBMIG-RIB`) | 0.62 / 0.63 (5) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Paulo Andre Saraiva Dos Santos vs Rafael Tosetto -- ATP Challenger Costa do Sauipe Q3

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 22:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-02T22:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02SARTOS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Paulo Andre Saraiva Dos Santos (`KXATPCHALLENGERMATCH-26NOV02SARTOS-SAR`) | 0.68 / 0.70 (90) | 69.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rafael Tosetto (`KXATPCHALLENGERMATCH-26NOV02SARTOS-TOS`) | 0.30 / 0.32 (13) | 31.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Patricio Alvarado vs Alberto Odiseo Alvarado Berrospi -- M25 Guadalajara R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105419:208726:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Patricio Alvarado (`KXITFMATCH-26NOV02ALVALV2-ALV`) | 0.27 / 0.89 (45) | 58.0% | 38.2% | 38.4% | 44.4% [43.4%-46.4%] | -- | -- | -- | -- | PASS | -19.8 pp | HIGH_REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alberto Odiseo Alvarado Berrospi (`KXITFMATCH-26NOV02ALVALV2-ALV2`) | 0.17 / 0.79 (23) | 48.0% | 61.8% | 61.6% | 55.6% [53.6%-56.6%] | -- | -- | -- | -- | PASS | +13.8 pp | REVIEW | FRESH | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 867.0, B 570.0; serve-point win A 59.7%, B 38.0%; Elo A 1086.3, B 1107.9; model uncertainty 0.0152
* Form inputs: days since last match A 217, B 336; matches on record A 82, B 63; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.020, surface_dev_loose -0.010, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Clavel / Tchinda Kepche vs Nobel / St-Hilaire -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-02T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02CLATCHNOBSTH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clavel / Tchinda Kepche (`KXITFDOUBLES-26NOV02CLATCHNOBSTH-CLATCH`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Nobel / St-Hilaire (`KXITFDOUBLES-26NOV02CLATCHNOBSTH-NOBSTH`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Marcel Hornung vs Tarun Karra -- M25 Guadalajara R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206623:213598:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcel Hornung (`KXITFMATCH-26NOV02HORKAR-HOR`) | 0.25 / 0.39 (10) | 32.0% | 67.1% | 82.1% | 68.2% [67.2%-68.2%] | -- | -- | -- | -- | PASS | +35.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Tarun Karra (`KXITFMATCH-26NOV02HORKAR-KAR`) | 0.64 / 0.70 (183) | 67.0% | 32.9% | 17.9% | 31.9% [31.8%-32.8%] | -- | -- | -- | -- | PASS | -34.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 201.0; serve-point win A 59.5%, B 43.9%; Elo A 1258.4, B 1125.9; model uncertainty 0.0052
* Form inputs: days since last match A 1113, B 231; matches on record A 1, B 8; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV02HORKAR-HOR  (YES = Marcel Hornung)
Model: 67%
Kalshi: 32%
Gap: +35 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high -0.000, surface_dev_loose +0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Reid Jarvis vs Erick Manzano Navarro -- M25 Guadalajara R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-02T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02JARMAN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reid Jarvis (`KXITFMATCH-26NOV02JARMAN-JAR`) | 0.85 / 0.93 (58) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Erick Manzano Navarro (`KXITFMATCH-26NOV02JARMAN-MAN`) | 0.06 / 0.11 (6) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kliebhan / Michibata vs Massotte / Roussel -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-02T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02KLIMICMASROU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kliebhan / Michibata (`KXITFDOUBLES-26NOV02KLIMICMASROU-KLIMIC`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Massotte / Roussel (`KXITFDOUBLES-26NOV02KLIMICMASROU-MASROU`) | 0.06 / 0.90 (1) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Brandon Perez vs Jack McGary -- M25 Guadalajara R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207738:214117:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jack McGary (`KXITFMATCH-26NOV02PERMCG-MCG`) | 0.24 / 0.33 (4) | 28.5% | 66.6% | 77.3% | 72.1% [71.2%-73.1%] | -- | -- | -- | -- | PASS | +38.1 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Brandon Perez (`KXITFMATCH-26NOV02PERMCG-PER`) | 0.65 / 0.71 (5) | 68.0% | 33.4% | 22.7% | 27.9% [26.9%-28.8%] | -- | -- | -- | -- | PASS | -34.6 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1426.0, B 281.0; serve-point win A 62.3%, B 34.3%; Elo A 1018.4, B 1177.5; model uncertainty 0.0097
* Form inputs: days since last match A 182, B 189; matches on record A 100, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV02PERMCG-MCG  (YES = Jack McGary)
Model: 67%
Kalshi: 28%
Gap: +38 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.004, surface_dev_loose +0.001, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amanda Carolina Nava Elkin vs Giulia Alessia Monteleone -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222158:260604:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giulia Alessia Monteleone (`KXITFWMATCH-26NOV02NAVMON-MON`) | 0.03 / 0.11 (122) | 7.0% | 29.6% | 23.0% | 35.9% [30.5%-40.0%] | -- | -- | -- | -- | PASS | +22.6 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Amanda Carolina Nava Elkin (`KXITFWMATCH-26NOV02NAVMON-NAV`) | 0.87 / 0.93 (100) | 90.0% | 70.4% | 77.0% | 64.1% [60.1%-69.5%] | -- | -- | -- | -- | PASS | -19.6 pp | HIGH_REVIEW | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 845.0, B 643.0; serve-point win A 54.1%, B 49.9%; Elo A 1099.1, B 1042.9; model uncertainty 0.0473
* Form inputs: days since last match A 238, B 22; matches on record A 106, B 79; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV02NAVMON-MON  (YES = Giulia Alessia Monteleone)
Model: 30%
Kalshi: 7%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.020, surface_dev_loose +0.020, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Natalia Sousa Salazar vs Ashleigh Harvey -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:266455:269708:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashleigh Harvey (`KXITFWMATCH-26NOV02SOUHAR-HAR`) | 0.35 / 0.37 (39) | 36.0% | 39.4% | 74.0% | 53.2% [52.1%-54.3%] | -- | -- | -- | -- | PASS | +3.4 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Natalia Sousa Salazar (`KXITFWMATCH-26NOV02SOUHAR-SOU`) | 0.57 / 0.61 (7) | 59.0% | 60.6% | 26.0% | 46.8% [45.7%-47.9%] | -- | -- | -- | -- | PASS | +1.6 pp | NORMAL | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1161.0, B 67.0; serve-point win A 53.1%, B 48.9%; Elo A 1237.0, B 1252.0; model uncertainty 0.0107
* Form inputs: days since last match A 7, B 532; matches on record A 90, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Annabelle Xu vs Caterina Odorizzi -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-02 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-02T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222376:222613:2026-11-02`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caterina Odorizzi (`KXITFWMATCH-26NOV02XUXODO-ODO`) | 0.05 / 0.10 (27) | 7.5% | 17.2% | 8.6% | 17.7% [11.9%-26.0%] | -- | -- | -- | -- | PASS | +9.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Annabelle Xu (`KXITFWMATCH-26NOV02XUXODO-XUX`) | 0.88 / 0.93 (105) | 90.5% | 82.8% | 91.4% | 82.3% [74.0%-88.1%] | -- | -- | -- | -- | PASS | -7.7 pp | NORMAL | FRESH | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 722.0, B 1069.0; serve-point win A 55.6%, B 51.4%; Elo A 1347.8, B 1147.2; model uncertainty 0.0707
* Form inputs: days since last match A 96, B 189; matches on record A 43, B 126; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.010, surface_dev_loose +0.007, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maxwell Benson vs Lance Lage -- M25 Guadalajara R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02BENLAG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxwell Benson (`KXITFMATCH-26NOV02BENLAG-BEN`) | 0.24 / 0.35 (0) | 29.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lance Lage (`KXITFMATCH-26NOV02BENLAG-LAG`) | 0.64 / 0.71 (5) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ian Lucca Cervantes Tomas vs Tomas Quesada Perez -- M25 Guadalajara R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212486:214032:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ian Lucca Cervantes Tomas (`KXITFMATCH-26NOV02CERQUE-CER`) | 0.56 / 0.66 (5) | 61.0% | 46.1% | 27.4% | 39.7% [36.7%-40.8%] | -- | -- | -- | -- | PASS | -14.9 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tomas Quesada Perez (`KXITFMATCH-26NOV02CERQUE-QUE`) | 0.34 / 0.38 (40) | 36.0% | 53.9% | 72.6% | 60.3% [59.2%-63.3%] | -- | -- | -- | -- | PASS | +17.9 pp | HIGH_REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 529.0, B 183.0; serve-point win A 58.2%, B 41.0%; Elo A 1163.1, B 1229.7; model uncertainty 0.0205
* Form inputs: days since last match A 406, B 455; matches on record A 24, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV02CERQUE-QUE  (YES = Tomas Quesada Perez)
Model: 54%
Kalshi: 36%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Miles Clark vs Patricio Betancourt -- M25 Guadalajara R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212473:213666:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Patricio Betancourt (`KXITFMATCH-26NOV02CLABET-BET`) | 0.05 / 0.18 (31) | 11.5% | 51.4% | 40.3% | 52.1% [49.0%-54.1%] | -- | -- | -- | -- | PASS | +39.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Miles Clark (`KXITFMATCH-26NOV02CLABET-CLA`) | 0.76 / 0.91 (2) | 83.5% | 48.6% | 59.7% | 47.9% [45.9%-51.0%] | -- | -- | -- | -- | PASS | -34.9 pp | EXTREME (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 422.0, B 393.0; serve-point win A 59.3%, B 40.4%; Elo A 1169.9, B 1205.5; model uncertainty 0.0258
* Form inputs: days since last match A 350, B 189; matches on record A 13, B 9; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV02CLABET-BET  (YES = Patricio Betancourt)
Model: 51%
Kalshi: 12%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.010, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bynoe / Hammond vs Arseneault / Oscar Lien -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02BYNHAMARSOSC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arseneault / Oscar Lien (`KXITFDOUBLES-26NOV02BYNHAMARSOSC-ARSOSC`) | 0.60 / 0.84 (156) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bynoe / Hammond (`KXITFDOUBLES-26NOV02BYNHAMARSOSC-BYNHAM`) | 0.09 / 0.32 (2) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Carlos Alvarez Valdes / Flores vs Pacheco Mendez / Patino -- M25 Guadalajara R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02CARFLOPACPAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlos Alvarez Valdes / Flores (`KXITFDOUBLES-26NOV02CARFLOPACPAT-CARFLO`) | 0.20 / 0.45 (2) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pacheco Mendez / Patino (`KXITFDOUBLES-26NOV02CARFLOPACPAT-PACPAT`) | 0.46 / 0.73 (92) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Gales / Markov vs Fellows / Mesarovic -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02GALMARFELMES:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fellows / Mesarovic (`KXITFDOUBLES-26NOV02GALMARFELMES-FELMES`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gales / Markov (`KXITFDOUBLES-26NOV02GALMARFELMES-GALMAR`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Sofia Avataneo vs Kennedy Gibbs -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:242450:249680:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Avataneo (`KXITFWMATCH-26NOV02AVAGIB-AVA`) | 0.41 / 0.45 (5) | 43.0% | -- | 8.2% | 22.6% [22.6%-23.4%] | -- | -- | -- | -- | PASS | -20.4 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kennedy Gibbs (`KXITFWMATCH-26NOV02AVAGIB-GIB`) | 0.53 / 0.54 (4) | 53.5% | -- | 91.8% | 77.4% [76.6%-77.4%] | -- | -- | -- | -- | PASS | +23.9 pp | HIGH_REVIEW (DATA_WARNING) | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 821.0, B 0.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0041
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV02AVAGIB-GIB  (YES = Kennedy Gibbs)
Model: 77%
Kalshi: 54%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: FRESH
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.008, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luisa Hrda vs Maria Jose Portillo Ramirez -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215019:222358:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luisa Hrda (`KXITFWMATCH-26NOV02HRDPOR-HRD`) | 0.08 / 0.11 (76) | 9.5% | -- | 62.6% | 22.8% [18.2%-28.8%] | -- | -- | -- | -- | PASS | +13.3 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maria Jose Portillo Ramirez (`KXITFWMATCH-26NOV02HRDPOR-POR`) | 0.84 / 0.91 (100) | 87.5% | -- | 37.4% | 77.2% [71.2%-81.8%] | -- | -- | -- | -- | PASS | -10.3 pp | REVIEW | FRESH | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 916.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0528
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.045, surface_pool_high +0.060, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Carlo Arena Fava vs Roberto Herman -- M25 Guadalajara R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02AREHER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlo Arena Fava (`KXITFMATCH-26NOV02AREHER-ARE`) | 0.90 / 0.94 (38) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Roberto Herman (`KXITFMATCH-26NOV02AREHER-HER`) | 0.06 / 0.07 (152) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Brostrom Poulsen / Slavic vs Benchetrit / Qin -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02BROSLABENQIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benchetrit / Qin (`KXITFDOUBLES-26NOV02BROSLABENQIN-BENQIN`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Brostrom Poulsen / Slavic (`KXITFDOUBLES-26NOV02BROSLABENQIN-BROSLA`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alvarado / Hornung vs Cooper / McKennon -- M25 Guadalajara R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02ALVHORCOOMCK:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alvarado / Hornung (`KXITFDOUBLES-26NOV02ALVHORCOOMCK-ALVHOR`) | 0.07 / 0.40 (2) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cooper / McKennon (`KXITFDOUBLES-26NOV02ALVHORCOOMCK-COOMCK`) | 0.50 / 0.78 (113) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jarvis / Matta vs Jauregui Sainz de Rozas / Tunas -- M25 Guadalajara R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02JARMATJAUTUN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jarvis / Matta (`KXITFDOUBLES-26NOV02JARMATJAUTUN-JARMAT`) | 0.39 / 0.68 (78) | 53.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jauregui Sainz de Rozas / Tunas (`KXITFDOUBLES-26NOV02JARMATJAUTUN-JAUTUN`) | 0.25 / 0.52 (2) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Avi Shugar vs Mathias Roy -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 04:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T04:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02SHUROY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mathias Roy (`KXITFMATCH-26NOV02SHUROY-ROY`) | 0.18 / 0.31 (37) | 24.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Avi Shugar (`KXITFMATCH-26NOV02SHUROY-SHU`) | 0.62 / 0.77 (39) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Angel Escandon Fong / Jose Morales Gutierrez vs De Alba / Sau Franco -- M25 Guadalajara R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 04:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T04:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02ANGJOSDEASAU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Angel Escandon Fong / Jose Morales Gutierrez (`KXITFDOUBLES-26NOV02ANGJOSDEASAU-ANGJOS`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| De Alba / Sau Franco (`KXITFDOUBLES-26NOV02ANGJOSDEASAU-DEASAU`) | 0.06 / 0.89 (2) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Betancourt / Echazu vs Rengifo / Esteban Rico Arias -- M25 Guadalajara R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 04:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T04:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02BETECHRENEST:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Betancourt / Echazu (`KXITFDOUBLES-26NOV02BETECHRENEST-BETECH`) | 0.23 / 0.51 (2) | 37.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rengifo / Esteban Rico Arias (`KXITFDOUBLES-26NOV02BETECHRENEST-RENEST`) | 0.40 / 0.70 (83) | 55.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Claverie / Covato vs Lucca Cervantes Tomas / Alejandro Reyes Tirado -- M25 Guadalajara R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 04:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T04:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02CLACOVLUCALE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Claverie / Covato (`KXITFDOUBLES-26NOV02CLACOVLUCALE-CLACOV`) | 0.59 / 0.87 (192) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lucca Cervantes Tomas / Alejandro Reyes Tirado (`KXITFDOUBLES-26NOV02CLACOVLUCALE-LUCALE`) | 0.06 / 0.32 (2) | 19.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Fuchs / Perez vs Lage / Martinez Miranda -- M25 Guadalajara R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 04:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T04:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV02FUCPERLAGMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fuchs / Perez (`KXITFDOUBLES-26NOV02FUCPERLAGMAR-FUCPER`) | 0.84 / 0.90 (1) | 87.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lage / Martinez Miranda (`KXITFDOUBLES-26NOV02FUCPERLAGMAR-LAGMAR`) | 0.04 / 0.09 (27) | 6.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ya-Hsin Lee / Fang-Hsien Wu vs Venus Williams / Yifan Xu -- WTA Hong Kong R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-02 06:59Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-03T05:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-03T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03LEEFANWILYIF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ya-Hsin Lee / Fang-Hsien Wu (`KXWTADOUBLES-26NOV03LEEFANWILYIF-LEEFAN`) | 0.05 / 0.93 (2) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Venus Williams / Yifan Xu (`KXWTADOUBLES-26NOV03LEEFANWILYIF-WILYIF`) | 0.05 / 0.93 (2) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | FRESH | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
