# ASSISTED SLATE -- 2026-11-03T16:47Z (`SL-20261103T164735Z-726b0ecc`)

**AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. CHATGPT_ASSISTED_TRACK = ACTIVE.** This is a handicapping packet: it selects nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; re-check the live book before deciding.

321 open matches not seen started, 835 markets. Skipped: {"scheduled_start_over_24h_past": 21, "first_ball_already_observed": 5}. Sources: shadow board 2026-11-03T16:28:06.784113+00:00, Model 4 2026-11-03T16:29:31.971973+00:00, Gen-1 ledger 2026-11-03T16:28:02.036440+00:00, external 2026-11-03T15:52:58.593006+00:00, capture 20261103T155032Z.quotes.jsonl.gz.

## NEXT ACTIONABLE MAIN-TOUR WINDOW

* Earliest credible first ball: **2026-11-03 19:30Z**
* Recommended RUN TENNIS time: **2026-11-03 18:45Z**
* Final price/status check time: **2026-11-03 19:20Z**
* Number of matches in window: 1 (Casper Ruud vs Rafael Jodar)

* **11 main-tour match(es) have NO verified start status** (START_UNKNOWN, STATUS_AMBIGUOUS): BET blocked until a live status check.

Slate built 2026-11-03T16:47Z. Refresh due by: 2026-11-03 18:45Z. A slate built before a window's recommended time, or before a match's status changed, is NOT authoritative for that window.

**Discrepancy sanity layer** (`discrepancy_sanity_v1`): the model should usually sit close to the market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities are unchanged by this layer.

Bands (all priced contracts): {"EXTREME": 85, "HIGH_REVIEW": 87, "NORMAL": 341, "REVIEW": 72, "UNPRICED": 250}; match winners: {"EXTREME": 70, "HIGH_REVIEW": 62, "NORMAL": 224, "REVIEW": 52, "UNPRICED": 234}; quote freshness at build: {"AGING": 585}.

## Ignacio Buse vs Daniil Medvedev -- ATP Paris R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-03 13:00Z
* Current expected start: 2026-11-03 13:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-03 12:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-04T05:00:00+00:00 as not a valid time; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (MASTERS_1000) · Hard · scheduled 2026-11-03T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:106421:209860:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ignacio Buse (`KXATPMATCH-26NOV03BUSMED-BUS`) | 0.14 / 0.16 (114968) | 15.0% | 15.9% | 11.9% | 11.9% [11.2%-13.3%] | -- | -- | -- | -- | PASS | +0.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniil Medvedev (`KXATPMATCH-26NOV03BUSMED-MED`) | 0.85 / 0.86 (89481) | 85.5% | 84.1% | 88.0% | 88.0% [86.7%-88.8%] | -- | -- | -- | -- | WATCH | -1.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5542.0, B 6507.0; serve-point win A 57.1%, B 35.1%; Elo A 1763.6, B 2105.6; model uncertainty 0.0104
* Form inputs: days since last match A 1, B 3; matches on record A 288, B 879; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.008
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV03BUSMED-16` Over 15.5 games: 0.42/0.98 mid 70.0%, model 95.8% (projection_v2.0 (prediction ledger)) -- gap +25.8 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV03BUSMED-MED3` Will Daniil Medvedev win at least 2.5 more games than Ignacio Buse?: 0.27/0.84 mid 55.5%, model 73.7% (projection_v2.0 (prediction ledger)) -- gap +18.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV03BUSMED-MED20` Will Daniil Medvedev win the Ignacio Buse vs Daniil Medvedev match by a set score of 2-0?: 0.63/0.69 mid 66.0%, model 55.8% (projection_v2.0 (prediction ledger)) -- gap -10.2 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV03BUSMED-21` Over 20.5 games: 0.48/0.51 mid 49.5%, model 57.8% (projection_v2.0 (prediction ledger)) -- gap +8.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV03BUSMED-26` Over 25.5 games: 0.28/0.58 mid 43.0%, model 35.0% (projection_v2.0 (prediction ledger)) -- gap -8.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV03BUSMED-MED6` Will Daniil Medvedev win at least 5.5 more games than Ignacio Buse?: 0.40/0.42 mid 41.0%, model 33.8% (projection_v2.0 (prediction ledger)) -- gap -7.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV03BUSMED-2-MED` Will Daniil Medvedev win set 2 in the Ignacio Buse vs Daniil Medvedev match: 0.57/0.81 mid 69.0%, model 74.7% (projection_v2.0 (prediction ledger)) -- gap +5.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV03BUSMED-1-BUS` Will Ignacio Buse win set 1 in the Ignacio Buse vs Daniil Medvedev match: 0.21/0.23 mid 22.0%, model 25.3% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV03BUSMED-1-MED` Will Daniil Medvedev win set 1 in the Ignacio Buse vs Daniil Medvedev match: 0.77/0.79 mid 78.0%, model 74.7% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV03BUSMED-2-BUS` Will Ignacio Buse win set 2 in the Ignacio Buse vs Daniil Medvedev match: 0.19/0.36 mid 27.5%, model 25.3% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alexander Zverev vs Lorenzo Musetti -- ATP Paris R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-03 13:00Z
* Current expected start: 2026-11-03 13:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-03 12:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-04T05:00:00+00:00 as not a valid time; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (MASTERS_1000) · Hard · scheduled 2026-11-03T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:100644:207518:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Musetti (`KXATPMATCH-26NOV03ZVEMUS-MUS`) | 0.31 / 0.32 (1830) | 31.5% | 32.7% | 29.1% | 28.2% [27.4%-29.1%] | -- | -- | -- | -- | PASS | +1.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexander Zverev (`KXATPMATCH-26NOV03ZVEMUS-ZVE`) | 0.68 / 0.69 (1862) | 68.5% | 67.3% | 70.9% | 71.8% [70.9%-72.6%] | -- | -- | -- | -- | PASS | -1.2 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 8106.0, B 5227.0; serve-point win A 69.5%, B 34.2%; Elo A 2142.2, B 1959.7; model uncertainty 0.0081
* Form inputs: days since last match A 3, B 1; matches on record A 940, B 491; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose -0.001, surface_dev_tight +0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV03ZVEMUS-18` Over 17.5 games: 0.51/0.92 mid 71.5%, model 95.7% (projection_v2.0 (prediction ledger)) -- gap +24.2 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV03ZVEMUS-2-ZVE` Will Alexander Zverev win set 2 in the Alexander Zverev vs Lorenzo Musetti match: 0.05/0.77 mid 41.0%, model 61.8% (projection_v2.0 (prediction ledger)) -- gap +20.8 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV03ZVEMUS-MUS2` Will Lorenzo Musetti win at least 1.5 more games than Alexander Zverev?: 0.03/0.77 mid 40.0%, model 25.4% (projection_v2.0 (prediction ledger)) -- gap -14.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV03ZVEMUS-23` Over 22.5 games: 0.51/0.53 mid 52.0%, model 63.3% (projection_v2.0 (prediction ledger)) -- gap +11.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV03ZVEMUS-MUS21` Will Lorenzo Musetti win the Alexander Zverev vs Lorenzo Musetti match by a set score of 2-1?: 0.13/0.43 mid 28.0%, model 18.1% (projection_v2.0 (prediction ledger)) -- gap -9.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV03ZVEMUS-ZVE20` Will Alexander Zverev win the Alexander Zverev vs Lorenzo Musetti match by a set score of 2-0?: 0.44/0.51 mid 47.5%, model 38.2% (projection_v2.0 (prediction ledger)) -- gap -9.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV03ZVEMUS-ZVE4` Will Alexander Zverev win at least 3.5 more games than Lorenzo Musetti?: 0.43/0.45 mid 44.0%, model 35.8% (projection_v2.0 (prediction ledger)) -- gap -8.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV03ZVEMUS-2-MUS` Will Lorenzo Musetti win set 2 in the Alexander Zverev vs Lorenzo Musetti match: 0.15/0.77 mid 46.0%, model 38.2% (projection_v2.0 (prediction ledger)) -- gap -7.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV03ZVEMUS-1-MUS` Will Lorenzo Musetti win set 1 in the Alexander Zverev vs Lorenzo Musetti match: 0.34/0.37 mid 35.5%, model 38.2% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV03ZVEMUS-1-ZVE` Will Alexander Zverev win set 1 in the Alexander Zverev vs Lorenzo Musetti match: 0.63/0.66 mid 64.5%, model 61.8% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV03ZVEMUS-28` Over 27.5 games: 0.29/0.57 mid 43.0%, model 42.2% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Francisco Cerundolo / Tomas Martin Etcheverry vs Christian Harrison / Neal Skupski -- ATP Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-04T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-03T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03CERETCHARSKU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francisco Cerundolo / Tomas Martin Etcheverry (`KXATPDOUBLES-26NOV03CERETCHARSKU-CERETC`) | 0.21 / 0.26 (2531) | 23.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Christian Harrison / Neal Skupski (`KXATPDOUBLES-26NOV03CERETCHARSKU-HARSKU`) | 0.72 / 0.73 (1) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Daniel Elahi Galan vs Gonzalo Bueno -- ATP Challenger Costa do Sauipe R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:123755:208293:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gonzalo Bueno (`KXATPCHALLENGERMATCH-26NOV03GALBUE-BUE`) | 0.42 / 0.43 (37) | 42.5% | -- | 46.9% | 47.9% [45.9%-49.5%] | 43.7% | 45.1% | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +5.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daniel Elahi Galan (`KXATPCHALLENGERMATCH-26NOV03GALBUE-GAL`) | 0.56 / 0.58 (9670) | 57.0% | -- | 53.1% | 52.1% [50.5%-54.1%] | 56.3% | 54.7% | -- | INSUFFICIENT_INPUTS | PASS | -4.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5067.0, B 4809.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0181
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.016, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Marcel Granollers / Horacio Zeballos vs Quentin Halys / Pierre-Hugues Herbert -- ATP Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-04T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-03T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03GRAZEBHALHER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcel Granollers / Horacio Zeballos (`KXATPDOUBLES-26NOV03GRAZEBHALHER-GRAZEB`) | 0.57 / 0.59 (60) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Quentin Halys / Pierre-Hugues Herbert (`KXATPDOUBLES-26NOV03GRAZEBHALHER-HALHER`) | 0.39 / 0.44 (2306) | 41.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Orlando Luz / Rafael Matos vs Mariano Navone / Alejandro Tabilo -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-04T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-03T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03LUZMATNAVTAB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Orlando Luz / Rafael Matos (`KXATPDOUBLES-26NOV03LUZMATNAVTAB-LUZMAT`) | 0.62 / 0.72 (45) | 67.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mariano Navone / Alejandro Tabilo (`KXATPDOUBLES-26NOV03LUZMATNAVTAB-NAVTAB`) | 0.25 / 0.32 (4) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Alex Michelsen / Learner Tien vs Kevin Krawietz / Tim Putz -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-03T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03MICTIEKRAPUT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kevin Krawietz / Tim Putz (`KXATPDOUBLES-26NOV03MICTIEKRAPUT-KRAPUT`) | 0.45 / 0.74 (2) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alex Michelsen / Learner Tien (`KXATPDOUBLES-26NOV03MICTIEKRAPUT-MICTIE`) | 0.29 / 0.50 (5) | 39.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Luis Felipe Miguel vs Igor Marcondes -- ATP Challenger Costa do Sauipe R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-03T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03MIGMAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Igor Marcondes (`KXATPCHALLENGERMATCH-26NOV03MIGMAR-MAR`) | 0.67 / 0.68 (0) | 67.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luis Felipe Miguel (`KXATPCHALLENGERMATCH-26NOV03MIGMAR-MIG`) | 0.31 / 0.32 (15) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Filip Misolic vs Juan Pablo Varillas -- ATP Challenger Costa do Sauipe R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122669:209209:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Misolic (`KXATPCHALLENGERMATCH-26NOV03MISVAR-MIS`) | 0.59 / 0.60 (511) | 59.5% | -- | 49.5% | 55.6% [53.1%-58.7%] | 59.9% | 61.0% | 61.0% | MODEL_LONE_OUTLIER | PASS | -3.9 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Juan Pablo Varillas (`KXATPCHALLENGERMATCH-26NOV03MISVAR-VAR`) | 0.40 / 0.41 (7281) | 40.5% | -- | 50.5% | 44.4% [41.3%-46.9%] | 40.1% | 39.7% | 39.7% | MODEL_LONE_OUTLIER | WATCH | +3.9 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3412.0, B 5073.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0279
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.005, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Joao Lucas Reis Da Silva vs Santiago Rodriguez Taverna -- ATP Challenger Costa do Sauipe R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-03T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03REIROD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Lucas Reis Da Silva (`KXATPCHALLENGERMATCH-26NOV03REIROD-REI`) | 0.68 / 0.69 (6212) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Santiago Rodriguez Taverna (`KXATPCHALLENGERMATCH-26NOV03REIROD-ROD`) | 0.31 / 0.32 (5) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Rafael Tosetto vs Franco Roncadelli -- ATP Challenger Costa do Sauipe R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208006:208364:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Franco Roncadelli (`KXATPCHALLENGERMATCH-26NOV03TOSRON-RON`) | 0.86 / 0.87 (5015) | 86.5% | -- | 91.6% | 90.6% [88.4%-92.3%] | 84.4% | 86.1% | 84.4% | MARKETS_AGREE | SHADOW_BET | +4.1 pp | NORMAL | AGING | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Rafael Tosetto (`KXATPCHALLENGERMATCH-26NOV03TOSRON-TOS`) | 0.13 / 0.14 (440) | 13.5% | -- | 8.4% | 9.4% [7.7%-11.6%] | 15.6% | 13.3% | 15.6% | EXTERNAL_LONE_OUTLIER | PASS | -4.1 pp | NORMAL | AGING | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 1630.0, B 4155.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0195
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.004, surface_dev_loose -0.006, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; NOMINAL_START_IS_DAY_PLACEHOLDER

## Sumit Nagal vs Georgii Kravchenko -- ATP Challenger Taranto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 14:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-03T14:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111576:206662:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Georgii Kravchenko (`KXATPCHALLENGERMATCH-26NOV03NAGKRA-KRA`) | 0.46 / 0.47 (10400) | 46.5% | -- | 49.0% | 40.8% [35.4%-44.3%] | -- | 49.3% | 49.3% | MODEL_LONE_OUTLIER | PASS | -5.7 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Sumit Nagal (`KXATPCHALLENGERMATCH-26NOV03NAGKRA-NAG`) | 0.53 / 0.54 (1797) | 53.5% | -- | 51.0% | 59.2% [55.7%-64.6%] | -- | 50.8% | 50.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +5.7 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4831.0, B 3083.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0448
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

## Francesco Maestrelli vs Francesco Forti -- ATP Challenger Taranto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-03T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208353:209506:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Francesco Forti (`KXATPCHALLENGERMATCH-26NOV03MAEFOR-FOR`) | 0.15 / 0.16 (18095) | 15.5% | -- | 53.0% | 47.5% [44.0%-50.5%] | 37.5% | 37.4% | 37.4% | MODEL_LONE_OUTLIER | SHADOW_BET | +32.0 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |
| Francesco Maestrelli (`KXATPCHALLENGERMATCH-26NOV03MAEFOR-MAE`) | 0.84 / 0.85 (838) | 84.5% | -- | 47.0% | 52.5% [49.5%-56.0%] | 62.5% | 62.7% | 62.6% | MODEL_LONE_OUTLIER | PASS | -32.0 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | SUPPORTS_MODEL_DIRECTION | VERIFIED |

* Serve evidence (points): A 5128.0, B 3864.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0324
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV03MAEFOR-FOR  (YES = Francesco Forti)
Model: 48%
Kalshi: 16%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: SUPPORTS_MODEL_DIRECTION
Data quality: A (ADEQUATE)
Reasons: EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

## Matteo Martineau vs Inaki Montes-de la Torre -- ATP Challenger Taranto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-03T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200188:208540:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Martineau (`KXATPCHALLENGERMATCH-26NOV03MARMON-MAR`) | 0.38 / 0.40 (3995) | 39.0% | -- | 30.0% | 32.7% [30.5%-36.0%] | 38.4% | 37.6% | 38.0% | MODEL_LONE_OUTLIER | PASS | -6.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Inaki Montes-de la Torre (`KXATPCHALLENGERMATCH-26NOV03MARMON-MON`) | 0.60 / 0.62 (4308) | 61.0% | -- | 70.0% | 67.3% [64.0%-69.5%] | 61.6% | 62.3% | 62.0% | MODEL_LONE_OUTLIER | WATCH | +6.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5600.0, B 4035.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0279
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

## Maxim Mrva vs Michele Ribecai -- ATP Challenger Taranto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 15:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-03T15:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211617:212020:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxim Mrva (`KXATPCHALLENGERMATCH-26NOV03MRVRIB-MRV`) | 0.60 / 0.61 (8589) | 60.5% | -- | 34.5% | 41.6% [38.0%-48.4%] | 58.4% | 58.9% | 58.6% | MODEL_LONE_OUTLIER | PASS | -18.9 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Michele Ribecai (`KXATPCHALLENGERMATCH-26NOV03MRVRIB-RIB`) | 0.40 / 0.41 (6922) | 40.5% | -- | 65.5% | 58.4% [51.6%-62.0%] | 41.6% | 41.3% | 41.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +17.9 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4552.0, B 4673.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0522
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV03MRVRIB-RIB  (YES = Michele Ribecai)
Model: 58%
Kalshi: 40%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED

## Ben Shelton vs Cameron Norrie -- ATP Paris R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-03 21:00Z
* Current expected start: 2026-11-03 15:53Z
* Source: COURT_PROGRESSION: preceding match on Court Central finished; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-03 15:08Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-307_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (MASTERS_1000) · Hard · scheduled 2026-11-03T21:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111815:210097:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cameron Norrie (`KXATPMATCH-26NOV03SHENOR-NOR`) | 0.28 / 0.29 (120603) | 28.5% | 31.2% | 31.2% | 29.9% [29.1%-31.6%] | 29.4% | 29.0% | 29.2% | MODEL_LONE_OUTLIER | PASS | +2.7 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Ben Shelton (`KXATPMATCH-26NOV03SHENOR-SHE`) | 0.71 / 0.72 (134) | 71.5% | 68.8% | 68.8% | 70.0% [68.5%-70.9%] | 70.6% | 71.0% | 70.8% | MODEL_LONE_OUTLIER | PASS | -2.7 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 6486.0, B 5450.0; serve-point win A 69.9%, B 34.2%; Elo A 2066.0, B 1893.2; model uncertainty 0.0121
* Form inputs: days since last match A 5, B 1; matches on record A 317, B 680; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.013, surface_pool_high +0.008, surface_dev_loose +0.004, surface_dev_tight -0.012
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV03SHENOR-SHE20` Will Ben Shelton win the Ben Shelton vs Cameron Norrie match by a set score of 2-0?: 0.46/0.48 mid 47.0%, model 39.4% (projection_v2.0 (prediction ledger)) -- gap -7.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV03SHENOR-SHE7` Will Ben Shelton win at least 6.5 more games than Cameron Norrie?: 0.06/0.15 mid 10.5%, model 4.6% (projection_v2.0 (prediction ledger)) -- gap -5.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV03SHENOR-SHE21` Will Ben Shelton win the Ben Shelton vs Cameron Norrie match by a set score of 2-1?: 0.22/0.25 mid 23.5%, model 29.3% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV03SHENOR-25` Over 24.5 games: 0.47/0.49 mid 48.0%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV03SHENOR-NOR21` Will Cameron Norrie win the Ben Shelton vs Cameron Norrie match by a set score of 2-1?: 0.11/0.15 mid 13.0%, model 17.4% (projection_v2.0 (prediction ledger)) -- gap +4.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV03SHENOR-SHE4` Will Ben Shelton win at least 3.5 more games than Cameron Norrie?: 0.40/0.42 mid 41.0%, model 36.7% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV03SHENOR-20` Over 19.5 games: 0.79/0.82 mid 80.5%, model 84.6% (projection_v2.0 (prediction ledger)) -- gap +4.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV03SHENOR-2-NOR` Will Cameron Norrie win set 2 in the Ben Shelton vs Cameron Norrie match: 0.33/0.34 mid 33.5%, model 37.2% (projection_v2.0 (prediction ledger)) -- gap +3.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV03SHENOR-2-SHE` Will Ben Shelton win set 2 in the Ben Shelton vs Cameron Norrie match: 0.66/0.67 mid 66.5%, model 62.8% (projection_v2.0 (prediction ledger)) -- gap -3.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV03SHENOR-30` Over 29.5 games: 0.30/0.33 mid 31.5%, model 34.9% (projection_v2.0 (prediction ledger)) -- gap +3.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV03SHENOR-NOR2` Will Cameron Norrie win at least 1.5 more games than Ben Shelton?: 0.18/0.26 mid 22.0%, model 24.0% (projection_v2.0 (prediction ledger)) -- gap +2.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV03SHENOR-1-NOR` Will Cameron Norrie win set 1 in the Ben Shelton vs Cameron Norrie match: 0.35/0.36 mid 35.5%, model 37.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV03SHENOR-1-SHE` Will Ben Shelton win set 1 in the Ben Shelton vs Cameron Norrie match: 0.64/0.65 mid 64.5%, model 62.8% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV03SHENOR-NOR20` Will Cameron Norrie win the Ben Shelton vs Cameron Norrie match by a set score of 2-0?: 0.13/0.16 mid 14.5%, model 13.8% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Anna Blinkova vs Farah Heddar -- WTA 125K Luanda R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-03 18:30Z
* Current expected start: 2026-11-03 15:55Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-03 15:10Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · Hard · scheduled 2026-11-03T18:30:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215020:267380:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna Blinkova (`KXWTACHALLENGERMATCH-26NOV03BLIHED-BLI`) | 0.98 / 0.99 (31005) | 98.5% | 99.7% | 96.9% | 98.2% [97.8%-98.6%] | -- | 95.0% | -- | INSUFFICIENT_INPUTS | PASS | +1.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Farah Heddar (`KXWTACHALLENGERMATCH-26NOV03BLIHED-HED`) | 0.02 / 0.03 (5814) | 2.5% | 0.3% | 3.1% | 1.8% [1.4%-2.2%] | -- | 14.8% | 14.8% | EXTERNAL_LONE_OUTLIER | PASS | -2.2 pp | NORMAL | AGING | D / POOR | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 4417.0, B 379.0; serve-point win A 64.1%, B 56.4%; Elo A 1826.1, B 1100.7; model uncertainty 0.0044
* Form inputs: days since last match A 3, B 204; matches on record A 636, B 14; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.005, surface_dev_loose +0.002, surface_dev_tight -0.001
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; STATUS_AMBIGUOUS

## Benjamin Bonzi vs Taylor Fritz -- ATP Paris R64

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-03 13:00Z
* Current expected start: 2026-11-03 16:00Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-03 15:15Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_+180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

ATP (MASTERS_1000) · Hard · scheduled 2026-11-03T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126127:126203:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Benjamin Bonzi (`KXATPMATCH-26NOV03BONFRI-BON`) | 0.20 / 0.21 (7967) | 20.5% | 21.6% | 19.4% | 20.1% [19.4%-21.0%] | 22.5% | 21.5% | 22.0% | MARKETS_AGREE | PASS | +1.1 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Taylor Fritz (`KXATPMATCH-26NOV03BONFRI-FRI`) | 0.79 / 0.80 (9657) | 79.5% | 78.4% | 80.6% | 79.9% [79.0%-80.6%] | 77.5% | 77.8% | 77.6% | MARKETS_AGREE | PASS | -1.1 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5634.0, B 6763.0; serve-point win A 64.4%, B 29.0%; Elo A 1836.3, B 2053.7; model uncertainty 0.0081
* Form inputs: days since last match A 2, B 3; matches on record A 802, B 768; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.004, surface_dev_loose +0.000, surface_dev_tight -0.000
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV03BONFRI-FRI21` Will Taylor Fritz win the Benjamin Bonzi vs Taylor Fritz match by a set score of 2-1?: 0.23/0.25 mid 24.0%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV03BONFRI-FRI20` Will Taylor Fritz win the Benjamin Bonzi vs Taylor Fritz match by a set score of 2-0?: 0.53/0.54 mid 53.5%, model 48.9% (projection_v2.0 (prediction ledger)) -- gap -4.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV03BONFRI-25` Over 24.5 games: 0.44/0.45 mid 44.5%, model 48.4% (projection_v2.0 (prediction ledger)) -- gap +3.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV03BONFRI-30` Over 29.5 games: 0.33/0.34 mid 33.5%, model 30.5% (projection_v2.0 (prediction ledger)) -- gap -3.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV03BONFRI-BON21` Will Benjamin Bonzi win the Benjamin Bonzi vs Taylor Fritz match by a set score of 2-1?: 0.09/0.11 mid 10.0%, model 12.6% (projection_v2.0 (prediction ledger)) -- gap +2.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV03BONFRI-2-BON` Will Benjamin Bonzi win set 2 in the Benjamin Bonzi vs Taylor Fritz match: 0.27/0.28 mid 27.5%, model 30.0% (projection_v2.0 (prediction ledger)) -- gap +2.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV03BONFRI-2-FRI` Will Taylor Fritz win set 2 in the Benjamin Bonzi vs Taylor Fritz match: 0.72/0.73 mid 72.5%, model 70.0% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV03BONFRI-BON20` Will Benjamin Bonzi win the Benjamin Bonzi vs Taylor Fritz match by a set score of 2-0?: 0.11/0.12 mid 11.5%, model 9.0% (projection_v2.0 (prediction ledger)) -- gap -2.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV03BONFRI-1-BON` Will Benjamin Bonzi win set 1 in the Benjamin Bonzi vs Taylor Fritz match: 0.28/0.29 mid 28.5%, model 30.0% (projection_v2.0 (prediction ledger)) -- gap +1.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV03BONFRI-BON2` Will Benjamin Bonzi win at least 1.5 more games than Taylor Fritz?: 0.16/0.18 mid 17.0%, model 15.9% (projection_v2.0 (prediction ledger)) -- gap -1.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV03BONFRI-20` Over 19.5 games: 0.77/0.82 mid 79.5%, model 80.5% (projection_v2.0 (prediction ledger)) -- gap +1.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV03BONFRI-FRI7` Will Taylor Fritz win at least 6.5 more games than Benjamin Bonzi?: 0.03/0.13 mid 8.0%, model 7.3% (projection_v2.0 (prediction ledger)) -- gap -0.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV03BONFRI-1-FRI` Will Taylor Fritz win set 1 in the Benjamin Bonzi vs Taylor Fritz match: 0.70/0.71 mid 70.5%, model 70.0% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV03BONFRI-FRI4` Will Taylor Fritz win at least 3.5 more games than Benjamin Bonzi?: 0.46/0.47 mid 46.5%, model 47.0% (projection_v2.0 (prediction ledger)) -- gap +0.5 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; SCHEDULED_START_PASSED; STATUS_AMBIGUOUS; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Elvina Kalieva vs Irene Burillo Escorihuela -- WTA 125K Cali R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-03 19:00Z
* Current expected start: 2026-11-03 16:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-03 15:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · Clay · scheduled 2026-11-03T19:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:213706:220722:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Irene Burillo Escorihuela (`KXWTACHALLENGERMATCH-26NOV03KALBUR-BUR`) | 0.39 / 0.40 (18974) | 39.5% | 41.7% | 46.8% | 47.3% [45.2%-48.4%] | 48.0% | 48.1% | 48.0% | MODEL_LONE_OUTLIER | PASS | +2.2 pp | NORMAL | AGING | A / LIMITED | EXTERNAL_OUTLIER | VERIFIED |
| Elvina Kalieva (`KXWTACHALLENGERMATCH-26NOV03KALBUR-KAL`) | 0.60 / 0.61 (15789) | 60.5% | 58.3% | 53.2% | 52.7% [51.6%-54.8%] | 52.0% | 51.8% | 51.9% | MODEL_LONE_OUTLIER | PASS | -2.2 pp | NORMAL | AGING | A / LIMITED | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 3992.0, B 3586.0; serve-point win A 52.6%, B 49.0%; Elo A 1681.0, B 1666.3; model uncertainty 0.016
* Form inputs: days since last match A 24, B 20; matches on record A 365, B 648; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS

## Jazmin Ortenzi vs Elizabeth Mandlik -- WTA 125K Cali R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-03 19:00Z
* Current expected start: 2026-11-03 16:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-03 15:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · Clay · scheduled 2026-11-03T19:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:216097:220446:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elizabeth Mandlik (`KXWTACHALLENGERMATCH-26NOV03ORTMAN-MAN`) | 0.51 / 0.52 (1495) | 51.5% | 44.6% | 32.9% | 35.9% [31.9%-46.8%] | 42.8% | 42.6% | 42.7% | MODEL_LONE_OUTLIER | PASS | -6.9 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Jazmin Ortenzi (`KXWTACHALLENGERMATCH-26NOV03ORTMAN-ORT`) | 0.48 / 0.49 (35690) | 48.5% | 55.4% | 67.1% | 64.1% [53.2%-68.1%] | 57.2% | 57.5% | 57.4% | MODEL_LONE_OUTLIER | WATCH | +6.9 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 3121.0, B 3798.0; serve-point win A 52.4%, B 48.5%; Elo A 1676.8, B 1610.9; model uncertainty 0.0744
* Form inputs: days since last match A 4, B 2; matches on record A 368, B 371; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.030, surface_pool_high +0.034, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS

## Katrina Scott vs Renata Zarazua -- WTA 125K Cali R32

**START STATUS: STATUS_AMBIGUOUS** -- BET BLOCKED
* Nominal schedule: 2026-11-03 19:00Z
* Current expected start: 2026-11-03 16:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-03 15:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN

WTA125 (WTA_125) · Clay · scheduled 2026-11-03T19:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:213887:221512:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katrina Scott (`KXWTACHALLENGERMATCH-26NOV03SCOZAR-SCO`) | 0.06 / 0.07 (6134) | 6.5% | 20.1% | 37.4% | 30.5% [24.8%-32.9%] | 20.8% | 19.8% | 20.3% | MODEL_LONE_OUTLIER | SHADOW_BET | +13.6 pp | REVIEW | AGING | A / LIMITED | AGREES_WITH_MODEL | VERIFIED |
| Renata Zarazua (`KXWTACHALLENGERMATCH-26NOV03SCOZAR-ZAR`) | 0.92 / 0.93 (20) | 92.5% | 79.9% | 62.6% | 69.5% [67.1%-75.2%] | 79.2% | 80.7% | 80.0% | MODEL_LONE_OUTLIER | PASS | -12.6 pp | REVIEW | AGING | A / LIMITED | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 2201.0, B 4923.0; serve-point win A 50.0%, B 43.7%; Elo A 1570.1, B 1793.9; model uncertainty 0.0408
* Form inputs: days since last match A 7, B 24; matches on record A 251, B 698; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight +0.000
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; STATUS_AMBIGUOUS

## Laslo Djere vs Edas Butvilas -- ATP Challenger Bratislava II R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 16:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T16:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111513:210220:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edas Butvilas (`KXATPCHALLENGERMATCH-26NOV03DJEBUT-BUT`) | 0.35 / 0.37 (1) | 36.0% | -- | 28.4% | 23.9% [21.2%-25.9%] | 35.4% | -- | 35.4% | MODEL_LONE_OUTLIER | SHADOW_BET | -12.1 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Laslo Djere (`KXATPCHALLENGERMATCH-26NOV03DJEBUT-DJE`) | 0.61 / 0.64 (193) | 62.5% | -- | 71.6% | 76.1% [74.1%-78.8%] | 64.6% | -- | 64.6% | MODEL_LONE_OUTLIER | PASS | +13.6 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4372.0, B 4862.0; serve-point win A --, B --; Elo A None, B None; model uncertainty 0.0234
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.019, surface_dev_loose +0.019, surface_dev_tight -0.020
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; THIN_DISPLAYED_SIZE

## Andrej Martin / Lukas Pokorny vs Inigo Cervantes / Benjamin Winter Lopez -- ATP Challenger Bratislava II R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-03T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03MARPOKCERWIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Inigo Cervantes / Benjamin Winter Lopez (`KXATPCHALLENGERDOUBLES-26NOV03MARPOKCERWIN-CERWIN`) | 0.37 / 0.45 (30) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Andrej Martin / Lukas Pokorny (`KXATPCHALLENGERDOUBLES-26NOV03MARPOKCERWIN-MARPOK`) | 0.54 / 0.63 (812) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Felitsata Dorofeeva-Rybas vs Charo Esquiva Banuls -- W50 Heraklion R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264962:267022:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felitsata Dorofeeva-Rybas (`KXITFWMATCH-26NOV03DORESQ-DOR`) | 0.72 / 0.80 (7) | 76.0% | 55.8% | 66.6% | 54.3% [48.4%-59.0%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.2 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Charo Esquiva Banuls (`KXITFWMATCH-26NOV03DORESQ-ESQ`) | 0.17 / 0.25 (108) | 21.0% | 44.2% | 33.4% | 45.7% [41.0%-51.6%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +23.2 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 923.0, B 1005.0; serve-point win A 52.3%, B 48.8%; Elo A 1447.6, B 1466.2; model uncertainty 0.0532
* Form inputs: days since last match A 337, B 49; matches on record A 19, B 35; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV03DORESQ-ESQ  (YES = Charo Esquiva Banuls)
Model: 44%
Kalshi: 21%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, SCHEDULED_START_PASSED
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.000, surface_dev_loose +0.016, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria Yesypchuk vs Teodora Miron -- W50 Heraklion R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 16:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T16:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260032:270171:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Teodora Miron (`KXITFWMATCH-26NOV03YESMIR-MIR`) | 0.10 / 0.11 (3722) | 10.5% | 13.6% | 28.7% | 28.7% [27.0%-30.6%] | 34.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +3.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daria Yesypchuk (`KXITFWMATCH-26NOV03YESMIR-YES`) | 0.89 / 0.90 (12961) | 89.5% | 86.5% | 71.3% | 71.3% [69.4%-73.0%] | 65.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -3.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2518.0, B 136.0; serve-point win A 57.4%, B 50.8%; Elo A 1478.0, B 1320.1; model uncertainty 0.0181
* Form inputs: days since last match A 8, B 470; matches on record A 153, B 2; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.013, surface_pool_high -0.018, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Khotchenkov / Yazdani vs Laubic / Lugaric -- M15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03KHOYAZLAULUG:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Khotchenkov / Yazdani (`KXITFDOUBLES-26NOV03KHOYAZLAULUG-KHOYAZ`) | 0.08 / 0.96 (1) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Laubic / Lugaric (`KXITFDOUBLES-26NOV03KHOYAZLAULUG-LAULUG`) | 0.02 / 0.92 (7) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Valentini Grammatikopoulou vs Natalija Senic -- W50 Heraklion R64

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204394:239476:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentini Grammatikopoulou (`KXITFWMATCH-26NOV03GRASEN-GRA`) | 0.80 / 0.81 (191) | 80.5% | 40.9% | 35.3% | 37.9% [32.9%-49.5%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -39.6 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Natalija Senic (`KXITFWMATCH-26NOV03GRASEN-SEN`) | 0.18 / 0.20 (324) | 19.0% | 59.1% | 64.7% | 62.1% [50.5%-67.1%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +40.1 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2942.0, B 2163.0; serve-point win A 51.0%, B 47.2%; Elo A 1508.1, B 1564.9; model uncertainty 0.0829
* Form inputs: days since last match A 113, B 190; matches on record A 724, B 257; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV03GRASEN-SEN  (YES = Natalija Senic)
Model: 59%
Kalshi: 19%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.047, surface_pool_high -0.040, surface_dev_loose +0.015, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Iushchenko / Turkmen vs Agureeva / Cirpanli -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03IUSTURAGUCIR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agureeva / Cirpanli (`KXITFWDOUBLES-26NOV03IUSTURAGUCIR-AGUCIR`) | 0.01 / 0.69 (1) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Iushchenko / Turkmen (`KXITFWDOUBLES-26NOV03IUSTURAGUCIR-IUSTUR`) | 0.03 / 0.74 (1) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Kumru / Senica vs Stamatova / Wirges -- W15 Antalya R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 17:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T17:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03KUMSENSTAWIR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kumru / Senica (`KXITFWDOUBLES-26NOV03KUMSENSTAWIR-KUMSEN`) | 0.11 / 0.89 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Stamatova / Wirges (`KXITFWDOUBLES-26NOV03KUMSENSTAWIR-STAWIR`) | 0.03 / 0.69 (1) | 36.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Thiago Cigarran vs Hernan Casanova -- ATP Challenger Villa Maria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 17:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106292:208532:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hernan Casanova (`KXATPCHALLENGERMATCH-26NOV03CIGCAS-CAS`) | 0.74 / 0.78 (67) | 76.0% | 79.4% | 86.9% | 86.0% [84.1%-88.0%] | -- | 75.5% | 75.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.4 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Thiago Cigarran (`KXATPCHALLENGERMATCH-26NOV03CIGCAS-CIG`) | 0.22 / 0.25 (150) | 23.5% | 20.6% | 13.1% | 14.0% [12.0%-15.9%] | -- | 24.6% | 24.6% | MODEL_LONE_OUTLIER | PASS | -2.9 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 2033.0, B 3101.0; serve-point win A 53.7%, B 40.1%; Elo A 1271.0, B 1574.9; model uncertainty 0.0195
* Form inputs: days since last match A 22, B 15; matches on record A 165, B 812; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.006, surface_dev_loose -0.006, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Juan Estevez vs Ryo Tabata -- ATP Challenger Villa Maria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 17:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211661:212944:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Juan Estevez (`KXATPCHALLENGERMATCH-26NOV03ESTTAB-EST`) | 0.66 / 0.69 (0) | 67.5% | 69.9% | 74.6% | 72.5% [70.7%-74.3%] | -- | 68.3% | 68.3% | MODEL_LONE_OUTLIER | WATCH | +2.4 pp | NORMAL | AGING | B / LIMITED | ALL_AGREE | VERIFIED |
| Ryo Tabata (`KXATPCHALLENGERMATCH-26NOV03ESTTAB-TAB`) | 0.30 / 0.33 (151) | 31.5% | 30.1% | 25.4% | 27.5% [25.7%-29.3%] | -- | 32.0% | 32.0% | MODEL_LONE_OUTLIER | PASS | -1.4 pp | NORMAL | AGING | B / LIMITED | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 3310.0, B 1648.0; serve-point win A 61.2%, B 42.8%; Elo A 1467.9, B 1325.5; model uncertainty 0.0178
* Form inputs: days since last match A 8, B 141; matches on record A 196, B 39; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.009, surface_dev_loose -0.018, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Juan Manuel La Serna vs Mateo Del Pino -- ATP Challenger Villa Maria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 17:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210182:210412:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateo Del Pino (`KXATPCHALLENGERMATCH-26NOV03LADEL-DEL`) | 0.51 / 0.52 (0) | 51.5% | 11.8% | 13.9% | 11.8% [10.7%-12.9%] | 8.0% | -- | 8.0% | MODEL_LONE_OUTLIER | PASS | -39.7 pp | EXTREME (DATA_WARNING) | AGING | B / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Juan Manuel La Serna (`KXATPCHALLENGERMATCH-26NOV03LADEL-LA`) | 0.46 / 0.49 (65) | 47.5% | 88.2% | 86.1% | 88.2% [87.1%-89.3%] | 92.0% | -- | 92.0% | MODEL_LONE_OUTLIER | SHADOW_BET | +40.7 pp | EXTREME (DATA_WARNING) | AGING | B / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 3904.0, B 1012.0; serve-point win A 60.9%, B 48.1%; Elo A 1577.7, B 1201.9; model uncertainty 0.0111
* Form inputs: days since last match A 8, B 8; matches on record A 197, B 95; data quality B

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV03LADEL-LA  (YES = Juan Manuel La Serna)
Model: 88%
Kalshi: 48%
Gap: +41 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_MODEL
Data quality: B (ADEQUATE)
Reasons: EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.008, surface_dev_loose +0.003, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE

## Giovanni Mpetshi Perricard vs Martin Krumich -- ATP Challenger Bratislava II R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 17:10Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T17:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208659:209322:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Martin Krumich (`KXATPCHALLENGERMATCH-26NOV03MPEKRU-KRU`) | 0.27 / 0.28 (2153) | 27.5% | 33.6% | 61.1% | 51.5% [43.7%-56.3%] | -- | 27.2% | -- | INSUFFICIENT_INPUTS | WATCH | +6.1 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Giovanni Mpetshi Perricard (`KXATPCHALLENGERMATCH-26NOV03MPEKRU-MPE`) | 0.72 / 0.73 (7143) | 72.5% | 66.4% | 38.9% | 48.5% [43.7%-56.3%] | -- | 72.8% | -- | INSUFFICIENT_INPUTS | PASS | -6.1 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4293.0, B 5586.0; serve-point win A 67.7%, B 35.8%; Elo A 1774.2, B 1593.4; model uncertainty 0.063
* Form inputs: days since last match A 7, B 29; matches on record A 328, B 371; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.019, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Maria Carle vs Despina Papamichail -- WTA 125K Cali R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-03 20:10Z
* Current expected start: 2026-11-03 17:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-03 16:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · surface ? · scheduled 2026-11-03T20:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:26NOV03CARPAP:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Carle (`KXWTACHALLENGERMATCH-26NOV03CARPAP-CAR`) | 0.69 / 0.70 (172) | 69.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Despina Papamichail (`KXWTACHALLENGERMATCH-26NOV03CARPAP-PAP`) | 0.30 / 0.31 (2782) | 30.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: BET_BLOCKED_START_STATUS; NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Rebeka Masarova vs Alice Tubello -- WTA 125K Cali R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-03 20:10Z
* Current expected start: 2026-11-03 17:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-03 16:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-11-03T20:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214119:220554:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rebeka Masarova (`KXWTACHALLENGERMATCH-26NOV03MASTUB-MAS`) | 0.53 / 0.54 (582) | 53.5% | 55.7% | 35.6% | 44.2% [39.1%-56.8%] | 53.1% | 53.4% | 53.4% | MARKETS_AGREE | PASS | +2.2 pp | NORMAL | AGING | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Alice Tubello (`KXWTACHALLENGERMATCH-26NOV03MASTUB-TUB`) | 0.45 / 0.46 (124) | 45.5% | 44.3% | 64.4% | 55.8% [43.2%-60.9%] | 46.9% | 46.8% | 46.8% | MODEL_LONE_OUTLIER | WATCH | -1.2 pp | NORMAL | AGING | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4283.0, B 2580.0; serve-point win A 57.2%, B 43.8%; Elo A 1790.4, B 1725.0; model uncertainty 0.0887
* Form inputs: days since last match A 7, B 2; matches on record A 453, B 337; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.010, surface_dev_loose -0.005, surface_dev_tight +0.011
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Carole Monnet vs Maria Fernanda Herazo Gonzalez -- WTA 125K Cali R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-03 20:10Z
* Current expected start: 2026-11-03 17:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-03 16:45Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-11-03T20:10:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:211864:220733:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maria Fernanda Herazo Gonzalez (`KXWTACHALLENGERMATCH-26NOV03MONHER-HER`) | 0.05 / 0.06 (2194) | 5.5% | 13.3% | 23.8% | 21.8% [18.1%-24.7%] | -- | 4.9% | 4.9% | MODEL_LONE_OUTLIER | WATCH | +7.8 pp | NORMAL | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Carole Monnet (`KXWTACHALLENGERMATCH-26NOV03MONHER-MON`) | 0.94 / 0.95 (2283) | 94.5% | 86.7% | 76.2% | 78.2% [75.3%-81.9%] | -- | 94.8% | 94.8% | MODEL_LONE_OUTLIER | PASS | -7.8 pp | NORMAL | AGING | C / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3719.0, B 1645.0; serve-point win A 55.8%, B 52.5%; Elo A 1670.2, B 1433.1; model uncertainty 0.0328
* Form inputs: days since last match A 2, B 211; matches on record A 525, B 525; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.029, surface_dev_loose +0.012, surface_dev_tight -0.016
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Jurij Rodionov vs Stefano Travaglia -- ATP Challenger Bratislava II R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 17:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T17:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105882:200514:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jurij Rodionov (`KXATPCHALLENGERMATCH-26NOV03RODTRA-ROD`) | 0.59 / 0.61 (14502) | 60.0% | 55.2% | 45.9% | 47.4% [46.4%-48.4%] | 58.4% | 59.6% | 59.0% | MODEL_LONE_OUTLIER | PASS | -4.8 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Stefano Travaglia (`KXATPCHALLENGERMATCH-26NOV03RODTRA-TRA`) | 0.39 / 0.40 (0) | 39.5% | 44.8% | 54.1% | 52.6% [51.5%-53.6%] | 41.6% | 40.1% | 40.9% | MODEL_LONE_OUTLIER | SHADOW_BET | +5.3 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5184.0, B 5435.0; serve-point win A 60.3%, B 40.7%; Elo A 1685.1, B 1670.1; model uncertainty 0.0103
* Form inputs: days since last match A 6, B 8; matches on record A 613, B 1011; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE

## Alastair Gray vs Valentin Royer -- ATP Challenger Charlottesville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-03T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202400:208316:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alastair Gray (`KXATPCHALLENGERMATCH-26NOV03GRAROY-GRA`) | 0.78 / 0.79 (13880) | 78.5% | 34.8% | 58.9% | 51.0% [41.6%-56.4%] | 30.3% | -- | 30.3% | MODEL_LONE_OUTLIER | PASS | -43.7 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |
| Valentin Royer (`KXATPCHALLENGERMATCH-26NOV03GRAROY-ROY`) | 0.21 / 0.22 (32931) | 21.5% | 65.2% | 41.1% | 49.0% [43.6%-58.4%] | 69.7% | -- | 69.7% | MODEL_LONE_OUTLIER | WATCH | +43.7 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | AGREES_WITH_MODEL | VERIFIED |

* Serve evidence (points): A 3694.0, B 6272.0; serve-point win A 62.8%, B 34.1%; Elo A 1580.2, B 1713.8; model uncertainty 0.074
* Form inputs: days since last match A 50, B 8; matches on record A 326, B 459; data quality A

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV03GRAROY-ROY  (YES = Valentin Royer)
Model: 65%
Kalshi: 22%
Gap: +44 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_MODEL
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_CONFIRMATION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Michel Hopp vs Cezar Cretu -- M25 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206470:210424:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cezar Cretu (`KXITFMATCH-26NOV03HOPCRE-CRE`) | 0.94 / 0.95 (4) | 94.5% | 77.8% | 74.8% | 72.6% [69.9%-75.2%] | 81.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -16.7 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Michel Hopp (`KXITFMATCH-26NOV03HOPCRE-HOP`) | 0.05 / 0.06 (938) | 5.5% | 22.2% | 25.2% | 27.4% [24.8%-30.1%] | 18.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +16.7 pp | HIGH_REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2320.0, B 4025.0; serve-point win A 50.7%, B 43.5%; Elo A 1346.6, B 1482.5; model uncertainty 0.0267
* Form inputs: days since last match A 204, B 22; matches on record A 83, B 422; data quality B

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03HOPCRE-HOP  (YES = Michel Hopp)
Model: 22%
Kalshi: 6%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.026, surface_pool_high +0.027, surface_dev_loose +0.018, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikita Mashtakov vs Lorenzo Angelini -- M25 Heraklion R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 18:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149117:tml:MW62:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Angelini (`KXITFMATCH-26NOV03MASANG-ANG`) | 0.99 / -- (0) | -- | 65.2% | 73.5% | 48.9% [46.8%-53.2%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | AGING | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |
| Nikita Mashtakov (`KXITFMATCH-26NOV03MASANG-MAS`) | -- / 0.01 (223542) | -- | 34.8% | 26.5% | 51.1% [46.8%-53.2%] | 50.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | AGING | F / POOR | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 306.0, B 2397.0; serve-point win A 52.1%, B 45.0%; Elo A 1415.8, B 1370.3; model uncertainty 0.032
* Form inputs: days since last match A 43, B 197; matches on record A 5, B 69; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.011, surface_dev_loose -0.011, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chiesa / Pedone vs Lew Yan Foon / Nguyen Tan -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03CHIPEDLEWNGU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chiesa / Pedone (`KXITFWDOUBLES-26NOV03CHIPEDLEWNGU-CHIPED`) | 0.06 / 0.78 (2) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lew Yan Foon / Nguyen Tan (`KXITFWDOUBLES-26NOV03CHIPEDLEWNGU-LEWNGU`) | -- / 0.68 (1) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## De Ezcurra / Zaremba vs Donnell / Mewett -- W15 Monastir R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03DEEZARDONMEW:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| De Ezcurra / Zaremba (`KXITFWDOUBLES-26NOV03DEEZARDONMEW-DEEZAR`) | 0.55 / 0.76 (1) | 65.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Donnell / Mewett (`KXITFWDOUBLES-26NOV03DEEZARDONMEW-DONMEW`) | 0.25 / 0.40 (0) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ruxandra Bertea / Nicoleta Todoni vs Allen / Karatancheva -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03RUXNICALLKAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Allen / Karatancheva (`KXITFWDOUBLES-26NOV03RUXNICALLKAR-ALLKAR`) | -- / 0.78 (1) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ruxandra Bertea / Nicoleta Todoni (`KXITFWDOUBLES-26NOV03RUXNICALLKAR-RUXNIC`) | 0.02 / 0.68 (1) | 35.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Svatikova / Tichackova vs Cortez Llorca / Roura Llaverias -- W50 Heraklion R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 18:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T18:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03SVATICCORROU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cortez Llorca / Roura Llaverias (`KXITFWDOUBLES-26NOV03SVATICCORROU-CORROU`) | 0.04 / 0.50 (31) | 27.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Svatikova / Tichackova (`KXITFWDOUBLES-26NOV03SVATICCORROU-SVATIC`) | 0.43 / 0.74 (10) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Gabriele Crivellaro vs Lorenzo Berto -- M15 San Gregorio di Catania R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-03T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213120:213927:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Berto (`KXITFMATCH-26NOV03CRIBER-BER`) | 0.20 / 0.26 (2) | 23.0% | 53.1% | 45.4% | 58.2% [55.1%-59.2%] | 43.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +30.1 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Gabriele Crivellaro (`KXITFMATCH-26NOV03CRIBER-CRI`) | 0.73 / 0.78 (0) | 75.5% | 46.9% | 54.6% | 41.8% [40.8%-44.9%] | 57.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -28.6 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 464.0, B 253.0; serve-point win A 59.8%, B 39.6%; Elo A 1235.5, B 1308.4; model uncertainty 0.0203
* Form inputs: days since last match A 57, B 43; matches on record A 16, B 7; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03CRIBER-BER  (YES = Lorenzo Berto)
Model: 53%
Kalshi: 23%
Gap: +30 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pietro Marino vs Gabriele Maria Noce -- M15 San Gregorio di Catania R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 18:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-03T18:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:122294:209233:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pietro Marino (`KXITFMATCH-26NOV03MARNOC-MAR`) | 0.99 / -- (0) | -- | 39.1% | 29.2% | 37.2% [33.3%-43.8%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -- | UNPRICED | AGING | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |
| Gabriele Maria Noce (`KXITFMATCH-26NOV03MARNOC-NOC`) | -- / 0.01 (32523) | -- | 60.9% | 70.8% | 62.8% [56.2%-66.7%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -- | UNPRICED | AGING | C / LIMITED | INSUFFICIENT_INPUTS | VERIFIED |

* Serve evidence (points): A 1636.0, B 2114.0; serve-point win A 57.6%, B 40.3%; Elo A 1264.5, B 1283.7; model uncertainty 0.0524
* Form inputs: days since last match A 92, B 204; matches on record A 149, B 245; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.015, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; ONE_SIDED_OR_NO_QUOTE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kimmer Coppejans vs Jonas Forejtek -- ATP Challenger Bratislava II R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 18:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T18:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106293:207797:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kimmer Coppejans (`KXATPCHALLENGERMATCH-26NOV03COPFOR-COP`) | 0.38 / 0.39 (376) | 38.5% | 51.9% | 54.7% | 56.2% [55.2%-57.8%] | 40.1% | 39.0% | 39.5% | MODEL_LONE_OUTLIER | WATCH | +13.4 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jonas Forejtek (`KXATPCHALLENGERMATCH-26NOV03COPFOR-FOR`) | 0.61 / 0.62 (6874) | 61.5% | 48.1% | 45.3% | 43.8% [42.2%-44.8%] | 59.9% | 61.0% | 60.5% | MODEL_LONE_OUTLIER | PASS | -13.4 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4985.0, B 4481.0; serve-point win A 58.9%, B 41.4%; Elo A 1685.3, B 1607.1; model uncertainty 0.0128
* Form inputs: days since last match A 17, B 15; matches on record A 895, B 413; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Sofia Costoulas vs Marina Bassols Ribera -- WTA 125K Cali R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-03 21:20Z
* Current expected start: 2026-11-03 19:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-03 18:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-11-03T21:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:215453:223321:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marina Bassols Ribera (`KXWTACHALLENGERMATCH-26NOV03COSBAS-BAS`) | 0.65 / 0.66 (2419) | 65.5% | 66.3% | 44.2% | 50.0% [46.8%-55.8%] | 65.7% | 64.8% | 64.8% | MODEL_LONE_OUTLIER | PASS | +0.8 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Sofia Costoulas (`KXWTACHALLENGERMATCH-26NOV03COSBAS-COS`) | 0.34 / 0.35 (439) | 34.5% | 33.7% | 55.8% | 50.0% [44.2%-53.2%] | 34.3% | 34.6% | 34.6% | MODEL_LONE_OUTLIER | SHADOW_BET | -0.8 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4020.0, B 4611.0; serve-point win A 52.5%, B 44.3%; Elo A 1622.6, B 1728.6; model uncertainty 0.0451
* Form inputs: days since last match A 7, B 4; matches on record A 329, B 582; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high +0.000, surface_dev_loose -0.016, surface_dev_tight +0.021
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Julia Grabher vs Laura Pigossi -- WTA 125K Cali R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-03 21:20Z
* Current expected start: 2026-11-03 19:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-03 18:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-11-03T21:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:206007:211814:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Grabher (`KXWTACHALLENGERMATCH-26NOV03GRAPIG-GRA`) | 0.80 / 0.81 (2198) | 80.5% | 79.5% | 69.0% | 70.9% [69.9%-72.2%] | 78.7% | 80.7% | 80.7% | MODEL_LONE_OUTLIER | PASS | -1.0 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Laura Pigossi (`KXWTACHALLENGERMATCH-26NOV03GRAPIG-PIG`) | 0.19 / 0.20 (943) | 19.5% | 20.5% | 31.0% | 29.1% [27.8%-30.1%] | 21.3% | 19.7% | 19.7% | MODEL_LONE_OUTLIER | SHADOW_BET | +1.0 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3872.0, B 4474.0; serve-point win A 56.3%, B 49.9%; Elo A 1839.1, B 1633.2; model uncertainty 0.0115
* Form inputs: days since last match A 2, B 7; matches on record A 707, B 770; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.014, surface_dev_loose +0.009, surface_dev_tight +0.004
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Tamara Zidansek vs Bianca Andreescu -- WTA 125K Cali R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-03 21:20Z
* Current expected start: 2026-11-03 19:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-03 18:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-11-03T21:20:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:214461:215370:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bianca Andreescu (`KXWTACHALLENGERMATCH-26NOV03ZIDAND-AND`) | 0.66 / 0.67 (2324) | 66.5% | 52.5% | 46.8% | 46.8% [43.6%-54.2%] | 65.7% | 66.5% | 66.1% | MODEL_LONE_OUTLIER | PASS | -13.9 pp | REVIEW | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Tamara Zidansek (`KXWTACHALLENGERMATCH-26NOV03ZIDAND-ZID`) | 0.32 / 0.33 (66) | 32.5% | 47.4% | 53.2% | 53.2% [45.8%-56.4%] | 34.3% | 33.9% | 34.1% | MODEL_LONE_OUTLIER | WATCH | +14.9 pp | REVIEW | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4639.0, B 2877.0; serve-point win A 53.8%, B 45.8%; Elo A 1856.9, B 1837.6; model uncertainty 0.0531
* Form inputs: days since last match A 4, B 2; matches on record A 638, B 376; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.043, surface_pool_high +0.032, surface_dev_loose +0.011, surface_dev_tight -0.016
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE

## Consolo / Massucco vs Angeloni / Primucci -- M15 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03CONMASANGPRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Angeloni / Primucci (`KXITFDOUBLES-26NOV03CONMASANGPRI-ANGPRI`) | 0.89 / 0.90 (0) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Consolo / Massucco (`KXITFDOUBLES-26NOV03CONMASANGPRI-CONMAS`) | 0.07 / 0.10 (0) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Nathan Cox vs John Chin -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210675:213920:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| John Chin (`KXITFMATCH-26NOV03COXCHI-CHI`) | 0.28 / 0.29 (105) | 28.5% | 28.0% | 44.8% | 29.2% [28.1%-30.1%] | 23.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nathan Cox (`KXITFMATCH-26NOV03COXCHI-COX`) | 0.72 / 0.73 (75) | 72.5% | 72.0% | 55.2% | 70.8% [69.9%-71.9%] | 76.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 418.0, B 154.0; serve-point win A 60.7%, B 43.8%; Elo A 1287.9, B 1119.6; model uncertainty 0.0096
* Form inputs: days since last match A 358, B 71; matches on record A 7, B 24; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Buvaysar Gadamauri vs Pierluigi Basile -- ATP Challenger Taranto R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-03T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207527:213003:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pierluigi Basile (`KXATPCHALLENGERMATCH-26NOV03GADBAS-BAS`) | 0.32 / 0.33 (709) | 32.5% | 26.2% | 26.3% | 23.5% [22.8%-24.7%] | 32.3% | 32.3% | 32.3% | MODEL_LONE_OUTLIER | PASS | -6.3 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Buvaysar Gadamauri (`KXATPCHALLENGERMATCH-26NOV03GADBAS-GAD`) | 0.67 / 0.68 (3544) | 67.5% | 73.8% | 73.7% | 76.5% [75.3%-77.2%] | 67.7% | 68.5% | 68.1% | MODEL_LONE_OUTLIER | SHADOW_BET | +6.3 pp | NORMAL | AGING | B / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4560.0, B 1734.0; serve-point win A 64.9%, B 40.1%; Elo A 1705.6, B 1467.0; model uncertainty 0.0097
* Form inputs: days since last match A 22, B 15; matches on record A 312, B 62; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Valentino Grippo vs Genaro Alberto Olivieri -- ATP Challenger Villa Maria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144821:213201:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentino Grippo (`KXATPCHALLENGERMATCH-26NOV03GRIOLI-GRI`) | 0.04 / 0.06 (2323) | 5.0% | 5.3% | 12.6% | 7.7% [6.7%-8.6%] | 7.3% | 4.5% | 5.9% | MODEL_LONE_OUTLIER | PASS | +0.3 pp | NORMAL | AGING | D / POOR | ALL_AGREE | VERIFIED |
| Genaro Alberto Olivieri (`KXATPCHALLENGERMATCH-26NOV03GRIOLI-OLI`) | 0.94 / 0.96 (2538) | 95.0% | 94.7% | 87.4% | 92.3% [91.3%-93.3%] | 92.7% | 95.8% | 94.2% | MODEL_LONE_OUTLIER | PASS | -0.3 pp | NORMAL | AGING | D / POOR | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 635.0, B 5035.0; serve-point win A 52.6%, B 34.9%; Elo A 1113.5, B 1586.5; model uncertainty 0.0096
* Form inputs: days since last match A 190, B 8; matches on record A 13, B 609; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high -0.002, surface_dev_loose -0.005, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER

## Alan Magadan vs Valerio Aboian -- ATP Challenger Villa Maria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209246:209254:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valerio Aboian (`KXATPCHALLENGERMATCH-26NOV03MAGABO-ABO`) | 0.73 / 0.74 (7155) | 73.5% | 70.5% | 61.8% | 67.5% [65.2%-69.8%] | 73.1% | 74.1% | 74.1% | MODEL_LONE_OUTLIER | PASS | -3.0 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Alan Magadan (`KXATPCHALLENGERMATCH-26NOV03MAGABO-MAG`) | 0.26 / 0.27 (1630) | 26.5% | 29.5% | 38.2% | 32.5% [30.2%-34.8%] | 26.9% | 25.5% | 25.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +3.0 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 2054.0, B 4857.0; serve-point win A 57.3%, B 38.6%; Elo A 1370.0, B 1559.0; model uncertainty 0.0233
* Form inputs: days since last match A 8, B 8; matches on record A 85, B 372; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.018, surface_dev_loose +0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Rohan Sachdev vs Justin Roberts -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03SACROB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justin Roberts (`KXITFMATCH-26NOV03SACROB-ROB`) | 0.59 / 0.60 (3999) | 59.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rohan Sachdev (`KXITFMATCH-26NOV03SACROB-SAC`) | 0.40 / 0.41 (623) | 40.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dalibor Svrcina vs Norbert Gombos -- ATP Challenger Bratislava II R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105613:207494:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Norbert Gombos (`KXATPCHALLENGERMATCH-26NOV03SVRGOM-GOM`) | 0.30 / 0.31 (1997) | 30.5% | 25.5% | 33.7% | 34.6% [32.2%-37.1%] | 32.9% | 31.3% | 32.1% | MARKETS_AGREE | WATCH | -5.0 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Dalibor Svrcina (`KXATPCHALLENGERMATCH-26NOV03SVRGOM-SVR`) | 0.68 / 0.70 (18588) | 69.0% | 74.5% | 66.3% | 65.4% [62.9%-67.8%] | 67.1% | 69.0% | 68.0% | MARKETS_AGREE | PASS | +5.5 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5261.0, B 4496.0; serve-point win A 59.8%, B 45.2%; Elo A 1728.4, B 1632.9; model uncertainty 0.0243
* Form inputs: days since last match A 22, B 22; matches on record A 426, B 1035; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.024, surface_pool_high -0.025, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER

## Juan Bautista Torres vs Nicolas Bruna -- ATP Challenger Villa Maria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202220:208913:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolas Bruna (`KXATPCHALLENGERMATCH-26NOV03TORBRU-BRU`) | 0.08 / 0.09 (127) | 8.5% | 7.1% | 3.6% | 5.4% [3.8%-8.4%] | 11.1% | 9.3% | -- | INSUFFICIENT_INPUTS | PASS | -1.4 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Juan Bautista Torres (`KXATPCHALLENGERMATCH-26NOV03TORBRU-TOR`) | 0.90 / 0.91 (2494) | 90.5% | 92.8% | 96.4% | 94.6% [91.6%-96.2%] | 88.9% | 91.8% | 91.8% | MARKETS_AGREE | WATCH | +2.4 pp | NORMAL | AGING | B / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5064.0, B 1663.0; serve-point win A 61.6%, B 49.5%; Elo A 1604.3, B 1175.9; model uncertainty 0.023
* Form inputs: days since last match A 190, B 190; matches on record A 360, B 130; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE

## Kian Vakili vs Richard Mallory -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:130688:210704:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Richard Mallory (`KXITFMATCH-26NOV03VAKMAL-MAL`) | 0.86 / 0.87 (460) | 86.5% | 48.2% | 40.7% | 47.9% [46.4%-49.0%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -38.3 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kian Vakili (`KXITFMATCH-26NOV03VAKMAL-VAK`) | 0.13 / 0.14 (1277) | 13.5% | 51.8% | 59.3% | 52.1% [51.0%-53.6%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +38.3 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 173.0, B 145.0; serve-point win A 59.4%, B 41.0%; Elo A 1201.5, B 1193.7; model uncertainty 0.0131
* Form inputs: days since last match A 190, B 400; matches on record A 16, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03VAKMAL-VAK  (YES = Kian Vakili)
Model: 52%
Kalshi: 14%
Gap: +38 pp
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
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jefferson Wendler Filho vs Giovanni Branchetti -- M15 Salvador R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03WENBRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Giovanni Branchetti (`KXITFMATCH-26NOV03WENBRA-BRA`) | 0.58 / 0.59 (11) | 58.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jefferson Wendler Filho (`KXITFMATCH-26NOV03WENBRA-WEN`) | 0.40 / 0.42 (3077) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anika Jaskova vs Lea Boskovic -- W35 Liberec R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-03T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214521:222637:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lea Boskovic (`KXITFWMATCH-26NOV03JASBOS-BOS`) | 0.98 / 0.99 (6384) | 98.5% | 92.0% | 73.2% | 80.5% [79.0%-81.8%] | 92.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anika Jaskova (`KXITFWMATCH-26NOV03JASBOS-JAS`) | 0.01 / 0.02 (3437) | 1.5% | 8.0% | 26.8% | 19.5% [18.2%-21.0%] | 7.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +6.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 199.0, B 2773.0; serve-point win A 46.4%, B 43.1%; Elo A 1389.6, B 1638.8; model uncertainty 0.0143
* Form inputs: days since last match A 456, B 18; matches on record A 182, B 440; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.015, surface_dev_loose -0.000, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Denisa Zoldakova vs Jade Groen -- W35 Liberec R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-03T19:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:267616:267722:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jade Groen (`KXITFWMATCH-26NOV03ZOLGRO-GRO`) | 0.13 / 0.14 (1055) | 13.5% | 14.9% | 17.4% | 25.1% [22.2%-27.8%] | 10.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +1.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Denisa Zoldakova (`KXITFWMATCH-26NOV03ZOLGRO-ZOL`) | 0.86 / 0.87 (1557) | 86.5% | 85.0% | 82.6% | 74.9% [72.2%-77.8%] | 89.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 870.0, B 470.0; serve-point win A 55.8%, B 52.0%; Elo A 1456.0, B 1292.1; model uncertainty 0.028
* Form inputs: days since last match A 48, B 358; matches on record A 20, B 9; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.004, surface_dev_loose +0.025, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Justin Boulais vs Jeffrey John Wolf -- ATP Challenger Charlottesville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · surface ? · scheduled 2026-11-03T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03BOUWOL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Justin Boulais (`KXATPCHALLENGERMATCH-26NOV03BOUWOL-BOU`) | 0.20 / 0.21 (5468) | 20.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Jeffrey John Wolf (`KXATPCHALLENGERMATCH-26NOV03BOUWOL-WOL`) | 0.79 / 0.80 (12027) | 79.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Aidan Mayo vs Pyotr Nesterov -- ATP Challenger Charlottesville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-03T19:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208854:209318:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aidan Mayo (`KXATPCHALLENGERMATCH-26NOV03MAYNES-MAY`) | 0.74 / 0.75 (13905) | 74.5% | 62.0% | 61.5% | 60.0% [57.0%-62.0%] | 74.0% | 71.9% | 74.0% | MODEL_LONE_OUTLIER | PASS | -12.5 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | AMBIGUOUS |
| Pyotr Nesterov (`KXATPCHALLENGERMATCH-26NOV03MAYNES-NES`) | 0.25 / 0.26 (333) | 25.5% | 38.0% | 38.5% | 40.0% [38.0%-43.0%] | 26.0% | 27.0% | 26.0% | MODEL_LONE_OUTLIER | PASS | +12.5 pp | REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | AMBIGUOUS |

* Serve evidence (points): A 3926.0, B 3670.0; serve-point win A 63.5%, B 38.9%; Elo A 1573.4, B 1522.2; model uncertainty 0.0246
* Form inputs: days since last match A 8, B 29; matches on record A 260, B 263; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.015, surface_dev_loose +0.010, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Casper Ruud vs Rafael Jodar -- ATP Paris R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-03 22:30Z
* Current expected start: 2026-11-03 19:30Z
* Source: LIVE_SCHEDULE:espn_atp; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-03 18:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-03T22:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:134770:212588:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael Jodar (`KXATPMATCH-26NOV03RUUJOD-JOD`) | 0.63 / 0.64 (80008) | 63.5% | 62.6% | 63.2% | 62.7% [58.4%-65.5%] | 62.3% | 63.1% | 63.1% | MODEL_LONE_OUTLIER | PASS | -0.9 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Casper Ruud (`KXATPMATCH-26NOV03RUUJOD-RUU`) | 0.36 / 0.37 (39881) | 36.5% | 37.4% | 36.8% | 37.3% [34.5%-41.6%] | 37.7% | 37.1% | 37.1% | MODEL_LONE_OUTLIER | PASS | +0.9 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5180.0, B 5302.0; serve-point win A 63.0%, B 34.4%; Elo A 1943.9, B 2016.7; model uncertainty 0.0354
* Form inputs: days since last match A 1, B 1; matches on record A 720, B 143; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.028, surface_dev_loose -0.018, surface_dev_tight +0.014
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV03RUUJOD-23` Over 22.5 games: 0.51/0.52 mid 51.5%, model 60.3% (projection_v2.0 (prediction ledger)) -- gap +8.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV03RUUJOD-28` Over 27.5 games: 0.31/0.33 mid 32.0%, model 40.1% (projection_v2.0 (prediction ledger)) -- gap +8.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV03RUUJOD-18` Over 17.5 games: 0.85/0.89 mid 87.0%, model 93.4% (projection_v2.0 (prediction ledger)) -- gap +6.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV03RUUJOD-JOD6` Will Rafael Jodar win at least 5.5 more games than Casper Ruud?: 0.13/0.24 mid 18.5%, model 12.8% (projection_v2.0 (prediction ledger)) -- gap -5.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV03RUUJOD-JOD21` Will Rafael Jodar win the Casper Ruud vs Rafael Jodar match by a set score of 2-1?: 0.22/0.24 mid 23.0%, model 28.4% (projection_v2.0 (prediction ledger)) -- gap +5.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV03RUUJOD-JOD20` Will Rafael Jodar win the Casper Ruud vs Rafael Jodar match by a set score of 2-0?: 0.39/0.40 mid 39.5%, model 34.2% (projection_v2.0 (prediction ledger)) -- gap -5.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV03RUUJOD-JOD3` Will Rafael Jodar win at least 2.5 more games than Casper Ruud?: 0.52/0.53 mid 52.5%, model 47.3% (projection_v2.0 (prediction ledger)) -- gap -5.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV03RUUJOD-RUU21` Will Casper Ruud win the Casper Ruud vs Rafael Jodar match by a set score of 2-1?: 0.14/0.18 mid 16.0%, model 20.2% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV03RUUJOD-RUU20` Will Casper Ruud win the Casper Ruud vs Rafael Jodar match by a set score of 2-0?: 0.19/0.22 mid 20.5%, model 17.2% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV03RUUJOD-2-RUU` Will Casper Ruud win set 2 in the Casper Ruud vs Rafael Jodar match: 0.37/0.40 mid 38.5%, model 41.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV03RUUJOD-2-JOD` Will Rafael Jodar win set 2 in the Casper Ruud vs Rafael Jodar match: 0.58/0.62 mid 60.0%, model 58.5% (projection_v2.0 (prediction ledger)) -- gap -1.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV03RUUJOD-RUU2` Will Casper Ruud win at least 1.5 more games than Rafael Jodar?: 0.30/0.33 mid 31.5%, model 30.3% (projection_v2.0 (prediction ledger)) -- gap -1.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV03RUUJOD-1-RUU` Will Casper Ruud win set 1 in the Casper Ruud vs Rafael Jodar match: 0.39/0.42 mid 40.5%, model 41.5% (projection_v2.0 (prediction ledger)) -- gap +1.0 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV03RUUJOD-1-JOD` Will Rafael Jodar win set 1 in the Casper Ruud vs Rafael Jodar match: 0.58/0.60 mid 59.0%, model 58.5% (projection_v2.0 (prediction ledger)) -- gap -0.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Allen / Kaczmarek vs Milev / Parisca -- M25 Valencia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03ALLKACMILPAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Allen / Kaczmarek (`KXITFDOUBLES-26NOV03ALLKACMILPAR-ALLKAC`) | 0.02 / 0.06 (1) | 4.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Milev / Parisca (`KXITFDOUBLES-26NOV03ALLKACMILPAR-MILPAR`) | 0.93 / 0.96 (5) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Barroso Campos / Pujol Navarro vs Gulin / Sheyngezikht -- M25 Valencia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03BARPUJGULSHE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barroso Campos / Pujol Navarro (`KXITFDOUBLES-26NOV03BARPUJGULSHE-BARPUJ`) | 0.53 / 0.63 (888) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gulin / Sheyngezikht (`KXITFDOUBLES-26NOV03BARPUJGULSHE-GULSHE`) | 0.37 / 0.45 (1) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Maxence Bertimon vs Radu David Turcanu -- M15 San Gregorio di Catania R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-03T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202230:212886:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxence Bertimon (`KXITFMATCH-26NOV03BERTUR-BER`) | 0.22 / 0.27 (0) | 24.5% | 27.9% | 31.0% | 29.7% [27.9%-33.0%] | 26.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +3.4 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Radu David Turcanu (`KXITFMATCH-26NOV03BERTUR-TUR`) | 0.76 / 0.78 (0) | 77.0% | 72.1% | 69.0% | 70.3% [67.0%-72.1%] | 73.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.9 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2659.0, B 2023.0; serve-point win A 56.7%, B 38.8%; Elo A 1298.1, B 1468.2; model uncertainty 0.0254
* Form inputs: days since last match A 190, B 211; matches on record A 133, B 62; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.018, surface_dev_loose -0.013, surface_dev_tight +0.014
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Miletich / Rojas vs Naharro / Talan Lopatic -- M25 Valencia R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03MILROJNAHTAL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miletich / Rojas (`KXITFDOUBLES-26NOV03MILROJNAHTAL-MILROJ`) | 0.21 / 0.30 (20) | 25.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Naharro / Talan Lopatic (`KXITFDOUBLES-26NOV03MILROJNAHTAL-NAHTAL`) | 0.73 / 0.76 (1) | 74.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Moutama / Suslova vs Pahwa / Popovic -- W15 Sharm ElSheikh R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 19:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T19:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03MOUSUSPAHPOP:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Moutama / Suslova (`KXITFWDOUBLES-26NOV03MOUSUSPAHPOP-MOUSUS`) | 0.19 / 0.21 (10) | 20.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pahwa / Popovic (`KXITFWDOUBLES-26NOV03MOUSUSPAHPOP-PAHPOP`) | 0.81 / 0.82 (439) | 81.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Victor Braga vs Diego Ortiz Gamonal -- M15 Salvador R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-03T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212480:212786:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Victor Braga (`KXITFMATCH-26NOV03BRAORT-BRA`) | 0.79 / 0.80 (5153) | 79.5% | 41.5% | 11.0% | 35.6% [31.2%-40.7%] | 56.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -38.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Diego Ortiz Gamonal (`KXITFMATCH-26NOV03BRAORT-ORT`) | 0.20 / 0.21 (1137) | 20.5% | 58.5% | 89.0% | 64.4% [59.3%-68.8%] | 43.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +38.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1053.0, B 287.0; serve-point win A 55.7%, B 42.7%; Elo A 1132.3, B 1186.5; model uncertainty 0.0477
* Form inputs: days since last match A 190, B 295; matches on record A 26, B 10; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03BRAORT-ORT  (YES = Diego Ortiz Gamonal)
Model: 58%
Kalshi: 20%
Gap: +38 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.020, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Caruso / Cocola vs Cristian Breazu / Fiorentini -- M15 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03CARCOCCRIFIO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caruso / Cocola (`KXITFDOUBLES-26NOV03CARCOCCRIFIO-CARCOC`) | 0.43 / 0.59 (60) | 51.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cristian Breazu / Fiorentini (`KXITFDOUBLES-26NOV03CARCOCCRIFIO-CRIFIO`) | 0.24 / 0.51 (51) | 37.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Enzo Crevelaro vs Vitor Machado De Melo Cunha -- M15 Salvador R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03CRECUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enzo Crevelaro (`KXITFMATCH-26NOV03CRECUN-CRE`) | 0.77 / 0.78 (6233) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Vitor Machado De Melo Cunha (`KXITFMATCH-26NOV03CRECUN-CUN`) | 0.22 / 0.23 (4340) | 22.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Agustin Eduardo Cuellar Lorberg vs Bruno Vieira Alves Malacarne Bruno -- M15 Salvador R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03CUEBRU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bruno Vieira Alves Malacarne Bruno (`KXITFMATCH-26NOV03CUEBRU-BRU`) | 0.05 / 0.06 (2694) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Agustin Eduardo Cuellar Lorberg (`KXITFMATCH-26NOV03CUEBRU-CUE`) | 0.94 / 0.95 (4953) | 94.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mitchell Dobek vs Tariq Simons -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:131997:tml:800496619:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mitchell Dobek (`KXITFMATCH-26NOV03DOBSIM-DOB`) | 0.43 / 0.48 (1) | 45.5% | 28.8% | 50.0% | 28.5% [28.5%-28.5%] | -- | -- | -- | -- | PASS | -16.7 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Tariq Simons (`KXITFMATCH-26NOV03DOBSIM-SIM`) | 0.51 / 0.60 (6) | 55.5% | 71.2% | 50.0% | 71.5% [71.5%-71.5%] | -- | -- | -- | -- | PASS | +15.7 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 0.0; serve-point win A 58.0%, B 37.7%; Elo A 1238.3, B 1400.3; model uncertainty 0.0
* Form inputs: days since last match A 4201, B 44; matches on record A 2, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03DOBSIM-SIM  (YES = Tariq Simons)
Model: 71%
Kalshi: 56%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karol Pio Osti / Tammaro vs Botta / Stella -- M15 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03KARTAMBOTSTE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Botta / Stella (`KXITFDOUBLES-26NOV03KARTAMBOTSTE-BOTSTE`) | 0.03 / 0.68 (1) | 35.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Karol Pio Osti / Tammaro (`KXITFDOUBLES-26NOV03KARTAMBOTSTE-KARTAM`) | 0.09 / 0.91 (7) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mikovic / Mikovic vs Ciurnelli / Gribaldo -- M15 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03MIKMIKCIUGRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ciurnelli / Gribaldo (`KXITFDOUBLES-26NOV03MIKMIKCIUGRI-CIUGRI`) | 0.07 / 0.91 (2) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mikovic / Mikovic (`KXITFDOUBLES-26NOV03MIKMIKCIUGRI-MIKMIK`) | 0.03 / 0.79 (2) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Pedro Petroski Rocha vs Jacob Brumm -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03PETBRU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jacob Brumm (`KXITFMATCH-26NOV03PETBRU-BRU`) | 0.86 / 0.93 (1) | 89.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pedro Petroski Rocha (`KXITFMATCH-26NOV03PETBRU-PET`) | 0.09 / 0.11 (100) | 10.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luiz Felipe Silva vs Glauco Pinheiro da Cruz Junior -- M15 Salvador R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-03T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213415:214262:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Glauco Pinheiro da Cruz Junior (`KXITFMATCH-26NOV03SILPIN-PIN`) | 0.45 / 0.49 (1) | 47.0% | 44.1% | 20.6% | 40.6% [39.0%-41.7%] | 44.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -2.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luiz Felipe Silva (`KXITFMATCH-26NOV03SILPIN-SIL`) | 0.52 / 0.55 (10) | 53.5% | 55.9% | 79.4% | 59.4% [58.3%-61.0%] | 55.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 92.0, B 303.0; serve-point win A 56.7%, B 44.4%; Elo A 1208.5, B 1150.9; model uncertainty 0.0135
* Form inputs: days since last match A 344, B 225; matches on record A 2, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.011, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kacper Szymkowiak vs Stephen Slocombe -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212852:213723:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stephen Slocombe (`KXITFMATCH-26NOV03SZYSLO-SLO`) | 0.04 / 0.05 (0) | 4.5% | 13.5% | 20.5% | 28.2% [26.4%-29.2%] | 8.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +9.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kacper Szymkowiak (`KXITFMATCH-26NOV03SZYSLO-SZY`) | 0.93 / 0.94 (0) | 93.5% | 86.5% | 79.5% | 71.8% [70.8%-73.6%] | 91.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -7.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1216.0, B 127.0; serve-point win A 62.3%, B 46.2%; Elo A 1370.4, B 1213.2; model uncertainty 0.0141
* Form inputs: days since last match A 239, B 246; matches on record A 41, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Drew Van Orderlain vs Ben Chetewy Ungar -- M15 Pembroke R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132018:213682:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ben Chetewy Ungar (`KXITFMATCH-26NOV03VANCHE-CHE`) | 0.18 / 0.19 (4919) | 18.5% | 66.1% | 79.7% | 74.2% [74.2%-74.2%] | 24.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | +47.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Drew Van Orderlain (`KXITFMATCH-26NOV03VANCHE-VAN`) | 0.81 / 0.82 (966) | 81.5% | 33.9% | 20.3% | 25.8% [25.8%-25.8%] | 75.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | -47.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1474.0, B 0.0; serve-point win A 57.5%, B 39.3%; Elo A 1084.0, B 1264.0; model uncertainty 0.0004
* Form inputs: days since last match A 190, B 708; matches on record A 73, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03VANCHE-CHE  (YES = Ben Chetewy Ungar)
Model: 66%
Kalshi: 18%
Gap: +48 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mora Carrocera vs Alisa Danilova -- W15 Neuquén R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-03T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:206161:264240:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mora Carrocera (`KXITFWMATCH-26NOV03CARDAN-CAR`) | 0.21 / 0.25 (1) | 23.0% | 51.5% | 71.8% | 51.1% [50.0%-52.1%] | 27.6% | -- | 27.6% | KALSHI_LONE_OUTLIER | PASS | +28.5 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Alisa Danilova (`KXITFWMATCH-26NOV03CARDAN-DAN`) | 0.72 / 0.78 (3) | 75.0% | 48.5% | 28.2% | 48.9% [47.9%-50.0%] | 72.4% | -- | 72.4% | KALSHI_LONE_OUTLIER | PASS | -26.5 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 67.0, B 466.0; serve-point win A 53.5%, B 46.8%; Elo A 1184.0, B 1180.2; model uncertainty 0.0107
* Form inputs: days since last match A 407, B 190; matches on record A 3, B 31; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV03CARDAN-CAR  (YES = Mora Carrocera)
Model: 51%
Kalshi: 23%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, EXTERNAL_MARKET_REJECTION, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sol Ailin Larraya Guidi vs Melina Maria Maruca -- W15 Neuquén R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-03T20:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260709:260723:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sol Ailin Larraya Guidi (`KXITFWMATCH-26NOV03LARMAR-LAR`) | 0.98 / 0.99 (6865) | 98.5% | 85.6% | 77.0% | 78.6% [77.0%-81.2%] | 95.7% | -- | 95.7% | MODEL_LONE_OUTLIER | PASS | -12.9 pp | REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |
| Melina Maria Maruca (`KXITFWMATCH-26NOV03LARMAR-MAR`) | 0.01 / 0.02 (1063) | 1.5% | 14.4% | 23.0% | 21.4% [18.8%-23.0%] | 4.3% | -- | 4.3% | MODEL_LONE_OUTLIER | PASS | +12.9 pp | REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 409.0, B 387.0; serve-point win A 55.8%, B 52.1%; Elo A 1373.5, B 1148.3; model uncertainty 0.0213
* Form inputs: days since last match A 218, B 225; matches on record A 66, B 54; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Franco Agamenone vs Ignacio Monzon -- ATP Challenger Villa Maria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106162:133820:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Franco Agamenone (`KXATPCHALLENGERMATCH-26NOV03AGAMON-AGA`) | 0.76 / 0.77 (3650) | 76.5% | 67.6% | 65.0% | 68.9% [67.5%-70.8%] | 75.7% | 77.3% | 77.3% | MODEL_LONE_OUTLIER | PASS | -8.9 pp | NORMAL | AGING | A / LIMITED | EXTERNAL_STALE | VERIFIED |
| Ignacio Monzon (`KXATPCHALLENGERMATCH-26NOV03AGAMON-MON`) | 0.23 / 0.24 (7776) | 23.5% | 32.4% | 35.0% | 31.1% [29.2%-32.5%] | 24.3% | 22.8% | 22.8% | MODEL_LONE_OUTLIER | SHADOW_BET | +8.9 pp | NORMAL | AGING | A / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 4605.0, B 3341.0; serve-point win A 56.5%, B 46.9%; Elo A 1559.4, B 1356.6; model uncertainty 0.0164
* Form inputs: days since last match A 15, B 120; matches on record A 698, B 427; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Thiago Cigarran / Lucio Ratti vs Federico Aguilar Cardozo / Nicolas Kicker -- ATP Challenger Villa Maria R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-03T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03CIGRATAGUKIC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Aguilar Cardozo / Nicolas Kicker (`KXATPCHALLENGERDOUBLES-26NOV03CIGRATAGUKIC-AGUKIC`) | 0.39 / 0.45 (36) | 42.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thiago Cigarran / Lucio Ratti (`KXATPCHALLENGERDOUBLES-26NOV03CIGRATAGUKIC-CIGRAT`) | 0.54 / 0.57 (33) | 55.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Shintaro Mochizuki vs Nicolai Budkov Kjaer -- ATP Challenger Bratislava II R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149282:208278:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicolai Budkov Kjaer (`KXATPCHALLENGERMATCH-26NOV03MOCBUD-BUD`) | 0.62 / 0.63 (5115) | 62.5% | 59.0% | 63.8% | 61.9% [55.2%-64.3%] | -- | 62.0% | 62.0% | MODEL_LONE_OUTLIER | PASS | -3.5 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Shintaro Mochizuki (`KXATPCHALLENGERMATCH-26NOV03MOCBUD-MOC`) | 0.37 / 0.38 (397) | 37.5% | 41.0% | 36.1% | 38.1% [35.6%-44.8%] | -- | 38.1% | 38.1% | MODEL_LONE_OUTLIER | PASS | +3.5 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5037.0, B 4323.0; serve-point win A 57.0%, B 41.3%; Elo A 1640.9, B 1677.7; model uncertainty 0.0457
* Form inputs: days since last match A 8, B 8; matches on record A 455, B 182; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.020, surface_dev_loose -0.020, surface_dev_tight +0.026
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Dante Pagani vs Murkel Dellien -- ATP Challenger Villa Maria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T20:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:123961:213677:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Murkel Dellien (`KXATPCHALLENGERMATCH-26NOV03PAGDEV-DEV`) | 0.63 / 0.65 (9470) | 64.0% | 78.5% | 71.6% | 76.4% [74.7%-77.6%] | 63.1% | 65.0% | 64.1% | MODEL_LONE_OUTLIER | PASS | +14.5 pp | REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | AMBIGUOUS |
| Dante Pagani (`KXATPCHALLENGERMATCH-26NOV03PAGDEV-PAG`) | 0.35 / 0.36 (66) | 35.5% | 21.5% | 28.4% | 23.6% [22.4%-25.3%] | 36.9% | 35.2% | 36.0% | MODEL_LONE_OUTLIER | PASS | -14.0 pp | REVIEW | AGING | D / POOR | AGREES_WITH_KALSHI | AMBIGUOUS |

* Serve evidence (points): A 964.0, B 4395.0; serve-point win A 52.1%, B 42.0%; Elo A 1287.0, B 1515.2; model uncertainty 0.0144
* Form inputs: days since last match A 190, B 22; matches on record A 23, B 403; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.012, surface_dev_loose -0.000, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY

## Andrew Fenty vs Darwin Blanch -- ATP Challenger Charlottesville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-03T20:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208649:210464:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Darwin Blanch (`KXATPCHALLENGERMATCH-26NOV03FENBLA-BLA`) | 0.78 / 0.79 (2450) | 78.5% | 82.3% | 66.7% | 71.9% [69.3%-75.9%] | 76.6% | 77.5% | 76.6% | MODEL_LONE_OUTLIER | PASS | +3.8 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Andrew Fenty (`KXATPCHALLENGERMATCH-26NOV03FENBLA-FEN`) | 0.21 / 0.22 (864) | 21.5% | 17.7% | 33.3% | 28.1% [24.1%-30.7%] | 23.4% | 21.3% | 23.4% | MODEL_LONE_OUTLIER | WATCH | -3.8 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3101.0, B 4745.0; serve-point win A 61.3%, B 31.1%; Elo A 1432.6, B 1686.9; model uncertainty 0.0329
* Form inputs: days since last match A 36, B 8; matches on record A 177, B 181; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose -0.003, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Andres Santamarta Roig vs Clement Chidekh -- ATP Challenger Charlottesville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-03T20:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206889:212749:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Clement Chidekh (`KXATPCHALLENGERMATCH-26NOV03SANCHI-CHI`) | 0.91 / 0.92 (710) | 91.5% | 78.9% | 84.5% | 82.2% [79.7%-83.6%] | 89.5% | 92.2% | 92.2% | MODEL_LONE_OUTLIER | PASS | -12.6 pp | REVIEW | AGING | B / LIMITED | EXTERNAL_STALE | VERIFIED |
| Andres Santamarta Roig (`KXATPCHALLENGERMATCH-26NOV03SANCHI-SAN`) | 0.08 / 0.09 (6187) | 8.5% | 21.1% | 15.5% | 17.8% [16.4%-20.3%] | 10.5% | 7.2% | 7.2% | MODEL_LONE_OUTLIER | SHADOW_BET | +12.6 pp | REVIEW | AGING | B / LIMITED | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 1785.0, B 5040.0; serve-point win A 55.8%, B 38.0%; Elo A 1501.0, B 1734.9; model uncertainty 0.0197
* Form inputs: days since last match A 113, B 11; matches on record A 62, B 331; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.007, surface_dev_loose -0.007, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Cammilleri / Reule vs Kovackova / Krejcova -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 20:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T20:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03CAMREUKOVKRE:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cammilleri / Reule (`KXITFWDOUBLES-26NOV03CAMREUKOVKRE-CAMREU`) | 0.01 / 0.94 (11) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kovackova / Krejcova (`KXITFWDOUBLES-26NOV03CAMREUKOVKRE-KOVKRE`) | 0.03 / 0.94 (10) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Aleksandar Amarandei / Bautista Otegui vs Berto / Crivellaro -- M15 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03ALEBAUBERCRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksandar Amarandei / Bautista Otegui (`KXITFDOUBLES-26NOV03ALEBAUBERCRI-ALEBAU`) | 0.15 / 0.42 (30) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Berto / Crivellaro (`KXITFDOUBLES-26NOV03ALEBAUBERCRI-BERCRI`) | 0.50 / 0.82 (11) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Lucas Andrade Da Silva vs Lautaro Midon -- ATP Challenger Costa do Sauipe R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210510:212455:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Andrade Da Silva (`KXATPCHALLENGERMATCH-26NOV03ANDMID-AND`) | 0.32 / 0.33 (8494) | 32.5% | 23.5% | 30.0% | 26.2% [25.2%-27.9%] | 33.6% | 32.4% | -- | INSUFFICIENT_INPUTS | PASS | -9.0 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lautaro Midon (`KXATPCHALLENGERMATCH-26NOV03ANDMID-MID`) | 0.66 / 0.68 (9930) | 67.0% | 76.5% | 70.0% | 73.8% [72.1%-74.8%] | 66.4% | 67.7% | -- | INSUFFICIENT_INPUTS | WATCH | +9.5 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 803.0, B 4609.0; serve-point win A 58.7%, B 35.7%; Elo A 1483.2, B 1677.8; model uncertainty 0.0133
* Form inputs: days since last match A 36, B 8; matches on record A 24, B 274; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.008, surface_dev_loose +0.004, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; EXTERNAL_PRICE_STALE

## De Marchi / Mecarelli vs Battiston / Ferrari -- M15 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03DEMMECBATFER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Battiston / Ferrari (`KXITFDOUBLES-26NOV03DEMMECBATFER-BATFER`) | 0.63 / 0.83 (30) | 73.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| De Marchi / Mecarelli (`KXITFDOUBLES-26NOV03DEMMECBATFER-DEMMEC`) | 0.17 / 0.36 (10) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Ingarao / Marino vs Marigliano / Tartaglione -- M15 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03INGMARMARTAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ingarao / Marino (`KXITFDOUBLES-26NOV03INGMARMARTAR-INGMAR`) | 0.02 / 0.91 (2) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Marigliano / Tartaglione (`KXITFDOUBLES-26NOV03INGMARMARTAR-MARTAR`) | 0.02 / 0.91 (2) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Thiago Monteiro vs Leonardo Storck Franca -- ATP Challenger Costa do Sauipe R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106329:214148:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thiago Monteiro (`KXATPCHALLENGERMATCH-26NOV03MONSTO-MON`) | 0.89 / 0.90 (2044) | 89.5% | 98.5% | 89.2% | 94.1% [93.3%-94.8%] | 87.4% | 90.1% | 90.1% | MODEL_LONE_OUTLIER | PASS | +9.0 pp | NORMAL | AGING | F / POOR | EXTERNAL_STALE | VERIFIED |
| Leonardo Storck Franca (`KXATPCHALLENGERMATCH-26NOV03MONSTO-STO`) | 0.09 / 0.10 (23) | 9.5% | 1.5% | 10.8% | 5.9% [5.1%-6.7%] | 12.6% | 9.6% | 9.6% | MODEL_LONE_OUTLIER | PASS | -8.0 pp | NORMAL | AGING | F / POOR | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 5161.0, B 159.0; serve-point win A 70.1%, B 47.1%; Elo A 1715.7, B 1225.7; model uncertainty 0.0076
* Form inputs: days since last match A 15, B 351; matches on record A 948, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.008, surface_dev_loose +0.002, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Oetzbach / Sperle vs Macchione / Maria Noce -- M15 San Gregorio di Catania R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 21:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03OETSPEMACMAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Macchione / Maria Noce (`KXITFDOUBLES-26NOV03OETSPEMACMAR-MACMAR`) | 0.05 / 0.20 (31) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oetzbach / Sperle (`KXITFDOUBLES-26NOV03OETSPEMACMAR-OETSPE`) | 0.73 / 0.91 (2) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Jaden Weekes vs Daniel De Jonge -- M15 Trois-Rivières R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 21:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T21:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207893:211647:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel De Jonge (`KXITFMATCH-26NOV03WEEDEJ-DEJ`) | 0.94 / 0.96 (580) | 95.0% | 67.3% | 84.3% | 67.0% [60.0%-72.3%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -27.7 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jaden Weekes (`KXITFMATCH-26NOV03WEEDEJ-WEE`) | 0.04 / 0.05 (11) | 4.5% | 32.7% | 15.7% | 33.0% [27.7%-40.0%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | +28.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 553.0, B 1867.0; serve-point win A 61.1%, B 35.3%; Elo A 1299.0, B 1359.3; model uncertainty 0.0615
* Form inputs: days since last match A 463, B 120; matches on record A 34, B 147; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03WEEDEJ-WEE  (YES = Jaden Weekes)
Model: 33%
Kalshi: 4%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.018, surface_dev_loose -0.004, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Michael Antonius / Marcel Latak vs Trey Hilderbrand / Bogdan Pavel -- ATP Challenger Charlottesville R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-03T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03ANTLATHILPAV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Michael Antonius / Marcel Latak (`KXATPCHALLENGERDOUBLES-26NOV03ANTLATHILPAV-ANTLAT`) | 0.16 / 0.21 (51) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Trey Hilderbrand / Bogdan Pavel (`KXATPCHALLENGERDOUBLES-26NOV03ANTLATHILPAV-HILPAV`) | 0.77 / 0.83 (367) | 80.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Justine Hejtmanek / Sucha vs Gniewkowska / Slavikova -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03JUSSUCGNISLA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gniewkowska / Slavikova (`KXITFWDOUBLES-26NOV03JUSSUCGNISLA-GNISLA`) | 0.30 / 0.46 (10) | 38.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Justine Hejtmanek / Sucha (`KXITFWDOUBLES-26NOV03JUSSUCGNISLA-JUSSUC`) | 0.48 / 0.65 (71) | 56.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Lukas / Primorac Pavicic vs Chytilova / Hsu -- W35 Liberec R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 21:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T21:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03LUKPRICHYHSU:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chytilova / Hsu (`KXITFWDOUBLES-26NOV03LUKPRICHYHSU-CHYHSU`) | 0.03 / 0.08 (27) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Lukas / Primorac Pavicic (`KXITFWDOUBLES-26NOV03LUKPRICHYHSU-LUKPRI`) | 0.13 / 0.95 (2) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Valentina Mediorreal Arias vs Julia Riera -- WTA 125K Cali R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-04 01:00Z
* Current expected start: 2026-11-03 22:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-03 21:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA125 (WTA_125) · Clay · scheduled 2026-11-04T01:00:00Z · first ball: NOT_OBSERVED_STARTED (source NO_SOURCE) · match `WTA:220699:260848:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Valentina Mediorreal Arias (`KXWTACHALLENGERMATCH-26NOV03MEDRIE-MED`) | 0.01 / 0.02 (4894) | 1.5% | 3.5% | 6.1% | 7.5% [6.3%-9.6%] | -- | -- | -- | -- | SHADOW_BET | +2.0 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julia Riera (`KXWTACHALLENGERMATCH-26NOV03MEDRIE-RIE`) | 0.98 / 0.99 (47857) | 98.5% | 96.5% | 93.9% | 92.5% [90.4%-93.7%] | -- | -- | -- | -- | PASS | -2.0 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1150.0, B 3855.0; serve-point win A 46.8%, B 39.6%; Elo A 1318.2, B 1722.1; model uncertainty 0.0166
* Form inputs: days since last match A 56, B 3; matches on record A 54, B 389; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose -0.012, surface_dev_tight +0.010
* Warnings: BET_BLOCKED_START_STATUS; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Miguel Bellorio Pinheiro vs Ioan Alexandru Chirita -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03BELCHI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miguel Bellorio Pinheiro (`KXITFMATCH-26NOV03BELCHI-BEL`) | 0.38 / 0.39 (2) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ioan Alexandru Chirita (`KXITFMATCH-26NOV03BELCHI-CHI`) | 0.59 / 0.61 (48) | 60.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Breno Braga vs Henrique Ortenblad Nogueira -- M15 Salvador R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213393:214332:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Breno Braga (`KXITFMATCH-26NOV03BRA2ORT2-BRA2`) | 0.30 / 0.34 (25) | 32.0% | 17.2% | 4.8% | 23.5% [16.1%-30.9%] | 37.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.8 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Henrique Ortenblad Nogueira (`KXITFMATCH-26NOV03BRA2ORT2-ORT2`) | 0.64 / 0.70 (401) | 67.0% | 82.8% | 95.2% | 76.5% [69.1%-83.9%] | 63.0% | -- | -- | INSUFFICIENT_INPUTS | PASS | +15.8 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 636.0, B 375.0; serve-point win A 50.4%, B 42.5%; Elo A 1117.0, B 1252.3; model uncertainty 0.0739
* Form inputs: days since last match A 197, B 197; matches on record A 16, B 7; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03BRA2ORT2-ORT2  (YES = Henrique Ortenblad Nogueira)
Model: 83%
Kalshi: 67%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.008, surface_dev_loose -0.017, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Theodore Dean vs Xavier Massotte -- M15 Trois-Rivières R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03DEAMAS:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theodore Dean (`KXITFMATCH-26NOV03DEAMAS-DEA`) | 0.90 / 0.92 (100) | 91.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xavier Massotte (`KXITFMATCH-26NOV03DEAMAS-MAS`) | 0.09 / 0.10 (0) | 9.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rafael Augusto Garcia Finetto vs Kaua Lorenzo Santos Gava -- M15 Salvador R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211732:214312:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael Augusto Garcia Finetto (`KXITFMATCH-26NOV03GARSAN-GAR`) | 0.08 / 0.10 (21) | 9.0% | 69.4% | 64.3% | 65.3% [64.1%-65.4%] | 13.3% | -- | -- | INSUFFICIENT_INPUTS | PASS | +60.4 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kaua Lorenzo Santos Gava (`KXITFMATCH-26NOV03GARSAN-SAN`) | 0.88 / 0.92 (24) | 90.0% | 30.6% | 35.7% | 34.7% [34.6%-35.9%] | 86.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -59.4 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 92.0, B 50.0; serve-point win A 60.1%, B 43.8%; Elo A 1281.6, B 1174.3; model uncertainty 0.0062
* Form inputs: days since last match A 344, B 463; matches on record A 2, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03GARSAN-GAR  (YES = Rafael Augusto Garcia Finetto)
Model: 69%
Kalshi: 9%
Gap: +60 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Antoine Genereux vs Evan Bynoe -- M15 Trois-Rivières R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03GENBYN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Evan Bynoe (`KXITFMATCH-26NOV03GENBYN-BYN`) | 0.91 / 0.95 (4) | 93.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Antoine Genereux (`KXITFMATCH-26NOV03GENBYN-GEN`) | 0.03 / 0.06 (1) | 4.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marcos Giron vs Dylan Dietrich -- ATP Challenger Charlottesville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106218:210157:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dylan Dietrich (`KXATPCHALLENGERMATCH-26NOV03GIRDIE-DIE`) | 0.64 / 0.65 (4208) | 64.5% | 67.6% | 76.0% | 60.3% [52.5%-68.5%] | 63.1% | 63.7% | 63.4% | MODEL_LONE_OUTLIER | PASS | +3.1 pp | NORMAL | AGING | B / ADEQUATE | ALL_AGREE | VERIFIED |
| Marcos Giron (`KXATPCHALLENGERMATCH-26NOV03GIRDIE-GIR`) | 0.35 / 0.37 (9593) | 36.0% | 32.4% | 24.0% | 39.7% [31.4%-47.5%] | 36.9% | 36.4% | 36.6% | MODEL_LONE_OUTLIER | WATCH | -3.6 pp | NORMAL | AGING | B / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4763.0, B 1719.0; serve-point win A 62.7%, B 33.6%; Elo A 1783.3, B 1715.7; model uncertainty 0.0803
* Form inputs: days since last match A 10, B 8; matches on record A 723, B 71; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.000, surface_dev_loose -0.028, surface_dev_tight +0.024
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Aleksandar Hudjec vs James Quattro -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212891:213606:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aleksandar Hudjec (`KXITFMATCH-26NOV03HUDQUA-HUD`) | 0.05 / 0.06 (5746) | 5.5% | 46.2% | 61.2% | 52.1% [52.1%-52.1%] | -- | -- | -- | -- | PASS | +40.7 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| James Quattro (`KXITFMATCH-26NOV03HUDQUA-QUA`) | 0.94 / 0.95 (16) | 94.5% | 53.8% | 38.8% | 47.9% [47.9%-47.9%] | -- | -- | -- | -- | PASS | -40.7 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 65.0; serve-point win A 59.1%, B 40.2%; Elo A 1223.4, B 1208.0; model uncertainty 0.0001
* Form inputs: days since last match A 540, B 484; matches on record A 2, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03HUDQUA-HUD  (YES = Aleksandar Hudjec)
Model: 46%
Kalshi: 6%
Gap: +41 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Balthazar Huss vs Constantinos Djakouris -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:148672:214268:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Constantinos Djakouris (`KXITFMATCH-26NOV03HUSDJA-DJA`) | 0.92 / 0.93 (2817) | 92.5% | 43.4% | 47.4% | 45.9% [45.9%-45.9%] | -- | -- | -- | -- | PASS | -49.1 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Balthazar Huss (`KXITFMATCH-26NOV03HUSDJA-HUS`) | 0.07 / 0.08 (1503) | 7.5% | 56.6% | 52.6% | 54.1% [54.1%-54.1%] | -- | -- | -- | -- | PASS | +49.1 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 82.0, B 64.0; serve-point win A 60.6%, B 40.6%; Elo A 1223.2, B 1193.5; model uncertainty 0.0
* Form inputs: days since last match A 351, B 526; matches on record A 2, B 4; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03HUSDJA-HUS  (YES = Balthazar Huss)
Model: 57%
Kalshi: 8%
Gap: +49 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Enzo Lima vs Hernando Jose Escurra Isnardi -- M15 Salvador R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200622:211478:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hernando Jose Escurra Isnardi (`KXITFMATCH-26NOV03LIMESC-ESC`) | 0.80 / 0.83 (6) | 81.5% | 51.1% | 52.6% | 55.2% [53.1%-57.2%] | 79.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | -30.4 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Enzo Lima (`KXITFMATCH-26NOV03LIMESC-LIM`) | 0.19 / 0.20 (104) | 19.5% | 48.9% | 47.4% | 44.8% [42.8%-46.9%] | 20.6% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +29.4 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 984.0, B 505.0; serve-point win A 59.5%, B 40.3%; Elo A 1128.6, B 1174.9; model uncertainty 0.0204
* Form inputs: days since last match A 190, B 45; matches on record A 42, B 61; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03LIMESC-LIM  (YES = Enzo Lima)
Model: 49%
Kalshi: 20%
Gap: +29 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.005, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kaue Noatto vs Thomas Enrique Menzel Piccioli -- M15 Salvador R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213613:214207:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thomas Enrique Menzel Piccioli (`KXITFMATCH-26NOV03NOAMEN-MEN`) | 0.49 / 0.57 (8) | 53.0% | 55.8% | 28.5% | 46.9% [45.9%-47.9%] | 52.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | +2.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kaue Noatto (`KXITFMATCH-26NOV03NOAMEN-NOA`) | 0.40 / 0.49 (5) | 44.5% | 44.2% | 71.5% | 53.1% [52.1%-54.1%] | 47.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.3 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 89.0, B 349.0; serve-point win A 59.6%, B 39.3%; Elo A 1194.2, B 1180.9; model uncertainty 0.0103
* Form inputs: days since last match A 288, B 280; matches on record A 3, B 7; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hiroki Sakagawa vs Spencer Papa -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:111509:212243:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Spencer Papa (`KXITFMATCH-26NOV03SAKPAP-PAP`) | 0.34 / 0.35 (791) | 34.5% | 77.7% | 62.9% | 66.3% [66.2%-67.9%] | -- | -- | -- | -- | PASS | +43.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Hiroki Sakagawa (`KXITFMATCH-26NOV03SAKPAP-SAK`) | 0.65 / 0.66 (810) | 65.5% | 22.3% | 37.1% | 33.7% [32.1%-33.8%] | -- | -- | -- | -- | PASS | -43.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 42.0, B 300.0; serve-point win A 54.8%, B 39.4%; Elo A 1202.3, B 1324.7; model uncertainty 0.0085
* Form inputs: days since last match A 351, B 2437; matches on record A 9, B 64; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03SAKPAP-PAP  (YES = Spencer Papa)
Model: 78%
Kalshi: 34%
Gap: +43 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sofia Johnson vs Demi Tran -- W50 Huamantla R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221994:260338:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Johnson (`KXITFWMATCH-26NOV03JOHTRA-JOH`) | 0.96 / 0.97 (4958) | 96.5% | 87.2% | 84.8% | 79.3% [72.2%-84.8%] | -- | -- | -- | -- | PASS | -9.3 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Demi Tran (`KXITFWMATCH-26NOV03JOHTRA-TRA`) | 0.03 / 0.04 (8718) | 3.5% | 12.8% | 15.2% | 20.7% [15.2%-27.8%] | -- | -- | -- | -- | WATCH | +9.3 pp | NORMAL | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1199.0, B 1766.0; serve-point win A 57.7%, B 50.8%; Elo A 1493.3, B 1311.1; model uncertainty 0.0632
* Form inputs: days since last match A 7, B 8; matches on record A 46, B 291; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.011, surface_dev_loose -0.008, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rosario Jurado vs Melissa Boyden -- W15 Neuquén R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03JURBOY:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melissa Boyden (`KXITFWMATCH-26NOV03JURBOY-BOY`) | 0.92 / 0.95 (6) | 93.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rosario Jurado (`KXITFWMATCH-26NOV03JURBOY-JUR`) | 0.03 / 0.07 (167) | 5.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luisana Mondati / Tejada vs Labrana / Vergara Rivera -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03LUITEJLABVER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Labrana / Vergara Rivera (`KXITFWDOUBLES-26NOV03LUITEJLABVER-LABVER`) | 0.92 / 0.98 (6) | 95.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Luisana Mondati / Tejada (`KXITFWDOUBLES-26NOV03LUITEJLABVER-LUITEJ`) | 0.01 / 0.05 (5) | 3.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE

## Isabella Marton vs Cadence Brace -- W50 Huamantla R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223335:260400:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cadence Brace (`KXITFWMATCH-26NOV03MARBRA-BRA`) | 0.96 / 0.97 (5091) | 96.5% | 94.7% | 90.7% | 91.6% [89.8%-93.1%] | -- | -- | -- | -- | PASS | -1.8 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Isabella Marton (`KXITFWMATCH-26NOV03MARBRA-MAR`) | 0.03 / 0.04 (1067) | 3.5% | 5.3% | 9.3% | 8.4% [6.9%-10.2%] | -- | -- | -- | -- | WATCH | +1.8 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1055.0, B 2165.0; serve-point win A 46.8%, B 41.1%; Elo A 1223.0, B 1646.4; model uncertainty 0.0167
* Form inputs: days since last match A 94, B 48; matches on record A 32, B 222; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.004, surface_dev_loose -0.008, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ingrid Carolina Millan Acosta vs Amanda Carolina Nava Elkin -- W50 Huamantla R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216311:222158:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ingrid Carolina Millan Acosta (`KXITFWMATCH-26NOV03MILNAV-MIL`) | 0.96 / 0.97 (3468) | 96.5% | 77.2% | 84.3% | 77.8% [70.4%-83.3%] | -- | -- | -- | -- | PASS | -19.3 pp | HIGH_REVIEW (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Amanda Carolina Nava Elkin (`KXITFWMATCH-26NOV03MILNAV-NAV`) | 0.03 / 0.04 (548) | 3.5% | 22.8% | 15.7% | 22.2% [16.7%-29.6%] | -- | -- | -- | -- | PASS | +19.3 pp | HIGH_REVIEW (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 792.0, B 845.0; serve-point win A 53.6%, B 51.9%; Elo A 1280.9, B 1099.1; model uncertainty 0.0645
* Form inputs: days since last match A 239, B 239; matches on record A 18, B 106; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV03MILNAV-NAV  (YES = Amanda Carolina Nava Elkin)
Model: 23%
Kalshi: 4%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.016, surface_pool_high +0.016, surface_dev_loose +0.012, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zuzanna Pawlikowska vs Annabelle Xu -- W50 Huamantla R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222376:264187:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zuzanna Pawlikowska (`KXITFWMATCH-26NOV03PAWXUX-PAW`) | 0.79 / 0.80 (1) | 79.5% | 76.9% | 50.5% | 62.7% [58.0%-70.4%] | -- | -- | -- | -- | PASS | -2.6 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Annabelle Xu (`KXITFWMATCH-26NOV03PAWXUX-XUX`) | 0.20 / 0.21 (565) | 20.5% | 23.1% | 49.5% | 37.3% [29.6%-42.0%] | -- | -- | -- | -- | WATCH | +2.6 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2671.0, B 722.0; serve-point win A 53.5%, B 52.0%; Elo A 1482.3, B 1347.8; model uncertainty 0.0621
* Form inputs: days since last match A 7, B 97; matches on record A 146, B 43; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.020, surface_pool_high -0.021, surface_dev_loose -0.015, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Simon Padros / Simon Padros vs Grinberg / Nahiara Nappi -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T22:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03SIMSIMGRINAH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Grinberg / Nahiara Nappi (`KXITFWDOUBLES-26NOV03SIMSIMGRINAH-GRINAH`) | -- / 0.94 (10) | -- | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Simon Padros / Simon Padros (`KXITFWDOUBLES-26NOV03SIMSIMGRINAH-SIMSIM`) | 0.02 / 0.94 (10) | 48.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Jesse Flores vs Tarun Karra -- M25 Guadalajara R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:132374:213598:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jesse Flores (`KXITFMATCH-26NOV03FLOKAR-FLO`) | 0.80 / 0.84 (301) | 82.0% | 86.9% | 88.4% | 79.9% [76.2%-84.4%] | -- | -- | -- | -- | PASS | +4.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tarun Karra (`KXITFMATCH-26NOV03FLOKAR-KAR`) | 0.16 / 0.19 (18) | 17.5% | 13.1% | 11.6% | 20.1% [15.6%-23.8%] | -- | -- | -- | -- | PASS | -4.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2047.0, B 201.0; serve-point win A 66.3%, B 42.5%; Elo A 1350.9, B 1125.9; model uncertainty 0.0412
* Form inputs: days since last match A 190, B 232; matches on record A 190, B 8; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.022, surface_pool_high +0.017, surface_dev_loose +0.008, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rodolfo Jauregui Sainz de Rozas vs Stefan Cooper -- M25 Guadalajara R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T22:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106245:138104:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Cooper (`KXITFMATCH-26NOV03JAUCOO-COO`) | 0.50 / 0.54 (198) | 52.0% | 68.7% | 65.1% | 63.2% [62.7%-64.1%] | -- | -- | -- | -- | PASS | +16.7 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rodolfo Jauregui Sainz de Rozas (`KXITFMATCH-26NOV03JAUCOO-JAU`) | 0.47 / 0.48 (100) | 47.5% | 31.3% | 34.9% | 36.8% [35.9%-37.3%] | -- | -- | -- | -- | PASS | -16.2 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 744.0, B 556.0; serve-point win A 61.9%, B 34.2%; Elo A 1123.1, B 1213.5; model uncertainty 0.0071
* Form inputs: days since last match A 190, B 190; matches on record A 34, B 19; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03JAUCOO-COO  (YES = Stefan Cooper)
Model: 69%
Kalshi: 52%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.005, surface_dev_loose -0.004, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexis Galarneau vs Daniel Milavsky -- ATP Challenger Charlottesville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 22:40Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-03T22:40:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200008:212251:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexis Galarneau (`KXATPCHALLENGERMATCH-26NOV03GALMIL-GAL`) | 0.49 / 0.50 (1569) | 49.5% | 56.5% | 36.7% | 45.0% [41.0%-50.5%] | 50.0% | 49.5% | 50.0% | MARKETS_AGREE | PASS | +7.0 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Daniel Milavsky (`KXATPCHALLENGERMATCH-26NOV03GALMIL-MIL`) | 0.50 / 0.51 (1351) | 50.5% | 43.5% | 63.3% | 55.0% [49.5%-59.0%] | 50.0% | 50.3% | 50.0% | MARKETS_AGREE | WATCH | -7.0 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 5304.0, B 3885.0; serve-point win A 63.8%, B 37.5%; Elo A 1674.7, B 1557.6; model uncertainty 0.0473
* Form inputs: days since last match A 8, B 8; matches on record A 438, B 124; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Alberto Odiseo Alvarado Berrospi vs Luis Carlos Alvarez Valdes -- M25 Guadalajara R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208726:211468:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alberto Odiseo Alvarado Berrospi (`KXITFMATCH-26NOV03ALVALV2-ALV`) | 0.05 / 0.06 (190) | 5.5% | 9.4% | 11.2% | 13.0% [10.5%-15.4%] | -- | -- | -- | -- | PASS | +3.9 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luis Carlos Alvarez Valdes (`KXITFMATCH-26NOV03ALVALV2-ALV2`) | 0.93 / 0.96 (31) | 94.5% | 90.6% | 88.8% | 87.0% [84.6%-89.5%] | -- | -- | -- | -- | PASS | -3.9 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 570.0, B 923.0; serve-point win A 54.5%, B 35.3%; Elo A 1107.9, B 1421.8; model uncertainty 0.0246
* Form inputs: days since last match A 337, B 372; matches on record A 63, B 45; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.008, surface_dev_loose +0.001, surface_dev_tight +0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Siwanat Auytayakul vs Ilya Maltsev -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212291:213734:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Siwanat Auytayakul (`KXITFMATCH-26NOV03AUYMAL-AUY`) | 0.81 / 0.84 (185) | 82.5% | 62.2% | 70.9% | 45.4% [43.9%-49.0%] | -- | -- | -- | -- | PASS | -20.3 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ilya Maltsev (`KXITFMATCH-26NOV03AUYMAL-MAL`) | 0.16 / 0.17 (18) | 16.5% | 37.8% | 29.1% | 54.6% [51.0%-56.1%] | -- | -- | -- | -- | PASS | +21.3 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 389.0, B 85.0; serve-point win A 62.6%, B 39.8%; Elo A 1182.7, B 1221.8; model uncertainty 0.0256
* Form inputs: days since last match A 442, B 344; matches on record A 21, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03AUYMAL-MAL  (YES = Ilya Maltsev)
Model: 38%
Kalshi: 16%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Antreas Djakouris vs Linus Rohlin -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03DJAROH:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Antreas Djakouris (`KXITFMATCH-26NOV03DJAROH-DJA`) | 0.91 / 0.92 (137) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Linus Rohlin (`KXITFMATCH-26NOV03DJAROH-ROH`) | 0.07 / 0.09 (2) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Henry Lieberman vs Lucca C Pignaton -- M15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03LIECPI:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucca C Pignaton (`KXITFMATCH-26NOV03LIECPI-CPI`) | 0.02 / 0.75 (100) | 38.5% | 31.2% | -- | -- [-----] | -- | -- | -- | -- | -- | -7.3 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Henry Lieberman (`KXITFMATCH-26NOV03LIECPI-LIE`) | 0.35 / 0.93 (2) | 64.0% | 68.8% | -- | -- [-----] | -- | -- | -- | -- | -- | +4.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 60.3%, B 43.5%; Elo A 1210.8, B 1175.9; model uncertainty None
* Form inputs: days since last match A 190, B 715; matches on record A 18, B 3; data quality F
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## William Mirarchi vs Nicholas Bybel -- M15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03MIRBYB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nicholas Bybel (`KXITFMATCH-26NOV03MIRBYB-BYB`) | 0.02 / 0.91 (2) | 46.5% | 28.3% | -- | -- [-----] | -- | -- | -- | -- | -- | -18.2 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| William Mirarchi (`KXITFMATCH-26NOV03MIRBYB-MIR`) | 0.01 / 0.91 (2) | 46.0% | 71.7% | -- | -- [-----] | -- | -- | -- | -- | -- | +25.7 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 60.1%, B 44.3%; Elo A 1311.5, B 1165.5; model uncertainty None
* Form inputs: days since last match A 316, B 1464; matches on record A 5, B 69; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03MIRBYB-MIR  (YES = William Mirarchi)
Model: 72%
Kalshi: 46%
Gap: +26 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Eduardo Ribeiro vs Luis Guto Miguel -- ATP Challenger Costa do Sauipe R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200495:213036:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Luis Guto Miguel (`KXATPCHALLENGERMATCH-26NOV03RIBMIG-MIG`) | 0.69 / 0.70 (2070) | 69.5% | 55.1% | 56.7% | 47.9% [44.3%-51.0%] | 68.8% | 69.2% | 69.0% | MODEL_LONE_OUTLIER | PASS | -14.4 pp | REVIEW | AGING | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Eduardo Ribeiro (`KXATPCHALLENGERMATCH-26NOV03RIBMIG-RIB`) | 0.30 / 0.31 (18382) | 30.5% | 44.9% | 43.3% | 52.1% [49.0%-55.7%] | 31.2% | 32.0% | 31.6% | MODEL_LONE_OUTLIER | WATCH | +14.4 pp | REVIEW | AGING | B / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3467.0, B 1286.0; serve-point win A 58.5%, B 40.5%; Elo A 1526.8, B 1455.2; model uncertainty 0.0336
* Form inputs: days since last match A 22, B 22; matches on record A 305, B 34; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose -0.005, surface_dev_tight +0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Erik Schiessl vs August Brostroem Poulsen -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03SCHPOU:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| August Brostroem Poulsen (`KXITFMATCH-26NOV03SCHPOU-POU`) | 0.07 / 0.09 (16) | 8.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Erik Schiessl (`KXITFMATCH-26NOV03SCHPOU-SCH`) | 0.88 / 0.92 (188) | 90.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Max Sheldon vs Tyler Lee -- M15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210376:212989:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tyler Lee (`KXITFMATCH-26NOV03SHELEE-LEE`) | 0.33 / 0.37 (173) | 35.0% | 44.0% | 46.9% | 55.2% [55.1%-55.2%] | -- | -- | -- | -- | PASS | +9.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Max Sheldon (`KXITFMATCH-26NOV03SHELEE-SHE`) | 0.62 / 0.65 (140) | 63.5% | 56.0% | 53.1% | 44.8% [44.8%-44.9%] | -- | -- | -- | -- | PASS | -7.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 264.0, B 0.0; serve-point win A 59.3%, B 41.9%; Elo A 1237.2, B 1268.6; model uncertainty 0.0004
* Form inputs: days since last match A 519, B 876; matches on record A 13, B 1; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Elijah Strode vs Guillermo Tunas -- M25 Guadalajara R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210565:213784:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elijah Strode (`KXITFMATCH-26NOV03STRTUN-STR`) | 0.88 / 0.91 (100) | 89.5% | 78.0% | 80.5% | 71.0% [67.8%-76.4%] | -- | -- | -- | -- | PASS | -11.5 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Guillermo Tunas (`KXITFMATCH-26NOV03STRTUN-TUN`) | 0.08 / 0.10 (1) | 9.0% | 22.0% | 19.5% | 29.0% [23.6%-32.2%] | -- | -- | -- | -- | PASS | +13.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 869.0, B 327.0; serve-point win A 68.5%, B 37.7%; Elo A 1301.0, B 1166.9; model uncertainty 0.0432
* Form inputs: days since last match A 477, B 197; matches on record A 57, B 10; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.004, surface_dev_loose +0.007, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Togan Tokac vs Connor Henry Van Schalkwyk -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210227:210485:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Togan Tokac (`KXITFMATCH-26NOV03TOKVAN-TOK`) | 0.51 / 0.53 (49) | 52.0% | 27.9% | 53.1% | 38.8% [36.8%-38.8%] | -- | -- | -- | -- | PASS | -24.1 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Connor Henry Van Schalkwyk (`KXITFMATCH-26NOV03TOKVAN-VAN`) | 0.47 / 0.48 (3) | 47.5% | 72.1% | 46.9% | 61.2% [61.2%-63.2%] | -- | -- | -- | -- | PASS | +24.6 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 53.0, B 56.0; serve-point win A 57.8%, B 37.6%; Elo A 1196.1, B 1282.3; model uncertainty 0.0098
* Form inputs: days since last match A 99, B 162; matches on record A 4, B 14; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03TOKVAN-VAN  (YES = Connor Henry Van Schalkwyk)
Model: 72%
Kalshi: 48%
Gap: +25 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Agudelo / Arabarco vs Sofia Madrid Rocca / Morini -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03AGUARASOFMOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agudelo / Arabarco (`KXITFWDOUBLES-26NOV03AGUARASOFMOR-AGUARA`) | 0.09 / 0.16 (30) | 12.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sofia Madrid Rocca / Morini (`KXITFWDOUBLES-26NOV03AGUARASOFMOR-SOFMOR`) | 0.83 / 0.89 (250) | 86.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Julia Garcia vs Malaika Rapolu -- W50 Huamantla R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222049:222837:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julia Garcia (`KXITFWMATCH-26NOV03GARRAP-GAR`) | 0.08 / 0.09 (16) | 8.5% | 17.4% | 21.5% | 22.3% [21.1%-23.1%] | -- | -- | -- | -- | PASS | +8.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Malaika Rapolu (`KXITFWMATCH-26NOV03GARRAP-RAP`) | 0.89 / 0.91 (1) | 90.0% | 82.6% | 78.5% | 77.7% [76.9%-78.9%] | -- | -- | -- | -- | PASS | -7.4 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 492.0, B 1761.0; serve-point win A 50.2%, B 42.7%; Elo A 1405.9, B 1619.4; model uncertainty 0.0101
* Form inputs: days since last match A 477, B 47; matches on record A 33, B 134; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose -0.000, surface_dev_tight +0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Victoria Jimenez Kasintseva vs Anna-Lena Friedsam -- W75 Petange R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:204431:223286:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anna-Lena Friedsam (`KXITFWMATCH-26NOV03JIMFRI-FRI`) | 0.60 / 0.61 (166) | 60.5% | 45.8% | 42.1% | 45.3% [44.2%-48.4%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -14.7 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Victoria Jimenez Kasintseva (`KXITFWMATCH-26NOV03JIMFRI-JIM`) | 0.39 / 0.40 (29) | 39.5% | 54.2% | 57.9% | 54.7% [51.6%-55.8%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +14.7 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4373.0, B 3834.0; serve-point win A 57.3%, B 43.5%; Elo A 1678.5, B 1702.3; model uncertainty 0.0209
* Form inputs: days since last match A 7, B 22; matches on record A 336, B 669; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.011, surface_dev_loose +0.005, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Emma Kamper vs Isabella Kruger -- W35 Orlando FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221996:241715:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emma Kamper (`KXITFWMATCH-26NOV03KAMKRU-KAM`) | 0.71 / 0.74 (206) | 72.5% | 21.7% | 77.4% | 26.8% [21.8%-32.4%] | -- | -- | -- | -- | PASS | -50.8 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Isabella Kruger (`KXITFWMATCH-26NOV03KAMKRU-KRU`) | 0.27 / 0.28 (137) | 27.5% | 78.3% | 22.6% | 73.2% [67.6%-78.2%] | -- | -- | -- | -- | PASS | +50.8 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 510.0, B 0.0; serve-point win A 48.5%, B 45.7%; Elo A 1345.8, B 1520.0; model uncertainty 0.0529
* Form inputs: days since last match A 365, B 743; matches on record A 33, B 148; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV03KAMKRU-KRU  (YES = Isabella Kruger)
Model: 78%
Kalshi: 28%
Gap: +51 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.050, surface_pool_high +0.056, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Misa Malkin vs Sofia Avataneo -- W50 Huamantla R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222509:242450:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sofia Avataneo (`KXITFWMATCH-26NOV03MALAVA-AVA`) | 0.11 / 0.13 (1155) | 12.0% | 14.2% | 10.4% | 19.1% [13.6%-26.9%] | -- | -- | -- | -- | PASS | +2.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Misa Malkin (`KXITFWMATCH-26NOV03MALAVA-MAL`) | 0.87 / 0.89 (255) | 88.0% | 85.8% | 89.6% | 80.9% [73.2%-86.4%] | -- | -- | -- | -- | PASS | -2.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 892.0, B 821.0; serve-point win A 53.8%, B 54.2%; Elo A 1364.5, B 1178.7; model uncertainty 0.0664
* Form inputs: days since last match A 239, B 190; matches on record A 39, B 143; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.007, surface_pool_high +0.004, surface_dev_loose +0.014, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Moyano / Romero vs Pajello / Delfina Vega Gudino -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03MOYROMPAJDEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Moyano / Romero (`KXITFWDOUBLES-26NOV03MOYROMPAJDEL-MOYROM`) | 0.92 / 0.95 (32) | 93.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Pajello / Delfina Vega Gudino (`KXITFWDOUBLES-26NOV03MOYROMPAJDEL-PAJDEL`) | 0.03 / 0.05 (124) | 4.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Sobolieva / Weckerle vs Morderger / Morderger -- W75 Petange R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T23:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03SOBWECMORMOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Morderger / Morderger (`KXITFWDOUBLES-26NOV03SOBWECMORMOR-MORMOR`) | 0.28 / 0.40 (1) | 34.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sobolieva / Weckerle (`KXITFWDOUBLES-26NOV03SOBWECMORMOR-SOBWEC`) | 0.56 / 0.69 (250) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Max Hans Rehberg vs Trevor Svajda -- ATP Challenger Charlottesville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-03T23:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208819:212216:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Max Hans Rehberg (`KXATPCHALLENGERMATCH-26NOV03REHSVA-REH`) | 0.59 / 0.60 (1076) | 59.5% | 56.0% | 63.8% | 59.0% [56.0%-62.4%] | 59.9% | 60.5% | 60.5% | MODEL_LONE_OUTLIER | PASS | -3.5 pp | NORMAL | AGING | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |
| Trevor Svajda (`KXATPCHALLENGERMATCH-26NOV03REHSVA-SVA`) | 0.39 / 0.40 (5) | 39.5% | 44.0% | 36.1% | 41.0% [37.6%-44.0%] | 40.1% | 39.9% | 39.9% | MODEL_LONE_OUTLIER | PASS | +4.5 pp | NORMAL | AGING | B / ADEQUATE | EXTERNAL_STALE | VERIFIED |

* Serve evidence (points): A 3984.0, B 1651.0; serve-point win A 63.1%, B 38.1%; Elo A 1604.4, B 1573.1; model uncertainty 0.0319
* Form inputs: days since last match A 8, B 15; matches on record A 260, B 90; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.034, surface_pool_high -0.030, surface_dev_loose +0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE

## Maxwell Benson vs Carlo Arena Fava -- M25 Guadalajara R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03BENARE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carlo Arena Fava (`KXITFMATCH-26NOV03BENARE-ARE`) | 0.40 / 0.42 (7) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Maxwell Benson (`KXITFMATCH-26NOV03BENARE-BEN`) | 0.57 / 0.61 (132) | 59.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tiago Pires vs Antoine Clavel -- M15 Trois-Rivières R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03PIRCLA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Antoine Clavel (`KXITFMATCH-26NOV03PIRCLA-CLA`) | 0.09 / 0.12 (30) | 10.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tiago Pires (`KXITFMATCH-26NOV03PIRCLA-PIR`) | 0.88 / 0.90 (375) | 89.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alan Fernando Rubio Fierros vs Emilio Bravo -- M25 Guadalajara R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03RUBBRA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Emilio Bravo (`KXITFMATCH-26NOV03RUBBRA-BRA`) | 0.08 / 0.09 (2034) | 8.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alan Fernando Rubio Fierros (`KXITFMATCH-26NOV03RUBBRA-RUB`) | 0.91 / 0.93 (190) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Liam Spiers vs Viktor Markov -- M15 Trois-Rivières R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-03T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210722:213574:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Viktor Markov (`KXITFMATCH-26NOV03SPIMAR-MAR`) | 0.86 / 0.91 (101) | 88.5% | 66.0% | 30.5% | 50.0% [50.0%-50.0%] | -- | -- | -- | -- | PASS | -22.5 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Liam Spiers (`KXITFMATCH-26NOV03SPIMAR-SPI`) | 0.11 / 0.13 (28) | 12.0% | 34.0% | 69.5% | 50.0% [50.0%-50.0%] | -- | -- | -- | -- | PASS | +22.0 pp | HIGH_REVIEW (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 549.0; serve-point win A 56.8%, B 40.1%; Elo A 1264.4, B 1261.4; model uncertainty 0.0
* Form inputs: days since last match A 757, B 351; matches on record A 1, B 23; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03SPIMAR-SPI  (YES = Liam Spiers)
Model: 34%
Kalshi: 12%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Giordano / Hrda vs Castillo Meza / Odorizzi -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03GIOHRDCASODO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Castillo Meza / Odorizzi (`KXITFWDOUBLES-26NOV03GIOHRDCASODO-CASODO`) | 0.44 / 0.57 (250) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Giordano / Hrda (`KXITFWDOUBLES-26NOV03GIOHRDCASODO-GIOHRD`) | 0.41 / 0.51 (51) | 46.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Gomez Pezuela Cano / Tikhonova vs Chan / Hinojosa Gomez -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-03T23:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03GOMTIKCHAHIN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chan / Hinojosa Gomez (`KXITFWDOUBLES-26NOV03GOMTIKCHAHIN-CHAHIN`) | 0.32 / 0.48 (250) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gomez Pezuela Cano / Tikhonova (`KXITFWDOUBLES-26NOV03GOMTIKCHAHIN-GOMTIK`) | 0.51 / 0.61 (64) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Harry Wendelken vs Andres Andrade -- ATP Challenger Charlottesville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:50Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-03T23:50:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200748:207784:2026-11-03`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andres Andrade (`KXATPCHALLENGERMATCH-26NOV03WENAND-AND`) | 0.47 / 0.48 (204) | 47.5% | 51.1% | 41.7% | 43.8% [41.2%-49.0%] | 46.9% | 47.7% | 47.3% | MARKETS_AGREE | PASS | +3.6 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Harry Wendelken (`KXATPCHALLENGERMATCH-26NOV03WENAND-WEN`) | 0.52 / 0.53 (1534) | 52.5% | 48.9% | 58.3% | 56.2% [51.0%-58.8%] | 53.1% | 53.1% | 53.1% | MARKETS_AGREE | WATCH | -3.6 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 4155.0, B 4704.0; serve-point win A 57.9%, B 41.9%; Elo A 1636.1, B 1638.6; model uncertainty 0.0389
* Form inputs: days since last match A 8, B 8; matches on record A 317, B 302; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.021, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Matthew Segura vs Gregoire Delattre -- M15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:53Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T23:53:35Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03SEGDEL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gregoire Delattre (`KXITFMATCH-26NOV03SEGDEL-DEL`) | 0.02 / 0.80 (100) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Matthew Segura (`KXITFMATCH-26NOV03SEGDEL-SEG`) | 0.34 / 0.91 (5) | 62.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## James Weber vs Anuj Watane -- M15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-03 23:53Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-03T23:53:35Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03WEBWAT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anuj Watane (`KXITFMATCH-26NOV03WEBWAT-WAT`) | 0.03 / 0.91 (2) | 47.0% | 49.8% | -- | -- [-----] | -- | -- | -- | -- | -- | +2.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| James Weber (`KXITFMATCH-26NOV03WEBWAT-WEB`) | 0.01 / 0.89 (4) | 45.0% | 50.2% | -- | -- [-----] | -- | -- | -- | -- | -- | +5.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 58.8%, B 41.3%; Elo A 1259.9, B 1253.6; model uncertainty None
* Form inputs: days since last match A 449, B 232; matches on record A 1, B 1; data quality F
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Achurra Correa / Bechtlufft Cardoso vs Adesalu / Wriedt -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03ACHBECADEWRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Achurra Correa / Bechtlufft Cardoso (`KXITFDOUBLES-26NOV03ACHBECADEWRI-ACHBEC`) | 0.04 / 0.89 (2) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Adesalu / Wriedt (`KXITFDOUBLES-26NOV03ACHBECADEWRI-ADEWRI`) | 0.04 / 0.89 (2) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Blu Baker vs Oswaldo Alejandro Reyes Tirado -- M25 Guadalajara R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209124:213783:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Blu Baker (`KXITFMATCH-26NOV03BAKREY-BAK`) | 0.83 / 0.86 (170) | 84.5% | 76.8% | 86.1% | 72.2% [68.6%-76.9%] | -- | -- | -- | -- | PASS | -7.7 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oswaldo Alejandro Reyes Tirado (`KXITFMATCH-26NOV03BAKREY-REY`) | 0.14 / 0.15 (190) | 14.5% | 23.2% | 13.9% | 27.8% [23.1%-31.4%] | -- | -- | -- | -- | PASS | +8.7 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1707.0, B 411.0; serve-point win A 60.9%, B 44.7%; Elo A 1343.1, B 1216.0; model uncertainty 0.0418
* Form inputs: days since last match A 204, B 190; matches on record A 119, B 9; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.026, surface_pool_high -0.027, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mateo Barreiros Reyes vs Julian Cundom -- M15 Salvador R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-04T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207595:208424:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mateo Barreiros Reyes (`KXITFMATCH-26NOV03BARCUN-BAR`) | 0.55 / 0.56 (18) | 55.5% | 66.8% | 58.9% | 63.5% [60.5%-69.1%] | -- | -- | -- | -- | PASS | +11.3 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Julian Cundom (`KXITFMATCH-26NOV03BARCUN-CUN`) | 0.43 / 0.45 (114) | 44.0% | 33.2% | 41.1% | 36.5% [30.9%-39.5%] | -- | -- | -- | -- | PASS | -10.8 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1996.0, B 948.0; serve-point win A 57.7%, B 45.6%; Elo A 1320.5, B 1203.3; model uncertainty 0.0431
* Form inputs: days since last match A 498, B 148; matches on record A 128, B 49; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.029, surface_pool_high -0.030, surface_dev_loose +0.010, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Chin / Mallory vs Gurenko / Peter Van Noord -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03CHIMALGURPET:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chin / Mallory (`KXITFDOUBLES-26NOV03CHIMALGURPET-CHIMAL`) | 0.04 / 0.89 (2) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Gurenko / Peter Van Noord (`KXITFDOUBLES-26NOV03CHIMALGURPET-GURPET`) | 0.04 / 0.89 (2) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Rafael De Alba vs Nicolas Esteban Rico Arias -- M25 Guadalajara R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208381:208908:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rafael De Alba (`KXITFMATCH-26NOV03DEARIC-DEA`) | 0.78 / 0.79 (161) | 78.5% | 70.5% | 48.9% | 62.1% [59.0%-66.3%] | -- | -- | -- | -- | PASS | -8.0 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicolas Esteban Rico Arias (`KXITFMATCH-26NOV03DEARIC-RIC`) | 0.20 / 0.21 (31) | 20.5% | 29.5% | 51.1% | 38.0% [33.7%-41.0%] | -- | -- | -- | -- | PASS | +9.0 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1439.0, B 684.0; serve-point win A 56.8%, B 47.3%; Elo A 1191.5, B 1064.7; model uncertainty 0.0367
* Form inputs: days since last match A 190, B 190; matches on record A 35, B 20; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.005, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oscar Jose Gutierrez vs Manuel Mouilleron Salvo -- M15 Salvador R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-04T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:121264:211389:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oscar Jose Gutierrez (`KXITFMATCH-26NOV03GUTMOU-GUT`) | 0.89 / 0.90 (651) | 89.5% | 80.8% | 63.4% | 76.9% [73.6%-78.7%] | -- | -- | -- | -- | PASS | -8.7 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Manuel Mouilleron Salvo (`KXITFMATCH-26NOV03GUTMOU-MOU`) | 0.10 / 0.13 (2241) | 11.5% | 19.2% | 36.6% | 23.1% [21.3%-26.4%] | -- | -- | -- | -- | WATCH | +7.7 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2766.0, B 690.0; serve-point win A 60.8%, B 45.8%; Elo A 1315.8, B 1058.9; model uncertainty 0.0255
* Form inputs: days since last match A 204, B 190; matches on record A 606, B 48; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high -0.000, surface_dev_loose +0.004, surface_dev_tight -0.008
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Krishna / Sakagawa vs Foster / Jeff Planinsek -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03KRISAKFOSJEF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Foster / Jeff Planinsek (`KXITFDOUBLES-26NOV03KRISAKFOSJEF-FOSJEF`) | 0.04 / 0.89 (2) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Krishna / Sakagawa (`KXITFDOUBLES-26NOV03KRISAKFOSJEF-KRISAK`) | 0.04 / 0.89 (2) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mintz / Zielinski vs Mercier / Aubriel Ngounoue -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03MINZIEMERAUB:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mercier / Aubriel Ngounoue (`KXITFDOUBLES-26NOV03MINZIEMERAUB-MERAUB`) | 0.68 / 0.79 (2) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Mintz / Zielinski (`KXITFDOUBLES-26NOV03MINZIEMERAUB-MINZIE`) | 0.05 / 0.27 (1) | 16.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Raphael Perot vs Hunter Heck -- M25 Harlingen TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209067:212222:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hunter Heck (`KXITFMATCH-26NOV03PERHEC-HEC`) | 0.28 / 0.30 (2) | 29.0% | 43.6% | 41.6% | 41.1% [39.6%-43.2%] | -- | -- | -- | -- | WATCH | +14.6 pp | REVIEW | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Raphael Perot (`KXITFMATCH-26NOV03PERHEC-PER`) | 0.69 / 0.70 (83) | 69.5% | 56.4% | 58.4% | 58.9% [56.8%-60.4%] | -- | -- | -- | -- | PASS | -13.1 pp | REVIEW | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2367.0, B 1168.0; serve-point win A 57.7%, B 43.5%; Elo A 1518.3, B 1455.7; model uncertainty 0.0181
* Form inputs: days since last match A 36, B 50; matches on record A 86, B 63; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.021, surface_pool_high +0.015, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sebastian Dominguez Collado / Gomez Osorio vs Bilicic / Sachdev -- M15 Pembroke R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03SEBGOMBILSAC:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bilicic / Sachdev (`KXITFDOUBLES-26NOV03SEBGOMBILSAC-BILSAC`) | 0.04 / 0.89 (2) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sebastian Dominguez Collado / Gomez Osorio (`KXITFDOUBLES-26NOV03SEBGOMBILSAC-SEBGOM`) | 0.04 / 0.89 (2) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Quinn Vandecasteele vs Bryce Nakashima Nakashima -- M25 Harlingen TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 00:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209088:210416:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bryce Nakashima Nakashima (`KXITFMATCH-26NOV03VANNAK-NAK`) | 0.54 / 0.57 (230) | 55.5% | 24.9% | 34.5% | 26.4% [25.2%-28.1%] | -- | -- | -- | -- | PASS | -30.6 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Quinn Vandecasteele (`KXITFMATCH-26NOV03VANNAK-VAN`) | 0.41 / 0.42 (43) | 41.5% | 75.1% | 65.5% | 73.6% [71.9%-74.8%] | -- | -- | -- | -- | PASS | +33.6 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 3610.0, B 491.0; serve-point win A 63.0%, B 42.2%; Elo A 1502.8, B 1302.9; model uncertainty 0.0147
* Form inputs: days since last match A 71, B 8; matches on record A 165, B 47; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03VANNAK-VAN  (YES = Quinn Vandecasteele)
Model: 75%
Kalshi: 42%
Gap: +34 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.004, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Bianca Bulgaru / Lim vs Capurro Taborda / Colmegna -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03BIALIMCAPCOL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bianca Bulgaru / Lim (`KXITFWDOUBLES-26NOV03BIALIMCAPCOL-BIALIM`) | 0.28 / 0.35 (38) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Capurro Taborda / Colmegna (`KXITFWDOUBLES-26NOV03BIALIMCAPCOL-CAPCOL`) | 0.58 / 0.69 (3) | 63.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Danilova / Belen Moron vs Doldan / Celina Sosa -- W15 Neuquén R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03DANBELDOLCEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Danilova / Belen Moron (`KXITFWDOUBLES-26NOV03DANBELDOLCEL-DANBEL`) | 0.39 / 0.46 (46) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Doldan / Celina Sosa (`KXITFWDOUBLES-26NOV03DANBELDOLCEL-DOLCEL`) | 0.51 / 0.58 (77) | 54.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Fouad / Kuhl vs Eisch / Eisch -- W35 Orlando FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 00:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T00:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03FOUKUHEISEIS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eisch / Eisch (`KXITFWDOUBLES-26NOV03FOUKUHEISEIS-EISEIS`) | 0.05 / 0.89 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fouad / Kuhl (`KXITFWDOUBLES-26NOV03FOUKUHEISEIS-FOUKUH`) | 0.05 / 0.89 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## James Kent Trotter vs Michael Zheng -- ATP Challenger Charlottesville R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 00:20Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-04T00:20:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208801:210116:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Kent Trotter (`KXATPCHALLENGERMATCH-26NOV03TROZHE-TRO`) | 0.25 / 0.26 (18642) | 25.5% | 6.9% | 35.7% | 19.6% [15.5%-24.9%] | -- | -- | -- | -- | PASS | -18.6 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Michael Zheng (`KXATPCHALLENGERMATCH-26NOV03TROZHE-ZHE`) | 0.75 / 0.76 (1934) | 75.5% | 93.1% | 64.3% | 80.4% [75.1%-84.5%] | -- | -- | -- | -- | PASS | +17.6 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 223.0, B 3505.0; serve-point win A 57.1%, B 31.1%; Elo A 1506.0, B 1772.6; model uncertainty 0.0472
* Form inputs: days since last match A 232, B 27; matches on record A 28, B 141; data quality D

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV03TROZHE-ZHE  (YES = Michael Zheng)
Model: 93%
Kalshi: 76%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.027, surface_pool_high +0.021, surface_dev_loose +0.004, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE

## Serafima Elizarova vs Ireland O'Brien -- W15 Hilton Head Island SC R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 00:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T00:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03ELIOBR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Serafima Elizarova (`KXITFWMATCH-26NOV03ELIOBR-ELI`) | 0.08 / 0.92 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ireland O'Brien (`KXITFWMATCH-26NOV03ELIOBR-OBR`) | 0.09 / 0.92 (1) | 50.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alexandru Chirita / Velcz vs Alvares De Castro Rocha / Huss -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03ALEVELALVHUS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexandru Chirita / Velcz (`KXITFDOUBLES-26NOV03ALEVELALVHUS-ALEVEL`) | 0.75 / 0.90 (1) | 82.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alvares De Castro Rocha / Huss (`KXITFDOUBLES-26NOV03ALEVELALVHUS-ALVHUS`) | 0.04 / 0.18 (30) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Marco Cecchinato vs Francisco Comesana -- ATP Challenger Costa do Sauipe R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-04T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106065:207681:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marco Cecchinato (`KXATPCHALLENGERMATCH-26NOV03CECCOM-CEC`) | 0.31 / 0.32 (6374) | 31.5% | 33.9% | 48.5% | 45.5% [41.0%-47.0%] | -- | -- | -- | -- | SHADOW_BET | +2.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Francisco Comesana (`KXATPCHALLENGERMATCH-26NOV03CECCOM-COM`) | 0.69 / 0.70 (4174) | 69.5% | 66.1% | 51.5% | 54.5% [53.0%-59.0%] | -- | -- | -- | -- | PASS | -3.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5742.0, B 5246.0; serve-point win A 61.6%, B 35.1%; Elo A 1685.2, B 1804.3; model uncertainty 0.0298
* Form inputs: days since last match A 15, B 15; matches on record A 995, B 465; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.020, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Chunduru / Chunduru vs Azais / Rendon -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03CHUCHUAZAREN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Azais / Rendon (`KXITFDOUBLES-26NOV03CHUCHUAZAREN-AZAREN`) | 0.09 / 0.84 (250) | 46.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Chunduru / Chunduru (`KXITFDOUBLES-26NOV03CHUCHUAZAREN-CHUCHU`) | 0.14 / 0.89 (250) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Federico Coria vs Ivan Dreycopp -- ATP Challenger Villa Maria R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-04T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105948:210403:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Federico Coria (`KXATPCHALLENGERMATCH-26NOV03CORDRE-COR`) | 0.77 / 0.78 (1386) | 77.5% | 95.1% | 84.4% | 93.6% [92.2%-94.8%] | -- | -- | -- | -- | PASS | +17.6 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ivan Dreycopp (`KXATPCHALLENGERMATCH-26NOV03CORDRE-DRE`) | 0.22 / 0.23 (1907) | 22.5% | 4.9% | 15.6% | 6.4% [5.2%-7.8%] | -- | -- | -- | -- | PASS | -17.6 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3047.0, B 293.0; serve-point win A 63.9%, B 48.8%; Elo A 1695.4, B 1189.4; model uncertainty 0.0131
* Form inputs: days since last match A 8, B 253; matches on record A 1069, B 10; data quality D

```
DISCREPANCY SANITY CHECK  KXATPCHALLENGERMATCH-26NOV03CORDRE-COR  (YES = Federico Coria)
Model: 95%
Kalshi: 78%
Gap: +18 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.012, surface_dev_loose +0.003, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Facundo Diaz Acosta vs Matheus Pucinelli de Almeida -- ATP Challenger Costa do Sauipe R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-04T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207680:207799:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Facundo Diaz Acosta (`KXATPCHALLENGERMATCH-26NOV03DIAPDA-DIA`) | 0.61 / 0.62 (1342) | 61.5% | 63.9% | 60.8% | 63.2% [61.7%-64.7%] | -- | -- | -- | -- | WATCH | +2.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matheus Pucinelli de Almeida (`KXATPCHALLENGERMATCH-26NOV03DIAPDA-PDA`) | 0.39 / 0.40 (5491) | 39.5% | 36.1% | 39.2% | 36.8% [35.3%-38.3%] | -- | -- | -- | -- | PASS | -3.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5488.0, B 5105.0; serve-point win A 60.8%, B 41.9%; Elo A 1835.0, B 1673.8; model uncertainty 0.0147
* Form inputs: days since last match A 13, B 15; matches on record A 468, B 414; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.010, surface_dev_loose +0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Ritesh Patil vs Bor Artnak -- M25 Harlingen TX R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210107:212541:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bor Artnak (`KXITFMATCH-26NOV03PATART-ART`) | 0.91 / 0.93 (100) | 92.0% | 87.9% | 70.5% | 79.9% [78.4%-81.9%] | -- | -- | -- | -- | PASS | -4.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ritesh Patil (`KXITFMATCH-26NOV03PATART-PAT`) | 0.06 / 0.10 (1112) | 8.0% | 12.1% | 29.5% | 20.1% [18.1%-21.6%] | -- | -- | -- | -- | PASS | +4.1 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 76.0, B 3186.0; serve-point win A 53.5%, B 37.6%; Elo A 1224.6, B 1469.8; model uncertainty 0.0173
* Form inputs: days since last match A 484, B 46; matches on record A 5, B 251; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.015, surface_dev_loose -0.001, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nikolas Sanchez Izquierdo vs Camilo Ugo Carabelli -- ATP Challenger Costa do Sauipe R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 01:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-04T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200116:207663:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nikolas Sanchez Izquierdo (`KXATPCHALLENGERMATCH-26NOV03SAIUGO-SAI`) | 0.38 / 0.39 (5347) | 38.5% | 43.6% | 61.3% | 52.6% [45.3%-56.7%] | -- | -- | -- | -- | SHADOW_BET | +5.1 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Camilo Ugo Carabelli (`KXATPCHALLENGERMATCH-26NOV03SAIUGO-UGO`) | 0.61 / 0.62 (120) | 61.5% | 56.4% | 38.7% | 47.4% [43.3%-54.7%] | -- | -- | -- | -- | PASS | -5.1 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5109.0, B 5218.0; serve-point win A 58.2%, B 40.6%; Elo A 1664.6, B 1854.3; model uncertainty 0.057
* Form inputs: days since last match A 15, B 8; matches on record A 582, B 655; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE

## Brace / Xu vs Fernanda Navarro / Pawlikowska -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03BRAXUXFERPAW:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brace / Xu (`KXITFWDOUBLES-26NOV03BRAXUXFERPAW-BRAXUX`) | 0.19 / 0.34 (37) | 26.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fernanda Navarro / Pawlikowska (`KXITFWDOUBLES-26NOV03BRAXUXFERPAW-FERPAW`) | 0.59 / 0.78 (113) | 68.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Rapolu / Sholokhova vs Cherubini / Johnson -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03RAPSHOCHEJOH:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cherubini / Johnson (`KXITFWDOUBLES-26NOV03RAPSHOCHEJOH-CHEJOH`) | 0.09 / 0.89 (250) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rapolu / Sholokhova (`KXITFWDOUBLES-26NOV03RAPSHOCHEJOH-RAPSHO`) | 0.09 / 0.89 (250) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Rodriguez / Tran vs Alessia Monteleone / Montiel -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 01:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T01:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03RODTRAALEMON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessia Monteleone / Montiel (`KXITFWDOUBLES-26NOV03RODTRAALEMON-ALEMON`) | 0.05 / 0.06 (26) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rodriguez / Tran (`KXITFWDOUBLES-26NOV03RODTRAALEMON-RODTRA`) | 0.88 / 0.95 (156) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Fernandes / David Verdes vs Barrett / Wessels -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03FERDAVBARWES:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Barrett / Wessels (`KXITFDOUBLES-26NOV03FERDAVBARWES-BARWES`) | 0.17 / 0.26 (31) | 21.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Fernandes / David Verdes (`KXITFDOUBLES-26NOV03FERDAVBARWES-FERDAV`) | 0.67 / 0.80 (250) | 73.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Marko Mesarovic vs Mikael Arseneault -- M15 Trois-Rivières R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211670:212530:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mikael Arseneault (`KXITFMATCH-26NOV03MESARS-ARS`) | 0.55 / 0.58 (225) | 56.5% | 50.1% | 22.2% | 44.3% [36.8%-51.0%] | -- | -- | -- | -- | PASS | -6.4 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Marko Mesarovic (`KXITFMATCH-26NOV03MESARS-MES`) | 0.41 / 0.43 (100) | 42.0% | 49.9% | 77.8% | 55.7% [49.0%-63.2%] | -- | -- | -- | -- | PASS | +7.9 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 489.0, B 759.0; serve-point win A 59.4%, B 40.6%; Elo A 1238.1, B 1251.9; model uncertainty 0.0713
* Form inputs: days since last match A 269, B 106; matches on record A 18, B 33; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.010, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Laskevich / Mamedova vs Bartashevich / Kamper -- W35 Orlando FL R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 01:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T01:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03LASMAMBARKAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bartashevich / Kamper (`KXITFWDOUBLES-26NOV03LASMAMBARKAM-BARKAM`) | 0.09 / 0.88 (250) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Laskevich / Mamedova (`KXITFWDOUBLES-26NOV03LASMAMBARKAM-LASMAM`) | 0.10 / 0.90 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Felipe Badaro vs Joao Vitor Scramin do Lago -- M15 Salvador R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03BADSCR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felipe Badaro (`KXITFMATCH-26NOV03BADSCR-BAD`) | 0.06 / 0.09 (1833) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Joao Vitor Scramin do Lago (`KXITFMATCH-26NOV03BADSCR-SCR`) | 0.90 / 0.93 (5) | 91.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ryan Cozad vs Duje Markovina -- M15 Hilton Head Island SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212064:213743:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryan Cozad (`KXITFMATCH-26NOV03COZMAR-COZ`) | 0.39 / 0.40 (41) | 39.5% | 38.2% | 62.1% | 51.0% [50.0%-52.0%] | -- | -- | -- | -- | PASS | -1.3 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Duje Markovina (`KXITFMATCH-26NOV03COZMAR-MAR`) | 0.57 / 0.59 (101) | 58.0% | 61.8% | 37.9% | 49.0% [47.9%-50.0%] | -- | -- | -- | -- | PASS | +3.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 157.0, B 1318.0; serve-point win A 59.7%, B 37.9%; Elo A 1228.1, B 1228.3; model uncertainty 0.0102
* Form inputs: days since last match A 204, B 204; matches on record A 3, B 38; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vignesh Gogineni vs Kai Thompson -- M15 Hilton Head Island SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213987:214142:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vignesh Gogineni (`KXITFMATCH-26NOV03GOGTHO-GOG`) | 0.80 / 0.81 (100) | 80.5% | 81.1% | 81.2% | 71.2% [69.7%-74.8%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kai Thompson (`KXITFMATCH-26NOV03GOGTHO-THO`) | 0.17 / 0.19 (12) | 18.0% | 18.9% | 18.8% | 28.8% [25.2%-30.3%] | -- | -- | -- | -- | PASS | +0.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 277.0, B 164.0; serve-point win A 62.2%, B 44.6%; Elo A 1402.2, B 1255.5; model uncertainty 0.0253
* Form inputs: days since last match A 84, B 302; matches on record A 6, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Noah Lopez Cherubino vs Vihaan Reddy -- M15 Hilton Head Island SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212106:214247:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Noah Lopez Cherubino (`KXITFMATCH-26NOV03LOPRED-LOP`) | 0.61 / 0.64 (76) | 62.5% | 59.8% | 48.4% | 51.5% [51.0%-52.1%] | -- | -- | -- | -- | PASS | -2.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vihaan Reddy (`KXITFMATCH-26NOV03LOPRED-RED`) | 0.36 / 0.38 (230) | 37.0% | 40.2% | 51.5% | 48.4% [47.9%-49.0%] | -- | -- | -- | -- | PASS | +3.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 888.0, B 276.0; serve-point win A 60.7%, B 41.2%; Elo A 1229.1, B 1217.9; model uncertainty 0.0052
* Form inputs: days since last match A 351, B 204; matches on record A 16, B 4; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Brandon Perez vs Matteo Covato -- M25 Guadalajara R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149145:207738:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Covato (`KXITFMATCH-26NOV03PERCOV-COV`) | 0.63 / 0.64 (156) | 63.5% | 57.3% | 63.9% | 61.6% [59.8%-63.9%] | -- | -- | -- | -- | PASS | -6.2 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Brandon Perez (`KXITFMATCH-26NOV03PERCOV-PER`) | 0.37 / 0.38 (357) | 37.5% | 42.7% | 36.0% | 38.4% [36.1%-40.2%] | -- | -- | -- | -- | PASS | +5.2 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1426.0, B 2229.0; serve-point win A 64.5%, B 34.0%; Elo A 1018.4, B 1088.3; model uncertainty 0.0203
* Form inputs: days since last match A 183, B 183; matches on record A 100, B 72; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.009, surface_dev_loose +0.001, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Matias Soto vs Frazier Rengifo -- M25 Guadalajara R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200105:207130:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Frazier Rengifo (`KXITFMATCH-26NOV03SOTREN-REN`) | 0.15 / 0.18 (742) | 16.5% | 16.4% | 29.2% | 22.5% [16.9%-27.5%] | -- | -- | -- | -- | PASS | -0.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Matias Soto (`KXITFMATCH-26NOV03SOTREN-SOT`) | 0.83 / 0.84 (189) | 83.5% | 83.6% | 70.8% | 77.5% [72.5%-83.1%] | -- | -- | -- | -- | PASS | +0.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4186.0, B 468.0; serve-point win A 62.8%, B 44.8%; Elo A 1466.8, B 1234.6; model uncertainty 0.0529
* Form inputs: days since last match A 15, B 190; matches on record A 288, B 29; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.044, surface_pool_high -0.049, surface_dev_loose -0.005, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniel Uta vs Dragos Cazacu -- M15 Hilton Head Island SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03UTACAZ:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dragos Cazacu (`KXITFMATCH-26NOV03UTACAZ-CAZ`) | 0.63 / 0.69 (133) | 66.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Daniel Uta (`KXITFMATCH-26NOV03UTACAZ-UTA`) | 0.29 / 0.35 (220) | 32.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Avataneo / Harvey vs Oz / Tona -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03AVAHAROZXTON:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Avataneo / Harvey (`KXITFWDOUBLES-26NOV03AVAHAROZXTON-AVAHAR`) | 0.05 / 0.06 (26) | 5.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Oz / Tona (`KXITFWDOUBLES-26NOV03AVAHAROZXTON-OZXTON`) | 0.11 / 0.94 (2) | 52.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Petja Drame vs Scarlett Fagan -- W15 Hilton Head Island SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223337:270087:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Petja Drame (`KXITFWMATCH-26NOV03DRAFAG-DRA`) | 0.24 / 0.25 (80) | 24.5% | 57.4% | 54.3% | 58.5% [58.5%-59.6%] | -- | -- | -- | -- | PASS | +32.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Scarlett Fagan (`KXITFWMATCH-26NOV03DRAFAG-FAG`) | 0.75 / 0.76 (182) | 75.5% | 42.6% | 45.7% | 41.5% [40.5%-41.5%] | -- | -- | -- | -- | PASS | -32.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 254.0, B 210.0; serve-point win A 53.3%, B 48.1%; Elo A 1342.5, B 1277.8; model uncertainty 0.0053
* Form inputs: days since last match A 456, B 197; matches on record A 53, B 6; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV03DRAFAG-DRA  (YES = Petja Drame)
Model: 57%
Kalshi: 24%
Gap: +33 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hernandez Miranda / Carolina Nava Elkin vs Garcia / Carmen Zamburek -- W50 Huamantla R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 02:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03HERCARGARCAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Garcia / Carmen Zamburek (`KXITFWDOUBLES-26NOV03HERCARGARCAR-GARCAR`) | 0.09 / 0.89 (250) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Hernandez Miranda / Carolina Nava Elkin (`KXITFWDOUBLES-26NOV03HERCARGARCAR-HERCAR`) | 0.09 / 0.89 (250) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Kallista Liu vs Berrak Kocak -- W15 Hilton Head Island SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264180:266571:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Berrak Kocak (`KXITFWMATCH-26NOV03LIUKOC-KOC`) | 0.25 / 0.27 (6) | 26.0% | 25.0% | 43.1% | 44.6% [43.1%-45.2%] | -- | -- | -- | -- | PASS | -1.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kallista Liu (`KXITFWMATCH-26NOV03LIUKOC-LIU`) | 0.73 / 0.75 (86) | 74.0% | 75.0% | 56.9% | 55.4% [54.8%-56.9%] | -- | -- | -- | -- | PASS | +1.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1064.0, B 171.0; serve-point win A 54.1%, B 50.9%; Elo A 1295.7, B 1260.0; model uncertainty 0.0107
* Form inputs: days since last match A 211, B 245; matches on record A 41, B 6; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Isha Manchala vs Yael Saffar -- W15 Hilton Head Island SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03MANSAF:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Isha Manchala (`KXITFWMATCH-26NOV03MANSAF-MAN`) | 0.49 / 0.59 (56) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yael Saffar (`KXITFWMATCH-26NOV03MANSAF-SAF`) | 0.43 / 0.44 (44) | 43.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Charlotte Narti vs Ava Catanzarite -- W15 Hilton Head Island SC R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 02:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T02:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260303:270203:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ava Catanzarite (`KXITFWMATCH-26NOV03NARCAT-CAT`) | 0.51 / 0.52 (173) | 51.5% | 45.8% | 60.5% | 45.8% [44.7%-47.3%] | -- | -- | -- | -- | PASS | -5.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Charlotte Narti (`KXITFWMATCH-26NOV03NARCAT-NAR`) | 0.47 / 0.49 (51) | 48.0% | 54.2% | 39.5% | 54.2% [52.6%-55.3%] | -- | -- | -- | -- | PASS | +6.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 300.0, B 106.0; serve-point win A 55.0%, B 45.8%; Elo A 1309.0, B 1275.2; model uncertainty 0.0133
* Form inputs: days since last match A 197, B 232; matches on record A 6, B 12; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Pedro Boscardin Dias / Gustavo Heide vs Federico Zeballos / Marcelo Zormann -- ATP Challenger Costa do Sauipe R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 02:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-04T02:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03BOSHEIZEBZOR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedro Boscardin Dias / Gustavo Heide (`KXATPCHALLENGERDOUBLES-26NOV03BOSHEIZEBZOR-BOSHEI`) | 0.06 / 0.46 (126) | 26.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Federico Zeballos / Marcelo Zormann (`KXATPCHALLENGERDOUBLES-26NOV03BOSHEIZEBZOR-ZEBZOR`) | 0.48 / 0.93 (250) | 70.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Guido Ivan Justo / Lautaro Midon vs Bruno (2002) Oliveira / Paulo Andre Saraiva Dos Santos -- ATP Challenger Costa do Sauipe R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 02:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (CHALLENGER) · surface ? · scheduled 2026-11-04T02:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03JUSMIDOLISAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guido Ivan Justo / Lautaro Midon (`KXATPCHALLENGERDOUBLES-26NOV03JUSMIDOLISAR-JUSMID`) | 0.06 / 0.59 (250) | 32.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Bruno (2002) Oliveira / Paulo Andre Saraiva Dos Santos (`KXATPCHALLENGERDOUBLES-26NOV03JUSMIDOLISAR-OLISAR`) | 0.35 / 0.93 (250) | 64.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Thiago Seyboth Wild vs Felipe Meligeni Alves -- ATP Challenger Costa do Sauipe R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 02:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Clay · scheduled 2026-11-04T02:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200335:205734:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Felipe Meligeni Alves (`KXATPCHALLENGERMATCH-26NOV03SEYMEL-MEL`) | 0.27 / 0.28 (1669) | 27.5% | 27.1% | 19.6% | 24.3% [21.7%-27.5%] | -- | -- | -- | -- | PASS | -0.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Thiago Seyboth Wild (`KXATPCHALLENGERMATCH-26NOV03SEYMEL-SEY`) | 0.72 / 0.73 (1163) | 72.5% | 72.9% | 80.4% | 75.7% [72.5%-78.3%] | -- | -- | -- | -- | WATCH | +0.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4921.0, B 3374.0; serve-point win A 66.8%, B 38.1%; Elo A 1772.0, B 1677.8; model uncertainty 0.0288
* Form inputs: days since last match A 22, B 15; matches on record A 510, B 532; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high +0.000, surface_dev_loose +0.008, surface_dev_tight -0.012
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE

## Edwards / Shugar vs Dean / Tripathi -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 02:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T02:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03EDWSHUDEATRI:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dean / Tripathi (`KXITFDOUBLES-26NOV03EDWSHUDEATRI-DEATRI`) | 0.09 / 0.89 (250) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Edwards / Shugar (`KXITFDOUBLES-26NOV03EDWSHUDEATRI-EDWSHU`) | 0.09 / 0.89 (250) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Rodrigo Alujas vs Alan Sau Franco -- M25 Guadalajara R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206827:212286:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigo Alujas (`KXITFMATCH-26NOV03ALUSAU-ALU`) | 0.86 / 0.91 (2101) | 88.5% | 73.9% | 82.2% | 74.1% [69.9%-79.0%] | -- | -- | -- | -- | PASS | -14.7 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alan Sau Franco (`KXITFMATCH-26NOV03ALUSAU-SAU`) | 0.08 / 0.12 (102) | 10.0% | 26.2% | 17.8% | 25.9% [21.0%-30.1%] | -- | -- | -- | -- | WATCH | +16.1 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2335.0, B 649.0; serve-point win A 59.2%, B 45.6%; Elo A 1298.5, B 1149.2; model uncertainty 0.0455
* Form inputs: days since last match A 197, B 197; matches on record A 83, B 35; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03ALUSAU-SAU  (YES = Alan Sau Franco)
Model: 26%
Kalshi: 10%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.017, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Patricio Alvarado vs Lorenzo Claverie -- M25 Guadalajara R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105419:209936:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Patricio Alvarado (`KXITFMATCH-26NOV03ALVCLA-ALV`) | 0.12 / 0.13 (128) | 12.5% | 11.3% | 19.9% | 19.2% [16.0%-22.1%] | -- | -- | -- | -- | WATCH | -1.2 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lorenzo Claverie (`KXITFMATCH-26NOV03ALVCLA-CLA`) | 0.86 / 0.89 (555) | 87.5% | 88.7% | 80.1% | 80.8% [77.9%-84.0%] | -- | -- | -- | -- | PASS | +1.2 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 867.0, B 484.0; serve-point win A 58.0%, B 32.4%; Elo A 1086.3, B 1342.4; model uncertainty 0.0306
* Form inputs: days since last match A 218, B 8; matches on record A 82, B 99; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.032, surface_pool_high +0.029, surface_dev_loose -0.003, surface_dev_tight -0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ian Lucca Cervantes Tomas vs Maxwell McKennon -- M25 Guadalajara R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208297:212486:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ian Lucca Cervantes Tomas (`KXITFMATCH-26NOV03CERMCK-CER`) | 0.28 / 0.29 (170) | 28.5% | 16.5% | 15.7% | 20.0% [17.3%-22.1%] | -- | -- | -- | -- | PASS | -12.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maxwell McKennon (`KXITFMATCH-26NOV03CERMCK-MCK`) | 0.68 / 0.69 (81) | 68.5% | 83.5% | 84.3% | 80.0% [77.9%-82.7%] | -- | -- | -- | -- | PASS | +15.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 529.0, B 3096.0; serve-point win A 59.2%, B 33.0%; Elo A 1163.1, B 1386.5; model uncertainty 0.0242
* Form inputs: days since last match A 407, B 190; matches on record A 24, B 140; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.007, surface_dev_loose +0.001, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Joao Cunha Cunha vs Rafael Ferreira -- M15 Salvador R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03CUNFER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joao Cunha Cunha (`KXITFMATCH-26NOV03CUNFER-CUN`) | 0.45 / 0.46 (46) | 45.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Rafael Ferreira (`KXITFMATCH-26NOV03CUNFER-FER`) | 0.53 / 0.55 (126) | 54.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Mauricio Echazu vs Mauricio Schtulmann Gasca -- M25 Guadalajara R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 03:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:105273:214271:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mauricio Echazu (`KXITFMATCH-26NOV03ECHSCH-ECH`) | 0.88 / 0.93 (2105) | 90.5% | 46.2% | 68.5% | 47.0% [43.9%-50.0%] | -- | -- | -- | -- | PASS | -44.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mauricio Schtulmann Gasca (`KXITFMATCH-26NOV03ECHSCH-SCH`) | 0.06 / 0.10 (101) | 8.0% | 53.8% | 31.5% | 53.0% [50.0%-56.1%] | -- | -- | -- | -- | PASS | +45.8 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 170.0, B 64.0; serve-point win A 61.9%, B 37.4%; Elo A 1331.0, B 1360.7; model uncertainty 0.0303
* Form inputs: days since last match A 190, B 211; matches on record A 685, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03ECHSCH-SCH  (YES = Mauricio Schtulmann Gasca)
Model: 54%
Kalshi: 8%
Gap: +46 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.030, surface_pool_high -0.030, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Thomas George / Peck vs Colburne / Genereux -- M15 Trois-Rivières R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 03:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T03:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03THOPECCOLGEN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Colburne / Genereux (`KXITFDOUBLES-26NOV03THOPECCOLGEN-COLGEN`) | 0.09 / 0.88 (2) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Thomas George / Peck (`KXITFDOUBLES-26NOV03THOPECCOLGEN-THOPEC`) | 0.09 / 0.89 (250) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Charles Broom vs Liam Broady -- ATP Challenger Taipei R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-04T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106281:200277:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Charles Broom (`KXATPCHALLENGERMATCH-26NOV03BROBRO2-BRO`) | 0.51 / 0.53 (1336) | 52.0% | 57.4% | 50.5% | 50.0% [49.5%-50.5%] | 55.4% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Liam Broady (`KXATPCHALLENGERMATCH-26NOV03BROBRO2-BRO2`) | 0.47 / 0.48 (115) | 47.5% | 42.6% | 49.5% | 50.0% [49.5%-50.5%] | 44.6% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | -4.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4307.0, B 4694.0; serve-point win A 63.1%, B 38.3%; Elo A 1636.7, B 1640.6; model uncertainty 0.0051
* Form inputs: days since last match A 8, B 8; matches on record A 395, B 951; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high +0.005, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Harold Mayot vs Petr Bar Biryukov -- ATP Challenger Taipei R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 05:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-04T05:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:208004:209951:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Petr Bar Biryukov (`KXATPCHALLENGERMATCH-26NOV03MAYBAR-BAR`) | 0.15 / 0.16 (1704) | 15.5% | 24.8% | 18.4% | 20.8% [19.1%-22.9%] | 21.3% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +9.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Harold Mayot (`KXATPCHALLENGERMATCH-26NOV03MAYBAR-MAY`) | 0.84 / 0.85 (1421) | 84.5% | 75.2% | 81.5% | 79.2% [77.1%-80.9%] | 78.7% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.3 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4935.0, B 4332.0; serve-point win A 70.5%, B 35.1%; Elo A 1731.6, B 1576.5; model uncertainty 0.0189
* Form inputs: days since last match A 8, B 8; matches on record A 412, B 246; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.021, surface_dev_loose +0.006, surface_dev_tight -0.010
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Lothringer / Lovern vs Papa / Perot -- M25 Harlingen TX R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 05:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T05:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03LOTLOVPAPPER:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lothringer / Lovern (`KXITFDOUBLES-26NOV03LOTLOVPAPPER-LOTLOV`) | 0.09 / 0.89 (250) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Papa / Perot (`KXITFDOUBLES-26NOV03LOTLOVPAPPER-PAPPER`) | 0.09 / 0.89 (250) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Yaroslav Demin vs Alexandre Muller -- ATP Challenger Taipei R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 06:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-04T06:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:124186:211596:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yaroslav Demin (`KXATPCHALLENGERMATCH-26NOV03DEMMUL-DEM`) | 0.36 / 0.37 (1342) | 36.5% | 31.5% | 58.5% | 44.5% [22.4%-51.5%] | 38.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | -5.0 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alexandre Muller (`KXATPCHALLENGERMATCH-26NOV03DEMMUL-MUL`) | 0.63 / 0.64 (1031) | 63.5% | 68.5% | 41.5% | 55.5% [48.5%-77.6%] | 61.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | +5.0 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2769.0, B 4505.0; serve-point win A 60.8%, B 35.4%; Elo A 1479.2, B 1713.7; model uncertainty 0.1456
* Form inputs: days since last match A 218, B 8; matches on record A 121, B 787; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.040, surface_pool_high +0.030, surface_dev_loose +0.035, surface_dev_tight -0.040
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; EXTERNAL_PRICE_STALE

## Carl Emil Overbeck vs Chun Hsin Tseng -- ATP Challenger Taipei R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 06:10Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

CHALLENGER (CHALLENGER) · Hard · scheduled 2026-11-04T06:10:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:202358:209274:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carl Emil Overbeck (`KXATPCHALLENGERMATCH-26NOV03OVETSE-OVE`) | 0.33 / 0.34 (22) | 33.5% | 31.1% | 53.5% | 45.5% [35.4%-51.5%] | 36.2% | -- | 36.2% | MARKETS_AGREE | WATCH | -2.4 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |
| Chun Hsin Tseng (`KXATPCHALLENGERMATCH-26NOV03OVETSE-TSE`) | 0.66 / 0.67 (1085) | 66.5% | 68.9% | 46.5% | 54.5% [48.5%-64.6%] | 63.8% | -- | 63.8% | MARKETS_AGREE | PASS | +2.4 pp | NORMAL | AGING | A / ADEQUATE | EXTERNAL_OUTLIER | VERIFIED |

* Serve evidence (points): A 2090.0, B 5329.0; serve-point win A 62.2%, B 33.9%; Elo A 1498.7, B 1615.1; model uncertainty 0.0805
* Form inputs: days since last match A 36, B 29; matches on record A 83, B 518; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.034, surface_pool_high +0.030, surface_dev_loose +0.005, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE

## Patricio Betancourt vs Reid Jarvis -- M25 Guadalajara R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 06:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T06:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213666:213928:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Patricio Betancourt (`KXITFMATCH-26NOV03BETJAR-BET`) | 0.19 / 0.20 (25) | 19.5% | 50.4% | 32.2% | 47.9% [45.4%-49.0%] | -- | -- | -- | -- | PASS | +30.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Reid Jarvis (`KXITFMATCH-26NOV03BETJAR-JAR`) | 0.75 / 0.80 (7) | 77.5% | 49.6% | 67.8% | 52.0% [51.0%-54.6%] | -- | -- | -- | -- | PASS | -27.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 393.0, B 213.0; serve-point win A 61.0%, B 39.1%; Elo A 1205.5, B 1207.8; model uncertainty 0.0178
* Form inputs: days since last match A 190, B 351; matches on record A 9, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03BETJAR-BET  (YES = Patricio Betancourt)
Model: 50%
Kalshi: 20%
Gap: +31 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cristobal Plasencia Robles vs Rodrigo Pacheco Mendez -- M25 Guadalajara R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 06:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T06:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03PLAPAC:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rodrigo Pacheco Mendez (`KXITFMATCH-26NOV03PLAPAC-PAC`) | 0.61 / 0.94 (25) | 77.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cristobal Plasencia Robles (`KXITFMATCH-26NOV03PLAPAC-PLA`) | 0.05 / 0.39 (100) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Natsuho Arakawa vs Yuno Kitahara -- W35 Hamamatsu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-04T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214398:263881:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Natsuho Arakawa (`KXITFWMATCH-26NOV03ARAKIT-ARA`) | 0.17 / 0.18 (6) | 17.5% | 20.4% | 14.6% | 22.8% [17.6%-29.2%] | 19.5% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +2.9 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuno Kitahara (`KXITFWMATCH-26NOV03ARAKIT-KIT`) | 0.78 / 0.82 (283) | 80.0% | 79.6% | 85.4% | 77.2% [70.8%-82.4%] | 80.5% | -- | -- | INSUFFICIENT_INPUTS | PASS | -0.4 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1193.0, B 2068.0; serve-point win A 51.5%, B 42.2%; Elo A 1225.9, B 1370.5; model uncertainty 0.058
* Form inputs: days since last match A 225, B 197; matches on record A 225, B 119; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.008, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tiana Tian Deng vs Meng Yi Chen -- W35 Hamamatsu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-04T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221903:260528:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Meng Yi Chen (`KXITFWMATCH-26NOV03DENCHE-CHE`) | 0.28 / 0.32 (217) | 30.0% | 50.8% | 45.7% | 52.7% [50.0%-56.4%] | 30.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | +20.8 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tiana Tian Deng (`KXITFWMATCH-26NOV03DENCHE-DEN`) | 0.68 / 0.72 (189) | 70.0% | 49.2% | 54.3% | 47.3% [43.6%-50.0%] | 69.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | -20.8 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 853.0, B 1394.0; serve-point win A 53.5%, B 46.4%; Elo A 1297.9, B 1341.3; model uncertainty 0.0319
* Form inputs: days since last match A 120, B 239; matches on record A 41, B 162; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV03DENCHE-CHE  (YES = Meng Yi Chen)
Model: 51%
Kalshi: 30%
Gap: +21 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.005, surface_pool_high +0.011, surface_dev_loose +0.027, surface_dev_tight -0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuka Hosoki vs Funa Kozaki -- W35 Hamamatsu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-04T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215956:216260:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuka Hosoki (`KXITFWMATCH-26NOV03HOSKOZ-HOS`) | 0.20 / 0.21 (100) | 20.5% | 11.4% | 29.1% | 20.3% [20.3%-21.1%] | 21.9% | -- | -- | INSUFFICIENT_INPUTS | PASS | -9.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Funa Kozaki (`KXITFWMATCH-26NOV03HOSKOZ-KOZ`) | 0.76 / 0.79 (16) | 77.5% | 88.6% | 70.9% | 79.7% [78.9%-79.7%] | 78.1% | -- | -- | INSUFFICIENT_INPUTS | PASS | +11.1 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 859.0, B 166.0; serve-point win A 48.4%, B 42.5%; Elo A 1236.2, B 1477.7; model uncertainty 0.004
* Form inputs: days since last match A 190, B 197; matches on record A 222, B 222; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karen Tsutsumi vs Kisa Yoshioka -- W35 Hamamatsu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 07:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-04T07:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215616:223271:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Karen Tsutsumi (`KXITFWMATCH-26NOV03TSUYOS-TSU`) | 0.06 / 0.08 (8) | 7.0% | 39.2% | 44.7% | 45.7% [44.7%-45.7%] | -- | -- | -- | -- | PASS | +32.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kisa Yoshioka (`KXITFWMATCH-26NOV03TSUYOS-YOS`) | 0.90 / 0.94 (177) | 92.0% | 60.8% | 55.3% | 54.3% [54.3%-55.3%] | -- | -- | -- | -- | PASS | -31.2 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 138.0, B 1530.0; serve-point win A 52.0%, B 46.0%; Elo A 1331.2, B 1360.9; model uncertainty 0.0054
* Form inputs: days since last match A 519, B 197; matches on record A 22, B 159; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV03TSUYOS-TSU  (YES = Karen Tsutsumi)
Model: 39%
Kalshi: 7%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Talia Gibson vs Aliaksandra Sasnovich -- WTA Hong Kong R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-04 09:00Z
* Current expected start: 2026-11-04 07:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-04 06:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-90_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-04T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:205925:221883:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Talia Gibson (`KXWTAMATCH-26NOV04GIBSAS-GIB`) | 0.37 / 0.39 (1000) | 38.0% | 57.2% | 71.1% | 67.0% [53.1%-70.7%] | 39.8% | -- | 39.8% | KALSHI_LONE_OUTLIER | WATCH | +19.2 pp | HIGH_REVIEW | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |
| Aliaksandra Sasnovich (`KXWTAMATCH-26NOV04GIBSAS-SAS`) | 0.60 / 0.62 (1522) | 61.0% | 42.8% | 28.9% | 33.0% [29.3%-46.9%] | 60.2% | -- | 60.2% | MODEL_LONE_OUTLIER | PASS | -18.2 pp | HIGH_REVIEW | AGING | A / LIMITED | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4414.0, B 4822.0; serve-point win A 60.4%, B 41.0%; Elo A 1884.7, B 1854.6; model uncertainty 0.0877
* Form inputs: days since last match A 0, B 1; matches on record A 356, B 799; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26NOV04GIBSAS-GIB  (YES = Talia Gibson)
Model: 57%
Kalshi: 38%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: A (LIMITED)
Reasons: SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.024, surface_pool_high +0.023, surface_dev_loose +0.014, surface_dev_tight -0.019
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26NOV04GIBSAS-1-SAS` Will Aliaksandra Sasnovich win set 1 in the Talia Gibson vs Aliaksandra Sasnovich match: 0.50/0.85 mid 67.5%, model 45.2% (projection_v2.0 (prediction ledger)) -- gap -22.3 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV04GIBSAS-1-GIB` Will Talia Gibson win set 1 in the Talia Gibson vs Aliaksandra Sasnovich match: 0.16/0.50 mid 33.0%, model 54.8% (projection_v2.0 (prediction ledger)) -- gap +21.8 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV04GIBSAS-2-GIB` Will Talia Gibson win set 2 in the Talia Gibson vs Aliaksandra Sasnovich match: 0.05/0.93 mid 49.0%, model 54.8% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV04GIBSAS-2-SAS` Will Aliaksandra Sasnovich win set 2 in the Talia Gibson vs Aliaksandra Sasnovich match: 0.05/0.93 mid 49.0%, model 45.2% (projection_v2.0 (prediction ledger)) -- gap -3.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; WIDE_SPREAD

## Claire Liu vs Katie Boulter -- WTA Hong Kong R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-04 09:00Z
* Current expected start: 2026-11-04 07:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-04 06:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-90_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-04T09:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:211107:214906:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Katie Boulter (`KXWTAMATCH-26NOV04LIUBOU-BOU`) | 0.59 / 0.60 (2010) | 59.5% | 65.9% | 66.9% | 67.4% [65.5%-68.3%] | 59.4% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +6.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Claire Liu (`KXWTAMATCH-26NOV04LIUBOU-LIU`) | 0.40 / 0.41 (2845) | 40.5% | 34.1% | 33.1% | 32.6% [31.6%-34.5%] | 40.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -6.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3837.0, B 3928.0; serve-point win A 54.2%, B 42.7%; Elo A 1769.5, B 1893.7; model uncertainty 0.0143
* Form inputs: days since last match A 1, B 1; matches on record A 460, B 595; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.005
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV04LIUBOU-18` Over 17.5 games: 0.42/0.83 mid 62.5%, model 86.1% (projection_v2.0 (prediction ledger)) -- gap +23.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV04LIUBOU-2-BOU` Will Katie Boulter win set 2 in the Claire Liu vs Katie Boulter match: 0.05/0.93 mid 49.0%, model 60.8% (projection_v2.0 (prediction ledger)) -- gap +11.8 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV04LIUBOU-2-LIU` Will Claire Liu win set 2 in the Claire Liu vs Katie Boulter match: 0.05/0.93 mid 49.0%, model 39.2% (projection_v2.0 (prediction ledger)) -- gap -9.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV04LIUBOU-23` Over 22.5 games: 0.44/0.46 mid 45.0%, model 53.6% (projection_v2.0 (prediction ledger)) -- gap +8.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV04LIUBOU-1-BOU` Will Katie Boulter win set 1 in the Claire Liu vs Katie Boulter match: 0.55/0.58 mid 56.5%, model 60.8% (projection_v2.0 (prediction ledger)) -- gap +4.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV04LIUBOU-1-LIU` Will Claire Liu win set 1 in the Claire Liu vs Katie Boulter match: 0.42/0.45 mid 43.5%, model 39.2% (projection_v2.0 (prediction ledger)) -- gap -4.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV04LIUBOU-28` Over 27.5 games: 0.05/0.53 mid 29.0%, model 32.3% (projection_v2.0 (prediction ledger)) -- gap +3.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Yue Xia vs Weiyi Kong -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213058:213883:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weiyi Kong (`KXITFMATCH-26NOV03XIAKON-KON`) | 0.32 / 0.37 (121) | 34.5% | 71.2% | 78.1% | 62.5% [60.1%-67.1%] | -- | -- | -- | -- | PASS | +36.7 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yue Xia (`KXITFMATCH-26NOV03XIAKON-XIA`) | 0.62 / 0.65 (313) | 63.5% | 28.8% | 21.9% | 37.5% [32.9%-39.9%] | -- | -- | -- | -- | PASS | -34.7 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 202.0, B 302.0; serve-point win A 59.6%, B 36.0%; Elo A 1205.9, B 1279.3; model uncertainty 0.035
* Form inputs: days since last match A 421, B 428; matches on record A 4, B 9; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03XIAKON-KON  (YES = Weiyi Kong)
Model: 71%
Kalshi: 34%
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
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xin Zhou vs Boris Butulija -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03ZHOBUT:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Boris Butulija (`KXITFMATCH-26NOV03ZHOBUT-BUT`) | 0.56 / 0.60 (201) | 58.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Xin Zhou (`KXITFMATCH-26NOV03ZHOBUT-ZHO`) | 0.40 / 0.42 (143) | 41.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maxim Zhukov vs Stefan Storch -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 08:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210393:213532:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stefan Storch (`KXITFMATCH-26NOV03ZHUSTO-STO`) | 0.07 / 0.10 (101) | 8.5% | 12.4% | 8.1% | 15.5% [11.2%-19.3%] | -- | -- | -- | -- | PASS | +3.9 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maxim Zhukov (`KXITFMATCH-26NOV03ZHUSTO-ZHU`) | 0.89 / 0.92 (100) | 90.5% | 87.6% | 91.9% | 84.5% [80.7%-88.8%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2791.0, B 469.0; serve-point win A 65.2%, B 43.8%; Elo A 1452.3, B 1199.1; model uncertainty 0.0402
* Form inputs: days since last match A 85, B 225; matches on record A 199, B 12; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.005, surface_dev_tight -0.006
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Hiromi Abe vs Maiko Uchijima -- W35 Hamamatsu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-04T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221362:264134:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hiromi Abe (`KXITFWMATCH-26NOV03ABEUCH-ABE`) | 0.85 / 0.95 (105) | 90.0% | 94.6% | 78.9% | 83.2% [80.4%-85.8%] | -- | -- | -- | -- | PASS | +4.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Maiko Uchijima (`KXITFWMATCH-26NOV03ABEUCH-UCH`) | 0.05 / 0.15 (27) | 10.0% | 5.4% | 21.1% | 16.8% [14.2%-19.6%] | -- | -- | -- | -- | PASS | -4.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 2555.0, B 0.0; serve-point win A 59.2%, B 52.8%; Elo A 1623.4, B 1346.7; model uncertainty 0.0268
* Form inputs: days since last match A 232, B 1233; matches on record A 200, B 10; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.025, surface_pool_high -0.028, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Haruna Arakawa vs Yuzuha Negishi -- W35 Hamamatsu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-04T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214505:266700:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haruna Arakawa (`KXITFWMATCH-26NOV03ARANEG-ARA`) | 0.88 / 0.91 (105) | 89.5% | 86.4% | 77.3% | 76.1% [73.6%-77.8%] | -- | -- | -- | -- | PASS | -3.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yuzuha Negishi (`KXITFWMATCH-26NOV03ARANEG-NEG`) | 0.08 / 0.11 (106) | 9.5% | 13.6% | 22.7% | 23.9% [22.2%-26.4%] | -- | -- | -- | -- | PASS | +4.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2195.0, B 533.0; serve-point win A 56.7%, B 51.5%; Elo A 1466.1, B 1274.4; model uncertainty 0.0209
* Form inputs: days since last match A 365, B 197; matches on record A 411, B 22; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.016, surface_pool_high -0.026, surface_dev_loose +0.008, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Dayeon Back vs Berfu Cengiz -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214507:220432:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dayeon Back (`KXITFWMATCH-26NOV03BACCEN-BAC`) | 0.37 / 0.40 (38) | 38.5% | 61.3% | 78.5% | 70.8% [58.5%-76.5%] | 39.4% | -- | -- | INSUFFICIENT_INPUTS | WATCH | +22.8 pp | HIGH_REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Berfu Cengiz (`KXITFWMATCH-26NOV03BACCEN-CEN`) | 0.58 / 0.62 (32) | 60.0% | 38.7% | 21.5% | 29.2% [23.5%-41.5%] | 60.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -21.3 pp | HIGH_REVIEW | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3370.0, B 1612.0; serve-point win A 54.5%, B 47.6%; Elo A 1649.3, B 1571.0; model uncertainty 0.0901
* Form inputs: days since last match A 41, B 35; matches on record A 295, B 455; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV03BACCEN-BAC  (YES = Dayeon Back)
Model: 61%
Kalshi: 38%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (LIMITED)
Reasons: SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.028, surface_pool_high +0.027, surface_dev_loose -0.009, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## BoYoung Jeong vs YeXin Ma -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03JEOMAX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BoYoung Jeong (`KXITFWMATCH-26NOV03JEOMAX-JEO`) | 0.17 / 0.19 (45) | 18.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| YeXin Ma (`KXITFWMATCH-26NOV03JEOMAX-MAX`) | 0.80 / 0.84 (331) | 82.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ekaterina Khodzhaeva vs Ru Xi Wu -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:267885:270262:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ekaterina Khodzhaeva (`KXITFWMATCH-26NOV03KHOWUX-KHO`) | 0.18 / 0.19 (31) | 18.5% | 28.5% | 33.9% | 30.5% [29.6%-31.4%] | -- | -- | -- | -- | PASS | +10.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ru Xi Wu (`KXITFWMATCH-26NOV03KHOWUX-WUX`) | 0.78 / 0.81 (86) | 79.5% | 71.5% | 66.1% | 69.5% [68.6%-70.4%] | -- | -- | -- | -- | PASS | -8.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 532.0, B 171.0; serve-point win A 49.9%, B 45.8%; Elo A 1270.1, B 1417.8; model uncertainty 0.0092
* Form inputs: days since last match A 190, B 35; matches on record A 13, B 3; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.000, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yujin Kim vs Eunhye Lee -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215501:264973:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yujin Kim (`KXITFWMATCH-26NOV03KIMLEE-KIM`) | 0.31 / 0.35 (138) | 33.0% | 26.1% | 29.3% | 29.7% [28.4%-31.1%] | -- | -- | -- | -- | PASS | -6.9 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Eunhye Lee (`KXITFWMATCH-26NOV03KIMLEE-LEE`) | 0.66 / 0.70 (217) | 68.0% | 73.9% | 70.7% | 70.3% [68.9%-71.6%] | -- | -- | -- | -- | PASS | +5.9 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1654.0, B 2856.0; serve-point win A 52.6%, B 42.6%; Elo A 1434.1, B 1581.7; model uncertainty 0.0138
* Form inputs: days since last match A 190, B 44; matches on record A 103, B 303; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.009, surface_pool_high +0.009, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kanon Sawashiro vs Nagisa Suzuki -- W35 Hamamatsu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-04T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220717:263905:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kanon Sawashiro (`KXITFWMATCH-26NOV03SAWSUZ-SAW`) | 0.67 / 0.71 (4) | 69.0% | 73.2% | 68.5% | 53.2% [52.1%-55.3%] | 69.2% | -- | -- | INSUFFICIENT_INPUTS | PASS | +4.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nagisa Suzuki (`KXITFWMATCH-26NOV03SAWSUZ-SUZ`) | 0.30 / 0.32 (28) | 31.0% | 26.8% | 31.5% | 46.8% [44.7%-47.9%] | 30.8% | -- | -- | INSUFFICIENT_INPUTS | PASS | -4.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 827.0, B 99.0; serve-point win A 54.9%, B 49.7%; Elo A 1351.6, B 1335.4; model uncertainty 0.016
* Form inputs: days since last match A 17, B 197; matches on record A 37, B 10; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yushan Shao vs Ke Ren -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:260621:269253:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ke Ren (`KXITFWMATCH-26NOV03SHAREN-REN`) | 0.12 / 0.13 (11) | 12.5% | 12.7% | 10.0% | 25.6% [19.6%-30.1%] | -- | -- | -- | -- | PASS | +0.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yushan Shao (`KXITFWMATCH-26NOV03SHAREN-SHA`) | 0.85 / 0.86 (448) | 85.5% | 87.3% | 90.0% | 74.4% [69.9%-80.4%] | -- | -- | -- | -- | PASS | +1.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1123.0, B 366.0; serve-point win A 57.4%, B 51.2%; Elo A 1398.2, B 1253.1; model uncertainty 0.0525
* Form inputs: days since last match A 28, B 190; matches on record A 29, B 72; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high +0.000, surface_dev_loose +0.017, surface_dev_tight -0.013
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jiaqi Wang vs Yiru Chen -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221181:266372:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yiru Chen (`KXITFWMATCH-26NOV03WANCHE-CHE`) | 0.04 / 0.09 (7) | 6.5% | 8.6% | 8.0% | 12.8% [10.4%-14.8%] | -- | -- | -- | -- | PASS | +2.1 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jiaqi Wang (`KXITFWMATCH-26NOV03WANCHE-WAN`) | 0.88 / 0.94 (25) | 91.0% | 91.4% | 92.0% | 87.2% [85.2%-89.6%] | -- | -- | -- | -- | PASS | +0.4 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2849.0, B 625.0; serve-point win A 57.5%, B 52.7%; Elo A 1543.7, B 1245.2; model uncertainty 0.0222
* Form inputs: days since last match A 190, B 190; matches on record A 250, B 28; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high +0.000, surface_dev_loose +0.011, surface_dev_tight -0.003
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kamonwan Yodpetch vs Shiho Tsujioka -- W35 Hamamatsu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 08:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-04T08:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:259907:263801:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shiho Tsujioka (`KXITFWMATCH-26NOV03YODTSU-TSU`) | 0.55 / 0.57 (138) | 56.0% | 54.2% | 64.6% | 58.5% [54.8%-61.6%] | -- | -- | -- | -- | PASS | -1.8 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kamonwan Yodpetch (`KXITFWMATCH-26NOV03YODTSU-YOD`) | 0.41 / 0.45 (135) | 43.0% | 45.8% | 35.4% | 41.5% [38.4%-45.2%] | -- | -- | -- | -- | PASS | +2.8 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1037.0, B 1131.0; serve-point win A 52.2%, B 47.0%; Elo A 1341.4, B 1368.7; model uncertainty 0.034
* Form inputs: days since last match A 190, B 10; matches on record A 72, B 43; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jordan Chiu vs Kristjan Tamm -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144932:207780:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jordan Chiu (`KXITFMATCH-26NOV03CHITAM-CHI`) | 0.22 / 0.30 (28) | 26.0% | 20.5% | 45.5% | 24.0% [21.9%-27.7%] | -- | -- | -- | -- | PASS | -5.5 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kristjan Tamm (`KXITFMATCH-26NOV03CHITAM-TAM`) | 0.68 / 0.73 (128) | 70.5% | 79.5% | 54.5% | 76.0% [72.3%-78.1%] | -- | -- | -- | -- | PASS | +9.0 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 402.0, B 1552.0; serve-point win A 59.9%, B 33.6%; Elo A 1004.9, B 1248.5; model uncertainty 0.029
* Form inputs: days since last match A 190, B 46; matches on record A 30, B 257; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.012, surface_pool_high -0.004, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lorenzo Lorusso vs Tianhui Zhang -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 09:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210047:212221:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Lorusso (`KXITFMATCH-26NOV03LORZHA-LOR`) | 0.23 / 0.28 (155) | 25.5% | 36.4% | 40.0% | 39.0% [37.1%-40.9%] | -- | -- | -- | -- | WATCH | +10.9 pp | REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Tianhui Zhang (`KXITFMATCH-26NOV03LORZHA-ZHA`) | 0.71 / 0.74 (100) | 72.5% | 63.6% | 60.0% | 61.0% [59.1%-62.9%] | -- | -- | -- | -- | PASS | -8.9 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1815.0, B 1273.0; serve-point win A 61.3%, B 35.9%; Elo A 1247.5, B 1331.9; model uncertainty 0.0192
* Form inputs: days since last match A 197, B 8; matches on record A 96, B 78; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.019, surface_pool_high +0.015, surface_dev_loose +0.005, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zhuoxuan Bai vs Caroline Werner -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222296:espn:espn:4384:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zhuoxuan Bai (`KXITFWMATCH-26NOV03BAIWER-BAI`) | 0.66 / 0.68 (10) | 67.0% | 80.4% | 83.6% | 71.3% [71.3%-71.3%] | -- | -- | -- | -- | PASS | +13.4 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Caroline Werner (`KXITFWMATCH-26NOV03BAIWER-WER`) | 0.31 / 0.34 (26) | 32.5% | 19.6% | 16.4% | 28.7% [28.7%-28.7%] | -- | -- | -- | -- | PASS | -12.9 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1601.0, B 0.0; serve-point win A 56.2%, B 50.2%; Elo A 1765.4, B 1606.9; model uncertainty 0.0001
* Form inputs: days since last match A 25, B 6; matches on record A 213, B 25; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xinyu Gao vs Natsumi Kawaguchi -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214386:221229:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xinyu Gao (`KXITFWMATCH-26NOV03GAOKAW-GAO`) | 0.74 / 0.80 (141) | 77.0% | 81.3% | 71.6% | 72.5% [71.6%-73.5%] | -- | -- | -- | -- | PASS | +4.3 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Natsumi Kawaguchi (`KXITFWMATCH-26NOV03GAOKAW-KAW`) | 0.14 / 0.24 (6) | 19.0% | 18.7% | 28.4% | 27.5% [26.6%-28.4%] | -- | -- | -- | -- | PASS | -0.3 pp | NORMAL | AGING | A / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3203.0, B 2084.0; serve-point win A 58.6%, B 48.1%; Elo A 1711.8, B 1533.5; model uncertainty 0.0091
* Form inputs: days since last match A 31, B 38; matches on record A 419, B 213; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.004, surface_dev_loose +0.004, surface_dev_tight -0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Kristiana Sidorova vs Priska Madelyn Nugroho -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221187:260006:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Priska Madelyn Nugroho (`KXITFWMATCH-26NOV03SIDNUG-NUG`) | 0.52 / 0.64 (175) | 58.0% | 44.3% | 51.6% | 51.6% [50.0%-52.6%] | -- | -- | -- | -- | PASS | -13.7 pp | REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Kristiana Sidorova (`KXITFWMATCH-26NOV03SIDNUG-SID`) | 0.34 / 0.48 (13) | 41.0% | 55.7% | 48.4% | 48.4% [47.3%-50.0%] | -- | -- | -- | -- | PASS | +14.7 pp | REVIEW | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2506.0, B 2457.0; serve-point win A 56.5%, B 44.6%; Elo A 1564.7, B 1567.2; model uncertainty 0.0133
* Form inputs: days since last match A 30, B 218; matches on record A 140, B 235; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high +0.016, surface_dev_loose +0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yuna Sugiyama vs Anna Yang -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263879:264242:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuna Sugiyama (`KXITFWMATCH-26NOV03SUGYAN-SUG`) | 0.39 / 0.45 (161) | 42.0% | 19.3% | 45.2% | 30.6% [29.6%-31.5%] | -- | -- | -- | -- | PASS | -22.7 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anna Yang (`KXITFWMATCH-26NOV03SUGYAN-YAN`) | 0.55 / 0.58 (14) | 56.5% | 80.7% | 54.8% | 69.4% [68.5%-70.3%] | -- | -- | -- | -- | PASS | +24.2 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 66.0, B 270.0; serve-point win A 50.8%, B 42.7%; Elo A 1151.8, B 1302.6; model uncertainty 0.0094
* Form inputs: days since last match A 197, B 372; matches on record A 9, B 21; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV03SUGYAN-YAN  (YES = Anna Yang)
Model: 81%
Kalshi: 56%
Gap: +24 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.009, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Junlu Sun vs Yingqun Sun -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264029:264970:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Junlu Sun (`KXITFWMATCH-26NOV03SUNSUN2-SUN`) | 0.29 / 0.33 (129) | 31.0% | 18.0% | 52.6% | 38.5% [37.4%-38.5%] | -- | -- | -- | -- | PASS | -13.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Yingqun Sun (`KXITFWMATCH-26NOV03SUNSUN2-SUN2`) | 0.65 / 0.71 (102) | 68.0% | 82.0% | 47.3% | 61.5% [61.5%-62.6%] | -- | -- | -- | -- | PASS | +14.0 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 1826.0; serve-point win A 51.8%, B 41.3%; Elo A 1304.4, B 1387.9; model uncertainty 0.0053
* Form inputs: days since last match A 778, B 190; matches on record A 15, B 99; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arina Varaksina vs Thasaporn Naklo -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220597:255662:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thasaporn Naklo (`KXITFWMATCH-26NOV03VARNAK-NAK`) | 0.79 / 0.86 (147) | 82.5% | 77.7% | 78.8% | 75.2% [73.0%-77.3%] | -- | -- | -- | -- | PASS | -4.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arina Varaksina (`KXITFWMATCH-26NOV03VARNAK-VAR`) | 0.09 / 0.19 (24) | 14.0% | 22.3% | 21.2% | 24.8% [22.7%-27.0%] | -- | -- | -- | -- | PASS | +8.3 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 586.0, B 2173.0; serve-point win A 51.3%, B 43.0%; Elo A 1277.4, B 1456.9; model uncertainty 0.021
* Form inputs: days since last match A 197, B 190; matches on record A 27, B 166; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.017, surface_pool_high +0.009, surface_dev_loose -0.012, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## JiaYi Wang vs Ha Eum Lee -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:265692:270449:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ha Eum Lee (`KXITFWMATCH-26NOV03WANLEE-LEE`) | 0.27 / 0.38 (124) | 32.5% | 26.3% | 16.9% | 26.2% [22.4%-32.5%] | -- | -- | -- | -- | PASS | -6.2 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| JiaYi Wang (`KXITFWMATCH-26NOV03WANLEE-WAN`) | 0.55 / 0.72 (12) | 63.5% | 73.7% | 83.1% | 73.9% [67.5%-77.6%] | -- | -- | -- | -- | PASS | +10.2 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2216.0, B 1048.0; serve-point win A 57.4%, B 47.3%; Elo A 1510.1, B 1390.4; model uncertainty 0.0505
* Form inputs: days since last match A 35, B 190; matches on record A 72, B 15; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.025, surface_dev_tight -0.022
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ikumi Yamazaki vs Ying Xue -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 09:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03YAMXUE:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ying Xue (`KXITFWMATCH-26NOV03YAMXUE-XUE`) | 0.02 / 0.04 (713) | 3.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ikumi Yamazaki (`KXITFWMATCH-26NOV03YAMXUE-YAM`) | 0.91 / 0.97 (5) | 94.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Robin Montgomery vs Jeline Vandromme -- WTA Chennai R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-04 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-11-04 09:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-04 08:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-04T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221905:259871:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Robin Montgomery (`KXWTAMATCH-26NOV04MONVAN-MON`) | 0.56 / 0.58 (3012) | 57.0% | 41.8% | 12.1% | 27.5% [19.2%-48.9%] | 57.5% | -- | 57.5% | MODEL_LONE_OUTLIER | PASS | -15.2 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Jeline Vandromme (`KXWTAMATCH-26NOV04MONVAN-VAN`) | 0.42 / 0.44 (1390) | 43.0% | 58.2% | 87.9% | 72.5% [51.0%-80.8%] | 42.5% | -- | 42.5% | MODEL_LONE_OUTLIER | WATCH | +15.2 pp | HIGH_REVIEW | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 2060.0, B 3468.0; serve-point win A 58.2%, B 40.2%; Elo A 1841.0, B 1792.4; model uncertainty 0.1486
* Form inputs: days since last match A 0, B 0; matches on record A 251, B 132; data quality A

```
DISCREPANCY SANITY CHECK  KXWTAMATCH-26NOV04MONVAN-VAN  (YES = Jeline Vandromme)
Model: 58%
Kalshi: 43%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: AGREES_WITH_KALSHI
Data quality: A (ADEQUATE)
Reasons: MODEL_HIGH_UNCERTAINTY, EXTERNAL_MARKET_REJECTION, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.017, surface_dev_loose -0.009, surface_dev_tight +0.004
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV04MONVAN-18` Over 17.5 games: 0.35/0.83 mid 59.0%, model 89.5% (projection_v2.0 (prediction ledger)) -- gap +30.5 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV04MONVAN-28` Over 27.5 games: 0.03/0.32 mid 17.5%, model 36.0% (projection_v2.0 (prediction ledger)) -- gap +18.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV04MONVAN-23` Over 22.5 games: 0.41/0.44 mid 42.5%, model 57.0% (projection_v2.0 (prediction ledger)) -- gap +14.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV04MONVAN-1-MON` Will Robin Montgomery win set 1 in the Robin Montgomery vs Jeline Vandromme match: 0.54/0.57 mid 55.5%, model 44.5% (projection_v2.0 (prediction ledger)) -- gap -11.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV04MONVAN-1-VAN` Will Jeline Vandromme win set 1 in the Robin Montgomery vs Jeline Vandromme match: 0.43/0.46 mid 44.5%, model 55.5% (projection_v2.0 (prediction ledger)) -- gap +11.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV04MONVAN-2-VAN` Will Jeline Vandromme win set 2 in the Robin Montgomery vs Jeline Vandromme match: 0.02/0.94 mid 48.0%, model 55.5% (projection_v2.0 (prediction ledger)) -- gap +7.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV04MONVAN-2-MON` Will Robin Montgomery win set 2 in the Robin Montgomery vs Jeline Vandromme match: 0.02/0.94 mid 48.0%, model 44.5% (projection_v2.0 (prediction ledger)) -- gap -3.5 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Oksana Selekhmeteva vs Polina Kudermetova -- WTA Chennai R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-04 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-11-04 09:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-04 08:45Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-04T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:221236:221407:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Polina Kudermetova (`KXWTAMATCH-26NOV04SELKUD-KUD`) | 0.53 / 0.93 (2857) | 73.0% | 66.0% | 51.6% | 53.2% [52.6%-54.8%] | -- | -- | -- | -- | PASS | -7.0 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Oksana Selekhmeteva (`KXWTAMATCH-26NOV04SELKUD-SEL`) | 0.09 / 0.51 (125) | 30.0% | 34.0% | 48.4% | 46.8% [45.2%-47.3%] | -- | -- | -- | -- | PASS | +4.0 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4338.0, B 4285.0; serve-point win A 53.8%, B 43.1%; Elo A 1744.2, B 1810.3; model uncertainty 0.0106
* Form inputs: days since last match A 0, B 0; matches on record A 356, B 393; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high -0.011, surface_dev_loose -0.011, surface_dev_tight +0.005
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; WIDE_SPREAD

## Arakawa / Katsumi vs Yi Chen / Tian Deng -- W35 Hamamatsu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03ARAKATYICTIA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arakawa / Katsumi (`KXITFWDOUBLES-26NOV03ARAKATYICTIA-ARAKAT`) | 0.05 / 0.89 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yi Chen / Tian Deng (`KXITFWDOUBLES-26NOV03ARAKATYICTIA-YICTIA`) | 0.05 / 0.89 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Han / Yi Tsao vs Kawamura / Kozaki -- W35 Hamamatsu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03HANYITKAWKOZ:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Han / Yi Tsao (`KXITFWDOUBLES-26NOV03HANYITKAWKOZ-HANYIT`) | 0.05 / 0.89 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kawamura / Kozaki (`KXITFWDOUBLES-26NOV03HANYITKAWKOZ-KAWKOZ`) | 0.05 / 0.89 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Himari Sato vs Mio Mushika -- W35 Hamamatsu R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 10:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Carpet · scheduled 2026-11-04T10:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216156:222986:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mio Mushika (`KXITFWMATCH-26NOV03SATMUS-MUS`) | 0.69 / 0.75 (179) | 72.0% | 91.2% | 95.2% | 83.5% [77.3%-89.8%] | -- | -- | -- | -- | PASS | +19.2 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Himari Sato (`KXITFWMATCH-26NOV03SATMUS-SAT`) | 0.25 / 0.30 (242) | 27.5% | 8.8% | 4.8% | 16.5% [10.2%-22.7%] | -- | -- | -- | -- | PASS | -18.7 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 578.0, B 2224.0; serve-point win A 48.3%, B 41.5%; Elo A 1275.5, B 1475.3; model uncertainty 0.0624
* Form inputs: days since last match A 204, B 197; matches on record A 200, B 201; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV03SATMUS-MUS  (YES = Mio Mushika)
Model: 91%
Kalshi: 72%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.006, surface_pool_high +0.007, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Maya Joint vs Maria Sakkari -- WTA Hong Kong R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-04 13:30Z
* Current expected start: 2026-11-04 10:30Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-04 09:45Z

* Status notes: EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-180_MIN; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-04T13:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:206289:233741:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maya Joint (`KXWTAMATCH-26NOV04JOISAK-JOI`) | 0.33 / 0.35 (1954) | 34.0% | 42.0% | 43.2% | 41.1% [35.5%-43.2%] | 34.8% | -- | 34.8% | MODEL_LONE_OUTLIER | WATCH | +8.0 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Maria Sakkari (`KXWTAMATCH-26NOV04JOISAK-SAK`) | 0.64 / 0.66 (1574) | 65.0% | 58.0% | 56.8% | 58.9% [56.8%-64.5%] | 65.2% | -- | 65.2% | MODEL_LONE_OUTLIER | PASS | -7.0 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3855.0, B 3640.0; serve-point win A 55.3%, B 43.2%; Elo A 1847.5, B 1937.6; model uncertainty 0.0382
* Form inputs: days since last match A 0, B 1; matches on record A 245, B 863; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.015, surface_pool_high +0.021, surface_dev_loose -0.000, surface_dev_tight -0.000
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26NOV04JOISAK-1-SAK` Will Maria Sakkari win set 1 in the Maya Joint vs Maria Sakkari match: 0.02/0.93 mid 47.5%, model 55.3% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV04JOISAK-2-SAK` Will Maria Sakkari win set 2 in the Maya Joint vs Maria Sakkari match: 0.02/0.93 mid 47.5%, model 55.3% (projection_v2.0 (prediction ledger)) -- gap +7.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV04JOISAK-1-JOI` Will Maya Joint win set 1 in the Maya Joint vs Maria Sakkari match: 0.03/0.92 mid 47.5%, model 44.7% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV04JOISAK-2-JOI` Will Maya Joint win set 2 in the Maya Joint vs Maria Sakkari match: 0.02/0.93 mid 47.5%, model 44.7% (projection_v2.0 (prediction ledger)) -- gap -2.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; WIDE_SPREAD

## Dzmitry Dziubailau vs Nikita Ianin -- M15 Fergana R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210394:213870:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dzmitry Dziubailau (`KXITFMATCH-26NOV03DZIIAN-DZI`) | 0.14 / 0.90 (70) | 52.0% | 51.4% | 54.1% | 58.2% [57.2%-58.2%] | -- | -- | -- | -- | PASS | -0.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nikita Ianin (`KXITFMATCH-26NOV03DZIIAN-IAN`) | 0.13 / 0.90 (70) | 51.5% | 48.6% | 45.9% | 41.8% [41.8%-42.8%] | -- | -- | -- | -- | PASS | -2.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 64.0, B 2048.0; serve-point win A 60.8%, B 39.5%; Elo A 1257.4, B 1204.4; model uncertainty 0.005
* Form inputs: days since last match A 533, B 190; matches on record A 1, B 74; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Jan Hrazdil vs Maxim Groysman -- M15 Fergana R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210754:213868:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maxim Groysman (`KXITFMATCH-26NOV03HRAGRO-GRO`) | 0.35 / 0.48 (6) | 41.5% | 64.1% | 75.3% | 68.8% [68.0%-70.6%] | -- | -- | -- | -- | PASS | +22.6 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Jan Hrazdil (`KXITFMATCH-26NOV03HRAGRO-HRA`) | 0.55 / 0.69 (10) | 62.0% | 35.9% | 24.6% | 31.2% [29.4%-32.0%] | -- | -- | -- | -- | PASS | -26.1 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1017.0, B 124.0; serve-point win A 58.4%, B 38.8%; Elo A 1177.9, B 1309.7; model uncertainty 0.0133
* Form inputs: days since last match A 225, B 533; matches on record A 72, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03HRAGRO-GRO  (YES = Maxim Groysman)
Model: 64%
Kalshi: 42%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ilya Ignatov vs Aryan Lakshmanan -- M15 Fergana R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212767:213959:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ilya Ignatov (`KXITFMATCH-26NOV03IGNLAK-IGN`) | 0.05 / 0.16 (15) | 10.5% | 54.4% | 62.2% | 62.1% [61.7%-62.1%] | -- | -- | -- | -- | PASS | +43.9 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Aryan Lakshmanan (`KXITFMATCH-26NOV03IGNLAK-LAK`) | 0.86 / 0.94 (10) | 90.0% | 45.6% | 37.8% | 37.9% [37.9%-38.4%] | -- | -- | -- | -- | PASS | -44.4 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 122.0, B 548.0; serve-point win A 60.8%, B 40.1%; Elo A 1229.6, B 1145.6; model uncertainty 0.0024
* Form inputs: days since last match A 269, B 225; matches on record A 4, B 18; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03IGNLAK-IGN  (YES = Ilya Ignatov)
Model: 54%
Kalshi: 10%
Gap: +44 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Digvijay Pratap Singh vs Uladzislau Tarasevich -- M15 Fergana R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV03SINTAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Digvijay Pratap Singh (`KXITFMATCH-26NOV03SINTAR-SIN`) | 0.50 / 0.94 (25) | 72.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Uladzislau Tarasevich (`KXITFMATCH-26NOV03SINTAR-TAR`) | 0.05 / 0.53 (150) | 29.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rigele Te vs Yuta Kikuchi -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:144751:209043:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuta Kikuchi (`KXITFMATCH-26NOV03TEXKIK-KIK`) | 0.21 / 0.33 (37) | 27.0% | 47.1% | 67.5% | 56.2% [51.0%-61.7%] | -- | -- | -- | -- | PASS | +20.1 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rigele Te (`KXITFMATCH-26NOV03TEXKIK-TEX`) | 0.68 / 0.75 (60) | 71.5% | 52.9% | 32.5% | 43.8% [38.3%-49.0%] | -- | -- | -- | -- | PASS | -18.6 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1492.0, B 1925.0; serve-point win A 60.2%, B 40.4%; Elo A 1414.4, B 1381.1; model uncertainty 0.0533
* Form inputs: days since last match A 8, B 50; matches on record A 319, B 137; data quality A

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03TEXKIK-KIK  (YES = Yuta Kikuchi)
Model: 47%
Kalshi: 27%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: WIDE_SPREAD, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.005, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xiaoyin Yang vs Filip Peliwo -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:106290:212466:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Filip Peliwo (`KXITFMATCH-26NOV03YANPEL-PEL`) | 0.86 / 0.91 (147) | 88.5% | 75.8% | 78.1% | 77.7% [74.0%-80.8%] | -- | -- | -- | -- | PASS | -12.7 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Xiaoyin Yang (`KXITFMATCH-26NOV03YANPEL-YAN`) | 0.08 / 0.14 (122) | 11.0% | 24.2% | 21.9% | 22.3% [19.2%-26.0%] | -- | -- | -- | -- | PASS | +13.2 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 817.0, B 3377.0; serve-point win A 59.3%, B 35.2%; Elo A 1172.5, B 1385.5; model uncertainty 0.0342
* Form inputs: days since last match A 204, B 8; matches on record A 21, B 825; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.015, surface_pool_high -0.011, surface_dev_loose -0.010, surface_dev_tight +0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Zijiang Yang vs Zhao Zhao -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206888:208447:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zijiang Yang (`KXITFMATCH-26NOV03YANZHA-YAN`) | 0.18 / 0.25 (126) | 21.5% | 53.6% | 26.3% | 58.2% [54.1%-62.2%] | -- | -- | -- | -- | PASS | +32.1 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zhao Zhao (`KXITFMATCH-26NOV03YANZHA-ZHA`) | 0.73 / 0.79 (100) | 76.0% | 46.4% | 73.7% | 41.8% [37.8%-45.9%] | -- | -- | -- | -- | PASS | -29.6 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 208.0, B 155.0; serve-point win A 60.3%, B 40.4%; Elo A 1261.8, B 1177.3; model uncertainty 0.0403
* Form inputs: days since last match A 470, B 211; matches on record A 5, B 25; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV03YANZHA-YAN  (YES = Zijiang Yang)
Model: 54%
Kalshi: 22%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yajing Cao vs Zijun Jiang -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:223214:263764:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yajing Cao (`KXITFWMATCH-26NOV03CAOJIA-CAO`) | 0.06 / 0.08 (567) | 7.0% | 22.4% | 45.2% | 33.5% [32.5%-34.5%] | -- | -- | -- | -- | PASS | +15.3 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Zijun Jiang (`KXITFWMATCH-26NOV03CAOJIA-JIA`) | 0.92 / 0.94 (129) | 93.0% | 77.6% | 54.8% | 66.5% [65.5%-67.5%] | -- | -- | -- | -- | PASS | -15.3 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 105.0, B 178.0; serve-point win A 52.2%, B 42.1%; Elo A 1231.6, B 1360.3; model uncertainty 0.01
* Form inputs: days since last match A 190, B 190; matches on record A 55, B 73; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV03CAOJIA-CAO  (YES = Yajing Cao)
Model: 22%
Kalshi: 7%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sohyun Park vs Yujia Huang -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216213:264207:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yujia Huang (`KXITFWMATCH-26NOV03PARHUA-HUA`) | 0.54 / 0.63 (142) | 58.5% | 18.9% | 39.0% | 31.2% [22.4%-35.5%] | -- | -- | -- | -- | PASS | -39.6 pp | EXTREME (DATA_WARNING) | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sohyun Park (`KXITFWMATCH-26NOV03PARHUA-PAR`) | 0.36 / 0.41 (133) | 38.5% | 81.1% | 61.0% | 68.8% [64.5%-77.6%] | -- | -- | -- | -- | PASS | +42.6 pp | EXTREME (DATA_WARNING) | AGING | B / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3623.0, B 1640.0; serve-point win A 59.5%, B 47.2%; Elo A 1658.9, B 1447.1; model uncertainty 0.0657
* Form inputs: days since last match A 41, B 30; matches on record A 366, B 88; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV03PARHUA-PAR  (YES = Sohyun Park)
Model: 81%
Kalshi: 38%
Gap: +43 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.023, surface_pool_high -0.019, surface_dev_loose +0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Yufei Ren vs Yeonwoo Ku -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03RENKUX:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yeonwoo Ku (`KXITFWMATCH-26NOV03RENKUX-KUX`) | 0.66 / 0.74 (210) | 70.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yufei Ren (`KXITFWMATCH-26NOV03RENKUX-REN`) | 0.27 / 0.30 (132) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Rina Saigo vs Miho Kuramochi -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221099:246478:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miho Kuramochi (`KXITFWMATCH-26NOV03SAIKUR-KUR`) | 0.50 / 0.62 (7) | 56.0% | 49.2% | 52.7% | 51.6% [51.6%-52.1%] | -- | -- | -- | -- | PASS | -6.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Rina Saigo (`KXITFWMATCH-26NOV03SAIKUR-SAI`) | 0.37 / 0.51 (164) | 44.0% | 50.8% | 47.3% | 48.4% [47.9%-48.4%] | -- | -- | -- | -- | PASS | +6.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3065.0, B 3111.0; serve-point win A 52.8%, B 47.3%; Elo A 1547.5, B 1555.6; model uncertainty 0.0027
* Form inputs: days since last match A 10, B 44; matches on record A 396, B 279; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Marianna Shikhanova vs Shiyu Ye -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264085:269845:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marianna Shikhanova (`KXITFWMATCH-26NOV03SHIYEX-SHI`) | 0.18 / 0.29 (5) | 23.5% | 11.0% | 48.9% | 27.8% [26.0%-29.6%] | -- | -- | -- | -- | PASS | -12.5 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Shiyu Ye (`KXITFWMATCH-26NOV03SHIYEX-YEX`) | 0.68 / 0.79 (119) | 73.5% | 89.0% | 51.1% | 72.2% [70.4%-74.0%] | -- | -- | -- | -- | PASS | +15.5 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 49.0, B 931.0; serve-point win A 48.5%, B 42.4%; Elo A 1210.1, B 1380.8; model uncertainty 0.0179
* Form inputs: days since last match A 372, B 36; matches on record A 6, B 65; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV03SHIYEX-YEX  (YES = Shiyu Ye)
Model: 89%
Kalshi: 74%
Gap: +16 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.018, surface_pool_high -0.018, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Xiaotong Wang vs Wenfei Yu -- W15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 10:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T10:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:264184:270213:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xiaotong Wang (`KXITFWMATCH-26NOV03WANYUX-WAN`) | 0.32 / 0.40 (142) | 36.0% | 20.4% | 38.9% | 33.9% [32.4%-34.4%] | -- | -- | -- | -- | PASS | -15.6 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Wenfei Yu (`KXITFWMATCH-26NOV03WANYUX-YUX`) | 0.56 / 0.63 (4) | 59.5% | 79.6% | 61.1% | 66.1% [65.6%-67.6%] | -- | -- | -- | -- | PASS | +20.1 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 124.0, B 238.0; serve-point win A 49.8%, B 44.0%; Elo A 1230.6, B 1351.8; model uncertainty 0.0098
* Form inputs: days since last match A 239, B 190; matches on record A 3, B 35; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV03WANYUX-YUX  (YES = Wenfei Yu)
Model: 80%
Kalshi: 60%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.005, surface_dev_loose -0.005, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Janice Tjen vs Joanna Garland -- WTA Chennai R16

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-04 12:30Z (day placeholder, not a start time)
* Current expected start: 2026-11-04 11:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-04 10:15Z

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

WTA (TOUR_500_250) · Hard · scheduled 2026-11-04T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220466:222145:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Joanna Garland (`KXWTAMATCH-26NOV04TJEGAR-GAR`) | 0.29 / 0.33 (500) | 31.0% | 40.2% | 28.3% | 30.0% [28.7%-36.0%] | 32.4% | -- | 32.4% | MODEL_LONE_OUTLIER | PASS | +9.2 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |
| Janice Tjen (`KXWTAMATCH-26NOV04TJEGAR-TJE`) | 0.65 / 0.67 (1) | 66.0% | 59.8% | 71.7% | 70.0% [64.0%-71.3%] | 67.6% | -- | 67.6% | MODEL_LONE_OUTLIER | WATCH | -6.2 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 3631.0, B 2480.0; serve-point win A 64.8%, B 37.2%; Elo A 1889.9, B 1776.1; model uncertainty 0.0364
* Form inputs: days since last match A 0, B 0; matches on record A 187, B 396; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.018, surface_pool_high +0.013, surface_dev_loose +0.008, surface_dev_tight -0.012
* Derivatives listed: 7 (MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 7 carry a model probability
  * `KXWTAGTOTAL-26NOV04TJEGAR-15` Over 14.5 games: 0.03/0.94 mid 48.5%, model 99.8% (projection_v2.0 (prediction ledger)) -- gap +51.3 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTAGTOTAL-26NOV04TJEGAR-20` Over 19.5 games: 0.03/0.93 mid 48.0%, model 80.7% (projection_v2.0 (prediction ledger)) -- gap +32.7 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXWTASETWINNER-26NOV04TJEGAR-1-TJE` Will Janice Tjen win set 1 in the Janice Tjen vs Joanna Garland match: 0.02/0.93 mid 47.5%, model 56.6% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV04TJEGAR-2-TJE` Will Janice Tjen win set 2 in the Janice Tjen vs Joanna Garland match: 0.01/0.94 mid 47.5%, model 56.6% (projection_v2.0 (prediction ledger)) -- gap +9.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV04TJEGAR-1-GAR` Will Joanna Garland win set 1 in the Janice Tjen vs Joanna Garland match: 0.02/0.93 mid 47.5%, model 43.4% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTASETWINNER-26NOV04TJEGAR-2-GAR` Will Joanna Garland win set 2 in the Janice Tjen vs Joanna Garland match: 0.01/0.94 mid 47.5%, model 43.4% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXWTAGTOTAL-26NOV04TJEGAR-25` Over 24.5 games: 0.05/0.93 mid 49.0%, model 52.8% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Han Shi vs Sakura Hosogi -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220718:222559:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sakura Hosogi (`KXITFWMATCH-26NOV04SHIHOS-HOS`) | 0.09 / 0.12 (112) | 10.5% | 37.0% | 35.9% | 40.5% [38.4%-44.1%] | -- | -- | -- | -- | WATCH | +26.5 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Han Shi (`KXITFWMATCH-26NOV04SHIHOS-SHI`) | 0.87 / 0.90 (100) | 88.5% | 63.0% | 64.1% | 59.5% [55.9%-61.6%] | -- | -- | -- | -- | PASS | -25.5 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 3226.0, B 2576.0; serve-point win A 53.6%, B 48.9%; Elo A 1600.6, B 1583.4; model uncertainty 0.0287
* Form inputs: days since last match A 190, B 190; matches on record A 228, B 392; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04SHIHOS-HOS  (YES = Sakura Hosogi)
Model: 37%
Kalshi: 10%
Gap: +26 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.005, surface_dev_loose +0.021, surface_dev_tight -0.026
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Shimizu / Yoshioka vs Hosoki / Nishimoto -- W35 Hamamatsu R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 11:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T11:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV04SHIYOSHOSNIS:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hosoki / Nishimoto (`KXITFWDOUBLES-26NOV04SHIYOSHOSNIS-HOSNIS`) | 0.05 / 0.89 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Shimizu / Yoshioka (`KXITFWDOUBLES-26NOV04SHIYOSHOSNIS-SHIYOS`) | 0.05 / 0.89 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ye Hongyu vs Xirui Han -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212067:212472:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Xirui Han (`KXITFMATCH-26NOV04HONHAN-HAN`) | 0.61 / 0.66 (156) | 63.5% | 63.2% | 67.2% | 65.8% [65.1%-67.8%] | -- | -- | -- | -- | PASS | -0.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ye Hongyu (`KXITFMATCH-26NOV04HONHAN-HON`) | 0.32 / 0.34 (1) | 33.0% | 36.8% | 32.8% | 34.2% [32.2%-34.8%] | -- | -- | -- | -- | PASS | +3.8 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 644.0, B 542.0; serve-point win A 56.4%, B 41.0%; Elo A 1043.9, B 1153.8; model uncertainty 0.0131
* Form inputs: days since last match A 204, B 379; matches on record A 32, B 15; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose -0.010, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Millen Hurrion vs Alexey Aleshchev -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:134310:209140:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alexey Aleshchev (`KXITFMATCH-26NOV04HURALE-ALE`) | 0.05 / 0.07 (34) | 6.0% | 10.2% | 5.8% | 8.0% [6.4%-10.6%] | -- | -- | -- | -- | WATCH | +4.2 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Millen Hurrion (`KXITFMATCH-26NOV04HURALE-HUR`) | 0.89 / 0.95 (100) | 92.0% | 89.8% | 94.2% | 92.0% [89.4%-93.6%] | -- | -- | -- | -- | PASS | -2.2 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2993.0, B 1173.0; serve-point win A 63.6%, B 46.1%; Elo A 1434.9, B 1059.7; model uncertainty 0.0211
* Form inputs: days since last match A 92, B 190; matches on record A 179, B 69; data quality C
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.007, surface_pool_high -0.008, surface_dev_loose +0.009, surface_dev_tight -0.007
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Madhwin Kamath vs David Eichenseher -- M15 Fergana R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:209979:212631:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Eichenseher (`KXITFMATCH-26NOV04KAMEIC-EIC`) | 0.51 / 0.79 (2) | 65.0% | 46.2% | 42.9% | 50.0% [47.9%-53.1%] | -- | -- | -- | -- | PASS | -18.8 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Madhwin Kamath (`KXITFMATCH-26NOV04KAMEIC-KAM`) | 0.06 / 0.38 (2) | 22.0% | 53.8% | 57.1% | 50.0% [46.9%-52.0%] | -- | -- | -- | -- | PASS | +31.8 pp | EXTREME (DATA_WARNING) | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 843.0, B 1106.0; serve-point win A 61.0%, B 39.8%; Elo A 1167.2, B 1191.7; model uncertainty 0.0257
* Form inputs: days since last match A 190, B 190; matches on record A 53, B 30; data quality C

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV04KAMEIC-KAM  (YES = Madhwin Kamath)
Model: 54%
Kalshi: 22%
Gap: +32 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oleg Kolninov vs Grigoriy Lomakin -- M15 Fergana R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200441:212809:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oleg Kolninov (`KXITFMATCH-26NOV04KOLLOM-KOL`) | 0.06 / 0.27 (14) | 16.5% | 59.0% | 75.6% | 69.7% [69.7%-69.7%] | -- | -- | -- | -- | PASS | +42.5 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Grigoriy Lomakin (`KXITFMATCH-26NOV04KOLLOM-LOM`) | 0.75 / 0.94 (110) | 84.5% | 41.0% | 24.3% | 30.3% [30.3%-30.3%] | -- | -- | -- | -- | PASS | -43.5 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A 0.0, B 2308.0; serve-point win A 61.4%, B 40.3%; Elo A 1284.0, B 1138.2; model uncertainty 0.0
* Form inputs: days since last match A 946, B 50; matches on record A 1, B 336; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV04KOLLOM-KOL  (YES = Oleg Kolninov)
Model: 59%
Kalshi: 16%
Gap: +43 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, PLAYER_IDENTITY_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Arkhip Kozlov vs Qian Sun -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04KOZSUN:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arkhip Kozlov (`KXITFMATCH-26NOV04KOZSUN-KOZ`) | 0.06 / 0.09 (408) | 7.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Qian Sun (`KXITFMATCH-26NOV04KOZSUN-SUN`) | 0.90 / 0.94 (432) | 92.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Makar Krivoshchekov vs Abdurakhmon Karimov -- M15 Fergana R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04KRIKAR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Abdurakhmon Karimov (`KXITFMATCH-26NOV04KRIKAR-KAR`) | 0.15 / 0.29 (8) | 22.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Makar Krivoshchekov (`KXITFMATCH-26NOV04KRIKAR-KRI`) | 0.68 / 0.86 (12) | 77.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lingxi Zhao vs James Connel -- M15 Maanshan R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:206789:212250:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| James Connel (`KXITFMATCH-26NOV04ZHACON-CON`) | 0.50 / 0.54 (198) | 52.0% | 68.8% | 73.8% | 66.6% [65.1%-68.6%] | -- | -- | -- | -- | PASS | +16.8 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Lingxi Zhao (`KXITFMATCH-26NOV04ZHACON-ZHA`) | 0.45 / 0.48 (100) | 46.5% | 31.2% | 26.2% | 33.4% [31.4%-34.8%] | -- | -- | -- | -- | PASS | -15.2 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 337.0, B 844.0; serve-point win A 57.1%, B 39.2%; Elo A 1269.4, B 1378.7; model uncertainty 0.017
* Form inputs: days since last match A 379, B 190; matches on record A 39, B 26; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV04ZHACON-CON  (YES = James Connel)
Model: 69%
Kalshi: 52%
Gap: +17 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.014, surface_pool_high +0.009, surface_dev_loose -0.000, surface_dev_tight +0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Alan Zinatulin vs Muzammil Murtaza -- M15 Fergana R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 11:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04ZINMUR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Muzammil Murtaza (`KXITFMATCH-26NOV04ZINMUR-MUR`) | 0.33 / 0.53 (1) | 43.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alan Zinatulin (`KXITFMATCH-26NOV04ZINMUR-ZIN`) | 0.47 / 0.53 (1) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Naho Sato vs Jia-Jing Lu -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:203288:220997:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jia-Jing Lu (`KXITFWMATCH-26NOV04SATLUX-LUX`) | 0.35 / 0.51 (165) | 43.0% | 71.9% | 84.9% | 75.8% [68.1%-80.5%] | -- | -- | -- | -- | PASS | +28.9 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Naho Sato (`KXITFWMATCH-26NOV04SATLUX-SAT`) | 0.50 / 0.59 (60) | 54.5% | 28.1% | 15.1% | 24.2% [19.5%-31.9%] | -- | -- | -- | -- | PASS | -26.4 pp | EXTREME (DATA_WARNING) | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1522.0, B 3089.0; serve-point win A 48.8%, B 46.9%; Elo A 1476.0, B 1582.4; model uncertainty 0.0622
* Form inputs: days since last match A 197, B 28; matches on record A 304, B 905; data quality B

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04SATLUX-LUX  (YES = Jia-Jing Lu)
Model: 72%
Kalshi: 43%
Gap: +29 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: B (LIMITED)
Reasons: WIDE_SPREAD, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.008, surface_pool_high +0.000, surface_dev_loose -0.008, surface_dev_tight +0.009
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Katie Swan vs Aoi Ito -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 11:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T11:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215042:256684:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aoi Ito (`KXITFWMATCH-26NOV04SWAITO-ITO`) | 0.29 / 0.33 (1) | 31.0% | 44.3% | 17.0% | 29.8% [23.7%-42.6%] | -- | -- | -- | -- | PASS | +13.3 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Katie Swan (`KXITFWMATCH-26NOV04SWAITO-SWA`) | 0.65 / 0.66 (73) | 65.5% | 55.7% | 83.0% | 70.2% [57.4%-76.3%] | -- | -- | -- | -- | WATCH | -9.8 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2343.0, B 2722.0; serve-point win A 56.1%, B 45.0%; Elo A 1722.0, B 1759.4; model uncertainty 0.0946
* Form inputs: days since last match A 39, B 10; matches on record A 387, B 304; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.022, surface_pool_high -0.019, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Nuno Borges vs Karen Khachanov -- ATP Paris R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-04 12:00Z
* Current expected start: 2026-11-04 12:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-04 11:15Z

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-04T05:00:00+00:00 as not a valid time; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min

ATP (MASTERS_1000) · Hard · scheduled 2026-11-04T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111575:132686:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nuno Borges (`KXATPMATCH-26NOV04BORKHA-BOR`) | 0.34 / 0.35 (500) | 34.5% | 33.6% | 35.0% | 35.9% [35.5%-36.8%] | -- | -- | -- | -- | PASS | -0.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Karen Khachanov (`KXATPMATCH-26NOV04BORKHA-KHA`) | 0.63 / 0.67 (744) | 65.0% | 66.4% | 65.0% | 64.1% [63.2%-64.5%] | -- | -- | -- | -- | PASS | +1.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5796.0, B 5872.0; serve-point win A 65.7%, B 30.8%; Elo A 1861.3, B 1938.0; model uncertainty 0.0065
* Form inputs: days since last match A 2, B 1; matches on record A 555, B 766; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.004, surface_pool_high +0.005, surface_dev_loose -0.004, surface_dev_tight +0.004
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPEXACTMATCH-26NOV04BORKHA-BOR20` Will Nuno Borges win the Nuno Borges vs Karen Khachanov match by a set score of 2-0?: 0.01/0.94 mid 47.5%, model 15.1% (projection_v2.0 (prediction ledger)) -- gap -32.4 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04BORKHA-BOR21` Will Nuno Borges win the Nuno Borges vs Karen Khachanov match by a set score of 2-1?: 0.02/0.93 mid 47.5%, model 18.5% (projection_v2.0 (prediction ledger)) -- gap -29.0 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04BORKHA-KHA21` Will Karen Khachanov win the Nuno Borges vs Karen Khachanov match by a set score of 2-1?: 0.01/0.94 mid 47.5%, model 29.0% (projection_v2.0 (prediction ledger)) -- gap -18.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV04BORKHA-1-KHA` Will Karen Khachanov win set 1 in the Nuno Borges vs Karen Khachanov match: 0.02/0.93 mid 47.5%, model 61.1% (projection_v2.0 (prediction ledger)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV04BORKHA-2-KHA` Will Karen Khachanov win set 2 in the Nuno Borges vs Karen Khachanov match: 0.02/0.93 mid 47.5%, model 61.1% (projection_v2.0 (prediction ledger)) -- gap +13.6 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV04BORKHA-23` Over 22.5 games: 0.47/0.54 mid 50.5%, model 63.4% (projection_v2.0 (prediction ledger)) -- gap +12.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV04BORKHA-28` Over 27.5 games: 0.28/0.34 mid 31.0%, model 42.3% (projection_v2.0 (prediction ledger)) -- gap +11.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV04BORKHA-KHA6` Will Karen Khachanov win at least 5.5 more games than Nuno Borges?: 0.19/0.23 mid 21.0%, model 10.1% (projection_v2.0 (prediction ledger)) -- gap -10.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04BORKHA-KHA20` Will Karen Khachanov win the Nuno Borges vs Karen Khachanov match by a set score of 2-0?: 0.01/0.94 mid 47.5%, model 37.4% (projection_v2.0 (prediction ledger)) -- gap -10.1 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV04BORKHA-1-BOR` Will Nuno Borges win set 1 in the Nuno Borges vs Karen Khachanov match: 0.02/0.93 mid 47.5%, model 38.9% (projection_v2.0 (prediction ledger)) -- gap -8.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV04BORKHA-2-BOR` Will Nuno Borges win set 2 in the Nuno Borges vs Karen Khachanov match: 0.02/0.93 mid 47.5%, model 38.9% (projection_v2.0 (prediction ledger)) -- gap -8.6 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV04BORKHA-18` Over 17.5 games: 0.87/0.90 mid 88.5%, model 95.7% (projection_v2.0 (prediction ledger)) -- gap +7.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV04BORKHA-KHA3` Will Karen Khachanov win at least 2.5 more games than Nuno Borges?: 0.50/0.57 mid 53.5%, model 48.7% (projection_v2.0 (prediction ledger)) -- gap -4.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV04BORKHA-BOR2` Will Nuno Borges win at least 1.5 more games than Karen Khachanov?: 0.27/0.32 mid 29.5%, model 26.2% (projection_v2.0 (prediction ledger)) -- gap -3.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Tommy Paul vs Daniel Merida -- ATP Paris R32

**START STATUS: ESTIMATED_UPCOMING** -- BET BLOCKED
* Nominal schedule: 2026-11-04 12:00Z
* Current expected start: 2026-11-04 12:00Z
* Source: KALSHI_NOMINAL; confidence LOW
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: 2026-11-04 11:15Z

* Status notes: NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source)

ATP (MASTERS_1000) · Hard · scheduled 2026-11-04T12:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:26NOV04PAUMER:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Merida (`KXATPMATCH-26NOV04PAUMER-MER`) | 0.05 / 0.93 (1) | 49.0% | 24.1% | -- | -- [-----] | -- | -- | -- | -- | -- | -24.9 pp | HIGH_REVIEW (DATA_WARNING) | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Tommy Paul (`KXATPMATCH-26NOV04PAUMER-PAU`) | 0.06 / 0.93 (1) | 49.5% | 75.9% | -- | -- [-----] | -- | -- | -- | -- | -- | +26.4 pp | EXTREME (DATA_WARNING) | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 64.2%, B 41.3%; Elo A 2034.6, B 1779.9; model uncertainty None
* Form inputs: days since last match A 4, B 1; matches on record A 732, B 357; data quality A

```
DISCREPANCY SANITY CHECK  KXATPMATCH-26NOV04PAUMER-PAU  (YES = Tommy Paul)
Model: 76%
Kalshi: 50%
Gap: +26 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, PLAYER_IDENTITY_RISK, EVENT_MAPPING_RISK, NO_EXTERNAL_REFERENCE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: BET_BLOCKED_START_STATUS; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ya-Hsin Lee / Fang-Hsien Wu vs Venus Williams / Yifan Xu -- WTA Hong Kong R16

**START STATUS: ESTIMATED_UPCOMING**
* Nominal schedule: 2026-11-03 09:00Z
* Current expected start: 2026-11-04 12:00Z
* Source: LIVE_SCHEDULE:espn_wta; confidence MEDIUM
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: 2026-11-04 11:15Z

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL

DOUBLES (TOUR_500_250) · surface ? · scheduled 2026-11-03T09:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV03LEEFANWILYIF:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ya-Hsin Lee / Fang-Hsien Wu (`KXWTADOUBLES-26NOV03LEEFANWILYIF-LEEFAN`) | 0.49 / 0.50 (48) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Venus Williams / Yifan Xu (`KXWTADOUBLES-26NOV03LEEFANWILYIF-WILYIF`) | 0.51 / 0.52 (675) | 51.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; SCHEDULED_START_PASSED; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE

## Hsun Lin / Lorusso vs Kuan Lai / Sarksian -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04HSULORKUASAR:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hsun Lin / Lorusso (`KXITFDOUBLES-26NOV04HSULORKUASAR-HSULOR`) | 0.32 / 0.63 (67) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kuan Lai / Sarksian (`KXITFDOUBLES-26NOV04HSULORKUASAR-KUASAR`) | 0.24 / 0.61 (64) | 42.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Petr Nouza / Michael Venus vs Marcelo Arevalo / Mate Pavic -- ATP Paris R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-04T05:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-04T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04NOUVENAREPAV:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marcelo Arevalo / Mate Pavic (`KXATPDOUBLES-26NOV04NOUVENAREPAV-AREPAV`) | 0.30 / 0.93 (2) | 61.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Petr Nouza / Michael Venus (`KXATPDOUBLES-26NOV04NOUVENAREPAV-NOUVEN`) | 0.05 / 0.75 (2) | 40.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Wang / Zheng vs Yang / Zhang -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04WANZHEYANZHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wang / Zheng (`KXITFDOUBLES-26NOV04WANZHEYANZHA-WANZHE`) | 0.04 / 0.33 (37) | 18.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yang / Zhang (`KXITFDOUBLES-26NOV04WANZHEYANZHA-YANZHA`) | 0.60 / 0.85 (166) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Yuki Naito vs Sara Saito -- W100 Incheon R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:216044:260170:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yuki Naito (`KXITFWMATCH-26NOV04NAISAI-NAI`) | 0.54 / 0.58 (100) | 56.0% | 42.3% | 59.0% | 50.0% [43.6%-53.2%] | -- | -- | -- | -- | PASS | -13.7 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Sara Saito (`KXITFWMATCH-26NOV04NAISAI-SAI`) | 0.40 / 0.45 (100) | 42.5% | 57.7% | 41.0% | 50.0% [46.8%-56.4%] | -- | -- | -- | -- | PASS | +15.2 pp | HIGH_REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2186.0, B 3341.0; serve-point win A 52.6%, B 45.9%; Elo A 1477.3, B 1574.9; model uncertainty 0.0479
* Form inputs: days since last match A 43, B 36; matches on record A 359, B 198; data quality A

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04NAISAI-SAI  (YES = Sara Saito)
Model: 58%
Kalshi: 42%
Gap: +15 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: A (ADEQUATE)
Reasons: LOW_DISPLAYED_LIQUIDITY, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.011, surface_pool_high -0.011, surface_dev_loose +0.011, surface_dev_tight -0.011
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ovcharenko / Savinykh vs Lee / Eum Lee -- W100 Incheon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 12:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T12:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV04OVCSAVLEEEUM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lee / Eum Lee (`KXITFWDOUBLES-26NOV04OVCSAVLEEEUM-LEEEUM`) | 0.08 / 0.52 (52) | 30.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ovcharenko / Savinykh (`KXITFWDOUBLES-26NOV04OVCSAVLEEEUM-OVCSAV`) | 0.41 / 0.71 (86) | 56.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Daniele Augenti vs Alexander Wagner -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04AUGWAG:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniele Augenti (`KXITFMATCH-26NOV04AUGWAG-AUG`) | 0.06 / 0.93 (2) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Alexander Wagner (`KXITFMATCH-26NOV04AUGWAG-WAG`) | 0.07 / 0.93 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Stefan Horia Haita vs Alessio Basile -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-04T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211450:213066:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alessio Basile (`KXITFMATCH-26NOV04HAIBAS-BAS`) | 0.31 / 0.50 (6) | 40.5% | 62.9% | 82.5% | 63.2% [53.6%-72.0%] | -- | -- | -- | -- | PASS | +22.4 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Stefan Horia Haita (`KXITFMATCH-26NOV04HAIBAS-HAI`) | 0.50 / 0.63 (5) | 56.5% | 37.1% | 17.5% | 36.8% [28.0%-46.4%] | -- | -- | -- | -- | PASS | -19.4 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 614.0, B 952.0; serve-point win A 58.2%, B 39.2%; Elo A 1224.1, B 1252.5; model uncertainty 0.0922
* Form inputs: days since last match A 120, B 344; matches on record A 21, B 43; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV04HAIBAS-BAS  (YES = Alessio Basile)
Model: 63%
Kalshi: 40%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.019, surface_dev_loose -0.024, surface_dev_tight +0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## David Tixhon vs Alan Wazny -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-04T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207591:213048:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| David Tixhon (`KXITFMATCH-26NOV04TIXWAZ-TIX`) | 0.05 / 0.25 (16) | 15.0% | 35.4% | 57.3% | 50.0% [49.0%-51.0%] | -- | -- | -- | -- | PASS | +20.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alan Wazny (`KXITFMATCH-26NOV04TIXWAZ-WAZ`) | 0.80 / 0.94 (10) | 87.0% | 64.6% | 42.7% | 50.0% [49.0%-51.0%] | -- | -- | -- | -- | PASS | -22.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 0.0, B 1502.0; serve-point win A 57.1%, B 40.1%; Elo A 1285.9, B 1283.8; model uncertainty 0.0104
* Form inputs: days since last match A 498, B 50; matches on record A 1, B 36; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV04TIXWAZ-TIX  (YES = David Tixhon)
Model: 35%
Kalshi: 15%
Gap: +20 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Martin Van Der Meerschen vs Beren Tan -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-04T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:207592:210738:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beren Tan (`KXITFMATCH-26NOV04VANTAN-TAN`) | 0.06 / 0.93 (2) | 49.5% | 13.2% | 37.7% | 25.7% [24.2%-26.5%] | -- | -- | -- | -- | PASS | -36.3 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Martin Van Der Meerschen (`KXITFMATCH-26NOV04VANTAN-VAN`) | 0.07 / 0.93 (2) | 50.0% | 86.8% | 62.3% | 74.3% [73.5%-75.8%] | -- | -- | -- | -- | PASS | +36.8 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2032.0, B 35.0; serve-point win A 62.9%, B 45.7%; Elo A 1326.4, B 1135.5; model uncertainty 0.0117
* Form inputs: days since last match A 190, B 365; matches on record A 103, B 5; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV04VANTAN-VAN  (YES = Martin Van Der Meerschen)
Model: 87%
Kalshi: 50%
Gap: +37 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.008, surface_pool_high -0.009, surface_dev_loose +0.004, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Facundo Yunis vs Andrey Chepelev -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-04T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:200184:209947:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrey Chepelev (`KXITFMATCH-26NOV04YUNCHE-CHE`) | 0.73 / 0.94 (25) | 83.5% | 87.1% | 72.7% | 84.9% [83.9%-86.7%] | -- | -- | -- | -- | PASS | +3.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Facundo Yunis (`KXITFMATCH-26NOV04YUNCHE-YUN`) | 0.06 / 0.21 (37) | 13.5% | 12.9% | 27.4% | 15.1% [13.3%-16.1%] | -- | -- | -- | -- | PASS | -0.6 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 77.0, B 3714.0; serve-point win A 53.9%, B 37.4%; Elo A 1142.1, B 1452.1; model uncertainty 0.0138
* Form inputs: days since last match A 449, B 43; matches on record A 46, B 605; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.009, surface_pool_high -0.018, surface_dev_loose -0.003, surface_dev_tight -0.002
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ilary Pistola vs Semra Aksu -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-04T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220798:270265:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Semra Aksu (`KXITFWMATCH-26NOV04PISAKS-AKS`) | 0.04 / 0.76 (88) | 40.0% | 28.4% | 63.1% | 36.4% [35.4%-36.4%] | -- | -- | -- | -- | PASS | -11.6 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ilary Pistola (`KXITFWMATCH-26NOV04PISAKS-PIS`) | 0.28 / 0.93 (2) | 60.5% | 71.6% | 36.9% | 63.6% [63.6%-64.6%] | -- | -- | -- | -- | PASS | +11.1 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 175.0, B 0.0; serve-point win A 55.4%, B 48.9%; Elo A 1281.7, B 1182.8; model uncertainty 0.0051
* Form inputs: days since last match A 105, B 44; matches on record A 5, B 37; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Diana-Ioana Simionescu vs Greta Nemcsek -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV04SIMNEM:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Greta Nemcsek (`KXITFWMATCH-26NOV04SIMNEM-NEM`) | 0.04 / 0.53 (37) | 28.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Diana-Ioana Simionescu (`KXITFWMATCH-26NOV04SIMNEM-SIM`) | 0.51 / 0.94 (10) | 72.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Theresa Stabauer vs Angelina Wirges -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 12:30Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T12:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV04STAWIR:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Theresa Stabauer (`KXITFWMATCH-26NOV04STAWIR-STA`) | 0.04 / 0.46 (12) | 25.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Angelina Wirges (`KXITFWMATCH-26NOV04STAWIR-WIR`) | 0.58 / 0.93 (2) | 75.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anastasia Zakharova vs Vaishnavi Adkar -- WTA Chennai R16

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-04 12:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_wta marks 2026-11-05T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

WTA (TOUR_500_250) · Hard · scheduled 2026-11-04T12:30:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `WTA:220435:261038:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vaishnavi Adkar (`KXWTAMATCH-26NOV04ZAKADK-ADK`) | 0.12 / 0.27 (1) | 19.5% | 20.1% | 34.0% | 27.0% [19.7%-30.1%] | -- | -- | -- | -- | PASS | +0.6 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anastasia Zakharova (`KXWTAMATCH-26NOV04ZAKADK-ZAK`) | 0.69 / 0.89 (150) | 79.0% | 79.9% | 66.0% | 73.0% [69.8%-80.3%] | -- | -- | -- | -- | PASS | +0.9 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4628.0, B 2186.0; serve-point win A 57.8%, B 48.5%; Elo A 1807.2, B 1540.6; model uncertainty 0.0521
* Form inputs: days since last match A 0, B 190; matches on record A 485, B 143; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.017, surface_pool_high -0.018, surface_dev_loose -0.004, surface_dev_tight +0.000
* Derivatives listed: 4 (MATCH_WINNER, SET_WINNER); 4 carry a model probability
  * `KXWTASETWINNER-26NOV04ZAKADK-1-ZAK` Will Anastasia Zakharova win set 1 in the Anastasia Zakharova vs Vaishnavi Adkar match: 0.01/0.94 mid 47.5%, model 71.2% (projection_v2.0 (prediction ledger)) -- gap +23.7 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV04ZAKADK-2-ZAK` Will Anastasia Zakharova win set 2 in the Anastasia Zakharova vs Vaishnavi Adkar match: 0.01/0.94 mid 47.5%, model 71.2% (projection_v2.0 (prediction ledger)) -- gap +23.7 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV04ZAKADK-1-ADK` Will Vaishnavi Adkar win set 1 in the Anastasia Zakharova vs Vaishnavi Adkar match: 0.01/0.94 mid 47.5%, model 28.8% (projection_v2.0 (prediction ledger)) -- gap -18.7 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data LIMITED
  * `KXWTASETWINNER-26NOV04ZAKADK-2-ADK` Will Vaishnavi Adkar win set 2 in the Anastasia Zakharova vs Vaishnavi Adkar match: 0.01/0.94 mid 47.5%, model 28.8% (projection_v2.0 (prediction ledger)) -- gap -18.7 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data LIMITED
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Mattia Bellucci vs Arthur Rinderknech -- ATP Paris R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-04 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-04T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-04T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126239:208233:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mattia Bellucci (`KXATPMATCH-26NOV04BELRIN-BEL`) | 0.56 / 0.57 (1347) | 56.5% | 55.0% | 50.5% | 50.5% [49.5%-51.0%] | 55.6% | -- | -- | INSUFFICIENT_INPUTS | PASS | -1.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Arthur Rinderknech (`KXATPMATCH-26NOV04BELRIN-RIN`) | 0.43 / 0.44 (81) | 43.5% | 45.0% | 49.5% | 49.5% [49.0%-50.5%] | 44.4% | -- | -- | INSUFFICIENT_INPUTS | SHADOW_BET | +1.5 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 5542.0, B 5481.0; serve-point win A 68.4%, B 32.7%; Elo A 1832.6, B 1825.9; model uncertainty 0.0072
* Form inputs: days since last match A 1, B 0; matches on record A 434, B 570; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.010
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV04BELRIN-19` Over 18.5 games: 0.42/0.93 mid 67.5%, model 93.3% (projection_v2.0 (prediction ledger)) -- gap +25.9 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV04BELRIN-BEL5` Will Mattia Bellucci win at least 4.5 more games than Arthur Rinderknech?: 0.01/0.58 mid 29.5%, model 13.9% (projection_v2.0 (prediction ledger)) -- gap -15.7 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04BELRIN-BEL21` Will Mattia Bellucci win the Mattia Bellucci vs Arthur Rinderknech match by a set score of 2-1?: 0.01/0.28 mid 14.5%, model 26.5% (projection_v2.0 (prediction ledger)) -- gap +12.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV04BELRIN-RIN2` Will Arthur Rinderknech win at least 1.5 more games than Mattia Bellucci?: 0.01/0.93 mid 47.0%, model 36.7% (projection_v2.0 (prediction ledger)) -- gap -10.3 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV04BELRIN-24` Over 23.5 games: 0.48/0.50 mid 49.0%, model 57.9% (projection_v2.0 (prediction ledger)) -- gap +8.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04BELRIN-BEL20` Will Mattia Bellucci win the Mattia Bellucci vs Arthur Rinderknech match by a set score of 2-0?: 0.01/0.40 mid 20.5%, model 28.4% (projection_v2.0 (prediction ledger)) -- gap +7.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV04BELRIN-2-BEL` Will Mattia Bellucci win set 2 in the Mattia Bellucci vs Arthur Rinderknech match: 0.02/0.93 mid 47.5%, model 53.3% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04BELRIN-RIN20` Will Arthur Rinderknech win the Mattia Bellucci vs Arthur Rinderknech match by a set score of 2-0?: 0.01/0.31 mid 16.0%, model 21.8% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV04BELRIN-29` Over 28.5 games: 0.32/0.41 mid 36.5%, model 41.4% (projection_v2.0 (prediction ledger)) -- gap +4.9 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04BELRIN-RIN21` Will Arthur Rinderknech win the Mattia Bellucci vs Arthur Rinderknech match by a set score of 2-1?: 0.13/0.25 mid 19.0%, model 23.2% (projection_v2.0 (prediction ledger)) -- gap +4.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV04BELRIN-BEL2` Will Mattia Bellucci win at least 1.5 more games than Arthur Rinderknech?: 0.49/0.52 mid 50.5%, model 46.4% (projection_v2.0 (prediction ledger)) -- gap -4.1 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV04BELRIN-1-RIN` Will Arthur Rinderknech win set 1 in the Mattia Bellucci vs Arthur Rinderknech match: 0.43/0.45 mid 44.0%, model 46.7% (projection_v2.0 (prediction ledger)) -- gap +2.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV04BELRIN-1-BEL` Will Mattia Bellucci win set 1 in the Mattia Bellucci vs Arthur Rinderknech match: 0.55/0.56 mid 55.5%, model 53.3% (projection_v2.0 (prediction ledger)) -- gap -2.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV04BELRIN-2-RIN` Will Arthur Rinderknech win set 2 in the Mattia Bellucci vs Arthur Rinderknech match: 0.02/0.93 mid 47.5%, model 46.7% (projection_v2.0 (prediction ledger)) -- gap -0.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; EXTERNAL_PRICE_STALE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Matteo Berrettini vs Ugo Humbert -- ATP Paris R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-04 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min (never observed by a live source); NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-04T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:126610:200005:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matteo Berrettini (`KXATPMATCH-26NOV04BERHUM-BER`) | 0.50 / 0.74 (767) | 62.0% | 48.1% | 49.5% | 48.6% [45.4%-52.8%] | -- | -- | -- | -- | PASS | -13.9 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ugo Humbert (`KXATPMATCH-26NOV04BERHUM-HUM`) | 0.26 / 0.54 (1) | 40.0% | 51.9% | 50.5% | 51.4% [47.2%-54.6%] | -- | -- | -- | -- | PASS | +11.9 pp | REVIEW | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 4209.0, B 4891.0; serve-point win A 70.0%, B 29.6%; Elo A 1912.1, B 1942.4; model uncertainty 0.0372
* Form inputs: days since last match A 4, B 1; matches on record A 565, B 626; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.033, surface_pool_high -0.032, surface_dev_loose -0.005, surface_dev_tight +0.009
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPSETWINNER-26NOV04BERHUM-1-HUM` Will Ugo Humbert win set 1 in the Matteo Berrettini vs Ugo Humbert match: 0.01/0.94 mid 47.5%, model 51.3% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV04BERHUM-2-HUM` Will Ugo Humbert win set 2 in the Matteo Berrettini vs Ugo Humbert match: 0.01/0.94 mid 47.5%, model 51.3% (projection_v2.0 (prediction ledger)) -- gap +3.8 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV04BERHUM-1-BER` Will Matteo Berrettini win set 1 in the Matteo Berrettini vs Ugo Humbert match: 0.01/0.94 mid 47.5%, model 48.7% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV04BERHUM-2-BER` Will Matteo Berrettini win set 2 in the Matteo Berrettini vs Ugo Humbert match: 0.01/0.94 mid 47.5%, model 48.7% (projection_v2.0 (prediction ledger)) -- gap +1.2 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Chirag Duhan vs Amir Asylkozhaev -- M15 Fergana R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210003:213741:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amir Asylkozhaev (`KXITFMATCH-26NOV04DUHASY-ASY`) | 0.05 / 0.32 (129) | 18.5% | 41.6% | 53.6% | 50.0% [50.0%-50.0%] | -- | -- | -- | -- | PASS | +23.1 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Chirag Duhan (`KXITFMATCH-26NOV04DUHASY-DUH`) | 0.64 / 0.94 (10) | 79.0% | 58.4% | 46.4% | 50.0% [50.0%-50.0%] | -- | -- | -- | -- | PASS | -20.6 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1525.0, B 43.0; serve-point win A 60.6%, B 41.0%; Elo A 1258.0, B 1260.9; model uncertainty 0.0
* Form inputs: days since last match A 225, B 638; matches on record A 96, B 1; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV04DUHASY-ASY  (YES = Amir Asylkozhaev)
Model: 42%
Kalshi: 18%
Gap: +23 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, LEVEL_TRANSFER_RISK, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Tomas Martin Etcheverry vs Alex de Minaur -- ATP Paris R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-04 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-04T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-04T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:144869:200282:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex de Minaur (`KXATPMATCH-26NOV04ETCDE-DE`) | 0.76 / 0.77 (13) | 76.5% | 77.5% | 79.2% | 81.0% [80.2%-82.3%] | 75.5% | -- | 75.5% | MODEL_LONE_OUTLIER | SHADOW_BET | +1.0 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Tomas Martin Etcheverry (`KXATPMATCH-26NOV04ETCDE-ETC`) | 0.21 / 0.24 (1532) | 22.5% | 22.5% | 20.8% | 19.1% [17.7%-19.8%] | 24.5% | -- | 24.5% | ALL_THREE_DISAGREE | PASS | +0.0 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 5577.0, B 6579.0; serve-point win A 61.9%, B 31.9%; Elo A 1775.7, B 2099.2; model uncertainty 0.0102
* Form inputs: days since last match A 0, B 2; matches on record A 650, B 694; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.003, surface_pool_high +0.004, surface_dev_loose +0.001, surface_dev_tight -0.001
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV04ETCDE-18` Over 17.5 games: 0.07/0.93 mid 50.0%, model 91.1% (projection_v2.0 (prediction ledger)) -- gap +41.1 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04ETCDE-ETC20` Will Tomas Martin Etcheverry win the Tomas Martin Etcheverry vs Alex de Minaur match by a set score of 2-0?: 0.02/0.93 mid 47.5%, model 9.4% (projection_v2.0 (prediction ledger)) -- gap -38.0 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV04ETCDE-DE7` Will Alex de Minaur win at least 6.5 more games than Tomas Martin Etcheverry?: 0.02/0.93 mid 47.5%, model 10.3% (projection_v2.0 (prediction ledger)) -- gap -37.1 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04ETCDE-ETC21` Will Tomas Martin Etcheverry win the Tomas Martin Etcheverry vs Alex de Minaur match by a set score of 2-1?: 0.02/0.93 mid 47.5%, model 13.1% (projection_v2.0 (prediction ledger)) -- gap -34.4 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV04ETCDE-ETC2` Will Tomas Martin Etcheverry win at least 1.5 more games than Alex de Minaur?: 0.02/0.93 mid 47.5%, model 17.1% (projection_v2.0 (prediction ledger)) -- gap -30.4 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV04ETCDE-1-DE` Will Alex de Minaur win set 1 in the Tomas Martin Etcheverry vs Alex de Minaur match: 0.06/0.87 mid 46.5%, model 69.3% (projection_v2.0 (prediction ledger)) -- gap +22.8 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV04ETCDE-2-DE` Will Alex de Minaur win set 2 in the Tomas Martin Etcheverry vs Alex de Minaur match: 0.02/0.93 mid 47.5%, model 69.3% (projection_v2.0 (prediction ledger)) -- gap +21.8 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04ETCDE-DE20` Will Alex de Minaur win the Tomas Martin Etcheverry vs Alex de Minaur match by a set score of 2-0?: 0.01/0.59 mid 30.0%, model 48.0% (projection_v2.0 (prediction ledger)) -- gap +18.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV04ETCDE-1-ETC` Will Tomas Martin Etcheverry win set 1 in the Tomas Martin Etcheverry vs Alex de Minaur match: 0.08/0.87 mid 47.5%, model 30.7% (projection_v2.0 (prediction ledger)) -- gap -16.8 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV04ETCDE-2-ETC` Will Tomas Martin Etcheverry win set 2 in the Tomas Martin Etcheverry vs Alex de Minaur match: 0.02/0.93 mid 47.5%, model 30.7% (projection_v2.0 (prediction ledger)) -- gap -16.8 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04ETCDE-DE21` Will Alex de Minaur win the Tomas Martin Etcheverry vs Alex de Minaur match by a set score of 2-1?: 0.01/0.29 mid 15.0%, model 29.5% (projection_v2.0 (prediction ledger)) -- gap +14.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV04ETCDE-28` Over 27.5 games: 0.03/0.93 mid 48.0%, model 35.1% (projection_v2.0 (prediction ledger)) -- gap -12.9 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV04ETCDE-23` Over 22.5 games: 0.03/0.93 mid 48.0%, model 54.3% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV04ETCDE-DE4` Will Alex de Minaur win at least 3.5 more games than Tomas Martin Etcheverry?: 0.02/0.93 mid 47.5%, model 50.5% (projection_v2.0 (prediction ledger)) -- gap +3.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Arthur Fils vs Tomas Machac -- ATP Paris R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-04 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-04T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-04T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:207830:209950:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arthur Fils (`KXATPMATCH-26NOV04FILMAC-FIL`) | 0.64 / 0.65 (63667) | 64.5% | 69.3% | 79.0% | 76.0% [74.5%-77.5%] | 64.6% | -- | 64.6% | MODEL_LONE_OUTLIER | SHADOW_BET | +4.8 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Tomas Machac (`KXATPMATCH-26NOV04FILMAC-MAC`) | 0.36 / 0.37 (6470) | 36.5% | 30.7% | 21.0% | 24.0% [22.5%-25.5%] | 35.4% | -- | 35.4% | MODEL_LONE_OUTLIER | PASS | -5.8 pp | NORMAL | AGING | A / ADEQUATE | AGREES_WITH_KALSHI | VERIFIED |

* Serve evidence (points): A 4555.0, B 4090.0; serve-point win A 66.5%, B 37.6%; Elo A 2043.7, B 1918.8; model uncertainty 0.0153
* Form inputs: days since last match A 4, B 1; matches on record A 338, B 460; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.004, surface_pool_high -0.008, surface_dev_loose +0.011, surface_dev_tight -0.015
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGSPREAD-26NOV04FILMAC-MAC2` Will Tomas Machac win at least 1.5 more games than Arthur Fils?: 0.28/0.93 mid 60.5%, model 24.2% (projection_v2.0 (prediction ledger)) -- gap -36.2 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV04FILMAC-18` Over 17.5 games: 0.45/0.91 mid 68.0%, model 92.6% (projection_v2.0 (prediction ledger)) -- gap +24.6 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04FILMAC-FIL20` Will Arthur Fils win the Arthur Fils vs Tomas Machac match by a set score of 2-0?: 0.01/0.47 mid 24.0%, model 39.9% (projection_v2.0 (prediction ledger)) -- gap +15.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV04FILMAC-2-FIL` Will Arthur Fils win set 2 in the Arthur Fils vs Tomas Machac match: 0.02/0.93 mid 47.5%, model 63.1% (projection_v2.0 (prediction ledger)) -- gap +15.7 pp, HIGH_REVIEW, DATA_WARNING, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04FILMAC-FIL21` Will Arthur Fils win the Arthur Fils vs Tomas Machac match by a set score of 2-1?: 0.01/0.27 mid 14.0%, model 29.4% (projection_v2.0 (prediction ledger)) -- gap +15.4 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV04FILMAC-2-MAC` Will Tomas Machac win set 2 in the Arthur Fils vs Tomas Machac match: 0.02/0.93 mid 47.5%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap -10.7 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV04FILMAC-28` Over 27.5 games: 0.02/0.58 mid 30.0%, model 38.4% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV04FILMAC-23` Over 22.5 games: 0.49/0.51 mid 50.0%, model 58.2% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV04FILMAC-1-FIL` Will Arthur Fils win set 1 in the Arthur Fils vs Tomas Machac match: 0.60/0.62 mid 61.0%, model 63.1% (projection_v2.0 (prediction ledger)) -- gap +2.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV04FILMAC-1-MAC` Will Tomas Machac win set 1 in the Arthur Fils vs Tomas Machac match: 0.38/0.40 mid 39.0%, model 36.9% (projection_v2.0 (prediction ledger)) -- gap -2.1 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGSPREAD-26NOV04FILMAC-FIL4` Will Arthur Fils win at least 3.5 more games than Tomas Machac?: 0.43/0.45 mid 44.0%, model 42.3% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04FILMAC-MAC21` Will Tomas Machac win the Arthur Fils vs Tomas Machac match by a set score of 2-1?: 0.10/0.21 mid 15.5%, model 17.2% (projection_v2.0 (prediction ledger)) -- gap +1.6 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04FILMAC-MAC20` Will Tomas Machac win the Arthur Fils vs Tomas Machac match by a set score of 2-0?: 0.03/0.25 mid 14.0%, model 13.6% (projection_v2.0 (prediction ledger)) -- gap -0.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; ONE_SIDED_OR_NO_QUOTE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Quentin Halys vs Frances Tiafoe -- ATP Paris R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-04 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-04T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-04T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:111460:126207:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Quentin Halys (`KXATPMATCH-26NOV04HALTIA-HAL`) | 0.42 / 0.43 (1860) | 42.5% | 44.3% | 50.5% | 46.2% [43.3%-48.6%] | 42.5% | -- | 42.5% | MARKETS_AGREE | WATCH | +1.8 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |
| Frances Tiafoe (`KXATPMATCH-26NOV04HALTIA-TIA`) | 0.57 / 0.58 (2338) | 57.5% | 55.7% | 49.5% | 53.8% [51.4%-56.7%] | 57.5% | -- | 57.5% | MARKETS_AGREE | PASS | -1.8 pp | NORMAL | AGING | A / ADEQUATE | ALL_AGREE | VERIFIED |

* Serve evidence (points): A 6312.0, B 6397.0; serve-point win A 67.4%, B 31.4%; Elo A 1838.2, B 1990.7; model uncertainty 0.0262
* Form inputs: days since last match A 0, B 6; matches on record A 841, B 716; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose +0.005, surface_dev_tight -0.005
* Derivatives listed: 14 (EXACT_SET_SCORE, GAME_SPREAD, MATCH_WINNER, SET_WINNER, TOTAL_GAMES); 14 carry a model probability
  * `KXATPGTOTAL-26NOV04HALTIA-20` Over 19.5 games: 0.45/0.93 mid 69.0%, model 87.0% (projection_v2.0 (prediction ledger)) -- gap +18.0 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV04HALTIA-TIA5` Will Frances Tiafoe win at least 4.5 more games than Quentin Halys?: 0.01/0.58 mid 29.5%, model 14.0% (projection_v2.0 (prediction ledger)) -- gap -15.5 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV04HALTIA-HAL2` Will Quentin Halys win at least 1.5 more games than Frances Tiafoe?: 0.01/0.93 mid 47.0%, model 36.0% (projection_v2.0 (prediction ledger)) -- gap -11.0 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04HALTIA-TIA20` Will Frances Tiafoe win the Quentin Halys vs Frances Tiafoe match by a set score of 2-0?: 0.01/0.40 mid 20.5%, model 28.9% (projection_v2.0 (prediction ledger)) -- gap +8.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04HALTIA-TIA21` Will Frances Tiafoe win the Quentin Halys vs Frances Tiafoe match by a set score of 2-1?: 0.08/0.29 mid 18.5%, model 26.7% (projection_v2.0 (prediction ledger)) -- gap +8.2 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04HALTIA-HAL21` Will Quentin Halys win the Quentin Halys vs Frances Tiafoe match by a set score of 2-1?: 0.07/0.25 mid 16.0%, model 23.0% (projection_v2.0 (prediction ledger)) -- gap +7.0 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV04HALTIA-2-TIA` Will Frances Tiafoe win set 2 in the Quentin Halys vs Frances Tiafoe match: 0.02/0.93 mid 47.5%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap +6.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPGTOTAL-26NOV04HALTIA-25` Over 24.5 games: 0.51/0.52 mid 51.5%, model 57.3% (projection_v2.0 (prediction ledger)) -- gap +5.8 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04HALTIA-HAL20` Will Quentin Halys win the Quentin Halys vs Frances Tiafoe match by a set score of 2-0?: 0.01/0.31 mid 16.0%, model 21.3% (projection_v2.0 (prediction ledger)) -- gap +5.3 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGSPREAD-26NOV04HALTIA-TIA2` Will Frances Tiafoe win at least 1.5 more games than Quentin Halys?: 0.49/0.52 mid 50.5%, model 47.1% (projection_v2.0 (prediction ledger)) -- gap -3.4 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPGTOTAL-26NOV04HALTIA-30` Over 29.5 games: 0.04/0.77 mid 40.5%, model 37.8% (projection_v2.0 (prediction ledger)) -- gap -2.7 pp, NORMAL, OK, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV04HALTIA-1-HAL` Will Quentin Halys win set 1 in the Quentin Halys vs Frances Tiafoe match: 0.43/0.46 mid 44.5%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap +1.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV04HALTIA-1-TIA` Will Frances Tiafoe win set 1 in the Quentin Halys vs Frances Tiafoe match: 0.54/0.57 mid 55.5%, model 53.8% (projection_v2.0 (prediction ledger)) -- gap -1.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV04HALTIA-2-HAL` Will Quentin Halys win set 2 in the Quentin Halys vs Frances Tiafoe match: 0.02/0.93 mid 47.5%, model 46.2% (projection_v2.0 (prediction ledger)) -- gap -1.3 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ianin / Seleznev vs Bessonov / Kharlamov -- M15 Fergana R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04IANSELBESKHA:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bessonov / Kharlamov (`KXITFDOUBLES-26NOV04IANSELBESKHA-BESKHA`) | 0.04 / 0.93 (2) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Ianin / Seleznev (`KXITFDOUBLES-26NOV04IANSELBESKHA-IANSEL`) | 0.04 / 0.93 (2) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Daniel Khazime vs Maxim Shin -- M15 Fergana R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:149278:210535:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniel Khazime (`KXITFMATCH-26NOV04KHASHI-KHA`) | 0.51 / 0.63 (7) | 57.0% | 43.2% | 53.6% | 44.3% [40.8%-46.4%] | -- | -- | -- | -- | PASS | -13.8 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Maxim Shin (`KXITFMATCH-26NOV04KHASHI-SHI`) | 0.38 / 0.53 (7) | 45.5% | 56.8% | 46.4% | 55.7% [53.6%-59.2%] | -- | -- | -- | -- | PASS | +11.3 pp | REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 769.0, B 1523.0; serve-point win A 58.3%, B 40.4%; Elo A 1152.4, B 1229.1; model uncertainty 0.028
* Form inputs: days since last match A 267, B 190; matches on record A 62, B 86; data quality D
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.000, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Sergio Martos Gornes / Szymon Walkow vs Sadio Doumbia / David Pel -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-04T05:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-04T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04MARWALDOUPEL:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sadio Doumbia / David Pel (`KXATPDOUBLES-26NOV04MARWALDOUPEL-DOUPEL`) | 0.05 / 0.93 (2) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sergio Martos Gornes / Szymon Walkow (`KXATPDOUBLES-26NOV04MARWALDOUPEL-MARWAL`) | 0.05 / 0.93 (2) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lucas Miedler / Neil Oberleitner vs Arthur Reymond / Luca Sanchez -- ATP Paris R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-04T05:00:00+00:00 as not a valid time; NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (MASTERS_1000) · surface ? · scheduled 2026-11-04T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04MIEOBEREYSAN:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucas Miedler / Neil Oberleitner (`KXATPDOUBLES-26NOV04MIEOBEREYSAN-MIEOBE`) | 0.05 / 0.93 (2) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Arthur Reymond / Luca Sanchez (`KXATPDOUBLES-26NOV04MIEOBEREYSAN-REYSAN`) | 0.05 / 0.93 (2) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Aristarkh Safonov vs Akmal Abdullaev -- M15 Fergana R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04SAFABD:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Akmal Abdullaev (`KXITFMATCH-26NOV04SAFABD-ABD`) | 0.06 / 0.93 (2) | 49.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Aristarkh Safonov (`KXITFMATCH-26NOV04SAFABD-SAF`) | 0.07 / 0.93 (2) | 50.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Luca Van Assche vs Learner Tien -- ATP Paris R32

**START STATUS: START_UNKNOWN** -- BET BLOCKED
* Nominal schedule: 2026-11-04 13:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NOT_OBSERVED_STARTED
* Last status refresh: 2026-11-03 15:48Z
* Recommended handicap-by time: UNKNOWN

* Status notes: LIVE_TIME_IS_PLACEHOLDER: espn_atp marks 2026-11-04T05:00:00+00:00 as not a valid time; NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_RECENT_LIVE_STATUS: no live PRE reading within 30 min; NO_CREDIBLE_START_TIME

ATP (MASTERS_1000) · Hard · scheduled 2026-11-04T13:00:00Z · first ball: NOT_OBSERVED_STARTED (source COVERED) · match `ATP:209414:210530:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Learner Tien (`KXATPMATCH-26NOV04VANTIE-TIE`) | 0.68 / 0.71 (1001) | 69.5% | 63.6% | 63.1% | 65.5% [63.1%-67.4%] | -- | -- | -- | -- | PASS | -5.9 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |
| Luca Van Assche (`KXATPMATCH-26NOV04VANTIE-VAN`) | 0.27 / 0.33 (4) | 30.0% | 36.4% | 36.9% | 34.4% [32.6%-36.9%] | -- | -- | -- | -- | PASS | +6.4 pp | NORMAL | AGING | A / ADEQUATE | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 6055.0, B 5395.0; serve-point win A 58.9%, B 38.4%; Elo A 1807.2, B 1981.2; model uncertainty 0.0216
* Form inputs: days since last match A 1, B 6; matches on record A 395, B 251; data quality A
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.019, surface_pool_high -0.019, surface_dev_loose +0.000, surface_dev_tight +0.005
* Derivatives listed: 8 (EXACT_SET_SCORE, MATCH_WINNER, SET_WINNER); 8 carry a model probability
  * `KXATPEXACTMATCH-26NOV04VANTIE-VAN20` Will Luca Van Assche win the Luca Van Assche vs Learner Tien match by a set score of 2-0?: 0.01/0.94 mid 47.5%, model 16.7% (projection_v2.0 (prediction ledger)) -- gap -30.8 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04VANTIE-VAN21` Will Luca Van Assche win the Luca Van Assche vs Learner Tien match by a set score of 2-1?: 0.01/0.94 mid 47.5%, model 19.7% (projection_v2.0 (prediction ledger)) -- gap -27.8 pp, EXTREME, DATA_WARNING, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04VANTIE-TIE21` Will Learner Tien win the Luca Van Assche vs Learner Tien match by a set score of 2-1?: 0.01/0.94 mid 47.5%, model 28.6% (projection_v2.0 (prediction ledger)) -- gap -18.9 pp, HIGH_REVIEW, EXPLANATION_REQUIRED_BEFORE_BET, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPEXACTMATCH-26NOV04VANTIE-TIE20` Will Learner Tien win the Luca Van Assche vs Learner Tien match by a set score of 2-0?: 0.01/0.94 mid 47.5%, model 35.0% (projection_v2.0 (prediction ledger)) -- gap -12.5 pp, REVIEW, REVIEW_CONTEXT, quote AGING, identity VERIFIED, data ADEQUATE
  * `KXATPSETWINNER-26NOV04VANTIE-1-TIE` Will Learner Tien win set 1 in the Luca Van Assche vs Learner Tien match: 0.01/0.98 mid 49.5%, model 59.2% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV04VANTIE-2-TIE` Will Learner Tien win set 2 in the Luca Van Assche vs Learner Tien match: 0.01/0.98 mid 49.5%, model 59.2% (projection_v2.0 (prediction ledger)) -- gap +9.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV04VANTIE-1-VAN` Will Luca Van Assche win set 1 in the Luca Van Assche vs Learner Tien match: 0.01/0.94 mid 47.5%, model 40.8% (projection_v2.0 (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
  * `KXATPSETWINNER-26NOV04VANTIE-2-VAN` Will Luca Van Assche win set 2 in the Luca Van Assche vs Learner Tien match: 0.01/0.94 mid 47.5%, model 40.8% (projection_v2.0 (prediction ledger)) -- gap -6.7 pp, NORMAL, OK, quote AGING, identity AMBIGUOUS, data ADEQUATE
* Warnings: BET_BLOCKED_START_STATUS; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Cai / Wang vs An / Cao -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV04CAIWANANXCAO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| An / Cao (`KXITFWDOUBLES-26NOV04CAIWANANXCAO-ANXCAO`) | 0.05 / 0.90 (1) | 47.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cai / Wang (`KXITFWDOUBLES-26NOV04CAIWANANXCAO-CAIWAN`) | 0.05 / 0.89 (2) | 47.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Dang / You vs Kawaguchi / Sato -- W100 Incheon R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T13:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV04DANYOUKAWSAT:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dang / You (`KXITFWDOUBLES-26NOV04DANYOUKAWSAT-DANYOU`) | 0.36 / 0.68 (78) | 52.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Kawaguchi / Sato (`KXITFWDOUBLES-26NOV04DANYOUKAWSAT-KAWSAT`) | 0.20 / 0.57 (58) | 38.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; WIDE_SPREAD

## Tobia Costanzo Baragiola Mordini vs Mattia Nannelli -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-04T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:213617:213701:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tobia Costanzo Baragiola Mordini (`KXITFMATCH-26NOV04BARNAN-BAR`) | 0.47 / 0.94 (25) | 70.5% | 47.9% | 25.5% | 41.6% [37.5%-47.4%] | -- | -- | -- | -- | PASS | -22.6 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Mattia Nannelli (`KXITFMATCH-26NOV04BARNAN-NAN`) | 0.06 / 0.54 (37) | 30.0% | 52.1% | 74.5% | 58.4% [52.6%-62.5%] | -- | -- | -- | -- | PASS | +22.1 pp | HIGH_REVIEW | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1087.0, B 425.0; serve-point win A 56.8%, B 42.8%; Elo A 1181.4, B 1206.3; model uncertainty 0.0493
* Form inputs: days since last match A 204, B 253; matches on record A 26, B 9; data quality D

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV04BARNAN-NAN  (YES = Mattia Nannelli)
Model: 52%
Kalshi: 30%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.010, surface_pool_high -0.010, surface_dev_loose -0.011, surface_dev_tight +0.016
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Cem Christopher Kucukhuseyin vs Antoni Fabre -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04KUCFAB:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Antoni Fabre (`KXITFMATCH-26NOV04KUCFAB-FAB`) | 0.81 / 0.94 (10) | 87.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Cem Christopher Kucukhuseyin (`KXITFMATCH-26NOV04KUCFAB-KUC`) | 0.06 / 0.16 (11) | 11.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lieven Mietusch vs Ali Yazdani -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-04T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:212070:214093:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lieven Mietusch (`KXITFMATCH-26NOV04MIEYAZ-MIE`) | 0.06 / 0.93 (2) | 49.5% | 55.0% | 56.2% | 56.2% [55.1%-57.2%] | -- | -- | -- | -- | PASS | +5.5 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ali Yazdani (`KXITFMATCH-26NOV04MIEYAZ-YAZ`) | 0.07 / 0.93 (2) | 50.0% | 45.0% | 43.8% | 43.8% [42.8%-44.9%] | -- | -- | -- | -- | PASS | -5.0 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 57.0, B 2400.0; serve-point win A 59.4%, B 41.6%; Elo A 1283.7, B 1240.0; model uncertainty 0.0105
* Form inputs: days since last match A 442, B 218; matches on record A 1, B 70; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose +0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Vuk Radjenovic vs Egor Khotchenkov -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-04T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:210615:211366:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Egor Khotchenkov (`KXITFMATCH-26NOV04RADKHO-KHO`) | 0.06 / 0.67 (53) | 36.5% | 23.3% | 57.1% | 37.9% [37.9%-38.9%] | -- | -- | -- | -- | PASS | -13.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Vuk Radjenovic (`KXITFMATCH-26NOV04RADKHO-RAD`) | 0.37 / 0.94 (10) | 65.5% | 76.7% | 42.9% | 62.1% [61.1%-62.1%] | -- | -- | -- | -- | PASS | +11.2 pp | REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 799.0, B 33.0; serve-point win A 63.7%, B 42.0%; Elo A 1242.8, B 1155.2; model uncertainty 0.0051
* Form inputs: days since last match A 365, B 645; matches on record A 71, B 5; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.000, surface_pool_high +0.000, surface_dev_loose +0.000, surface_dev_tight +0.001
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daniil Stepanov vs Nicolo Toffanin -- M15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-04T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:211532:213905:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Daniil Stepanov (`KXITFMATCH-26NOV04STETOF-STE`) | 0.06 / 0.50 (15) | 28.0% | 33.1% | 47.3% | 45.8% [44.7%-46.8%] | -- | -- | -- | -- | PASS | +5.2 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Nicolo Toffanin (`KXITFMATCH-26NOV04STETOF-TOF`) | 0.53 / 0.94 (10) | 73.5% | 66.8% | 52.7% | 54.2% [53.2%-55.3%] | -- | -- | -- | -- | PASS | -6.7 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 210.0, B 1135.0; serve-point win A 52.8%, B 43.9%; Elo A 1158.9, B 1189.8; model uncertainty 0.0108
* Form inputs: days since last match A 190, B 225; matches on record A 4, B 38; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.011, surface_pool_high -0.000, surface_dev_loose -0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ayse Bal vs Alja Senica -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-04T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:263808:270062:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ayse Bal (`KXITFWMATCH-26NOV04BALSEN-BAL`) | 0.24 / 0.54 (76) | 39.0% | 22.6% | 40.5% | 39.4% [38.4%-40.5%] | -- | -- | -- | -- | PASS | -16.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Alja Senica (`KXITFWMATCH-26NOV04BALSEN-SEN`) | 0.41 / 0.69 (80) | 55.0% | 77.4% | 59.5% | 60.6% [59.5%-61.6%] | -- | -- | -- | -- | PASS | +22.4 pp | HIGH_REVIEW | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 53.0, B 989.0; serve-point win A 49.7%, B 44.7%; Elo A 1254.7, B 1329.2; model uncertainty 0.0103
* Form inputs: days since last match A 114, B 8; matches on record A 2, B 52; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04BALSEN-SEN  (YES = Alja Senica)
Model: 77%
Kalshi: 55%
Gap: +22 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.010, surface_pool_high +0.010, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Magdalena Hedrzak vs Yu Shan -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:220031:221795:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Magdalena Hedrzak (`KXITFWMATCH-26NOV04HEDSHA-HED`) | 0.08 / 0.92 (1) | 50.0% | 23.6% | 80.6% | 47.3% [43.6%-53.2%] | -- | -- | -- | -- | PASS | -26.4 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Yu Shan (`KXITFWMATCH-26NOV04HEDSHA-SHA`) | 0.06 / 0.91 (2) | 48.5% | 76.3% | 19.4% | 52.6% [46.8%-56.4%] | -- | -- | -- | -- | PASS | +27.9 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 243.0, B 408.0; serve-point win A 53.0%, B 41.5%; Elo A 1128.5, B 1186.3; model uncertainty 0.0476
* Form inputs: days since last match A 218, B 190; matches on record A 18, B 153; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04HEDSHA-SHA  (YES = Yu Shan)
Model: 76%
Kalshi: 48%
Gap: +28 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.011, surface_dev_loose +0.011, surface_dev_tight -0.005
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Miroslava Medvedeva vs Karla Popovic -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:210500:263948:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Miroslava Medvedeva (`KXITFWMATCH-26NOV04MEDPOP-MED`) | 0.05 / 0.93 (2) | 49.0% | 5.8% | 13.6% | 15.4% [14.2%-16.1%] | -- | -- | -- | -- | PASS | -43.2 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Karla Popovic (`KXITFWMATCH-26NOV04MEDPOP-POP`) | 0.10 / 0.93 (2) | 51.5% | 94.2% | 86.4% | 84.6% [83.9%-85.8%] | -- | -- | -- | -- | PASS | +42.7 pp | EXTREME (DATA_WARNING) | AGING | D / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 43.0, B 1204.0; serve-point win A 46.6%, B 41.6%; Elo A 1158.4, B 1454.1; model uncertainty 0.0095
* Form inputs: days since last match A 197, B 190; matches on record A 18, B 82; data quality D

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04MEDPOP-POP  (YES = Karla Popovic)
Model: 94%
Kalshi: 52%
Gap: +43 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: D (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, ASYMMETRIC_SAMPLE_SIZE, STALE_PLAYER_DATA, SURFACE_DATA_THIN, MODEL_CALIBRATION_OUTLIER, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, no_severe_asymmetry_or_justified, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.006, surface_pool_high -0.012, surface_dev_loose -0.000, surface_dev_tight -0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Andreea Prisacariu vs Selina Atay -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-04T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:214653:220297:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Selina Atay (`KXITFWMATCH-26NOV04PRIATA-ATA`) | 0.03 / 0.09 (8) | 6.0% | 7.1% | 10.1% | 10.4% [8.6%-13.3%] | -- | -- | -- | -- | PASS | +1.1 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Andreea Prisacariu (`KXITFWMATCH-26NOV04PRIATA-PRI`) | 0.85 / 0.94 (25) | 89.5% | 92.8% | 89.9% | 89.6% [86.7%-91.4%] | -- | -- | -- | -- | PASS | +3.4 pp | NORMAL | AGING | B / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2406.0, B 1670.0; serve-point win A 56.0%, B 55.0%; Elo A 1566.8, B 1205.0; model uncertainty 0.0236
* Form inputs: days since last match A 99, B 190; matches on record A 444, B 207; data quality B
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.005, surface_pool_high -0.010, surface_dev_loose +0.018, surface_dev_tight -0.015
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Daria Shadchneva vs Aya El Sayed -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:221083:263646:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Aya El Sayed (`KXITFWMATCH-26NOV04SHAELS-ELS`) | 0.44 / 0.93 (1) | 68.5% | 28.0% | 35.5% | 28.4% [26.6%-30.7%] | -- | -- | -- | -- | PASS | -40.5 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Daria Shadchneva (`KXITFWMATCH-26NOV04SHAELS-SHA`) | 0.05 / 0.59 (4) | 32.0% | 72.0% | 64.5% | 71.6% [69.3%-73.4%] | -- | -- | -- | -- | PASS | +40.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 628.0, B 698.0; serve-point win A 57.5%, B 46.9%; Elo A 1381.4, B 1200.5; model uncertainty 0.0203
* Form inputs: days since last match A 491, B 330; matches on record A 45, B 81; data quality F

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04SHAELS-SHA  (YES = Daria Shadchneva)
Model: 72%
Kalshi: 32%
Gap: +40 pp
Band: EXTREME
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.023, surface_pool_high +0.018, surface_dev_loose -0.005, surface_dev_tight -0.004
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Anja Wildgruber vs Dana Baidaulet -- W15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:222668:237455:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dana Baidaulet (`KXITFWMATCH-26NOV04WILBAI-BAI`) | 0.05 / 0.58 (4) | 31.5% | 40.4% | 52.1% | 39.5% [33.5%-47.9%] | -- | -- | -- | -- | PASS | +8.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |
| Anja Wildgruber (`KXITFWMATCH-26NOV04WILBAI-WIL`) | 0.45 / 0.94 (10) | 69.5% | 59.6% | 47.9% | 60.5% [52.1%-66.5%] | -- | -- | -- | -- | PASS | -9.9 pp | NORMAL | AGING | F / POOR | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 2380.0, B 52.0; serve-point win A 54.9%, B 46.9%; Elo A 1305.7, B 1235.5; model uncertainty 0.0721
* Form inputs: days since last match A 190, B 729; matches on record A 348, B 63; data quality F
* Surface-prior sensitivity (P(A) change): surface_pool_low -0.084, surface_pool_high +0.060, surface_dev_loose +0.000, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Ilay Yoruk vs Ada Kumru -- W15 Antalya R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 13:30Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Clay · scheduled 2026-11-04T13:30:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:215879:261964:2026-11-04`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ada Kumru (`KXITFWMATCH-26NOV04YORKUM-KUM`) | 0.47 / 0.73 (25) | 60.0% | 42.2% | 62.1% | 48.9% [37.9%-54.8%] | -- | -- | -- | -- | PASS | -17.8 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |
| Ilay Yoruk (`KXITFWMATCH-26NOV04YORKUM-YOR`) | 0.30 / 0.47 (47) | 38.5% | 57.8% | 37.9% | 51.1% [45.2%-62.1%] | -- | -- | -- | -- | PASS | +19.3 pp | HIGH_REVIEW | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | VERIFIED |

* Serve evidence (points): A 1694.0, B 1232.0; serve-point win A 53.0%, B 48.5%; Elo A 1423.6, B 1335.5; model uncertainty 0.0846
* Form inputs: days since last match A 30, B 190; matches on record A 466, B 53; data quality C

```
DISCREPANCY SANITY CHECK  KXITFWMATCH-26NOV04YORKUM-YOR  (YES = Ilay Yoruk)
Model: 58%
Kalshi: 38%
Gap: +19 pp
Band: HIGH_REVIEW
Identity: VERIFIED (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: C (LIMITED)
Reasons: WIDE_SPREAD, LOW_DATA_QUALITY, STALE_PLAYER_DATA, MODEL_HIGH_UNCERTAINTY, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE, MODEL_INTERNAL_DISAGREEMENT
Status: HIGH_REVIEW / EXPLAIN BEFORE ANY BET
```
* Surface-prior sensitivity (P(A) change): surface_pool_low +0.021, surface_pool_high -0.011, surface_dev_loose +0.011, surface_dev_tight +0.000
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Karim Bennani vs Melih Anavatan -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04BENANA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Melih Anavatan (`KXITFMATCH-26NOV04BENANA-ANA`) | 0.07 / 0.36 (3) | 21.5% | 12.2% | -- | -- [-----] | -- | -- | -- | -- | -- | -9.3 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Karim Bennani (`KXITFMATCH-26NOV04BENANA-BEN`) | 0.80 / 0.93 (5) | 86.5% | 87.8% | -- | -- [-----] | -- | -- | -- | -- | -- | +1.3 pp | NORMAL | AGING | C / LIMITED | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 65.2%, B 43.9%; Elo A 1496.5, B 1191.9; model uncertainty None
* Form inputs: days since last match A 45, B 190; matches on record A 60, B 30; data quality C
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Lorenzo Bocchi vs Igor Piasek -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04BOCPIA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lorenzo Bocchi (`KXITFMATCH-26NOV04BOCPIA-BOC`) | 0.07 / 0.93 (2) | 50.0% | 84.5% | -- | -- [-----] | -- | -- | -- | -- | -- | +34.5 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Igor Piasek (`KXITFMATCH-26NOV04BOCPIA-PIA`) | 0.06 / 0.93 (2) | 49.5% | 15.5% | -- | -- [-----] | -- | -- | -- | -- | -- | -34.0 pp | EXTREME (DATA_WARNING) | AGING | F / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 63.3%, B 44.5%; Elo A 1362.7, B 1233.0; model uncertainty None
* Form inputs: days since last match A 190, B 456; matches on record A 308, B 2; data quality F

```
DISCREPANCY SANITY CHECK  KXITFMATCH-26NOV04BOCPIA-BOC  (YES = Lorenzo Bocchi)
Model: 84%
Kalshi: 50%
Gap: +34 pp
Band: EXTREME
Identity: AMBIGUOUS (ticker orientation VERIFIED)
Quote freshness: AGING
External: NO_EXTERNAL_REFERENCE
Data quality: F (POOR)
Reasons: WIDE_SPREAD, LOW_DISPLAYED_LIQUIDITY, EVENT_MAPPING_RISK, LOW_DATA_QUALITY, THIN_PLAYER_HISTORY, STALE_PLAYER_DATA, NO_EXTERNAL_REFERENCE, START_UNVERIFIABLE
Status: DATA_WARNING / PASS UNTIL RECHECKED
Unmet before human review: identity_verified, fresh_executable_price, adequate_data_quality, external_supports_or_documented_unavailable, explains_why_market_may_be_wrong, explains_why_model_may_be_wrong, price_clears_fees_and_execution
```
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Oskari Eerola vs Kerem Yilmaz -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · Hard · scheduled 2026-11-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04EERYIL:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oskari Eerola (`KXITFMATCH-26NOV04EERYIL-EER`) | 0.08 / 0.52 (33) | 30.0% | 26.2% | -- | -- [-----] | -- | -- | -- | -- | -- | -3.8 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |
| Kerem Yilmaz (`KXITFMATCH-26NOV04EERYIL-YIL`) | 0.50 / 0.93 (3) | 71.5% | 73.8% | -- | -- [-----] | -- | -- | -- | -- | -- | +2.3 pp | NORMAL | AGING | D / POOR | NO_EXTERNAL_REFERENCE | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A 54.5%, B 40.7%; Elo A 1139.7, B 1248.5; model uncertainty None
* Form inputs: days since last match A 232, B 92; matches on record A 17, B 42; data quality D
* Warnings: FIRST_BALL_SOURCE_UNAVAILABLE; LOW_DATA_QUALITY; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Amr Elsayed vs Marwan Ehab -- M15 Sharm ElSheikh R32

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

ITF (ITF) · surface ? · scheduled 2026-11-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04ELSEHA:singles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marwan Ehab (`KXITFMATCH-26NOV04ELSEHA-EHA`) | 0.06 / 0.57 (22) | 31.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Amr Elsayed (`KXITFMATCH-26NOV04ELSEHA-ELS`) | 0.72 / 0.94 (10) | 83.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; NO_EXTERNAL_PRICE; WIDE_SPREAD
* Frozen research context: W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)

## Liu / Xiao vs Chen / Te -- M15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 14:00Z
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_UNRELIABLE_AT_THIS_LEVEL; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `ATP:26NOV04LIUXIACHETEX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chen / Te (`KXITFDOUBLES-26NOV04LIUXIACHETEX-CHETEX`) | 0.04 / 0.93 (2) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Liu / Xiao (`KXITFDOUBLES-26NOV04LIUXIACHETEX-LIUXIA`) | 0.04 / 0.93 (2) | 48.5% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Khodzhaeva / Varaksina vs Tikhonova / Yamazaki -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV04KHOVARTIKYAM:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Khodzhaeva / Varaksina (`KXITFWDOUBLES-26NOV04KHOVARTIKYAM-KHOVAR`) | 0.05 / 0.93 (2) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Tikhonova / Yamazaki (`KXITFWDOUBLES-26NOV04KHOVARTIKYAM-TIKYAM`) | 0.05 / 0.93 (2) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Li / Yang vs Yi Liu / Luo -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV04LIXYANYILLUO:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Li / Yang (`KXITFWDOUBLES-26NOV04LIXYANYILLUO-LIXYAN`) | 0.05 / 0.93 (2) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Yi Liu / Luo (`KXITFWDOUBLES-26NOV04LIXYANYILLUO-YILLUO`) | 0.05 / 0.93 (2) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Lu / Naklo vs Qu / Xi Wu -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV04LUXNAKQUXXIW:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lu / Naklo (`KXITFWDOUBLES-26NOV04LUXNAKQUXXIW-LUXNAK`) | 0.05 / 0.93 (2) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Qu / Xi Wu (`KXITFWDOUBLES-26NOV04LUXNAKQUXXIW-QUXXIW`) | 0.05 / 0.93 (2) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

## Ren / Ching Wu vs Sun / Xu -- W15 Maanshan R16

**START STATUS: START_UNKNOWN**
* Nominal schedule: 2026-11-04 14:00Z (day placeholder, not a start time)
* Current expected start: UNKNOWN
* Source: none; confidence NONE
* First ball: NO_FIRST_BALL_SOURCE
* Last status refresh: never (no live reading)
* Recommended handicap-by time: UNKNOWN

* Status notes: NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series; NO_CREDIBLE_START_TIME

DOUBLES (ITF) · surface ? · scheduled 2026-11-04T14:00:00Z · first ball: NO_FIRST_BALL_SOURCE (source NO_SOURCE) · match `WTA:26NOV04RENCHISUNXUX:doubles`

| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector | MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ren / Ching Wu (`KXITFWDOUBLES-26NOV04RENCHISUNXUX-RENCHI`) | 0.05 / 0.93 (2) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |
| Sun / Xu (`KXITFWDOUBLES-26NOV04RENCHISUNXUX-SUNXUX`) | 0.05 / 0.93 (2) | 49.0% | -- | -- | -- [-----] | -- | -- | -- | -- | -- | -- | UNPRICED | AGING | ? / UNKNOWN | INSUFFICIENT_INPUTS | AMBIGUOUS |

* **Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE** -- Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping pending a validated replacement. No model probability is shown for doubles; prices, liquidity and external markets remain for manual handicapping. Gen-1: --, Gen-2: --, fair_v1: -- (no model evidence; prices only)

* Serve evidence (points): A None, B None; serve-point win A --, B --; Elo A None, B None; model uncertainty None
* Form inputs: days since last match A None, B None; matches on record A None, B None; data quality None
* Warnings: NO_MODEL_FOR_MATCH; DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; FIRST_BALL_SOURCE_UNAVAILABLE; NOMINAL_START_IS_DAY_PLACEHOLDER; GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE; NO_EXTERNAL_PRICE; THIN_DISPLAYED_SIZE; WIDE_SPREAD

---

Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the `TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the first ball and are never edited afterwards.
